from django.shortcuts import render, redirect
from django.views import generic
from django.utils import timezone  # 日付時刻を取得するためのモジュール
from django.utils.timezone import localtime  # 日付時刻をsettings.pyのTIME_ZONE(すなわち日本時間)に合わせるためのモジュール
from django.http.response import JsonResponse

from .models import Words, UserAnswers

import random
import copy
import json
from typing import List, Tuple, Dict, Any, Union


STIMULI_NUM = 5  # 刺激語の数
QUESTIONS_NUM = 2  # 本当は 87 だが開発用に 2
STIMULI_HEADER = [f"stimulus_{i+1}" for i in range(STIMULI_NUM)]  # DB中から刺激語を探す時に使う用のヘッダー
STR_STIMULI_ORDER = [str(order+1) for order in range(STIMULI_NUM)]  # DBに保存する用の刺激語の提示順を表した文字列

RAMDOM_ORDER = False  # False ならばDBに載っている刺激語の順に提示（現在は実装予定無し）

# 質問のカテゴリに応じた質問文の辞書
with open ("data/input_sentences.json", encoding='utf-8') as f:
    Q_SENTENCES = json.load(f)

class IndexView(generic.TemplateView):

    template_name = "index.html"

    def get(self, request, *args, **kwargs):

        if not 'status' in request.session:
            request.session['status'] = 1  # 通常状態として status に 2^0(1) を加算

        return super().get(request, **kwargs)


class GamingView(generic.TemplateView):

    template_name = "gaming.html"


    # gaming.htmlに遷移されたら行われるGETメソッド
    def get(self, request, *args, **kwargs):

        # ログインしていない場合タイトル画面へリダイレクト
        if (not request.user.is_authenticated) or (not 'status' in request.session):
            return redirect('/')

        context = {}

        # index.htmlからgaming.htmlに遷移した時
        if request.session['status'] == 1:

            print("Game Start!")
            request.session['status'] = 3  # ゲーム中なら status に 2^1(2) を加算

            #　ユーザーのゲーム履歴がDB上にない or 最後のセッションですべての質問を解答し終えている場合、新たにゲームを始める
            if UserAnswers.objects.filter(user=request.user).exists() == False or \
                UserAnswers.objects.filter(user=request.user).latest('id').user_answer != None:

                # ゲームの回を識別するための識別IDを作成
                start_datetime = localtime(timezone.now())  # 開始の日付時刻を記憶
                request.session['session_id'] = start_datetime.strftime("%Y%m%d%H%M%S")  # 同ユーザーの最新のゲーム(セッション)ID

                left_questions = QUESTIONS_NUM
                qid = QUESTIONS_NUM - left_questions + 1  # ユーザーが答える質問のID

                # データベースに最初の質問IDを登録
                UserAnswers.objects.create(
                    user=request.user,
                    session_id=request.session['session_id'],
                    qid=qid,
                    q_order = ''.join(STR_STIMULI_ORDER)  # ユーザーに提示する刺激語の順序
                )

            # 前回のセッションでユーザーが途中の質問までしか解答してない場合、途中の質問から答える
            else:
                latest_row = UserAnswers.objects.filter(user=request.user).latest('id')
                request.session['session_id'] = latest_row.session_id
                qid = latest_row.qid
                left_questions = QUESTIONS_NUM - qid + 1

        # ゲーム中に誤ってリロード等して再度GamingViewが実行された場合
        else:
            qid = UserAnswers.objects.filter(user=request.user).last().qid
            left_questions = QUESTIONS_NUM - qid + 1

        context['left_questions'] = left_questions  # ユーザーが答えなければいけない質問の残数
        context['stimuli']: List = [
            list(Words.objects.filter(qid=qid).values_list(header, flat=True))[0] for header in STIMULI_HEADER
        ]
        q_sentence = Q_SENTENCES[Words.objects.filter(qid=qid).values('category')[0]['category']]  # qidのカテゴリに応じた質問文を用意
        context['q_sentence'] = q_sentence[-1]  # ユーザーに提示する質問文

        return render(request, self.template_name, context)


    # 解答ボタンを押したら行われるPOSTメソッド
    def post(self, request, *args, **kwargs):

        context = {}
        results = UserAnswers.objects.filter(user=request.user).last()  # テーブルの最後のクエリを抽出

        results.time_ms = request.POST.get('time')  # 解答にかかった時間

        # fetchで送信されるユーザーの解答をモデルに保存
        user_answer = request.POST.get('user-answer')  # 解答フォームから解答を受け取る
        # print(f"'{user_answer}'と解答されました")
        results.user_answer = user_answer  # ユーザーの解答を記録

        # fetchで送信されるユーザーが選択した刺激語の順序をモデルに保存
        u_order = request.POST.get('u-order')  # ユーザーが選択した刺激語の順序を受け取る
        # print(f"ユーザーが選択した順序は {u_order} です")
        results.u_order = u_order

        results.save()  # 結果を保存
        left_questions = int(request.POST.get('left-questions'))
        left_questions -= 1
        context['left_questions'] = left_questions  # ユーザーが答えなければいけない質問の残数

        # 質問がなくなった場合
        if left_questions == 0:
            print("ゲーム終了！")
            # return redirect('/results/')  # 本当はこのようにサーバー側で遷移させたかったがうまくいかんのでjsで制御
            request.session['status'] = 1  # ゲーム中ではないので 2^1(2) を減算
            return JsonResponse(context)

        # 質問がまだある場合
        else:
            # print(f"残り{left_questions}問です")
            qid = QUESTIONS_NUM - left_questions + 1  # ユーザーが答える質問のID

            # 次の質問を作る
            UserAnswers.objects.create(
                user=request.user,
                session_id=request.session['session_id'],
                qid=qid,
                q_order = ''.join(STR_STIMULI_ORDER)  # ユーザーに提示する刺激語の順序
            )

            # context['stimuli']: Dict = {
            #     header: list(Words.objects.filter(qid=qid).values_list(header, flat=True))[0] for header in STIMULI_HEADER
            # }  # qidに該当する刺激後を抽出する
            context['stimuli']: List = [
                list(Words.objects.filter(qid=qid).values_list(header, flat=True))[0] for header in STIMULI_HEADER
            ]
            q_sentence = Q_SENTENCES[Words.objects.filter(qid=qid).values('category')[0]['category']]  # qidのカテゴリに応じた質問文を用意
            context['q_sentence'] = q_sentence[-1]  # ユーザーに提示する質問文

            return JsonResponse(context)


class ResultsView(generic.TemplateView):

    template_name = "results.html"

    def get(self, request, *args, **kwargs):

        # ログインしていない場合タイトル画面へリダイレクト
        if (not request.user.is_authenticated) or (not 'status' in request.session):
            return redirect('/')

        request.session['status'] = 1  # ゲーム中ではないので 2^1(2) を減算
        context = {}
        context["results"] = list(
            UserAnswers.objects.filter(user=request.user, session_id=request.session['session_id']).values('qid', 'user_answer')
        )  # ログインユーザーの今回の結果をモデルから取得しリストにする

        # ユーザーに提示した質問文を作成
        for result in context["results"]:
            stimuli = [
                list(Words.objects.filter(qid=result["qid"]).values_list(header, flat=True))[0] for header in STIMULI_HEADER
            ]  # qid（queston id）に対応する刺激語を取得
            q_sentence = Q_SENTENCES[Words.objects.filter(qid=result["qid"]).values('category')[0]['category']]  # qidに対応する質問文を取得
            q_sentence = "、".join(stimuli) + q_sentence[-1]  # 刺激語と質問文を連結
            result["q_sentence"] = q_sentence  # レスポンスに格納
        # print(context)

        return self.render_to_response(context)

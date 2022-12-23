from django.shortcuts import render, redirect
from django.views import generic
from django.utils import timezone  # 日付時刻を取得するためのモジュール
from django.utils.timezone import localtime  # 日付時刻をsettings.pyのTIME_ZONE(すなわち日本時間)に合わせるためのモジュール
from django.http.response import JsonResponse

from .models import Words, UserAnswers

import random
import copy


STIMULI_NUM = 5  # 刺激語の数
STIMULI_HEADER = [f"stimulus_{i+1}" for i in range(STIMULI_NUM)]
STIMULI_ORDER = [i for i in range(STIMULI_NUM)]
RAMDOM_ORDER = False  # False ならばDBに載っている刺激語の順に提示

class IndexView(generic.TemplateView):

    template_name = "index.html"

    def get(self, request, *args, **kwargs):

        # ログインしてから初めてタイトル画面を訪れた場合
        if not 'visited' in request.session:
            print("Hello!")
            request.session['visited'] = True

        request.session['started'] = False  # ゲームがスタートしたらTrueにする
        request.session['qid_list'] = [1, 2, 4]  # 解答しなければいけない質問(qid)のリスト(仮)

        # ランダムに刺激語を提示する場合
        if RAMDOM_ORDER:
            stimuli_order = copy.copy(STIMULI_ORDER)
            request.session['stimuli_order'] = random.shuffle(stimuli_order)
            stimuli_header = copy.copy(STIMULI_HEADER)
            request.session['stimuli_header'] = [stimuli_header[i] for i in range(stimuli_order)]

        else:
            request.session['stimuli_order'] = copy.copy(STIMULI_ORDER)
            request.session['stimuli_header'] = copy.copy(STIMULI_HEADER)

        str_stimuli_order = [str(order+1) for order in request.session['stimuli_order']]
        request.session['q_order'] = ''.join(str_stimuli_order)

        return super().get(request, **kwargs)


class GamingView(generic.TemplateView):

    template_name = "gaming.html"


    # gaming.htmlに遷移されたら行われるGETメソッド
    def get(self, request, *args, **kwargs):

        context = {}

        # 1問目
        if request.session['started'] == False:

            print("Game Start!")
            start_datetime = localtime(timezone.now())  # 開始の日付時刻を記憶
            request.session['started'] = True  # ゲーム中ならTrue
            request.session['session_id'] = start_datetime.strftime("%Y%m%d%H%M%S")  # 同ユーザーの異なるゲーム(セッション)を識別
            qid = request.session['qid_list'].pop(0)  # qid_listからqidをpopする. このリストが空になったらゲーム終了.

            # データベースに最初の質問IDを登録
            UserAnswers.objects.create(
                user=request.user,
                datetime=start_datetime,
                session_id=request.session['session_id'],
                qid=qid,
                q_order = request.session['q_order']
            )

        context['stimuli'] = {
            header: list(Words.objects.filter(qid=qid).values_list(header, flat=True))[0] for header in request.session['stimuli_header']
        }  # qidに該当する刺激後を抽出する
        print(context)
        context['status_message'] = "スタート!"

        return render(request, self.template_name, context)


    # 解答ボタンを押したら行われるPOSTメソッド
    def post(self, request, *args, **kwargs):

        context = {}
        results = UserAnswers.objects.filter(user=request.user).last()  # テーブルの最後のクエリを抽出

        # fetchで送信されるユーザーの解答をモデルに保存
        user_answer = request.POST.get('user-answer')  # 解答フォームから解答を受け取る
        print(f"'{user_answer}'と解答されました")
        results.user_answer = user_answer  # ユーザーの解答を記録

        # fetchで送信されるユーザーが選択した刺激語の順序をモデルに保存
        u_order = request.POST.get('u-order')  # ユーザーが選択した刺激語の順序を受け取る
        print(f"ユーザーが選択した順序は {u_order} です")
        results.u_order = u_order

        results.save()  # 結果を保存

        # 質問がなくなった場合
        if len(request.session['qid_list']) == 0:
            print("ゲーム終了！")
            return redirect('/results/')

        # 質問がまだある場合
        else:

            print(f"残り{len(request.session['qid_list'])}問です")
            qid = request.session['qid_list'].pop(0)  # qid_listからqidをpopする. このリストが空になったらゲーム終了.

            # 次の質問を作る
            UserAnswers.objects.create(
                user=request.user,
                datetime=localtime(timezone.now()),
                session_id=request.session['session_id'],
                qid=qid,
                q_order = request.session['q_order']
            )

            context['stimuli'] = {
                header: list(Words.objects.filter(qid=qid).values_list(header, flat=True))[0] for header in request.session['stimuli_header']
            }  # qidに該当する刺激後を抽出する
            print(context)

        return JsonResponse(context)


class ResultsView(generic.TemplateView):

    template_name = "results.html"

    def get(self, request, *args, **kwargs):

        request.session['started'] = False

        return super().get(request, **kwargs)


    # def post(self, request, *args, **kwargs):

    #     request.session['started'] = False

    #     return super().get(request, **kwargs)

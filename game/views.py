from django.shortcuts import render
from django.views import generic
from django.utils import timezone  # 日付時刻を取得するためのモジュール
from django.utils.timezone import localtime  # 日付時刻をsettings.pyのTIME_ZONE(すなわち日本時間)に合わせるためのモジュール
from django.http.response import JsonResponse

from .models import Words, UserAnswers

STIMULI_NUM = 5
STIMULI_HEADER = [f"stimulus_{i+1}" for i in range(STIMULI_NUM)]
class IndexView(generic.TemplateView):

    template_name = "index.html"

    def get(self, request, *args, **kwargs):

        # 1回目にタイトル画面を訪れた場合
        if not 'visited' in request.session:
            print("Hello!")
            request.session['visited'] = True

        request.session['started'] = False  # ゲームがスタートしたらTrueにする
        request.session['qid_list'] = [1, 2, 4]  # 解答しなければいけない質問(qid)のリスト(仮)
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
            print(f"qid: {qid}")

            # データベースに最初の質問IDを登録
            UserAnswers.objects.create(
                user=request.user,
                datetime=start_datetime,
                session_id=request.session['session_id'],
                qid=qid
            )

        context['stimuli'] = {header: list(Words.objects.filter(qid=qid).values_list(header, flat=True))[0] for header in STIMULI_HEADER}  # qidに該当する刺激後を抽出する
        print(context)
        context['status_message'] = "スタート!"

        return render(request, self.template_name, context)


class ResultsView(generic.TemplateView):
    template_name = "results.html"

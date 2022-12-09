from django.shortcuts import render
from django.views import generic


class IndexView(generic.TemplateView):

    template_name = "index.html"

    def get(self, request, *args, **kwargs):

        # 1回目にタイトル画面を訪れた場合
        if not 'visited' in request.session:
            print("Hello!")
            request.session['visited'] = True

        request.session['started'] = False  # ゲームがスタートしたらTrueにする
        request.session['qid_list'] = [1, 2, 4]  # 解答しなければいけない質問(qid)のリスト
        return super().get(request, **kwargs)


class GamingView(generic.TemplateView):
    template_name = "gaming.html"


class ResultsView(generic.TemplateView):
    template_name = "results.html"

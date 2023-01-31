import csv
import datetime
import os
from typing import Any, Optional

from django.conf import settings
from django.core.management.base import BaseCommand

from ...models import UserAnswers


class Command(BaseCommand):
    help = "Backup UserAnswers data"

    def handle(self, *args: Any, **options: Any) -> Optional[str]:
        # 実行時のYYYYMMDDを取得
        date = datetime.date.today().strftime("%Y%m%d")

        # 保存ファイルの相対パス
        file_path = settings.BACKUP_PATH + 'answers_' + date + '.csv'

        # 保存ディレクトリが存在しなければ作成
        os.makedirs(settings.BACKUP_PATH, exist_ok=True)

        # バックアップファイルの作成
        with open(file_path, 'w') as file:
            writer = csv.writer(file)

            # ヘッダーの書き込み
            header = [field.name for field in UserAnswers._meta.fields]
            writer.writerow(header)

            # UserAnswersテーブルの全データ取得
            results = UserAnswers.objects.all()

            # データ部分の書き込み
            for result in results:
                writer.writerow([
                    str(result.id),
                    str(result.user_id),
                    str(result.datetime),
                    result.session_id,
                    str(result.qid),
                    result.user_answer,
                    result.q_order,
                    result.u_order,
                ])

            # 保存ディレクトリのファイルリストを取得
            files = os.listdir(settings.BACKUP_PATH)
            #ファイルが設定数以上あったら一番古いファイルを削除
            if len(files) >= settings.NUM_SAVED_BACKUP:
                files.sort()
                os.remove(settings.BACKUP_PATH + files[0])

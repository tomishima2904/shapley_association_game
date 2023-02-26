import csv, shutil
import sys

filename = './data/keywords_fit2022.csv'
base_filename = './data/base.sql'  # 元となるsqlファイル
output_filename = './data/words_data.sql'  # DBに読み込ませるsqlファイル

shutil.copyfile(base_filename, output_filename)  # baseをコピーして追記

total_row = sum([1 for _ in open(filename)])

with open(filename, encoding='utf-8-sig', newline='') as rf:
    csvreader = csv.reader(rf)
    with open(output_filename, 'a') as wf:
        print("", file=wf)
        for i, row in enumerate(csvreader):  # csvを1行ずつ読み込む
            if not i == total_row - 1 :
                print(f"{tuple(row)},", file=wf)
            else:
                print(f"{tuple(row)};", file=wf)
print("Successfully Output")

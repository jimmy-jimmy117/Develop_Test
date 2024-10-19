import pandas as pd

# 入力CSVファイルの読み込み
input_file = "input.csv"  # 実際の入力ファイル名を指定
data = pd.read_csv(input_file, header=None, names=["名前", "教科", "点数"])

# 生徒ごとの集計
students = data.groupby("名前").agg(list).reset_index()


# 通知簿の計算
def calculate_report(student):
    subjects = {1: "国語", 2: "数学", 3: "理科", 4: "社会", 5: "英語"}
    report = []

    for subject in range(1, 6):
        scores = [
            score
            for (subj, score) in zip(student["教科"], student["点数"])
            if subj == subject
        ]
        average = sum(scores) / len(scores) if scores else 0
        average = round(average, 1)

        report.append([subjects[subject], average])

    return pd.DataFrame(report, columns=["教科", "平均点"])


# 各生徒の通知簿を作成
reports = []
for index, student in students.iterrows():
    report_df = calculate_report(student)
    reports.append(report_df)

# 生徒ごとの成績と判定を追加
for idx, report in enumerate(reports):
    total_average = report["平均点"].mean()
    rank = sorted([r["平均点"].mean() for r in reports]).index(total_average) + 1

    # 成績の決定
    if rank == 1:
        grade = "A"
    elif 2 <= rank <= 3:
        grade = "B"
    elif 4 <= rank <= 7:
        grade = "C"
    elif 8 <= rank <= 9:
        grade = "D"
    else:
        grade = "E"

    # 判定の決定
    scores = [score for (_, score) in zip(student["教科"], student["点数"])]
    if sum(score <= 30 for score in scores) >= 3:
        judgment = "再テスト"
    elif any(score < 10 for score in scores):
        judgment = "不合格"
    else:
        judgment = (
            "合格"
            if grade in ["A", "B", "C"]
            else "再テスト" if grade == "D" else "不合格"
        )

    # 追加情報を報告書に追加
    report["順位"] = rank
    report["成績"] = grade
    report["判定"] = judgment

# 通知簿CSVの出力
for index, report in enumerate(reports):
    filename = f"生徒{index + 1}.csv"
    report.to_csv(filename, index=False, encoding="utf-8-sig")

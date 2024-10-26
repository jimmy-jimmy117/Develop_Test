import csv
import os


def make_judge(grade, points):
    # 判定基準
    # 成績のバリデーション
    if grade not in ["A", "B", "C", "D", "E"]:
        raise ValueError(
            "gradeは'A', 'B', 'C', 'D', 'E'のいずれかでなければなりません。"
        )

    # 点数のバリデーション
    if (
        not isinstance(points, list)
        or len(points) != 10
        or not all(isinstance(score, int) and 0 <= score <= 100 for score in points)
    ):
        raise ValueError(
            "pointsは整数値0～100の数値が10個のリストでなければなりません。"
        )
    if any(score < 10 for score in points):
        return 3  # 不合格
    if sum(1 for score in points if score <= 30) >= 3:
        return 2  # 再テスト
    if grade in ["A", "B", "C"]:
        return 1  # 合格
    elif grade == "D":
        return 2  # 再テスト
    else:  # E
        return 3  # 不合格


def create_report(input_file):
    with open(input_file, "r", encoding="utf-8") as infile:
        reader = csv.DictReader(infile)
        results = []

        for row in reader:
            scores = [int(row[f"教科{i}"]) for i in range(1, 6)]
            subjects = ["国語", "数学", "理科", "社会", "英語"]
            average_scores = [sum(scores[i::5]) / 10 for i in range(5)]
            average_scores = [round(avg, 1) for avg in average_scores]

            for i, avg in enumerate(average_scores):
                # 成績の計算
                if avg >= 90:
                    grade = "A"
                elif avg >= 80:
                    grade = "B"
                elif avg >= 70:
                    grade = "C"
                elif avg >= 60:
                    grade = "D"
                else:
                    grade = "E"

                # 順位の決定
                sorted_averages = sorted(average_scores, reverse=True)
                rank = sorted_averages.index(avg) + 1

                # 判定の取得
                judgment = make_judge(grade, scores[i * 10 : (i + 1) * 10])

                results.append(
                    {
                        "教科": subjects[i],
                        "平均点": avg,
                        "順位": rank,
                        "成績": grade,
                        "判定": judgment,
                    }
                )

            # 出力CSVファイルの作成
            output_file = f'生徒1{row["ID"]}.csv'  # IDをファイル名に使用
            with open(output_file, "w", newline="", encoding="utf-8") as outfile:
                fieldnames = ["教科", "平均点", "順位", "成績", "判定"]
                writer = csv.DictWriter(outfile, fieldnames=fieldnames)
                writer.writeheader()
                writer.writerows(results)


# 使用例
if __name__ == "__main__":
    input_file = "input.csv"  # ここに入力CSVのパスを指定
    create_report(input_file)

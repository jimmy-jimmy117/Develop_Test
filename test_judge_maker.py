from judge_maker import make_judge  # テストする関数をインポート


def test_make_judge_no1():
    """マトリックスNo1 ←テストを行うマトリックスの番号
    10点より下の点数がある場合 ←テストの内容
    """
    result = make_judge(
        "A", [9, 100, 100, 100, 100, 100, 100, 100, 100, 100]
    )  # テスト関数の呼び出し
    assert result == 3  # assertを使用して結果が正しいことを確認する

    result = make_judge("B", [23, 19, 13, 60, 50, 70, 60, 80, 90, 98])
    assert result == 2

    result = make_judge("B", [25, 80, 60, 70, 90, 95, 70, 80, 90, 80])
    assert result == 1

    result = make_judge("D", [19, 16, 50, 60, 65, 70, 50, 40, 50, 60])
    assert result == 2

    result = make_judge("E", [14, 17, 40, 70, 40, 50, 50, 60, 35, 50])
    assert result == 3

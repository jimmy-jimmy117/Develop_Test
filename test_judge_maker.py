
from judge_maker import make_judge # テストする関数をインポート

def test_make_judge_no1():
    """マトリックスNo1 ←テストを行うマトリックスの番号
    10点より下の点数がある場合 ←テストの内容
    """
    result = make_judge('A', [9, 100, 100, 100, 100,
                        100, 100, 100, 100, 100]) # テスト関数の呼び出し
    assert result == 3 # assertを使用して結果が正しいことを確認する

"""
データを入力してください(スペース区切り) > 1 1 2 3 5 8 13 21
合計値: 54
最大値: 21
最小値: 1
平均値: 6

入力は「スペース区切り」
    スペースは分解して配列にする　= 一つ一つに分ける
最大値を求める
    すべての値に対し大きい　一つ一つの数字に対し「総当たり」

"""

date = [int(i) for i in input('データを入力してください(スペース区切り) > ').split()]


# 合計値: 54
def date_sum1():
    date_sum2 = 0
    for i in date:
        date_sum2 += i
    return date_sum2


print(f"合計値: {date_sum1()}")

# 最大値: 21
""" #自分で作成
def date_max():
    count = 1
    dummy = 0
    for i in date:
        if count == 1:
            dummy = int(i)
        else:
            if dummy < int(i):
                dummy = int(i)

        count += 1

    return dummy


print(f"最大値: {date_max()}")


# def date_max():
# date_max2 = 0
"""
# 先生作成
numbers_str = "1 1 2 3 5 8 13 21"
numbers = numbers_str.split(" ")

max = 0  # 0で初期化して関数を作成
# もしくは↓　　最大や最小を求めるときはリストの１番最初を関数に定義付けしちゃう
# max = int(numbers[0])

for numbers in numbers:
    # maxと比較して大きかったら↓
    if int(numbers) > max:
        # 入れ替えてしまう↓
        max = int(numbers)
print(max)


# 最小値: 1
def date_min():
    count = 1
    dummy = 0
    for i in date:
        if count == 1:
            dummy = int(i)
        else:
            if dummy > int(i):
                dummy = int(i)

        count += 1

    return dummy


print(f"最小値: {date_min()}")


# 平均値: 6
def date_min():
    count = 1
    dummy = 0
    for i in date:
        dummy += int(i)
        count += 1
    return dummy / count


print(f"平均値: {date_min()}")

"""
データを入力してください(スペース区切り) > 1 1 2 3 5 8 13 21
合計値: 54
最大値: 21
最小値: 1
平均値: 6
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

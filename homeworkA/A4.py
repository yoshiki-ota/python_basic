member = ["Bob", "Tom", "Ken"]
# print(member[0]) #自分
# print(member[1])   #自分
# print(member[:2])  #他回答
print('\n'.join(member for member in member if member == 'Bob' or member == 'Tom'))  # 他回答
print(member[0], member[1])

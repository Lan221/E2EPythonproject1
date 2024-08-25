# 导入random模块,生成1-100间所有整数的随机列表(列表中的数字不重复,长度为100)
import random
data_list = []

while len(data_list) <100:
    data = random.randint(1,100)
    if data not in data_list:
        data_list.append(data)

print(data_list)

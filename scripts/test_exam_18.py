
# 通过循环创建十个文件，命名为1.txt，2.txt，3.txt....
# 拓展：将文件名修改为：副本1.txt，副本2.txt，副本3.txt...
# 提示：使用Python的os模块中的rename()函数进行重命名，
# 用法：
# import os
# os.rename(旧的文件名, 新的文件名)  # 旧的文件名必须是已经存在的文件
import os

for i in range (1,11):
    with open(f'{i}.txt','w') as f:
        f.write(f'this is file{i}')
for i in range (1,11):
    os.rename(f'{i}.txt',f'copy{i}.txt')

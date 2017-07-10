import os

#每次修改这个目录
d=r'D:\友高工作\发布内容要求\城堡\14'


lst = os.listdir(d)
n = len(lst)
for a in lst:
    os.rename(d+"\\"+a, d+"\\"+str(lst.index(a)+1)+".JPG")
print("ok")

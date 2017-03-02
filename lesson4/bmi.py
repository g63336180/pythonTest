#!/usr/local/bin/python3

tizhong = input("请输入您的体重:")
shengao = input("请输入您的身高:")
tizhong = float(tizhong)
shengao = float(shengao)
bmi = tizhong / (shengao * shengao)

print(bmi)
if bmi < 18.5:
    print("非常苗条")
elif bmi >= 18.5 and bmi < 25:
    print("完美身材")
elif bmi >= 25 and bmi <28:
    print("身材还可以啦")
elif bmi >=28 and bmi < 32:
    print("你该减肥啦")
else:
    print("你这体重每天还好意思吃饭？")
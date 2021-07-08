#練習:計算長方形週長和面積
def cal(x,y):
    ar = x*y
    c = (x+y)*2
    return ar,c

num1 = int(input("num1 = "))
num2 = int(input("num2 = "))
col , area = cal(num1,num2)
print("周長 = ",area)
print("面積 = ",col)
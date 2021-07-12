# 練習:運用迭代做數學運算
"""
設計prod()函數,傳入含數字的iterable ,計算所有元素的乘積
-然後他開發階乘函數factorial()!
"""

def prod(itr):
    it = iter(itr)
    ret = 1
    while True:
        try:
            ret = ret * next(it)
        except:
            break
    return ret
n = int(input("n = "))
range1 = range(1,n+1)
ans = prod(range1)
print (ans)

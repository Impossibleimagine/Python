# 練習: 低於 500 的數字做過濾
"""
請問小於 500 且同時是 7 和 9 的倍數，列出並
計算這樣的自然數總和
"""

list1 = range(1,500+1)
list2 = [num for num in list1 if num%7==0 and num%9==0]

print (list2)
print (sum(list2))
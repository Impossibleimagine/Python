# 練習:處理低於 1000 元的消費

"""
消費資料: [30, 45, 1024, 2500, 699, 126]
– 計算低於 1000 元的消費總和以及平均
"""
list1 = [30, 45, 1024, 2500, 699, 126]
list2 = [price for price in list1 if price<1000]
sum1 = sum(list2)
avg1 = sum1/len(list2)

print (sum1)
print (avg1)
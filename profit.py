# 練習: 計算複利

"""
假設最初存簿本金10萬，年複利1,234%，
請計算出第1到第20年的期末(年尾)的存簿金額
"""

money = 100000
rate = 1.01234
list1 = [(i,(money*(rate**i))) for i in range (1,20+1)]

for it in list1:
    print(it)
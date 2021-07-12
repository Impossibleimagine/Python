# 練習: 串列內容並排
"""
你手中有下列資料
names = ['Amy', 'Bob', 'Cathy']
scores = [70, 92, 85]
請用上列串列做以下的輸出
0 Amy 70
1 Bob 92
2 Cathy 85
"""
names = ['Amy', 'Bob', 'Cathy']
scores = [70, 92, 85]
list1 = list(enumerate(zip(names,scores)))
for i in list1:
    print (i[0],i[1][0],i[1][1])
#for i in list1:
#    print (i)
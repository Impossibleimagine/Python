#練習:調整成績
"""
建立一個成績串列 scores ,資料內容是 [10, 40, 96, 77]
建立一個自訂函數,可以傳入成績串列 scores ,每個分
數都加上 20 分計算並回傳成績串列,但滿分最多 100
印出調整完的成績串列
"""

def change_score(scores):
    index = 0
    for origin_score in scores:
        scores[index] = origin_score + 20
        if scores[index] > 100 :
            scores[index] = 100
        index += 1
scores = [10,40,96,77]
change_score(scores)
print(scores)
# 雙重串列生成式: 九九乘法表

# 一般作法

result = []
for x in range(1,9+1):
    for y in range(1,9+1):
        result.append(str(x) + ' * ' + str(y) + ' = ' + str(x*y))

for i in result:
    print (i)

# 串列生成式

result = [str(i) + ' * ' + str(j) + ' = ' + str(i*j) \
for i in range (1,9+1) \
for j in range(1,9+1)]

for num in result:
    print(num)
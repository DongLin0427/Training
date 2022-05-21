#Today is 21Mar2022
#有序可變動列表 List
grades=[12,60,15,70,90]
print(grades[0])

grade=[12,60,15,70,90]
grade[0]=55             #把 55 放到列表中第一個位置
print(grade)
length=len(grade)       #len: 取得列表長度
print(length)

#有序不可變動列表 Tuple
data=(3,4,5)
#data[0]=5     #錯誤；Tuple的資料不可變動
print(data)

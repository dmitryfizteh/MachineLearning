import pandas
from scipy.stats.stats import pearsonr

print("Неделя №1. Задание №1")
data = pandas.read_csv('./Data/titanic.csv', index_col='PassengerId')

print("\nРешение задачи №1")
a1 = data['Sex'].value_counts()
#print(a1)
print("Ответ: %d %d" % (a1['male'],a1['female']))
f = open('./Answers/1.txt', 'w')
f.write("%d %d" % (a1['male'],a1['female']))
f.close()

print("\nРешение задачи №2")
a2 = data['Survived'].value_counts()
#print(a2)
#print("%d погибло, %d выжило" % (a2[0],a2[1]))
print("Ответ: %.2f" % (round(a2[1]/(a2[0]+a2[1])*100,2)))
f = open('./Answers/2.txt', 'w')
f.write("%.2f" % (round(a2[1]/(a2[0]+a2[1])*100,2)))
f.close()

print("\nРешение задачи №3")
a3 = data['Pclass'].value_counts()
#print(a3)
print("Ответ: %.2f" % (round(a3[1]/(a3[1]+a3[2]+a3[3])*100,2)))
f = open('./Answers/3.txt', 'w')
f.write("%.2f" % (round(a3[1]/(a3[1]+a3[2]+a3[3])*100,2)))
f.close()

print("\nРешение задачи №4")
a4_1 = (data['Age'].dropna()).mean()
a4_2 = (data['Age'].dropna()).median()
print("Ответ: %0.2f %0.2f" % (a4_1, a4_2))
f = open('./Answers/4.txt', 'w')
f.write("%0.2f %0.2f" % (a4_1, a4_2))
f.close()

print("\nРешение задачи №5")
a5 = pearsonr(data['SibSp'], data['Parch'])
#print('Коэффициент корреляции r= %0.2f, уровень значимости p = %0.3f.' % a5)
print("Ответ: %0.2f" % a5[0])
f = open('./Answers/5.txt', 'w')
f.write("%0.2f" % a5[0])
f.close()

print("\nРешение задачи №6")
a6 = data[data['Sex'] == "female"]
a6 = a6['Name']

names = list()
for (key,value) in enumerate(a6):
    value = value.replace("Mrs. ","")
    value = value.replace("Miss. ","")
    value = value.replace("(","")
    value = value.replace(")","")
    value = value.replace('"','')
    value = value.split(", ")
    names_i = value[0]
    names.append(value[0])
    for name in value[1].split(" "):
        names.append(name)

# Функция поиска самого частого элемента в массиве
def Freq2(b):
  d = {}
  m, i = 0, 0 # Максимальная частота и индекс в словаре
  for x in b: # Пробегаем в цикле исходный массив
    d[x] = d[x] + 1 if x in d else 1 # Если ключ уже есть, прибавляем 1, если нет, записываем 1
    if d[x] > m:
      m, i = d[x], x # Запоминаем максимум и его индекс
  #return {i:m}
  return i

print("Ответ: %s" % (Freq2(names)))
f = open('./Answers/6.txt', 'w')
f.write("%s" % (Freq2(names)))
f.close()


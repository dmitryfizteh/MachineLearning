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
'''
data = data['Age'].dropna()
data = data.astype(int)
print(data)
'''
a4_1 = (data['Age'].dropna()).mean()
a4_2 = (data['Age'].dropna()).median()
print("Ответ: %d %d" % (a4_1, a4_2))
f = open('./Answers/4.txt', 'w')
f.write("%d %d" % (a4_1, a4_2))
f.close()

print("\nРешение задачи №5")
a5 = pearsonr(data['SibSp'], data['Parch'])
#print('Коэффициент корреляции r= %0.2f, уровень значимости p = %0.3f.' % a5)
print("Ответ: %0.2f" % a5[0])
f = open('./Answers/5.txt', 'w')
f.write("%0.2f" % a5[0])
f.close()

print("\nРешение задачи №6")
#print(data)
print(data[data['Sex'] == "female"])



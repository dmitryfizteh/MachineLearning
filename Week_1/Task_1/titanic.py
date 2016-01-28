import pandas
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



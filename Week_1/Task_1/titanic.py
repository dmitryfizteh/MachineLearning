import pandas
print("Неделя №1. Задание №1")

data = pandas.read_csv('./Data/titanic.csv', index_col='PassengerId')

print("\nРешение задачи №1")

a1 = data['Sex'].value_counts()
#print(a1)
print("Ответ: %d %d" % (a1['male'],a1['female']))

print("\nРешение задачи №2")

a2 = data['Survived'].value_counts()
#print(a2)
#print("%d погибло, %d выжило" % (a2[0],a2[1]))
print("Ответ: %d" % (round(a2[1]/(a2[0]+a2[1])*100)))

print("\nРешение задачи №3")
a3 = data['Pclass'].value_counts()
#print(a3)
print("Ответ: %d" % (round(a3[1]/(a3[1]+a3[2]+a3[3])*100)))

"""
import numpy as np

X = np.random.normal(loc=1, scale=10, size=(1000, 50))
print(X)

m = np.mean(X, axis=0)
std = np.std(X, axis=0)
X_norm = ((X - m)/std)
print(X_norm)


print("Hello!")

Z = np.array([[4, 5, 10],
             [1, 9, 3],
             [5, 1, 1],
             [3, 3, 3],
             [9, 9, 9],
             [4, 7, 1]])

r = np.sum(Z, axis=1)
print(r)
print(np.nonzero(r > 10))
"""


import pandas
print("Неделя №1. Задание №1 \n")

data = pandas.read_csv('./Data/titanic.csv', index_col='PassengerId')

print("Решение задачи №1")

a1 = data['Sex'].value_counts()
print("Ответ: %d %d" % (a1['male'],a1['female']))


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


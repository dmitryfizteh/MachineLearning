import pandas
from sklearn.tree import DecisionTreeClassifier

print("Неделя №1. Задание №2")

# Оставьте в выборке четыре признака: класс пассажира (Pclass), цену билета (Fare), возраст пассажира (Age) и его пол (Sex)
usecols=['PassengerId', 'Pclass', 'Fare', 'Age', 'Sex', 'Survived']

# Загрузите выборку из файла titanic.csv с помощью пакета Pandas
X = pandas.read_csv('./Data/titanic.csv', index_col='PassengerId', usecols=usecols)

# Выведем статистику выживаемости в зависимости от класса и пола.
#print(X.groupby(["Pclass", "Sex"])["Survived"].value_counts(normalize=True))
#print(X.groupby(["Sex"])["Survived"].value_counts(normalize=True))

# Обратите внимание, что признак Sex имеет строковые значения. Заменяем на {0;1}
X['Sex'] = X['Sex'].factorize()[0]

# В данных есть пропущенные значения — например, для некоторых пассажиров неизвестен их возраст. Такие записи при чтении их в pandas принимают значение nan. Найдите все объекты, у которых есть пропущенные признаки, и удалите их из выборки.
X = X.dropna()

# Выделите целевую переменную — она записана в столбце Survived.
Y = X['Survived']
X = X.drop('Survived', axis=1)

# Обучите решающее дерево с параметром random_state=241 и остальными параметрами по умолчанию.
clf = DecisionTreeClassifier(random_state=241)
clf.fit(X, Y)

# Вычислите важности признаков и найдите два признака с наибольшей важностью. Их названия будут ответами для данной задачи (в качестве ответа укажите названия признаков через запятую или пробел).
importances = clf.feature_importances_

imp = list(importances)
imp.sort()
imp.reverse()

a1 = list.index(list(importances), imp[0])
a2 = list.index(list(importances), imp[1])

print("Ответ: %s %s" % (usecols[a1+1], usecols[a2+1]))
f = open('./Answers/1.txt', 'w')
f.write("%s %s" % (usecols[a1+1], usecols[a2+1]))
f.close()

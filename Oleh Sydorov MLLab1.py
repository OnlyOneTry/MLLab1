import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt

pd.set_option('display.max_rows', 10)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1500)

print('Лабораторна робота №1.\n'
      'Використання бібліотек Pandas та Matplotlib\n'
      'Підгрупа №1\n'
      'Група КМ-92\n'
      'Сидоров Олег Сергійович'
      )
# Task 1
print('TASK 1: Відкрити та зчитати файл з даними.')
sales = pd.read_csv(r'C:\Users\olegi\DataspellProjects\MachineLearning/Vehicle_Sales.csv')
print(sales)

# Task 2
print('TASK 2: Визначити та вивести кількість записів та кількість полів у кожному записі.')
column_count = sum(1 for row in sales)
print('Number of columns: ', column_count)

print('Number of rows: ', len(sales))

# Task 3
print('TASK 3: Вивести К+7 перших та 5К-3 останніх записів.')
K = int(input("Please, enter value of K: "))

# A
print('TASK 3 - A: Вивести К+7 перших')
print(sales.head(K + 7))

# B
print('TASK 3 - B: Вивести 5К-3 останніх записів.')
print(sales.tail(5 * K - 7))

# Task 4
print('TASK 4: Визначити та вивести тип полів кожного запису.')
sales.info()

for i in sales:
    if sales[i].dtype == 'int64':
        print("Type is integer")
    if sales[i].dtype == 'object':
        print("Type is string")

# Task 5
print('TASK 5: Привести поля, що відповідають обсягам продаж, до числового вигляду (показати, що це виконано).')
SalesNewList = sales['Total Sales New'].tolist()
print(SalesNewList)

ch = '$'
for i in range(len(SalesNewList)):
    SalesNewList[i] = SalesNewList[i].lstrip(ch)
print(SalesNewList)

SalesUsedList = sales['Total Sales Used'].tolist()
print(SalesUsedList)

ch = '$'
for i in range(len(SalesUsedList)):
    SalesUsedList[i] = SalesUsedList[i].lstrip(ch)
print(SalesUsedList)

# Task 6
print('TASK 6')
salescopy = sales.copy()
print(salescopy)

for i in range(len(SalesNewList)):
    SalesNewList[i] = int(SalesNewList[i])
for i in range(len(SalesUsedList)):
    SalesUsedList[i] = int(SalesUsedList[i])

salescopy['Total Sales New int'] = SalesNewList
salescopy['Total Sales Used int'] = SalesUsedList
print(salescopy)

salescopy.info()

# A
print('TASK 6 - A: Сумарний обсяг продаж автомобілів (нових та б/в) у кожний період;')
salescopy['Total Money Earned'] = salescopy[['Total Sales New int', 'Total Sales Used int']].sum(axis=1)
print(salescopy)

# B
print('TASK 6 - B: Сумарний дохід від продажу автомобілів (нових та б/в) у кожний період;')
salescopy['Total Cars Sold'] = salescopy[['New', 'Used']].sum(axis=1)
print(salescopy)

# C
print('TASK 6 - C: Різницю в обсязі продаж нових та б/в автомобілів у кожній період.')
salescopy['Difference of New and Used'] = salescopy['Used'] - salescopy['New']
print(salescopy)

# Task 7
print('TASK 7:Змінити порядок розташування полів таким чином: Рік, Місяць,\n'
      'Сумарний дохід, Дохід від продажу нових автомобілів, Дохід від\n'
      'продажу б/в автомобілів, Сумарний обсяг продаж, Обсяг продаж нових\n'
      'автомобілів, Обсяг продаж б/в автомобілів, Різниця між обсягами\n'
      'продаж нових та б/в автомобілів.')
salescopy_new = salescopy.reindex(columns=['Year', 'Month', 'Total Money Earned', 'Total Sales New',
                                           'Total Sales Used', 'Total Cars Sold', 'Difference of New and Used'])
print(salescopy_new)

# Task 8
print('TASK 8')

# A
print('TASK 8 - A: Рік та місяць, у які нових автомобілів було продано менше за б/в;')
print(sales[sales['New'] > sales['Used']])

# B
print('TASK 8 - B: Рік та місяць, коли сумарний дохід був мінімальним;')
minmoney = salescopy_new['Total Money Earned'].min()
print(minmoney)

# C
print('TASK 8 - C: Рік та місяць, коли було продано найбільше б/в авто.')
maxsold = salescopy_new['Total Cars Sold'].max()
print(maxsold)

# Task 9
print('TASK 9')

# A
print('TASK 9 - A: Сумарний обсяг продажу транспортних засобів за кожен рік;')
salescopy_new = salescopy_new.groupby('Year', as_index=False).sum()
salescopy_new = salescopy_new[['Year', 'Total Money Earned']].sort_values(by=['Year'],
                                                                          ascending=True)
print(salescopy_new)

# B
print('TASK 9 - B: Середній дохід від продажу б/в транспортних засобів в місяці М(1),\n' 
'де М(1) – це порядковий номер у списку підгрупи за абеткою')
salescopy2 = salescopy.copy()
salescopy2 = salescopy2.groupby('Month', as_index=False).mean()
salescopy2 = salescopy2[['Month', 'Total Money Earned']].sort_values(by=['Month'],
                                                                     ascending=True)
print(salescopy2)
print(salescopy2.loc[4])

# Task 10
print('TASK 10: Побудувати стовпчикову діаграму обсягу продаж нових авто у\n'
'році 20YY, де дві останні цифри року визначаються як 17 – порядковий номер\n'
'у списку підгрупи за абеткою. ')
salescopy3 = salescopy.copy()
print(salescopy3)
salescopy3 = salescopy3[salescopy3['Year'] == 2016]
print(salescopy3)

plt.bar(salescopy3['Month'], salescopy3['New'])
plt.show()

# Task 11
print('TASK 11: Побудувати кругову діаграму сумарного обсягу продаж за кожен рік.')
salescopy4 = salescopy.copy()
salescopy4 = salescopy4.groupby('Year', as_index=False).sum()
salescopy4 = salescopy4[['Year', 'Total Cars Sold']].sort_values(by=['Year'],
                                                                 ascending=True)
print(salescopy4)

labels = salescopy4['Year'].tolist()
print(labels)

fig, ax = plt.subplots()
ax.pie(salescopy4['Total Cars Sold'], labels=labels)
ax.axis("equal")
plt.show()

# Task 12
print('TASK 12: Побудувати на одному графіку:\n'
'a. Сумарний дохід від продажу нових авто;\n'
'b. Сумарний дохід від продажу старих авто.')
sales = sales.groupby('Year', as_index=False).sum()
sales = sales[['Year', 'New', 'Used']].sort_values(by=['Year'],
                                                   ascending=True)
print(sales)

figg = plt.figure(dpi=100, figsize=(512 / 100, 384 / 100))
mpl.rcParams.update({'font.size': 8})

plt.title('Sales New and Used')

ax = plt.axes()

xs = range(len(sales['Year']))

plt.bar([x + 0.05 for x in xs], sales['New'],
        width=0.2, color='red', alpha=1, label='New',
        zorder=2)
plt.bar([x + 0.3 for x in xs], sales['Used'],
        width=0.2, color='blue', alpha=1, label='Used',
        zorder=2)
plt.xticks(xs, sales['Year'])

plt.legend(loc='upper right')
plt.show()

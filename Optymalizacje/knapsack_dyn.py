import pandas
import random

pandas.set_option('display.expand_frame_repr', False)
pandas.set_option('display.max_columns', None)
backpack_cap = 30
data_dict = {'Items': ["P" + str(i + 1) for i in range(6)],
             'Values': [10, 8, 7, 12, 5, 3],
             'Weights': [7, 10, 3, 12, 8, 5]}
# comment above data_dict and uncomment below data_dict for any random set of starting items
n = 6
# data_dict = {'Items': ["Item" + str(i + 1) for i in range(n)],
#              'Values': [random.randrange(1, 30) for i in range(n)],
#              'Weights': [random.randrange(1, 7) for i in range(n)]}

data = pandas.DataFrame(data_dict)
print(data, '\n')
index = [['Item'] + [x for x in data['Items']],
         ['Value'] + [x for x in data['Values']],
         ['Weight'] + [x for x in data['Weights']]]
table = pandas.DataFrame([[0 for column in range(backpack_cap + 1)] for row in range(len(data.index)+1)],
                         columns=[x for x in range(backpack_cap + 1)], index=index)
items = pandas.DataFrame([[0 for column in range(backpack_cap + 1)] for row in range(len(data.index)+1)],
                         columns=[x for x in range(backpack_cap + 1)], index=index)
sum_weights = 0

for i in range(1, len(table.index)):
    fill = ""
    sum_weights += table.index[i][2]
    for j in range(1, len(table.columns)):
        if i == 0 or j == 0:
            table.iloc[i, j] = 0
            items.iloc[i, j] = 0
        elif j < table.index[i][2]:
            table.iloc[i, j] = table.iloc[i - 1, j]
            items.iloc[i, j] = items.iloc[i - 1, j]
        else:
            table.iloc[i, j] = max(table.iloc[i-1, j], table.iloc[i-1, j - table.index[i][2]] + table.index[i][1])
            if table.iloc[i, j] == table.iloc[i-1, j - table.index[i][2]] + table.index[i][1]:
                if items.iloc[i-1, j - items.index[i][2]] == 0:
                    items.iloc[i, j] = items.index[i][0]
                else:
                    items.iloc[i, j] = items.iloc[i - 1, j - items.index[i][2]] + "+" + items.index[i][0]
            if table.iloc[i, j] == table.iloc[i-1, j]:
                items.iloc[i, j] = items.iloc[i - 1, j]
print(backpack_cap)
print(table)
print('\n')
print(items)


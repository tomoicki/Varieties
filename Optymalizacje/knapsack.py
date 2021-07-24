import pandas
import random

backpack_cap = 100
# data_dict = {'Items': ["P" + str(i + 1) for i in range(6)],
#              'Values': [10, 8, 7, 12, 5, 3],
#              'Weights': [7, 10, 3, 12, 8, 5],
#              'Quantity': [7, 10, 5, 4, 7, 11]}
# comment above data_dict and uncomment below data_dict for any random set of starting items
n = 10
data_dict = {'Items': ["Item" + str(i + 1) for i in range(n)],
             'Values': [random.randrange(1, 30) for i in range(n)],
             'Weights': [random.randrange(1, 7) for i in range(n)],
             'Quantity': [random.randrange(1, 10) for i in range(n)]}

data = pandas.DataFrame(data_dict)
print(data)
data['V/W'] = data['Values'] / data['Weights']
data.sort_values('V/W', inplace=True, ascending=False)
print("\n Calculating Value / Weight and sorting...")
print(data)
min_weight = data['Weights'].min()
backpack = pandas.DataFrame()
cap = 0
remaining_cap = backpack_cap
while backpack_cap - cap >= min_weight and len(data.index) >= 1:
    quantity2add = backpack_cap // data.iloc[0, 2]
    q = min(quantity2add, data.iloc[0, 3], remaining_cap // data.iloc[0, 2])
    new_row = {'Items': data.iloc[0, 0],
               'Quantity': q,
               'Item_value': data.iloc[0, 1],
               'Item_weight': data.iloc[0, 2],
               'Sum_weight': q * data.iloc[0, 2],
               'Sum_value': q * data.iloc[0, 1]}
    if q > 0:
        backpack = backpack.append(new_row, ignore_index=True)
    cap = backpack['Sum_weight'].sum()
    remaining_cap = backpack_cap - cap
    data.reset_index(inplace=True, drop=True)
    if quantity2add > data.iloc[0, 3]:
        data.drop(0, inplace=True)
    elif backpack_cap - cap < data.iloc[0, 2]:
        data.drop(0, inplace=True)
backpack = backpack.applymap(lambda x: int(x) if type(x) != str else x)
backpack = backpack.reindex(columns=['Items', 'Sum_value', 'Item_value', 'Quantity', 'Item_weight', 'Sum_weight'])
print("\nItems in our backpack...")
print(backpack)
print("\nWe managed to get {} items of total value {} weighting {} leaving {} free space in the backpack.".format(
    backpack['Quantity'].sum(),
    backpack['Sum_value'].sum(),
    int(cap),
    int(backpack_cap - cap)))

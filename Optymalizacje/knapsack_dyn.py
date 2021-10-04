import pandas as pd

pd.set_option('display.expand_frame_repr', False)
pd.set_option('display.max_columns', None)

pojemnosc_plecaka = 30
przedmioty = pd.DataFrame([['p1', 8, 5], ['p2', 8, 9], ['p3', 10, 6],
                           ['p4', 11, 8], ['p5', 4, 12], ['p6', 5, 11]],
                          columns=['P', 'Cena', 'Waga'],
                          index=['111','222','333',2,3,4])
print(przedmioty, '\n')
print(przedmioty.loc['222', 'Cena'])
# index = [['Item'] + [x for x in data['Items']],
#          ['Value'] + [x for x in data['Values']],
#          ['Weight'] + [x for x in data['Weights']]]
# table = pd.DataFrame([[0 for column in range(backpack_cap + 1)] for row in range(len(data.index) + 1)],
#                      columns=[x for x in range(backpack_cap + 1)], index=index)
# items = pd.DataFrame([[0 for column in range(backpack_cap + 1)] for row in range(len(data.index) + 1)],
#                      columns=[x for x in range(backpack_cap + 1)], index=index)
# sum_weights = 0
#
# for i in range(1, len(table.index)):
#     fill = ""
#     sum_weights += table.index[i][2]
#     for j in range(1, len(table.columns)):
#         if i == 0 or j == 0:
#             table.iloc[i, j] = 0
#             items.iloc[i, j] = 0
#         elif j < table.index[i][2]:
#             table.iloc[i, j] = table.iloc[i - 1, j]
#             items.iloc[i, j] = items.iloc[i - 1, j]
#         else:
#             table.iloc[i, j] = max(table.iloc[i - 1, j], table.iloc[i - 1, j - table.index[i][2]] + table.index[i][1])
#             if table.iloc[i, j] == table.iloc[i - 1, j - table.index[i][2]] + table.index[i][1]:
#                 if items.iloc[i - 1, j - items.index[i][2]] == 0:
#                     items.iloc[i, j] = items.index[i][0]
#                 else:
#                     items.iloc[i, j] = items.iloc[i - 1, j - items.index[i][2]] + "+" + items.index[i][0]
#             if table.iloc[i, j] == table.iloc[i - 1, j]:
#                 items.iloc[i, j] = items.iloc[i - 1, j]
# print(backpack_cap)
# print(table)
# print('\n')
# print(items)

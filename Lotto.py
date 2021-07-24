import pandas


pandas.set_option('display.width', None)
pandas.set_option('display.max_columns', None)
pandas.set_option('colheader_justify','center')
pandas.set_option('display.show_dimensions', False)
pandas.set_option('display.max_rows', None)

data = pandas.read_csv('Lotto.csv',delimiter=';')
data['5'] = 0
j = 0
data5 = pandas.DataFrame(columns=data.columns)
for i in range(data.index.size):
    series_of_matches_sum = data.loc[:,'L1':'L6'].isin(data.loc[i,'L1':'L6'].unique()).astype(int).sum(axis=1)
    if series_of_matches_sum.loc[series_of_matches_sum >= 5].index.size > 1:
        temp = data.iloc[series_of_matches_sum.loc[series_of_matches_sum >= 5].index]
        temp['5'] = j
        data5 = pandas.concat([data5, temp])
        j += 1
data5.set_index('5', drop=True, inplace=True)
data5.to_csv('Lotto5.csv')
import numpy as np
import pandas as pd

data_trn = 'iriss_trn.txt'
data_tst = 'iriss_tst.txt'
trn = pd.read_csv(data_trn, skiprows=1, header=None, delim_whitespace=True)  # delimiter=r"\s+"
tst = pd.read_csv(data_tst, skiprows=1, header=None, delim_whitespace=True)  # delimiter=r"\s+"

# Number of classes
with open(data_tst) as f:
    first_line = f.readline()
class_number = int(first_line.split()[0])

# Standardisation parameters
mv = trn.mean()
sd = trn.std()

# AssignedClass gravity centers before standardisation
p_bs = []
i = 1
while i <= class_number:
    p_bs.append(trn.loc[trn[0] == i].mean())
    i += 1

print('AssignedClass gravity centers before standardisation:\n')
df_bs = pd.DataFrame(p_bs)  # AssignedClass gravity centers before standardisation
del df_bs[0]
df_bs.index = range(1, len(df_bs) + 1)
print(df_bs.to_string(), '\n')

# AssignedClass gravity centers after standardisation
p_as = []
i = 1
while i <= class_number:
    p_as.append((trn.loc[trn[0] == i].mean() - mv) / sd)
    i += 1

print('AssignedClass gravity centers after standardisation:\n')
df_as = pd.DataFrame(p_as)  # AssignedClass gravity centers after standardisation
del df_as[0]
df_as.index = range(1, len(df_as) + 1)
print(df_as.to_string(), '\n')

# Zad2
print('Weights before standardisation including:\n')
wb_first_col = df_as * 2
wb_last_col = -(df_as ** 2)
wb_last_col = wb_last_col.sum(axis=1, skipna=True)
wb_last_col.name = number_of_rows = trn.shape[1]
wb = pd.concat([wb_first_col, wb_last_col], axis=1)
print(wb.to_string(), '\n')

print('Weights after standardisation including:\n')
del sd[0]
del mv[0]
wa_first_col = wb_first_col / sd
wa_last_col = wa_first_col * mv
wa_last_col = wb_last_col - wa_last_col.sum(axis=1, skipna=True)
wa_last_col.name = number_of_rows = trn.shape[1]
wa = pd.concat([wa_first_col, wa_last_col], axis=1)
print(wa.to_string(), '\n')

# Calculating g
class_column = pd.DataFrame(tst[0])
class_column.index = range(1, len(class_column) + 1)

del tst[0]
g_l = []
i = 0
while i < class_number:
    g_l.append((wa.iloc[i] * tst).T.sum() + wa_last_col[i + 1])
    i += 1
g_df = pd.DataFrame(g_l)
g = g_df.T
g.index = range(1, len(g) + 1)

g['Max'] = g.max(axis=1)
g['AssignedClass'] = g.idxmax(axis=1)
g['AssignedClass'] = g['AssignedClass'] + 1

g.insert(0, 'TrueClass', class_column)
g.index.name = 'Object Nr'

# Comparing True Class with AssignedClass
g['Error'] = np.where(g['TrueClass'] == g['AssignedClass'], 0, 1)

print('Error rate:', round(g['Error'].sum()/tst.shape[0]*100, 2), '% \n')
print(g)
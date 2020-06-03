import pandas as pd
import random

dfs = pd.read_excel('hsk4_vocabulary.xlsx', sheet_name=None)

print(dfs)

przerobione = dfs['Przerobione']['id']
losowe_znaczki = []
while len(losowe_znaczki) < 5:
    znaczek = random.randint(1, 1200)
    if znaczek not in przerobione:
        losowe_znaczki.append([znaczek, dfs['baza']['Chinese'][znaczek], dfs['baza']['Pinyin'][znaczek],
                               dfs['baza']['English'][znaczek]])
        print('losowe znaczki len to ' + str(len(losowe_znaczki)))

losowy_df = pd.DataFrame(losowe_znaczki, columns=dfs['Przerobione'].columns)
print(losowy_df)
przerobiony_df = pd.concat([dfs['Przerobione'], losowy_df])
print(przerobiony_df)

with pd.ExcelWriter('hsk4_vocabulary.xlsx') as writer:
    dfs['baza'].to_excel(writer, sheet_name='baza', index=False)
    przerobiony_df.to_excel(writer, sheet_name='Przerobione', index=False)
    losowy_df.to_excel(writer, sheet_name='5 losowych', index=False)
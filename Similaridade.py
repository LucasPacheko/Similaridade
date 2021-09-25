import pandas as pd

df = pd.read_csv('CÓDIGOS CBHPM.csv', encoding = 'windows-1252')
df = df.astype(str)
str_la = 'JO103484'

def blocagem(df, column):
    df['bloco'] = df[column].apply(lambda a: a.split())
def similarity(s1:str, s2:str):
    longer = s1
    shorter = s2
    if len(s1)< len(s2):
        longer = s2
        shorter = s1
    lenLong = len(longer)
    if lenLong == 0:
        return 1.0
    return (lenLong - editDistance(longer, shorter))/ lenLong
def editDistance(s1:str, s2:str, caseSensitive:bool = False):
    if not caseSensitive:
        s1 = s1.lower()
        s2 = s2.lower()
    m = len(s1)
    n = len(s2)
    dp = [[0 for x in range(n + 1)] for x in range(m + 1)]

    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0:
                dp[i][j] = j  # Min. operations = j

            elif j == 0:
                dp[i][j] = i  # Min. operations = i

            elif s1[i - 1] == s2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]

            else:
                dp[i][j] = 1 + min(dp[i][j - 1],  # Insert
                                   dp[i - 1][j],  # Remove
                                   dp[i - 1][j - 1])  # Replace

    return dp[m][n]

def similar_CBHPM(str,pesquisarPor='Descrição'):
    df['temp'] = df[pesquisarPor].apply(lambda a: similarity(str, a))
    print('oi')
    return df.nlargest(10,'temp')
print(similar_CBHPM('ZAP-70'))




# df['temp'] = df['Descrição'].apply(lambda a: similarity(str_la,a))



# df['temp2'] = df['bloco'].apply(lambda a: similarity(str_la,a))
# print(df.nlargest(10,'temp'))
# df1 = df.nlargest(10,'temp')




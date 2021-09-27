import pandas as pd

class similaridade():
    def __init__(self) -> None:
        self.df = pd.read_csv('CÓDIGOS CBHPM.csv', encoding = 'windows-1252')
        self.df = self.df.astype(str)

    def blocagem(self,df, column):
        df['bloco'] = df[column].apply(lambda a: a.split())

    def similarity(self,s1:str, s2:str):
        longer = s1
        shorter = s2
        if len(s1)< len(s2):
            longer = s2
            shorter = s1
        lenLong = len(longer)
        if lenLong == 0:
            return 1.0
        return (lenLong - self.editDistance(longer, shorter))/ lenLong

    def editDistance(self,s1:str, s2:str, caseSensitive:bool = False):
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

    def similar_CBHPM(self,str,pesquisarPor='Descrição'):
        self.df['temp'] = self.df[pesquisarPor].apply(lambda a: self.similarity(str, a))
        print('oi')
        return self.df.nlargest(10,'temp')

# df['temp'] = df['Descrição'].apply(lambda a: similarity(str_la,a))
# df['temp2'] = df['bloco'].apply(lambda a: similarity(str_la,a))
# print(df.nlargest(10,'temp'))
# df1 = df.nlargest(10,'temp')

if __name__=="__main__":
    print(similaridade().similar_CBHPM('ZAP-70'))
    print(similaridade().similar_CBHPM('JO103484','TISS código'))
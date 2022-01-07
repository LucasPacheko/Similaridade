import pandas as pd
import os.path


class Similarity:
    def __init__(self, file = 'CÓDIGOS CBHPM.csv', encoding= 'windows-1252'):
        self.df = pd.DataFrame()
        if(os.path.isfile(file)):
            self.load_from(file,encoding= encoding)
    def load_from(self,file, encoding= 'windows-1252'):
        self.df = pd.read_csv(file, encoding = encoding)
        self.df = self.df.astype(str)
    def similarity(self, s1: str, s2: str, caseSensitive):
        return self.__similarity( s1, s2, caseSensitive)
        
    def __similarity(self, s1: str, s2: str, caseSensitive):
        longer = s1
        shorter = s2
        if len(s1) < len(s2):
            longer = s2
            shorter = s1
        lenLong = len(longer)
        if lenLong == 0:
            return 1.0

        score = 0.0
        key_list = s1.split(" ")
        targ_list = s2.split(" ")
        for keyi in key_list:
            best = 0 
            for targ in targ_list:

                longer = keyi
                shorter = targ
                if len(keyi ) < len(targ):
                    longer = targ
                    shorter = keyi

                lenLong = len(longer)
                score_prov = (lenLong - self.__editDistance(longer, shorter, caseSensitive)) / lenLong
                if score_prov>best:
                    best = score_prov
            score+=best
        return score/(len(key_list))

    def __editDistance(self, s1: str, s2: str, caseSensitive):
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

    def similar(self,df_linhas, chave, coluna='text', caseSensitive: bool = False):
        df_linhas['temp'] = df_linhas[coluna].apply(lambda a: self.__similarity(chave,a, caseSensitive))

        return df_linhas.nlargest(10, 'temp')


if __name__ == '__main__':
    sim = Similarity()
    # print(sim.similar('zap-7'))

    # sim.load_from('chaves.csv')

    print(sim.similarity('CREATININA', 'CREATININA - (LABORATORIO EXAMES URGENCIA E EMERGENCIA)' ,False))




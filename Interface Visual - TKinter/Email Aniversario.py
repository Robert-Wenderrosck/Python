import pandas as pd
from datetime import date
import numpy as np


arquivoAniversario = pd.read_excel("Aniversario.xlsx")

arquivoAniversario["Nascimento"] = arquivoAniversario["Nascimento"].astype(str) #Converte a coluna nascimento para texto



arquivoAniversario["Ano"] = arquivoAniversario["Nascimento"].str[:4] #Cria uma coluna nova chamada ano e adiciona os 4 primeiros digitos de cada linha da coluna Nascimento

arquivoAniversario["Mes"] = arquivoAniversario["Nascimento"].str[5:7] #Cria uma coluna nova chamada mês e adiciona os 2 digitos que representa os meses

arquivoAniversario["Dia"] = arquivoAniversario["Nascimento"].str[-2:] #Cria uma coluna nova chamada dia e adiciona os 2 últimos digitos que representa os dias


arquivoAniversario["Data Atual"] = date.today()

arquivoAniversario["Data Atual"] = arquivoAniversario["Data Atual"].astype(str) #Converte a coluna Data Atual para texto


arquivoAniversario["Ano Atual"] = arquivoAniversario["Data Atual"].str[:4]

arquivoAniversario["Mes Atual"] = arquivoAniversario["Data Atual"].str[5:7]

arquivoAniversario["Dia Atual"] = arquivoAniversario["Data Atual"].str[-2:]


arquivoAniversario["aniversario"] = np.where((arquivoAniversario["Mes"] == arquivoAniversario["Mes Atual"]) &
                                             (arquivoAniversario["Dia"] == arquivoAniversario["Dia Atual"]), "Sim", "")


print(arquivoAniversario)

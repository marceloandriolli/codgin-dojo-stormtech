""""
Todas as vezes que alguém passa na porta do maior banco da cidade de 
Pirenópolis, é gravado em um arquivo de log a data e a hora da abertura da 
porta.

Cada registro no arquivo de log possui o seguinte formato:

[YYYY-mm-dd H:i:s] - Abertura da Porta OK

O gerente do banco precisa saber quantas pessoas entraram no banco no horário 
de expediente, para isso ele solicitou que você faça um programa que verifique 
se o registro de entrada é válido e se a hora se encontra dentro do intervalo 
de funcionamento do banco, das 10:00:00 até as 16:00:00.

"""
from datetime import datetime

def log(data):
    hora = int(data[10:].replace(':', ''))
    return hora >= 100000 and hora <= 160000


assert log('2018-03-29 09:48:01') == False
assert log('2018-03-29 10:48:01') == True
assert log('2018-03-29 10:00:00') == True
assert log('2018-03-29 16:48:01') == False
assert log('2018-03-29 16:00:00') == True
assert log('2018-03-29 16:00:00') == True


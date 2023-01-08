import os
import smtplib
from email.message import EmailMessage

import pandas as pd 
tabela_vendas = pd.read_excel('Vendas.xlsx')

# vizualiar a base de dados 
pd.set_option('display.max_columns',None)
#print (tabela_vendas)
#print('-'*50)
#faturamento por loja, agrupar e somar 

faturamento = tabela_vendas [['ID Loja','Valor Final']].groupby('ID Loja').sum()
#print (faturamento)
#print('-'*50)

#quantidades de produtos vendidos por loja, agrupar e somar
quantidade = tabela_vendas [['ID Loja','Quantidade']].groupby('ID Loja').sum()
#print(quantidade)
#print('-'*50)

#tiket medio por produto de cada loja 
tiket = (faturamento['Valor Final'] / quantidade['Quantidade']).to_frame()
tiket = tiket.rename(columns={0: 'ticket médio'})
#print(tiket)
#print('-'*50)





# configurar email

EMAIL_ADDRESS = 'alessandrohn120@gmail.com'
EMAIL_PASSWORD = 'ogeielibgbukrvzs'

#criar um email

msg = EmailMessage()
msg['subject'] = 'o relatorio esta pronto'
msg['from'] = 'alessandrohn120@gmail.com'
msg['to'] = 'alessandrohn120@gmail.com'
msg.set_content (f"""
Prezados,
Segue os dados do relatorio da empresa atualizados.\n


faturamento da loja\n
{faturamento}

Quantidade de produtos vendidos por loja.\n 
{quantidade}

ticket medio de produto por cada loja.\n
{tiket}


Qualquer duvida estou à disposição...

""")

#enviar um email

with smtplib.SMTP_SSL('smtp.gmail.com',465) as smtp:
        smtp.login(EMAIL_ADDRESS,EMAIL_PASSWORD)
        smtp.send_message(msg)
print ('mensagem enviada')
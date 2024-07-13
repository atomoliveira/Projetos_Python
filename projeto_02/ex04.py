#Faça um programa que envie um email 

import smtplib
from email.message import EmailMessage

# Informações do e-mail
remetente = 'adriano_396@hotmial.com'
destinatario = 'oliveiraadriano478@gmail.com'
assunto = 'Ola blz'
corpo = 'Este é o corpo do e-mail.'

# Crie a mensagem de e-mail
mensagem = EmailMessage()
mensagem['From'] = remetente
mensagem['To'] = destinatario
mensagem['Subject'] = assunto
mensagem.set_content(corpo)

# Detalhes do servidor SMTP (exemplo: Gmail)
smtp_servidor = 'smtp.gmail.com'
smtp_porta = 587
senha = 'ap020613'

# Enviando o e-mail
try:
    with smtplib.SMTP(smtp_servidor, smtp_porta) as servidor:
        servidor.starttls()  # Inicia a conexão TLS
        servidor.login(remetente, senha)  # Faz login no servidor SMTP
        servidor.send_message(mensagem)  # Envia a mensagem de e-mail
        print('E-mail enviado com sucesso!')
except Exception as e:
    print(f'Erro ao enviar e-mail: {e}')

#Faça um programa que crie um QR Code de um determinado link

import qrcode

def gerar_qrcode(url, nome_aqruivo):
  qr= qrcode,QRCODE(
      version = 1,
      error_correction=qrcode.constants.ERROR_correct_L,
      box_size=10,
      border=1
  )
  qr.add_data(url)
  qr.make(fit = True)

  img = qr.make_image(fill_color="black",back_color="white")
  img.save(nome_arquivo)

  url = "https://github.com/atomoliveira"

  nome_arquivo = "qr_code.png"

  gerar_qrcode(url, nome_arquivo)

  print(f"QR code gerado e salvo com (nome_arquivo)")
    
    
    
  

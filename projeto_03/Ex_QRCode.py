#Crie um programa que gere qrcode

import qrcode

def gerar_qr_code(dados, nome_arquivo):
    # Cria um objeto QRCode
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )

    # Adiciona os dados ao QRCode
    qr.add_data(dados)
    qr.make(fit=True)

    # Cria uma imagem do QRCode usando a biblioteca Pillow (PIL)
    imagem_qr = qr.make_image(fill_color="black", back_color="white")

    # Salva a imagem do QRCode em um arquivo
    imagem_qr.save(nome_arquivo)

if __name__ == "__main__":
    # Exemplo de dados para o QRCode (pode ser um link, texto, etc.)
    dados_qr = "file:///C:/Users/adria/OneDrive/%C3%81rea%20de%20Trabalho/Pag.html"

    # Nome do arquivo de saída (pode ser alterado conforme necessário)
    nome_arquivo_qr = "qr_code_exemplo.png"

    # Gera o QRCode
    gerar_qr_code(dados_qr, nome_arquivo_qr)

    print(f"QRCode gerado com sucesso! Salvo como '{nome_arquivo_qr}'.")

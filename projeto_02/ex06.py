#Faça um programa que construa um boleto com dados e valores.

from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from datetime import date

def gerar_boleto(id_boleto, cedente, cedente_cnpj, agencia, conta, nosso_numero, valor, vencimento, sacado_nome, sacado_documento, sacado_endereco):
    # Criação do PDF
    c = canvas.Canvas(f"boleto_{id_boleto}.pdf", pagesize=A4)
    largura, altura = A4
    
    # Desenhando o boleto
    c.setFont("Helvetica", 12)
    
    # Título
    c.drawString(30, altura - 30, "Boleto Bancário")
    
    # Cedente
    c.drawString(30, altura - 60, f"Cedente: {cedente}")
    c.drawString(30, altura - 80, f"CNPJ: {cedente_cnpj}")
    
    # Agência/Conta
    c.drawString(30, altura - 110, f"Agência/Código do Cedente: {agencia}/{conta}")
    
    # Nosso Número
    c.drawString(30, altura - 140, f"Nosso Número: {nosso_numero}")
    
    # Valor
    c.drawString(30, altura - 170, f"Valor: R$ {valor:.2f}")
    
    # Vencimento
    c.drawString(30, altura - 200, f"Data de Vencimento: {vencimento.strftime('%d/%m/%Y')}")
    
    # Sacado
    c.drawString(30, altura - 230, f"Nome do Sacado: {sacado_nome}")
    c.drawString(30, altura - 250, f"Documento: {sacado_documento}")
    c.drawString(30, altura - 270, f"Endereço: {sacado_endereco}")

    # Linha digitável (exemplo fictício)
    linha_digitavel = "34191.79001 01043.510047 91020.150008 8 89070000001000"
    c.drawString(30, altura - 300, f"Linha Digitável: {linha_digitavel}")
    
    # Código de Barras (exemplo fictício)
    # Aqui, normalmente, você usaria uma biblioteca para desenhar um código de barras real
    c.drawString(30, altura - 330, "Código de Barras: |||||| |||| |||| |||| |||| |||| |||| |||| ||||")

    # Finaliza o PDF
    c.save()

# Exemplo de uso
if __name__ == "__main__":
    id_boleto = 1
    cedente = "Empresa Exemplo"
    cedente_cnpj = "12.345.678/0001-99"
    agencia = "1234"
    conta = "56789-0"
    nosso_numero = "1234567"
    valor = 100.50
    vencimento = date(2023, 12, 10)
    sacado_nome = "Nome do Cliente"
    sacado_documento = "123.456.789-00"
    sacado_endereco = "Rua Exemplo, 123 - Bairro - Cidade/UF"
    
    gerar_boleto(id_boleto, cedente, cedente_cnpj, agencia, conta, nosso_numero, valor, vencimento, sacado_nome, sacado_documento, sacado_endereco)
    print(f"Boleto gerado com sucesso e salvo como 'boleto_{id_boleto}.pdf'")

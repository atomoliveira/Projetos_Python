#Faça um programa que construa um codigo de barra partir dos numeros dados

codigos_produtos = {
    "Feijao" : "551746511111",
    "Arroz" : "665789011111",
    "Macarrao" : "665887111111",
    "Azeite" : "998556211111" }

from barcode import EAN13
from barcode.writer import ImageWriter

for produto in codigos_produtos:
    codigo = codigos_produtos[produto]
    codigo_barra = EAN13(codigo,writer = ImageWriter())
    codigo_barra.save(f"codigo_barra{produto}")

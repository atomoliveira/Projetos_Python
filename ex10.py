
import yfinance as yf

# Lista de símbolos das bolsas de valores
bolsas = ['^GSPC', '^IXIC', '^DJI', '^N225', '^FTSE', '^GDAXI']

# Dicionário para armazenar as informações das bolsas de valores
bolsas_info = {}

# Obtém as informações de cada bolsa de valores
for simbolo in bolsas:
    bolsa = yf.Ticker(simbolo)
    bolsas_info[simbolo] = {
        'nome': bolsa.info['shortName'],
        'preco': bolsa.info['regularMarketPrice'],
        'variacao': bolsa.info['regularMarketChangePercent']
    }

# Exibe as maiores altas do dia
print("Maiores altas do dia:")
for simbolo, info in sorted(bolsas_info.items(), key=lambda x: x[1]['variacao'], reverse=True)[:3]:
    print(f"{info['nome']} ({simbolo}): {info['variacao']:.2f}%")

# Exibe as maiores baixas do dia
print("\nMaiores baixas do dia:")
for simbolo, info in sorted(bolsas_info.items(), key=lambda x: x[1]['variacao'])[:3]:
    print(f"{info['nome']} ({simbolo}): {info['variacao']:.2f}%")




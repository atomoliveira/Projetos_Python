
ph_valores = {
  "agua" : 7.0,
  "limao" : 2.0,
  "leite" : 6.5,
  "soda_cautica" : 14.0,
  "vinagre" : 2.4,
  "coca cola" : 2.5,
  "lagrimas" : 7.5,
  "suor" : 6.8,
  
}
nome_solucao= input("Digite o nome da solução:"). lower()
if nome_solucao in ph_valores :
  ph = ph_valores[nome_solucao]
  print(f"O pH da solução{nome_solucao} é {ph}")
else:
  print("Solução não encontrada no banco de dados.")
  
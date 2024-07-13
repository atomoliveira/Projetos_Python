import pyttsx3

# Inicializa o módulo pyttsx3
engine = pyttsx3.init()

# Define a frase a ser falada
frase = "Ola Boa Noite, Seja Bem Vindo!"

# Fala a frase
engine.say(frase)

# Aguarda a finalização da fala
engine.runAndWait()

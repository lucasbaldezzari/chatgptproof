import openai
import time
import configparser

def getCompletion(prompt, modelo="gpt-3.5-turbo"):
    """Genera una respuesta a partir de un prompt y un modelo de GPT.
    
    Por defecto el modelo es gpt-3.5-turbo, que es el que mejor resultados
    ha dado hasta ahora."""

    messages = [{"role": "user", "content": prompt}]

    response = openai.ChatCompletion.create(
        model=modelo,
        messages=messages,
        temperature=0, # this is the degree of randomness of the model's output
    )

    return response.choices[0].message["content"]

config = configparser.ConfigParser()
config.read("key.ini")

APIkey = config["openai"]["API_Key"]
openai.api_key  = APIkey

## Creamos un archivo de texto para guardar las respuestas
filename = "iterative.txt"
#guardamos el archivo en modo append
file = open(filename, "a")

#prompt inicial
prompt = "Hola, ¿cómo estás?"

# Bucle para iterar preguntas y respuestas
while True:
    # Genera la respuesta a partir del prompt actual
    response = getCompletion(prompt)

    # Obtiene la respuesta generada
    answer = response

    # Imprime la respuesta
    print("Bot: " + answer)

    #guardamos prompt y respuesta en el archivo
    file.write("User: " + prompt + "\n")
    file.write("Bot: " + answer + "\n")

    #Solicitamos una pregunta/prompt
    prompt = input("What else?: ")

    if prompt:
        # Agrega la pregunta o respuesta del usuario al prompt
        prompt += "\nBot: " + answer

        # Espera un segundo antes de continuar
        time.sleep(1)

    #chequeo si el usuario ingrso un prompt vacio
    if prompt == "":
        file.write("finalizado")
        file.close()
        break


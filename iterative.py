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
filename = "test.txt"
#guardamos el archivo en modo append
file = open(filename, "a", encoding='utf-8')

#prompt inicial
lista_promts = []
prompt = "Necesito un bot que me ayude a responder cuánto dinero gasto usando gpt-3.5-turbo considerando el\
costo igual a $0.002 / 1K tokens. No entiendo qué son los tokens y cómo contabilizarlo. ¿Podrías mostrarme un ejemplo? para\
entenderlo mejor. Usa el siguiente formato para dar las respuestas, [prompt] [respuesta] [cantidad tokens] [costo]. \
Dame los resultados en formato JSON con los siguientes keys [prompt] [respuesta] [cantidad tokens] [costo]."
lista_promts.append(prompt)

lista_respuestas = []

# Bucle para iterar preguntas y respuestas
while True:
    # Genera la respuesta a partir del prompt actual
    response = getCompletion(prompt)
    lista_respuestas.append(response)

    # Imprime la respuesta
    print("Bot: " + response)

    #guardamos prompt y respuesta en el archivo
    file.write("User: " + prompt + "\n")
    file.write("Bot: " + response + "\n")

    #Solicitamos una pregunta/prompt
    prompt = input("What else?: ")

    if prompt:

        ##La idea es brindar al bot sus respuestas anteriores para que pueda
        ##aprender de ellas y generar una respuesta más acorde a lo que el usuario
        ##está buscando. Para esto vamos a generar un prompt formado por el prompt nuevo
        ##y las respuestas anteriores. Cada respuesta la vamos a separar con un \n y todas estarán entre [].
        ##Usamos la lista lista_respuestas para generar el prompt

        ##Generamos el prompt
        respuestas = [{f"-{respuesta}\n" for respuesta in lista_respuestas}]
        prompt += f"El nuevo prompt esta entre ``````. El mismo es ```{prompt}```. Por favor, usa tus respuestas anteriores\
        para generar una respuesta. Tus respuestas están entre [] y se listan debajo.\n [{respuestas}]"

        # Espera un segundo antes de continuar
        time.sleep(1)

    #chequeo si el usuario ingrso un prompt vacio
    if prompt == "":
        file.write("finalizado")
        file.close()
        break


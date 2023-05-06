"""Primeros pasos con chatgpt y buenas prácticas de prompts."""

import configparser
import openai
import os

config = configparser.ConfigParser()
config.read("key.ini")

APIkey = config["openai"]["API_Key"]

openai.api_key  = APIkey

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

text = """Hola, soy un bot que te ayuda a aprender a programar en Python."""
# promt = f"""Por favor, usar el texto en triple backsticks ```{text}``` para identificar qué quiere el bot"""
promt = """Necesito saber cómo puedo usar tu motor de inteligencia artificial para generar respuestas a partir de un prompt iterativo.
Cuando digo iterativo quiero decir que podamos tener un ida y vuelta de preguntas y respuestas de tal manera que
el bot pueda aprender de lo que le digo y pueda generar respuestas más precisas.

Muestrame esto con código de Python, por favor."""

response = getCompletion(promt)
print(response) #nice!
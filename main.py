from fastapi import FastAPI
from pydantic import BaseModel
from transformers import pipeline

# Carga del modelo GPT-2
generador = pipeline("text-generation", model="gpt2")

# Función mejorada para responder en español
def responder_local(mensaje: str):
    prompt = f"Responde de forma natural en español: {mensaje}"
    resultado = generador(prompt, max_length=60, num_return_sequences=1)
    return resultado[0]['generated_text']

# Inicializa la app de FastAPI
app = FastAPI()

# Esquema de datos para recibir preguntas
class Pregunta(BaseModel):
    mensaje: str

# Endpoint principal para que Reyori responda
@app.post("/preguntar")
def responder(pregunta: Pregunta):
    respuesta = responder_local(pregunta.mensaje)
    return {"respuesta": respuesta}
import streamlit as st
import os
from openai import AzureOpenAI
from dotenv import load_dotenv

# Cargar las variables de entorno
load_dotenv()

# Título de la aplicación
st.title("Aplicación de Resumen y Respuesta con Azure OpenAI")

# Texto introductorio
st.write("Ingresa tu correo electrónico en el área de texto y selecciona si deseas generar un resumen o una respuesta.")

# Configurar el cliente de Azure OpenAI
client = AzureOpenAI(
    azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
    api_key=os.getenv("AZURE_OPENAI_API_KEY"),
    api_version="2024-02-01"
)

# Área de texto para ingresar el correo electrónico
email = st.text_area("Escribe tu correo electrónico aquí:")

# Función para generar un resumen utilizando Azure OpenAI
def generar_resumen(email_content):
    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",  # Asegúrate de que este modelo esté disponible en tu cuenta
            messages=[
                {"role": "system", "content": "Eres un asistente que hace resumenes de emails"},
                {"role": "user", "content": email_content}
            ]
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Error al generar el resumen: {e}"

# Función para generar una respuesta utilizando Azure OpenAI
def generar_respuesta(email_content):
    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",  # Asegúrate de que este modelo esté disponible en tu cuenta
            messages=[
                {"role": "system", "content": "Eres un asistente que genera respuestas a emails"},
                {"role": "user", "content": email_content}
            ]
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Error al generar la respuesta: {e}"

# Botón para generar un resumen
if st.button("Generar Resumen"):
    if email.strip():
        resumen = generar_resumen(email)
        st.subheader("Resumen:")
        st.write(resumen)
    else:
        st.warning("Por favor, ingresa un correo electrónico válido.")

# Botón para generar una respuesta
if st.button("Generar Respuesta"):
    if email.strip():
        respuesta = generar_respuesta(email)
        st.subheader("Respuesta:")
        st.write(respuesta)
    else:
        st.warning("Por favor, ingresa un correo electrónico válido.")

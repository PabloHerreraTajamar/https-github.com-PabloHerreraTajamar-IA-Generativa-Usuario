# Chat email

# Aplicación de Generación de Resumen y Respuesta

Esta es una aplicación interactiva construida con **Streamlit** que utiliza **Azure OpenAI** para procesar el contenido de un correo electrónico. La aplicación permite a los usuarios generar un **resumen** o una **respuesta** para el texto ingresado de forma rápida y sencilla.

## Características

- **Generar Resumen:** 
  - Proporciona un resumen conciso del contenido de un correo electrónico.
  - Ideal para revisar correos largos de manera eficiente.

- **Generar Respuesta:** 
  - Redacta una respuesta adecuada basada en el contenido ingresado.
  - Simplifica la redacción de correos electrónicos.

- **Interfaz Intuitiva:**
  - Basada en Streamlit, ofrece una experiencia interactiva y fácil de usar.
  - Muestra resultados directamente en la página después de procesar el texto.

- **Gestión Segura de Credenciales:**
  - Utiliza un archivo `.env` para almacenar de forma segura las credenciales de Azure OpenAI.

## ¿Cómo Funciona?

1. El usuario ingresa el contenido de un correo electrónico en un cuadro de texto.
2. Selecciona una de las dos opciones disponibles:
   - **Generar Resumen:** El modelo de Azure OpenAI procesa el correo y devuelve un resumen.
   - **Generar Respuesta:** El modelo genera una posible respuesta para el correo.
3. La salida generada se muestra directamente en la interfaz de usuario.

## Requisitos

- **Python:** Versión 3.8 o superior.
- Bibliotecas necesarias:
  - `streamlit`
  - `python-dotenv`
  - `openai`

Para instalar las dependencias, ejecuta:

```bash
pip install streamlit python-dotenv openai

import os
from openai import AzureOpenAI
from dotenv import load_dotenv

# Cargar las variables de entorno
load_dotenv()

# Configurar el cliente de Azure OpenAI
client = AzureOpenAI(
    azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
    api_key=os.getenv("AZURE_OPENAI_API_KEY"),
    api_version="2024-02-01"
)

# Inicializar el historial de la conversación
conversation_history = [
    {"role": "system", "content": "You are a helpful assistant."}
]

def chat_with_model():
    print("Bienvenido al chat interactivo. Escribe 'salir' para terminar.\n")

    while True:
        # Leer entrada del usuario
        user_input = input("Tú: ")

        if user_input.lower() == "salir":
            print("¡Adiós!")
            break

        # Agregar la entrada del usuario al historial
        conversation_history.append({"role": "user", "content": user_input})

        # Hacer la solicitud al modelo
        response = client.chat.completions.create(
            model="gpt-4o-mini",  # Asegúrate de usar el modelo correcto configurado en Azure
            messages=conversation_history
        )

        # Obtener la respuesta del modelo
        assistant_response = response.choices[0].message.content
        print(f"Asistente: {assistant_response}")

        # Agregar la respuesta del asistente al historial
        conversation_history.append({"role": "assistant", "content": assistant_response})

# Iniciar el chat
if __name__ == "__main__":
    chat_with_model()
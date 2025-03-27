import requests

# URL de tu webhook
url = "https://a6b9-187-189-50-8.ngrok-free.app/webhook/fa833c9e-f44a-44e5-9515-378505671975"

# Bucle infinito para recibir preguntas hasta que el usuario lo detenga
while True:
    # Solicitar al usuario que ingrese una pregunta
    mensaje = input("Escribe tu pregunta (o 'salir' para terminar): ")

    # Si el usuario ingresa 'salir', termina el bucle
    if mensaje.lower() == 'salir':
        print("Fin del programa.")
        break

    data = {"mensaje": mensaje}

    try:
        # Enviar la solicitud POST con el mensaje
        response = requests.post(url, json=data)
        response.raise_for_status()  # Si hay un error HTTP, lo detecta

        # Verificar si la respuesta tiene formato JSON
        if response.headers.get("Content-Type") == "application/json":
            # Obtener el JSON y extraer el campo 'respuesta'
            json_response = response.json()
            print("Respuesta de n8n:", json_response.get("respuesta", "No se recibió la respuesta esperada"))
        else:
            print(":", response.text)  # Si no es JSON, mostrar el texto recibido

    except requests.exceptions.RequestException as e:
        print(f"Error en la solicitud: {e}")

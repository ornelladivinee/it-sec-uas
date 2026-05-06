# Se define la función caesar_cipher con los parámetros text, key y mode
# - text: el mensaje ingresado por el usuario
# - key: número de desplazamiento del cifrado Caesar
# - mode: encrypt o decrypt

def caesar_cipher(text, key, mode):

    # Alfabeto usado en el cifrado
    alphabet = "abcdefghijklmnopqrstuvwxyz"

    # Aquí se almacena el resultado final
    result = ""

    # Aseguramos que la clave funcione dentro del rango del alfabeto
    key = key % 26

    # Recorremos cada carácter del texto
    for char in text:

        # Verificamos si el carácter es una letra
        if char.lower() in alphabet:

            # Encontramos su posición en el alfabeto
            index = alphabet.index(char.lower())

            # Si el modo es encrypt, sumamos la clave
            if mode == "encrypt":
                new_index = (index + key) % 26

            # Si es decrypt, restamos la clave
            else:
                new_index = (index - key) % 26

            # Obtenemos la nueva letra
            new_char = alphabet[new_index]

            # Mantener mayúsculas si existían
            if char.isupper():
                result += new_char.upper()
            else:
                result += new_char

        else:
            # Si no es letra, se deja igual
            result += char

    return result


## crear un bucle sin reiniciar 
while True:

    print("\n=== CAESAR CIPHER TOOL ===")

    # texto
    text = input("Enter text: ")

    # key con control de error
    while True:
        try:
            key = int(input("Enter key: "))
            break
        except ValueError:
            print("Error: key must be a number.")

    #  menú
    print("1. Encrypt")
    print("2. Decrypt")

    while True:
        option = input("Choose option (1 or 2): ")

        if option == "1":
            mode = "encrypt"
            break
        elif option == "2":
            mode = "decrypt"
            break
        else:
            print("Invalid option.")

    # resultado
    result = caesar_cipher(text, key, mode)
    print("Result:", result)

    # loop continuar o salir
    again = input("\nDo you want to continue? (y/n): ")
    
    # opcion de cierre

    if again.lower() != "y":
        print("Exiting program...")
        break


#### EJECUCIÓN FINAL ####

result = caesar_cipher(text, key, mode)

print("Result:", result)
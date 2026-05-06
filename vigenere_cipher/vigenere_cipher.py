# Función que implementa el cifrado y descifrado Vigenère
# - text: mensaje del usuario
# - key: palabra clave (ej: security)
# - mode: encrypt o decrypt

def vigenere_cipher(text, key, mode):

    # Alfabeto base
    alphabet = "abcdefghijklmnopqrstuvwxyz"

    result = ""

    # Convertimos la clave a minúsculas para estandarizar
    key = key.lower()

    # Índice para recorrer la clave
    key_index = 0

    # Recorremos cada carácter del texto
    for char in text:

        # Si es letra, la procesamos
        if char.lower() in alphabet:

            # Posición de la letra del texto
            text_index = alphabet.index(char.lower())

            # Posición de la letra de la clave (cíclica)
            key_char = key[key_index % len(key)]
            key_shift = alphabet.index(key_char)

            # Si es encrypt, sumamos el shift
            if mode == "encrypt":
                new_index = (text_index + key_shift) % 26

            # Si es decrypt, restamos el shift
            else:
                new_index = (text_index - key_shift) % 26

            # Nueva letra
            new_char = alphabet[new_index]

            # Mantener mayúsculas si existen
            if char.isupper():
                result += new_char.upper()
            else:
                result += new_char

            # Solo avanzamos la clave si la letra es válida
            key_index += 1

        else:
            # Si no es letra (espacios, símbolos), se mantiene igual
            result += char

    return result

## bucle para continuar sin reiniciar el programa ##
while True:

    print("\n=== VIGENERE CIPHER TOOL ===")

    # ingreso de texto
    text = input("Enter text: ")

    # ingreso de clave
    key = input("Enter key (word): ")

    # menú
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
            print("Invalid option. Try again.")

    # ejecutar cifrado
    result = vigenere_cipher(text, key, mode)
    print("Result:", result)

    # opción de continuar o salir
    again = input("\nDo you want to continue? (y/n): ")

    if again.lower() != "y":
        print("Exiting program...")
        break

# EJECUCIÓN

result = vigenere_cipher(text, key, mode)
print("Result:", result)

Caesar Cipher:
toma un texto
lo “mueve” en el alfabeto
ejemplo:
hello → khoor
Idea:
Cada letra se desplaza un número fijo (key).

Vigenère Cipher:
en vez de número, usas una palabra clave
ejemplo:
hello + security → texto cifrado distinto por letra
Idea:
Cada letra del texto se mueve diferente según la clave.

LÓGICA REAL DE SOFTWARE
Menús
1. Encrypt
2. Decrypt
interfaz de usuario básica (CLI)

Bucles
el programa no se cierra
puedes usarlo varias veces

Control de errores
Ejemplo:

try:
    key = int(input())
except:

evita que el programa se caiga si el usuario escribe mal


# IT Security Exercises – UAS FRA

This repository contains implementations of classical cryptographic algorithms developed as part of an IT Security course at UAS Frankfurt.

The goal of this project is to understand fundamental concepts of symmetric cryptography through practical implementation.

---

## Project Structure


it-sec-uas/
│
├── caesar_cipher/
│ └── caesar_cipher.py
│
├── vigenere_cipher/
│ └── vigenere_cipher.py
│
└── README.md


---

## Implemented Ciphers

### 1. Caesar Cipher
- Simple substitution cipher
- Shifts letters based on a numeric key
- Supports both encryption and decryption
- Includes infinite loop mode and input validation

### 2. Vigenère Cipher
- Polyalphabetic substitution cipher
- Uses a keyword instead of a numeric shift
- More secure than Caesar cipher
- Supports infinite loop interaction mode

---

## Features

- Interactive command-line interface (CLI)
- Input validation (error handling for invalid keys/options)
- Encryption and decryption modes
- Continuous execution loop (no restart needed)
- Preserves spaces, symbols, and letter casing

---

## How to Run

### Caesar Cipher
```bash
cd caesar_cipher
python3 caesar_cipher.py

### Vigenère Cipher
```bash
Vigenère Cipher
cd vigenere_cipher
python3 vigenere_cipher.py

Learning Objectives
Understanding classical encryption techniques
Implementing symmetric cryptography
Practicing secure coding principles
Handling user input safely
Working with CLI-based tools


👩‍💻 Author
Ornella Mesina.
IT Security Student – UAS Frankfurt

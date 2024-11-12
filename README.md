# BRUTEFORCEWEB-BETA

### **Instrucciones de Uso**

---

#### **1. Clonando el Repositorio**

Para comenzar a usar los scripts, primero necesitas clonar el repositorio **BRUTEFORCEWEB-BETA** desde GitHub. Abre tu terminal en **Termux** y ejecuta el siguiente comando:

```bash
git clone https://github.com/danissj45/BRUTEFORCEWEB-BETA.git
cd BRUTEFORCEWEB-BETA
```

---

#### **2. Creador de Diccionarios (gd.py)**

Este script te permite generar un diccionario de contraseñas en formato `.txt` que puedes utilizar con el script de ataque de fuerza bruta.

##### **Pasos para ejecutar el creador de diccionarios**:

1. **Instalar dependencias**:
   Asegúrate de tener Python instalado en **Termux** para ejecutar el script **gd.py**. Si no lo tienes, puedes instalarlo ejecutando:

   ```bash
   pkg install python
   ```

2. **Ejecutar el generador de diccionarios**:
   Navega al directorio del repositorio **BRUTEFORCEWEB-BETA** y ejecuta el siguiente comando para correr el script **gd.py**:

   ```bash
   python gd.py
   ```

3. **Configura el diccionario**:
   El script te pedirá varias opciones como:
   - La cantidad de contraseñas que quieres generar.
   - La longitud mínima y máxima de las contraseñas.
   - El tipo de caracteres a usar (números, letras, números y letras, o todos).
   - Si deseas incluir palabras relacionadas en las contraseñas.

   Después de seleccionar las opciones, el script generará el diccionario y lo guardará en un archivo `.txt`.

---

#### **3. Ataque de Fuerza Bruta (bruteforceweb.sh)**

Este script realiza un ataque de fuerza bruta a una página web, probando contraseñas desde un diccionario que hayas generado con el script **gd.py**.

##### **Pasos para ejecutar el ataque de fuerza bruta**:

1. **Haz que el script sea ejecutable**:
   Asegúrate de que **bruteforceweb.sh** tenga permisos de ejecución. Si no es así, ejecuta el siguiente comando:

   ```bash
   chmod +x bruteforceweb.sh
   ```

2. **Ejecutar el ataque**:
   A continuación, ejecuta el script **bruteforceweb.sh**:

   ```bash
   ./bruteforceweb.sh
   ```

3. **Seleccionar el diccionario**:
   El script te pedirá que selecciones un diccionario de contraseñas que hayas generado previamente con **gd.py**. Puedes elegirlo del directorio **diccionarios/**.

4. **Configurar el ataque**:
   Después de seleccionar el diccionario, el script te pedirá que ingreses los siguientes datos:
   - **URL** del objetivo al que deseas realizar el ataque.
   - **Nombre de usuario** que se usará en el ataque de fuerza bruta.
   - **Velocidad** del ataque (1-4, donde 4 es el más rápido, sin pausas).

   El ataque comenzará y probará cada contraseña del diccionario con el nombre de usuario proporcionado. Si una contraseña es correcta, se mostrará un mensaje de éxito.

---

### **Notas Importantes**:

- **El ataque de fuerza bruta está destinado solo para fines educativos y en entornos controlados.** No realices ataques a sitios web sin el permiso explícito del propietario.
- Asegúrate de usar los scripts de forma ética y legal.
- Si deseas detener el ataque, puedes presionar **Ctrl+C** en cualquier momento.
- El script de **bruteforceweb.sh** realiza un ataque a un formulario de login, por lo que debe estar configurado para que el POST a la URL funcione correctamente.

---

### **Resumen de Archivos**:

- **gd.py**: Creador de diccionarios de contraseñas.
  - Este script genera un archivo `.txt` con contraseñas aleatorias según las opciones que elijas (longitud, caracteres, cantidad, etc.).

- **bruteforceweb.sh**: Script de ataque de fuerza bruta.
  - Usa el diccionario generado por **gd.py** para intentar adivinar la contraseña en un formulario web, probando diferentes contraseñas hasta encontrar la correcta.

---

### **Ejemplo de Flujo**:

1. Ejecuta **gd.py** para generar un diccionario.
2. Ejecuta **bruteforceweb.sh** para realizar el ataque de fuerza bruta con el diccionario generado.

---

Si tienes alguna pregunta o necesitas ayuda adicional, ¡no dudes en contactar!

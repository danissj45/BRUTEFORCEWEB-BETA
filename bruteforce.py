from flask import Flask, render_template_string, request

app = Flask(__name__)

# Datos de acceso (usuario y contraseña correctos)
USUARIO_CORRECTO = "admin"
CONTRASENA_CORRECTA = "1234"

# Página HTML con formulario de login
pagina_html = """
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Login - Página de prueba</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f4f4f4;
            padding: 50px;
            text-align: center;
        }
        .login-box {
            width: 300px;
            margin: 0 auto;
            padding: 30px;
            background-color: white;
            border-radius: 8px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
        }
        input[type="text"], input[type="password"] {
            width: 100%;
            padding: 10px;
            margin: 10px 0;
            border: 1px solid #ccc;
            border-radius: 4px;
        }
        input[type="submit"] {
            background-color: #4CAF50;
            color: white;
            padding: 10px 20px;
            border: none;
            border-radius: 4px;
            cursor: pointer;
        }
        .error {
            color: red;
            font-weight: bold;
        }
    </style>
</head>
<body>
    <div class="login-box">
        <h2>Iniciar sesión</h2>
        <form method="POST">
            <input type="text" name="usuario" placeholder="Usuario" required><br>
            <input type="password" name="contraseña" placeholder="Contraseña" required><br>
            <input type="submit" value="Ingresar">
        </form>
        {% if error %}
            <p class="error">{{ error }}</p>
        {% endif %}
    </div>
</body>
</html>
"""

# Ruta principal
@app.route('/', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        usuario = request.form['usuario']
        contraseña = request.form['contraseña']
        if usuario == USUARIO_CORRECTO and contraseña == CONTRASENA_CORRECTA:
            return "<h1>¡Bienvenido, has iniciado sesión correctamente!</h1>"
        else:
            error = "Usuario o contraseña incorrectos."
    
    return render_template_string(pagina_html, error=error)

# Iniciar el servidor web
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

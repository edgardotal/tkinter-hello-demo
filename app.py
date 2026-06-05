"""
Hello World Web App - Flask Demo
Aplicación web simple para mostrar en la nube
Autor: Edgardo Talavera
"""

from flask import Flask, render_template_string

app = Flask(__name__)

# HTML de la página principal
HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>Hello World - Flask Demo</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            text-align: center;
            margin-top: 100px;
            background-color: #f0f0f0;
        }
        .container {
            background-color: white;
            padding: 40px;
            border-radius: 10px;
            width: 400px;
            margin: 0 auto;
            box-shadow: 0 0 10px rgba(0,0,0,0.1);
        }
        h1 {
            color: #2c3e50;
        }
        button {
            background-color: #e74c3c;
            color: white;
            border: none;
            padding: 10px 20px;
            font-size: 16px;
            border-radius: 5px;
            cursor: pointer;
        }
        button:hover {
            background-color: #c0392b;
        }
        .mensaje {
            color: #27ae60;
            margin-top: 20px;
            font-size: 18px;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Hello, World!</h1>
        <p>Bienvenido a mi demo de Flask</p>
        <button onclick="mostrarMensaje()">Haz clic aquí</button>
        <div id="mensaje" class="mensaje"></div>
    </div>
    
    <script>
        function mostrarMensaje() {
            document.getElementById('mensaje').innerHTML = '¡Botón clickeado! ✅';
        }
    </script>
</body>
</html>
"""

@app.route('/')
def home():
    """Página principal"""
    return render_template_string(HTML_TEMPLATE)

@app.route('/saludar')
def saludar():
    """API simple que devuelve JSON"""
    return {'mensaje': 'Hola desde Flask', 'status': 'ok'}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
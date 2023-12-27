from flask import Flask, render_template, request
import mysql.connector

app = Flask(__name__)

# Configura la conexión a la base de datos
db = mysql.connector.connect(
    host="34.135.195.20",
    user="root",
    password="kaoGxH%s'Q0o/8s+",
    database="practica3"
)

cursor = db.cursor()

#@app.route('/')
#def index():
#    return 'Página de inicio'

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Obtén las credenciales del formulario
        username = request.form['username']
        password = request.form['password']

        # Consulta para verificar las credenciales en la base de datos
        query = "SELECT * FROM usuarios WHERE username=%s AND password=%s"
        cursor.execute(query, (username, password))
        user = cursor.fetchone()

        if user:
            return f'¡Hola, {username}! Has iniciado sesión correctamente.'
        else:
            return 'Usuario o contraseña incorrectos. Inténtalo de nuevo.'

    return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
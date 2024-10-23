from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register_user', methods=['GET', 'POST'])
def register_user():
    if request.method == 'POST':
        # Aquí puedes manejar los datos del formulario
        email = request.form['email']
        dni = request.form['dni']
        nombre = request.form['nombre']
        apellidos = request.form['apellidos']
        fecha_nacimiento = request.form['fecha_nacimiento']
        # Guardar los datos en la base de datos o realizar alguna acción
        return redirect(url_for('index'))
    return render_template('register_user.html')

@app.route('/register_tutor', methods=['GET', 'POST'])
def register_tutor():
    if request.method == 'POST':
        # Aquí puedes manejar los datos del formulario
        email = request.form['email']
        dni = request.form['dni']
        nombre = request.form['nombre']
        apellidos = request.form['apellidos']
        fecha_nacimiento = request.form['fecha_nacimiento']
        usuario = request.form['usuario']
        # Guardar los datos en la base de datos o realizar alguna acción
        return redirect(url_for('index'))
    return render_template('register_tutor.html')

if __name__ == '__main__':
    app.run(debug=True)
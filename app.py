from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return '''
        <h2>Calculadora Web</h2>
        <form action="/calcular" method="post">
            <input type="number" name="num1" placeholder="Primer número" required>
            <select name="operador">
                <option value="suma">+</option>
                <option value="resta">-</option>
                <option value="multiplicacion">*</option>
                <option value="division">/</option>
            </select>
            <input type="number" name="num2" placeholder="Segundo número" required>
            <button type="submit">Calcular</button>
        </form>
    '''

@app.route('/calcular', methods=['POST'])
def calcular():
    num1 = float(request.form['num1'])
    num2 = float(request.form['num2'])
    operador = request.form['operador']
    resultado = None

    if operador == 'suma':
        resultado = num1 + num2
    elif operador == 'resta':
        resultado = num1 - num2
    elif operador == 'multiplicacion':
        resultado = num1 * num2
    elif operador == 'division':
        resultado = num1 / num2 if num2 != 0 else 'Indefinido'

    return f"<h3>Resultado: {resultado}</h3><a href='/'>Volver</a>"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

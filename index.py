from flask import Flask, render_template, request, redirect, url_for
import sqlite3
app = Flask(__name__)

@app.route('/')
def index(): #para los enlaces en html este es el nombre que reconoce
    
    return render_template ('home.html')

@app.route('/info')
def info():
    return render_template ('info.html')

@app.route('/calendario')
def calendario():
    return render_template('calendario.html')

@app.route('/juegos')
def juegos():
    return render_template('juegos.html')

@app.route('/casco_historico')
def casco_historico():
    return render_template('casco_historico.html')

@app.route('/ventanas_hierro')
def ventanas_hierro():
    return render_template('ventanas_hierro.html')

@app.route('/balcon_arcayas')
def balcon_arcayas():
    return render_template('balcon_arcayas.html')

@app.route('/museo_guadalupano')
def museo_guadalupano():
    return render_template('museo_guadalupano.html')



#Aqui esta la logica de los Quiz

# Función auxiliar para conectar a la DB
def get_db_connection():
    conn = sqlite3.connect('quiz.db')
    conn.row_factory = sqlite3.Row  # Crucial: permite usar p['pregunta'] en vez de p[1]
    return conn


@app.route('/cuestionario')
def cuestionario():
    db = get_db_connection()
    # Traemos todas las filas de la tabla preguntas
    lista_preguntas = db.execute('SELECT * FROM preguntas').fetchall()
    db.close()
    return render_template('juegos.html', preguntas=lista_preguntas)


@app.route('/verificar', methods=['POST'])
def verificar():
    puntos = 0
    db = get_db_connection()
    preguntas_db = db.execute('SELECT * FROM preguntas').fetchall()
    
    for p in preguntas_db:
        # Buscamos la respuesta que envió el usuario por el ID de la pregunta
        respuesta_usuario = request.form.get(str(p['id']))
        if respuesta_usuario == p['correcta']:
            puntos += 1
            
    db.close()
    return render_template('verificar_quiz.html')












if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
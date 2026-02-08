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
def centro_juegos():
    return render_template('centro_juegos.html')

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
#Preguntas del quiz




# Preguntas del quiz (puedes modificar estas)
QUIZ_QUESTIONS = [
    {
        "id": 1,
        "question": "¿En que año fue fundada la ciudad de Santa Ana de Coro por Juan de Ampies?",
        "options": ["1492", "1567", "1527", "1993"],
        "correct_answer": "1527"
    },
    {
        "id": 2,
        "question": "¿Cual es la caracteristica principal de la catedral de Coro ?",
        "options": ["Sus vitrales modernos traidos de Francia", "Tener una fachada hecha completamente de mármol", 
        "Ser la construccion más alta del país"
        , "Poseer muros de gran espesor y ser las más antiguas del contienente"],
        "correct_answer": "Poseer muros de gran espesor y ser las más antiguas del contienente"
    },
    {
        "id": 3,
        "question": "¿De donde provienen los detalles de herrería que dan nombre a la famosa edificacion Ventanas de Hierro?",
        "options": ["Ciudad de mexico", "Lisboa, Portugal", "Sevilla, España", "Ámsterdam, Países Bajos"],
        "correct_answer": "Sevilla, España"
    },
    {
        "id": 4,
        "question": "¿Que evento historico importante simboliza la Cruz de San Clemente?",
        "options": ["El final de la Guerra de Independencia", "La firma del acta de la UNESCO",
         "Lugar donde se ofició la primera misa", "La llegada del primer obispo de Venezuela"],
        "correct_answer": "Lugar donde se ofició la primera misa"
    },
    {
        "id": 5,
        "question": "¿Cual es la tecnica de construcción tradicionales se preservan activamente hoy en dia en Coro?",
        "options": ["Tallado de piedras volcánicas", "Uso de estructura de acero y hormigón", "Construcción en tierra (adobe y tapia)",
         "Arquitectura de vidrio y madera"],
        "correct_answer": "Construcción en tierra (adobe y tapia)"
    }
]


@app.route('/game')
def juegos():
    """Página principal del juego"""
    return render_template('juegos.html', questions=QUIZ_QUESTIONS)


@app.route('/submit', methods=['POST'])
def submit_quiz():
    """Procesa las respuestas del quiz"""
    score = 0
    total_questions = len(QUIZ_QUESTIONS)
    results = []
    
    for question in QUIZ_QUESTIONS:
        question_id = str(question['id'])
        user_answer = request.form.get(question_id, '')
        correct_answer = question['correct_answer']
        
        is_correct = user_answer == correct_answer
        if is_correct:
            score += 1
            
        results.append({
            'question': question['question'],
            'user_answer': user_answer,
            'correct_answer': correct_answer,
            'is_correct': is_correct
        })
    
    percentage = (score / total_questions) * 100
    
    return render_template('verificar_quiz.html', 
                         score=score, 
                         total=total_questions, 
                         percentage=percentage,
                         results=results)


@app.route('/restart')
def restart():
    """Reinicia el juego"""
    return redirect(url_for('juegos'))


#segundo juegos

# index.py - Añadir después de las rutas existentes


PALABRAS_SCRAMBLE = [
    {"palabra": "HIERRO", "mezclada": "IRHREO"},
    {"palabra": "ADOBE", "mezclada": "BADEO"},
    {"palabra": "BALCÓN", "mezclada": "ÓBLCNA"},
    {"palabra": "BARRO", "mezclada": "RBROA"},
    {"palabra": "ARTE", "mezclada": "ETAR"},
]


@app.route('/scramble')
def scramble():
    """Juego de palabras mezcladas"""
    return render_template('scramble.html', palabras=PALABRAS_SCRAMBLE)


@app.route('/verificar_scramble', methods=['POST'])
def verificar_scramble():
    """Verifica las respuestas del scramble"""
    correctas = 0
    resultados = []
    
    for i in range(len(PALABRAS_SCRAMBLE)):
        respuesta = request.form.get(f'respuesta_{i}', '').upper().strip()
        palabra_real = PALABRAS_SCRAMBLE[i]['palabra']
        mezclada = PALABRAS_SCRAMBLE[i]['mezclada']
        
        es_correcta = respuesta == palabra_real
        if es_correcta:
            correctas += 1
            
        resultados.append({
            'mezclada': mezclada,
            'respuesta': respuesta,
            'correcta': palabra_real,
            'es_correcta': es_correcta
        })
    
    return render_template('resultado_scramble.html',
                         correctas=correctas,
                         total=len(PALABRAS_SCRAMBLE),
                         resultados=resultados)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
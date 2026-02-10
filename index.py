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

@app.route('/restart')
def restart():
    return redirect(url_for('juegos'))  


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
    },

    
    {
        "id": 6,
        "question": "¿En qué año fue declarado el Casco Histórico de Coro y su Puerto de La Vela como Patrimonio de la Humanidad por la UNESCO?",
        "options": ["1990", "1993", "1999", "2005"],
        "correct_answer": "1993"
    },
    {
        "id": 7,
        "question": "¿Cuál es el nombre de la casa famosa por tener un portal tallado con la figura del 'Astro Rey'?",
        "options": ["Casa de los Arcaya", "Casa del Sol", "Casa del Tesoro", "Casa de las Ventanas de Hierro"],
        "correct_answer": "Casa del Sol"
    },
    {
        "id": 8,
        "question": "¿Qué influencia arquitectónica europea se mezcló con la española en Coro debido al comercio con las islas vecinas como Curazao?",
        "options": ["Francesa", "Inglesa", "Holandesa", "Italiana"],
        "correct_answer": "Holandesa"
    },
    {
        "id": 9,
        "question": "¿Cómo se llama la casa de dos plantas conocida por sus extensos balcones de madera que perteneció a una de las familias más influyentes?",
        "options": ["Casa de los Arcaya", "Casa del Obispo", "Casa de la Poesía", "Casa de los Senior"],
        "correct_answer": "Casa de los Arcaya"
    },
    {
        "id": 10,
        "question": "¿Qué madera local, conocida por su dureza, se utiliza tradicionalmente para las vigas de las casas coloniales corianas?",
        "options": ["Pino", "Cují", "Cedro", "Caobo"],
        "correct_answer": "Cují"
    },

    
    {
        "id": 11,
        "question": "¿Cómo se conoce popularmente a Coro debido a su estrecha relación con la fe católica y sus múltiples templos?",
        "options": ["La Ciudad de los Puertos", "La Ciudad Mariana", "La Ciudad de los Vientos", "La Atenas de Venezuela"],
        "correct_answer": "La Ciudad Mariana"
    },
    {
        "id": 12,
        "question": "¿Qué héroe de la independencia y expresidente de Venezuela nació en el estado Falcón y tiene una plaza importante en el casco histórico?",
        "options": ["Simón Bolívar", "José Antonio Páez", "Juan Crisóstomo Falcón", "Antonio José de Sucre"],
        "correct_answer": "Juan Crisóstomo Falcón"
    },
    {
        "id": 13,
        "question": "¿Qué nombre recibe el desierto de dunas que rodea la entrada a la ciudad de Coro?",
        "options": ["Médanos de Coro", "Dunas de Falcón", "Desierto de Ampíes", "Arenales de la Vela"],
        "correct_answer": "Médanos de Coro"
    },
    {
        "id": 14,
        "question": "¿En qué lugar de la ciudad se cree que se encuentra enterrado un tesoro real, dando pie a numerosas leyendas locales?",
        "options": ["En la Catedral", "En la Casa del Tesoro", "Bajo la Cruz de San Clemente", "En el Puerto de La Vela"],
        "correct_answer": "En la Casa del Tesoro"
    },
    {
        "id": 15,
        "question": "¿Cuál es el nombre de la familia de origen judío cuya casa es un hito arquitectónico y cultural en el casco histórico?",
        "options": ["Familia Senior", "Familia Smith", "Familia Gumersindo", "Familia Pinto"],
        "correct_answer": "Familia Senior"
    },
    {
        "id": 16,
        "question": "¿Qué elemento decorativo exterior, ubicado sobre las puertas, es típico para identificar las casas coloniales de Coro?",
        "options": ["Gárgolas de piedra", "Mosaicos romanos", "Tejaroces y portales tallados", "Estatua de bronce"],
        "correct_answer": "Tejaroces y portales tallados"
    },
    {
        "id": 17,
        "question": "¿Qué puerto, ubicado a pocos minutos de Coro, es parte integral de la zona declarada Patrimonio de la Humanidad?",
        "options": ["Puerto Cabello", "Puerto de La Vela", "Puerto de Adícora", "Puerto de Cumarebo"],
        "correct_answer": "Puerto de La Vela"
    },
    {
        "id": 18,
        "question": "¿Cómo se llama el cementerio judío de Coro, considerado el más antiguo de su tipo en uso continuo en América?",
        "options": ["Cementerio de los Mártires", "Cementerio Judío de Coro", "Panteón de Falcón", "Jardín de la Memoria"],
        "correct_answer": "Cementerio Judío de Coro"
    },
    {
        "id": 19,
        "question": "¿Qué material se mezcla con la tierra y la paja para dar el acabado liso y blanco a las paredes de las casas coloniales?",
        "options": ["Yeso", "Cal", "Cemento blanco", "Mármol pulverizado"],
        "correct_answer": "Cal"
        },

]



import random  # 
from flask import render_template, request, redirect, url_for, Flask



@app.route('/game')
def juegos():
    """Página principal del juego con solo 4 preguntas aleatorias"""
    preguntas_mezcladas = QUIZ_QUESTIONS.copy()
    random.shuffle(preguntas_mezcladas)
    
    # EL PUNTO ESPECÍFICO: Cortamos la lista para quedarnos solo con 4
    selección_final = preguntas_mezcladas[:4]
    
    for q in selección_final:
        # Copiamos las opciones para no mezclar las originales del JSON
        opciones = q['options'].copy()
        random.shuffle(opciones)
        q['options_shuffled'] = opciones # Guardamos una versión mezclada
        
    return render_template('juegos.html', questions=selección_final)

@app.route('/submit', methods=['POST'])
def submit_quiz():
    score = 0
    results = []
    
    # Obtenemos todos los IDs que el usuario respondió (que serán 4)
    # request.form tiene los IDs como llaves
    ids_respondidos = request.form.keys() 
    
    for question in QUIZ_QUESTIONS:
        question_id = str(question['id'])
        
        # Solo procesamos si el ID de esta pregunta está en las respuestas enviadas
        if question_id in ids_respondidos:
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
    
    # EL PUNTO ESPECÍFICO PARA EL CÁLCULO:
    total_respondidas = len(results) # Esto será 4
    percentage = (score / total_respondidas) * 100 if total_respondidas > 0 else 0
    
    return render_template('verificar_quiz.html', 
                         score=score, 
                         total=total_respondidas, 
                         percentage=percentage,
                         results=results)
#Segundo Quiz




#segundo juegos Sacrambble

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
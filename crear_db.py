import sqlite3


def inicializar_base_datos():
    # Se crea el archivo físico en tu carpeta
    conexion = sqlite3.connect('quiz.db')
    cursor = conexion.cursor()


    # Borramos la tabla si ya existe para evitar errores al probar
    cursor.execute('DROP TABLE IF EXISTS preguntas')


    # Creamos la tabla con las columnas necesarias
    cursor.execute('''
        CREATE TABLE preguntas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            pregunta TEXT NOT NULL,
            opcion_a TEXT NOT NULL,
            opcion_b TEXT NOT NULL,
            opcion_c TEXT NOT NULL,
            correcta TEXT NOT NULL
        )
    ''')


    # Insertamos algunas preguntas de ejemplo (A, B o C)
    preguntas = [
        ('¿Qué significa SQL?', 'Structured Query Language', 'Strong Question Language', 'Simple Query List', 'A'),
        ('¿En qué carpeta van los HTML en Flask?', 'static', 'templates', 'views', 'B'),
        ('¿Qué símbolo se usa para comentarios en Python?', '//', '/*', '#', 'C')
    ]


    cursor.executemany('INSERT INTO preguntas (pregunta, opcion_a, opcion_b, opcion_c, correcta) VALUES (?,?,?,?,?)', preguntas)
    
    conexion.commit()
    conexion.close()
    print("¡Base de datos 'quiz.db' creada con éxito!")


if __name__ == '__main__':
    inicializar_base_datos()
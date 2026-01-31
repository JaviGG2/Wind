from flask import Flask, render_template, url_for
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

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
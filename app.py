# Flask, WSGI libraries
from flask import Flask, render_template

# Configuratins and castom libraries
from config import CONFIG
from LibrarySiteElements import menu

# Blueprint block
from energy_quality.energy_quality import quality

# --- CONFIGURATION BLOCK ---

# SECRET_KEY = CONFIG['FLASK_SECRET_KEY']
app = Flask (__name__)
app.register_blueprint(quality, url_prefix='/quality')


# --- HEANDLERS BLOCK ---
@app.route('/')
def index():
    return render_template('index.html', title="Главная страница", menu=menu)


@app.route('/product')
def services():
    return render_template('product.html', title="Услуги", menu=menu)


@app.route('/objects')
def objects():
    return render_template('objects.html', title="Наши объекты", menu=menu)


@app.route('/contact')
def contact():
    return render_template('contact.html', title="Наши объекты", menu=menu)


if __name__ == "__main__":
    app.run(debug=True)
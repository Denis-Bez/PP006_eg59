# Other libraries

# Flask, WSGI libraries
from flask import Flask, render_template
from Class_SQLAlchemy import db, Menu

# Configuratins and castom libraries
from config import CONFIG

# # Blueprint block
from Quality.quality import quality
from Bushing.bushing import bushing

# --- CONFIGURATION BLOCK ---
app = Flask (__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///content.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

app.register_blueprint(quality, url_prefix='/quality') # A Subsite of "Power quality" business line
app.register_blueprint(bushing, url_prefix='/bushing') # A Subsite of "Transformer " business line


# --- HEANDLERS BLOCK ---
# Need to delete so many heandlers and do it dynamic generated. Remember DRY!


@app.route('/')
def index():
        menu = get_menu()
        if menu:
            return render_template('index.html', title="Главная страница", menu=menu)
        else:
            return render_template('error.html', title="Ошибка")


# Page with List of business activities
@app.route('/solutions')
def solutions():
    menu = get_menu()
    if menu:
        return render_template('solutions.html', title="Направления", menu=menu)
    else:
        return render_template('error.html', title="Ошибка")


# Page with company's products
@app.route('/product')
def product():
    menu = get_menu()
    if menu:
        return render_template('products.html', title="Продукция", menu=menu)
    else:
        return render_template('error.html', title="Ошибка")


# Page with infotmation about the company's completed works
@app.route('/objects')
def objects():
    menu = get_menu()
    if menu:
        return render_template('objects.html', title="Наши объекты", menu=menu)
    else:
        return render_template('error.html', title="Ошибка")


# Page with the company's contacts
@app.route('/contact')
def contact():
    menu = get_menu()
    if menu:
        return render_template('contact.html', title="Наши объекты", menu=menu)
    else:
        return render_template('error.html', title="Ошибка")


@app.route('/objects/<object>')
def object(object):
    menu = get_menu()
    if menu:
        return render_template('layout_object.html', menu=menu, object=object)
    else:
        return render_template('error.html', title="Ошибка")


# --- DATBASE CONTENT GETTING ---

def get_menu():
    try:
        res = Menu.query.filter_by(visibility='visible').order_by(Menu.priorities).all()
        return res 
    except:
        return False


def get_content():
    pass


# --- START SERVER ---
if __name__ == "__main__": 
    # db.create_all() # Uncomment For creating new tables
    app.run(debug=True)
    
    
    
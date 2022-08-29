# Other libraries

# Flask, WSGI libraries
from flask import Flask, render_template
from Class_SQLAlchemy import db, Menu, Solutions_menu, Product_menu

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
        content = get_all([Menu, Solutions_menu])
        if content:
            return render_template('index.html', title="Главная страница", menu=content[0], solution_menu=content[1])
        else:
            return render_template('error.html', title="Ошибка")


# Page with List of business activities
@app.route('/solutions')
def solutions():
    menu = get_all([Menu])
    if menu:
        return render_template('solutions.html', title="Направления", menu=menu)
    else:
        return render_template('error.html', title="Ошибка")


# Page with company's products
@app.route('/product')
def product():
    menu = get_all([Menu])
    if menu:
        return render_template('products.html', title="Продукция", menu=menu)
    else:
        return render_template('error.html', title="Ошибка")


# Page with infotmation about the company's completed works
@app.route('/objects')
def objects():
    content = get_all([Menu])
    if content:
        return render_template('objects.html', title="Наши объекты", menu=content[0])
    else:
        return render_template('error.html', title="Ошибка")


# Page with the company's contacts
@app.route('/contact')
def contact():
    content = get_all([Menu])
    if content:
        return render_template('contact.html', title="Наши объекты", menu=content[0])
    else:
        return render_template('error.html', title="Ошибка")


@app.route('/objects/<object>')
def object(object):
    menu = get_all([Menu])
    if menu:
        return render_template('layout_object.html', menu=menu, object=object)
    else:
        return render_template('error.html', title="Ошибка")


@app.route('/test')
def test():
    menu = get_all([Menu])
    content = get_content([Product_menu])
    return render_template('test.html', menu=menu[0], product_menu=content[0])


# --- DATBASE CONTENT GETTING ---

def get_all(tables):
    res = []
    try:
        for table in tables:
            res.append(table.query.filter_by(visibility='visible').order_by(table.priorities).all())
        return res 
    except:
        return False


def get_content(tables):
    res = []
    try:
        for table in tables:
            res.append(table.query.filter_by(visibility='visible', solutions_menu_id='1').order_by(table.priorities).all())
        return res 
    except:
        return False

# --- START SERVER ---
if __name__ == "__main__": 
    # db.create_all() # Uncomment For creating new tables
    app.run(debug=True)
    
    
    
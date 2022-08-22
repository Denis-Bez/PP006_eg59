from flask import Blueprint, render_template
from Class_SQLAlchemy import db, Menu, Product_menu

quality = Blueprint('quality', __name__, template_folder='templates', static_folder='static')


@quality.route('/')
def index():
    menu = get_menu()
    if menu:
        return render_template('index_quality.html', title='Главная качество энергии', menu=menu[0])
    else:
        return render_template('error.html', title="Ошибка")


@quality.route('/objects')
def objects():
    menu = get_menu()
    if menu:
        return render_template('index_quality.html', title='Главная качество энергии', menu=menu[0])
    else:
        return render_template('error.html', title="Ошибка")

@quality.route('/contact')
def contact():
    menu = get_menu()
    if menu:
        return render_template('index_quality.html', title='Главная качество энергии', menu=menu[0])
    else:
        return render_template('error.html', title="Ошибка")

@quality.route('/<name>')
def productCard(name):
    menu = get_menu()
    if menu:
        return render_template('layout_productCard.html', title='Карточка продукта', menu=menu[0], solutions_menu=menu[1])
    else:
        return render_template('error.html', title="Ошибка")

# --- DATBASE CONTENT GETTING ---

def get_menu():
    try:
        res1 = Menu.query.filter_by(visibility='visible').order_by(Menu.priorities).all()
        res2 = Product_menu.query.filter_by(visibility='visible', solutions_menu_id='1').order_by(Product_menu.priorities).all()
        return [res1, res2]
    except:
        return False

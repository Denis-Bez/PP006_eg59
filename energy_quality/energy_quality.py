from flask import Blueprint, render_template
from Class_SQLAlchemy import Menu, Drop_menu, db

quality = Blueprint('energy_quality', __name__, template_folder='templates', static_folder='static')


@quality.route('/')
def index():
    menu = get_menu()
    if menu:
        return render_template('index_quality.html', title='Главная качество энергии', menu=menu)
    else:
        return render_template('error.html', title="Ошибка")


@quality.route('/objects')
def objects():
    menu = get_menu()
    if menu:
        return render_template('index_quality.html', title='Главная качество энергии', menu=menu)
    else:
        return render_template('error.html', title="Ошибка")

@quality.route('/contact')
def contact():
    menu = get_menu()
    if menu:
        return render_template('index_quality.html', title='Главная качество энергии', menu=menu)
    else:
        return render_template('error.html', title="Ошибка")

@quality.route('/<name>')
def productCard(name):
    return render_template('layout_productCard.html', title='Карточка продукта', menu=get_menu())


# --- DATBASE CONTENT GETTING ---

def get_menu():
    try:
        res = Menu.query.filter_by(visibility='visible').order_by(Menu.priorities).all()
        return res
    except:
        return False

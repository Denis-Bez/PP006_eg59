from flask import Blueprint, render_template
from Class_SQLAlchemy import db, Menu, Product_menu, Solution

quality = Blueprint('quality', __name__, template_folder='templates', static_folder='static')


@quality.route('/')
def index():
    menu = get_menu()
    if menu:
        return render_template('layout_indexSolutions.html', title='Главная качество энергии', menu=menu[0], product_menu=menu[1], solutions=menu[2])
    else:
        return render_template('error.html', title="Ошибка")


@quality.route('/objects')
def objects():
    menu = get_menu()
    if menu:
        return render_template('layout_indexSolutions.html', title='Главная качество энергии', menu=menu[0])
    else:
        return render_template('error.html', title="Ошибка")

@quality.route('/contact')
def contact():
    menu = get_menu()
    if menu:
        return render_template('layout_indexSolutions.html', title='Главная качество энергии', menu=menu[0])
    else:
        return render_template('error.html', title="Ошибка")

@quality.route('/<name>')
def productCard(name):
    menu = get_menu()
    if menu:
        return render_template('layout_productCard.html', title='Карточка продукта', menu=menu[0], product_menu=menu[1], name=name)
    else:
        return render_template('error.html', title="Ошибка")


@quality.route('<product>/<property>')
def productCard(product, property):
    menu = get_menu()
    if menu:
        return render_template('layout_productCard.html', title='Карточка продукта', menu=menu[0], product_menu=menu[1])
    else:
        return render_template('error.html', title="Ошибка")


# --- DATBASE CONTENT GETTING ---
def get_menu():
    try:
        query_1 = Menu.query.filter_by(visibility='visible').order_by(Menu.priorities).all()
        query_2 = Product_menu.query.filter_by(visibility='visible', solutions_menu_id='1').order_by(Product_menu.priorities).all()
        query_3 = Solution.query.filter_by(visibility='visible', solutions_menu_id='1').first()
        return [query_1, query_2, query_3]
    except:
        return False

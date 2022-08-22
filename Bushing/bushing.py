from flask import Blueprint, render_template
from Class_SQLAlchemy import db, Product_menu

bushing = Blueprint('bushing', __name__, template_folder='templates', static_folder='static')


@bushing.route('/')
def index():
    menu = get_menu()
    if menu:
        return render_template('index.html', title='Главная качество энергии', menu=menu)
    else:
        return render_template('error.html', title="Ошибка")


# --- DATBASE CONTENT GETTING ---

def get_menu():
    try:
        res = Product_menu.query.filter_by(visibility='visible', solutions_menu_id='2').order_by(Product_menu.priorities).all()
        return res
    except:
        return False

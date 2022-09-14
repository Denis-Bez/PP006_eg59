from flask import Blueprint, render_template
from Class_SQLAlchemy import db, Menu, Product_menu, Solution, SEO

quality = Blueprint('quality', __name__, template_folder='templates', static_folder='static')


@quality.route('/')
def index():
    menu = get_menu()
    seo = get_seo('quality')
    if menu:
        return render_template('layout_indexSolutions.html', seo=seo, menu=menu[0], product_menu=menu[1], solutions=menu[2])
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

@quality.route('/<product>')
def productCard(product):
    menu = get_menu()
    seo = get_seo(product)
    if menu:
        return render_template('layout_productCard.html', menu=menu[0], product_menu=menu[1], seo=seo, url_name=product)
    else:
        return render_template('error.html')


@quality.route('<products>/<product>')
def productCards(products, product):
    menu = get_menu()
    seo = get_seo(product)
    if menu:
        return render_template('layout_productCard.html', menu=menu[0], product_menu=menu[1], seo=seo, single_product=True, url_name=product)
    else:
        return render_template('error.html')


# --- DATBASE CONTENT GETTING ---
def get_menu():
    try:
        query_1 = Menu.query.filter_by(visibility='visible').order_by(Menu.priorities).all()
        query_2 = Product_menu.query.filter_by(visibility='visible', solutions_menu_id='1').order_by(Product_menu.priorities).all()
        query_3 = Solution.query.filter_by(visibility='visible', solutions_menu_id='1').first()
        return [query_1, query_2, query_3]
    except:
        return False

def get_seo(url_name):
    try:
        res = SEO.query.filter_by(url_name=url_name).first()
        return res 
    except:
        return False

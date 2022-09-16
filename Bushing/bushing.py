from flask import Blueprint, render_template
from Class_SQLAlchemy import db, Menu, Product_menu, Solution, SEO

bushing = Blueprint('bushing', __name__, template_folder='templates', static_folder='static')


@bushing.route('/')
def index():
    content = get_content()
    seo = get_seo("bushing")
    if content:
        return render_template('layout_indexSolutions.html', seo=seo, menu=content[0], product_menu=content[1], solutions=content[2])
    else:
        return render_template('error.html', title="Ошибка")


@bushing.route('/<product>')
def productCard(product):
    content = get_content()
    seo = get_seo(product)
    if content:
        return render_template('layout_productCard.html', seo=seo, menu=content[0], product_menu=content[1], url_name=product)
    else:
        return render_template('error.html')


@bushing.route('<products>/<product>')
def productCards(products, product):
    content = get_content()
    seo = get_seo(product)
    if content:
        return render_template('layout_productCard.html', seo=seo, menu=content[0], product_menu=content[1], single_product=True, url_name=product)
    else:
        return render_template('error.html')


# --- DATBASE CONTENT GETTING ---
def get_content():
    try:
        query_1 = Menu.query.filter_by(visibility='visible').order_by(Menu.priorities).all()
        query_2 = Product_menu.query.filter_by(visibility='visible', solutions_menu_id='2').order_by(Product_menu.priorities).all()
        query_3 = Solution.query.filter_by(visibility='visible', solutions_menu_id='2').first()
        query_4 = SEO.query.filter_by(solutions_menu_id='1').all()
        return [query_1, query_2, query_3, query_4]
    except:
        return False


def get_seo(url_name):
    try:
        res = SEO.query.filter_by(url_name=url_name).first()
        return res 
    except:
        return False
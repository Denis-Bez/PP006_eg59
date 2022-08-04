from flask import Blueprint, render_template

from LibrarySiteElements import menu

quality = Blueprint('energy_quality', __name__, template_folder='templates', static_folder='static')

@quality.route('/')
def index():
    return render_template('index_quality.html', title='Главная качество энергии', menu=menu)

@quality.route('/services')
def services():
    return render_template('index_quality.html', title='Главная качество энергии', menu=menu)

@quality.route('/objects')
def objects():
    return render_template('index_quality.html', title='Главная качество энергии', menu=menu)

@quality.route('/contact')
def contact():
    return render_template('index_quality.html', title='Главная качество энергии', menu=menu)
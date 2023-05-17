# Other libraries
import re
import os.path

# Flask, WSGI libraries
from flask import Flask, render_template, request, redirect, flash
from flask_mail import Mail, Message
from Class_SQLAlchemy import Object, db, Menu, Solutions_menu, Product_menu, SEO

# Configuratins and castom libraries
from config import CONFIG
from spam_list import spam_filter

# # Blueprint block
from Quality.quality import quality
from Bushing.bushing import bushing
from Own.own import own

# --- CONFIGURATION BLOCK ---
application = Flask (__name__)

# Configurate abs path for database
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(BASE_DIR, "content.db")
application.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{db_path}'

application.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

application.config["SECRET_KEY"] = CONFIG["SECRET_KEY"]
application.config["MAIL_DEFAULT_SENDER"] = CONFIG["MAIL_DEFAULT_SENDER"]
application.config["MAIL_PASSWORD"] = CONFIG["MAIL_PASSWORD"]
application.config["MAIL_PORT"] = 465
application.config["MAIL_SERVER"] = "mail.eg-expert.ru"
application.config["MAIL_USE_TLS"] = False
application.config["MAIL_USE_SSL"] = True
application.config["MAIL_USERNAME"] = CONFIG["MAIL_USERNAME"]
mail = Mail(application)

db.init_app(application)

application.register_blueprint(quality, url_prefix='/quality') # A Subsite of "Power quality" business line
application.register_blueprint(bushing, url_prefix='/bushing') # A Subsite of "Transformer " business line
application.register_blueprint(own, url_prefix='/own') # A Subsite of "Own products " business line


# --- HEANDLERS BLOCK ---
# Need to delete so many heandlers and do it dynamic generated. Remember DRY!


@application.route('/')
def index():
        content = get_all([Menu, Solutions_menu])
        seo = get_seo('')
        for i in content[1]:
            print(i.title)
        if content and seo:
            return render_template('index.html', seo=seo, menu=content[0], solution_menu=content[1])
        else:
            return render_template('error.html', title="Ошибка")


# Page with List of business activities
@application.route('/solutions')
def solutions():
    menu = get_all([Menu])
    if menu:
        return render_template('solutions.html', title="Направления", menu=menu)
    else:
        return render_template('error.html', title="Ошибка")


# Page with company's products
@application.route('/product')
def product():
    menu = get_all([Menu])
    if menu:
        return render_template('products.html', title="Продукция", menu=menu)
    else:
        return render_template('error.html', title="Ошибка")


# Page with infotmation about the company's completed works
@application.route('/objects')
def objects():
    content = get_all([Menu, Object])
    seo = get_seo('objects')
    if content:
        return render_template('objects.html', seo=seo, menu=content[0], object_content=content[1])
    else:
        return render_template('error.html', title="Ошибка")


@application.route('/objects/<int:object>')
def object(object):
    content = get_all([Menu, Object])
    seo = get_seo('object')
    if content:
        return render_template('layout_object.html', seo=seo, menu=content[0], object_content=content[1], object=object)
    else:
        return render_template('error.html', title="Ошибка")


# Page with the company's contacts
@application.route('/contact')
def contact():
    content = get_all([Menu])
    seo = get_seo('contact')
    if content:
        return render_template('contact.html', seo=seo, menu=content[0])
    else:
        return render_template('error.html', title="Ошибка")


# Page with company's certificates
@application.route('/certificates')
def certificates():
    content = get_all([Menu])
    seo = get_seo('certificates')
    if content:
        return render_template('certificates.html', seo=seo, menu=content[0])
    else:
        return render_template('error.html', title="Ошибка")


# Privacy policy
@application.route('/privacy')
def privacy():
    content = get_all([Menu])
    seo = get_seo('privacy')
    if content:
        return render_template('privacy.html', seo=seo, menu=content[0])
    else:
        return render_template('error.html', title="Ошибка")


@application.route("/email", methods=["POST", "GET"])
def email():

    if request.method == "POST":
        # Getting client's date from form
        name = request.form.get("name")
        phone = request.form.get("phone")
        email = request.form.get("email")
        text = request.form.get("text")
        # Create text for sending message
        msg = Message("Заявка c сайта eg59.ru", recipients=["v417459@yandex.ru"])
        msg_client = Message("Заявка успешно отправлена", recipients=[email])
        msg_client.body = ("Мы получили заявку на экспертизу. Свяжемся с вами в ближайшее время для уточнения информации") 
        # Spam filter
        try:
            if not text:
                flash("Ошибка поле 'Текст заявки' не должно быть пустым! Попробуйте написать нам на почту office@eg59.ru или позвонить по телефону +7 (342) 200-85-05", category="danger")
                return redirect ("/")
            if text == '_':
                flash("Ошибка поле 'Текст заявки' не должно быть пустым! Попробуйте написать нам на почту office@eg59.ru или позвонить по телефону +7 (342) 200-85-05", category="danger")
                return redirect ("/")
            for spam_text in spam_filter["text"]:
                if re.search(spam_text, text):
                    flash("Заявка распознана системой как спам! Попробуйте написать нам на почту office@eg59.ru или позвонить по телефону +7 (342) 200-85-05", category="danger")
                    return redirect ("/")
            for spam_text in spam_filter["name"]:
                print(spam_text)
                if re.search(spam_text, name):
                    flash("Заявка распознана системой как спам! Попробуйте написать нам на почту office@eg59.ru или позвонить по телефону +7 (342) 200-85-05", category="danger")
                    return redirect ("/")
            for spam_text in spam_filter["email"]:
                print(spam_text)
                if re.search(spam_text, email):
                    flash("Заявка распознана системой как спам! Попробуйте написать нам на почту office@eg59.ru или позвонить по телефону +7 (342) 200-85-05", category="danger")
                    return redirect ("/")
        except Exception as e:
            msg_error = Message("Ошибка на сайте eg59.ru", recipients=["v417459@yandex.ru"])
            msg_error.body = ("Ошибка при работе спам-фильтра")
            flash("Ошибка при отправке заявки! Попробуйте написать нам на почту office@eg59.ru или позвонить по телефону +7 (342) 200-85-05", category="danger")
            mail.send(msg_error)
            print(f"Error: {e}")
            return redirect ("/")
        # Sending mail
        try:
            mail.send(msg_client)
            status = "Подтверждение на почту отправлено"
        except:
            status = "Подтверждение на почту не отправлено"
        msg.body = (f"Имя клиента: {name}\nТелефон клиента: {phone}\nEmail заявки: {email}\nТекст заявки: {text}\nСтатус отправки письма клиенту: {status}")      
        try:
            mail.send(msg)
            flash("Заявка успешно отправлена! Мы свяжемся с Вами в ближайшее время", category="success")
        except:
            flash("Произошла ошибка при отправке заявки. Попробуйте написать нам на почту expert@eg59.ru или позвонить по телефону +7 912-88-97-709", category="danger")        
    return redirect ("/")


# --- DATBASE CONTENT GETTING ---
def get_all(tables):
    res = []
    try:
        for table in tables:
            res.append(table.query.filter_by(visibility='visible').order_by(table.priorities).all())
        return res 
    except:
        return False


def get_seo(url_name):
    try:
        res = SEO.query.filter_by(url_name=url_name).first()
        return res 
    except:
        return False


# --- START SERVER ---
if __name__ == "__main__": 
    application.run(debug=True)
    
    
    
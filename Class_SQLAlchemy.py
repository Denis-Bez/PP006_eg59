from extensions import db


class Menu(db.Model):
    id = db.Column(db.Integer, unique=True, primary_key=True) 
    title = db.Column(db.String(100), nullable=False) # Button's text
    url = db.Column(db.String(100), nullable=False) # Button's link
    menu_name = db.Column(db.String(100), nullable=False) # mainmenu or menu of other business (power quality and other ...)
    visibility = db.Column(db.String(50), nullable=False) # Visible/Unvisible
    button_type = db.Column(db.String(50), nullable=False) # button or dropmenu
    priorities = db.Column(db.Integer) # To determine the position button in menu
    icon = db.Column(db.String(50), nullable=True)

    drop = db.relationship('Drop_menu', backref='menu', lazy=True)

    def __repr__(self):
        return f'<menu {self.id}>'  

class Drop_menu(db.Model):
    id = db.Column(db.Integer, unique=True, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    url = db.Column(db.String(100), nullable=False)
    visibility = db.Column(db.String(50), nullable=False)
    # Need invite!!! --> priorities = db.Column(db.Integer)

    menu_id = db.Column(db.Integer, db.ForeignKey('menu.id'), nullable=False)

    def __repr__(self):
        return f'<dropmenu {self.id}>'


# class Solution(db.Model):
#     pass


# class Product(db.Model):
#     pass


# class Image(db.Model):
#     pass


# class Objects(db.Model):
#     pass


# class SEO(db.Model):
#     pass


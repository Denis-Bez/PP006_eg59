from extensions import db


class Menu(db.Model):
    id = db.Column(db.Integer, unique=True, primary_key=True) 
    title = db.Column(db.String(100), nullable=False) # Button's text
    url = db.Column(db.String(100), nullable=True) # Button's link
    menu_name = db.Column(db.String(100), nullable=False) # mainmenu or menu of other business (power quality and other ...)
    visibility = db.Column(db.String(50), nullable=False) # Visible/Unvisible
    button_type = db.Column(db.String(50), nullable=False) # button or dropmenu
    priorities = db.Column(db.Integer) # To determine the position button in menu
    icon = db.Column(db.String(100), nullable=True)
    note = db.Column(db.String(100), nullable=True)

    solutions_menu = db.relationship('Solutions_menu', backref='menu', lazy=True)
    product_menu = db.relationship('Product_menu', backref='menu', lazy=True)

    def __repr__(self):
        return f'<menu {self.id}>'  


class Solutions_menu(db.Model):
    id = db.Column(db.Integer, unique=True, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    url = db.Column(db.String(100), nullable=False)
    menu_name = db.Column(db.String(100), nullable=False)
    visibility = db.Column(db.String(50), nullable=False)
    priorities = db.Column(db.Integer)
    button_type = db.Column(db.String(50), nullable=True)
    icon = db.Column(db.String(100), nullable=True)
    note = db.Column(db.String(100), nullable=True)

    menu_id = db.Column(db.Integer, db.ForeignKey('menu.id'), nullable=False)
    product_menu = db.relationship('Product_menu', backref='Solutions_menu', lazy=True)
    solution = db.relationship('Solution', backref='Solutions_menu', lazy=True)
    product = db.relationship('Solution', backref='Solutions_menu', lazy=True)


    def __repr__(self):
        return f'<solutions_menu {self.id}>'


class Product_menu(db.Model):
    id = db.Column(db.Integer, unique=True, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    url = db.Column(db.String(100), nullable=False)
    menu_name = db.Column(db.String(100), nullable=False)
    visibility = db.Column(db.String(50), nullable=False)
    priorities = db.Column(db.Integer)
    button_type = db.Column(db.String(50), nullable=True)
    icon = db.Column(db.String(100), nullable=True)
    note = db.Column(db.String(100), nullable=True)

    menu_id = db.Column(db.Integer, db.ForeignKey('menu.id'), nullable=False)
    solutions_menu_id = db.Column(db.Integer, db.ForeignKey('Solutions_menu.id'), nullable=False)
    property_menu = db.relationship('Property_menu', backref='product_menu', lazy=True)

    def __repr__(self):
        return f'<product_menu {self.id}>'


class Property_menu(db.Model):
    id = db.Column(db.Integer, unique=True, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    url = db.Column(db.String(100), nullable=False)
    menu_name = db.Column(db.String(100), nullable=False)
    visibility = db.Column(db.String(50), nullable=False)
    priorities = db.Column(db.Integer)
    button_type = db.Column(db.String(50), nullable=True)
    icon = db.Column(db.String(100), nullable=True)
    note = db.Column(db.String(100), nullable=True)

    menu_id = db.Column(db.Integer, db.ForeignKey('menu.id'), nullable=False)
    product_menu_id = db.Column(db.Integer, db.ForeignKey('product_menu.id'), nullable=False)

    def __repr__(self):
        return f'<property_menu {self.id}>'


class Solution(db.Model):
    
    solutions_menu_id = db.Column(db.Integer, db.ForeignKey('Solutions_menu.id'), nullable=False)

    def __repr__(self):
        return f'<solution {self.id}>'


class Product(db.Model):
    
    
    def __repr__(self):
        return f'<product {self.id}>'


class Product_property(db.Model):
    

    def __repr__(self):
        return f'<product_property {self.id}>'


class Objects(db.Model):
    
    # Может не быть связи с  Product или Solutions
    def __repr__(self):
        return f'<objects {self.id}>'


class SEO(db.Model):

    # Title
    # Discription
    
    def __repr__(self):
        return f'<seo {self.id}>'


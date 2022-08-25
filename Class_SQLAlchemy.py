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
    note = db.Column(db.String(200), nullable=True)

    solutions_menu = db.relationship('Solutions_menu', backref='menu', lazy=True)
    product_menu = db.relationship('Product_menu', backref='menu', lazy=True)

    def __repr__(self):
        return f'<menu {self.id}>'  


class Solutions_menu(db.Model):
    id = db.Column(db.Integer, unique=True, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    url = db.Column(db.String(100), nullable=False)
    menu_name = db.Column(db.String(100), nullable=False) # Correct to url_name and nullable=True
    visibility = db.Column(db.String(50), nullable=False)
    priorities = db.Column(db.Integer)
    button_type = db.Column(db.String(50), nullable=True)
    icon = db.Column(db.String(100), nullable=True)
    note = db.Column(db.String(100), nullable=True)

    menu_id = db.Column(db.Integer, db.ForeignKey('menu.id'), nullable=False)
    product_menu = db.relationship('Product_menu', backref='solutions_menu', lazy=True)
    solution = db.relationship('Solution', backref='solutions_menu', lazy=True)
    product = db.relationship('Product', backref='solutions_menu', lazy=True)
    property = db.relationship('Property_menu', backref='solutions_menu', lazy=True) # Need name - 'property_menu'
    objects = db.relationship('Objects', backref='solutions_menu', lazy=True)
    seo = db.relationship('SEO', backref='solutions_menu', lazy=True)

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
    solutions_menu_id = db.Column(db.Integer, db.ForeignKey('solutions_menu.id'), nullable=False)
    property_menu = db.relationship('Property_menu', backref='product_menu', lazy=True)
    product = db.relationship('Product', backref='product_menu', lazy=True)

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

    solutions_menu_id = db.Column(db.Integer, db.ForeignKey('solutions_menu.id'), nullable=True)
    product_menu_id = db.Column(db.Integer, db.ForeignKey('product_menu.id'), nullable=False)
    product = db.relationship('Product', backref='property_menu', lazy=True)
    seo = db.relationship('SEO', backref='property_menu', lazy=True)

    def __repr__(self):
        return f'<property_menu {self.id}>'


class Solution(db.Model):
    id = db.Column(db.Integer, unique=True, primary_key=True)
    index_content = db.Column(db.String(10000), nullable=True) # May be 20 000 symbols?
    title = db.Column(db.String(1000), nullable=True)
    short_discription = db.Column(db.String(2000), nullable=True)
    photo = db.Column(db.String(500), nullable=True)
    visibility = db.Column(db.String(50), nullable=False)
    priorities = db.Column(db.Integer)
    note = db.Column(db.String(200), nullable=True)
    
    solutions_menu_id = db.Column(db.Integer, db.ForeignKey('solutions_menu.id'), nullable=False)

    def __repr__(self):
        return f'<solution {self.id}>'


class Product(db.Model):
    id = db.Column(db.Integer, unique=True, primary_key=True)
    title = db.Column(db.String(1000), nullable=True)
    short_discription = db.Column(db.String(2000), nullable=True)
    url = db.Column(db.String(100), nullable=True)
    photo = db.Column(db.String(500), nullable=True)
    index_content = db.Column(db.String(10000), nullable=True) # Need more symbols (50 000 - 100 000)
    questionnaire = db.Column(db.String(4000), nullable=True)
    visibility = db.Column(db.String(50), nullable=False)
    priorities = db.Column(db.Integer)
    note = db.Column(db.String(200), nullable=True)
    
    solutions_menu_id = db.Column(db.Integer, db.ForeignKey('solutions_menu.id'), nullable=True)
    product_menu_id = db.Column(db.Integer, db.ForeignKey('product_menu.id'), nullable=True)
    property_menu_id = db.Column(db.Integer, db.ForeignKey('property_menu.id'), nullable=True)
    blocks = db.relationship('Blocks', backref='product', lazy=True)
    seo = db.relationship('SEO', backref='product', lazy=True)

    def __repr__(self):
        return f'<product {self.id}>'


# Delete
class Blocks(db.Model):
    id = db.Column(db.Integer, unique=True, primary_key=True)
    title = db.Column(db.String(1000), nullable=True)
    html_content = db.Column(db.String(10000), nullable=True)
    visibility = db.Column(db.String(50), nullable=False)
    priorities = db.Column(db.Integer)
    icon = db.Column(db.String(100), nullable=True)
    note = db.Column(db.String(200), nullable=True)
    
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'), nullable=True)
    
    def __repr__(self):
        return f'<blocks {self.id}>'


class Objects(db.Model):  
    id = db.Column(db.Integer, unique=True, primary_key=True)
    title = db.Column(db.String(1000), nullable=True)
    url = db.Column(db.String(100), nullable=True) # If doing separate pages
    content = db.Column(db.String(6000), nullable=True)
    photo = db.Column(db.String(500), nullable=True)
    visibility = db.Column(db.String(50), nullable=False)
    priorities = db.Column(db.Integer)
    note = db.Column(db.String(200), nullable=True)

    solutions_menu_id = db.Column(db.Integer, db.ForeignKey('solutions_menu.id'), nullable=True)
    seo = db.relationship('SEO', backref='objects', lazy=True)
    
    def __repr__(self):
        return f'<objects {self.id}>'


class SEO(db.Model):
    id = db.Column(db.Integer, unique=True, primary_key=True)
    title = db.Column(db.String(1000), nullable=True)
    discription = db.Column(db.String(3000), nullable=True)
    note = db.Column(db.String(2000), nullable=True)
    # Need invite 'url_name'

    solutions_menu_id = db.Column(db.Integer, db.ForeignKey('solutions_menu.id'), nullable=True)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'), nullable=True) # Need?
    property_menu_id = db.Column(db.Integer, db.ForeignKey('property_menu.id'), nullable=True)
    objects_id = db.Column(db.Integer, db.ForeignKey('objects.id'), nullable=True)
    
    def __repr__(self):
        return f'<seo {self.id}>'


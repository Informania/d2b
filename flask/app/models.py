from app import db

class Base(db.Model):
    __abstract__  = True

    id            = db.Column(db.Integer, primary_key=True)

class Product(Base):
    __tablename__   = 'product'
    name            = db.Column(db.String(150), unique=False)
    description     = db.Column(db.Text, unique=False)
    image           = db.Column(db.String(200), unique=False)
    url             = db.Column(db.String(100), unique=True)
    productGroup_id = db.Column(db.Integer, db.ForeignKey('productGroup.id'))
    productInfos    = db.relationship('ProductInfo', backref=db.backref('products'), lazy='dynamic')


    def __init__(self, name, description, image, productgroup, url):
        self.name           = name
        self.description    = description
        self.image          = image
        self.productgroup   = productgroup
        self.url            = url

    def __repr__(self):
        return '<User %r>' % self.name

class ProductGroup(Base):
    __tablename__   = 'productGroup'
    name            = db.Column(db.String(200), unique=False)
    image           = db.Column(db.String(150), unique=False)
    category_id     = db.Column(db.Integer, db.ForeignKey('productCategory.id'))
    products        = db.relationship('Product', backref=db.backref('productgroup'))
    url             = db.Column(db.String(100), unique=True)

    def __init__(self, name, image, category, url):
        self.name       = name
        self.image      = image
        self.category   = category
        self.url        = url
    

class ProductCategory(Base):
    __tablename__   = 'productCategory'
    name            = db.Column(db.String(200), unique=False)
    productGroups   = db.relationship('ProductGroup', backref=db.backref('category')) 
    def __init__(self, name):
        self.name = name

	def __repr__(self):
		return '<Category %r>' % self.name


class ProductInfo(Base):
    __tablename__   = 'productInfo'
    infoname_id     = db.Column(db.Integer, db.ForeignKey('infoName.id'))
    infoname        = db.relationship('InfoName', backref=db.backref('productinfo', lazy='dynamic'))
    value           = db.Column(db.String(50), unique=False)
    collection_id   = db.Column(db.Integer)
    product_id      = db.Column(db.Integer, db.ForeignKey('product.id'))

    def __init__(self, value, collectionId, infoname, product):
        self.infoname       = infoname
        self.value          = value
        self.collection_id  = collectionId
        self.product_id     = product.id

class InfoName(Base):
    __tablename__   = 'infoName'
    name            = db.Column(db.String(50), unique=True)
    order           = db.Column(db.Integer)

    def __init__(self, name, order):
        self.name   = name
        self.order  = order

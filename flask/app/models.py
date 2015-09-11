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
    productInfos    = db.relationship('ProductInfo', backref=db.backref('product'), lazy='joined')


    def __init__(self, name, description, image, productgroup, url):
        self.name           = name
        self.description    = description
        self.image          = image
        self.productgroup   = productgroup
        self.url            = url

    def __repr__(self):
        return '<Product %r>' % self.name

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
    
    def __repr__(self):
        return '<productGroup %r>' % self.name

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
    infoName_id     = db.Column(db.Integer, db.ForeignKey('infoName.id'))
    infoName        = db.relationship('InfoName', lazy='joined', foreign_keys='ProductInfo.infoName_id')
    value           = db.Column(db.String(50), unique=False)
    collection_id   = db.Column(db.Integer)
    product_id      = db.Column(db.Integer, db.ForeignKey('product.id'))

    def __init__(self, value, collectionId, infoName, product):
        self.infoName       = infoName
        self.value          = value
        self.collection_id  = collectionId
        self.product        = product

class InfoName(Base):
    __tablename__   = 'infoName'
    name            = db.Column(db.String(50), unique=True)
    order           = db.Column(db.Integer)
    
    def __init__(self, name, order):
        self.name   = name
        self.order  = order

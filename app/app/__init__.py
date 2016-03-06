from flask import Flask, render_template, jsonify
from flask.ext.sqlalchemy import SQLAlchemy
import operator
# 1: Define the WSGI application object
# 2: Set configurations
# 3: Define the database object which is imported
# by modules and controllers
app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)
db.text_factory = str
##from app import models, data
from models import *
# Sample HTTP error handling
@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404

# Import a module / component using its blueprint handler variable (mod_auth)
# from app.front_end.controllers import front_end as front_end
# ..

# Register blueprint(s)
# app.register_blueprint(front_end)
# app.register_blueprint(xyz_module)
# ..

# Build the database:
# This will create the database file using SQLAlchemy
db.drop_all()
db.create_all()
import data
data.CreateData()
#pc = ProductCategory('Distanser')
#db.session.add(pc)
#db.session.commit()



@app.route('/')
def home():
    return render_template('index.html')

@app.route('/produkter/')
def allProducts():
    productGroups = ProductGroup.query.all() 
    return render_template('product_groups.html', groups=productGroups)

@app.route('/produkter/add')
def addProduct():
    productGroups = ProductGroup.query.all()
    columns = InfoName.query.order_by(InfoName.order.asc()).all()
    return render_template('addProduct.html', groups=productGroups, columns=columns)


@app.route('/produkter/<category>')
def productGroups(category):
    pCat = ProductCategory.query.filter_by(name=category).first_or_404()
    productgroups = ProductGroup.query.filter_by(category=pCat).all()
    return render_template('product_groups.html', category=category, groups=productgroups) 

@app.route('/produkter/<category>/<productGroupUrl>/<productUrl>')
def productPage(category, productGroupUrl, productUrl):
    product = Product.query.filter_by(url=productUrl).first_or_404()
    # Get the unique headers for the table. InfoName is the name of the productInfo (cell in table)
    # Also fill a list with lists of productInfos as [['info', 'info], ['info, 'info']]
    infoNames = []
    #if product.productInfos:
    if product.productInfos:
        productInfos = [[] for _ in xrange(max(product.productInfos, key=operator.attrgetter('collection_id')).collection_id)]
        for productInfo in product.productInfos:
            productInfos[productInfo.collection_id-1].append(productInfo.value)

            if productInfo.infoName in infoNames:
                pass
            else:
                infoNames.append(productInfo.infoName)
        infoNames.sort(key=operator.attrgetter('order'), reverse=False)
        return render_template('product.html', product=product,
                tableHeaders=infoNames,
                tableRows=productInfos).encode('utf-8')
    else:
        return render_template('product.html', product=product,
                tableHeaders=infoNames,
                tableRows=[]).encode('utf-8')

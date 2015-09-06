from flask import Flask, render_template
from flask.ext.sqlalchemy import SQLAlchemy

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
    return render_template('product_groups.html')

@app.route('/produkter/<category>')
def productGroups(category):
    pCat = ProductCategory.query.filter_by(name=category).first_or_404()
    productgroups = ProductGroup.query.filter_by(category=pCat).all()
    return render_template('product_groups.html', category=category, groups=productgroups) 

@app.route('/produkter/<category>/<productGroupUrl>/<productUrl>')
def productPage(category, productGroupUrl, productUrl):
    product = Product.query.filter_by(url=productUrl).first_or_404()
    # Get the unique headers for the table
    infoNames = []
    for productInfo in product.productInfos:
        if productInfo.infoName.name in infoNames:
            pass
        else:
            infoNames.append(productInfo.infoName.name)

    ## TODO: infoNames needs to be sorted vy infoName.order to get in the right order.
    return render_template('product.html', product=product, tableHeaders=infoNames).encode('utf-8')

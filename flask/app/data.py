#!/usr/bin/python
# -*- coding: utf-8 -*-
from models import *
from app import db
def CreateData():
	
    pc = ProductCategory('Distanser')
    db.session.add(pc)
    pg = ProductGroup(u'Distanser för Mark', 'markdistans_varg.png', pc, u'Mark')
    db.session.add(pg)
    p = Product('Markdistans typ VARG', u'Den absolut största produkten sett till antalet som används för både lösarmering och armeringsnät. Fungerar lika bra på löst som fast/hårt underlag, viktigt att anläggningsytan är slät, så att markdistansen står stabilt mot underlaget. Det är också mycket viktigt att den är konstruerad i vädertåligt material och att den klarar hög belastning ovanifrån, då den bl.a. ska tåla en 120-kilos byggnadsarbetare som kliver i formen. <br/>Rekommenderat antal per kvadratmeter är 3-4 st.<br/>Kan även levereras i även i ”storpack”. <br/>Kontakta oss så löser vi det tillsammans med Er!', 'markdistans_varg.png', pg, 'Markdistans_varg')
    db.session.add(p)
    
    lagerstatus = InfoName('Lagerstatus', 20)
    antalforp = InfoName(u'Antal per förpackning', 19)
    hojd = InfoName(u'Höjd', 1)
    jarn = InfoName(u'Järn diameter', 4)
    
    db.session.add_all([
        lagerstatus, 
        antalforp,        
        hojd,
        jarn ])
    db.session.add_all([
        ProductInfo('Lagervara', 1, lagerstatus, p),
        ProductInfo('Lagervara', 2, lagerstatus, p),
        ProductInfo('Lagervara', 3, lagerstatus, p),
        ProductInfo('Lagervara', 4, lagerstatus, p),
        ProductInfo('Lagervara', 5, lagerstatus, p),
        ProductInfo('500', 1, antalforp, p),
        ProductInfo('500', 2, antalforp, p),
        ProductInfo('400 / 250*', 3, antalforp, p),
        ProductInfo('300', 4, antalforp, p),
        ProductInfo('125', 5, antalforp, p),
        ProductInfo('15/20', 1, hojd, p),
        ProductInfo('25/30', 2, hojd, p),
        ProductInfo('40/50', 3, hojd, p),
        ProductInfo('60/70', 4, hojd, p),
        ProductInfo('70/80', 5, hojd, p),
        ProductInfo('4-16', 1, jarn, p),
        ProductInfo('4-16', 2, jarn, p),
        ProductInfo('4-16', 3, jarn, p),
        ProductInfo('4-16', 4, jarn, p),
        ProductInfo('4-16', 5, jarn, p),

       ])

    #pg = ProductGroup('Valv', 'valvdistans_jarv.png', pc)
    #db.session.add(pg) 
    #pc = ProductCategory('Magneter')
    #db.session.add(pc)
    	
    
    
    db.session.commit()

#!/usr/bin/python
# -*- coding: utf-8 -*-
from models import *
from app import db
def CreateData():
    #####  ---- ProduktInfoNamn ----  #####
    lagerstatus = InfoName('Lagerstatus', 20)
    antalforpSt = InfoName(u'Antal per förpackning [st.]', 19)
    hojd = InfoName(u'Höjd [mm]', 1)
    jarn = InfoName(u'Järn diameter [mm]', 4)
    
    db.session.add_all([
        lagerstatus, 
        antalforpSt,        
        hojd,
        jarn ])


    #####  ---- Distanser ----  #####	
    pc = ProductCategory('Distanser')
    db.session.add(pc)
    ## Distanser för Mark ##
    pg = ProductGroup(u'Distanser för Mark', 'markdistans_varg.png', pc, u'Mark')
    db.session.add(pg)
    # Markdistans varg #
    p = Product('Markdistans typ VARG', u'Den absolut största produkten sett till antalet som används för både lösarmering och armeringsnät. Fungerar lika bra på löst som fast/hårt underlag, viktigt att anläggningsytan är slät, så att markdistansen står stabilt mot underlaget. Det är också mycket viktigt att den är konstruerad i vädertåligt material och att den klarar hög belastning ovanifrån, då den bl.a. ska tåla en 120-kilos byggnadsarbetare som kliver i formen. <br/>Rekommenderat antal per kvadratmeter är 3-4 st.<br/>Kan även levereras i även i ”storpack”. <br/>Kontakta oss så löser vi det tillsammans med Er!', 'markdistans_varg.png', pg, 'Markdistans_varg')
    db.session.add(p)
 
    db.session.add_all([
        ProductInfo('15/20', 1, hojd, p),
        ProductInfo('25/30', 2, hojd, p),
        ProductInfo('40/50', 3, hojd, p),
        ProductInfo('60/70', 4, hojd, p),
        ProductInfo('70/80', 5, hojd, p),
        ProductInfo('90/100', 6, hojd, p),
        ProductInfo('110/120', 7, hojd, p),
        ProductInfo('130/140', 8, hojd, p),
        ProductInfo('4-16', 1, jarn, p),
        ProductInfo('4-16', 2, jarn, p),
        ProductInfo('4-16', 3, jarn, p),
        ProductInfo('4-16', 4, jarn, p),
        ProductInfo('4-16', 5, jarn, p),
        ProductInfo('4-16', 6, jarn, p),
        ProductInfo('4-16', 7, jarn, p),
        ProductInfo('4-16', 8, jarn, p),
        ProductInfo('500', 1, antalforpSt, p),
        ProductInfo('500', 2, antalforpSt, p),
        ProductInfo('400 / 250*', 3, antalforpSt, p),
        ProductInfo('300', 4, antalforpSt, p),
        ProductInfo('125', 5, antalforpSt, p),
        ProductInfo('100', 6, antalforpSt, p),
        ProductInfo('-', 7, antalforpSt, p),
        ProductInfo('-', 8, antalforpSt, p),
        ProductInfo('Lagervara', 1, lagerstatus, p),
        ProductInfo('Lagervara', 2, lagerstatus, p),
        ProductInfo('Lagervara', 3, lagerstatus, p),
        ProductInfo('Lagervara', 4, lagerstatus, p),
        ProductInfo('Lagervara', 5, lagerstatus, p),
        ProductInfo('Lagervara', 6, lagerstatus, p),
        ProductInfo('Ring oss', 7, lagerstatus, p),
        ProductInfo('Ring oss', 8, lagerstatus, p)
       ])
        
    ## Distanser för valv ##
    pg = ProductGroup(u'Distanser för Valv', 'valvdistans_jarv.png', pc, u'Valv')

    # VäggValvdistans Järv #
    p = Product(u'Vägg- och Valvdistans JÄRV', u'Denna distans har funnits i många olika och varierande utformningar, alla med sina egna goda egenskaper och fördelar. <br/> I mitten på 90 talet satte sig “Mr Distans” ner och försökte samla alla dess goda egenskaper i en distans. Resultatet blev Varianten, som genom åren har visat sig vara just den bästa och mest användbara vägg- och valvdistansen. Den används mot hårt underlag både på valv och i väggar, och passar likväl för lösarmering såsom armeringsnät. <br/>Vi tillverkar den i ett material som tål både värme och kyla. Rekommenderat antal per kvadratmeter är 3-4 st. <br/><br/>Höjderna 20/25, 30/35 och 40/45 finns numera även i regranulerat material. Den har samma hållfasthet fast färgen är mer mellangrå. Eftersom det är regranulerat (återanvänt) material innebär det lite lägre pris och mindre mijlöpåverkan.', 'valvdistans_jarv.png', pg, 'Vagg_valvdistans_jarv')
    db.session.add(p)
    db.session.add_all([
        ProductInfo('15/20', 1, hojd, p),        
        ProductInfo('20/25', 2, hojd, p),        
        ProductInfo('30/35', 3, hojd, p),        
        ProductInfo('40/45', 4, hojd, p),        
        ProductInfo('50/55', 5, hojd, p),
        ProductInfo('4-16', 1, jarn, p),
        ProductInfo('4-16', 2, jarn, p),
        ProductInfo('4-16', 3, jarn, p),
        ProductInfo('4-16', 4, jarn, p),
        ProductInfo('4-16', 5, jarn, p),
        ProductInfo('1000', 1, antalforpSt, p),
        ProductInfo('1700', 2, antalforpSt, p),
        ProductInfo('1500', 3, antalforpSt, p),
        ProductInfo('1300', 4, antalforpSt, p),
        ProductInfo('500', 5, antalforpSt, p),
        ProductInfo('Ring oss', 1, lagerstatus, p),
        ProductInfo('Lagervara', 2, lagerstatus, p),
        ProductInfo('Lagervara', 3, lagerstatus, p),
        ProductInfo('Lagervara', 4, lagerstatus, p),
        ProductInfo('Lagervara', 5, lagerstatus, p)
    ])
    db.session.commit()

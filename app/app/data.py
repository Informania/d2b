#!/usr/bin/python
# -*- coding: utf-8 -*-
from models import *
from app import db
def CreateData():
    #####  ---- ProduktInfoNamn ----  #####
    lagerstatus = InfoName('Lagerstatus', 20)
    antalforpSt = InfoName(u'Antal per förpackning [st.]', 19)
    antalForpPall = InfoName(u'Antal per förpackning / pall [st.]', 18)
    hojd = InfoName(u'Höjd [mm]', 1)
    jarn = InfoName(u'Järn diameter [mm]', 4)
    
    db.session.add_all([
        lagerstatus, 
        antalforpSt,        
        hojd,
		antalForpPall,
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
    # Distanslister för mark # 
    p = Product(u'Distanslister för mark', u'Samma användningsområde som markdistansen. Passar dock bättre för nät än för lösarmering. Läggs ut i längder direkt på underlaget, därefter läggs nätet ovanpå. Enkelt och mindre risk för olämpliga arbetsställningar.<br/>Skall kapas i längder under 1 meter innan utläggning sker, och bör ej läggas i långa rader efter varandra. Det bästa är att ha en förskjutning i sidled. Görs inte detta är det stor risk att man skapar sprickanvisningar i den platta man gjuter. <br/>Rekommenderas cirka 1 meter per kvadratmeter.<br/>Levereras i längder om 2 meter. Kapade längder kan levereras på begäran. ', 'distanslist_mark.png', pg, 'Distanslist_mark')
    db.session.add(p)
    db.session.add_all([
        ProductInfo('15', 1, hojd, p),
        ProductInfo('20', 2, hojd, p),
        ProductInfo('25', 3, hojd, p),
        ProductInfo('30', 4, hojd, p),
        ProductInfo('35', 5, hojd, p),
        ProductInfo('40', 6, hojd, p),
        ProductInfo('50', 7, hojd, p),
        ProductInfo('60', 8, hojd, p),
        ProductInfo('70', 9, hojd, p),
        ProductInfo('50', 1, antalForpPall, p),
        ProductInfo('50 / 3150', 2, antalForpPall, p),
        ProductInfo('50 / 2100', 3, antalForpPall, p),
        ProductInfo('50 / 1800', 4, antalForpPall, p),
        ProductInfo('30 / 1200', 5, antalForpPall, p),
        ProductInfo('30 / 1200', 6, antalForpPall, p),
        ProductInfo('30 / 720', 7, antalForpPall, p),
        ProductInfo('20', 8, antalForpPall, p),
        ProductInfo('20', 9, antalForpPall, p),
		ProductInfo('Lagervara', 1, lagerstatus, p),
        ProductInfo('Lagervara', 2, lagerstatus, p),
        ProductInfo('Lagervara', 3, lagerstatus, p),
        ProductInfo('Lagervara', 4, lagerstatus, p),
        ProductInfo('Lagervara', 5, lagerstatus, p),
        ProductInfo('Lagervara', 6, lagerstatus, p),
        ProductInfo('Lagervara', 7, lagerstatus, p),
        ProductInfo('Ring oss', 8, lagerstatus, p),
        ProductInfo('Ring oss', 9, lagerstatus, p),
		
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

    # Valdistans Bock #
    p = Product(u'Valvdistans BOCK', u'Allmänt kallad sågbock på grund av sin likhet med denna, dock lite mindre till formatet. Genom sin storlek och anliggningsyta passar den bra inom prefabindustrin, att den sedan är billig försämrar ju inte saken.<br />Levereras förpackade i påse.', 'valvdistans_bock.png', pg, 'Valvdistans_bock')
    db.session.add(p)
    db.session.add_all([
        ProductInfo('15', 1, hojd, p),        
        ProductInfo('20', 2, hojd, p),        
        ProductInfo('25', 3, hojd, p),        
        ProductInfo('30', 4, hojd, p),        
        ProductInfo('35', 5, hojd, p),
        ProductInfo('40', 6, hojd, p),
        ProductInfo('45', 7, hojd, p),
        ProductInfo('50', 8, hojd, p),
        ProductInfo('6-12', 1, jarn, p),
        ProductInfo('6-12', 2, jarn, p),
        ProductInfo('6-12', 3, jarn, p),
        ProductInfo('6-12', 4, jarn, p),
        ProductInfo('6-12', 5, jarn, p),
        ProductInfo('6-12', 6, jarn, p),
        ProductInfo('6-12', 7, jarn, p),
        ProductInfo('6-12', 8, jarn, p),
        ProductInfo('500', 1, antalforpSt, p),
        ProductInfo('500', 2, antalforpSt, p),
        ProductInfo('500', 3, antalforpSt, p),
        ProductInfo('500', 4, antalforpSt, p),
        ProductInfo('250', 5, antalforpSt, p),
        ProductInfo('250', 6, antalforpSt, p),
        ProductInfo('125', 7, antalforpSt, p),
        ProductInfo('125', 8, antalforpSt, p),
        ProductInfo('Ring oss', 1, lagerstatus, p),
        ProductInfo('Lagervara', 2, lagerstatus, p),
        ProductInfo('Lagervara', 3, lagerstatus, p),
        ProductInfo('Lagervara', 4, lagerstatus, p),
        ProductInfo('Ring oss', 5, lagerstatus, p),
        ProductInfo('Ring oss', 6, lagerstatus, p),
        ProductInfo('Ring oss', 7, lagerstatus, p),
        ProductInfo('Ring oss', 8, lagerstatus, p),
    ])

    # Valvdistans VBOCK #
    p = Product(u'Valvdistans VBOCK', u'Förstärkt version av Bock, sätts endast på ett järn, passar ej i krysset.', 'valvdistans_vbock.png', pg, 'Valvdistans_vbock')
    db.session.add(p)
    db.session.add_all([
        ProductInfo('15', 1, hojd, p),        
        ProductInfo('20', 2, hojd, p),        
        ProductInfo('25', 3, hojd, p),        
        ProductInfo('30', 4, hojd, p),         
        ProductInfo('4-15', 1, jarn, p),
        ProductInfo('4-15', 2, jarn, p),
        ProductInfo('4-15', 3, jarn, p),
        ProductInfo('4-15', 4, jarn, p),
        ProductInfo('850', 1, antalforpSt, p),
        ProductInfo('650', 2, antalforpSt, p),
        ProductInfo('550', 3, antalforpSt, p),
        ProductInfo('450', 4, antalforpSt, p),
        ProductInfo('Lagervara', 1, lagerstatus, p),
        ProductInfo('Lagervara', 2, lagerstatus, p),
        ProductInfo('Lagervara', 3, lagerstatus, p),
        ProductInfo('Lagervara', 4, lagerstatus, p),
    ])

    # Valvdistans PRAXI #
    p = Product(u'Valvdistans PRAXI', u'Välkant fyrbening som är spikbar i alla ben samt i centrum. Används framförallt vid tung armering.', 'valvdistans_vbock.png', pg, 'Valvdistans_praxi')
    db.session.add(p)
    db.session.add_all([
        ProductInfo('15', 1, hojd, p),        
        ProductInfo('20', 2, hojd, p),        
        ProductInfo('25', 3, hojd, p),        
        ProductInfo('30', 4, hojd, p),        
        ProductInfo('35', 5, hojd, p),        
        ProductInfo('40', 6, hojd, p),        
        ProductInfo('45', 7, hojd, p),        
        ProductInfo('50', 8, hojd, p),        
        ProductInfo('6-20', 1, jarn, p),
        ProductInfo('6-20', 2, jarn, p),
        ProductInfo('6-20', 3, jarn, p),
        ProductInfo('6-20', 4, jarn, p),
        ProductInfo('6-20', 5, jarn, p),
        ProductInfo('6-20', 6, jarn, p),
        ProductInfo('6-20', 7, jarn, p),
        ProductInfo('6-20', 8, jarn, p),
        ProductInfo('1000', 1, antalforpSt, p),
        ProductInfo('1000', 2, antalforpSt, p),
        ProductInfo('1000', 3, antalforpSt, p),
        ProductInfo('1000', 4, antalforpSt, p),
        ProductInfo('650', 5, antalforpSt, p),
        ProductInfo('600', 6, antalforpSt, p),
        ProductInfo('550', 7, antalforpSt, p),
        ProductInfo('500', 8, antalforpSt, p),
        ProductInfo('Ring oss', 1, lagerstatus, p),
        ProductInfo('Lagervara', 2, lagerstatus, p),
        ProductInfo('Lagervara', 3, lagerstatus, p),
        ProductInfo('Lagervara', 4, lagerstatus, p),
        ProductInfo('Ring oss', 5, lagerstatus, p),
        ProductInfo('Ring oss', 6, lagerstatus, p),
        ProductInfo('Ring oss', 7, lagerstatus, p),
        ProductInfo('Ring oss', 8, lagerstatus, p),
    ])


    


    db.session.commit()


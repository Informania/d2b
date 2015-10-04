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
    langdCm = InfoName(u'Längd [cm]', 3) 
    db.session.add_all([
        lagerstatus, 
        antalforpSt,        
        hojd,
	antalForpPall,
        jarn,
        langdCm
    ])


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
    p = Product(u'Valvdistans PRAXI', u'Välkant fyrbening som är spikbar i alla ben samt i centrum. Används framförallt vid tung armering.', 'valvdistans_praxi.png', pg, 'Valvdistans_praxi')
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

    # Vägg- och valdistans GEMINI #
    p = Product(u'Vägg- och Valvdistans GEMINI', u'Den distans med högsta täckskikt som finns på marknaden. Mycket kraftig vilket medför att den tål hög belastning.<br/>Används oftast för att distansera överkantsarmering.<br/>Kan grensla över en underkantsarmering och runda fötter ger liten anliggningsyta.<br/>Mycket bra betongomslutning.', 'vagg_valvdistans_gemini.png', pg, 'Vagg_valvdistans_gemini')
    db.session.add(p)
    db.session.add_all([
        ProductInfo('60', 1, hojd, p),        
        ProductInfo('65', 2, hojd, p),        
        ProductInfo('70', 3, hojd, p),        
        ProductInfo('75', 4, hojd, p),        
        ProductInfo('80', 5, hojd, p),        
        ProductInfo('85', 6, hojd, p),        
        ProductInfo('90', 7, hojd, p),        
        ProductInfo('100/100', 8, hojd, p),        
        ProductInfo('110/120', 9, hojd, p),        
        ProductInfo('120/130', 10, hojd, p),        
        ProductInfo('140/150', 11, hojd, p),        
        ProductInfo('160/170', 12, hojd, p),        
        ProductInfo('4-24', 1, jarn, p),
        ProductInfo('4-24', 2, jarn, p),
        ProductInfo('4-24', 3, jarn, p),
        ProductInfo('4-24', 4, jarn, p),
        ProductInfo('4-24', 5, jarn, p),
        ProductInfo('4-24', 6, jarn, p),
        ProductInfo('4-24', 7, jarn, p),
        ProductInfo('4-24', 8, jarn, p),
        ProductInfo('4-24', 9, jarn, p),
        ProductInfo('4-24', 10, jarn, p),
        ProductInfo('4-24', 11, jarn, p),
        ProductInfo('4-24', 12, jarn, p),
        ProductInfo('250', 1, antalforpSt, p),
        ProductInfo('250', 2, antalforpSt, p),
        ProductInfo('250', 3, antalforpSt, p),
        ProductInfo('250', 4, antalforpSt, p),
        ProductInfo('250', 5, antalforpSt, p),
        ProductInfo('250', 6, antalforpSt, p),
        ProductInfo('200', 7, antalforpSt, p),
        ProductInfo('150', 8, antalforpSt, p),
        ProductInfo('150', 9, antalforpSt, p),
        ProductInfo('-', 10, antalforpSt, p),
        ProductInfo('100', 11, antalforpSt, p),
        ProductInfo('75', 12, antalforpSt, p),
        ProductInfo('Ring oss', 1, lagerstatus, p),
        ProductInfo('Ring oss', 2, lagerstatus, p),
        ProductInfo('Ring oss', 3, lagerstatus, p),
        ProductInfo('Ring oss', 4, lagerstatus, p),
        ProductInfo('Ring oss', 5, lagerstatus, p),
        ProductInfo('Ring oss', 6, lagerstatus, p),
        ProductInfo('Ring oss', 7, lagerstatus, p),
        ProductInfo('Ring oss', 8, lagerstatus, p),
        ProductInfo('Ring oss', 9, lagerstatus, p),
        ProductInfo('Ring oss', 10, lagerstatus, p),
        ProductInfo('Ring oss', 11, lagerstatus, p),
        ProductInfo('Ring oss', 12, lagerstatus, p),
    ])

    # Igelkott ENKEL # 
    p = Product(u'Igelkott ENKEL', u'Används som valvdistanser på stålunderlag.<br/>Läggs ut i formen, nätarmeringen läggs direkt ovanpå. Skapar bra arbetsmiljö med få böjningar. Risker finns dock för halkolyckor om man går i formen vid utläggningen. Några fördelar mot ringarna är att det är lättare att nå ut i hörnen samt att den är enklare att använda där det är smalt. <br/>Mått: 90 x 195 mm.', 'igelkott_enkel.png', pg, 'Igelkott_enkel')
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
        ProductInfo('9720', 1, antalForpPall, p),
        ProductInfo('9720', 2, antalForpPall, p),
        ProductInfo('9720', 3, antalForpPall, p),
        ProductInfo('9720', 4, antalForpPall, p),
        ProductInfo('9720', 5, antalForpPall, p),
        ProductInfo('9720', 6, antalForpPall, p),
        ProductInfo('9720', 7, antalForpPall, p),
        ProductInfo('9720', 8, antalForpPall, p),
        ProductInfo('Lagervara', 1, lagerstatus, p),
        ProductInfo('Lagervara', 2, lagerstatus, p),
        ProductInfo('Lagervara', 3, lagerstatus, p),
        ProductInfo('Lagervara', 4, lagerstatus, p),
        ProductInfo('Lagervara', 5, lagerstatus, p),
        ProductInfo('Ring oss', 6, lagerstatus, p),
        ProductInfo('Ring oss', 7, lagerstatus, p),
        ProductInfo('Ring oss', 8, lagerstatus, p),
    ])

    # Igelkott DUBBEL # 
    p = Product(u'Igelkott ENKEL', u'Används som Igelkott ENKEL.<br/>Mått: 195 x 195 mm', 'igelkott_dubbel.png', pg, 'Igelkott_dubbel')
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
        ProductInfo('4860/3240', 1, antalForpPall, p),
        ProductInfo('4860/3240', 2, antalForpPall, p),
        ProductInfo('4860/3240', 3, antalForpPall, p),
        ProductInfo('4860/3240', 4, antalForpPall, p),
        ProductInfo('4860/3240', 5, antalForpPall, p),
        ProductInfo('4860/3240', 6, antalForpPall, p),
        ProductInfo('4860/3240', 7, antalForpPall, p),
        ProductInfo('4860/3240', 8, antalForpPall, p),
        ProductInfo('Lagervara', 1, lagerstatus, p),
        ProductInfo('Lagervara', 2, lagerstatus, p),
        ProductInfo('Lagervara', 3, lagerstatus, p),
        ProductInfo('Lagervara', 4, lagerstatus, p),
        ProductInfo('Lagervara', 5, lagerstatus, p),
        ProductInfo('Lagervara', 6, lagerstatus, p),
        ProductInfo('Lagervara', 7, lagerstatus, p),
        ProductInfo('Lagervara', 8, lagerstatus, p),
    ])

    # Distanslist VESSLA # 
    p = Product(u'Distanslist VESSLA', u'Distanslist av typ Druzack. Fungerar mycket bra inom prefabindustrin, mot hårda underlag och på isolering om inte det blir för tung belastning. Kan naturligtvis även användas vid platsgjutning.<br/>Är hopkopplingsbar, även i vinkel upp till ca 30 grader, vilket gör det möjligt att bygga sin egen speciallist som bland annat kan gå runt hörn. Har fått sitt namn av att det är en smidig och slingrig typ.', 'distanslist_vessla.png', pg, 'Distanslist_vessla')
    db.session.add(p)
    db.session.add_all([
        ProductInfo('25', 1, hojd, p),        
        ProductInfo('30', 2, hojd, p),        
        ProductInfo('35', 3, hojd, p),        
        ProductInfo('40', 4, hojd, p),        
        ProductInfo('45', 5, hojd, p),        
        ProductInfo('50', 6, hojd, p),        
        ProductInfo('67', 1, langdCm, p),
        ProductInfo('67', 2, langdCm, p),
        ProductInfo('67', 3, langdCm, p),
        ProductInfo('67', 4, langdCm, p),
        ProductInfo('67', 5, langdCm, p),
        ProductInfo('67', 6, langdCm, p),
        ProductInfo('Ring oss', 1, lagerstatus, p),
        ProductInfo('Ring oss', 2, lagerstatus, p),
        ProductInfo('Ring oss', 3, lagerstatus, p),
        ProductInfo('Ring oss', 4, lagerstatus, p),
        ProductInfo('Ring oss', 5, lagerstatus, p),
        ProductInfo('Ring oss', 6, lagerstatus, p),
    ])
    
    # Distanslist VESSLA # 
    p = Product(u'Distanslist BÄVER', u'Distanslist av Quicktyp. Har mycket liten anliggningsyta tack vare sina små och spetsiga fötter. Är hopkopplingsbar, dock inte vinklingsbar. <br/>Har fått sitt namn av en kvinnlig fabriksägare, som tyckte att läppen som används för att koppla ihop dem med såg ut som en Bäversvans.<br/>Standardlängd 50 cm, finns i höjderna 15 till 60 mm.<br/>Kan levereras i sammansatta längder om 100, 150 eller 200 cm.', 'distanslist_baver.png', pg, 'Distanslist_baver')
    db.session.add(p)

    db.session.commit()


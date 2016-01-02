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
    jarn = InfoName(u'Järn diameter [mm]', 5)
    ror = InfoName(u'Rör-diameter [mm]', 5)
    langdCm = InfoName(u'Längd [cm]', 3)
    langdMm = InfoName(u'Längd [mm]', 4)
    farg = InfoName(u'Färgkod', 7)
    forIsolering = InfoName(u'För isolering [mm]', 8)
    tackskikt = InfoName(u'Täckskikt [mm]', 2)
    db.session.add_all([
        lagerstatus, 
        antalforpSt,        
        hojd,
	antalForpPall,
        jarn,
        langdCm,
        farg,
        langdMm,
        forIsolering,
        tackskikt
    ])


    #####  ---- Distanser ----  #####	
    pc = ProductCategory('Distanser')
    db.session.add(pc)
    ## Distanser för Mark ##
    pg = ProductGroup(u'Distanser för Mark', '1_markdistans_varg.png', pc, u'Mark')
    db.session.add(pg)
    # Markdistans varg #
    p = Product('Markdistans typ VARG', u'Den absolut största produkten sett till antalet som används för både lösarmering och armeringsnät. Fungerar lika bra på löst som fast/hårt underlag, viktigt att anläggningsytan är slät, så att markdistansen står stabilt mot underlaget. Det är också mycket viktigt att den är konstruerad i vädertåligt material och att den klarar hög belastning ovanifrån, då den bl.a. ska tåla en 120-kilos byggnadsarbetare som kliver i formen. <br/>Rekommenderat antal per kvadratmeter är 3-4 st.<br/>Kan även levereras i även i ”storpack”. <br/>Kontakta oss så löser vi det tillsammans med Er!', '1_markdistans_varg.png', pg, 'Markdistans_varg')
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
    p = Product(u'Distanslister för mark', u'Samma användningsområde som markdistansen. Passar dock bättre för nät än för lösarmering. Läggs ut i längder direkt på underlaget, därefter läggs nätet ovanpå. Enkelt och mindre risk för olämpliga arbetsställningar.<br/>Skall kapas i längder under 1 meter innan utläggning sker, och bör ej läggas i långa rader efter varandra. Det bästa är att ha en förskjutning i sidled. Görs inte detta är det stor risk att man skapar sprickanvisningar i den platta man gjuter. <br/>Rekommenderas cirka 1 meter per kvadratmeter.<br/>Levereras i längder om 2 meter. Kapade längder kan levereras på begäran. ', '20_distanslister_for_mark.png', pg, 'Distanslist_mark')
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
    pg = ProductGroup(u'Distanser för Valv', '2_vagg_valvdistans_jarv.png', pc, u'Valv')

    # VäggValvdistans Järv #
    p = Product(u'Vägg- och Valvdistans JÄRV', u'Denna distans har funnits i många olika och varierande utformningar, alla med sina egna goda egenskaper och fördelar. <br/> I mitten på 90 talet satte sig “Mr Distans” ner och försökte samla alla dess goda egenskaper i en distans. Resultatet blev Varianten, som genom åren har visat sig vara just den bästa och mest användbara vägg- och valvdistansen. Den används mot hårt underlag både på valv och i väggar, och passar likväl för lösarmering såsom armeringsnät. <br/>Vi tillverkar den i ett material som tål både värme och kyla. Rekommenderat antal per kvadratmeter är 3-4 st. <br/><br/>Höjderna 20/25, 30/35 och 40/45 finns numera även i regranulerat material. Den har samma hållfasthet fast färgen är mer mellangrå. Eftersom det är regranulerat (återanvänt) material innebär det lite lägre pris och mindre mijlöpåverkan.', 'valvdistans_jarv.png', pg, '2_vagg_valvdistans_jarv.png')
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
    p = Product(u'Valvdistans BOCK', u'Allmänt kallad sågbock på grund av sin likhet med denna, dock lite mindre till formatet. Genom sin storlek och anliggningsyta passar den bra inom prefabindustrin, att den sedan är billig försämrar ju inte saken.<br />Levereras förpackade i påse.', '14_valvdistans_bock.png', pg, 'Valvdistans_bock')
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
    p = Product(u'Valvdistans VBOCK', u'Förstärkt version av Bock, sätts endast på ett järn, passar ej i krysset.', '64_valvdistans_vbock.png', pg, 'Valvdistans_vbock')
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
    p = Product(u'Valvdistans PRAXI', u'Välkant fyrbening som är spikbar i alla ben samt i centrum. Används framförallt vid tung armering.', '51_valvdistans_praxi.png', pg, 'Valvdistans_praxi')
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
    p = Product(u'Vägg- och Valvdistans GEMINI', u'Den distans med högsta täckskikt som finns på marknaden. Mycket kraftig vilket medför att den tål hög belastning.<br/>Används oftast för att distansera överkantsarmering.<br/>Kan grensla över en underkantsarmering och runda fötter ger liten anliggningsyta.<br/>Mycket bra betongomslutning.', '30_valvdistans_gemini.png', pg, 'Vagg_valvdistans_gemini')
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
    p = Product(u'Igelkott ENKEL', u'Används som valvdistanser på stålunderlag.<br/>Läggs ut i formen, nätarmeringen läggs direkt ovanpå. Skapar bra arbetsmiljö med få böjningar. Risker finns dock för halkolyckor om man går i formen vid utläggningen. Några fördelar mot ringarna är att det är lättare att nå ut i hörnen samt att den är enklare att använda där det är smalt. <br/>Mått: 90 x 195 mm.', '53_igelkott_enkel.png', pg, 'Igelkott_enkel')
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
    p = Product(u'Igelkott DUBBEL', u'Används som Igelkott ENKEL.<br/>Mått: 195 x 195 mm', '22_igelkott_dubbel.png', pg, 'Igelkott_dubbel')
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
        ProductInfo('4860 / 3240', 1, antalForpPall, p),
        ProductInfo('4860 / 3240', 2, antalForpPall, p),
        ProductInfo('4860 / 3240', 3, antalForpPall, p),
        ProductInfo('4860 / 3240', 4, antalForpPall, p),
        ProductInfo('4860 / 3240', 5, antalForpPall, p),
        ProductInfo('4860 / 3240', 6, antalForpPall, p),
        ProductInfo('4860 / 3240', 7, antalForpPall, p),
        ProductInfo('4860 / 3240', 8, antalForpPall, p),
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
    p = Product(u'Distanslist VESSLA', u'Distanslist av typ Druzack. Fungerar mycket bra inom prefabindustrin, mot hårda underlag och på isolering om inte det blir för tung belastning. Kan naturligtvis även användas vid platsgjutning.<br/>Är hopkopplingsbar, även i vinkel upp till ca 30 grader, vilket gör det möjligt att bygga sin egen speciallist som bland annat kan gå runt hörn. Har fått sitt namn av att det är en smidig och slingrig typ.', '65_distanslist_vessla.png', pg, 'Distanslist_vessla')
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
        ProductInfo('Ring oss', 6, lagerstatus, p)
    ])
    
    # Distanslist BÄVER # 
    p = Product(u'Distanslist BÄVER', u'Distanslist av Quicktyp. Har mycket liten anliggningsyta tack vare sina små och spetsiga fötter. Är hopkopplingsbar, dock inte vinklingsbar. <br/>Har fått sitt namn av en kvinnlig fabriksägare, som tyckte att läppen som används för att koppla ihop dem med såg ut som en Bäversvans.<br/>Kan levereras i sammansatta längder om 100, 150 eller 200 cm.', '9_distanslist_baver.png', pg, 'Distanslist_baver')
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
        ProductInfo('55', 9, hojd, p),        
        ProductInfo('60', 10, hojd, p),        
        ProductInfo('50', 1, langdCm, p),
        ProductInfo('50', 2, langdCm, p),
        ProductInfo('50', 3, langdCm, p),
        ProductInfo('50', 4, langdCm, p),
        ProductInfo('50', 5, langdCm, p),
        ProductInfo('50', 6, langdCm, p),
        ProductInfo('50', 7, langdCm, p),
        ProductInfo('50', 8, langdCm, p),
        ProductInfo('50', 9, langdCm, p),
        ProductInfo('50', 10, langdCm, p),
        ProductInfo('Ring oss', 1, lagerstatus, p),
        ProductInfo('Ring oss', 2, lagerstatus, p),
        ProductInfo('Ring oss', 3, lagerstatus, p),
        ProductInfo('Ring oss', 4, lagerstatus, p),
        ProductInfo('Ring oss', 5, lagerstatus, p),
        ProductInfo('Ring oss', 6, lagerstatus, p),
        ProductInfo('Ring oss', 7, lagerstatus, p),
        ProductInfo('Ring oss', 8, lagerstatus, p),
        ProductInfo('Ring oss', 9, lagerstatus, p),
        ProductInfo('Ring oss', 10, lagerstatus, p)
    ])
    
    # Armeringsstege KOBRA # 
    p = Product(u'Armeringsstege KOBRA', u'Sinusformad armeringsstege, består av två längsgående vågformade armeringsjärn som hålls samman av vertikal tråd.<br/>Används vid dubbelarmering, läggs ovanpå lägsta armeringsnätet, nästa nät läggs ovanpå armeringsstegen. Rekommenderat är att armeringsstegen surras fast med najtråd i det undre nätet.<br/>Rekommenderat antal är 1 meter per kvadratmeter. Levereras i längder om 2 meter.', '40_armeringsstege_kobra.png', pg, 'Armeringsstege_kobra')
    db.session.add(p)
    db.session.add_all([
        ProductInfo('30', 1, hojd, p),        
        ProductInfo('40', 2, hojd, p),        
        ProductInfo('50', 3, hojd, p),        
        ProductInfo('60', 4, hojd, p),        
        ProductInfo('70', 5, hojd, p),        
        ProductInfo('80', 6, hojd, p),        
        ProductInfo('90', 7, hojd, p),        
        ProductInfo('100', 8, hojd, p),        
        ProductInfo('110', 9, hojd, p),        
        ProductInfo('120', 10, hojd, p),        
        ProductInfo('130', 11, hojd, p),        
        ProductInfo('140', 12, hojd, p),        
        ProductInfo('150', 13, hojd, p),        
        ProductInfo('160', 14, hojd, p),        
        ProductInfo('170', 15, hojd, p),        
        ProductInfo('180', 16, hojd, p),        
        ProductInfo('190', 17, hojd, p),        
        ProductInfo('200', 18, hojd, p),        
        ProductInfo('220', 19, hojd, p),        
        ProductInfo('240', 20, hojd, p),        
        ProductInfo('260', 21, hojd, p),        
        ProductInfo('280', 22, hojd, p),        
        ProductInfo('300', 23, hojd, p),        
        ProductInfo('400', 24, hojd, p),        
        ProductInfo('25 / 2000', 1, antalforpSt, p),
        ProductInfo('25 / 2000', 2, antalforpSt, p),
        ProductInfo('25 / 1500', 3, antalforpSt, p),
        ProductInfo('25 / 1500', 4, antalforpSt, p),
        ProductInfo('25 / 1000', 5, antalforpSt, p),
        ProductInfo('25 / 1000', 6, antalforpSt, p),
        ProductInfo('25 / 1000', 7, antalforpSt, p),
        ProductInfo('25 / 900', 8, antalforpSt, p),
        ProductInfo('25 / 800', 9, antalforpSt, p),
        ProductInfo('25 / 700', 10, antalforpSt, p),
        ProductInfo('25 / 600', 11, antalforpSt, p),
        ProductInfo('25 / 600', 12, antalforpSt, p),
        ProductInfo('25 / 600', 13, antalforpSt, p),
        ProductInfo('25 / 500', 14, antalforpSt, p),
        ProductInfo('25 / 500', 15, antalforpSt, p),
        ProductInfo('25 / 500', 16, antalforpSt, p),
        ProductInfo('25 / 500', 17, antalforpSt, p),
        ProductInfo('25 / 400', 18, antalforpSt, p),
        ProductInfo('25 / 400', 19, antalforpSt, p),
        ProductInfo('25 / 300', 20, antalforpSt, p),
        ProductInfo('25 / 300', 21, antalforpSt, p),
        ProductInfo('25 / 300', 22, antalforpSt, p),
        ProductInfo('25 / 300', 23, antalforpSt, p),
        ProductInfo('25 / 200', 24, antalforpSt, p),
        ProductInfo('Lagervara', 1, lagerstatus, p),
        ProductInfo('Lagervara', 2, lagerstatus, p),
        ProductInfo('Lagervara', 3, lagerstatus, p),
        ProductInfo('Lagervara', 4, lagerstatus, p),
        ProductInfo('Lagervara', 5, lagerstatus, p),
        ProductInfo('Lagervara', 6, lagerstatus, p),
        ProductInfo('Lagervara', 7, lagerstatus, p),
        ProductInfo('Lagervara', 8, lagerstatus, p),
        ProductInfo('Lagervara', 9, lagerstatus, p),
        ProductInfo('Lagervara', 10, lagerstatus, p),
        ProductInfo('Lagervara', 11, lagerstatus, p),
        ProductInfo('Lagervara', 12, lagerstatus, p),
        ProductInfo('Lagervara', 13, lagerstatus, p),
        ProductInfo('Lagervara', 14, lagerstatus, p),
        ProductInfo('Lagervara', 15, lagerstatus, p),
        ProductInfo('Lagervara', 16, lagerstatus, p),
        ProductInfo('Ring oss', 17, lagerstatus, p),
        ProductInfo('Lagervara', 18, lagerstatus, p),
        ProductInfo('Ring oss', 19, lagerstatus, p),
        ProductInfo('Ring oss', 20, lagerstatus, p),
        ProductInfo('Ring oss', 21, lagerstatus, p),
        ProductInfo('Ring oss', 22, lagerstatus, p),
        ProductInfo('Ring oss', 23, lagerstatus, p),
        ProductInfo('Ring oss', 24, lagerstatus, p),
    ])

    # Nätstöd typ A # 
    p = Product(u'Nätstöd typ A', u'Rak armeringsstege, består av tre längsgående armeringsjärn som hålls samman av vågformad, längsgående tråd.<br/>Används vid dubbelarmering, läggs direkt ovanpå undre armeringsnätet, nästa nät läggs därefter ovanpå armeringsstegen. Rekommenderat är att armeringsstegen surras fast med najtråd i det undre nätet.<br/>Rekommenderat antal är 1 meter per kvadratmeter. Levereras i längder om 2 meter.', '17_natstod_typ_a.png', pg, 'Natstod_typ_A')
    db.session.add(p)
    
    db.session.add_all([
        ProductInfo('50', 1, hojd, p),        
        ProductInfo('60', 2, hojd, p),        
        ProductInfo('70', 3, hojd, p),        
        ProductInfo('80', 4, hojd, p),        
        ProductInfo('90', 5, hojd, p),        
        ProductInfo('100', 6, hojd, p),        
        ProductInfo('110', 7, hojd, p),        
        ProductInfo('120', 8, hojd, p),        
        ProductInfo('130', 9, hojd, p),        
        ProductInfo('140', 10, hojd, p),        
        ProductInfo('150', 11, hojd, p),        
        ProductInfo('160', 12, hojd, p),        
        ProductInfo('170', 13, hojd, p),        
        ProductInfo('180', 14, hojd, p),        
        ProductInfo('200', 15, hojd, p),        
        ProductInfo('220', 16, hojd, p),        
        ProductInfo('50', 1, antalforpSt, p),
        ProductInfo('50', 2, antalforpSt, p),
        ProductInfo('50', 3, antalforpSt, p),
        ProductInfo('50', 4, antalforpSt, p),
        ProductInfo('50', 5, antalforpSt, p),
        ProductInfo('50', 6, antalforpSt, p),
        ProductInfo('50', 7, antalforpSt, p),
        ProductInfo('50', 8, antalforpSt, p),
        ProductInfo('50', 9, antalforpSt, p),
        ProductInfo('50', 10, antalforpSt, p),
        ProductInfo('50', 11, antalforpSt, p),
        ProductInfo('50', 12, antalforpSt, p),
        ProductInfo('50', 13, antalforpSt, p),
        ProductInfo('50', 14, antalforpSt, p),
        ProductInfo('50', 15, antalforpSt, p),
        ProductInfo('50', 16, antalforpSt, p),
        ProductInfo('Lagervara', 1, lagerstatus, p),
        ProductInfo('Lagervara', 2, lagerstatus, p),
        ProductInfo('Lagervara', 3, lagerstatus, p),
        ProductInfo('Lagervara', 4, lagerstatus, p),
        ProductInfo('Lagervara', 5, lagerstatus, p),
        ProductInfo('Lagervara', 6, lagerstatus, p),
        ProductInfo('Lagervara', 7, lagerstatus, p),
        ProductInfo('Lagervara', 8, lagerstatus, p),
        ProductInfo('Lagervara', 9, lagerstatus, p),
        ProductInfo('Lagervara', 10, lagerstatus, p),
        ProductInfo('Lagervara', 11, lagerstatus, p),
        ProductInfo('Lagervara', 12, lagerstatus, p),
        ProductInfo('Lagervara', 13, lagerstatus, p),
        ProductInfo('Lagervara', 14, lagerstatus, p),
        ProductInfo('Lagervara', 15, lagerstatus, p),
        ProductInfo('Lagervara', 16, lagerstatus, p),
    ])

     # Distanslister för valv # 
    p = Product(u'Distanslister för valv', u'Samma användningsområde som valvdistansen. Passar dock bättre för nät än för lösarmering.<br/>Läggs ut i längder direkt på underlaget, därefter läggs nätet ovanpå. Enkelt och mindre risk för olämpliga arbetsställningar.<br/>Skall kapas i längder under 1 meter innan utläggning sker, och bör ej läggas i långa rader efter varandra. Det bästa är att ha en förskjutning i sidoled. Görs inte detta är det stor risk att man skapar sprickanvisningar i den platta man gjuter. <br/>Rekommenderat antal cirka 1 meter per kvadratmeter. Levereras i längder om 2 meter. Kapade längder kan levereras på begäran.', '19_distansliste_for_valv.png', pg, 'Distanslist_valv')
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

    # Distansspiral # 
    p = Product(u'Distansspiral', u'Samma användningsområde som valvdistansen. Passar dock bättre för nät- än för lösarmering.<br/>Läggs ut i längder direkt på underlaget, därefter läggs nätet ovanpå. Enklare och mindre risk för olämpliga arbetsställningar.<br/>Skall kapas i längder under 1 meter innan utläggning sker, och bör ej läggas i långa rader efter varandra. Det bästa är att ha en förskjutning i sidoled. Görs inte detta är det mycket stor risk att man skapar sprickanvisningar i plattan man gjuter.<br/>Rekommenderat antal cirka 1 meter per kvadratmeter.<br/>Levereras i längder om 2,5 meter.', '18_distansspiral.png', pg, 'Distansspiral')
    db.session.add(p)

    # Betongkloss # 
    p = Product(u'Betongkloss', u'Runda distanser av betong, nns både som valv- och markdistanser. Används huvudsakligen vid tyngre armeringskonstruktioner, framförallt vid brobyggen och anläggningsbyggen.<br/>Finns i höjderna 20 till 100 mm med diameter från 35 till 100 mm.<br/>Standardutförande är med rak najtråd, tillverkad i anläggningscement.<br/>Finns även med spik, öglad najtråd, utan tråd och i annan cementkvalitet.', '12_betongklossar.png', pg, 'Betongkloss')
    db.session.add(p)

    # Kryssdistans # 
    p = Product(u'Kryssdistans', u'Används där det är viktigt med så liten anliggningsyta mot formen som möjligt, exempelvis en prefabvägg som skall slipas.<br/>Kan fås färgade i t.ex. svart eller vitt. Detta innebär dock längre leveranstid och minsta antal på ca 5000 st.', '42_kryssdistans.png', pg, 'Kryssdistans')
    db.session.add(p)
    
    db.session.add_all([
        ProductInfo('25', 1, hojd, p),        
        ProductInfo('30', 2, hojd, p),        
        ProductInfo('35', 3, hojd, p),        
        ProductInfo('5-6', 1, jarn, p),
        ProductInfo('5-6', 2, jarn, p),
        ProductInfo('5-6', 3, jarn, p),
        ProductInfo('1000', 1, antalforpSt, p),
        ProductInfo('500', 2, antalforpSt, p),
        ProductInfo('250', 3, antalforpSt, p),
        ProductInfo('Lagervara', 1, lagerstatus, p),
        ProductInfo('Lagervara', 2, lagerstatus, p),
        ProductInfo('Lagervara', 3, lagerstatus, p),
    ])

    ## Distanser för pallning ##
    pg = ProductGroup(u'Distanser för Pallning', 'pallningsbrickor_bjorn.png', pc, u'Pallning')

    # Pallningsbrickor BJÖRN #
    p = Product(u'Pallningsbrickor BJÖRN', u'Avsedda för temporär pallning av prefabricerade betongelement vid montage. Undergjutning med betong eller pallning med stålbrickor måste ske efteråt.<br/>En av de produkter som har flest användningsområde. Förutom vid prefabmontage, så används denna bricka på de flesta ställen där man vill ha pallning mellan två underlag, exempelvis läggning av ny läkt på ett gammalt tak. Användningsområdena begränsas bara av användarens fantasi.<br/>Dimensionen är 45 x 70 mm, och höjderna är färgkodade för att det skall vara enkelt att skilja på dem. Alla brickor är även kompatibla med Pallningsbricka 50 x 80 mm.<br/>Levereras även i andra förpackningsstorlekar enligt ert önskemål. ”Blandade” kartonger, dvs alla tre storlekarna i samma kartong, är också möjligt.<br/>Kontakta oss så löser vi det tillsammans med er!', '13_pallningsbrickor_bjorn.png', pg, 'Pallningsbrickor_bjorn')
    db.session.add(p)
    db.session.add_all([
        ProductInfo('2', 1, hojd, p),        
        ProductInfo('5', 2, hojd, p),        
        ProductInfo('10', 3, hojd, p),        
        ProductInfo(u'Blå', 1, farg, p),
        ProductInfo(u'Grön', 2, farg, p),
        ProductInfo(u'Svart', 3, farg, p),
        ProductInfo('1000', 1, antalforpSt, p),
        ProductInfo('450', 2, antalforpSt, p),
        ProductInfo('250', 3, antalforpSt, p),
        ProductInfo('Lagervara', 1, lagerstatus, p),
        ProductInfo('Lagervara', 2, lagerstatus, p),
        ProductInfo('Lagervara', 3, lagerstatus, p)
    ])
    
    # Pallningsbrickor SLAGBJÖRN #
    p = Product(u'Pallningsbrickor SLAGBJÖRN', u'Björnens storebror.<br/>Samma egenskaper som pallningsbricka BJÖRN.<br/>Dimension 95 x 95 mm', '56_pallningsbrickor_slagbjorn.png', pg, 'Pallningsbrickor_slagbjorn')
    db.session.add(p)
    db.session.add_all([
        ProductInfo('2', 1, hojd, p),        
        ProductInfo('5', 2, hojd, p),        
        ProductInfo('10', 3, hojd, p),        
        ProductInfo(u'Blå', 1, farg, p),
        ProductInfo(u'Grön', 2, farg, p),
        ProductInfo(u'Svart', 3, farg, p),
        ProductInfo('600', 1, antalforpSt, p),
        ProductInfo('240', 2, antalforpSt, p),
        ProductInfo('120', 3, antalforpSt, p),
        ProductInfo('Lagervara', 1, lagerstatus, p),
        ProductInfo('Lagervara', 2, lagerstatus, p),
        ProductInfo('Lagervara', 3, lagerstatus, p)
    ])

    ## Distanser för isolering ##
    pg = ProductGroup(u'Distanser för Isolering', '54_ror_hulling.png', pc, u'Isolering')

    # Hulling FALK #
    p = Product(u'Hulling FALK', u'Från början avsedda för att fästa isolering vid våt/obrunnen betong, vilket den fortfarande naturligtvis fungerar utmärkt för.<br/>I samband med att det har blivit allt vanligare med isolering i mark- plattor, och även i så kallad sandwichvägg, har det uppstått ett behov av en plastspik, som förbinder de olika isoleringsskivorna, till detta ändamål fungerar hulling utmärkt.<br/>Antal per kvadratmeter är mycket beroende på yttre omständigheter. Är det en grund, där isoleringen skall ligga utsatt för vind en längre period innan pågjutningen sker, behövs det upp 6-8 st per skiva.<br/>Är omständigheterna mer gynnsamma, och pågjutningen kommer att ske snart därpå, räcker det med 2-4 st per skiva.', '23_hulling_falk.png', pg, 'Hulling_falk')
    db.session.add(p)
    db.session.add_all([
        ProductInfo('50', 1, langdMm, p),        
        ProductInfo('75', 2, langdMm, p),        
        ProductInfo('90', 3, langdMm, p),        
        ProductInfo('125', 4, langdMm, p),        
        ProductInfo('150', 5, langdMm, p),        
        ProductInfo('180', 6, langdMm, p),        
        ProductInfo('200', 7, langdMm, p),        
        ProductInfo('250', 8, langdMm, p),        
        ProductInfo('1000', 1, antalforpSt, p),
        ProductInfo('500', 2, antalforpSt, p),
        ProductInfo('500', 3, antalforpSt, p),
        ProductInfo('900', 4, antalforpSt, p),
        ProductInfo('600', 5, antalforpSt, p),
        ProductInfo('500', 6, antalforpSt, p),
        ProductInfo('400', 7, antalforpSt, p),
        ProductInfo('250', 8, antalforpSt, p),
        ProductInfo('Lagervara', 1, lagerstatus, p),
        ProductInfo('Lagervara', 2, lagerstatus, p),
        ProductInfo('Lagervara', 3, lagerstatus, p),
        ProductInfo('Lagervara', 4, lagerstatus, p),
        ProductInfo('Lagervara', 5, lagerstatus, p),
        ProductInfo('Lagervara', 6, lagerstatus, p),
        ProductInfo('Lagervara', 7, lagerstatus, p),
        ProductInfo('Lagervara', 8, lagerstatus, p),
    ])
    
    # Rör-hulling #
    p = Product(u'Rör-hulling', u'Vidareuteckling av Hullingen, försedd med fästa för värmerör ovanpå skallen.', '54_ror_hulling.png', pg, 'Ror_hulling')
    db.session.add(p)
    db.session.add_all([
        ProductInfo('16', 1, ror, p),        
        ProductInfo('20', 2, ror, p),        
        ProductInfo('-', 1, antalforpSt, p),
        ProductInfo('-', 2, antalforpSt, p),
        ProductInfo('Lagervara', 1, lagerstatus, p),
        ProductInfo('Lagervara', 2, lagerstatus, p),
    ])

    # Hullingkrok #
    p = Product(u'Hullingkrok', u'Hulling avsedd för att hålla fast nät, ex putsnät eller annan tunn tråd mot isolering. Fungerar naturligtvis även för att hålla fast annat som passar i krokarna också.', '34_hullingkrok.png', pg, 'Hullingkrok')
    db.session.add(p)
    db.session.add_all([
        ProductInfo('180', 1, langdMm, p),        
        ProductInfo('1300', 1, antalforpSt, p),
        ProductInfo('Lagervara', 1, lagerstatus, p),
    ])

    # SVÄRDFISK #
    p = Product(u'SVÄRDFISK', u'Fixera isolering vid betong, fästa två isoleringsblock mot varandra, fixera isolering under en pålad grund och många andra användningsområden. Samma som hullingen eller Iso-skruven används till idag.<br/>Monteras ovanifrån då den körs ner genom skivorna och vrids ett kvarts varv, eller underifrån då man trär på skivorna. Tillverkad i rostfritt (A2) material, Ø 4 mm.<br/>Som standardlängder finns 350 mm för pålad grund med 300 mm isolering och 400 mm för att fästa 3-4 isoleringsblock mot varandra. Ytterligare längder kan tas fram vid behov.<br/>Leveranstid (standardlänger): Omgående. <br/>Leveranstid (special). 1-2 veckor.', '60_svardfisk.png', pg, 'Svardfisk')
    
    # Isolerstift #
    p = Product(u'Isolerstift', u'Avsett för att fästa isolering i brunnen betong.<br/> Borra ett Ø 8 mm hål i betongen, minst 40 mm djupt.<br/>Stick stiftet igenom isoleringen, tryck in den räfflade delen i hålet (använd med fördel gummiklubba eller hammare till detta).<br/>Stiftets längd beräknas enligt följande: Isoleringens tjocklek + 40 mm = Stiftlängd.<br/>Exempel: Isolering: 80 mm + 40 mm = Stiftlängd 20 mm.', '35_isolerstift.png', pg, 'Isolerstift')
    db.session.add(p)
    db.session.add_all([
        ProductInfo('80', 1, langdMm, p),        
        ProductInfo('110', 2, langdMm, p),        
        ProductInfo('140', 3, langdMm, p),        
        ProductInfo('170', 4, langdMm, p),        
        ProductInfo('200', 5, langdMm, p),        
        ProductInfo('40', 1, forIsolering, p),        
        ProductInfo('60', 2, forIsolering, p),        
        ProductInfo('100', 3, forIsolering, p),        
        ProductInfo('140', 4, forIsolering, p),        
        ProductInfo('160', 5, forIsolering, p),        
        ProductInfo('250', 1, antalforpSt, p),
        ProductInfo('250', 2, antalforpSt, p),
        ProductInfo('250', 3, antalforpSt, p),
        ProductInfo('250', 4, antalforpSt, p),
        ProductInfo('250', 5, antalforpSt, p),
        ProductInfo('Ring oss', 1, lagerstatus, p),
        ProductInfo('Ring oss', 2, lagerstatus, p),
        ProductInfo('Ring oss', 3, lagerstatus, p),
        ProductInfo('Ring oss', 4, lagerstatus, p),
        ProductInfo('Ring oss', 5, lagerstatus, p),
    ])

    # Isolerstiftsring #
    p = Product(u'Isolerstiftsring', u'Förstoringsring som passar både Hulling och Isolerstift.<br/>Ej nödvändig när det gäller frigolit, men användbar när det gäller så kallad “lös isolering”, exempelvis Rockwool eller Gulfiber.<br/>Antal per förpackning: 250 st', '36_isolerstiftsring.png', pg, 'Isolerstiftsring')
    db.session.add(p)

    # Fluktsticka #
    p = Product(u'Fluktsticka', u'Fluktstickan används huvudsakligen för avvägning, fluktning, mellan olika ytors höjd på en byggarbetsplats. Den har ingenting att göra med tittare, fluktare.', '27_fluktsticka.png', pg, 'Fluktsticka')
    db.session.add(p)
    
    db.session.add_all([
        ProductInfo('Vit', 1, farg, p),        
        ProductInfo('Gul', 2, farg, p),        
        ProductInfo(u'Röd', 3, farg, p),        
        ProductInfo(u'Blå', 4, farg, p),        
        ProductInfo('1000', 1, antalforpSt, p),
        ProductInfo('1000', 2, antalforpSt, p),
        ProductInfo('1000', 3, antalforpSt, p),
        ProductInfo('1000', 4, antalforpSt, p),
        ProductInfo('Lagervara', 1, lagerstatus, p),
        ProductInfo('Lagervara', 2, lagerstatus, p),
        ProductInfo('Lagervara', 3, lagerstatus, p),
        ProductInfo('Lagervara', 4, lagerstatus, p),
    ])

    # Isolerdistans typ ULV #
    p = Product(u'Isolerdistans typ ULV', u'Ett komplement till den vanliga markklossen.<br/>Mindre anliggningsyta och lågt pris.<br/>Främst avsedd för att användas på frigolit.<br/>Tänkbara användningsområden är prefabindustrin vid sandwichelement, platsbyggnation och mindre områden där det är låg belastning på frigoliten.', '62_isolerdistans_typ_ulv.png', pg, 'Isolerdistans_typ_ULV')
    db.session.add(p)
    
    db.session.add_all([
        ProductInfo('4-12', 1, jarn, p),        
        ProductInfo('4-12', 2, jarn, p),        
        ProductInfo('4-12', 3, jarn, p),        
        ProductInfo('4-12', 4, jarn, p),        
        ProductInfo('4-12', 5, jarn, p),        
        ProductInfo('4-12', 6, jarn, p),        
        ProductInfo('4-12', 7, jarn, p),        
        ProductInfo('10', 1, hojd, p),        
        ProductInfo('15', 2, hojd, p),        
        ProductInfo('20', 3, hojd, p),        
        ProductInfo('25', 4, hojd, p),        
        ProductInfo('30', 5, hojd, p),        
        ProductInfo('35', 6, hojd, p),        
        ProductInfo('40', 7, hojd, p),        
        ProductInfo('650', 1, antalforpSt, p),
        ProductInfo('600', 2, antalforpSt, p),
        ProductInfo('500', 3, antalforpSt, p),
        ProductInfo('450', 4, antalforpSt, p),
        ProductInfo('400', 5, antalforpSt, p),
        ProductInfo('400', 6, antalforpSt, p),
        ProductInfo('35', 7, antalforpSt, p),
        ProductInfo('Rings oss', 1, lagerstatus, p),
        ProductInfo('Ring oss', 2, lagerstatus, p),
        ProductInfo('Lagervara', 3, lagerstatus, p),
        ProductInfo('Lagervara', 4, lagerstatus, p),
        ProductInfo('Lagervara', 5, lagerstatus, p),
        ProductInfo('Ring oss', 6, lagerstatus, p),
        ProductInfo('Ring oss', 7, lagerstatus, p),
    ])

    ## Runda distanser ##
    pg = ProductGroup(u'Runda distanser', '15_dinkihjul.png', pc, u'Runda')

    # Hulling FALK #
    p = Product(u'Dinkihjul', u'Allroundhjul framtaget för att passa på era olika järndimensioner, 4-12 mm. Detta för att minska antalet hjul som behövs hållas i lager, framförallt hos användaren.<br/>Hjulet har vågformade toppar för att ligga bra i handen och gör inte ont i handen för den som monterar.<br/>Finns för de esta olika järndimensionerna och med olika täckskikt. Fråga gärna efter det hjul som just ni behöver. OBS: Vi har mycket bra priser på dessa, förmodligen det lägsta på hela marknaden. Höjderna 20 25 och 30 finns även i nymaterial (vita) och är lagervaror.', '15_dinkihjul.png', pg, 'Dinkhjul')
    db.session.add(p)
    db.session.add_all([
        ProductInfo('4-12', 1, jarn, p),        
        ProductInfo('4-12', 2, jarn, p), 
        ProductInfo('4-12', 3, jarn, p),        
        ProductInfo('4-12', 4, jarn, p),        
        ProductInfo('4-12', 5, jarn, p),        
        ProductInfo('4-12', 6, jarn, p),        
        ProductInfo('4-12', 7, jarn, p),        
        ProductInfo('8-20', 8, jarn, p),        
        ProductInfo('8-20', 9, jarn, p),        
        ProductInfo('8-20', 10, jarn, p),        
        ProductInfo('8-20', 11, jarn, p),        
        ProductInfo('8-20', 12, jarn, p),        
        ProductInfo('15', 1, tackskikt, p),
        ProductInfo('20', 2, tackskikt, p),
        ProductInfo('25', 3, tackskikt, p),
        ProductInfo('30', 4, tackskikt, p),
        ProductInfo('35', 5, tackskikt, p),
        ProductInfo('40', 6, tackskikt, p),
        ProductInfo('50', 7, tackskikt, p),
        ProductInfo('25', 8, tackskikt, p),
        ProductInfo('30', 9, tackskikt, p),
        ProductInfo('35', 10, tackskikt, p),
        ProductInfo('40', 11, tackskikt, p),
        ProductInfo('50', 12, tackskikt, p),
        ProductInfo('1000', 1, antalforpSt, p),
        ProductInfo('1000', 2, antalforpSt, p),
        ProductInfo('500', 3, antalforpSt, p),
        ProductInfo('500', 4, antalforpSt, p),
        ProductInfo('500', 5, antalforpSt, p),
        ProductInfo('125', 6, antalforpSt, p),
        ProductInfo('100', 7, antalforpSt, p),
        ProductInfo('-', 8, antalforpSt, p),
        ProductInfo('-', 9, antalforpSt, p),
        ProductInfo('-', 10, antalforpSt, p),
        ProductInfo('-', 11, antalforpSt, p),
        ProductInfo('-', 12, antalforpSt, p),
        ProductInfo('Lagervara', 1, lagerstatus, p),
        ProductInfo('Lagervara', 2, lagerstatus, p),
        ProductInfo('Lagervara', 3, lagerstatus, p),
        ProductInfo('Lagervara', 4, lagerstatus, p),
        ProductInfo('Lagervara', 5, lagerstatus, p),
        ProductInfo('Lagervara', 6, lagerstatus, p),
        ProductInfo('Lagervara', 7, lagerstatus, p),
        ProductInfo('Lagervara', 8, lagerstatus, p),
        ProductInfo('Lagervara', 9, lagerstatus, p),
        ProductInfo('Lagervara', 10, lagerstatus, p),
        ProductInfo('Lagervara', 11, lagerstatus, p),
        ProductInfo('Lagervara', 12, lagerstatus, p),
    ])

    db.session.commit()


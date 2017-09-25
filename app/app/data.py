#!/usr/bin/python
# -*- coding: utf-8 -*-
from models import *
from app import db
def CreateData():
    #####  ---- ProduktInfoNamn ----  #####
    lagerstatus = InfoName('Lagerstatus', 20)
    antalforpSt = InfoName(u'Antal per förp [st.]', 19)
    antalForpPall = InfoName(u'Antal per förp / pall [st.]', 18)
    hojd = InfoName(u'Höjd [mm]', 1)
    jarn = InfoName(u'Järn diameter [mm]', 5)
    ror = InfoName(u'Rör-diameter [mm]', 5)
    langdCm = InfoName(u'Längd [cm]', 3)
    langdMm = InfoName(u'Längd [mm]', 4)
    farg = InfoName(u'Färgkod', 7)
    forIsolering = InfoName(u'För isolering [mm]', 8)
    tackskikt = InfoName(u'Täckskikt [mm]', 2)
    ganga = InfoName(u'Gänga', 5)
    abc = InfoName(u'A x B x C [mm]', 5)
    utforande = InfoName(u'Utförande', 7)
    hbf = InfoName(u'Höjd x Bredd x Fasad [mm]', 5)
    artnr = InfoName(u'Artikelnummer', 1)
    benamning = InfoName(u'Benämning', 2)
    utokadBeskr = InfoName(u'Utökad beskrivning', 9)
    typ = InfoName(u'Typ', 5)
    diamInUt = InfoName(u'Diameter in/ut [mm]', 7)
    diameter = InfoName(u'Diameter [mm]', 5)
    blh = InfoName(u'B x L x H [mm]', 5)
    spik = InfoName(u'Spik', 5)
    magnetKraft = InfoName(u'Magnetkraft [kn]', 7)
    viktKg = InfoName(u'Vikt [kg]', 9)
    breddBotten = InfoName(u'Bredd botten [mm]', 11)
    breddToppen = InfoName(u'Bredd toppen [mm]', 12)
    hojdLateOrder = InfoName(u'Höjd [mm] ', 15)
    rekTappstrlk = InfoName(u'Rekommenderad tappstorlek', 18)
    tillAnkare = InfoName(u'Till ankarstorlek', 18)
    tapphojd = InfoName(u'Tapphöjd', 6)
    antMagneter = InfoName(u'Antal magneter som standard [st.]', 3)
    viktInklMagnet = InfoName(u'Vikt inkl. magneter [kg]', 5)
    viktPerMeter = InfoName(u'Vikt per meter', '20')
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
        tackskikt,
        ganga,
        abc,
        utforande,
        hbf,
        artnr,
        benamning,
        typ,
        diamInUt,
        diameter,
        blh,
        spik,
        magnetKraft,
        viktKg,
        breddBotten,
        breddToppen,
        hojdLateOrder,
        rekTappstrlk,
        tillAnkare,
        tapphojd,
        antMagneter,
        viktInklMagnet,
        utokadBeskr,
        viktPerMeter
    ])


    #####  ---- Distanser ----  #####   
    pc = ProductCategory('Distanser')
    db.session.add(pc)
    ## Distanser för Mark ##
    pg = ProductGroup(u'Distanser för Mark', '1_markdistans_varg.png', pc, u'Mark')
    db.session.add(pg)
    # Markdistans varg #
    p = Product('Markdistans typ VARG', u'Den absolut största produkten sett till antalet som används för både lösarmering och armeringsnät. Fungerar lika bra på löst som fast/hårt underlag, viktigt att anläggningsytan är slät, så att markdistansen står stabilt mot underlaget. Det är också mycket viktigt att den är konstruerad i vädertåligt material och att den klarar hög belastning ovanifrån, då den bl.a. ska tåla en 120-kilos byggnadsarbetare som kliver i formen. <br/>Rekommenderat antal per kvadratmeter är 3-4 st.<br/>Kan även levereras i även i ”storpack”. <br/>Kontakta oss så löser vi det tillsammans med Er!', '1_markdistans_varg.png', pg, 'Markdistans_varg', True)
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
    p = Product(u'Distanslister för mark', u'Samma användningsområde som markdistansen. Passar dock bättre för nät än för lösarmering. Läggs ut i längder direkt på underlaget, därefter läggs nätet ovanpå. Enkelt och mindre risk för olämpliga arbetsställningar.<br/>Skall kapas i längder under 1 meter innan utläggning sker, och bör ej läggas i långa rader efter varandra. Det bästa är att ha en förskjutning i sidled. Görs inte detta är det stor risk att man skapar sprickanvisningar i den platta man gjuter. <br/>Rekommenderas cirka 1 meter per kvadratmeter.<br/>Levereras i längder om 2 meter. Kapade längder kan levereras på begäran. ', '20_distanslister_for_mark.png', pg, 'Distanslist_mark', False)
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
        ProductInfo('50 / 3150', 1, antalForpPall, p),
        ProductInfo('50 / 3150', 2, antalForpPall, p),
        ProductInfo('50 / 2100', 3, antalForpPall, p),
        ProductInfo('50 / 1800', 4, antalForpPall, p),
        ProductInfo('30 / 1260', 5, antalForpPall, p),
        ProductInfo('30 / 1200', 6, antalForpPall, p),
        ProductInfo('30 / 840', 7, antalForpPall, p),
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
    p = Product(u'Vägg- och Valvdistans JÄRV', u'Denna distans har funnits i många olika och varierande utformningar, alla med sina egna goda egenskaper och fördelar. <br/> I mitten på 90 talet satte sig “Mr Distans” ner och försökte samla alla dess goda egenskaper i en distans. Resultatet blev Varianten, som genom åren har visat sig vara just den bästa och mest användbara vägg- och valvdistansen. Den används mot hårt underlag både på valv och i väggar, och passar likväl för lösarmering såsom armeringsnät. <br/>Vi tillverkar den i ett material som tål både värme och kyla. Rekommenderat antal per kvadratmeter är 3-4 st. <br/><br/>Höjderna 20/25, 30/35 och 40/45 finns numera även i regranulerat material. Den har samma hållfasthet fast färgen är mer mellangrå. Eftersom det är regranulerat (återanvänt) material innebär det lite lägre pris och mindre mijlöpåverkan.', 'valvdistans_jarv.png', pg, '2_vagg_valvdistans_jarv.png', True)
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
    p = Product(u'Valvdistans BOCK', u'Allmänt kallad sågbock på grund av sin likhet med denna, dock lite mindre till formatet. Genom sin storlek och anliggningsyta passar den bra inom prefabindustrin, att den sedan är billig försämrar ju inte saken.<br />Levereras förpackade i påse.', '14_valvdistans_bock.png', pg, 'Valvdistans_bock', False)
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
    p = Product(u'Valvdistans VBOCK', u'Förstärkt version av Bock, sätts endast på ett järn, passar ej i krysset.', '64_valvdistans_vbock.png', pg, 'Valvdistans_vbock', False)
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
    p = Product(u'Valvdistans PRAXI', u'Välkant fyrbening som är spikbar i alla ben samt i centrum. Används framförallt vid tung armering.', '51_valvdistans_praxi.png', pg, 'Valvdistans_praxi', False)
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
        ProductInfo('Ring oss', 2, lagerstatus, p),
        ProductInfo('Ring oss', 3, lagerstatus, p),
        ProductInfo('Ring oss', 4, lagerstatus, p),
        ProductInfo('Ring oss', 5, lagerstatus, p),
        ProductInfo('Ring oss', 6, lagerstatus, p),
        ProductInfo('Ring oss', 7, lagerstatus, p),
        ProductInfo('Ring oss', 8, lagerstatus, p),
    ])

    # Vägg- och valdistans GEMINI #
    p = Product(u'Vägg- och Valvdistans GEMINI', u'Den distans med högsta täckskikt som finns på marknaden. Mycket kraftig vilket medför att den tål hög belastning.<br/>Används oftast för att distansera överkantsarmering.<br/>Kan grensla över en underkantsarmering och runda fötter ger liten anliggningsyta.<br/>Mycket bra betongomslutning.', '30_valvdistans_gemini.png', pg, 'Vagg_valvdistans_gemini', False)
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
    p = Product(u'Igelkott ENKEL', u'Används som valvdistanser på stålunderlag.<br/>Läggs ut i formen, nätarmeringen läggs direkt ovanpå. Skapar bra arbetsmiljö med få böjningar. Risker finns dock för halkolyckor om man går i formen vid utläggningen. Några fördelar mot ringarna är att det är lättare att nå ut i hörnen samt att den är enklare att använda där det är smalt. <br/>Mått: 90 x 195 mm.', '53_igelkott_enkel.png', pg, 'Igelkott_enkel', True)
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
    p = Product(u'Igelkott DUBBEL', u'Används som Igelkott ENKEL.<br/>Mått: 195 x 195 mm', '22_igelkott_dubbel.png', pg, 'Igelkott_dubbel', True)
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
        ProductInfo('4860', 1, antalForpPall, p),
        ProductInfo('4860', 2, antalForpPall, p),
        ProductInfo('4860', 3, antalForpPall, p),
        ProductInfo('4860', 4, antalForpPall, p),
        ProductInfo('4860', 5, antalForpPall, p),
        ProductInfo('4860', 6, antalForpPall, p),
        ProductInfo('4860', 7, antalForpPall, p),
        ProductInfo('4860', 8, antalForpPall, p),
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
    p = Product(u'Distanslist VESSLA', u'Distanslist av typ Druzack. Fungerar mycket bra inom prefabindustrin, mot hårda underlag och på isolering om inte det blir för tung belastning. Kan naturligtvis även användas vid platsgjutning.<br/>Är hopkopplingsbar, även i vinkel upp till ca 30 grader, vilket gör det möjligt att bygga sin egen speciallist som bland annat kan gå runt hörn. Har fått sitt namn av att det är en smidig och slingrig typ.', '65_distanslist_vessla.png', pg, 'Distanslist_vessla', False)
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
    p = Product(u'Distanslist BÄVER', u'Distanslist av Quicktyp. Har mycket liten anliggningsyta tack vare sina små och spetsiga fötter. Är hopkopplingsbar, dock inte vinklingsbar. <br/>Har fått sitt namn av en kvinnlig fabriksägare, som tyckte att läppen som används för att koppla ihop dem med såg ut som en Bäversvans.<br/>Kan levereras i sammansatta längder om 100, 150 eller 200 cm.', '9_distanslist_baver.png', pg, 'Distanslist_baver', False)
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
    p = Product(u'Armeringsstege KOBRA', u'Sinusformad armeringsstege, består av två längsgående vågformade armeringsjärn som hålls samman av vertikal tråd.<br/>Används vid dubbelarmering, läggs ovanpå lägsta armeringsnätet, nästa nät läggs ovanpå armeringsstegen. Rekommenderat är att armeringsstegen surras fast med najtråd i det undre nätet.<br/>Rekommenderat antal är 1 meter per kvadratmeter. Levereras i längder om 2 meter.', '40_armeringsstege_kobra.png', pg, 'Armeringsstege_kobra', False)
    db.session.add(p)
    db.session.add_all([
        ProductInfo('20', 1, hojd, p),        
        ProductInfo('30', 2, hojd, p),        
        ProductInfo('40', 3, hojd, p),        
        ProductInfo('50', 4, hojd, p),        
        ProductInfo('60', 5, hojd, p),        
        ProductInfo('70', 6, hojd, p),        
        ProductInfo('80', 7, hojd, p),        
        ProductInfo('90', 8, hojd, p),        
        ProductInfo('100', 9, hojd, p),        
        ProductInfo('110', 10, hojd, p),        
        ProductInfo('120', 11, hojd, p),        
        ProductInfo('130', 12, hojd, p),        
        ProductInfo('140', 13, hojd, p),        
        ProductInfo('150', 14, hojd, p),        
        ProductInfo('160', 15, hojd, p),        
        ProductInfo('170', 16, hojd, p),        
        ProductInfo('180', 17, hojd, p),        
        ProductInfo('190', 18, hojd, p),        
        ProductInfo('200', 19, hojd, p),        
        ProductInfo('220', 20, hojd, p),        
        ProductInfo('240', 21, hojd, p),        
        ProductInfo('260', 22, hojd, p),        
        ProductInfo('280', 23, hojd, p),        
        ProductInfo('300', 24, hojd, p),        
        ProductInfo('400', 25, hojd, p),        
        ProductInfo('25 / 2000', 1, antalforpSt, p),
        ProductInfo('25 / 2000', 2, antalforpSt, p),
        ProductInfo('25 / 2000', 3, antalforpSt, p),
        ProductInfo('25 / 1500', 4, antalforpSt, p),
        ProductInfo('25 / 1500', 5, antalforpSt, p),
        ProductInfo('25 / 1000', 6, antalforpSt, p),
        ProductInfo('25 / 1000', 7, antalforpSt, p),
        ProductInfo('25 / 1000', 8, antalforpSt, p),
        ProductInfo('25 / 900', 9, antalforpSt, p),
        ProductInfo('25 / 800', 10, antalforpSt, p),
        ProductInfo('25 / 700', 11, antalforpSt, p),
        ProductInfo('25 / 600', 12, antalforpSt, p),
        ProductInfo('25 / 600', 13, antalforpSt, p),
        ProductInfo('25 / 600', 14, antalforpSt, p),
        ProductInfo('25 / 500', 15, antalforpSt, p),
        ProductInfo('25 / 500', 16, antalforpSt, p),
        ProductInfo('25 / 500', 17, antalforpSt, p),
        ProductInfo('25 / 500', 18, antalforpSt, p),
        ProductInfo('25 / 400', 19, antalforpSt, p),
        ProductInfo('25 / 400', 20, antalforpSt, p),
        ProductInfo('25 / 300', 21, antalforpSt, p),
        ProductInfo('25 / 300', 22, antalforpSt, p),
        ProductInfo('25 / 300', 23, antalforpSt, p),
        ProductInfo('25 / 300', 24, antalforpSt, p),
        ProductInfo('25 / 200', 25, antalforpSt, p),
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
        ProductInfo('Lagervara', 17, lagerstatus, p),
        ProductInfo('Ring oss', 18, lagerstatus, p),
        ProductInfo('Lagervara', 19, lagerstatus, p),
        ProductInfo('Ring oss', 20, lagerstatus, p),
        ProductInfo('Ring oss', 21, lagerstatus, p),
        ProductInfo('Ring oss', 22, lagerstatus, p),
        ProductInfo('Ring oss', 23, lagerstatus, p),
        ProductInfo('Ring oss', 24, lagerstatus, p),
        ProductInfo('Ring oss', 25, lagerstatus, p),
    ])

    # Nätstöd typ A # 
    p = Product(u'Nätstöd typ A', u'Rak armeringsstege, består av tre längsgående armeringsjärn som hålls samman av vågformad, längsgående tråd.<br/>Används vid dubbelarmering, läggs direkt ovanpå undre armeringsnätet, nästa nät läggs därefter ovanpå armeringsstegen. Rekommenderat är att armeringsstegen surras fast med najtråd i det undre nätet.<br/>Rekommenderat antal är 1 meter per kvadratmeter. Levereras i längder om 2 meter.', '17_natstod_typ_a.png', pg, 'Natstod_typ_A', False)
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
        ProductInfo('Ring oss', 13, lagerstatus, p),
        ProductInfo('Ring oss', 14, lagerstatus, p),
        ProductInfo('Ring oss', 15, lagerstatus, p),
        ProductInfo('Ring oss', 16, lagerstatus, p),
    ])

     # Distanslister för valv # 
    p = Product(u'Distanslister för valv', u'Samma användningsområde som valvdistansen. Passar dock bättre för nät än för lösarmering.<br/>Läggs ut i längder direkt på underlaget, därefter läggs nätet ovanpå. Enkelt och mindre risk för olämpliga arbetsställningar.<br/>Skall kapas i längder under 1 meter innan utläggning sker, och bör ej läggas i långa rader efter varandra. Det bästa är att ha en förskjutning i sidoled. Görs inte detta är det stor risk att man skapar sprickanvisningar i den platta man gjuter. <br/>Rekommenderat antal cirka 1 meter per kvadratmeter. Levereras i längder om 2 meter. Kapade längder kan levereras på begäran.', '19_distansliste_for_valv.png', pg, 'Distanslist_valv', False)
    db.session.add(p)

    db.session.add_all([
        ProductInfo('15', 1, hojd, p),        
        ProductInfo('20', 2, hojd, p),        
        ProductInfo('25', 3, hojd, p),        
        ProductInfo('30', 4, hojd, p),        
        ProductInfo('35', 5, hojd, p),        
        ProductInfo('40', 6, hojd, p),        
        ProductInfo('50', 7, hojd, p),        
        ProductInfo('50 / 3150', 1, antalForpPall, p),
        ProductInfo('50 / 3150', 2, antalForpPall, p),
        ProductInfo('50 / 2100', 3, antalForpPall, p),
        ProductInfo('50 / 1800', 4, antalForpPall, p),
        ProductInfo('30 / 1260', 5, antalForpPall, p),
        ProductInfo('30 / 1200', 6, antalForpPall, p),
        ProductInfo('30 / 840', 7, antalForpPall, p),
        ProductInfo('Lagervara', 1, lagerstatus, p),
        ProductInfo('Lagervara', 2, lagerstatus, p),
        ProductInfo('Lagervara', 3, lagerstatus, p),
        ProductInfo('Lagervara', 4, lagerstatus, p),
        ProductInfo('Lagervara', 5, lagerstatus, p),
        ProductInfo('Ring oss', 6, lagerstatus, p),
        ProductInfo('Ring oss', 7, lagerstatus, p),
    ])

    # Distansspiral # 
    p = Product(u'Distansspiral', u'Samma användningsområde som valvdistansen. Passar dock bättre för nät- än för lösarmering.<br/>Läggs ut i längder direkt på underlaget, därefter läggs nätet ovanpå. Enklare och mindre risk för olämpliga arbetsställningar.<br/>Skall kapas i längder under 1 meter innan utläggning sker, och bör ej läggas i långa rader efter varandra. Det bästa är att ha en förskjutning i sidoled. Görs inte detta är det mycket stor risk att man skapar sprickanvisningar i plattan man gjuter.<br/>Rekommenderat antal cirka 1 meter per kvadratmeter.<br/>Levereras i längder om 2,5 meter.', '18_distansspiral.png', pg, 'Distansspiral', False)
    db.session.add(p)

    # Betongkloss # 
    p = Product(u'Betongkloss', u'Runda distanser av betong, nns både som valv- och markdistanser. Används huvudsakligen vid tyngre armeringskonstruktioner, framförallt vid brobyggen och anläggningsbyggen.<br/>Finns i höjderna 20 till 100 mm med diameter från 35 till 100 mm.<br/>Standardutförande är med rak najtråd, tillverkad i anläggningscement.<br/>Finns även med spik, öglad najtråd, utan tråd och i annan cementkvalitet.', '12_betongklossar.png', pg, 'Betongkloss', False)
    db.session.add(p)

    # Kryssdistans # 
    p = Product(u'Kryssdistans', u'Används där det är viktigt med så liten anliggningsyta mot formen som möjligt, exempelvis en prefabvägg som skall slipas.<br/>Kan fås färgade i t.ex. svart eller vitt. Detta innebär dock längre leveranstid och minsta antal på ca 5000 st.', '42_kryssdistans.png', pg, 'Kryssdistans', False)
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
    p = Product(u'Pallningsbrickor BJÖRN', u'Avsedda för temporär pallning av prefabricerade betongelement vid montage. Undergjutning med betong eller pallning med stålbrickor måste ske efteråt.<br/>En av de produkter som har flest användningsområde. Förutom vid prefabmontage, så används denna bricka på de flesta ställen där man vill ha pallning mellan två underlag, exempelvis läggning av ny läkt på ett gammalt tak. Användningsområdena begränsas bara av användarens fantasi.<br/>Dimensionen är 45 x 70 mm, och höjderna är färgkodade för att det skall vara enkelt att skilja på dem. Alla brickor är även kompatibla med Pallningsbricka 50 x 80 mm.<br/>Levereras även i andra förpackningsstorlekar enligt ert önskemål. ”Blandade” kartonger, dvs alla tre storlekarna i samma kartong, är också möjligt.<br/>Kontakta oss så löser vi det tillsammans med er!', '13_pallningsbrickor_bjorn.png', pg, 'Pallningsbrickor_bjorn', True)
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
    p = Product(u'Pallningsbrickor SLAGBJÖRN', u'Björnens storebror.<br/>Samma egenskaper som pallningsbricka BJÖRN.<br/>Dimension 95 x 95 mm', '56_pallningsbrickor_slagbjorn.png', pg, 'Pallningsbrickor_slagbjorn', False)
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
    p = Product(u'Hulling FALK', u'Från början avsedda för att fästa isolering vid våt/obrunnen betong, vilket den fortfarande naturligtvis fungerar utmärkt för.<br/>I samband med att det har blivit allt vanligare med isolering i mark- plattor, och även i så kallad sandwichvägg, har det uppstått ett behov av en plastspik, som förbinder de olika isoleringsskivorna, till detta ändamål fungerar hulling utmärkt.<br/>Antal per kvadratmeter är mycket beroende på yttre omständigheter. Är det en grund, där isoleringen skall ligga utsatt för vind en längre period innan pågjutningen sker, behövs det upp 6-8 st per skiva.<br/>Är omständigheterna mer gynnsamma, och pågjutningen kommer att ske snart därpå, räcker det med 2-4 st per skiva.', '23_hulling_falk.png', pg, 'Hulling_falk', True)
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
    p = Product(u'Rör-hulling', u'Vidareuteckling av Hullingen, försedd med fästa för värmerör ovanpå skallen.', '54_ror_hulling.png', pg, 'Ror_hulling', True)
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
    p = Product(u'Hullingkrok', u'Hulling avsedd för att hålla fast nät, ex putsnät eller annan tunn tråd mot isolering. Fungerar naturligtvis även för att hålla fast annat som passar i krokarna också.', '34_hullingkrok.png', pg, 'Hullingkrok', False)
    db.session.add(p)
    db.session.add_all([
        ProductInfo('180', 1, langdMm, p),        
        ProductInfo('1300', 1, antalforpSt, p),
        ProductInfo('Lagervara', 1, lagerstatus, p),
    ])

    # SVÄRDFISK #
    p = Product(u'SVÄRDFISK', u'Fixera isolering vid betong, fästa två isoleringsblock mot varandra, fixera isolering under en pålad grund och många andra användningsområden. Samma som hullingen eller Iso-skruven används till idag.<br/>Monteras ovanifrån då den körs ner genom skivorna och vrids ett kvarts varv, eller underifrån då man trär på skivorna. Tillverkad i rostfritt (A2) material, Ø 4 mm.<br/>Som standardlängder finns 350 mm för pålad grund med 300 mm isolering och 400 mm för att fästa 3-4 isoleringsblock mot varandra. Ytterligare längder kan tas fram vid behov.<br/>Leveranstid (standardlänger): Omgående. <br/>Leveranstid (special). 1-2 veckor.', '60_svardfisk.png', pg, 'Svardfisk', False)
    
    # Isolerstift #
    p = Product(u'Isolerstift', u'Avsett för att fästa isolering i brunnen betong.<br/> Borra ett Ø 8 mm hål i betongen, minst 40 mm djupt.<br/>Stick stiftet igenom isoleringen, tryck in den räfflade delen i hålet (använd med fördel gummiklubba eller hammare till detta).<br/>Stiftets längd beräknas enligt följande: Isoleringens tjocklek + 40 mm = Stiftlängd.<br/>Exempel: Isolering: 80 mm + 40 mm = Stiftlängd 20 mm.', '35_isolerstift.png', pg, 'Isolerstift', False)
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
        ProductInfo('Lagervara', 1, lagerstatus, p),
        ProductInfo('Lagervara', 2, lagerstatus, p),
        ProductInfo('Lagervara', 3, lagerstatus, p),
        ProductInfo('Ring oss', 4, lagerstatus, p),
        ProductInfo('Lagervara', 5, lagerstatus, p),
    ])

    # Isolerstiftsring #
    p = Product(u'Isolerstiftsring', u'Förstoringsring som passar både Hulling och Isolerstift.<br/>Ej nödvändig när det gäller frigolit, men användbar när det gäller så kallad “lös isolering”, exempelvis Rockwool eller Gulfiber.<br/>Antal per förpackning: 250 st', '36_isolerstiftsring.png', pg, 'Isolerstiftsring', False)
    db.session.add(p)

    # Fluktsticka #
    p = Product(u'Fluktsticka', u'Fluktstickan används huvudsakligen för avvägning, fluktning, mellan olika ytors höjd på en byggarbetsplats. Den har ingenting att göra med tittare, fluktare.', '27_fluktsticka.png', pg, 'Fluktsticka', False)
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
    p = Product(u'Isolerdistans typ ULV', u'Ett komplement till den vanliga markklossen.<br/>Mindre anliggningsyta och lågt pris.<br/>Främst avsedd för att användas på frigolit.<br/>Tänkbara användningsområden är prefabindustrin vid sandwichelement, platsbyggnation och mindre områden där det är låg belastning på frigoliten.', '62_isolerdistans_typ_ulv.png', pg, 'Isolerdistans_typ_ULV', False)
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

    # Dinkihjul #
    p = Product(u'Dinkihjul', u'Allroundhjul framtaget för att passa på era olika järndimensioner, 4-12 mm. Detta för att minska antalet hjul som behövs hållas i lager, framförallt hos användaren.<br/>Hjulet har vågformade toppar för att ligga bra i handen och gör inte ont i handen för den som monterar.<br/>Finns för de esta olika järndimensionerna och med olika täckskikt. Fråga gärna efter det hjul som just ni behöver. OBS: Vi har mycket bra priser på dessa, förmodligen det lägsta på hela marknaden. Höjderna 20 25 och 30 finns även i nymaterial (vita) och är lagervaror.', '15_dinkihjul.png', pg, 'Dinkhjul', False)
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

    # Snok #
    p = Product(u'SNOK', u'Snoken är vår modell av twisthjulet. <br/>Ett speciellt hjul, anpassat för mindre järn och låga täckskickt. <br/>Sitter mycket bra fast på järnen, speciellt lämplig vid gjutning där man gör armeringskorgarna innan, exempelvis kabelrännor och dyl. Speciell låsning, träs parallellt på järnen och vrids därefter 90 grader.', '4_snok.png', pg, 'Snok', False)
    db.session.add(p)
    db.session.add_all([
        ProductInfo('4', 1, jarn, p),        
        ProductInfo('5', 2, jarn, p), 
        ProductInfo('6', 3, jarn, p),        
        ProductInfo('5', 4, jarn, p),        
        ProductInfo('6', 5, jarn, p),        
        ProductInfo('8', 6, jarn, p),        
        ProductInfo('12', 7, jarn, p),        
        ProductInfo('5', 8, jarn, p),        
        ProductInfo('6', 9, jarn, p),        
        ProductInfo('8', 10, jarn, p),        
        ProductInfo('4-6', 11, jarn, p),        
        ProductInfo('4-6', 12, jarn, p),        
        ProductInfo('10', 1, tackskikt, p),
        ProductInfo('10', 2, tackskikt, p),
        ProductInfo('10', 3, tackskikt, p),
        ProductInfo('15', 4, tackskikt, p),
        ProductInfo('15', 5, tackskikt, p),
        ProductInfo('15', 6, tackskikt, p),
        ProductInfo('15', 7, tackskikt, p),
        ProductInfo('20', 8, tackskikt, p),
        ProductInfo('20', 9, tackskikt, p),
        ProductInfo('20', 10, tackskikt, p),
        ProductInfo('25', 11, tackskikt, p),
        ProductInfo('30', 12, tackskikt, p),
        ProductInfo('15000', 1, antalforpSt, p),
        ProductInfo('15000', 2, antalforpSt, p),
        ProductInfo('15000', 3, antalforpSt, p),
        ProductInfo('6000', 4, antalforpSt, p),
        ProductInfo('6000', 5, antalforpSt, p),
        ProductInfo('6000', 6, antalforpSt, p),
        ProductInfo('6000', 7, antalforpSt, p),
        ProductInfo('4000', 8, antalforpSt, p),
        ProductInfo('4000', 9, antalforpSt, p),
        ProductInfo('4000', 10, antalforpSt, p),
        ProductInfo('650', 11, antalforpSt, p),
        ProductInfo('450', 12, antalforpSt, p),
        ProductInfo('Ring oss', 1, lagerstatus, p),
        ProductInfo('Ring oss', 2, lagerstatus, p),
        ProductInfo('Ring oss', 3, lagerstatus, p),
        ProductInfo('Lagervara', 4, lagerstatus, p),
        ProductInfo('Ring oss', 5, lagerstatus, p),
        ProductInfo('Ring oss', 6, lagerstatus, p),
        ProductInfo('Ring oss', 7, lagerstatus, p),
        ProductInfo('Lagervara', 8, lagerstatus, p),
        ProductInfo('Lagervara', 9, lagerstatus, p),
        ProductInfo('Lagervara', 10, lagerstatus, p),
        ProductInfo('Lagervara', 11, lagerstatus, p),
        ProductInfo('Lagervara', 12, lagerstatus, p),
    ])
    
    ## Änddistanser ##
    pg = ProductGroup(u'Änddistanser', '11_anddistans.png', pc, u'Anddistanser')

    # Änddistans #
    p = Product(u'Änddistans', u'Änddistansen används för att hålla rätt täckskikt på armeringsjärnets ändar.<br/>Tillverkad i ljusgrå LD-Polyeten.', '11_anddistans.png', pg, 'Anddistans', False)
    db.session.add(p)
    db.session.add_all([
        ProductInfo('4-8', 1, jarn, p),        
        ProductInfo('4-8', 2, jarn, p), 
        ProductInfo('4-8', 3, jarn, p),        
        ProductInfo('8-12', 4, jarn, p),        
        ProductInfo('8-12', 5, jarn, p),        
        ProductInfo('8-12', 6, jarn, p),        
        ProductInfo('20', 1, tackskikt, p),
        ProductInfo('25', 2, tackskikt, p),
        ProductInfo('30', 3, tackskikt, p),
        ProductInfo('20', 4, tackskikt, p),
        ProductInfo('25', 5, tackskikt, p),
        ProductInfo('30', 6, tackskikt, p),
        ProductInfo('1000', 1, antalforpSt, p),
        ProductInfo('1000', 2, antalforpSt, p),
        ProductInfo('1000', 3, antalforpSt, p),
        ProductInfo('500', 4, antalforpSt, p),
        ProductInfo('500', 5, antalforpSt, p),
        ProductInfo('500', 6, antalforpSt, p),
        ProductInfo('Lagervara', 1, lagerstatus, p),
        ProductInfo('Lagervara', 2, lagerstatus, p),
        ProductInfo('Lagervara', 3, lagerstatus, p),
        ProductInfo('Lagervara', 4, lagerstatus, p),
        ProductInfo('Lagervara', 5, lagerstatus, p),
        ProductInfo('Lagervara', 6, lagerstatus, p),
    ])
    
    ## Gängade brickor ##
    pg = ProductGroup(u'Gängade brickor', '33_gangad_spikkrage.png', pc, u'Gangade_brickor')

    # Änddistans #
    p = Product(u'Gängad spikkrage', u'Används för att fästa gängat lyft eller infästning i en prefabkonstruktion.<br/>Spikbar.<br/>Kan återanvändas.', '33_gangad_spikkrage.png', pg, 'Gangad_spikkrage', False)
    db.session.add(p)
    db.session.add_all([
        ProductInfo('M10', 1, ganga, p), 
        ProductInfo('M12', 2, ganga, p),        
        ProductInfo('M16', 3, ganga, p),        
        ProductInfo('M20', 4, ganga, p),        
        ProductInfo('M24', 5, ganga, p),        
        ProductInfo('M27', 6, ganga, p),        
        ProductInfo('M30', 7, ganga, p),        
        ProductInfo('100', 1, antalforpSt, p),
        ProductInfo('100', 2, antalforpSt, p),
        ProductInfo('100', 3, antalforpSt, p),
        ProductInfo('100', 4, antalforpSt, p),
        ProductInfo('100', 5, antalforpSt, p),
        ProductInfo('100', 6, antalforpSt, p),
        ProductInfo('100', 7, antalforpSt, p),
        ProductInfo('Lagervara', 1, lagerstatus, p),
        ProductInfo('Lagervara', 2, lagerstatus, p),
        ProductInfo('Lagervara', 3, lagerstatus, p),
        ProductInfo('Lagervara', 4, lagerstatus, p),
        ProductInfo('Lagervara', 5, lagerstatus, p),
        ProductInfo('Ring oss', 6, lagerstatus, p),
        ProductInfo('Lagervara', 7, lagerstatus, p),
    ])

    # Limspikbricka #
    p = Product(u'Limspikbricka', u'Används för att fästa gängat lyft eller infästning i en prefabkonstruktion.<br/>Limbar.<br/>Kan återanvändas.', '43_limspikbricka.png', pg, 'Limspikbricka', False)
    db.session.add(p)
    db.session.add_all([
        ProductInfo('M8', 1, ganga, p), 
        ProductInfo('M10', 2, ganga, p),        
        ProductInfo('M12', 3, ganga, p),        
        ProductInfo('M16', 4, ganga, p),        
        ProductInfo('M20', 5, ganga, p),        
        ProductInfo('M24', 6, ganga, p),        
        ProductInfo('500', 1, antalforpSt, p),
        ProductInfo('500', 2, antalforpSt, p),
        ProductInfo('500', 3, antalforpSt, p),
        ProductInfo('500', 4, antalforpSt, p),
        ProductInfo('500', 5, antalforpSt, p),
        ProductInfo('500', 6, antalforpSt, p),
        ProductInfo('Lagervara', 1, lagerstatus, p),
        ProductInfo('Lagervara', 2, lagerstatus, p),
        ProductInfo('Lagervara', 3, lagerstatus, p),
        ProductInfo('Lagervara', 4, lagerstatus, p),
        ProductInfo('Lagervara', 5, lagerstatus, p),
        ProductInfo('Lagervara', 6, lagerstatus, p),
    ])


    ## Lister och rör ##
    pg = ProductGroup(u'Faslister, rör m.m.', '25_faslister.png', pc, u'Lister_och_ror')

    # Faslister #
    p = Product(u'Fastlister och andra plastlister/rör', u'Strängsprutade plastlister och rör.<br/>Finns i många olika profiler och dimensioner. Standardländ är 3 meter. <br/>Finns inte just den du vill ha kan vi, tillsammans med en av Sveriges ledande strängsprutare, ta fram de flesta varianter och utföranden.', '25_faslister.png', pg, 'Faslister', False)
    db.session.add(p)
    db.session.add_all([
        ProductInfo('22 x 10 x 5', 1, abc, p), 
        ProductInfo('32 x 10 x 6', 2, abc, p),        
        ProductInfo('24 x 10 x 5', 3, abc, p),        
        ProductInfo('28 x 15 x 5', 4, abc, p),        
        ProductInfo(u'Spikhål', 1, utforande, p),
        ProductInfo(u'Vit, spikhål', 2, utforande, p),
        ProductInfo(u'Spikhål', 3, utforande, p),
        ProductInfo(u'Spikhål', 4, utforande, p),
        ProductInfo('Lagervara', 1, lagerstatus, p),
        ProductInfo('Ring oss', 2, lagerstatus, p),
        ProductInfo('Lagervara', 3, lagerstatus, p),
        ProductInfo('Lagervara', 4, lagerstatus, p),
    ])

    # Ståltrekantslist #
    p = Product(u'Ståltrekantslist', u'Används för att få en snygg fas på stålformar. Svetsbar.', '80_trekantslist.jpg', pg, 'Staltrekantslist', False)
    db.session.add(p)
    db.session.add_all([
        ProductInfo(u'22 x 10 x 5', 1, abc, p), 
        ProductInfo(u'32 x 10 x 6', 2, abc, p),        
        ProductInfo(u'Spikhål', 1, langdMm, p),
        ProductInfo(u'Vit, spikhål', 2, langdMm, p),
        ProductInfo(u'Ring oss', 1, lagerstatus, p),
        ProductInfo(u'Ring oss', 2, lagerstatus, p),
    ])

    # Droppnäseprofiler #
    p = Product(u'Droppnäseprofiler', u'Plastlist för att göra s.k. ”Droppnäsor” i underkant av utstickande betongelement, tex balkonger.<br/>Fördelen med denna modell är att både fasen och droppnäsan sitter färdiga på samma list och man slipper extra mätande.', '21_droppnaseprofiler.png', pg, 'Droppnaseprofiler', False)
    db.session.add(p)
    db.session.add_all([
        ProductInfo('10 x 33 x 10', 1, abc, p), 
        ProductInfo('10 x 48 x 10', 2, abc, p),        
        ProductInfo('12 x 55 x 16', 3, abc, p),        
        ProductInfo('2000', 1, langdMm, p),
        ProductInfo('2000', 2, langdMm, p),
        ProductInfo('2000', 3, langdMm, p),
        ProductInfo('40', 1, antalforpSt, p),
        ProductInfo('40', 2, antalforpSt, p),
        ProductInfo('40', 3, antalforpSt, p),
        ProductInfo('Ring oss', 1, lagerstatus, p),
        ProductInfo('Ring oss', 2, lagerstatus, p),
        ProductInfo('Lagervara', 3, lagerstatus, p),
    ])
    
    # Avstängarlist #
    p = Product(u'Avstängarlist', u'Används för att förhindra att fukt tränger ner i källargrundsisolering.<br/>Finns i två storlekar, 70 och 105 mm.<br/>Längd 4000mm.', '10_avstangarlist.png', pg, 'Avstangarlist', False)
    db.session.add(p)
    
    # Dubbursparing KORP #
    p = Product(u'Dubbursparing KORP', u'En ny modell av dubbursparing, i första hand för 20 mm dubb. Den är tvådelad, det förenklar vid fastsättandet i formen.<br/>Locket monteras i formsidan. När huvudarmeringen och tilläggsarmeringen är nedlagda i formen sätts rördelen dit. Detta innebär att den inte rivs bort eller hamnar snett. Den har en täckande plasthinna som förhindrar att det kommer in grus och vatten.<br/>Locket: 75x75 mm<br/>Rördelen: 160 mm<br/>Antal/förpackning: 450 st<br/>Lagervara','41_dubbsparing_korp.png', pg, 'Dubbursparing_korp', False)
    db.session.add(p)

    # Dubbursparing GÖK #
    p = Product(u'Dubbursparing GÖK', u'Samma användningsområde och specifikationer som Dubbursparing KORP, med skillnaden att den är anpassad för rör på 100mm.<br/>Lagervara', '31_dubbsparing_gok.png', pg, 'Dubbursparing_gok', False)
    db.session.add(p)

    # KAMEL #
    p = Product(u'Kraftfogsursparing KAMEL', u'Kamelen är en list för att skapa en fog för kraftöverföring mellan prefabväggar och liknande konstruktioner. Den har många andra benämningar, varav hönstrappa, puckelpist och förtagningslist är de vanligaste. Kamelen kan med fördel ersätta befintliga lister i trä, cellplast eller gummi då den är billigare än en trälist och tål att användas flera gånger.<br/>Kan monteras mot träform med spik eller skruv, mot stålform med magnet eller vår egna list, Kamelspåret.<br/>Har en mycket slät och fin yta vilket gör den lätt att ta bort.<br/>Mycket tålig vid varsam hantering.<br/>Tål alla former av formoljor, formvax mm.<br/>Längd: 615 mm<br/>Bredd: 72 mm<br/>Höjd: 20/38 mm<br/>Antal/förpackning: 50 st (30 meter)<br/>Lagervara', '39_kraftfogsursparing_kamel.png', pg, 'Kraftfogsursparing_kamel', False)
    db.session.add(p)

     # KAMELSPÅRET #
    p = Product(u'KAMELSPÅRET', u'Lock/list till Kraftfogsursparing KAMEL. Tillåter kamelen att användas på många fler ställen.<br/>Med locket monterat går kamelen utmärkt att användas ovanifrån, det är bara att doppa ner den i betongen där man vill ha den.<br/>Locket kan fungera som förlängare då själva kamelen är 615 mm och locket är metervara, så nu kan kamelen bli så lång som man önskar.<br/>Locket underlättar dessutom montering på stålsidor: limma fast locket och snäpp därefter fast kamelen.<br/>Längd: 1200 mm.<br/>Lagervara.', '38_kamelsparet.png', pg, 'Kamelsparet', False)
    db.session.add(p)


    # Dubbursparing #
    p = Product(u'Dubbursparing', u'Ett snabbt och enkelt sätt att skapa ursparingen för styrdubben.<br/>Man slipper merjobb med cellplastbitar.<br/>Finns även möjlighet att bygga på med förlängare och lock som underlättar montering och gör det enklare att få en snygg lagning.', '45_dubbursparing.png', pg, 'Dubbursparing', False)
    db.session.add(p)
    db.session.add_all([
        ProductInfo('DBBT', 1, artnr, p), 
        ProductInfo('DBBF50', 2, artnr, p),        
        ProductInfo('DBBF25', 3, artnr, p),        
        ProductInfo('DBBL', 4, artnr, p),        
        ProductInfo('Dubbursparing tub', 1, benamning, p),
        ProductInfo(u'Dubbursparing förlängare 50mm', 2, benamning, p),
        ProductInfo(u'Dubbursparing förlängare 25mm', 3, benamning, p),
        ProductInfo('Dubbursparing lock', 4, benamning, p),
        ProductInfo('50', 1, antalforpSt, p),
        ProductInfo('200', 2, antalforpSt, p),
        ProductInfo('400', 3, antalforpSt, p),
        ProductInfo('400', 4, antalforpSt, p),
        ProductInfo('Lagervara', 1, lagerstatus, p),
        ProductInfo('Lagervara', 2, lagerstatus, p),
        ProductInfo('Lagervara', 3, lagerstatus, p),
        ProductInfo('Lagervara', 4, lagerstatus, p),
    ])
    
    # T-List #
    p = Product(u'T-List', u'Används som underkantsavstängare på valv. Armeringen läggs i urklippta urtag på T-listen.<br/>Höjd 42 mm.<br/>Bredd 42 mm.<br/>Längd 2500 mm.<br/>Levereras med 100 eller 150 mm c/c mellan urtagen.<br/>Kan även levereras utan urtag.', '61_tlist.png', pg, 'T_list', False)
    db.session.add(p)

    # Plaströr #
    p = Product(u'Plaströr', u'Lettrade, runda rör i längder om 2000 mm.<br/>Har flera användningsområden men används vanligast som distans mellan väggformar då den kapas i rätt längd och används tillsammans med invändig kona RIK samt tätningsplugg RTP.', '57_plastror.png', pg, 'Plastror', False)
    db.session.add(p)
    db.session.add_all([
        ProductInfo('260', 1, typ, p), 
        ProductInfo('290', 2, typ, p),        
        ProductInfo(u'Kona invändig (RIK)', 3, typ, p),        
        ProductInfo(u'Plugg (RTP)', 4, typ, p),        
        ProductInfo('22/26', 1, diamInUt, p),
        ProductInfo(u'22/26', 2, diamInUt, p),
        ProductInfo(u'22', 3, diamInUt, p),
        ProductInfo('22', 4, diamInUt, p),
        ProductInfo('-', 1, antalforpSt, p),
        ProductInfo('-', 2, antalforpSt, p),
        ProductInfo('-', 3, antalforpSt, p),
        ProductInfo('-', 4, antalforpSt, p),
        ProductInfo('Ring oss', 1, lagerstatus, p),
        ProductInfo('Ring oss', 2, lagerstatus, p),
        ProductInfo('Ring oss', 3, lagerstatus, p),
        ProductInfo('Ring oss', 4, lagerstatus, p),
    ])

    ## Plugg och skydd ##
    pg = ProductGroup(u'Plugg och skydd', '49_plastplugg.png', pc, u'Plugg_och_skydd')

    
    # Plastplugg #
    p = Product(u'Plastplugg', u'Konisk plastplugg, främst avsedd för att skydda invändiga eller utvändiga M-gängor. Kan även användas överallt där man behöver täppa igen ett hål.Utöver det standardsortiment som vi erbjuder, kan vi snabbt få fram pluggar i andra dimensioner.<br/>Tillverkad i röd polyetenplast. Vi kan även ta fram pluggar i andra färger, men det kan innebära vissa minimikvantiteter vid beställning.', '49_plastplugg.png', pg, 'Plastplugg', False)
    db.session.add(p)
    db.session.add_all([
        ProductInfo('M6', 1, ganga, p), 
        ProductInfo('M8', 2, ganga, p),        
        ProductInfo('M10', 3, ganga, p),        
        ProductInfo('M12', 4, ganga, p),        
        ProductInfo('M16', 5, ganga, p),        
        ProductInfo('M20', 6, ganga, p),        
        ProductInfo('M24', 7, ganga, p),        
        ProductInfo('M30', 8, ganga, p),        
        ProductInfo('1000', 1, antalforpSt, p),
        ProductInfo('1000', 2, antalforpSt, p),
        ProductInfo('1000', 3, antalforpSt, p),
        ProductInfo('1000', 4, antalforpSt, p),
        ProductInfo('1000', 5, antalforpSt, p),
        ProductInfo('1000', 6, antalforpSt, p),
        ProductInfo('1000', 7, antalforpSt, p),
        ProductInfo('500', 8, antalforpSt, p),
        ProductInfo('Lagervara', 1, lagerstatus, p),
        ProductInfo('Lagervara', 2, lagerstatus, p),
        ProductInfo('Lagervara', 3, lagerstatus, p),
        ProductInfo('Lagervara', 4, lagerstatus, p),
        ProductInfo('Lagervara', 5, lagerstatus, p),
        ProductInfo('Lagervara', 6, lagerstatus, p),
        ProductInfo('Lagervara', 7, lagerstatus, p),
        ProductInfo('Lagervara', 8, lagerstatus, p),
    ])

    # Skyddsknopp #
    p = Product(u'Skyddsknopp', u'Används för att skydda mot utstickande armeringsjärn, exempelvis kvastar som sticker upp ur ett golv, ut från en balkong eller dylikt.<br/>Ett avklippt armeringsjärn med Ø 12 mm som sticker upp en halv meter är en potentiell dödsfälla, därför bör man täcka dessa järn med skyddsknoppar både för att de skall synas bra och för att risken för skador skall minimeras.<br/>Levereras i klar, röd färg.', '55_skyddsknopp.png', pg, 'Skyddsknopp', True)
    db.session.add(p)
    db.session.add_all([
        ProductInfo('8-16', 1, diameter, p), 
        ProductInfo('16-32', 2, diameter, p),        
        ProductInfo('1800', 1, antalforpSt, p),
        ProductInfo('250', 2, antalforpSt, p),
        ProductInfo('Lagervara', 1, lagerstatus, p),
        ProductInfo('Lagervara', 2, lagerstatus, p),
    ])

    # Kil GRÄVLING #
    p = Product(u'Kil GRÄVLING', u'Rillad kil i tre olika storlekar, kallas vanligen KK-kil.<br/>Används bland annat vid inpassning av fönster, dörrar och alla andra tänkbara och otänkbara ändamål.', '32_kil_gravling.png', pg, 'Kil_gravling', False)
    db.session.add(p)
    db.session.add_all([
        ProductInfo('30 x 70 x 10', 1, blh, p),        
        ProductInfo('44 x 85 x 17', 2, blh, p), 
        ProductInfo('44 x 135 x 25', 3, blh, p),        
        ProductInfo(u'Grön', 1, farg, p),
        ProductInfo(u'Brun', 2, farg, p),
        ProductInfo(u'Gul', 3, farg, p),
        ProductInfo('500', 1, antalforpSt, p),
        ProductInfo('200', 2, antalforpSt, p),
        ProductInfo('250', 3, antalforpSt, p),
        ProductInfo('Lagervara', 1, lagerstatus, p),
        ProductInfo('Lagervara', 2, lagerstatus, p),
        ProductInfo('Lagervara', 3, lagerstatus, p),
    ])

    ## Förtagningslådar ##
    pg = ProductGroup(u'Förtagningslådor', '8_fortagningslador.png', pc, u'Fortagningslador')

    
    # Förtagningslådor #
    p = Product(u'Förtagningslådor', u'Även kallade Comaxlådor.<br/>Låda innehållande bockade armeringsjärn, så kallade byglar, vilka kan bockas ut när locket tas bort.<br/>Används för fortsatt gjutning mot tidigare gjutning som har brunnit. <br/><br/>Finns i lådbredderna: 70, 110, 150, 190, 240 och 290 mm.<br/>Järndimensioner: 8, 10 och 12 mm.<br/> Normala bygelavstånd: 150, 200, 250 och 300 mm.<br/>Leveranstid: 1- 2 dagar efter beställning. <br/><br/>Lådor med andra mått, järn och bygelavstånd kan specialtillverkas efter kundens önskemål. Leveranstid för dessa specialvarianter är minst 1 vecka.', '8_fortagningslador.png', pg, 'Fortagningslador', False)
    db.session.add(p)

    ## Diverse ##
    pg = ProductGroup(u'Diverse', '29_formstag.png', pc, u'Diverse')

    # Formstag och tillbehör #
    p = Product(u'Formstag och tillbehör', u'Används för att hålla ihop två formsidor under gjutningen.<br/>Finns i flera olika utföranden, exempelvis med fri ände eller med ändknopp. Finns även för de flesta olika gjuttjocklekar. Ring gärna oss om Ni är osäkra på vilket formstag ni eller er kund vill ha, vi hjälper gärna till!<br/>Vi levererar alla vanliga modeller samt specialutföranden.<br/>Snabba leveranstider, även för special.', '29_formstag.png', pg, 'Formstag_tillbehor', False)
    db.session.add(p)


    # Utsättningskloss #
    p = Product(u'Utsättningskloss', u'Kraftig rund kloss, diameter 48 mm. Används som mothåll när man monterar väggformar.<br/>Skjuts fast i underlaget före väggformsmontage.<br/>Levereras med eller utan förmonterad spik.', '63_utsattningskloss.png', pg, 'Utsattningskloss', True)
    db.session.add(p)
    db.session.add_all([
        ProductInfo('48', 1, diameter, p), 
        ProductInfo('48', 2, diameter, p),        
        ProductInfo('Ja', 1, spik, p),        
        ProductInfo('Nej', 2, spik, p),        
        ProductInfo('500', 1, antalforpSt, p),
        ProductInfo('500', 2, antalforpSt, p),
        ProductInfo('Ring oss', 1, lagerstatus, p),
        ProductInfo('Ring oss', 2, lagerstatus, p),
    ])

    # Plåtursparingar #
    p = Product(u'Plåtursparingar: runda och rektangulära', u'Kvarsittande plåtursparing av sinusprofilerad svart plåt. Används vid valvgenomförningar, maskinfundament, bultmontage m.m.<br/>Rund finns i diametern 100 till 1000 mm.<br/>Kan specialdesignas efter kundens önskemål. Kan levereras med lock och botten. Finns även med fästband.', '50_platursparingar.png', pg, 'Platursparing', False)
    db.session.add(p)

    # Dubbar #
    p = Product(u'Brodubb, Loddubb och Rostfri dubb', u'<b>Brodubb:</b> Avvägningsdubb av mässing med rundad topp. Ingjutes eller inborras i kantbalk som punkt. Godkänd av vägverket. Dimension 100x10 mm.<br/><br/><b>Loddubb:</b> Diameter 10 mm, längd 125 mm. Med spår för lodlina.<br/><br/><b>Rostfri dubb:</b> Diameter 10 mm, längd 100 mm. Används till elektrokemisk potentialmätning.', '68_brodubb.png', pg, 'Dubbar', False)
    db.session.add(p)

    # Pappursparing #
    p = Product(u'Pappursparingar för gjutning', u'Papprör avsedda för gjutning av fundament, plintar m.m. Finns som standard i dimensionerna 150, 190, 300, 400, 500 och 600 mm.<br/>Standardlängd 2900 mm. Rör av andra dimensioner tas fram på beställning.<br/>De flesta dimensioner levereras inom 2 veckor.', '48_pappusparingar.png', pg, 'Pappursparing', False)
    db.session.add(p)

    # Gjutavstängare #
    p = Product(u'Gjutavstängare', u'Avstängare för gjutning, både temporär och kvarsittande.<br/>Finns i flertalet olika utformningar och med olika speciallösningar. Fråga oss efter just den du vill ha!', 'missing.png', pg, 'Gjutavstangare', False)
    db.session.add(p)

    # Märkbrickor #
    p = Product(u'Märkbrickor', u'Märkbrickan är, som namnet antyder, en bricka av plast som används för att märka olika saker, exempelvis en armeringskonstruktion.<br/>Plasten i brickan går att skriva på med en tuschpenna, men vanligen används självhäftande etiketter.<br/>Finns i storlekarna: 40x70, 70x90 och 70x120 mm. Finns i färgerna vit, gul, röd blå och grön.<br/>Går att få både med och utan tråd.', '44_markbrickor.png', pg, 'Markbrickor', False)
    db.session.add(p)

    
    ###### -- Formsättning -- ######
    pc = ProductCategory(u'Formsättning')
    db.session.add(pc)
   
    pg = ProductGroup(u'Magfly', 'Missing.png', pc, u'Magfly')
    db.session.add(pg)
    
    p = Product('Formbordsmagnet typ K', u'Även populärt kallad våffelmagnet.<br/>Allroundmagnet, går att tillsammans med lika applikationer att använda till det mesta som kan behöver på ett stålbord, applikationerna kan ni köpa av oss, eller tillverka er egen speciallösning. Fungerar naturligtvis alldeles utmärkt som bara magnet, är bra på att sitta i vägen', '70_magnet_typ_k.png', pg, 'Magfly_k', False)
    db.session.add(p)
 
    db.session.add_all([
        ProductInfo('MF1000K', 1, artnr, p),
        ProductInfo('MF1600K', 2, artnr, p),
        ProductInfo('MF2000K', 3, artnr, p),
        ProductInfo('MF2500K', 4, artnr, p),
        ProductInfo('MF3000K', 5, artnr, p),
        ProductInfo('1100', 1, magnetKraft, p),
        ProductInfo('1600', 2, magnetKraft, p),
        ProductInfo('2200', 3, magnetKraft, p),
        ProductInfo('2700', 4, magnetKraft, p),
        ProductInfo('3300', 5, magnetKraft, p),
        ProductInfo('5', 1, viktKg, p),
        ProductInfo('7.5', 2, viktKg, p),
        ProductInfo('10', 3, viktKg, p),
        ProductInfo('12.5', 4, viktKg, p),
        ProductInfo('15', 5, viktKg, p),
       ])

    p = Product(u'Adaptrar för formbordsmagnet typ K', u'Det finns många färdiga adaptrar för formbordssmaget typ K, alla ger möjligheter att använda K magneten på de mest olika sätt.<br/>Här finner ni bilder och beskrivning på ett urval av dem. Det finns fler, så fråga oss alltid om ni behöver någon speciallösning. Vi och vår leverantör är mycket positiva till att ta fram kundanpassade lösningar.', '71_adapter_multiform.jpg', pg, 'Magfly_k_adaptrar', False)
    db.session.add(p)
 
        
    p = Product(u'Magnetfot typ GB', u'<b>Magnetfäste för gängad infästning typ GB.</b><br/>Vår magnet för gängat är av stål, det finns för och nackdelar med stål kontra gummi, fördelen är hållbarheten, en i stål klarar betydligt fler gjutningar än en i gummi, en nackdel är att ytorna i ursparingen inte är lika fina, om det nu har någon betydelse.<br/>Andra fördelar med vår magnet är att det är enkelt att byta gängstorlek på dem, gängtapparna sitter fast med en segersäkring på undersidan, ta bara bort den, så lossa gängtappen och kan bytas till annan dimension, alla olika gängdimensioner passa i samma magnet.<br/>Magnetplattorna finns i fyra olika storlekar, med olika magnetkraft. Plattorna och tapparna kan paras ihop efter eget önskemål.<br/>Lätta att hålla rena, tål alla sorter av formsläppingsmedel. Är lätta att lossa efter användandet.', '72_magnet_typ_gb.png', pg, 'Magnetfot_gangtapp', False)
    db.session.add(p)
 
    db.session.add_all([
        ProductInfo('MFGB50', 1, artnr, p),
        ProductInfo('MFGB64', 2, artnr, p),
        ProductInfo('MFGB80', 3, artnr, p),
        ProductInfo('MFGB106', 4, artnr, p),
        ProductInfo('MFGB5010', 5, artnr, p),
        ProductInfo('MFGB5012', 6, artnr, p),
        ProductInfo('MFGB5016', 7, artnr, p),
        ProductInfo('MFGB5020', 8, artnr, p),
        ProductInfo('MFGB5024', 9, artnr, p),
        ProductInfo('MFGB5030', 10, artnr, p),
        ProductInfo('MFGB5036', 11, artnr, p),
        ProductInfo(u'', 1, ganga, p),
        ProductInfo(u'', 2, ganga, p),
        ProductInfo(u'', 3, ganga, p),
        ProductInfo(u'', 4, ganga, p),
        ProductInfo(u'M10', 5, ganga, p),
        ProductInfo(u'M12', 6, ganga, p),
        ProductInfo(u'M16', 7, ganga, p),
        ProductInfo(u'M20', 8, ganga, p),
        ProductInfo(u'M24', 9, ganga, p),
        ProductInfo(u'M30', 10, ganga, p),
        ProductInfo(u'M36', 11, ganga, p),
        ProductInfo(u'', 1, tapphojd, p),
        ProductInfo(u'', 2, tapphojd, p),
        ProductInfo(u'', 3, tapphojd, p),
        ProductInfo(u'', 4, tapphojd, p),
        ProductInfo(u'20', 5, tapphojd, p),
        ProductInfo(u'20', 6, tapphojd, p),
        ProductInfo(u'20', 7, tapphojd, p),
        ProductInfo(u'20', 8, tapphojd, p),
        ProductInfo(u'20', 9, tapphojd, p),
        ProductInfo(u'20', 10, tapphojd, p),
        ProductInfo(u'20', 11, tapphojd, p),
        ProductInfo('650', 1, magnetKraft, p),
        ProductInfo('1000', 2, magnetKraft, p),
        ProductInfo('1500', 3, magnetKraft, p),
        ProductInfo('1900', 4, magnetKraft, p),
        ProductInfo('', 5, magnetKraft, p),
        ProductInfo('', 6, magnetKraft, p),
        ProductInfo('', 7, magnetKraft, p),
        ProductInfo('', 8, magnetKraft, p),
        ProductInfo('', 9, magnetKraft, p),
        ProductInfo('', 10, magnetKraft, p),
        ProductInfo('', 11, magnetKraft, p),
        ProductInfo('0.13', 1, viktKg, p),
        ProductInfo('0.23', 2, viktKg, p),
        ProductInfo('0.4', 3, viktKg, p),
        ProductInfo('0.75', 4, viktKg, p),
        ProductInfo('', 5, viktKg, p),
        ProductInfo('', 6, viktKg, p),
        ProductInfo('', 7, viktKg, p),
        ProductInfo('', 8, viktKg, p),
        ProductInfo('', 9, viktKg, p),
        ProductInfo('', 10, viktKg, p),
        ProductInfo('', 11, viktKg, p),
        ProductInfo('50', 1, breddBotten, p),
        ProductInfo('64', 2, breddBotten, p),
        ProductInfo('80', 3, breddBotten, p),
        ProductInfo('106', 4, breddBotten, p),
        ProductInfo('', 5, breddBotten, p),
        ProductInfo('', 6, breddBotten, p),
        ProductInfo('', 7, breddBotten, p),
        ProductInfo('', 8, breddBotten, p),
        ProductInfo('', 9, breddBotten, p),
        ProductInfo('', 10, breddBotten, p),
        ProductInfo('', 11, breddBotten, p),
        ProductInfo('47', 1, breddToppen, p),
        ProductInfo('61', 2, breddToppen, p),
        ProductInfo('77', 3, breddToppen, p),
        ProductInfo('103', 4, breddToppen, p),
        ProductInfo('', 5, breddToppen, p),
        ProductInfo('', 6, breddToppen, p),
        ProductInfo('', 7, breddToppen, p),
        ProductInfo('', 8, breddToppen, p),
        ProductInfo('', 9, breddToppen, p),
        ProductInfo('', 10, breddToppen, p),
        ProductInfo('', 11, breddToppen, p),
        ProductInfo('12', 1, hojdLateOrder, p),
        ProductInfo('12', 2, hojdLateOrder, p),
        ProductInfo('12', 3, hojdLateOrder, p),
        ProductInfo('12', 4, hojdLateOrder, p),
        ProductInfo('', 5, hojdLateOrder, p),
        ProductInfo('', 6, hojdLateOrder, p),
        ProductInfo('', 7, hojdLateOrder, p),
        ProductInfo('', 8, hojdLateOrder, p),
        ProductInfo('', 9, hojdLateOrder, p),
        ProductInfo('', 10, hojdLateOrder, p),
        ProductInfo('', 11, hojdLateOrder, p),
        ProductInfo('M10 - M16', 1, rekTappstrlk, p),
        ProductInfo('M12 - M24', 2, rekTappstrlk, p),
        ProductInfo('M16 - M30', 3, rekTappstrlk, p),
        ProductInfo('M20 - M36', 4, rekTappstrlk, p),
        ProductInfo('', 5, rekTappstrlk, p),
        ProductInfo('', 6, rekTappstrlk, p),
        ProductInfo('', 7, rekTappstrlk, p),
        ProductInfo('', 8, rekTappstrlk, p),
        ProductInfo('', 9, rekTappstrlk, p),
        ProductInfo('', 10, rekTappstrlk, p),
        ProductInfo('', 11, rekTappstrlk, p),
       ])

     

    p = Product(u'Magnetfäste för kulankare typ KU', u'Vår magnet för gängat är av stål, det finns för och nackdelar med stål kontra gummi, fördelen är hållbarheten, en i stål klarar betydligt fler gjutningar än en i gummi, en nackdel är att ytorna i ursparingen inte är lika fina, om det nu har någon betydelse.<br/>Lätta att hålla rena, tål alla sorter av formsläppingsmedel. Är lätta att lossa efter användandet.<br>Artikelnummer som slutar på G är tillhörande gummiringar.', '73_magnet_typ_ku.png', pg, 'Magnetfot_kulankare', False)
    db.session.add(p)
 
    db.session.add_all([
        ProductInfo('MFKU13', 1, artnr, p),
        ProductInfo('MFKU25', 2, artnr, p),
        ProductInfo('MFKU35', 3, artnr, p),
        ProductInfo('MFKU75', 4, artnr, p),
        ProductInfo('MFKU10', 5, artnr, p),
        ProductInfo('MFKU13G', 6, artnr, p),
        ProductInfo('MFKU25G', 7, artnr, p),
        ProductInfo('MFKU35G', 8, artnr, p),
        ProductInfo('MFKU75G', 9, artnr, p),
        ProductInfo('MFKU10G', 10, artnr, p),
        ProductInfo('100', 1, magnetKraft, p),
        ProductInfo('100', 2, magnetKraft, p),
        ProductInfo('150', 3, magnetKraft, p),
        ProductInfo('200', 4, magnetKraft, p),
        ProductInfo('220', 5, magnetKraft, p),
        ProductInfo('', 6, magnetKraft, p),
        ProductInfo('', 7, magnetKraft, p),
        ProductInfo('', 8, magnetKraft, p),
        ProductInfo('', 9, magnetKraft, p),
        ProductInfo('', 10, magnetKraft, p),
        ProductInfo('0.49', 1, viktKg, p),
        ProductInfo('0.65', 2, viktKg, p),
        ProductInfo('2.5', 3, viktKg, p),
        ProductInfo('3.3', 4, viktKg, p),
        ProductInfo('3.3', 5, viktKg, p),
        ProductInfo('', 6, viktKg, p),
        ProductInfo('', 7, viktKg, p),
        ProductInfo('', 8, viktKg, p),
        ProductInfo('', 9, viktKg, p),
        ProductInfo('', 10, viktKg, p),
        ProductInfo('66', 1, breddBotten, p),
        ProductInfo('74', 2, breddBotten, p),
        ProductInfo('104', 3, breddBotten, p),
        ProductInfo('118', 4, breddBotten, p),
        ProductInfo('118', 5, breddBotten, p),
        ProductInfo('', 6, breddBotten, p),
        ProductInfo('', 7, breddBotten, p),
        ProductInfo('', 8, breddBotten, p),
        ProductInfo('', 9, breddBotten, p),
        ProductInfo('', 10, breddBotten, p),
        ProductInfo('20.5', 1, breddToppen, p),
        ProductInfo('27.5', 2, breddToppen, p),
        ProductInfo('38.5', 3, breddToppen, p),
        ProductInfo('48.5', 4, breddToppen, p),
        ProductInfo('48.5', 5, breddToppen, p),
        ProductInfo('', 6, breddToppen, p),
        ProductInfo('', 7, breddToppen, p),
        ProductInfo('', 8, breddToppen, p),
        ProductInfo('', 9, breddToppen, p),
        ProductInfo('', 10, breddToppen, p),
        ProductInfo('30.8', 1, hojdLateOrder, p),
        ProductInfo('33', 2, hojdLateOrder, p),
        ProductInfo('50.5', 3, hojdLateOrder, p),
        ProductInfo('53', 4, hojdLateOrder, p),
        ProductInfo('54', 5, hojdLateOrder, p),
        ProductInfo('', 6, hojdLateOrder, p),
        ProductInfo('', 7, hojdLateOrder, p),
        ProductInfo('', 8, hojdLateOrder, p),
        ProductInfo('', 9, hojdLateOrder, p),
        ProductInfo('', 10, hojdLateOrder, p),
        ProductInfo('1.3 ton', 1, tillAnkare, p),
        ProductInfo('2.5 ton', 2, tillAnkare, p),
        ProductInfo('3/5 ton', 3, tillAnkare, p),
        ProductInfo('7.5 ton', 4, tillAnkare, p),
        ProductInfo('10 ton', 5, tillAnkare, p),
        ProductInfo('1.3 ton', 6, tillAnkare, p),
        ProductInfo('2.5 ton', 7, tillAnkare, p),
        ProductInfo('3/5 ton', 8, tillAnkare, p),
        ProductInfo('7.5 ton', 9, tillAnkare, p),
        ProductInfo('10 ton', 10, tillAnkare, p),
       ])

    p = Product('Formbordsmagnet typ BR', u'Även populärt kallad våffelmagnet.<br/>Är i första hand avsedd att sitta inne i en U-stålprofil med måtten 60x70 mm.<br/>Naturligtvis går BR magneten att använda till annat också, det är nog bara fantasin som sätter gränser på de olika användningsområdena', '74_magnet_typ_br.png', pg, 'Magfly_br', False)
    db.session.add(p)
 
    db.session.add_all([
        ProductInfo('MFBR30185', 1, artnr, p),
        ProductInfo('MFBR40153', 2, artnr, p),
        ProductInfo('MFBR5097', 3, artnr, p),
        ProductInfo('MFBR50140', 4, artnr, p),
        ProductInfo('MFBR50185', 5, artnr, p),
        ProductInfo('MFBR50230', 6, artnr, p),
        ProductInfo('MFBRAV', 7, artnr, p),
        ProductInfo('Magnet typ BR', 1, benamning, p),
        ProductInfo('Magnet typ BR', 2, benamning, p),
        ProductInfo('Magnet typ BR', 3, benamning, p),
        ProductInfo('Magnet typ BR', 4, benamning, p),
        ProductInfo('Magnet typ BR', 5, benamning, p),
        ProductInfo('Magnet typ BR', 6, benamning, p),
        ProductInfo(u'Avformingsverktyg för BR', 7, benamning, p),
        ProductInfo('750', 1, magnetKraft, p),
        ProductInfo('750', 2, magnetKraft, p),
        ProductInfo('450', 3, magnetKraft, p),
        ProductInfo('650', 4, magnetKraft, p),
        ProductInfo('800', 5, magnetKraft, p),
        ProductInfo('1000', 6, magnetKraft, p),
        ProductInfo('', 7, magnetKraft, p),
        ProductInfo('2.2', 1, viktKg, p),
        ProductInfo('2.5', 2, viktKg, p),
        ProductInfo('1.7', 3, viktKg, p),
        ProductInfo('2.5', 4, viktKg, p),
        ProductInfo('3.3', 5, viktKg, p),
        ProductInfo('4.1', 6, viktKg, p),
        ProductInfo('2', 7, viktKg, p),
       ])


    p = Product('Formbordsmagnet typ FP', u'Magnetsystem huvudsakligen avsedd för kvarsittande formsida, men fungerar även vid fastsättning av andra typer av formsidor.<br/> Levereras komplett, men delarna går att köpa var för sig', '75_magnet_typ_fp.png', pg, 'Magfly_fp', False)
    db.session.add(p)
 
    db.session.add_all([
        ProductInfo('MFFP240', 1, artnr, p),
        ProductInfo('MFFP300', 2, artnr, p),
        ProductInfo('MFFP400', 3, artnr, p),
        ProductInfo('Magnet typ FP', 1, benamning, p),
        ProductInfo('Magnet typ FP', 2, benamning, p),
        ProductInfo('Magnet typ FP', 3, benamning, p),
        ProductInfo('500', 1, magnetKraft, p),
        ProductInfo('500', 2, magnetKraft, p),
        ProductInfo('500', 3, magnetKraft, p),
        ProductInfo('5', 1, viktKg, p),
        ProductInfo('7.5', 2, viktKg, p),
        ProductInfo('10', 3, viktKg, p),
       ])

    p = Product('Formsidesmagnet AP2200', u'Vår mest sålda magnet, designad för att klara den tuffa miljön i en prefabfabrik, de få rörliga delar som finns är väl skyddade, och går ändå lätt att rengöra. Tål betongdamm och betongspill bra. Inget separat avformningsverktyg behövs, det är inkluderat i magneten.<br/>Är anpassad för användning tillsammans med Multiform formsidesadaptrar system, men går utmärkt att använda med andra formsidor med en adapter typ 1, vilken kan antingen skruvas eller svetsas i befintlig formsida.<br/><br/>Dragkraft 2200 kn<br/>Vikt 5,4 kg<br/>Total höjd inklusive avformningsarm (h2) = 100 mm<br/>Höjd exklusive avformningsarm (h1) = 76 mm<br/>Total bredd inklusive avformningsarm (b2) = 130 mm<br/>Bredd vid anslutning till stålbord (b1) = 96 mm<br/>Total längd inklusive avformningsarm  (l2) =  385 mm<br/>Längd vid anslutning till stålbord (l1) = 260 mm', '69_ap_magnet.jpg', pg, 'Formsidesmaget_ap2200', False)
    db.session.add(p)
    
    p = Product('Formsidesmagnet AP2000', u'AP2200 får en lillebror med namn AP2000. Den största skillnaden är dess låga höjd och smala bredd. AP2000 är fortfarande i prototypstadiet, alla mått är inte helt klara än, men efterhand som de är klara kommer vi att uppdatera detta produktblad.<br/>Den har samma fördelar som AP när det gäller tålighet och praktisk användning, den är dock inte anpassad efter vår formsidessystem Multiform typ 2 utan skall användas med Multiform adapter typ 1.<br/><br/>Dragkraft 2000 kn<br/>Vikt ?<br/>Total höjd inklusive avformningsarm = 75 mm<br/>Höjd exklusive avformningsarm = ?<br/>Total bredd inklusive avformningsarm = 65 mm<br/>Total längd inklusive avformningsarm (i2) = ?<br/>Längd vid anslutning till stålbord (i1) = ?', '86_AP_2000.png', pg, 'Formsidesmaget_ap2000', False)
    db.session.add(p)

    p = Product('Formbordsmagnet typ PL/E', u'Enkel magnet vars enda funktion är att sitta fast på en stålyta. Mycket flexibel flera användningsområde, ex fönsterursparingar, i sibbformar, m.m. Ett prisvärt och flexibelt alternativ.<br/>Finns med olika magnetkraft, se tabell.', '82_magnet_typ_ple.jpg', pg, 'Formbordsmagnet_typ_pl-e', False)
    db.session.add(p)

    db.session.add_all([
        ProductInfo('MFPLE400', 1, artnr, p),
        ProductInfo('MFPLE650', 2, artnr, p),
        ProductInfo('MFPLE850', 3, artnr, p),
		ProductInfo('Magnet typ PL/E', 1, benamning, p),
        ProductInfo('Magnet typ PL/E', 2, benamning, p),
        ProductInfo('Magnet typ PL/E', 3, benamning, p),
        ProductInfo(u'252 x 180 x 160', 1, blh, p),
        ProductInfo(u'252 x 180 x 160', 2, blh, p),
        ProductInfo(u'252 x 180 x 160', 3, blh, p),
        ProductInfo('400', 1, magnetKraft, p),
        ProductInfo('650', 2, magnetKraft, p),
        ProductInfo('850', 3, magnetKraft, p),
        ProductInfo('3.7', 1, viktKg, p),
        ProductInfo('3.7', 2, viktKg, p),
        ProductInfo('3.7', 3, viktKg, p),
       ])

    p = Product(u'Magnet för eldosor Typ E', u'Magnet för elektriska dosor. Ny modell som är under utveckling, ring oss för mer information!', '87_eldosemagnet.png', pg, 'Magnet_eldosor_typ_e', False)
    db.session.add(p)

    p = Product(u'Magnet för rör Typ A', u'Magnet för rör. Ny modell som är under utveckling, ring oss för mer information!', '87_eldosemagnet.png', pg, 'Magnet_eldosor_typ_a', False)
    db.session.add(p)

    ###### LISTER MAGNETER ######

    pg = ProductGroup(u'Magnetlister', 'Missing.png', pc, u'Magnetlister')
    db.session.add(pg)
    
    p = Product('Magnetlister', u'Finns i olika storlekar och med olika magnetkraft. Kan även fås med magnet på två sidor eller andra dimensioner på förfrågan.', '76_trekantslist.jpg', pg, 'Magnetlister', False)
    db.session.add(p)
 
    db.session.add_all([
        ProductInfo('MCS1010E', 1, artnr, p),
        ProductInfo('MCS1010D', 2, artnr, p),
        ProductInfo('MCS1515E', 3, artnr, p),
        ProductInfo('MCS1515D', 4, artnr, p),
        ProductInfo('', 5, artnr, p),
        ProductInfo('MTT101515', 6, artnr, p),
        ProductInfo('MTT201010', 7, artnr, p),
        ProductInfo('MTT301020', 8, artnr, p),
        ProductInfo('MTT32106', 9, artnr, p),
        ProductInfo('MTT402020', 10, artnr, p),
        ProductInfo(u'Trekantslist av stål med en sida magnetisk', 1, benamning, p),
        ProductInfo(u'Trekantslist av stål med två sidor magnetiska', 2, benamning, p),
        ProductInfo(u'Trekantslist av stål med en sida magnetisk', 3, benamning, p),
        ProductInfo(u'Trekantslist av stål med två sidor magnetiska', 4, benamning, p),
        ProductInfo(u'', 5, benamning, p),
        ProductInfo(u'Blindfogslist magnetisk', 6, benamning, p),
        ProductInfo(u'Blindfogslist magnetisk', 7, benamning, p),
        ProductInfo(u'Blindfogslist magnetisk', 8, benamning, p),
        ProductInfo(u'Blindfogslist magnetisk', 9, benamning, p),
        ProductInfo(u'Blindfogslist magnetisk', 10, benamning, p),
        ProductInfo(u'10 x 10 x 20', 1, blh, p),
        ProductInfo(u'10 x 10 x 20', 2, blh, p),
        ProductInfo(u'15 x 15 x 20', 3, blh, p),
        ProductInfo(u'15 x 15 x 20', 4, blh, p),
        ProductInfo(u'', 5, blh, p),
        ProductInfo(u'10 x 10 x 15', 6, blh, p),
        ProductInfo(u'10 x 10 x 20', 7, blh, p),
        ProductInfo(u'10 x 20 x 30', 8, blh, p),
        ProductInfo(u'16 x 10 x 32', 9, blh, p),
        ProductInfo(u'20 x 20 x 40', 10, blh, p),
        ProductInfo(u'3000', 1, langdMm, p),
        ProductInfo(u'3000', 2, langdMm, p),
        ProductInfo(u'3000', 3, langdMm, p),
        ProductInfo(u'3000', 4, langdMm, p),
        ProductInfo(u'', 5, langdMm, p),
        ProductInfo(u'3000', 6, langdMm, p),
        ProductInfo(u'3000', 7, langdMm, p),
        ProductInfo(u'3000', 8, langdMm, p),
        ProductInfo(u'3000', 9, langdMm, p),
        ProductInfo(u'3000', 10, langdMm, p),
       ])

    
    ###### Formsidesadaptrar ######
    pg = ProductGroup(u'Formsidesadaptrar', 'Missing.png', pc, u'Formsidesadaptrar')
    db.session.add(pg)
    
    p = Product('Multiform typ 1', u'Formsidesadapter för bland annat AP magneten, när man har egna formsidor i trä eller stål.Utförande blankförzinkat stål', '78_multiform_typ_1.jpg', pg, 'multiform_typ_1', False)
    db.session.add(p)
 
    db.session.add_all([
        ProductInfo('MFT165', 1, artnr, p),
        ProductInfo('MFT170', 2, artnr, p),
        ProductInfo('MFT190', 3, artnr, p),
        ProductInfo('MFT148', 4, artnr, p),
        ProductInfo('MFT190', 5, artnr, p),
        ProductInfo('MFT1248', 6, artnr, p),
        ProductInfo(u'110 x 284 x 65', 1, blh, p),
        ProductInfo(u'110 x 284 x 70', 2, blh, p),
        ProductInfo(u'110 x 284 x 90', 3, blh, p),
        ProductInfo(u'110 x 284 x 148', 4, blh, p),
        ProductInfo(u'110 x 284 x 190', 5, blh, p),
        ProductInfo(u'110 x 284 x 248', 6, blh, p),
       ])

    p = Product('Multiform typ 2', u'Formsidesadapter i stål för i huvudsak AP magneten men magnet typ K med adapter fungerar också. Går oftast lätt att modifiera för att passa till andra modeller av formsidesmagneter.<br/>Låg vikt, mycket vridstyv och lätt att skruva plyfa mot då inga extra höjdstöd behövs oavsett höjd. Standardlängd 3050 mm, men det går enkelt att koppla ihop flera längder.', '83_multiform_typ_2.png', pg, 'multiform_typ_2', False)
    db.session.add(p)


    db.session.add_all([
        ProductInfo('MFT2983000', 1, artnr, p),
        ProductInfo('MFT21483000', 2, artnr, p),
        ProductInfo('MFT21983000', 3, artnr, p),
        ProductInfo('MFT22483000', 4, artnr, p),
        ProductInfo('MFT22983000', 5, artnr, p),
        ProductInfo('MFT23483000', 6, artnr, p),
        ProductInfo('MFT23983000', 7, artnr, p),
        ProductInfo('MFT24483000', 8, artnr, p),
        ProductInfo('MFT24983000', 9, artnr, p),
        ProductInfo('MFT25483000', 10, artnr, p),
        ProductInfo('MFT25983000', 11, artnr, p),
        ProductInfo('MFT26483000', 12, artnr, p),
        ProductInfo('MFT26983000', 13, artnr, p),
        ProductInfo(u'150 x 3050 x 65', 1, blh, p),
        ProductInfo(u'150 x 3050 x 70', 2, blh, p),
        ProductInfo(u'150 x 3050 x 90', 3, blh, p),
        ProductInfo(u'200 x 3050 x 148', 4, blh, p),
        ProductInfo(u'200 x 3050 x 190', 5, blh, p),
        ProductInfo(u'250 x 3050 x 248', 6, blh, p),
        ProductInfo(u'250 x 3050 x 248', 7, blh, p),
        ProductInfo(u'250 x 3050 x 248', 8, blh, p),
        ProductInfo(u'250 x 3050 x 248', 9, blh, p),
        ProductInfo(u'* x 3050 x 548', 10, blh, p),
        ProductInfo(u'* x 3050 x 598', 11, blh, p),
        ProductInfo(u'* x 3050 x 648', 12, blh, p),
        ProductInfo(u'* x 3050 x 698', 13, blh, p),
        ProductInfo('12.9', 1, viktKg, p),
        ProductInfo('17.8', 2, viktKg, p),
        ProductInfo('19.4', 3, viktKg, p),
        ProductInfo('23.6', 4, viktKg, p),
        ProductInfo('25.0', 5, viktKg, p),
        ProductInfo('29.7', 6, viktKg, p),
        ProductInfo('32.8', 7, viktKg, p),
        ProductInfo('35.4', 8, viktKg, p),
        ProductInfo('38.5', 9, viktKg, p),
        ProductInfo('*', 10, viktKg, p),
        ProductInfo('*', 11, viktKg, p),
        ProductInfo('*', 12, viktKg, p),
        ProductInfo('*', 13, viktKg, p),

       ])
 
    p = Product('Multiform typ Flyframe', u'Formsidesadapter i aluminium, samma fördelar som typ 2, men endast halva vikten', '84_multiform_typ_flyframe.png', pg, 'multiform_typ_flyframe', False)
    db.session.add(p)

    db.session.add_all([
        ProductInfo('MFFF98', 1, artnr, p),
        ProductInfo('MFFF198', 2, artnr, p),
        ProductInfo('MFFF298', 3, artnr, p),
        ProductInfo(u'180 x 3050 x 98', 1, blh, p),
        ProductInfo(u'180 x 3050 x 198', 2, blh, p),
        ProductInfo(u'180 x 3050 x 298', 3, blh, p),
        ProductInfo('8.1', 1, viktKg, p),
        ProductInfo('9.7', 2, viktKg, p),
        ProductInfo('11.3', 3, viktKg, p),
       ])
    
    p = Product(u'Tillbehör multiform', u'Det finns många olika tillbehör till Multiformsystemet. Nedan finns de vanligaste.<br/>Det finns fler och vi skräddarsyr gärna kundanpassade lösningar, kontakta oss för mer information.', 'multiform_toppformstag.jpg', pg, 'Tillbehor_multiform', False)
    db.session.add(p)

    
    ###### Färdiga adaptrar med magneter ######
    pg = ProductGroup(u'Färdiga adaptrar med magneter', 'Missing.png', pc, u'Adaptrar_med_magneter')
    db.session.add(pg)
    
    p = Product('MagPin', u'U-profilssystem med integrerade magneter.<br/>Lämplig vid gjutning av skalväggar och plattbärlag, även kallat filigranbärlag.<br/>Standarddimension, bredd 60 mm, höjd 70 mm, möjlig att få faser på en eller två sidor. Standard maxlängd 3000 mm.<br/>Går att få i andra dimensioner, och längder på beställning.<br/>Två olika magneter med olika dragkraft finns. Tabellen nedan visar standardlängder.', '79_magpin.png', pg, 'Magpin', False)
    db.session.add(p)
 
    db.session.add_all([
        ProductInfo('MP6070500', 1, artnr, p),
        ProductInfo('MP6070750', 2, artnr, p),
        ProductInfo('MP60701000', 3, artnr, p),
        ProductInfo('MP60701500', 4, artnr, p),
        ProductInfo('MP60702000', 5, artnr, p),
        ProductInfo('MP60702500', 6, artnr, p),
        ProductInfo('MP60703000', 7, artnr, p),
		ProductInfo('', 8, artnr, p),
		ProductInfo('MPM1054030', 9, artnr, p),
        ProductInfo('MPM2104030', 10, artnr, p),
        ProductInfo('MagPin 70x60 mm', 1, benamning, p),
        ProductInfo('MagPin 70x60 mm', 2, benamning, p),
        ProductInfo('MagPin 70x60 mm', 3, benamning, p),
        ProductInfo('MagPin 70x60 mm', 4, benamning, p),
        ProductInfo('MagPin 70x60 mm', 5, benamning, p),
        ProductInfo('MagPin 70x60 mm', 6, benamning, p),
        ProductInfo('MagPin 70x60 mm', 7, benamning, p),
        ProductInfo('', 8, benamning, p),
        ProductInfo(u'Magnet för magpin', 9, benamning, p),
        ProductInfo(u'Magnet för magpin', 10, benamning, p),
        ProductInfo(u'1', 1, antMagneter, p),
        ProductInfo(u'1', 2, antMagneter, p),
        ProductInfo(u'2', 3, antMagneter, p),
        ProductInfo(u'2', 4, antMagneter, p),
        ProductInfo(u'2', 5, antMagneter, p),
        ProductInfo(u'2', 6, antMagneter, p),
        ProductInfo(u'3', 7, antMagneter, p),
        ProductInfo(u'', 8, antMagneter, p),
        ProductInfo(u'', 9, antMagneter, p),
        ProductInfo(u'', 10, antMagneter, p),
        ProductInfo(u'500', 1, langdMm, p),
        ProductInfo(u'750', 2, langdMm, p),
        ProductInfo(u'1000', 3, langdMm, p),
        ProductInfo(u'1500', 4, langdMm, p),
        ProductInfo(u'2000', 5, langdMm, p),
        ProductInfo(u'2500', 6, langdMm, p),
        ProductInfo(u'3000', 7, langdMm, p),
        ProductInfo(u'', 8, langdMm, p),
        ProductInfo(u'', 9, langdMm, p),
        ProductInfo(u'', 10, langdMm, p),
		ProductInfo(u'', 1, blh, p),
		ProductInfo(u'', 2, blh, p),
		ProductInfo(u'', 3, blh, p),
		ProductInfo(u'', 4, blh, p),
		ProductInfo(u'', 5, blh, p),
		ProductInfo(u'', 6, blh, p),
		ProductInfo(u'', 7, blh, p),
		ProductInfo(u'', 8, blh, p),
		ProductInfo(u'40 x 105 x 30', 9, blh, p),
        ProductInfo(u'40 x 210 x 30', 10, blh, p),
        ProductInfo(u'8.5', 1, viktInklMagnet, p),
        ProductInfo(u'9.7', 2, viktInklMagnet, p),
        ProductInfo(u'17.0', 3, viktInklMagnet, p),
        ProductInfo(u'19.5', 4, viktInklMagnet, p),
        ProductInfo(u'22.0', 5, viktInklMagnet, p),
        ProductInfo(u'24.5', 6, viktInklMagnet, p),
        ProductInfo(u'33.0', 7, viktInklMagnet, p),
        ProductInfo(u'', 8, viktInklMagnet, p),
        ProductInfo(u'', 9, viktInklMagnet, p),
        ProductInfo(u'', 10, viktInklMagnet, p),
		ProductInfo(u'', 1, magnetKraft, p),
		ProductInfo(u'', 2, magnetKraft, p),
		ProductInfo(u'', 3, magnetKraft, p),
		ProductInfo(u'', 4, magnetKraft, p),
		ProductInfo(u'', 5, magnetKraft, p),
		ProductInfo(u'', 6, magnetKraft, p),
		ProductInfo(u'', 7, magnetKraft, p),
		ProductInfo(u'', 8, magnetKraft, p),
		ProductInfo(u'600', 9, magnetKraft, p),
        ProductInfo(u'1200', 10, magnetKraft, p),	       
    ])

    p = Product('Formsidor olika profiler m.m.', u'Formsidor med exempelvis H-profil, kan levereras både med och utan integrerad magnet. Även specialavstängare för plattbjälklag finns. <br/>Hittar ni inte det ni vill ha på bilden, ring oss det finns många fler modeller och vi skräddarsyr gärna enligt kundönskemål', '81_formsidor_olika_profiler.png', pg, 'Formsidor_profiler', False)
    db.session.add(p)
    ## Fjäril ##
    pg = ProductGroup(u'Fjäril för batteriformar', '90_fjaril.png', pc, u'Fjaril_batteriformar')
    db.session.add(pg)

    p = Product(u'Fjäril för batteriformar', u'Produktionen av prefabricerade element sker idag ibland med batteriform. Med hjälp av detta system, som är en ny lösning på hur man hanterar formsättningen i en batteriform, sparas både tid och arbetsbelastning.<br/><br/> Fördelar:<br/>Produktionen är snabb och enkel att använda. Ytan är slät på båda sidor så att ingen ytterligare efterbehandling krävs.<br/> Mängd element producerade i en batteriform ökar rejält med litet krav på extra utrymme.<br/>Ger flexibilitet när det gäller lämplig plats', '90_fjaril.png', pg, 'Fjaril_batteriformar', False)
    db.session.add(p)

    ###### -- ELEMENTINFÄSTNING  -- ######
    pc = ProductCategory(u'Elementinfästning')
    db.session.add(pc)
    
    pg = ProductGroup(u'Igloo', '88_igloo.png', pc, u'Igloo')
    db.session.add(pg)


    p = Product(u'Skruvkoppling IGLOO', u'För vidare teknisk information, mått, kraftupptagning osv: kontakta oss eller se den tekniska specifikationen längst ner (.PDF)', '88_igloo.png', pg, 'Skruvkoppling_igloo', False)
    db.session.add(p)

    db.session.add_all([
        ProductInfo('SP12FZV', 1, artnr, p),
        ProductInfo('SP12FZVSET', 2, artnr, p),
        ProductInfo('SP12RF', 3, artnr, p),
        ProductInfo('SP12RFSET', 4, artnr, p),
        ProductInfo('SP16FZV', 5, artnr, p),
        ProductInfo('SP16FZVSET', 6, artnr, p),
        ProductInfo('SP16RF', 7, artnr, p),
        ProductInfo('SP16RFSET', 8, artnr, p),
        ProductInfo('SP20FZV', 9, artnr, p),
        ProductInfo('SP20FZVSET', 10, artnr, p),
        ProductInfo('SP20RF', 11, artnr, p),
        ProductInfo('SP20RFSET', 12, artnr, p),
        ProductInfo(u'Skruvkoppling Igloo M12 FZV', 1, benamning, p),
        ProductInfo(u'Skruvkoppling Igloo M12 FZV', 2, benamning, p),
        ProductInfo(u'Skruvkoppling Igloo M12 Rostfritt', 3, benamning, p),
        ProductInfo(u'Skruvkoppling Igloo M12 Rostfritt', 4, benamning, p),
        ProductInfo(u'Skruvkoppling Igloo M16 FZV', 5, benamning, p),
        ProductInfo(u'Skruvkoppling Igloo M16 FZV', 6, benamning, p),
        ProductInfo(u'Skruvkoppling Igloo M16 Rostfritt', 7, benamning, p),
        ProductInfo(u'Skruvkoppling Igloo M16 Rostfritt', 8, benamning, p),
        ProductInfo(u'Skruvkoppling Igloo M20 FZV', 9, benamning, p),
        ProductInfo(u'Skruvkoppling Igloo M20 FZV', 10, benamning, p),
        ProductInfo(u'Skruvkoppling Igloo M20 Rostfritt', 11, benamning, p),
        ProductInfo(u'Skruvkoppling Igloo M20 Rostfritt', 12, benamning, p),
        ProductInfo(u'', 1, utokadBeskr, p),
        ProductInfo(u'Komplett med bultar och brickor 10 st per frp', 2, utokadBeskr, p),
        ProductInfo(u'', 3, utokadBeskr, p),
        ProductInfo(u'Komplett med bultar och brickor 10 st per frp', 4, utokadBeskr, p),
        ProductInfo(u'', 5, utokadBeskr, p),
        ProductInfo(u'Komplett med bultar och brickor 10 st per frp', 6, utokadBeskr, p),
        ProductInfo(u'', 7, utokadBeskr, p),
        ProductInfo(u'Komplett med bultar och brickor 10 st per frp', 8, utokadBeskr, p),
        ProductInfo(u'', 9, utokadBeskr, p),
        ProductInfo(u'Komplett med bultar och brickor 10 st per frp', 10, utokadBeskr, p),
        ProductInfo(u'', 11, utokadBeskr, p),
        ProductInfo(u'Komplett med bultar och brickor 10 st per frp', 12, utokadBeskr, p),
       ])

    p = Product(u'Ursparing för IGLOO', u'Fler modeller finns, kontakta oss för mer information.', '89_igloo_2.png', pg, 'Ursparing_igloo', False)
    db.session.add(p)

    db.session.add_all([
        ProductInfo('SPU112', 1, artnr, p),
        ProductInfo('SPUH16', 2, artnr, p),
        ProductInfo('SPU16', 3, artnr, p),
        ProductInfo('SPUH20', 4, artnr, p),
        ProductInfo('SPU20', 5, artnr, p),
        ProductInfo('SPUH12UM', 6, artnr, p),
        ProductInfo('SPU12UM', 7, artnr, p),
        ProductInfo('SPUH16UM', 8, artnr, p),
        ProductInfo('SPU16UM', 9, artnr, p),
        ProductInfo('SPUH20UM', 10, artnr, p),
        ProductInfo('SPU20UM', 11, artnr, p),
        ProductInfo(u'Skruvkoppling Igloo Ursparing M12', 1, benamning, p),
        ProductInfo(u'Skruvkoppling Igloo Ursparing för hörn M16', 2, benamning, p),
        ProductInfo(u'Skruvkoppling Igloo Ursparing M16', 3, benamning, p),
        ProductInfo(u'Skruvkoppling Igloo Ursparing för hörn M20', 4, benamning, p),
        ProductInfo(u'Skruvkoppling Igloo ursparing M20', 5, benamning, p),
        ProductInfo(u'Skruvkoppling Igloo Ursparing för hörn M12', 6, benamning, p),
        ProductInfo(u'Skruvkoppling Igloo Ursparing M12', 7, benamning, p),
        ProductInfo(u'Skruvkoppling Igloo Ursparing för hörn M16', 8, benamning, p),
        ProductInfo(u'Skruvkoppling Igloo Ursparing M16', 9, benamning, p),
        ProductInfo(u'Skruvkoppling Igloo Ursparing för hörn M20', 10, benamning, p),
        ProductInfo(u'Skruvkoppling Igloo Ursparing M20', 11, benamning, p),
        ProductInfo(u'Med magneter', 1, utokadBeskr, p),
        ProductInfo(u'Med magneter', 2, utokadBeskr, p),
        ProductInfo(u'Med magneter', 3, utokadBeskr, p),
        ProductInfo(u'Med magneter', 4, utokadBeskr, p),
        ProductInfo(u'Med magneter', 5, utokadBeskr, p),
        ProductInfo(u'Utan Magneter', 6, utokadBeskr, p),
        ProductInfo(u'Utan Magneter', 7, utokadBeskr, p),
        ProductInfo(u'Utan Magneter', 8, utokadBeskr, p),
        ProductInfo(u'Utan Magneter', 9, utokadBeskr, p),
        ProductInfo(u'Utan Magneter', 10, utokadBeskr, p),
        ProductInfo(u'Utan Magneter', 11, utokadBeskr, p),
       ])
    

    ## Rubberelast ##
    pg = ProductGroup(u'Rubberelast', '85_rubberelast.png', pc, u'Rubberelast')
    db.session.add(pg)


    p = Product(u'Rubberelast', u'RubberElast® är ett material som enkelt och snabbt tillämpas överallt, nästan helt oberoende på temperatur. Materialet blir vattentät omedelbart efter applicering, eftersom det är stadigt limmat mot de prefabricerade ytorna genom tryck. Materialet förblir tixotrop. Det är motståndskraftigt mot aggressiva miljöer. Detta gör att RubberElast® passar i miljöer där avloppsvatten förekommer. Testcertifikat utfärdas av Material Testing Institut i Braunschweig, Tyskland.<br/>Enkelt att applicera, extremt hög motståndskraft mot vatten och gas. <br/>Mycket god vidhäftnings kapacitet.  Snabbarbetat, inga verktyg behövs.<br/>Blir vattentät omedelbart efter applicering. Fungerar även vid låga temperaturer.<br/>Resistent mot syror, alkalier, salter och betongslam.', '85_rubberelast.png', pg, 'Rubberelast', False)
    db.session.add(p)

    db.session.add_all([
        ProductInfo('RE1717', 1, artnr, p),
        ProductInfo('RE2519', 2, artnr, p),
        ProductInfo('RE3225', 3, artnr, p),
        ProductInfo('RE3832', 4, artnr, p),
        ProductInfo('RE4842', 5, artnr, p),
        ProductInfo(u'Rubber Elast 17x17', 1, benamning, p),
        ProductInfo(u'Rubber Elast 25x19', 2, benamning, p),
        ProductInfo(u'Rubber Elast 32x25', 3, benamning, p),
        ProductInfo(u'Rubber Elast 38x32', 4, benamning, p),
        ProductInfo(u'Rubber Elast 48x42', 5, benamning, p),
        ProductInfo(u'4000', 1, langdMm, p),
        ProductInfo(u'4400', 2, langdMm, p),
        ProductInfo(u'4400', 3, langdMm, p),
        ProductInfo(u'3200', 4, langdMm, p),
        ProductInfo(u'2250', 5, langdMm, p),
        ProductInfo(u'9', 1, antalforpSt, p),
        ProductInfo(u'6', 2, antalforpSt, p),
        ProductInfo(u'4', 3, antalforpSt, p),
        ProductInfo(u'4', 4, antalforpSt, p),
        ProductInfo(u'4', 5, antalforpSt, p),
        ProductInfo(u'0.41', 1, viktPerMeter, p),
        ProductInfo(u'0.72', 2, viktPerMeter, p),
        ProductInfo(u'1.11', 3, viktPerMeter, p),
        ProductInfo(u'1.66', 4, viktPerMeter, p),
        ProductInfo(u'2.87', 5, viktPerMeter, p),
       ])

    
    p = Product(u'SPA-Byglar', u'Mer information kommer.', u'91_spa_byglar.png', pg, 'spa_byglar', False)
    db.session.add(p)


    db.session.commit()


from analize.models import Media, Party, Member

from django.core.management.base import BaseCommand

mediums = [
    'aljazeera',
    'aloonline',
    'atvbl',
    'banjaluka',
    'bhindex',
    'bhrt',
    'biscani',
    'bljesak',
    'blportal',
    'bosnainfo',
    'buka',
    'cazin',
    'depo',
    'dnevnik',
    'face',
    'faktor',
    'federalna',
    'fokus',
    'glassrpske',
    'haber',
    'hayat',
    'hercegovinainfo',
    'jabuka',
    'klix',
    'logicno',
    'mojabanjaluka',
    'n1info',
    'nap',
    'nezavisne',
    'oslobodjenje',
    'poskok',
    'pressmediabih',
    'radiosarajevo',
    'raport',
    'rediokameleon',
    'rtrs',
    'rtvbn',
    'saff',
    'slobodnabosna',
    'source',
    'srpskainfo',
    'stav',
    'tacno',
    'tip',
    'tuzlanski',
    'vecernji',
    'vijesti',
    'zenit',
    'zurnal',
    'avaz'
]

parties = [
    'Narod i pravda',
    'NiP',
    'Socijaldemokratska partija Bosne i Hercegovine',
    'SDP BiH',
    'Stranka demokratske akcije',
    'SDA',
    'Pokret demokratske akcije BiH',
    'PDA BiH',
    'PDA',
    'Partija demokratskog progresa',
    'PDP',
    'Ujedinjena Srpska',
    'Narodni Evropski Savez Bosne i Hercegovine',
    'NES BiH',
    'NES',
    'Hrvatska stranka prava dr. Ante Starčević Bosne i Hercegovine',
    'HSP dr. Ante Starčević BiH',
    'Narodni demokratski pokret',
    'NDP',
    'Građanski savez',
    'GS',
    'Srpska demokratska stranka',
    'SDS',
    'Socijalistička partija Republike Srpske',
    'SP RS',
    'SPRS',
    'Nezavisni blok',
    'NB',
    'Savez za bolju budućnoost',
    'SBB',
    'Hrvatska demokratska zajednica Bosne i Hercegovine',
    'HDZ BiH',
    'Hrvatska demokratska zajednica 1990',
    'HDZ 1990',
    'Savez Nezavisnih socijaldemokrata',
    'SNSD',
    'Demokratska fronta',
    'DF',
    'Naša stranka',
    'NS',
    'Laburistička stranka',
    'Demokratski narodni savez',
    'DNS',
]

members = [
    'Elmedin Konaković',
    'Denis Zvizdić',
    'Danijela Kristić',
    'Aljoša Čampara',
    'Kemal Ademović',
    'Nihad Omerović',
    'Elvedin Okerić',
    'Arijana Memić',
    'Elvis Vreto',
    'Edita Velić',
    'Naida Hota-Muminović',
    'Omer Osmanović',
    'Enver Hadžiahmetović',
    'Adnan Delić',
    'Haris Kaniža',
    'Amra Junuzović-Kljajić',
    'Samir Avdić',
    'Amel Mekić',
    'Amra Babić',
    'Nermin Muzur',
    'Ahmet Sejdić',
    'Amar Dovadžija',
    'Senad Mašetić',
    'Nezim Alagić',
    'Omer Hujdur',
    'Rusmir Pobrić',
    'Aida Terzić',
    'Izen Hajdarević',
    'Azhar Sejarić',
    'Dejan Kovačević',
    'Nermin Nikšić',
    'Elvir Karajbić',
    'Saša Magazinović',
    'Denis Bećirović',
    'Aner Žuljević',
    'Zukan Helez',
    'Igor Stojanović',
    'Damir Mašić',
    'Albin Muslić',
    'Irfan Čengić',
    'Adnan Šteta',
    'Razim Halkić',
    'Ivan Bobam',
    'Lana Prlić',
    'Benjamina Karić',
    'Vojin Mijatović',
    'Belma Kapo',
    'Jasmin Imamović',
    'Dževad Hadžić',
    'Jasna Duraković',
    'Samir Avdić',
    'Jelena Pekić',
    'Enid Tahirović',
    'Davor Čičić',
    'Haris Vranić',
    'Kenan Magoda',
    'Dervo Sejdić',
    'Kadrija Hodžić',
    'Lidija Korać',
    'Edina Papo',
    'Bakir Izetbegović',
    'Edin Ramić',
    'Šemsudin Dedić',
    'Melika Mahmutbegović',
    'Šerif Špago',
    'Mirsad Zaimović',
    'Alma Čolo',
    'Haris Zahiragić',
    'Aida Obuća',
    'Denijal Tulumović',
    'Ramiz Salkić',
    'Fadil Novalić',
    'Nermin Mandra',
    'Miralem Galijašević',
    'Eldar Čomor',
    'Tahir Lendo',
    'Irfan Halilagić',
    'Mahir Dević',
    'Irma Memidžan',
    'Jasmin Musić',
    'Begija Smajić',
    'Šefik Džaferović',
    'Safet Softić',
    'Adil Osmanović',
    'Halid Genjac',
    'Kenela Zuko',
    'Sebija Izetbegović',
    'Faruk Kapidžić',
    'Nijaz Hušić',
    'Azmir Husić',
    'Elzina Pirić',
    'Senad Alić',
    'Mujo Puzić',
    'Samir Imamović',
    'Nesib Serhatlić',
    'Azra Pašalić',
    'Jakub Suljkanović',
    'Mirsad Kukić',
    'Husein Topčagić',
    'Branislav Borenović',
    'Igor Crnadak',
    'Jelena Trivić',
    'Mira Pekić',
    'Slaviša Marković',
    'Draško Stanivuković',
    'Siniša Golić',
    'Radenko Čupić',
    'Perica Bundalo',
    'Ljubiša Krunić',
    'Tanja Vukomanović',
    'Igor Tošić',
    'Mirna Savić Banjac',
    'Saša Borjan',
    'Sanja Dimitrić',
    'Nenad Vuković',
    'Olivera Nedić',
    'Mladen Ivanić',
    'Nenad Stevandić',
    'Natalija Trivić',
    'Marinko Dragišić',
    'Slavo Dunjić',
    'Dušan Stojičić',
    'Neven Stanić',
    'Mijat Šarović',
    'Mile Aljetić',
    'Jovana Kodić',
    'Slava Brezo',
    'Milan Kovač',
    'Kostadin Vasić',
    'Milan Trninić',
    'Nenad Mejakić',
    'Sreto Đurković',
    'Milan Petković',
    'Milan Novitović',
    'Nenad Prodanović',
    'Miodrag Tešendić',
    'Mustafa Ružnić',
    'Jasmin Emrić',
    'Zlatko Kravić',
    'Ramo Isak',
    'Ilda Alibegović',
    'Nermin Ogrešević',
    'Ibrahim Hadžibajrić',
    'Mesud Hero',
    'Muhamed Ramović',
    'Mirza Batalović',
    'Nermin Vrtić',
    'Haris Selmanović',
    'Osman Puškar',
    'Jusuf Mehić',
    'Arnel Isak',
    'Milijan Nakić',
    'Marija Lovrić',
    'Dragan Čavić',
    'Muhamed Fazlagić',
    'Reuf Bajrović',
    'Mirko Šarović',
    'Miladin Stanić',
    'Nedeljko Glamočak',
    'Branko Butulija',
    'Darko Babalj',
    'Stevo Joksimović',
    'Slađana Nikolić',
    'Nebojša Vukanović',
    'Mladen Bosić',
    'Aleksandra Pandurević',
    'Vukota Govedarica',
    'Petar Đokić',
    'Živko Marjanac',
    'Srđan Todorović',
    'Senad Šepić',
    'Aida Baručija',
    'Fahrudin Radončić',
    'Lejla Bakrač',
    'Vesko Drljača',
    'Nermin Džindić',
    'Edita Đapo',
    'Sanela Prašović - Gadžo',
    'Adin Huremović',
    'Mirsad Kacila',
    'Šemsudin Kavazović',
    'Faika Mujanović-Glamočanin',
    'Hasan Muratović',
    'Munib Jusufović',
    'Dragan Čović',
    'Borjana Krišto',
    'Marinko Čavara',
    'Mladen Bošković',
    'Nikola Lovrinović',
    'Lidija Bradara',
    'Bariša Čolak',
    'Marina Pendeš',
    'Mijo Krešić',
    'Darijana Katić - Filipović',
    'Predrag Kožul',
    'Josip Grubeša',
    'Ankica Gudeljević',
    'Josip Brkić',
    'Martin Raguž',
    'Ilija Cvitanović',
    'Božo Perić',
    'Nediljko Rimac',
    'Milorad Dodik',
    'Željka Cvijanović',
    'Nebojša Radmanović',
    'Radovan Višković',
    'Radovan Kovačević',
    'Nikola Špirić',
    'Sanja Vulić',
    'Dušanka Majkić',
    'Luka Petrović',
    'Denis Šulić',
    'Zoran Tegeltija',
    'Staša Košarac',
    'Miloš Lučić',
    'Vojin Mitrović',
    'Lazar Prodanović',
    'Igor Žunić',
    'Srđan Mazalica',
    'Snježana Novaković Bursać',
    'Dragan Bogdanić',
    'Ljubica Miljanović',
    'Igor Radojičić',
    'Željko Komšić',
    'Milan Dunović',
    'Dženan Đonlagić',
    'Zlatan Begić',
    'Enver Bijedić',
    'Vlatko Glavaš',
    'Dževad Adžem',
    'Mara Đukić',
    'Samer Rešidat',
    'Predrag Kojović',
    'Sabina Čudić',
    'Damir Arnaut',
    'Mirsad Čamdžić',
    'Sanela Klarić',
    'Nasiha Pozder',
    'Miomirka Mila Melank',
    'Amela Kuskunović',
    'Mirjana Marinković - Lepić',
    'Edin Forto',
    'Srđan Mandić',
    'Damir Nikšić',
    'Alen Girt',
    'Nihad UK',
    'Elvira Abdić Jelenović',
    'Edina Abdić Pleho',
    'Amir Đogić',
    'Elma Đogić',
    'Nenad Nešić',
    'Neđo Trninić',
    'Radislav Jovičić',
    'Dane Malešević',
    'Dragutin Rodić',
    'Mirko Sovilj',
    'Aleksandar Glavaš',
    'Duško Ivić'
]

class Command(BaseCommand):
    help = 'Setup data'
    def handle(self, *args, **options):
        for media in mediums:
            Media(name=media).save()

        for party in parties:
            Party(name=party).save()

        for member in members:
            Member(name=member).save()


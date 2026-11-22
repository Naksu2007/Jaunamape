IT Helpdesk Tickets analīze un prognozēšana
Projekta apraksts
Šajā projektā tiek analizēta IT palīdzības dienesta (Help Desk) pieteikumu datu kopa.

Projekta gaitā:

Tiek nolasīti neapstrādātie dati no CSV faila.
Tiek iztīrītas trūkstošās vērtības un noņemti dublikāti.
Tiek izveidots attīrītais datu fails tirs.csv.
Dati tiek sadalīti treniņa un testa kopā.
Tiek apmācīts mašīnmācīšanās modelis.
Tiek aprēķināta modeļa precizitāte un salīdzinājums ar bāzes līniju.

Repozitorija struktūra
dati/ │ AVOTS.txt │ tirisana.py modelis.py tirs.csv rezultati.md README.md
Nepieciešamās Python bibliotēkas - pandas - scikit-learn 
Instalēšana: ```bash pip install pandas scikit-learn
Projekta palaišana
1. Datu tīrīšana

Palaid:

Shell
python tirisana.py

Rezultātā tiks izveidots fails:

Plain Text
tirs.csv

2. Modeļa apmācība

Palaid:

Shell
python modelis.py

Rezultātā terminālī tiks parādīta:

modeļa precizitāte;
bāzes līnijas precizitāte;
secinājums par to, vai modelis pārspēj bāzes līniju.
Rezultāti

Iegūtie rezultāti aprakstīti failā rezultati.md.


Rezultāti

Modeļa novērtējums

Modeļa precizitāte: 68,8%

Bāzes līnija: 45,8%

Modelis pārspēja bāzes līniju par 23,0 procentpunktiem, tādēļ tas prognozē pieteikumu kategorijas precīzāk nekā vienkārša biežākās atbildes izvēle.

Secinājums

Modelis ir noderīgs, jo tas sasniedza augstāku precizitāti nekā bāzes līnija. To var izmantot kā atbalsta rīku IT palīdzības dienesta pieteikumu prioritizēšanai un novirzīšanai atbildīgajiem speciālistiem.
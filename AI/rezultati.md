Kas ir šie dati un no kurienes tie nāk?

Tika izmantota IT palīdzības dienesta (help desk) pieteikumu datu kopa no GitHub repozitorija helpdesk_tickets.csv. Katra rinda apraksta vienu atbalsta pieteikumu, piemēram, ierīces tipu, kļūdas kodu, gaidīšanas laiku, problēmas nopietnību un citus parametrus. Prognozējamais lauks ir response_tier, kas nosaka, kāda līmeņa reakcija nepieciešama konkrētajam pieteikumam.


Kas ar datiem bija nepareizi un ko es izdarīju?

Šajā datu kopā bija trūkstošas vērtības vairākās kolonnās:

error_code
reported_severity
wait_time_minutes

Repozitorija aprakstā ir norādīts, ka šīs nepilnības ir atstātas apzināti.

Tīrīšanas laikā:

1.Trūkstošie error_code tika aizstāti ar "UNKNOWN".
2.Trūkstošās reported_severity vērtības tika aizstātas ar biežāk sastopamo kategoriju.
3.Trūkstošās wait_time_minutes vērtības tika aizstātas ar mediānu.
4.Tika izņemti iespējamie dublikāti.
5.Iztīrītie dati tika saglabāti failā tirs.csv, nemainot oriģinālo failu.


Ko modelis prognozē un cik labi?

Modelis prognozē lauku response_tier, tas ir, kāda reakcija nepieciešama konkrētajam pieteikumam:

log_only
assign_technician
escalate_now

Piemērs:

Rādītājs	Vērtība
Modeļa precizitāte	68.8%
Bāzes līnija	45.8%

Modeļa precizitāte bija 68,8%, bet bāzes līnijas precizitāte bija 45,8%. Modelis pārspēja bāzes līniju par 23,0 procentpunktiem, tādēļ tas spēj prognozēt pieteikumu kategorijas labāk nekā vienkārša biežākās atbildes izvēlēšanās. Tas liecina, ka modelis ir apguvis sakarības datos un var būt noderīgs lēmumu pieņemšanas atbalstam.


Ja modelis darbotos reālā sistēmā, ko darītu ar prognozi?

Viens konkrēts pielietojums:

Ja modelis prognozē escalate_now, sistēma automātiski izveidotu augstas prioritātes uzdevumu tehniķim un nosūtītu paziņojumu atbildīgajai IT komandai.

Piemēram:

pieteikums tiek saņemts;
modelis izvērtē datus;
tiek prognozēts escalate_now;
sistēma automātiski piešķir biļeti otrā līmeņa atbalsta speciālistam;
tehniķis sāk problēmas izmeklēšanu.
Kas notiek, ja modelis kļūdās?
Nepamatota trauksme (False Positive)

Modelis prognozē nopietnu problēmu, bet patiesībā tās nav.

Sekas:

tehniķi tērē laiku nevajadzīgiem darbiem;
tiek izmantoti resursi, kas būtu nepieciešami citur;
pieaug darba izmaksas.

Piemērs:

Parasts printera incidents kļūdaini tiek nosūtīts augstākā līmeņa speciālistam.

Nepamanīta problēma (False Negative)

Modelis neatzīst nopietnu problēmu, lai gan tā patiešām pastāv.

Sekas:

kavējas problēmas novēršana;
lietotāji ilgāk nevar izmantot sistēmu;
iespējami biznesa zaudējumi.

Piemērs:

Tīkla iekārtas atteice tiek klasificēta kā mazsvarīga problēma un netiek savlaicīgi apstrādāta.

Kurš kļūdas veids ir sliktāks?

Šajā situācijā sliktāks ir nepamanītas problēmas gadījums (False Negative).

Iemesls:

nepamatota trauksme rada papildu darbu;
nepamanīta kritiska problēma var izraisīt sistēmas dīkstāvi, klientu neapmierinātību un finanšu zaudējumus.

Tāpēc šādā sistēmā bieži izvēlas modeli, kas labāk pamana kritiskos gadījumus pat tad, ja reizēm rada liekas trauksmes.

Ko ar šo modeli NEDRĪKST darīt?

Šo modeli nedrīkst izmantot kā vienīgo pamatu darbinieku darba kvalitātes novērtēšanai.

Iemesls:

Modelis ir apmācīts prognozēt pieteikumu apstrādes līmeni (response_tier), nevis vērtēt tehniķu kompetenci vai darba efektivitāti. Šādam mērķim trūkst nepieciešamo datu, tāpēc secinājumi varētu būt neobjektīvi un nepareizi.

Noslēgums
Izdevās veiksmīgi iztīrīt datus, apmācīt modeli un iegūt precizitāti 68,8%, kas pārspēj bāzes līniju 45,8%.

Neizdevās sasniegt ļoti augstu precizitāti, jo datu kopā bija trūkstošas vērtības un salīdzinoši neliels ierakstu skaits.

Nākamreiz izmēģinātu vairākus dažādus mašīnmācīšanās modeļus un pielāgotu to parametrus, lai pārbaudītu, vai iespējams iegūt vēl labākus rezultātus.
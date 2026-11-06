# Vloga za soglasje

Orodje za pripravo in **spletno oddajo** Enotne vloge za izdajo soglasja za priključitev pri Elektro Maribor. Pokriva sončno elektrarno kot napravo za individualno samooskrbo in/ali hranilnik električne energije. Vlogo oddamo mi, kot pooblaščenec stranke.

Vloga se ne izpolnjuje v PDF-ju. Orodje pripravi podatke v enakem vrstnem redu kot spletni obrazec, z gumbom **Kopiraj** pri vsakem polju, poleg tega pa še pooblastilo in tehnično dokumentacijo za nalaganje.

**Najlažje:** odprite **`Vloga-za-soglasje.html`** v brskalniku (dvoklik). To je ena datoteka z vsem. Ne potrebuje strežnika ali namestitve.

`index.html` je izvorna različica in deluje samo, če je ob njej mapa `lib/`. Po spremembi `index.html` ponovno zgradite eno datoteko:

```
python3 tools/zgradi_eno_datoteko.py
```

## Postopek

1. **Nova vloga**: obkljukajte elektrarno in/ali hranilnik. Vpišite uporabnika (investitorja), merilno mesto (številka `4-…`, GSRN, priključna moč odjema), katastrsko občino in parcelo ter opremo (FN moduli, razsmerniki, hranilnik).
2. **Pooblastilo za podpis**: vsebuje tudi izjavo, da je stranka seznanjena s klavzulami o varstvu osebnih podatkov. Pri več solastnikih vsebuje še mesta za njihove podpise. Pošljite ga z mailom »Stranki – pooblastilo za podpis«. Mail sam našteje podatke, ki še manjkajo (davčna, številka MM, parcela …).
3. Za izdelavo enopolne sheme lahko podatke kadar koli izvozite, tudi če vloga še ni izpolnjena do konca: pri »Enopolna shema« izberite **Kopiraj podatke**, **Prenesi .txt** ali **Prenesi .json**. Izvoz vsebuje lokacijo, merilno mesto, priključno moč, FN module, razsmernike, hranilnik, shemo in način obratovanja ter seznam podatkov, ki še manjkajo. Ko je shema narejena, dodajte **enopolno shemo** in **tehnične liste**. Gumb **Tehnična dokumentacija** jih združi z opisom naprave v en PDF. Ta se naloži pri elektrarni in pri hranilniku. Spletni obrazec sprejme datoteke **do 4 MB**. Orodje opozori, če je datoteka večja.
4. Ko stranka vrne podpisano pooblastilo, ga dodajte z gumbom **Podpisano**.
5. **Oddaja na spletu →**: odprite spletni obrazec in ga postavite ob orodje. Pri vsakem polju kliknite **Kopiraj** in prilepite. Pri izbirah orodje pove, katero možnost kliknete. Koraki so enaki kot na obrazcu: Pričetek → Uporabnik → Plačnik → Elektrarna → Hranilnik → Opombe in potrditev → Tiskaj → Zaključi.
6. **Po oddaji**: vpišite številko vloge iz potrdila (pride na kontaktni e-naslov). Ko pride soglasje, vpišite še njegovo številko in priključno moč. Nato **Izvozi v Vloga-priklop** in datoteko uvozite v orodju Vloga-priklop (Vloge → Uvozi).

## Kontrole

- davčna številka (kontrolna števka) in GSRN merilnega mesta (GS1 kontrolna števka);
- oblika številke merilnega mesta (`4-…`);
- moč razsmernikov in nova priključna moč glede na priključno moč odjema;
- manjkajoča obvezna polja spletnega obrazca;
- priloge, večje od 4 MB.

## Pred prvo uporabo

1. **Nastavitve → Pooblaščenec**: dopolnite kontaktno osebo, telefon in e-pošto. Privzeto so v vlogi kontaktni podatki naši, zato potrdilo in številka vloge prideta k nam.
2. **Nastavitve → Katalog opreme**: v Vloga-priklop naredite *Izvozi varnostno kopijo*, tukaj pa *Uvozi katalog iz Vloga-priklop*. Pri hranilnikih preverite tehnologijo (LFP …) in faze.
3. **Nastavitve → Napredno → Pravila**:
   - izbira v polju »Dodatni podatki potrebni za izdajo soglasja«, če je vedno ista;
   - izbira »Vrsta proizvodne naprave«;
   - ocena letne proizvodnje (kWh/kWp) in delež za lastne potrebe;
   - decimalno ločilo pri kopiranju.

## Ko se spletni obrazec spremeni

Struktura obrazca je zapisana v `SPLETNI_OBRAZEC.md`, pomočnik pa v funkciji `koraki()` v `index.html`. Besedila izbir (sheme, način obratovanja, tehnologije …) so v `OPC`. Prepisana so z uradne Enotne vloge EM 10/26. Če je besedilo na spletu drugačno, ga popravite tam in ponovno zgradite eno datoteko.

## Podatki in GDPR

Vloge se shranjujejo samo v brskalniku na računalniku, kjer je orodje odprto (`localStorage`). Nič se ne pošilja na strežnik.

- Redno naredite **Izvozi varnostno kopijo** (JSON).
- Priložene datoteke (sheme, tehnični listi, podpisano pooblastilo) se ne shranjujejo. Ostanejo le do zaprtja strani.
- Ko je soglasje izdano in preneseno v Vloga-priklop, vlogo izbrišite.

## Licence

- [pdf-lib](https://github.com/Hopding/pdf-lib) in [@pdf-lib/fontkit](https://github.com/Hopding/fontkit) – MIT
- Pisava Liberation Sans – SIL Open Font License 1.1 (`lib/fonts/LICENSE-OFL.txt`)

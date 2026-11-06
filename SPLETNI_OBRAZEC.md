# Spletna enotna vloga Elektro Maribor – struktura obrazca

Zapis polj spletnega obrazca (pregled 3. 11. 2026), po katerem je narejen pomočnik za oddajo (`koraki()` v `index.html`).
Obrazec: https://mf-evloga.elektro-maribor.si/app/ (povezava je na strani Elektro Maribor → Priključevanje na omrežje).
Če se obrazec spremeni, posodobite ta zapis in `koraki()`.
Izbire v spustnih seznamih so prepisane z uradne Enotne vloge EM 10/26 (PDF), na spletu so lahko zapisane nekoliko drugače.

Koraki (ob izbiri 4 + 6, pooblaščenec):
1. Pričetek
2. Podatki o uporabniku
3. Podatki o plačniku stroškov priključevanja
4. Podatki o elektrarni oz. proizvodni napravi
5. Podatki o hranilniku električne energije
6. Opombe in potrditev
7. Tiskaj
8. Zaključi

## 1. Pričetek
- Osnovni podatki → Oddaje enotne vloge za * (POTRDITVENA POLJA, več hkrati):
  1 projektni pogoji (A) / 2 soglasje odjem + GD (B) / 3 mnenje k projektu, soglasje h gradnji (C) /
  4 proizvodna naprava / individualna / skupnostna samooskrba (D) / 5 polnilnica (E) / 6 hranilnik (F)
- Dodatni podatki potrebni za izdajo soglasja * (spustni seznam) – možnosti ŠE NEZNANE
- Uporabnik ali pooblaščenec → Vaša vloga *: Sem uporabnik / Sem pooblaščenec

## 2. Podatki o uporabniku
- Vrsta uporabnika *: Pravni subjekt / Fizična oseba
- Ali ima nepremičnina več solastnikov *: Ne / Da
- Priimek *, Ime *   (fizična oseba)
- Kraj (neobvezno), Naslov (ulica/naselje) *, Hišna številka *
- Pošta * (iskalnik s seznamom)
- Davčna številka *
### Podatki o pooblaščencu
- Vrsta pooblaščenca: Pravni subjekt / Fizična oseba
- Ime *, Priimek * (fizična)
- Kraj, Naslov (ulica/naselje) *, Hišna številka *, Pošta * (iskalnik), Davčna številka *
- Pravni subjekt pooblaščenec: polja ŠE NEZNANA
### Kontaktni podatki
- stikalo: Podatki o kontaktni osebi so enaki podatkom o uporabniku
- Kontaktna oseba *, Telefon *, E-mail * (na ta e-mail pride kopija izpolnjene vloge)
### Priloge
- Pooblastilo investitorja * (nalaganje; image/*, doc, docx, odt, xls, xlsx, ods, pdf; največ 4 MB)
- Opomba: prazen korak 2 ima 17 obveznih polj (rdeča značka 17)

## 3. Podatki o plačniku stroškov priključevanja
- Plačnik stroškov priključevanja *: Plačnik stroškov bo uporabnik / Plačnik stroškov bo tretja oseba
  (tretja oseba: polja ŠE NEZNANA – po PDF: naziv, naslov, pošta, davčna, davčni zavezanec, proračunski porabnik, podpisnik pogodb)

## 4. Podatki o elektrarni oz. proizvodni napravi
- stikalo: Sprememba na obstoječem merilnem mestu (vklopljeno →)
  - Številka merilnega mesta * (predizpolnjeno "4-", format EM 4-xxxxxx)
  - GSRN MM (neobvezno, "izpolniti če obstaja")
- Naziv elektrarne oz. proizvodne naprave *
- Številka predhodno izdane informacije o možnosti priključitve ali soglasja za priključitev proizvodne naprave (neobvezno)
- Vrsta proizvodne naprave * (spustni seznam – možnosti ŠE NEZNANE)
- Proizvodni vir energije * (verjetno odvisen od vrste – ŠE NEZNANO)
- gumb: Podatki o lokaciji so enaki uporabnikovemu naslovu (Kopiraj/Prenesi)
- Kraj, Naslov (ulica/naselje) *, Hišna številka *, Pošta * (iskalnik)
- Katastrska občina * (iskalnik), Parcelna številka * (več ločiti z vejico)
- stikalo: Objekt se nahaja v več kot eni katastrski občini
- Predvideno leto priključitve * (spustni seznam)
### Priključna moč proizvodne naprave
- Obstoječa * (kW), Nova * (kW), Celotna instalirana moč proizvodne naprave * (kVA)
### Tehnični podatki
- Način vključevanja v DS tipska shema * (izbira – možnosti ŠE NEZNANE; PDF: PS.1B/PS.1C/PS.2/PS.3A/PS.3B)
- Način obratovanja * – 4 potrditvena polja: Paralelno z DS / Otočno / P – porabniški / M – mešani (obkljuka se poljubne; običajno samo M)
- Na voljo za sistemske storitve (spustni seznam)
- Podatki o razsmernikih / generatorjih * – tabela z gumbom Dodaj:
  Generator/Razsmernik | Število enakih enot | Moč enote | Nazivna napetost | Vrsta generatorja/razsmernika | Število faz
  (obrazec za Dodaj ŠE NEZNAN)
- Predvidena letna proizvodnja za lastne potrebe (kWh), … za oddajo v omrežje EES (kWh), Predvidena letna proizvodnja (izračuna se – ikona kalkulatorja)
### Priloge (image/*, pdf, dxf, dwg; največ 4 MB)
- Gradbeno dovoljenje ali tehnična dokumentacija za izvedbo elektrarne * (GD za nove, ki ga potrebujejo; sicer tehnična dokumentacija)
- Kopija katastrskega načrta in zazidalna situacija
- Ostala dokazila (projekt, dokazilo o lastništvu, najemna pogodba, dokazilo o legalnosti objekta …)

## 5. Podatki o hranilniku električne energije
### Osnovni podatki
- stikalo: Sprememba na obstoječem merilnem mestu (izklopljeno → obvezno potrdilo "Opozorilo *":
  gre za novo MM, treba izpolniti še vlogo B – prvi zavihek). Vklopljeno → verjetno št. MM / GSRN kot v koraku 4 (PREVERITI)
### Številke predhodno izdanih dokumentov
- Številka predhodno izdanega soglasja za priključitev, na katerega se bo dodal nov hranilnik (neobvezno)
### Tehnični podatki
- Vrsta tehnologije * (spustni seznam; PDF: LFP/NMC/NCA/LTO/Drugo)
- Naznačena kapaciteta * (kWh), Naznačena napetost * (V)
- Največja delovna moč polnjenja * (kW), Največja delovna moč praznjenja * (kW)
- Število faz * (spustni seznam), Priključna moč * (kW)
- Način vključevanja v DS priključna shema * (spustni seznam)
- Način obratovanja * – 4 potrditvena polja kot pri elektrarni
- (en spustni seznam med Način obratovanja in Katastrsko občino – verjetno "Na voljo za sistemske storitve", PREVERITI)
### Katastrska občina in parcelna številka
- gumb: Podatki o lokaciji so enaki podatkom na vlogi za soglasje (Kopiraj/Prenesi) → kopira iz koraka 4
- Katastrska občina * (iskalnik), Parcelna številka * (vejica)
- stikalo: Objekt se nahaja v več kot eni katastrski občini
### Priloge (image/*, pdf, dxf, dwg; 4 MB)
- Idejna zasnova vključitve hranilnika el. energije v distribucijsko omrežje (interno omrežje/el. inštalacijo), bančna garancija * – OBVEZNO
### Bančna garancija
- informativno besedilo: samo PS.1B ≥ 1 MW (rok 14 dni po pozivu); za samooskrbo ne velja
- … nadaljevanje ŠE NEZNANO
- Prazen korak 5 ima 13 obveznih polj

## 6. Opombe in potrditev
- Opombe (prosto besedilo, neobvezno)
- Klavzule (varstvo osebnih podatkov – besedilo kot v PDF)
- Strinjam se s pogoji, navedenimi v klavzulah * (potrditev)

## 7. Tiskaj – ŠE NEZNANO
## 8. Zaključi – ne klikati (oddaja)

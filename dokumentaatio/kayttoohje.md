# Käyttöohje

Lataa projektin viimeisimmän [releasen](https://github.com/kalevat/ot-harjoitustyo/releases) lähdekoodi.

## Konfigurointi

Tallennukseen käytettävien tiedostojen nimiä voi konfiguroida  _.env_-tiedostossa. Tietokanta luodaan _data_-hakemistoon, jos sitä ei  vielä ole. 
```
DATABASE_FILENAME=database.sqlite
```

## Ohjelman käynnistäminen

Ennen ohjelman käynnistämistä, asenna riippuvuudet komennolla:

```bash
poetry install
```

Jonka jälkeen suorita alustustoimenpiteet komennolla:

```bash
poetry run invoke build
```

Nyt ohjelman voi käynnistää komennolla:

```
poetry run invoke start
```

## Kirjautuminen

Ohjelma pyytää ensin kirjautumaan:

Kirjautuminen onnistuu kirjoittamalla olemassaoleva käyttäjätunnus ja salasana.

## Uuden käyttäjän luominen

Jos käyttäjää ei löydy tietokannasta, ohjelma kysyy halutaanko luoda uusi tunnus (k/e = kyllä/ei)

Salasanan tulee olla vähintään 5 merkkiä pitkä

## Toimintajärjestys
- (1) Luo uusi kurssi (syötä nimi ja opintopisteet)
- (5) Syötä tenttipäivämäärä (syötä kurssin nimi, päivämäärän tulee olla tulevaisuudessa)
- (6) Ilmoittaudu kurssille (syötä kurssin nimi)
- (7) Tulevat tentit (tulevaisuudessa olevat tentit listattuna)

## Muut toiminnallisuudet
- (2) Hae kurssit (näyttää listauksen kaikista kursseista)
- (3) Poista kurssi (voidaan poistaa kurssi)
- (4) Muuta tietoja (voidaan vaihtaa kurssin opintopisteet) 

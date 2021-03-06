# Kurssikirjanpito
Sovelluksella käyttäjä voi ylläpitää tietoja kursseista, joita hän opiskelee ja mitä päivittäisi kotitehtäviä on eri kursseissa. Myös kurssien perustiedot (op määrä, tenttiaikataulu, yms) voi tallentaa sovellukseen. Sovelluksesta on nähtävissä päivittäinen työlista ja tehtäviä voi merkitä tehdyiksi. 
**"Mitä mun pitää tänään tehdä?"**

## Dokumentaatio
- [Vaatimusmäärittely](dokumentaatio/vaatimusmaarittely.md)
- [Työaikakirjanpito](dokumentaatio/tuntikirjanpito.md)
- [Arkkitehtuurikuvaus](dokumentaatio/arkkitehtuuri.md)
- [Testausdokumentti](dokumentaatio/testaus.md)
- [Käyttöohje](dokumentaatio/kayttoohje.md)

## Asennus

1. Asenna riippuvuudet komennolla:

```bash
poetry install (tai python3 -m poetry install)
```

2. Suorita vaadittavat alustustoimenpiteet komennolla:

```bash
poetry run invoke build
```

3. Käynnistä sovellus komennolla:

```bash
poetry run python3 src/index.py
```
   (komento "poetry run invoke start" ei toimi kunnolla)

## Komentorivitoiminnot

### Ohjelman suorittaminen

Ohjelman pystyy suorittamaan komennolla:

```bash
poetry run python3 src/index.py
```
(komento "poetry run invoke start" ei toimi kunnolla)
### Testaus

Testit suoritetaan komennolla:

```bash
poetry run invoke test
```

### Testikattavuus

Testikattavuusraportin voi generoida komennolla:

```bash
poetry run invoke coverage-report
```

Raportti generoituu _htmlcov_-hakemistoon.

### Pylint

Tiedoston [.pylintrc](./.pylintrc) määrittelemät tarkistukset voi suorittaa komennolla:

```bash
poetry run invoke lint
```

## Releases
- [Viikon 5 release](https://github.com/kalevat/ot-harjoitustyo/releases/tag/viikko5)

## Huomautukset
Ohjelma tulee käynnistää "poetry run python3 src/index.py" käskyllä. Komento "poetry run invoke start" ei toimi kunnolla, kun käyttäjä antaa syötteitä.

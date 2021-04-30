# Käyttöohje

Lataa projektin viimeisimmän [releasen](https://github.com/kalevat/ot-harjoitustyo/releases) lähdekoodi

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


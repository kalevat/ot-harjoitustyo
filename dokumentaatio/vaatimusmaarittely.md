# Vaatimusmäärittely

## Sovelluksen tarkoitus
Sovelluksella käyttäjä voi ylläpitää tietoja kursseista, joita hän opiskelee ja mitä päivittäisi kotitehtäviä on eri kursseissa. Myös kurssien perustiedot (op määrä, tenttiaikataulu, yms) voi tallentaa sovellukseen. Sovelluksesta on nähtävissä päivittäinen työlista ja tehtäviä voi merkitä tehdyiksi. 
"Mitä mun pitää tänään tehdä?"

## Käyttäjät
Alkuvaiheessa sovelluksella on ainoastaan yksi käyttäjärooli eli normaali käyttäjä. Myöhemmin sovellukseen mahdollisesti lisätään pääkäyttäjä rooli.

## Käyttöliittymäluonnos
Sovellus koostuu eri näkymistä:
- kirjautuminen
- kurssitietojen hallinta
- päivänäkymä ja tehtävien kuittaus
- muut raportit

## Perusversion tarjoama toiminnallisuus

### Ennen kirjautumista
- käyttäjä voi luoda järjestelmään käyttäjätunnuksen
  - käyttäjätunnuksen täytyy olla uniikki ja pituudeltaan vähintään 5 merkkiä
- käyttäjä voi kirjautua järjestelmään
  - kirjautuminen onnistuu syötettäessä olemassaoleva käyttäjätunnus kirjautumislomakkeelle
  - jos käyttäjää ei olemassa, ilmoittaa järjestelmä tästä

### Kirjautumisen jälkeen
- käyttäjä näkee kyseisen päivän työlistan
- käyttäjä voi hallita kurssitietoja
  - luoda uuden kurssin
  - muuttaa tietoja
  - poistaa kurssin
- käyttäjä päivittäisen tehtävän tai kurssikokonaisuuden tehdyksi
- käyttäjä voi ajaa raportteja kurssitiedoistaan
- käyttäjä voi kirjautua ulos järjestelmästä

## Jatkokehitysideoita

Perusversion jälkeen järjestelmää täydennetään ajan salliessa esim. seuraavilla toiminnallisuuksilla
- lisää raportteja (myös graaffisia)
- viikko- ja periodinäkymä
- lisää käyttäjäryhmiä (esim pääkäyttäjä, raportoija)
- ryhmitellä kurssitehtäviä (laskarit, vertaisarviointi, essee, koodaus)
- työmäärien ylläpito ja tuntikirjaus
- kurssisuorituksien kirjaaminen (op, pvm, työmäärä)
-  

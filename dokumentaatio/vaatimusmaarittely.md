# Vaatimusmäärittely

## Sovelluksen tarkoitus
Sovelluksella käyttäjä voi ylläpitää tietoja kursseista, joita hän opiskelee ja mitä päivittäisi kotitehtäviä on eri kursseissa. Myös kurssien perustiedot (op määrä, tenttiaikataulu) voi tallentaa sovellukseen. Sovelluksesta on nähtävissä tulevat tentit. 
"Koska on seuraava tentti?"

## Käyttäjät
Alkuvaiheessa sovelluksella on ainoastaan yksi käyttäjärooli eli normaali käyttäjä. Myöhemmin sovellukseen mahdollisesti lisätään pääkäyttäjä rooli.

## Käyttöliittymäluonnos
Sovellus koostuu eri toiminnoista:
- kirjautuminen (*tehty*)
- kurssitietojen hallinta (*tehty*)
- raportit (*tehty*)

## Perusversion tarjoama toiminnallisuus

### Ennen kirjautumista
- käyttäjä voi luoda järjestelmään käyttäjätunnuksen (*tehty*)
  - käyttäjätunnuksen täytyy olla uniikki ja pituudeltaan vähintään 5 merkkiä (*tehty*)
- käyttäjä voi kirjautua järjestelmään (*tehty*)
  - kirjautuminen onnistuu syötettäessä olemassaoleva käyttäjätunnus kirjautumislomakkeelle (*tehty*)
  - jos käyttäjää ei olemassa, ilmoittaa järjestelmä tästä (*tehty*)

### Kirjautumisen jälkeen
- käyttäjä voi hallita kurssitietoja
  - luoda uuden kurssin (*tehty*)
  - muuttaa tietoja (*tehty*)
  - poistaa kurssin (*tehty*)
- käyttäjä voi ajaa raportteja kurssitiedoistaan (*tehty*)
- käyttäjä näkee tulevat tentit (*tehty*)
- käyttäjä voi kirjautua ulos järjestelmästä (*tehty*)
 

## Jatkokehitysideoita

Perusversion jälkeen järjestelmää täydennetään ajan salliessa esim. seuraavilla toiminnallisuuksilla.
- lisää raportteja (myös graaffisia)
- viikko- ja periodinäkymä
- lisää käyttäjäryhmiä (esim pääkäyttäjä, raportoija)
- ryhmitellä kurssitehtäviä (laskarit, vertaisarviointi, essee, koodaus)
- työmäärien ylläpito ja tuntikirjaus
- kurssisuorituksien kirjaaminen (op, pvm, työmäärä)

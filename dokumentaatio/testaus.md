# Testausdokumentti

Ohjelmaan on tehty kattavat automatisoidut yksikkö- ja integraatiotestit unittestilla. Lisäksi on tehty manuaalisesti testausta.

## Yksikkö- ja integraatiotestaus

### Repositorio-luokat

Repositorio-luokkaa `CourseRepository` testataan tekemällä vastaavia tietokantatoimintoja. Testitietokannan nimi on konfiguroitu _.env.test_-tiedostoon. `CourseRepository`-luokkaa testataan [TestData](https://github.com/kalevat/ot-harjoitustyo/blob/master/src/tests/course_test.py)-testiluokalla.

### LoginMenu-luokka

Sisäänkirjautumisen luokkaa `LoginMenu` testataan tekemällä uusi käyttäjä ja tarkistamalla sisäänkirjautumisen toimivuus. `LoginMeny`-luokkaa testataan [TestLogin](https://github.com/kalevat/ot-harjoitustyo/blob/master/src/tests/login_test.py)-testiluokalla.

### Testauskattavuus

Käyttöliittymän valikkoja ei testata. Testauksen haarautumakattavuus on 97%

![](kuvat/testikattavuus.png)

## Järjestelmätestaus

Sovelluksen järjestelmätestaus on suoritettu manuaalisesti. Apuna on käytetty ulkopuolista testaajaa, joka on tehnyt testejä käyttöohjeen mukaisesti.

### Asennus ja konfigurointi

Sovelluksen asennusta ja käyttöä on testattu [käyttöohjeen](./kayttoohje.md) kuvaamalla tavalla kahdessa eri Linux-ympäristöön.

## Sovellukseen jääneet laatuongelmat

Sovelluksen päävalikon toiminnallisuutta testattiin vain manuaalisesti. Siihen ei tehty automaattitestejä.

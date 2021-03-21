import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassapaate = Kassapaate()
        self.maksukortti = Maksukortti(10)

    def test_luotu_kortti_on_olemassa(self):
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_lounaide_maara_alussa(self):
        self.assertEqual(self.kassapaate.edulliset, 0)
        self.assertEqual(self.kassapaate.maukkaat, 0)

    def test_edullinen_osto_kassa(self):
        self.assertEqual(self.kassapaate.syo_edullisesti_kateisella(250),10)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100240)
        self.assertEqual(self.kassapaate.edulliset, 1)

    def test_edullinen_osto_kassa_ei_riittava(self):
        self.assertEqual(self.kassapaate.syo_edullisesti_kateisella(200),200)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(self.kassapaate.edulliset, 0)
    
    def test_korttiosto_edullinen_onnistuu(self):
        self.maksukortti.lataa_rahaa(500)
        self.assertEqual(self.kassapaate.syo_edullisesti_kortilla(self.maksukortti),True)
        self.assertEqual(self.kassapaate.edulliset, 1)

    def test_korttiosto_edullinen_vahan_rahaa(self):
        self.assertEqual(self.kassapaate.syo_edullisesti_kortilla(self.maksukortti),False)
        self.assertEqual(self.kassapaate.edulliset, 0)
        self.assertEqual(str(self.maksukortti), "saldo: 0.1")
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_kortille_rahaa(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti,500)
        self.assertEqual(str(self.maksukortti), "saldo: 5.1")
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100500)

    def test_maukkaasti_kortilla(self):
        self.maksukortti.lataa_rahaa(500)
        self.assertEqual(self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti),True)
        self.assertEqual(self.kassapaate.maukkaat, 1)

    def test_maukas_osto_kassa(self):
        self.assertEqual(self.kassapaate.syo_maukkaasti_kateisella(450),50)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100400)
        self.assertEqual(self.kassapaate.maukkaat, 1)

    def test_kortille_nega_rahaa(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti,-100)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_korttiosto_maukas_vahan_rahaa(self):
        self.assertEqual(self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti),False)
        self.assertEqual(self.kassapaate.maukkaat, 0)
        self.assertEqual(str(self.maksukortti), "saldo: 0.1")
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_maukas_osto_kassa_vaara(self):
        self.assertEqual(self.kassapaate.syo_maukkaasti_kateisella(150),150)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(self.kassapaate.maukkaat, 0)
    
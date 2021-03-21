import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(10)

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)

    def test_alkusaldo_oikein(self):
        self.assertEqual(str(self.maksukortti), "saldo: 0.1")
    
    def test_rahan_lataaminen(self):
        self.maksukortti.lataa_rahaa(990)
        self.assertEqual(str(self.maksukortti), "saldo: 10.0")

    def test_raha_pienee(self):
        self.maksukortti.lataa_rahaa(990)
        self.maksukortti.ota_rahaa(100)
        self.assertEqual(str(self.maksukortti), "saldo: 9.0")

    def test_raha_pienee(self):
        self.maksukortti.lataa_rahaa(990)
        self.maksukortti.ota_rahaa(1200)
        self.assertEqual(str(self.maksukortti), "saldo: 10.0")

    def test_rahat_ottaminen_true(self):
        self.maksukortti.lataa_rahaa(990)
        self.assertEqual(self.maksukortti.ota_rahaa(100), True)
    
    def test_rahat_ottaminen_flase(self):
        self.maksukortti.lataa_rahaa(990)
        self.assertEqual(self.maksukortti.ota_rahaa(1200), False)
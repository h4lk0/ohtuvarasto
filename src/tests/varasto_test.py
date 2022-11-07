import unittest
from varasto import Varasto


class TestVarasto(unittest.TestCase):
    def setUp(self):
        self.varasto = Varasto(10)

    def test_konstruktori_luo_tyhjan_varaston(self):
        # https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertAlmostEqual
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_uudella_varastolla_oikea_tilavuus(self):
        self.assertAlmostEqual(self.varasto.tilavuus, 10)

    def test_lisays_lisaa_saldoa(self):
        self.varasto.lisaa_varastoon(8)

        self.assertAlmostEqual(self.varasto.saldo, 8)

    def test_lisays_lisaa_pienentaa_vapaata_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        # vapaata tilaa pitäisi vielä olla tilavuus-lisättävä määrä eli 2
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 2)

    def test_ottaminen_palauttaa_oikean_maaran(self):
        self.varasto.lisaa_varastoon(8)

        saatu_maara = self.varasto.ota_varastosta(2)

        self.assertAlmostEqual(saatu_maara, 2)

    def test_ottaminen_lisaa_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        self.varasto.ota_varastosta(2)

        # varastossa pitäisi olla tilaa 10 - 8 + 2 eli 4
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 4)

    def test_negatiivinen_alkutilavuus(self):
        varasto = Varasto(-1)

        self.assertAlmostEqual(varasto.tilavuus, 0)

    def test_negatiivinen_alkusaldo(self):
        varasto = Varasto(5,-1)

        self.assertAlmostEqual(varasto.saldo, 0)

    def test_alkusaldo_menee_yli(self):
        varasto = Varasto(5, 7)

        self.assertAlmostEqual(varasto.saldo, 5)

    def test_negatiivinen_lisays_ei_muuta_saldoa(self):
        self.varasto.lisaa_varastoon(2)
        alkusaldo = self.varasto.saldo
        self.varasto.lisaa_varastoon(-15)

        self.assertAlmostEqual(self.varasto.saldo, alkusaldo)

    def test_lisays_ylittaa_tilavuuden(self):
        self.varasto.lisaa_varastoon(99)

        self.assertAlmostEqual(self.varasto.saldo, self.varasto.tilavuus)

    def test_negatiivinen_otto_mahdoton(self):
        self.varasto.lisaa_varastoon(3)
        tulos = self.varasto.ota_varastosta(-1)

        self.assertAlmostEqual(tulos, 0)

    def test_iso_otto_tyhjentaa_varaston(self):
        self.varasto.lisaa_varastoon(3)
        self.varasto.ota_varastosta(4)

        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_iso_otto_palauttaa_koko_saldon(self):
        self.varasto.lisaa_varastoon(5)
        tulos = self.varasto.ota_varastosta(7)

        self.assertAlmostEqual(tulos, 5)

    def test_palauttaa_oikean_merkkijonon(self):
        self.varasto.lisaa_varastoon(4)
        tulos = str(self.varasto)

        self.assertEqual(tulos, "saldo = 4, vielä tilaa 6")
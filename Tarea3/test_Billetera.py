# -*- coding: utf-8 -*-
'''
Created on 11 de may. de 2016

@author: Alex & Amin
'''
import unittest
from Billetera import *
from datetime import timedelta, datetime


class Test_BilleteraElectronica(unittest.TestCase):

    @classmethod
    def setUp(self):
        self.BilleteraPrueba = BilleteraElectronica(0000,"Pedro","Perez",1111,"abc123")

    def testBilletera(self):
        self.assertEqual(self.BilleteraPrueba.ID , 0000, "El ID debe ser 0000")
        self.assertEqual(self.BilleteraPrueba.Nombres , "Pedro", "El nombre debe ser Pedro")
        self.assertEqual(self.BilleteraPrueba.Apellidos , "Perez", "El apellido debe ser Perez")
        self.assertEqual(self.BilleteraPrueba.CI , 1111, "El CI debe ser 1111")
        self.assertEqual(self.BilleteraPrueba.PIN , "abc123", "El PIN debe ser abc123")
        self.assertEqual(self.BilleteraPrueba.recargas , [], "Las recargas deben ser una lista vacia")
        self.assertEqual(self.BilleteraPrueba.consumos , [], "Los consumos deben ser una lista vacia")

    def testBilleteraSpanishChars(self):
        LatinBilletetera = BilleteraElectronica(0000,"áéíóúüÁÉÍÓÚÜ","ñÑ",1111,"abc123")
        self.assertEqual(LatinBilletetera.Nombres,"áéíóúüÁÉÍÓÚÜ")
        self.assertEqual(LatinBilletetera.Apellidos, "ñÑ")
        
    def testRecarga(self):
        recarga = Recarga(10, datetime(2016,5,11,15,0), 1)
        self.assertEqual(recarga.monto, 10)
        self.assertEqual(recarga.fecha, datetime(2016,5,11,15,0))
        self.assertEqual(recarga.ID, 1)

    def tesRecargaNegativa(self):
        with self.assertRaises(AssertionError):
            self.BilleteraPrueba.recargar(-10, datetime(2016,5,11,15,0), 1)
            
    def testRecargaFutura(self):
        with self.assertRaises(AssertionError):
            self.BilleteraPrueba.recargar(10, datetime(2017,5,11,15,0), 1)

    def testConsumo(self):
        consumo = Consumo(10, datetime(2016,5,11,15,0), 1)
        self.assertEqual(consumo.monto, 10)
        self.assertEqual(consumo.fecha, datetime(2016,5,11,15,0))
        self.assertEqual(consumo.ID, 1)

    def testSaldo(self):
        self.assertEqual(self.BilleteraPrueba.saldo(), 0, "El saldo debe ser 0")

    def testRecargar(self):
        recarga = Recarga(10, datetime(2016,5,11,15,0), 1)
        self.BilleteraPrueba.recargar(10, datetime(2016,5,11,15,0), 1)
        self.assertEqual(self.BilleteraPrueba.saldo(), 10, "El saldo debe ser 10")
        self.assertEqual(self.BilleteraPrueba.recargas[-1], recarga)

    def testConsumir(self):
        consumo = Consumo(10, datetime(2016,5,11,15,0), 1)
        recarga = Recarga(10, datetime(2016,5,11,15,0), 1)
        self.BilleteraPrueba.recargar(10, datetime(2016,5,11,15,0), 1)
        self.BilleteraPrueba.consumir(10, datetime(2016,5,11,15,0), 1, "abc123")

        self.assertEqual(self.BilleteraPrueba.saldo(), 0, "El saldo debe ser 0")
        self.assertEqual(self.BilleteraPrueba.consumos[-1], consumo)

    def testConsumirPinIncorrecto(self):
        consumo = Consumo(10, datetime(2016,5,11,15,0), 1)
        recarga = Recarga(10, datetime(2016,5,11,15,0), 1)
        self.BilleteraPrueba.recargar(10, datetime(2016,5,11,15,0), 1)

        with self.assertRaises(Exception):
            self.BilleteraPrueba.consumir(10, datetime(2016,5,11,15,0), 1, "blah")

    def testConsumirSaldoInsuficiente(self):
        consumo = Consumo(10, datetime(2016,5,11,15,0), 1)

        with self.assertRaises(Exception):
            self.BilleteraPrueba.consumir(10, datetime(2016,5,11,15,0), 1, "abc123")


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
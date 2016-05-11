'''
Created on 11 de may. de 2016

@author: Alex & Amin
'''
import unittest
from Billetera import *
from datetime import timedelta, datetime


class Test_BilleteraElectronica(unittest.TestCase):

    def testBilletera(self):
        BilleteraPrueba = BilleteraElectronica(0000,"Pedro","Perez",1111,"abc123")
        self.assertEqual(BilleteraPrueba.ID , 0000, "El ID debe ser 0000")
        self.assertEqual(BilleteraPrueba.Nombres , "Pedro", "El nombre debe ser Pedro")
        self.assertEqual(BilleteraPrueba.Apellidos , "Perez", "El apellido debe ser Perez")
        self.assertEqual(BilleteraPrueba.CI , 1111, "El CI debe ser 1111")
        self.assertEqual(BilleteraPrueba.PIN , "abc123", "El PIN debe ser abc123")
        self.assertEqual(BilleteraPrueba.recargas , [], "Las recargas deben ser una lista vacia")
        self.assertEqual(BilleteraPrueba.debitos , [], "Los debitos deben ser una lista vacia")

    def testRecarga(self):
        recarga = Recarga(10, datetime(2016,5,11,15,0), 1)
        self.assertEqual(recarga.monto, 10)
        self.assertEqual(recarga.fecha, datetime(2016,5,11,15,0))
        self.assertEqual(recarga.ID, 1)

    def testConsumo(self):
        consumo = Consumo(10, datetime(2016,5,11,15,0), 1)
        self.assertEqual(consumo.monto, 10)
        self.assertEqual(consumo.fecha, datetime(2016,5,11,15,0))
        self.assertEqual(consumo.ID, 1)

    def testSaldo(self):
        BilleteraPrueba = BilleteraElectronica(0000,"Pedro","Perez",1111,"abc123")
        self.assertEqual(BilleteraPrueba.saldo(), 0, "El saldo debe ser 0")
        
    
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
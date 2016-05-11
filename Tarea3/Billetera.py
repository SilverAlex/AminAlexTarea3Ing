'''
Created on 11 de may. de 2016

@author: Alex & Amin
'''

from datetime import timedelta, datetime

class Recarga():
    def __init__(self, monto, fecha, Id):
        self.monto = monto
        self.fecha = fecha
        self.ID = Id

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

class Consumo():
    def __init__(self, monto, fecha, Id):
        self.monto = monto
        self.fecha = fecha
        self.ID = Id

    def __eq__(self, other):
        return self.__dict__ == other.__dict__


class BilleteraElectronica():

    def __init__(self, Id, nombres, apellidos, ci, PIN):
        self.ID = Id
        self.Nombres = nombres
        self.Apellidos = apellidos
        self.CI = ci
        self.PIN = PIN
        self.recargas = []
        self.consumos = []
        self.Saldo = 0

    def saldo(self):
        return self.Saldo

    def recargar(self, monto, fecha, id):
        assert monto > 0
        assert fecha <= datetime.now()
        self.Saldo += monto
        recarga = Recarga(monto, fecha, id)
        self.recargas.append(recarga)

    def consumir(self, monto, fecha, id, PIN):
        assert monto > 0
        assert fecha <= datetime.now()

        if(not self.PIN == PIN):
            raise Exception("PIN incorrecto")
        if(monto > self.saldo()):
            raise Exception("Saldo insuficiente")

        consumo = Consumo(monto, fecha, id)
        self.Saldo -= monto
        self.consumos.append(consumo)
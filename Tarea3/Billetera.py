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

class Consumo():
    def __init__(self, monto, fecha, Id):
        self.monto = monto
        self.fecha = fecha
        self.ID = Id

class BilleteraElectronica():

    def __init__(self, Id=None, nombres=None, apellidos=None, ci=None, PIN=None):
        self.ID = Id
        self.Nombres = nombres
        self.Apellidos = apellidos
        self.CI = ci
        self.PIN = PIN
        self.recargas = []
        self.debitos = []

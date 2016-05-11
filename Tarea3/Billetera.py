'''
Created on 11 de may. de 2016

@author: Alex & Amin
'''
"""
class recargas():
    def __init__(self, monto, fecha, Id):
        self.monto = monto
        self.fecha = fecha
        self.Id = Id

class consumos():
    def __init__(self, monto, fecha, Id):
        self.monto = monto
        self.fecha = fecha
        self.Id = Id
"""     
class BilleteraElectronica():
    
    def __init__(self, Id=None, nombres=None, apellidos=None, ci=None, PIN=None):
        self.ID = Id
        self.Nombres = nombres
        self.Apellidos = apellidos
        self.CI = ci
        self.PIN = PIN
        self.recargas = []
        self.debitos = []
        
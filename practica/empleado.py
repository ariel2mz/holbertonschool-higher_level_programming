#!/usr/bin/python3
class Employee():

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    
    def get_details(self):
        print(f"{self.name}")
        print(f"{self.salary}")
    
class Manager(Employee):

    def get_details(self):
        print("QUESO HISTORICO")
    
empleado = Employee("juani", "5pesos")
Employee.get_details(empleado)
Manager.get_details(empleado)
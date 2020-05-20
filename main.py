import pytest
from abc import ABC, abstractmethod

class Departament:
    def __init__(self, name, code):
        self.name = name
        self.code = code


class Employee(ABC):

    def __init__(self, code, name, salary, departament):
        self.code = code
        self.name = name
        self.salary = salary
        self.__department= departament.name


    def calc_bonus(self):
        pass

    def get_hours(self):
        return 8

    def get_departament(self):
        return self.__departament

    def set_departament(self, departament):
        self.__departament.name = departament


class Manager(Employee):
    def __init__(self, code, name, salary):
        super().__init__(code, name, salary, Departament('managers', 1))
        self.__sales = salary
        self.__depart = Departament('managers',1)

    def calc_bonus(self):
        return (self.__sales * 0.15)

    def get_departament(self):
        return self.__depart


class Seller(Employee):
    def __init__(self, code, name, salary):
        super().__init__(code, name, salary, Departament('sellers', 2))
        self.__sales = 0
        self.__depart = Departament('managers', 1)

    def get_sales(self):
        return self.__sales

    def  put_sales(self, sales):
        self.__sales +=sales

    def calc_bonus(self):
        #print self.__sales * 0.15
        return self.__sales * 0.15

    def get_departament(self):
        return self.__depart.name








#Employee(123, 123, 123)
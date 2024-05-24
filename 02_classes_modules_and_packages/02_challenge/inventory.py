class Vehicle:
    def __init__(self, model=None, make=None, year=None, price=None, discount=None) -> None:
        self.model = model
        self.make = make
        self.year = year
        self.price = price
        self.discount = discount

    def set_model(self, model):
        self.model = model
    def get_model(self):
        return self.model

    def set_make(self, make):
        self.make = make
    def get_make(self):
        return self.make

    def set_year(self, year):
        self.year = year
    def get_year(self):
        return self.year

    def set_price(self, price):
        self.price = price
    def get_price(self):
        return self.price
    
    def set_discount(self, discount):
        self.discount = discount
    def get_discount(self):
        return self.discount
    
    def display(self):
        print("model:" + self.model + ", make:" + self.make
               + ", year" +  str(self.year) +  ", price:" 
               + str(self.price) +  ", discount:" + str(self.discount))
    

import re
class Inventory:
    def __init__(self) -> None:
        self.vehicles = []

    def add_vehicle(self, vehicle):
        self.vehicles.append(
            Vehicle(vehicle["model"],vehicle["make"],
                    vehicle["year"],vehicle["price"],vehicle["discount"])
        )
    
    def discounted(self, v, discount):
        """
        割引を適用したVehicleインスタンスを返す
        """
        v.discount = discount
        return v

    def apply_discount(self, f, discout):
        """
        self.vehiclesのうち条件に合うものだけを割引して、その他は割引しない
        """
        self.vehicles = [self.discounted(v, discout) if f(v) else v for v in self.vehicles]

    def search_vehicles(self, key_wrd):
        # vehicles = [v for v in self.vehicles if key_wrd in v.model]
        vehicles = [v for v in self.vehicles 
                    if not(re.fullmatch(f'[a-zA-Z0-9_]*{key_wrd}[a-zA-Z0-9_]*', v.model) is None)]
        return vehicles

    def retrieve_vehicles(self):
        for v in self.vehicles:
            yield v 
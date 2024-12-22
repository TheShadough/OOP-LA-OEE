class Kabayo:
    def __init__(self, brand, model, fuel_type):
        self.brand= brand
        self.model= model
        self.fuel_type= fuel_type
        
    def __str__(self):
        return f"  {self.brand} {self.model}  is using {self.fuel_type}"

class Car(Kabayo):
    pass
chikot= Car("Mitsubishi", "Mirage G4" , "Premium" )
print(chikot)

class Motorcycle(Kabayo):
    pass
broombroom= Motorcycle("Honda", "Beat" , "Premium" )
print(broombroom)
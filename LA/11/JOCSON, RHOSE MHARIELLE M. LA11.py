class Phone:
    def __init__(self, brand, model):
        self.brand= brand
        self.model= model
        
    def __str__(self):
        return f" {self.brand} {self.model}, was released year 2021"



class Android(Phone):
    def __init__(self, brand, model):
        Phone.__init__(self, brand, model)

silpon= Android("Oppo", "A55" )
print(silpon)
        
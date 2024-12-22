class MobileLegendHero:
    def __init__(self, hero_name, role):
        self.hero_name = hero_name
        self.role=role

    def __str__(self):
        return f"{self.hero_name} is a {self.role} hero." 

mm = MobileLegendHero("Hanabi", "Marksman")
print(mm) 
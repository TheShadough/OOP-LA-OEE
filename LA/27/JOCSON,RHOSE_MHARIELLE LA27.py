from abc import ABC, abstractmethod 

class Pagong(ABC):
    @abstractmethod 
    def langoy(self):
        pass

class Leonardo(Pagong):
    def langoy(self):
        print("Leonardo")

class MichaelAngelo(Pagong):
    def langoy(self):
        print("Michael Angelo")



class Donatello(Pagong):
    def langoy(self):
        print("Donatello")

class Raphael(Pagong):
    def langoy(self):
        print("Raphael")



if __name__ == "__main__":
    
    print ("Ang hirap naman nito sir hahahhahaha")

    rap= Raphael.langoy= "RAPSZKIE"
    print(rap)

    le= Leonardo.langoy= "LENGSSZZ"
    print(le)

    donz= Donatello.langoy= "DONDONOBONAN"
    print(donz)

    makz= MichaelAngelo.langoy= "MAK MAK MAK"
    print(makz)

class CarApp:
    '''car applcation for customer'''

    def __init__(self,name):
        '''Initializing of carapp class'''
        print("----------Constructor method called----------") #gets automatically called when oject is created.
        self.name = name
        print("car name: ",name)


    def info(self,cname):
        '''car info method'''
        print("----------function method is called here----------")
        self.cname = cname #object/instance variable
        print("Its a Audi Car", cname)


if __name__ == '__main__': #We can use if __name__ == "__main__" block to allow or prevent parts of code from being run when the modules are imported. 
    Audicar = CarApp("Kia")
    #dir(Audicar) - list object attribute
    print("doc string called from class: ",Audicar.__doc__) #print docstring
    Audicar.info("Audi")
    print(Audicar.cname)

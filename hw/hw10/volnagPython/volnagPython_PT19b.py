##Create a Car class with the attributes : ##name, kind, model
##and ##methods of start and stop,
##which indicate information that the car started or stoped accordingly.
#--------HW10--PT19b----July 27, 2023---

class Car:
    def __init__(self,name,kind,model,transmission):
        self.name = name
        self.kind = kind
        self.model = model
        self.transmission = transmission
    def __str__(self):
        return "-Car from inventory-"

    def start(self):
        start = input("Did it start already?  Y/N  :")
        if start == "Y":
            print("---It started accordingly.---")
        else:
            print("---It didn't start accordingly.---")
    def stop(self):
        stop = input("Did it stop properly?  Y/N  :")
        if stop == "Y":
            print("---It stopped properly.---")
        else:
            print("---It didn't stop properly.---")
            
##############----Cheking results-----######################   
c = Car("Ford","truck","F150","manual")
print(c)
print(c.name)
print(c.transmission)
c.start()
c.stop()


class Car:
    'This is a class about Car'

    def __init__(self,manufacturer,model,make, transmission,color):
        self.manufacturer=manufacturer
        self.model=model
        self.make=make
        self.transmission=transmission
        self.color=color

    def accelerate(self):
        accString=("The {} {} is moving")
        print(accString.format(self.manufacturer,self.model))

    def stop(self):
        stpString=("The {} {} has stopped")
        print(stpString.format(self.manufacturer,self.model))

c1=Car("Hyndai","Verna","2010","Manual","Black")
c2=Car("Renault","Duster","2014","Manual","Brown")
c3=Car("Tata","Nano","2014","Automatic","Yellow")

c1.accelerate()
c1.stop()

c2.accelerate()
c2.stop()

c3.accelerate()
c3.stop()


# Created on 2024/03/02
# By Suman Regmi

class vehicle:
    def __init__(self,brand,model,max_speed):
        self.brand = brand
        self.model = model
        self.max_speed = max_speed
      
    def display_info(self):
        print("Brand : ",self.brand)
        print("Model : ",self.model)
        print("Maximum Speed : ",self.max_speed,"Kmph")

class car(vehicle):
    pass            #This inheritates everthing of parent class

class bike(vehicle):
    def __init__(self,brand,model,max_speed):
        self.brand = brand
        self.model = model
        self.max_speed = max_speed
        
        #Another way
        # vehicle.__init__(self,brand,model,max_speed)      #calling constructor of the parent class
    
    def display_info(self):         #Overridden method in child class
        print("\nBrand : ",self.brand)
        print("Model : ",self.model)
        print("Maximum Speed : ",self.max_speed,"Kmph")

        # #Differnt ways of calling parent methods
        # vehicle.display_info(self) #calling the inherited class method
        # return super().display_info() #returning value to the parent class

        
    
my_car=car('Toyota','Corolla',150)
my_car.display_info()
my_bike = bike('Yamaha','FZs',45)
my_bike.display_info()

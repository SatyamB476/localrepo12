class company:
    def __init__(self,name_company,type_car):
     self.name_com=name_company
     self.type_car=type_car

class car(company):
   def __init__(self,name):
      super().__init__("toyota","suv")
      self.name=name
    
   def show(self):
      print("name of the company:",self.name_com)
      print("name of the car",self.name)
      print("type of the car",self.type_car)

obj=car("fortuner")
obj.show()
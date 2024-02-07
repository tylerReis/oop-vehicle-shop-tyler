import re


class CarManager:
    all_cars = {}
    total_cars = 0
    TERMINAL = ["1. Add a car",
                "2. View all cars",
                "3. View total number of cars",
                "4. See a car's details",
                "5. Service a car",
                "6. Update mileage",
                "7. Quit"] 
    
    def __init__(self, make, model, year, mileage = None, services = None):
        self._id = CarManager.total_cars + 1
        CarManager.total_cars += 1
        self._make = make 
        self._model = model
        self._year = year
        self._mileage = mileage
        self._services = services

        

    def __str__(self):
        return f"ID: {self._id}, Make: {self._make}, Model: {self._model}, Year: {self._year}, Mileage: {self._mileage}, Services: {self._services}"
    

    @staticmethod
    def menu_actions(input):
        match input:
            case "1":
                CarManager.add_car()
            case "2":
                CarManager.view_all_cars()
            case "3":
                CarManager.view_num_cars()
            case "4":
                CarManager.see_car_details()
            case "5":
                CarManager.car_service()
            case "6":
                CarManager.update_mileage()

   # Class Properties
    @property
    def get_id(self):
        return self._id
    
    @property
    def get_make(self):
        return self._make.title()
    
    @property
    def get_model(self):
        return self._model.title()
    
    @property
    def get_year(self):
        return self._year
    
    @property
    def get_mileage(self):
        return  self._mileage
    
    @property
    def get_service_history(self):
        return self._services
    
     #Setters
    @get_make.setter
    def set_make(self, new_make):
        if self.check_string(new_make):
            self._make = new_make.lower()

    @get_model.setter
    def set_model(self, new_model):
        if self.check_string(new_model):
            self._model = new_model

    @get_year.setter
    def set_year(self, new_year):
        if self.check_int(new_year) and len(str(new_year)) == 4:
            self._year = new_year
        else:
            print(('Invalid year: enter year in the yyyy format'))

    
    # def set_mileage(new_mileage):
    #     if CarManager.check_int(new_mileage):
    #         print(f'You cannot reduce car mileage') 
    #         new_try = input("Enter mileage: ") 
    #         self.set_mileage(new_try)

    @staticmethod
    def terminal_menu():
        user_input = input(f"Select an option {CarManager.TERMINAL}:")
        CarManager.menu_actions(user_input)

    @classmethod
    def add_car(cls):
        owner_name = input("Enter name in First_Last format: ")
        new_make = input("Enter make: ") 
        new_model = input("Enter model: ")
        new_year = CarManager.check_int(input("Enter year: "), "year")
        new_mileage = CarManager.check_int(input("Enter Mileage: "), "Mileage")
            

        new_car = cls(new_make, new_model, new_year, new_mileage)
        # print(new_car)
        CarManager.all_cars[owner_name] = new_car
        CarManager.terminal_menu()
        # print(new_car)
        #[f"ID: {new_car._id}", f"Make: {new_car._make}", f"Model: {new_car._model}", f"Year: {new_car._year}", f"Mileage: {new_car._mileage}", f"Services: {new_car._services}" ]
   
    def view_all_cars():
        for car in CarManager.all_cars:
             print(car, CarManager.all_cars[car])
        CarManager.terminal_menu()
    
    def view_num_cars():
        print(CarManager.total_cars)
        CarManager.terminal_menu()   

    def see_car_details():
        owner_search = input("Please enter owner to search in First_Last format: ")
        print(CarManager.all_cars[owner_search])
        CarManager.terminal_menu()
    
    def car_service():
        owner_name = input("Enter owner name in First_last format: ")
        service = input("Enter all services: ")
        CarManager.all_cars[owner_name]._services = service
        CarManager.terminal_menu()
    
    def update_mileage():
        owner_name = input("Enter owner name in First_last format: ")
        mileage = input("Enter mileage: ")
        if CarManager.check_int(mileage):
            if mileage > CarManager.all_cars[owner_name]._mileage:
                CarManager.all_cars[owner_name]._mileage = mileage
                CarManager.terminal_menu()
        else:
            print("Mileage must be a number and contain no decimals")
            CarManager.update_mileage()
            
        
    
    @staticmethod
    def check_int(value, Variable):
        try:
                return int(value)
        except:
                print("Input Error: Numeric values only.")
                CarManager.check_int(input(f"Enter {Variable}: "), Variable)


        

# action = input("Please enter what you would like to do. Add a car - enter 'Add' | View all cars - enter 'View all' | View total number of car - enter 'View num' | See a car's details - enter 'See car'. : ")
# if action == "Add":
#     owner_car = input("Please enter owner name: ")  
#     owner_name =  re.sub(r"\s", '_', owner_car)
#     new_make, new_model, new_year = input("Enter make: "), input("Enter model: "), input("Enter year: ")
#     new_car = CarManager(new_make, new_model, new_year)
#     new_car.add_car()
#     print(CarManager.view_all_cars())
#     action
print(CarManager.terminal_menu())


# car1 = CarManager()
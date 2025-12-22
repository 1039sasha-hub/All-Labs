#Задание 1
class UserAccount:
    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.__password = password

    def set_password(self, new_password):
        self.__password = new_password
        return f'Пароль изменен'

    def chek_password(self, password):
        if self.__password == password:
            return True
        else:
            return False
        
account = UserAccount('sanchez', '1039sasha@gmail.com', '1234')
account.set_password('4321')
print(account.chek_password('1244'))

#Задание 2
class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def get_info(self):
        return f'{self.make}, {self.model}'
    
class Car(Vehicle):
    def __init__(self, make, model, fuel_type):
        super().__init__ (make, model)
        self.fuel_type = fuel_type

    def get_info(self):
        return f'{self.make}, {self.model}, {self.fuel_type}'
    
a = Vehicle('Daewoo', 'Matiz')
car1 = Car('Ford', 'Mustang', 'бензин')
print(a.get_info())
print(car1.get_info())
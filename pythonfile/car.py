class Car():
    '''一次模拟汽车的简单尝试'''
    def __init__(self, make, model, year):
        '''初始化描述汽车的属性'''
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get__descriptive_name(self):
        '''返回整洁的描述信息'''
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    def read_odometer(self):
        '''打印一条指出汽车历程的消息'''
        print("This cat has " + str(self.odometer_reading) + " miles on it .")
    def update_odometer(self, mileage):
        self.odometer_reading = mileage 

    '''def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")
    '''
    def increment_odometer(self, miles):
        self.odometer_reading += miles
my_new_car = Car('audi', 'a4', 2018)
print(my_new_car.get__descriptive_name())
my_new_car.read_odometer()
my_new_car.odometer_reading = 23
my_new_car.read_odometer()
my_new_car.update_odometer(35)
my_new_car.read_odometer()
my_user_cat = Car('路虎', 'outback', '\n2018')
print(my_user_cat.get__descriptive_name())
my_user_cat.update_odometer(3500)
my_user_cat.read_odometer()

my_user_cat.increment_odometer(100)
my_user_cat.read_odometer()

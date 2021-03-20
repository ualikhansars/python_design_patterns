import datetime


def run_only_on_monday(fn):
    weekday = datetime.datetime.today().weekday()

    def wrapper():
        if weekday == 0:
            fn()
        else:
            print("today is not monday")

    return wrapper


def run_only_on_tuesday(fn):
    weekday = datetime.datetime.today().weekday()

    def wrapper(*args, **kwargs):
        if weekday == 1:
            fn(*args, **kwargs)
        else:
            print("today is not tuesday")

    return wrapper


def parameterize(fn):
    def wrapper(*args):
        for arg in args:
            fn(arg)

    return wrapper

@parameterize
def print_number(number):
    print("print number {}".format(number))


#run on monday
def test():
    print("Test is running")

@run_only_on_tuesday
def tuesday_test(*args, **kwargs):
    print("Tuesday tests is running")

#run test on monday
#run_tests_on_monday = run_only_on_monday(test)
#run_tests_on_monday()


#run test on tuesday
tuesday_test(1, 2, 3, arhs="ahsjdjhas")

#print_number(1, 2, 3, 4, 5)


class CheckDatabaseConnection:
    connection = True

    def __init__(self, fn):
        self.fn = fn

    def __call__(self, *args, **kwargs):
        if self.connection:
            return self.fn(*args, **kwargs)
        else:
            raise Exception("database connection failed")

@CheckDatabaseConnection
def get_users():
    print('fetching users from database')

#get_users()



#Вложенность декораторов
def connect_to_database():
    print("connection established")

def display_customers(fn):
    def wrapper():
        customers = fn()
        print("Function name", fn.__name__)
        for customer in customers:
            print("customer is ", customer)

    return wrapper

def open_connection(fn):
    def wrapper():
        print("Function name", fn.__name__)
        connect_to_database()
        fn()

    return wrapper()

# @h1
# @strong
# def get_customers():
#     print("fetch customers")
#     return ['Customer1', 'Customer2']

#get_customers_decorator = display_customers(open_connection(get_customers))

# @open_connection
# @display_customers
# def get_students():
#     print("fetch students")
#     return ['Student1', 'Student2']

#get_student_decorator = open_connection(display_customers(get_students))




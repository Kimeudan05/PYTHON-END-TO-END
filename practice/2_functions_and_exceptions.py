def my_name(name:str,age:int):
    print(f"my name is {name} and I am {age} yaers old")

# name = input("Enter name : ")
# age  =int(input("Enter age :"))
# my_name(name,age)
my_name("Jane",67)

# arbitrary arguements (*args) with return
def add_nums(*nums):
    total = 0
    for num in nums:
        total += num
    return total

print(f"The sum is {add_nums(67,54,345,234)}")

# arbitrary keyword arguements (**kwargs)
def dict_g(**kwargs):
    for key,value in kwargs.items():
        print(f"{key} => {value}")

dict_g(name ="jane",age =56,fr="2nd")

# default parameters
def seemore(country = "Kenya"):
    print(f"the best country for comedy is {country}")

seemore("India")
seemore()

# passing a list as an arguement
def my_likes(food:list):
    for i in food:
        print(f" {i}",sep=", ")
my_likes(["carrots","sukums","mukimo"])

def my_likes(food:list):
    if len(food):
        likes = ", ".join(food[:-1]) + " and " + food[-1]
    elif food:
        likes=food[0]
    else:
        likes = "nothing"
    print(f"I like {likes}.")
    
my_likes(["carrots","sukuma","mukimo","githeri"])

# keyword only arguements - must specify the keyword name
def func(*, name):
    print(f"My name is {name}")
func(name ="Masila")
# func("Masila") #- this produces an error

# position only
def func(name,/):
    print(f"My name is {name}")
# func(name ="Juma") # this produces an error
func("Juma")

## Recursion
def tri_recursion(k):
  if(k > 0):
    result = k + tri_recursion(k - 1)
    print(result)
  else:
    result = 0 #The recursion ends when the condition is not greater than 0 (i.e. when it is 0).
  return result

print("Recursion Example Results:")
tri_recursion(6)



############ DECORATORS ##########
#(Are functions that take another function as input and returns new function)
def change_case(func):
    def myinner():
        return func().upper()
    return myinner

@change_case
def myfunction():
    return "Hello Sally"
@change_case
def num():
    return "kaso"

print(myfunction())
print(num())

# multiple decorators
def changecase(func):
  def myinner():
    return func().upper()
  return myinner

def addgreeting(func):
  def myinner():
    return "Hello " + func() + " Have a good day!"
  return myinner

@changecase
@addgreeting
def myfunction():
  return "Tobias"

print(myfunction())
print(myfunction.__name__)



### LAMBDA ### (Anonymous function)
# lambda arguements : expression

print((lambda x :x+3)(6))
y = lambda a:a+10
print(y(5))

# Multiply argument a with argument b and return the result:
x = lambda a, b : a * b
print(x(5, 6))


# double a number
def myfunc(n):
  return lambda a : a * n
mydoubler = myfunc(2)
print(mydoubler(11))
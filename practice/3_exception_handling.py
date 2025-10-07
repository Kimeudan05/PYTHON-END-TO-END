# the try / except /else / finally block
try:
    print(x)
except NameError:
    print("Variable x is not defined")
except:
    print("Something else went wrong")
else:
    print("Nothing went wrong")
finally:
    print("you have finished the try/except")
    
#### Opem and write to a file
try:
    f= open("demo.txt")
    try:
        f.write("Lorem ipsum")
    except:
        print("Something went wrong when writing the file")
    finally:
        f.close()
except:
    print("sth went wrong opening the file")
    
##### raising exceptions
x = -1
if x <0:
    raise Exception("Sorry, number is below zero")

##
yj= "hello"
if not type(yj) is int: #if not isinstance(yj,int)
    raise TypeError("Only integers are allowed")

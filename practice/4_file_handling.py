with open("demo.txt",'w') as f: # use a  to just append
    f.write("You are awesome, in a new file\n")
    
# this overwrites the file 
with open('demo.txt','r+') as f:
    # print(f.read())
    f.write("Kasogo yeye\n")
    f.write("musa alinena naye mungu\n")
    f.writelines(["many are the days we went angry\n","we will always be remebered in the world\n"])
    f.seek(0) # go to the start of the file(move the pointer)
    print(f.read())
    
# By using the 'a+' -> we can append without overwriting it    
with open('demo.txt','r+') as f:
    # print(f.read())
    f.writelines(["many are the days we went angry\n","we will always be remebered in the world\n"])
    f.seek(0) # go to the start of the file(move the pointer)
    print(f.read())
    

####### CHEAT SHEET #######

# 1 . openinng and closing a file
f = open('demo.txt', 'w')  # open file for writing
f.write('Hello world!')
f.close()

# - for best practices use with
with open('demo.txt','w') as f:
    f.write("Hello kasongo")
# automatically closes the file
print(f.closed) # true

## 2 . File modes 
# | Mode   | Description                             |
# | ------ | --------------------------------------- |
# | `'r'`  | Read (default); error if file not found |
# | `'w'`  | Write; creates file or truncates        |
# | `'a'`  | Append; creates file or appends         |
# | `'r+'` | Read and Write                          |
# | `'a+'` | Append and Read                         |
# | `'w+'` | Write and Read (truncates file)         |
# | `'x'`  | Create and write; error if exists       |

# 3.  Read from files
# - Entire file
with open('demo.txt', 'r') as f:
    content = f.read()
    print(content)

# - Line by line
with open('demo.txt', 'r') as f:
    for line in f:
        print(line.strip())

# - specific number of characters

with open('demo.txt', 'r') as f:
    part = f.read(5) # the first 5 characters
    print(part)

# 4 . write to files
# - Overwrite the file
with open('demo.txt', 'w') as f:
    f.write("Overwriting the file\n")
# -append to the file
with open('demo.txt', 'a') as f:
    f.write("Adding another line\n")

# -write multiple lines
lines = ["First line\n", "Second line\n"]
with open('demo.txt', 'a') as f:
    f.writelines(lines)

# 5. Working with File Pointers
#-  f.seek(offset, whence)
# | Whence | Position         |
# | ------ | ---------------- |
# | `0`    | Start of file    |
# | `1`    | Current position |
# | `2`    | End of file      |

with open('demo.txt', 'r+') as f:
    f.seek(0, 2)  # Move to end
    f.write("Appending at end\n")
    f.seek(0)     # Back to start to read
    print(f.read())

# - f.tell() - get the current position
with open('demo.txt', 'r') as f:
    print(f.tell())  # Output: 0
    f.read(5)
    print(f.tell())  # Output: 5

## 6. Checking File Existence (Safe Handling)
import os
if os.path.exists('demo.txt'):
    with open('demo.txt') as f:
        print(f.read())
else:
    print("file not found")
    

# 7. Exception handling
try:
    with open("demo.txt") as f:
        print(f.read())
    
except FileNotFoundError:
    print("file not found")
except IOError:
    print("IO eror occured")
    

## 8 . Reading and writing  JSON
import json
data = {'name':'Alisce','age':10}

# write to json
with open('user.json','w') as f:
    json.dump(data,f,indent=4)
    
# diff btwn dump and dumps (dumps - converts to a string)
data = {'name': 'Alice', 'age': 25}
json_string = json.dumps(data)
print(json_string)  # {"name": "Alice", "age": 25}

# read from json
with open('user.json','r')as f:
    user  = json.load(f)
    print(user['name']) #alice
  
# loads - reads from a string  
json_data = '{"name": "Alice", "age": 25}'
user = json.loads(json_data)
print(user['age'])  # 25

### NB ###
import json

person = {"name": "John", "age": 30}

# --- dumps / loads (in-memory strings)
json_str = json.dumps(person)  # Python → JSON string
print(json_str)  # {"name": "John", "age": 30}

parsed = json.loads(json_str)  # JSON string → Python
print(parsed['name'])  # John

# --- dump / load (file I/O)
with open("person.json", "w") as f:
    json.dump(person, f)  # Save to file

with open("person.json", "r") as f:
    person_from_file = json.load(f)
print(person_from_file['age'])  # 30


## 9  working with csv
import csv
# writing
with open('people.csv','w',newline='',encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(['name',"age"]) 
    writer.writerow(['john',24])
    
# reading
with open("people.csv",'r') as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)
     
# working with file paths
from pathlib import Path

file =  Path('demo.txt')

if file.exists():
    print("file is available")
else:
    print("not found")
    
    

## 10 : REAL WORLD TO DO LIST APP
import json
import os
FILENAME = 'tasks.json'

def load_tasks():
    if not os.path.exists(FILENAME):
        return[]
    with open(FILENAME,'r') as f:
        return json.load(f)
    
def save_tasks(tasks):
    with open(FILENAME,'w') as f:
        json.dump(tasks,f,indent=2)

def view_tasks(tasks):
    if not tasks:
        print ("No tasks")
        return
    
    for task in tasks:
        print(f"{task['id']}: {task['title']} - {'Done' if task['done'] else 'Pending'}")

def add_task(tasks):
    title = input("task title : ")
    task_id = tasks[-1]['id'] +1 if tasks else 1
    tasks.append({'id':task_id,'title':title,'done':False})
    save_tasks(tasks)
    print('task added')
    
def mark_done(tasks):
    task_id = int(input("enter task id to mark done :"))
    for task in tasks:
        if task['id'] == task_id:
            task['done'] = True
            save_tasks(tasks)
            print("marked as done")
            return
    print("task not found")
    
def main():
    tasks = load_tasks()
    while True:
        print("\n1. View\n2. Add\n3. Mark Done\n4. Exit")
        choice = input("Choice: ")
        if choice == '1':
            view_tasks(tasks)
        elif choice == '2':
            add_task(tasks)
        elif choice == '3':
            mark_done(tasks)
        elif choice == '4':
            break
        else:
            print("Invalid choice")

main()
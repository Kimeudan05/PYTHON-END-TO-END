# a CLI todo list app (add, delete, mark as done,edit)
tasks =[
    {
        "id":1,
        "title":"visit the sick",
        "location":"Ruiru",
        "time":"today",
        "done": False
    },
    {
        "id":2,
        "title":"Go to fellowship",
        "location":"AIC Ruiru",
        "time":"tomorrow",
        "done": False
    },
    {   
        "id":3,
        "title":"Kazi bila kukoma",
        "location":"Makongeni",
        "time":"soon",
        "done": False
    },
]

# view all tasks
def view_task(todos):
    print(f"\n {"#"*10} MY TASKS {"#"*10}")
    if not todos:
        print("No tasks found")
        return
    for i, todo in enumerate(todos,1):
        print(f"\nTask {i}")
        print("-"*10) 
        print(f"id          :{todo['id']}")
        print(f"Title       :{todo['title']}")
        print(f"Location    :{todo['location']}")
        print(f"Time        :{todo['time']}")
        print(f"Completed   :{todo['done']}")
        print("-"*20)

# Add new tasks 
def add_task():
    # check id id exists before adding a task
    while True:
        try:
            id_set = {todo['id'] for todo in tasks} 
            id=int(input("enter id :"))
            if id in id_set:
                print("Id already exists (try another one :)")
                continue
            title = input("Enter task title : ")
            location = input("Enter task location : ")
            time = input("Enter task time   : ")    
            # declare a new task dictionary
            new_task = {
                "id":id,
                "title":title,
                "location":location,
                "time":time,
                "done":False
            }
            
            tasks.append(new_task)
            print("tasks added successifully")
            return
        except ValueError:
            print("please enter a valid number for ID")
            
# delete a task 
def delete_todo():
    try:
        id = int(input("Enter id of task to delete :"))
    except ValueError:
        print("Invalid input. please enter a number :")
        return
    for i, todo in enumerate(tasks):
        if todo['id'] == id:
            tasks.pop(i)
            print(f"Task deleted")
            return
    print("task not found")
            

# select and edit task by id
def edit_task():
    try:
        choice = int(input("Enter the id of the task to edit :"))
    except ValueError:
        print("Invalid input, enter a number ")
        return
    for todo in tasks:
        if todo['id'] == choice:
            print("The old values")
            print(f"Title         : {todo['title']}")
            print(f"Location      : {todo['location']}")
            print(f"Time          : {todo['time']}")
            print(f"Completed     : {todo['done']}")
            
            # declare new values for the task selected
            new_title = input("Enter new title :")
            new_location = input("Enter new location :")
            new_time = input("Enter new time :")
            completed_input = bool(input("Completed ? Select between (True and False)").strip().lower())
            if completed_input == "true":
                completed = True
            elif completed_input == "false":
                completed == False
            else:
                print("Invalid completion values . Use 'True' or 'False'")
                return
                
            todo.update({
                'title':new_title,
                'location':new_location,
                'time':new_time,
                'done':completed
            })
            print("task updated successifully")
            return
        
        print("task not available, try another task")

# mark as done 
def mark_done():
    try:
        task_id = int(input("enter id to mark as done :"))
    except ValueError:
        print("Please enter a valid number.")
        return
    for todo in tasks:
        if todo['id'] == task_id:
            todo['done'] = True
            print("Task marked as done :")
            return
    print("Task not found")
    
# then have a main function to run all these scripts
def main():
    while True:
        try:
            choice = int(input("Enter a choice to select an action :\n1 : view tasks\n2 : Add task\n3 : edit task\n4 : delete task\n5 : Mark as done\n6 : Exit\n choice : "))
        except ValueError:
            print("Invalid input. enter a number between 1 and 6.")
            continue
        if choice == 1:
            view_task(tasks)
        elif choice == 2:
            add_task()
        elif choice ==3:
            edit_task()
        elif choice == 4:
            delete_todo()
        elif choice == 5:
            mark_done()
        elif choice==6:
            print("Thank you for your time ")
            print("exiting...")
            exit()
        else:
            print("Invalid choice .Enter a number between 1 and 6")
main()

tasks=[]

print("Welcome to the TO Do List")
while True:
    try:
        choice=int(input("Enter number:\n 1.See list \n 2.Add task \n 3.Remove task \n"))
    except ValueError:
        print("Error: Enter valid number")

    if choice==1:
            print(tasks)
            
    elif choice==2:
            task=input("Add task: ")
            tasks.append(task)
            print("Added succesfully")

    elif choice==3:
            task=input("Remove task: ")
            try:
               tasks.remove(task)
            except Exception:
                  print("Task is not in list")
            print("Removed succefully")

    else:
            print("Enter correct choice")

    



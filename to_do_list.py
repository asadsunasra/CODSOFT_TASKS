print("=" * 50)
print("           TO-DO LIST APPLICATION")
print("=" * 50)

tasks = []

while True:

    print("\nChoose an Option")
    print("1. Add Task")
    print("2. View All Tasks")
    print("3. Update Task")
    print("4. Delete Task")
    print("5. Mark Task as Completed")
    print("6. View Completed Tasks")
    print("7. View Pending Tasks")
    print("8. Exit")

    choice = input("\nEnter your choice (1-8): ")

    # Add Task
    if choice == "1":

        task = input("Enter Task: ")

        tasks.append({
            "task": task,
            "completed": False
        })

        print("Task Added Successfully!")

    # View Tasks
    elif choice == "2":

        if len(tasks) == 0:
            print("No Tasks Available.")

        else:
            print("\n------ YOUR TASKS ------")

            for i, task in enumerate(tasks, start=1):

                status = "Completed" if task["completed"] else "Pending"

                print(f"{i}. {task['task']} [{status}]")

    # Update Task
    elif choice == "3":

        if len(tasks) == 0:
            print("No Tasks Available.")

        else:

            for i, task in enumerate(tasks, start=1):

                status = "Completed" if task["completed"] else "Pending"

                print(f"{i}. {task['task']} [{status}]")

            update = int(input("Enter Task Number to Update: "))

            if 1 <= update <= len(tasks):

                new_task = input("Enter New Task: ")

                tasks[update - 1]["task"] = new_task

                print("Task Updated Successfully!")

            else:

                print("Invalid Task Number.")

    # Delete Task
    elif choice == "4":

        if len(tasks) == 0:

            print("No Tasks Available.")

        else:

            for i, task in enumerate(tasks, start=1):

                status = "Completed" if task["completed"] else "Pending"

                print(f"{i}. {task['task']} [{status}]")

            delete = int(input("Enter Task Number to Delete: "))

            if 1 <= delete <= len(tasks):

                removed = tasks.pop(delete - 1)

                print(f"{removed['task']} Deleted Successfully!")

            else:

                print("Invalid Task Number.")

    # Mark Completed
    elif choice == "5":

        if len(tasks) == 0:

            print("No Tasks Available.")

        else:

            for i, task in enumerate(tasks, start=1):

                status = "Completed" if task["completed"] else "Pending"

                print(f"{i}. {task['task']} [{status}]")

            complete = int(input("Enter Task Number to Mark Completed: "))

            if 1 <= complete <= len(tasks):

                tasks[complete - 1]["completed"] = True

                print("Task Marked as Completed!")

            else:

                print("Invalid Task Number.")

    # View Completed
    elif choice == "6":

        found = False

        print("\nCompleted Tasks")

        for i, task in enumerate(tasks, start=1):

            if task["completed"]:

                print(f"{i}. {task['task']}")

                found = True

        if not found:

            print("No Completed Tasks.")

    # View Pending
    elif choice == "7":

        found = False

        print("\nPending Tasks")

        for i, task in enumerate(tasks, start=1):

            if not task["completed"]:

                print(f"{i}. {task['task']}")

                found = True

        if not found:

            print("No Pending Tasks.")

    # Exit
    elif choice == "8":

        print("\nThank You For Using To-Do List Application.")

        break

    else:

        print("Invalid Choice. Please Enter 1 to 8.")
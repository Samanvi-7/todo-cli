def for_help():
    print("\nOptions:")
    print("1. To add a todo, please type: 'add _your Task_' ")
    print("2. To delete a todo, please type: 'remove__your Task_number__' ")
    print("3. To show todo, please type: 'view'")
    print("4. To exit, please type: 'exit' ")

def add_task(todo_list,task_item):
    todo_list.append(task_item)
    print(f"\nTo_do '{task_item}' is added!")

def delete_task(todo_list, task_index):
    if 1 <= task_index <= len(todo_list):
        removed_task = todo_list.pop(task_index - 1)
        print(f"\nTodo '{removed_task}' deleted!")
    else:
        print("\nInvalid task number!")


def view_todo(todo_list):
    if todo_list:
        print("\nTo_do List:")
        for index,task in enumerate(todo_list,start=1):
            print(f"\n{index}.{task}")
    else:
        print("\nYour todo_list is empty!")

def main():
    todo_list=[]
    print("\nWelcome to To_do Application!!")
    while True:
        user_input=input(" > ").lower().strip()
        task_id=user_input.split(maxsplit=1)
        task_command=task_id[0]
        if task_command=="help":
            for_help()

        elif task_command == "add":
            if len(task_id) > 1:
                add_task(todo_list, task_id[1])
            else:
                print("\nPlease provide a task item to add.")
                
        elif task_command == "remove":
            if len(task_id) > 1 and task_id[1].isdigit():
                task_index = int(task_id[1])
                delete_task(todo_list, task_index)
            else:
                print("\nPlease provide a valid task number to delete.")
                
        elif task_command == "view":
            view_todo(todo_list)
                
            
        elif user_input == "exit":
            print("\nExiting the Todo Application!")
            break
        
        else:
            print("\nInvalid command. Type 'help' for options or 'exit' to quit.")

main()
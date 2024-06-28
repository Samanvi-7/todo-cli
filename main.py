from mydb import create_table, create_todo, delete_todo, get_all_todos
def for_help(): #displays all the available options
    print("\nOptions:")
    print("To add a todo, please type: add <Your Task> ")
    print("To delete a todo, please type: remove <Your Task_name> ")
    print("To show todo, please type: <view> ")
    print("To exit, please type: <exit> ")

def add_task(task_name):
   create_todo(task_name)


def delete_task(task_name):
    delete_todo(task_name)
'''
def view_todo():
    todos = get_all_todos()
    if todos:
        print("\nTo_do List:")
        for task_name in todos:
            print(f"\n{task_name}")
    else:
        print("\nYour todo_list is empty!")
        '''

def view_todo():
    todos = get_all_todos()
    if todos:
        print("\nTo_do List:")
        for index, task_name in enumerate(todos, start=1): 
            print(f"{index}",".",task_name[1],sep='')



def main():
    create_table()
    print("\nWelcome to To_do Application!!")
    while True:
        user_input=input(" > ").lower().strip()
        task_id=user_input.split(maxsplit=1)
        task_command=task_id[0]
        if task_command=="help":
            for_help()

        elif task_command == "add":
            if len(task_id) > 1:
                add_task(task_id[1])
                print(f"\nTo_do '{task_id[1]}' is added!")
            else:
                print("\nPlease provide a task item to add.")
                
        elif task_command == "remove":
                if len(task_id) < 2:
                    return
                delete_task(task_id[1])
                print(f"\nTodo {task_id[1]} deleted!")
        
                
        elif task_command == "view":
            view_todo()
                
            
        elif user_input == "exit":
            print("\nExiting the Todo Application!")
            break
        
        else:
            print("\nInvalid command. Type 'help' for options or 'exit' to quit.")

main()
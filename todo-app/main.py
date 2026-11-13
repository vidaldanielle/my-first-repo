from storage import load_tasks, save_tasks
from tasks import add_task, complete_task, delete_task, edit_task, get_pending

def show_tasks(tasks):
    for task in tasks:
        marker = "[x]" if task["done"] else "[ ]"
        print(f"{task['id']}. {marker} {task['title']}")

def main_menu():
    tasks = load_tasks()
    while True:
        print("\nMini Task Manager")
        print("1. Add Task")
        print("2. Complete Task")
        print("3. Show Tasks")
        print("4. Delete Task")
        print("5. Edit Task")
        print("6. Show Pending Tasks")
        print("7. Exit")

        choice = input("Pumili ng opsyon (1-7): ")

        if choice == "1":
            title = input("Ilagay ang pamagat ng task: ").strip()
            if not title.strip():
                print("Hindi puwedeng blangko ang pamagat.")
                continue
            add_task(tasks, title)
            save_tasks(tasks)
            print(f"Task '{title}' ay nadagdag.")
        elif choice == "2":
            try:
                task_id = int(input("Ilagay ang ID ng task na tapusin: "))
            except ValueError:
                print("Numero lang po ang ilagay.")
                continue
            if complete_task(tasks, task_id):
                save_tasks(tasks)
                print(f"Task ID {task_id} ay natapos na.")
            else:
                print(f"Walang task na may ID {task_id}.")
        elif choice == "3":
            def show_tasks(tasks):
                if not tasks:
                    print("Wala pang task.")
                    return
                for task in tasks:
                    marker = "[x]" if task["done"] else "[ ]"
                    print(f"{task['id']}. {marker} {task['title']}")
            show_tasks(tasks)
        elif choice == "4":
            try:
                task_id = int(input("Ilagay ang ID ng task na ide-delete: "))
            except ValueError:
                print("Numero lang po ang ilagay.")
                continue
            if delete_task(tasks, task_id):
                save_tasks(tasks)
                print(f"Task ID {task_id} ay nadelete na.")
            else:
                print(f"Walang task na may ID {task_id}.")
        elif choice == "5":
            try:
                task_id = int(input("Ilagay ang ID ng task na i-edit: "))
            except ValueError:
                print("Numero lang po ang ilagay.")
                continue
            new_title = input("Ilagay ang bagong pamagat ng task: ")
            if edit_task(tasks, task_id, new_title):
                save_tasks(tasks)
                print(f"Task ID {task_id} ay na-edit na.")
            else:
                print(f"Walang task na may ID {task_id}.")
        elif choice == "6":
            pending_tasks = get_pending(tasks)
            if pending_tasks:
                print("Hindi pa tapos na mga task:")
                show_tasks(pending_tasks)
            else:
                print("Walang hindi pa tapos na task.")
        elif choice == "7":
            print("Salamat sa paggamit ng Mini Task Manager!")
            break
        else:
            print("Maling opsyon. Subukan muli.")

if __name__ == "__main__":
    main_menu()
def add_task(tasks, title):
    if tasks:
        new_id = max(task["id"] for task in tasks) + 1
    else:
        new_id = 1
    tasks.append({"id": new_id, "title": title, "done": False})

def complete_task(tasks, task_id):
    for task in tasks:
        if task["id"] == task_id:
            task["done"] = True
            return True
    return False

def delete_task(tasks, task_id):
    for i, task in enumerate(tasks):
        if task["id"] == task_id:
            del tasks[i]
            return True
    return False

def edit_task(tasks, task_id, new_title):
    for task in tasks:
        if task["id"] == task_id:
            task["title"] = new_title
            return True
    return False

def get_pending(tasks):
    return [task for task in tasks if not task["done"]]

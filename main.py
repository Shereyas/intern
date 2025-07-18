from fastapi import FastAPI
from database import todos_tasks

api = FastAPI()


@api.get("/")
def index():
    return {"message": "hello world"}

@api.get("/todos/{todo_id}")
def get_todo(todo_id: int):
    for todo in todos_tasks:
        if todo['todo_id'] == todo_id:
            return todo

@api.get("/todos/{todo_name}")
def get_todo_by_name(todo_name: str):
    for todo in todos_tasks:
        if todo['todo_name'].lower() == todo_name.lower():
            return todo
    return {"message": "Todo not found"}

@api.post("/todos")
def create_todo(todo_name: str, todo_description: str):
    new_todo_id = len(todos_tasks) + 1
    new_todo = {
        'todo_id': new_todo_id,
        'todo_name': todo_name,
        'todo_description': todo_description
    }
    todos_tasks.append(new_todo)
    return {"message": "Todo created successfully", "todo_id": new_todo_id}

@api.put("/todos/{todo_id}")
def update_todo(todo_id: int, todo_name: str, todo_description: str):
    for todo in todos_tasks:
        if todo['todo_id'] == todo_id:
            todo['todo_name'] = todo_name
            todo['todo_description'] = todo_description
            return {"message": "Todo updated successfully"}

@api.delete("/todos/{todo_id}")
def delete_todo(todo_id: int): 
    for todo in todos_tasks:
        if todo['todo_id'] == todo_id:
            todos_tasks.remove(todo)
            return {"message": "Todo deleted successfully"}
import json
import sys
from pathlib import Path
import os
from datetime import datetime

STORAGE_PATH = Path("./.storage/storage.json")
STORAGE_PATH.parent.mkdir(parents=True, exist_ok=True)
if not STORAGE_PATH.exists() :
    with open("./.storage/storage.json", "w") as file :
        obj = {"tasks" : []}
        json.dump(obj, file, indent=4)

def get_new_id() :
    with open(STORAGE_PATH, "r") as file :
        try :
            obj = json.load(file)
            try :
                id = max([task["id"] for task in obj["tasks"]])+1
                return id
            except ValueError :
                return 1
        except json.JSONDecodeError:
            return 1



def store(title: str, priority: str, done: bool=False) :
    created_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    id = get_new_id()
    print(id)
    task = {
        "id" : id,
        "title": title,
        "priority": priority,
        "done": done,
        "created_at": created_date,
        "updated_at": created_date 
    }

    try :
        with open(STORAGE_PATH, "r") as file :
            obj = json.load(file)
            obj["tasks"].append(task)
            tasks = obj
    except json.JSONDecodeError :
        tasks = {
            "tasks" : [
                task
            ]
        }
    
    with open(STORAGE_PATH, "w") as file :
        json.dump(tasks, file, indent=4)
    
    return True



def delete(id: int) :
    try :
        with open(STORAGE_PATH, "r") as file :
            obj = json.load(file)
            tasks = [task for task in obj["tasks"] if task["id"] != id]
            id = 1
            for task in tasks :
                task["id"] = id
                id += 1
        
        with open(STORAGE_PATH, "w") as file :
            json.dump({"tasks": tasks}, file, indent=4)
            return True
    except json.JSONDecodeError :
        return False


def done(id: int) :
    updated_task = {}
    try :
        with open(STORAGE_PATH, "r") as file :
            obj = json.load(file)
            for task in obj["tasks"] :
                if task["id"] == id :
                    update_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    task["done"] = True
                    task["updated_at"] = update_date
                    updated_task = task
                    break
    except json.JSONDecodeError :
        return False
    
    if updated_task :
        with open(STORAGE_PATH, "w") as file :
            json.dump(obj, file, indent=4)
            return updated_task
    else : 
        return False

def get_tasks() :
    try :
        with open(STORAGE_PATH, "r") as file :
            tasks = json.load(file)
            return tasks["tasks"]
    except json.JSONDecodeError :
        tasks = []
        return tasks

def modify(id: int, title: str=None, priority:str=None) :
    updated_task = {}
    try :
        with open(STORAGE_PATH, "r") as file :
            obj = json.load(file)
            for task in obj["tasks"] :
                if task["id"] == id :
                    update_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    if title :
                        task["title"] = title
                    if priority :
                        task["priority"] = priority
                    task["updated_at"] = update_date
                    updated_task = task
                    break
    except json.JSONDecodeError :
        return False
    
    if updated_task :
        with open(STORAGE_PATH, "w") as file :
            json.dump(obj, file, indent=4)
            return updated_task
    else : 
        return False

get_tasks()


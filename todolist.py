import os.path
import json
import datetime
now = datetime.datetime.now()

"""
ToDoList
[v] 정렬이 안돼서 원하는 항목을 done 할 수 없음 
[ ] Index is changed to Id
"""

def init():
    year = now.strftime("%Y-%y")
    month = now.strftime("%M-%m")
    day = now.strftime("%D-%d")
    date = now.strftime("%y%m%d")

    try:
        msg = load_data(date)
    except:
        msg = "Nothing"
    
    # print ToDoList
    print(msg)

    menu = int(input("1)Add 2)Done 3) Finish\n")) 
    
    if menu == 1:
        input_todo = input("Input task\n")
        add_todo(date, input_todo)
    elif menu == 2:
        input_todo = input("Input task number\n")
        done_todo(date, input_todo)
    elif menu == 3:
        return

def done_todo(date, todo_id):
    file_nm = "todolist{}.json".format(date)

    with open(file_nm) as f:
        json_data = json.load(f)

    with open(file_nm, "w") as f:
        
        for i in range(len(json_data)):
            data = json_data[i]
            if i == int(todo_id):
                json_data[i]['is_done'] = True
                break
        json.dump(json_data, f)
        f.close()
        init()


def add_todo(date, todo):
    file_nm = "todolist{}.json".format(date)

    with open(file_nm) as f:
        json_data = json.load(f)


    with open(file_nm, "w") as f:
        json_data.append({
            "id": 13,
            "date": date,
            "todo": todo,
            "is_done": False 
            })
        json.dump(json_data, f, indent=4)
        f.close()
        init()
    
def load_data(date):
    file_nm = "todolist{}.json".format(date)
    if os.path.isfile(file_nm) == False:
        f = open(file_nm, "a")
        f.write("[\n]")
        f.close()

    with open(file_nm) as f:
        todo_json = json.load(f)

    msg = "오늘의 할 일!\n"
    todolist = []
    for todo in todo_json:
        if todo['is_done'] == True:
            todolist.append("\033[95m"+"["+"\033[32m"+"v"+"\033[95m"+"]"+"\033[0m"+" {}\n".format(todo['todo']))
        else:
            todolist.insert(0, "\033[95m"+"[ ]"+"\033[0m"+" {}\n".format(todo['todo']))
        
    for todo in todolist:
        msg = msg + todo

    return msg 

def todolist201126():
    return load_data()

def todolist201125():
    
    #json_file = open("todolist.json", "r")
    #json_data = json.load(json_file)
    #json_data['testObject2'] = {'obj1': 1}

    with open("todolist.json") as f:
        json_data = json.load(f)
    
    #with open("todolist.json", "w") as f:
    #    json_data['obj3'] = 3
    #    json.dump(json_data, f)

    #print(json_data)


    #json_file.close()
    



    #with open('todolist.json') as f:
    #    data = json.load(f)

    #print(data['testObject'])
    todolist = """

    """


    return todolist 

#
init()

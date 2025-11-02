import json
import random

###making file for importing data for password
file_data =( [chr(i)for i in range(97,123)]+  ###a-z
             [chr(i)for i in range(65,91)]+ ###A-Z
             [str(i)for i in range(1,20)] #### 1..20

)

########making and appending data to json file
with open("pass_store.json", "w") as pass_wd:
    json.dump(file_data,pass_wd)

##########making json file to store the web name and passwd
# open_file = open("pass_store.json", "r")
# list_data = json.load(open_file)
#
# user_data = input("enter your web name : ")
# user_web = input("enter your web url : ")
# user_pass = random.sample(list_data,8)

#############user infor stored

#
def user_add():
    open_file = open("pass_store.json", "r")
    list_data = json.load(open_file)

    user_data = input("enter your web name : ").lower()
    user_web = input("enter your web url : ").lower()
    user_pass = random.sample(list_data, 8)
    dict_data = {
        user_data: {
            "web_add": user_web,
            "use_pass": ("".join(user_pass))
        }
    }
    try:
        with open("store_data.json", "r") as file:
            data_file = json.load(file)
            data_file.update(dict_data)

    except:
        with open("store_data.json", "w") as mk_file:
            mk_file_data = json.dump(dict_data, mk_file, indent=4)
    else:
        with open("store_data.json", "w") as data_stored:
            json.dump(data_file,data_stored, indent=4)

    # finally:  ## just to check data
    #     with open("store_data.json" , "r") as reader:
    #         json_reader = json.load(reader)
    #         print(json_reader)

def search_data():
    try:
        with open("store_data.json" , "r") as file:
            find_data = json.load(file)

        web_search = input("enter your web name : ").lower()
        if web_search in find_data:
            print(f"your web add : {find_data[web_search]["web_add"]} \n your password is : {find_data[web_search]["use_pass"]}")
        else:
            print("no details found")
    except:
        print("no data found , first add user")

ask_user = input("what you want add or search : ").lower()

if ask_user =="add":
    user_add()
elif ask_user =="search":
    search_data()

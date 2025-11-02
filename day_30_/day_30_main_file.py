##here we will be learning reding and writing to jesion filea dn saving
##nad error hendeling

# with open("a_file.txt") as files:
#     files.read()

## keyError , with dictionary when key not exist

#IndexError , geting errir with list when someting not exist in list
#TypeError , when string and int are added

#############################################
##Error hendling
#try
#except
#else
#finally

###
##try --> executing the code
##except --> if try not work
##else -->if code not failed then continue from try to else
##finally --> continue no matter whether previous code work or not

##########
##solving file not find error,
##situation is that file not exist but we are trying to open it
# try:
#     file=open("a_file.txt")
# except:  ## with this exception we will dirctly execute the exception if in try block there is any type of error
#     # print("file not found") ## this will print that file not found
#     open("a_file.txt","w") ## using this it will create a file
#     file.write("hellow this is ")
################
######raiting execption for particular type of error
try:
    file=open("a_file.txt","r") ### if this is exist
    my_dic={"key":"value","files": "appear"}
    my_dic["file"]="delhi"

    print(my_dic["file"])  ## this is not exist
    print(my_dic["files"])
except FileNotFoundError: ## here we are pointing particular error file not found appaer when file not exist
    file=open("a_file.txt", "w")
    file.write("somethong")
# except KeyError: ## pointing only key error
#     print("key not found try again")
########## or
# ## we can print the error msg
# except KeyError as error_message:
#     print(f"the key error :{error_message}")
# else: ### this will only execute when there was no exception
#     cont = file.read()
#     print(cont)
#
# finally: ## this will always execute irrespective of all here appear before
#     file.close()
#     print("file is closed")

######################
##generate your own coading exceptions , video 229
##raise --> this allow us to raise  our own exceptions
# try:
#     file = open("a_file.txt", "r")
#     content = file.read()
#     print(content)
# except FileNotFoundError:
#     file = open("a_file.txt", "w")
#     file.write("something")
#     print("File not found, created a new one with default content.")
# else:
#     print("every thing is good to go")
# finally:
#     raise KeyError("this is error i made")  ## we will raise this error although everything is correct, this will crash the code
# ### we can raise any error through raise eg typeError etc

########################
# ######why need error --> to handle the wrong inputs
# height= float(input("enter your height in cm:"))
# weight = float(input("enter your waight in kg"))
#
# if height > 190:
#     raise("human can not be this much big")
# bmi = round(weight / height**2,2)
# print(f"your bmi is :{bmi}")

###############video 230

dect = {
    "label": {"user":"hello",
              "pass": "password"}
}

inputs_take = input("enetry : ").lower()
if inputs_take in dect:
    print(inputs_take)
else:
    print("not found")

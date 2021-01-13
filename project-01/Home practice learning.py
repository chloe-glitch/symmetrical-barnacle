def celeb():
    the_data=input("Excellent!\n"
        "Please enter your name, celebrity name and his occupation to give a full string!: ")
    name="chloe"
    the_info=the_data.split(" ")
    celebrity_firstname=the_info[1]
    celebrity_lastname=the_info[2]
    occupation="sings"
    
    name=the_info[0]
    celebrity_name=celebrity_firstname+" "+celebrity_lastname
    occupation=the_info[3]
    print("Hi, my name is {}, {} is my favourite musician, he {}.".format(name.title(),celebrity_name.title(),occupation))
def addition():
    teml=input("Enter list of numbers here: ")
    tem=teml.split(" ")
    templ=[]
    for i in tem:
        i=int(i)
        i+=70
        templ.append(i)
    print(templ)
def multipl():
    get_input=int(input("Enter input here: "))
    if get_input%5==0 and get_input%20==0:
        print("{} is a multiple of 5 and 20.".format(get_input))
    elif get_input%5==0:
        print("{} is a multiple of 5.".format(get_input))
    elif get_input%20==0:
        print("{} is a multiple of 20.".format(get_input))
    else:
        print("It is not a multiple of 5, 20 or both.")
def numbering():
    grocery_list=input("Enter list here!: ")
    the2=grocery_list.split(" ")
    iterator=1
    for item in the2:
        print(iterator,item)
        iterator+=1
def dictionaryy():
    get_data=input("Enter list to convert to dictionary here: ")
    to_split=get_data.split(" ")
    temp={}
    ori_length=len(list(to_split))
    needed_len=int(ori_length/2)
    if ori_length%2!=0:
        second_data=input("Do you want to insert value for key {}: ".format(to_split.index(-1)))
        if second_data=="Yes":
            the_value=input("Enter value for the last key: ")
            to_split.append(the_value)
        else: 
            to_split.remove[-1]
        
    counter=0
    for item in range(needed_len):
        new_key=to_split[counter]
        new_value=to_split[counter+1]
        if new_value.isnumeric==True:
            new_value=int(new_value)
        else:
            pass
            
        temp.update({new_key:new_value}) 

        counter+=2 

        print(temp)
def sec_highest():
    new_data = input("Enter details here: ")
    Names_data = new_data.split(" ")

    for index, item in enumerate(Names_data):
        if item.isnumeric() == True:
            Names_data[index] = int(Names_data[index])
        else:
            pass

    scores_only = Names_data[1: len(Names_data): 2]

    scores_as_set = set(scores_only)

    unique_scores = list(scores_as_set)

    unique_scores.sort()

    desired_score = unique_scores[-2]

    required_index = []

    for index, entry in enumerate(Names_data):
        if entry == desired_score:
            required_index.append(index -1)
        else:
            pass

    list_of_names = []
    for num in required_index:
        desired_name = Names_data[num]
        list_of_names.append(desired_name)

    list_of_names.sort()
    if len(list_of_names) == 1:
        print("The student with the second highest score {}".format(list_of_names[0]))

    else:
        print("The student with the second highest score are: ")
        for name in list_of_names:
            print(name)
def substring():
    Goku = str(input("Enter parent string here: "))
    Madara = str(input("Enter sub string here: "))

    par_len = len(Goku)
    sub_len = len(Madara)
    counter = 0
    for char in range(par_len):
        chunk = Goku[char:sub_len + char]
        if chunk == Madara:
            counter += 1
        else:
            pass
    print("The number of sub strings in parent string is {}".format(counter))

from datetime import datetime
now=datetime.now()
print("Hello!Today's date is {}-{}-{}".format(now.day,now.month,now.year))
user_name=input("Enter your name here: ")
print("Welcome {}!".format(user_name.title()))
def menu():
    print("What problem would you like me to solve today?\n"
    "Input 1 to access quiz 1-celebrity name quiz\n"
    "Input 2 to access quiz 2-add 70 to each item in a list\n"
    "Input 3 to access quiz 3-to find out if a number is a multiple of 5, 20 or both.\n"
    "Input 4 to access quiz 4-to number a list from 1 instead of 0\n"
    "Input 5 to access quiz 5-to convert a list to a dictionary\n"
    "Input 6 to access quiz 6- to get ther name with the second highest number\n"
    "Input 7 to access quiz 7- to get the number of substrings in a parent string\n"
    "Input 0 to exit the code.")

    first_input=int(input("Enter option here: "))
    if first_input==1:
        celeb()
        menu()
    elif first_input==2:
        addition()
        menu()
    elif first_input==3:
        multipl()
        menu() 
    elif first_input==4:
        numbering()
        menu()
    elif first_input==5:
        dictionaryy()
        menu()
    elif first_input==6:
        sec_highest()
        menu()
    elif first_input==7:
        substring()
        menu()
    elif first_input==0:
        print("Thanks for using my project, {}\n"
            "Goodbye!".format(user_name.title()))
    else:
        print("This is invalid")
        menu()
menu()

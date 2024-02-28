# Dokumentācija
# Mainīgie - https://www.w3schools.com/python/python_variables.asp
# Operācijas ar mainīgiem - https://www.w3schools.com/python/python_operators.asp
# Mainīgo drukāšana - https://www.w3schools.com/python/python_variables_output.asp
# Nosacījumi, zarošana, if ... else - https://www.w3schools.com/python/python_conditions.asp
# For cikls - https://www.w3schools.com/python/python_for_loops.asp
# Nejauša skaitļa generēšana - https://www.w3schools.com/python/ref_random_randint.asp
# Github Fork (repozitorija kopija) - https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/working-with-forks/fork-a-repo
# Saraksti - https://www.w3schools.com/python/python_lists.asp
# Vārdnīcas - https://www.w3schools.com/python/python_dictionaries.asp
# Klonēt repozitoriju - hhttps://code.visualstudio.com/docs/sourcecontrol/intro-to-git

import json


with open("watchlist.json",'r') as file:
    all_films = json.load(file)

def save():
    with open("watchlist.json", "w") as otherfile:
        json.dump(all_films, otherfile)

def sort(film):
    return film["name"]

def sort_rating(film):
    return int(film["rating"])


while True:  #loop thats stopped only on exit
    print('''
    1-pievienot filmu
    2-dzēst filmu
    3-atzīmēt filmu kā skatīto
    4-atfiltrēt noskatītas filmas
    5-atfiltrēt nenoskatītas filmas
    6-atspoguļot top 10 filmas pec reitinga
    7-iztukšot sarakstu
    8-meklēt filmu
    9-Exit
''')
    select = input("Select function: ")
    if select == '1':  #add film
        film = ''
        rating = 0
        while len(film) <2 or len(film) >120:  #Wait until user inputs correct info
            	film = input("Film name: ")
        while rating <1 or rating >10: #Wait until user inputs correct info
            rating = int(input("Rating(1-10): "))
            index = len(all_films)
        new_film = {"name" : film, "rating" : rating, "watched" : "no"}
        all_films.append(new_film)
        save()
    if select == '2':  #remove film
        film = input("Film name to delete: ").lower()
        for i in all_films:     #go over each element 
            if i['name'].lower() == film:   #check if input matches current elements name
                all_films.remove(i)
        save()
    if select == '3':  #mark film as watched
        film = input("Film name: ").lower()
        index = 0
        for i in all_films: #go over each element 
            if i['name'].lower() == film:   #check if input matches current elements name
                all_films[index]['watched'] = "yes"
            index += 1
        save()
    if select == '4':  #sort watched films
        watched_films = []
        for i in all_films:   #go over each element 
            if i['watched'] == 'yes':    #check if it has been watched
                watched_films.append(i)
        watched_films.sort(key = sort)
        for i in range(10):   #only print the top 10 elements 
            try:
                print("-------------------")
                print("Name:", watched_films[i]["name"])
                print("Rating:", watched_films[i]["rating"])
            except:
                break
    if select == '5':  #sort unwatched films
        unwatched_films = []
        for i in all_films: #go over each element 
            if i['watched'] == 'no':    #check if it hasnt been watched
                unwatched_films.append(i)
        unwatched_films.sort(key = sort)
        for i in range(10): #only print the top 10 elements 
            try:
                print("-------------------")
                print("Name:", unwatched_films[i]["name"])
                print("Rating:", unwatched_films[i]["rating"])
            except:
                break
    if select == '6':  #sort by rating
        all_films.sort(key = sort_rating, reverse=True)
        for i in range(10): #only print the top 10 elements 
            try:
                print("-------------------")
                print("Name:", all_films[i]["name"])
                print("Rating:", all_films[i]["rating"])
            except:
                break
    if select == '7':  #celear the whole list
        confirmation = input("you sure tho?(y/n) ")
        if confirmation == 'y': #just confirming the users decicion 
            all_films = []
        save()
    if select == '8':  #search for film by name
        search = input("Film name: ").lower()
        for i in all_films:  #go over each element 
            if search in i['name'].lower():    #check if search is in films name
                print("-------------------")
                print("Name:", i["name"])
                print("Rating:", i["rating"])
    if select == '9':  #exiting
        save()
        break

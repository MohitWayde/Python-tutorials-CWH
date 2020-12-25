def search_engine_lite(query):
    db = [
        "python is not python snake",
        "python is very good",
        "python is trending programming language"]
    for i in db:
        if i.lower() in db:
            print(i)

    





print("!WELCOME TO THE SEARCH ENGINE LITE!")
search_query = input("Search Here !")
search_engine_lite(search_query)
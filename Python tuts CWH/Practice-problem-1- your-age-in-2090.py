current_year = 2020
user_input = int(input("enter age or year"))
partic = input("do you want to know your age at particular year! yes or no? :")

if partic.lower() == 'yes':
    par_age = int(input("Enter the year for which you want your age :"))
    if user_input>=1 and user_input<=125:
        print("age")
        cal = current_year - user_input 
        calc = par_age - cal
        print(f"In {par_age}, You'll be {calc} years old")
        
    elif user_input>=1900 and user_input<=current_year:
        print("year")
        calc = par_age - user_input
        print(f"In {par_age}, You'll be {calc} years old")
        
    else:
        print("You are not yet borned or your are the most oldest person in the world!")
    
    
else:
    if user_input>=1 and user_input<=125:
        print("age")
        cal = current_year - user_input
        calc = cal+100
        print(f"You'll be 100 years old in the {calc} year")


    elif user_input>=1900 and user_input<=current_year:
        print("year")
        calc = user_input + 100
        print(f"You'll be 100 years old in the {calc} year")


    else:
        print("You are not yet borned or your are the most oldest person in the world!")
print("*************** Welcome to event manager ***************")
print("1.birthday\n2.wedding\n3.college event\n4.traditional events\n5.sports\n6.custom")
eno=int(input("please select event number: \n"))
dd = str(input("enter the day of event: \n"))
mm = str(input("enter the month of event: \n"))
yy = str(input("enter the year of event: \n"))
print("date of event in dd-mm-yyyy format is: ",dd,"-",mm,"-",yy)
if(eno==1):
    print("********** Welcome to the Birthday page **********\n")

    age = int(input("age: "))
    if (age < 10):
        print("Themes: ")
        print("1. car\n 2. princess\n 3. cartoon\n 4.sports\n5.custom theme")
        theme = int(input("Enter your theme: \n"))
        if (theme == 1):
            print("***** CAR THEME *****\n")
            cak = print("Birthday cake car\n")
            bno = int(input("number of balloons you required:\n "))
            hno = int(input("number of hats you required: \n"))
            gno = int(input("number of people to attending: \n"))
            cat = str(input("enter your catering service name:\n "))
            loc = str(input("enter your venue name: \n"))
            vnu = int(input("Enter the venue service number: \n"))
        elif (theme == 2):
            print("***** PRINCESS THEME *****\n")
            cak = print("Birthday cake princess\n")
            bno = int(input("number of balloons you required:\n "))
            hno = int(input("number of hats you required: \n"))
            gno = int(input("number of people to attending: \n"))
            cat = str(input("enter your catering service name: \n"))
            no = int(input("Enter the catering service number: \n"))
            loc = str(input("enter your venue name: \n"))
            vnu = int(input("Enter the venue service number:\n "))
        elif (theme == 3):
            print("***** CARTOON THEME ******\n")
            cn = str(input("Please enter the cartoon name:\n "))
            cak = print("Birthday cake of\n",cn)
            bno = int(input("number of balloons you required:\n"))
            hno = int(input("number of hats you required:\n "))
            gno = int(input("number of people to attending:\n "))
            cat = str(input("enter your catering service name:\n"))
            no = int(input("Enter the catering service number:\n"))
            loc = str(input("enter your venue name:\n"))
            vnu = int(input("Enter the venue service number:\n"))
        elif (theme == 4):
            print("***** SPORTS THEME *****\n")
            sn = str(input("Please enter the sport name:\n"))
            cak = print("Birthday cake of\n", sn)
            bno = int(input("number of balloons you required:\n"))
            hno = int(input("number of hats you required:\n"))
            gno = int(input("number of people to attending:\n"))
            cat = str(input("enter your catering service name:\n"))
            no=int(input("enter catering service number:\n"))
            loc = str(input("enter your venue name:\n"))
            vnu = int(input("Enter the venue service number:\n"))
        elif (theme == 5):
            print("***** CUSTOM THEME *****\n")
            cak = str(input("Please enter cake you would want:\n"))
            bno = int(input("number of balloons you required:\n"))
            hno = int(input("number of hats you required:\n"))
            gno = int(input("number of people to attending:\n"))
            cat = str(input("enter your catering service name:\n"))
            no = int(input("Enter the catering service number: \n"))
            loc = str(input("enter your venue name: \n"))
            vnu = int(input("Enter the venue service number:\n"))
    elif (age < 18 and age > 10):
        print("1.Gaming\n 2.Sports\n 3.Fiction\n 4.Party\n 5.custom\n")
        theme = int(input("Theme:\n"))
        if (theme == 1):
            print("***** GAMING THEME ******\n")
            sn = str(input("Please enter the Game name:\n"))
            print("Birthday cake of\n", sn)
            gno = int(input("number of people to attending:\n"))
            loc = str(input("enter your venue name:\n"))
            vnu = int(input("Enter the venue service number:\n"))
            cat = str(input("enter your catering service name:\n"))
            can = int(input("enter catering service number:\n"))
            con = int(input("What consoles or pc games needed:\n"))
            cont= int(input("How many controllers needed?\n"))
        elif (theme == 2):
            print("***** SPORTS THEME *****\n")
            sn = str(input("Please enter the sport name:\n"))
            print("Birthday cake of\n", sn)
            gno = int(input("number of people to attending:\n"))
            loc = str(input("enter your venue name:\n"))
            vnu = int(input("Enter the venue service number:\n"))
        elif (theme == 3):
            print("***** FICTION THEME *****\n")
            sn = str(input("Enter the Fictional universe name like MCU or DC:\n"))
            print("Birthday cake of\n", sn)
            gno = int(input("number of people to attending:\n"))
            loc = str(input("enter your venue name:\n"))
            vnu = int(input("Enter the venue service number:\n"))
            fun = str(input("enter some games or entertainment to provide:\n"))
        elif (theme == 4):
            print("****** PARTY THEME *****\n")
            cak = str(input("enter the birthday cake design:\n"))
            gno = int(input("number of people to attending:\n"))
            loc = str(input("enter your venue name:\n"))
            vnu = int(input("Enter the venue service number:\n"))
            cat = str(input("enter your catering service name:\n"))
            can = int(input("enter catering service number:\n"))
        elif (theme == 5):
            print("***** CUSTOM THEME ******\n")
            the = str(input("Enter the theme of the birthday:\n"))
            cak = str(input("enter the birthday cake design:\n"))
            gno = int(input("number of people to attending:\n"))
            loc = str(input("enter your venue name:\n"))
            vnu = int(input("Enter the venue service number:\n"))
            cat = str(input("enter your catering service name:\n"))
            can = int(input("enter catering service number:\n"))
            fun = str(input("enter some games or entertainment to provide:\n"))
    elif(age>18):
        print("1.casual\n 2.Sports\n 3.open\n 4.Party\n 5.custom\n")
        theme = int(input("Theme:\n"))
        if(theme == 1):
            print("***** CASUAL THEME AKA THE 90'S ******\n")
            gno = int(input("number of people to attending:\n"))
            loc = str(input("enter your venue name:\n"))
            vnu = int(input("Enter the venue service number:\n"))
            cat = str(input("enter your catering service name:\n"))
            can = int(input("enter catering service number:\n"))
        elif(theme == 2):
            print("***** SPORTS THEME ******\n")
            sn = str(input("Please enter the sport name:\n"))
            print("Birthday cake of\n", sn)
            gno = int(input("number of people to attending:\n"))
            loc = str(input("enter your venue name:\n"))
            vnu = int(input("Enter the venue service number:\n"))
        elif(theme == 3):
            print("***** OPEN THEME ******\n")
            loc = str(input("Enter the open area location:\n"))
            gno = int(input("number of people to attending:\n"))
            cat = str(input("enter the catering service name:\n"))
            catn = int(input("enter the catering service number:\n"))
            fun = str(input("enter some games or entertainment to provide:\n"))
        elif(theme == 4):
            print("***** PARTY THEME ******\n")
            loc = str(input("enter the club or restobars name:\n"))
            gno = int(input("number of people to attending: \n"))
            dj = str(input("enter the name of the dj artist you want for a performance: \n"))
            fun = str(input("enter some games or entertainment to provide: \n"))
        elif(theme == 5):
            print("****** CUSTOM THEME ******\n")
            the = str(input("Enter the theme of the birthday:\n"))
            cak = str(input("enter the birthday cake design: \n"))
            gno = int(input("number of people to attending: \n"))
            loc = str(input("enter your venue name: \n"))
            vnu = int(input("Enter the venue service number: \n"))
            cat = str(input("enter your catering service name: \n"))
            catn = int(input("enter catering service number: \n"))
            fun = str(input("enter some games or entertainment to provide: \n"))
    else:
        print("Invalid input\n")


elif(eno==2):
    print("********** Welcome to the Wedding page **********\n")
    print("1.traditional\n 2.mordern\n")
    typ = int(input("Enter the type of  wedding: \n"))
    if (typ == 1):
        print("1.Hindu\n 2.christian\n 3.muslim\n 4.other\n")
        rel = int(input("Enter religion:\n "))
        if (rel == 1):
            print("1.Party hall\n 2.conventional hall\n 3.Temple\n")
            loc = int(input("Enter the location:\n "))
            if (loc == 1):
                no = int(input("Enter the number of people to attending: \n"))
                cat = str(input("Enter the name of the catering company: \n"))
                catn = int(input("enter the number of the catering company: \n"))
                pho = str(input("enter the photographer name:\n "))
                phon = int(input("enter the number of the photographer: \n"))
            elif (loc == 2):
                no = int(input("Enter the number of people to attending: \n"))
                cat = str(input("Enter the name of the catering company: \n"))
                catn = int(input("enter the number of the catering company: \n"))
                pho = str(input("enter the photographer name: \n"))
                phon = int(input("enter the number of the photographer: \n"))
            elif (loc == 3):
                no = int(input("Enter the number of people to attending: \n"))
                cat = str(input("Enter the name of the catering company: \n"))
                catn = int(input("enter the number of the catering company: \n"))
                pho = str(input("enter the photographer name: \n"))
                phon = int(input("enter the number of the photographer: \n"))

        elif (rel == 2):
            print("1.Party hall\n 2.conventional hall\n 3.church\n")
            loc = int(input("Enter the location: \n"))
            if (loc == 1):
                no = int(input("Enter the number of people to attending: \n"))
                cat = str(input("Enter the name of the catering company: \n"))
                catn = int(input("enter the number of the catering company: \n"))
                pho = str(input("enter the photographer name: \n"))
                phon = int(input("enter the number of the photographer: \n"))
            elif (loc == 2):
                no = int(input("Enter the number of people to attending: \n"))
                cat = str(input("Enter the name of the catering company: \n"))
                catn = int(input("enter the number of the catering company: \n"))
                pho = str(input("enter the photographer name: \n"))
                phon = int(input("enter the number of the photographer: \n"))
            elif (loc == 3):
                no = int(input("Enter the number of people to attending: \n"))
                cat = str(input("Enter the name of the catering company: \n"))
                catn = int(input("enter the number of the catering company: \n"))
                pho = str(input("enter the photographer name: \n"))
                phon = int(input("enter the number of the photographer: \n"))

        elif (rel == 3):
            print("1.Party hall\n 2.conventional hall\n 3.mosque\n")
            loc = int(input("Enter the location: \n"))
            if (loc == 1):
                no = int(input("Enter the number of people to attending: \n"))
                cat = str(input("Enter the name of the catering company: \n"))
                catn = int(input("enter the number of the catering company: \n"))
                pho = str(input("enter the photographer name: \n"))
                phon = int(input("enter the number of the photographer: \n"))
            elif (loc == 2):
                no = int(input("Enter the number of people to attending: \n"))
                cat = str(input("Enter the name of the catering company: \n"))
                catn = int(input("enter the number of the catering company: \n"))
                pho = str(input("enter the photographer name: \n"))
                phon = int(input("enter the number of the photographer: \n"))
            elif (loc == 3):
                no = int(input("Enter the number of people to attending: \n"))
                cat = str(input("Enter the name of the catering company: \n"))
                catn = int(input("enter the number of the catering company: \n"))
                pho = str(input("enter the photographer name: \n"))
                phon = int(input("enter the number of the photographer: \n"))

    elif (typ == 2):
        loc = str(input("Enter the venue name for the wedding: \n"))
        dt = int(input("enter the date and time of the wedding\n"))
        no = int(input("Enter the number of people to attending:\n "))
        cat = str(input("Enter the name of the catering company: \n"))
        catn = int(input("enter the number of the catering company:\n "))
        pho = str(input("enter the photographer name: \n"))
        phon = int(input("enter the number of the photographer: \n"))

    else:
        print("Invalid input\n")
elif(eno==3):
    print("********** Welcome to the college events page **********\n")
    clg = str(input("Enter the college name: \n"))
    eve = str(input("enter the event name and details: \n"))
    spe = str(input("enter the speaker name: \n"))
    sta = str(input("Enter the food and games stalls to be present: \n"))
    foo = int(input("enter the number of food stalls to be placed: \n"))
    gam = int(input("enter the number of game stalls to be present: \n"))
    dj = str(input("enter the name of the dj artist you want for a performance: \n"))

elif(eno==4):
    print("********** Welcome to the traditional events page **********\n")
    eve = str(input("enter the event name and details: \n"))
    gno = int(input("Enter the number of people to attending: \n"))
    cat = str(input("Enter the name of the catering company: \n"))
    catn = int(input("enter the number of the catering company: \n"))
    ent = str(input("do you want there to be entertainment in the form of music or dance etc.(yes or no): \n"))
    if(ent == "yes"):
        ente = str(input("Enter the entertainment needed: \n"))
    else:
        print("Thank you for your response:\n")

elif(eno==5):
    print("********** Welcome to the sports events page **********\n")
    gno = int(input("Enter the number of people to attending: \n"))
    spe = str(input("enter the speaker name: \n"))
    spo = str(input("enter the sport/sports you want to play: \n"))
    loc = str(input("enter the location of the ground/court: \n"))
    foo = str(input("would you like food at the court(yes or no): \n"))
    if(foo == "yes"):
        food = str(input("enter the restaraunt name: \n"))
    else:
        print("Thank you for your response:\n")
    bol = str(input("do you want the ball to be provided?(yes or no):\n "))
    if(bol == "yes"):
        bal = int(input("enter the  number of balls: \n"))
    else:
        print("you can pay for a ball at the venue:\n")
    

elif(eno == 6):
    print("********** Welcome to the custom events page **********\n")
    event = str(input("enter the name of your event: \n"))
    theme = str(input("enter the theme of your event: \n"))
    gno = int(input("enter the number of people attending:\n "))
    ent = str(input("do you need any entertainment for the event?(yes or no): \n"))
    if(ent == "yes"):
        ente = str(input("enter the entertainment needed:\n "))
    else:
        no = str(input("enter the entertainers number: \n"))

    foo = str(input("do you need any food for the event?(yes or no: \n"))
    if (foo == "yes"):
        food = str(input("enter the restaraunt name: \n"))
    else:
        no = str(input("enter the restaurants number: \n"))


else:
    print("number not present:\n")

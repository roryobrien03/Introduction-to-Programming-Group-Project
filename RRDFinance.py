from module import*
def main_menu(): #This is the main menu that greets the user when launching our program
    print("=" * 29)
    row = "| {:18} | {:4.8} |"
    print(row.format("1.Walmart", "WLM"))
    print(row.format("2.Oracle", "ORCL"))
    print(row.format("3.Intel", "INTL"))
    print(row.format("4.ETSY", "ETSY"))
    print(row.format("5.Ralph Lauren", "RL"))
    print(row.format("6.Pfizer", "PFE"))
    print(row.format("7.Merck", "MRK"))
    print(row.format("8.Microsoft", "MSFT"))
    print(row.format("9.Quit",""))
    print("=" * 29)
    choice()
def choice(): #Allows user to select the stock they wish to use and assigns this stock to the stock variable to be used throughout the program until reassigned when user returns to homepage and selects a different stock
    print("At any stage if you wish to change the stock you are analysing please return to this page to select a new one.")
    choice=input("Please select the stock you wish to view: ").strip()
    global stock
    while choice != "9":
        if choice== "1":
            stock = ['WMT']
            sub_menu1()
        elif choice== "2":
            stock = ['ORCL']
            sub_menu1()
        elif choice== "3":
            stock = ['INTC']
            sub_menu1()
        elif choice== "4":
            stock = ['ETSY']
            sub_menu1()
        elif choice== "5":
            stock = ['RL']
            sub_menu1()
        elif choice== "6":
            stock = ['PFE']
            sub_menu1()
        elif choice== "7":
            stock = ['MRK']
            sub_menu1()
        elif choice== "8":
            stock = ['MSFT']
            sub_menu1()
        else: #Invalid choice
            print("Invalid choice, please try again.")
            choice=input("Please select the stock you wish to view: ").strip()
    quit_prog()#Quits program
def sub_menu1(): #Allows the user to view past performance, prediction or return to main menu
    print("1. Past Performance \n2. Prediction \n3. Return to homepage")
    select = input("Please select option: ").strip()
    while select != "3":
        if select == "1":
            time_select()
        elif select == "2":
            time_select_prediction()
        else:#Invalid choice
             print("Invalid choice, please try again.\nPlease select the number corresponding to the option you wish to view.")
             select = input("Please select option: ").strip()
    main_menu()
def time_select(): #Begins date selection , year for start date is selected in this function.
    global startyear
    print("\nPlease input what date you would like to begin analysis\nPlease only input numerical values (Example: 1st June 2022= 01-06-2022)")
    startyear=input("\nAt RRD Finance LTD we provide data from 2014 up to and including 2022\nFrom which year would you like to begin?\nIf you wish to return to the previous menu please input b: ").strip()
    while startyear != "b" :
       if startyear == "2014" or startyear =="2015" or startyear =="2016" or startyear =="2017" or startyear =="2018" or startyear =="2019" or startyear =="2020" or startyear == "2021" or startyear =="2022" :
          startmonths()
       else:
        print("Invalid choice, please try again.")
        startyear=input("From which year would you like to begin?: ").strip()
    sub_menu1()#Returns to previous menu
def time_select_prediction(): #Begins date selection , year for starting prediction modelling date is selected in this function.
    global startyear
    print("\nPlease input what date you would like to begin analysis\nPlease only input numerical values (Example: 1st June 2022= 01-06-2022)")
    startyear=input("\nAt RRD Finance LTD we provide data from 2014 up to and including 2022\nFrom which year would you like to begin?\nIf you wish to return to the previous menu please input b: ").strip()
    while startyear != "b" :
       if startyear == "2014" or startyear =="2015" or startyear =="2016" or startyear =="2017" or startyear =="2018" or startyear =="2019" or startyear =="2020" or startyear == "2021" or startyear =="2022" :
          startmonths_prediction()
       else:
        print("Invalid choice, please try again.")
        startyear=input("From which year would you like to begin?: ").strip()
    sub_menu1()
def startmonths():
    global startmonth
    startmonth= input("\nFrom which month would you like to begin?(Input b to return to year selection)(Example June= 06): ").strip()
    while startmonth != "b":
        if startmonth == "01" or startmonth == "03" or startmonth == "05" or startmonth == "07" or startmonth == "08" or startmonth == "10" or startmonth == "12":
            calendar31()
            startdates31()
            endinput()
        elif startmonth== "02":
            #Leap year detection
            if (int(startyear)%4) ==0:   # % shows remainder after dividing
                if (int(startyear)%100) == 0:
                    if (int(startyear)%400) ==0:
                        functions_leap()
                    else:
                        functions_feb()
                else:
                    functions_leap()
            else:
                functions_feb()
        elif startmonth == "04" or startmonth == "06" or startmonth == "09" or startmonth == "11":
            calendar30()
            startdates30()
            endinput()
        else:
            print("Invalid choice, please try again.")
            startmonth= input("From which month would you like to begin?: ").strip()
    time_select()#Returns to beginning of start date selection
def startmonths_prediction():
    #Links start date selection to prediction function
    global startmonth
    startmonth= input("\nFrom which month would you like to begin modelling?(Input b to return to year selection) (Example June= 06): ").strip()
    while startmonth != "b":
        if startmonth == "01" or startmonth == "03" or startmonth == "05" or startmonth == "07" or startmonth == "08" or startmonth == "10" or startmonth == "12":
            calendar31()
            startdates31()
            prediction()
        elif startmonth == "02":
            #Leap year detection
            if (int(startyear)%4) ==0:
                if (int(startyear)%100) == 0:
                    if (int(startyear)%400) ==0:
                        feb_leapyear_calendar()
                        startdatesfeb_leapyear()
                        prediction()
                    else:
                        febcalendar()
                        startdatesfeb()
                        prediction()
                else:
                    feb_leapyear_calendar()
                    startdatesfeb_leapyear()
                    prediction()
            else:
                febcalendar()
                startdatesfeb()
                prediction()
        elif startmonth == "04" or startmonth == "06" or startmonth == "09" or startmonth == "11":
            calendar30()
            startdates30()
            prediction()
        else:
            print("Invalid choice, please try again.")
            startmonth= input("From which month would you like to begin?: ").strip()
    time_select_prediction()#Returns to beginning of prediction date selection
def startdates31(): #Day selection for start date for months with 31 days
    global start
    global startday #global makes variables available to use in other functions
    startday=input("\nFrom which day of the month would you like to begin?\nInput b to return to month selection.:").strip() #.strip() removes the space before the input
    while startday != "01" and startday != "02" and startday != "03" and startday !="04" and startday !="05" and startday !="06" and startday != "07" and startday !="08" and startday !="09"  and startday != "10" and startday != "11" and startday !="12" and startday !="13" and startday != "14" and startday !="15" and startday !="16"and startday != "17" and startday != "18" and startday !="19" and startday != "20" and startday != "21" and startday != "22" and startday != "23" and startday != "24" and startday != "25" and startday != "26" and startday != "27" and startday !="28"  and startday !="29"  and startday != "30" and startday !="31":
        if startday == "b":
            startmonths()#Returns to start month selection
        else:
            print("Invalid choice, please try again.")
            startday=input("From which day of the month would you like to begin?:").strip()
    start= f'{startyear}-{startmonth}-{startday}' #f string allows us to format the date as a string
def startdates30(): #Day selection for start date for months with 30 days
    global start
    global startday
    startday=input("\nFrom which day of the month would you like to begin?\nInput b to return to month selection.:").strip()
    while startday != "01" and startday != "02" and startday != "03" and startday !="04" and startday !="05" and startday !="06" and startday != "07" and startday !="08" and startday !="09"  and startday != "10" and startday != "11" and startday !="12" and startday !="13" and startday != "14" and startday !="15" and startday !="16"and startday != "17" and startday != "18" and startday !="19" and startday != "20" and startday != "21" and startday != "22" and startday != "23" and startday != "24" and startday != "25" and startday != "26" and startday != "27" and startday !="28"  and startday !="29"  and startday != "30":
        if startday == "b":
            startmonths()
        else:
            print("Invalid choice, please try again.")
            startday=input("From which day of the month would you like to begin?\n Input b to return to month selection.:").strip()
    start= f'{startyear}-{startmonth}-{startday}' #assigns start date
def startdatesfeb(): #Day selection for start date when month is February
    global start
    global startday
    startday=input("\nFrom which day of the month would you like to begin?\nInput b to return to month selection.:").strip()
    while startday != "01" and startday != "02" and startday != "3" and startday !="04" and startday !="05" and startday !="06" and startday != "07" and startday !="08" and startday !="09"  and startday != "10" and startday != "11" and startday !="12" and startday !="13" and startday != "14" and startday !="15" and startday !="16"and startday != "17" and startday != "18" and startday !="19" and startday != "20" and startday != "21" and startday != "22" and startday != "23" and startday != "24" and startday != "25" and startday != "26" and startday != "27" and startday !="28" :
        if startday == "b":
            startmonths()
        else:
            print("Invalid choice, please try again.")
            startday=input("From which day of the month would you like to begin?:").strip()
    start= f'{startyear}-{startmonth}-{startday}' #assigns start date
def startdatesfeb_leapyear():
    global start
    global startday
    startday=input("\nFrom which day of the month would you like to begin?\nInput b to return to month selection.:").strip()
    while startday != "01" and startday != "02" and startday != "3" and startday !="04" and startday !="05" and startday !="06" and startday != "07" and startday !="08" and startday !="09"  and startday != "10" and startday != "11" and startday !="12" and startday !="13" and startday != "14" and startday !="15" and startday !="16"and startday != "17" and startday != "18" and startday !="19" and startday != "20" and startday != "21" and startday != "22" and startday != "23" and startday != "24" and startday != "25" and startday != "26" and startday != "27" and startday !="28" and startday !="29": #Allows 29th of February to be chosen in leap years
        if startday == "b":
            startmonths()
        else:
            print("Invalid choice, please try again.")
            startday=input("From which day of the month would you like to begin?:").strip()
    start= f'{startyear}-{startmonth}-{startday}' #assigns start date
def endinput(): # End date selection , month for end date is selected in this function. User also has option to select now as end date in this function.
    global end
    global endyear
    print("Would you like to conclude analysis on today's date?:")
    endtoday= input("Please input Yes or No: ")
    while endtoday !="Yes":
        if endtoday == "No":
            endyear=input("Please input the year you wish to conclude analysis\nIf you would like to return to start date selection input b :  ").strip()
            while endyear != "b":
                if endyear == "2014" or endyear =="2015" or endyear =="2016" or endyear =="2017" or endyear =="2018" or endyear =="2019" or endyear =="2020" or endyear == "2021" or endyear =="2022" :
                  endm()
                else:
                    print("Invalid choice, please try again.")
                    endyear=input("Please input the year you wish to conclude analysis\n If you would like to return to end day selection input b :  ").strip()
            time_select()
        else:
            print("Invalid choice, please try again.")
            print("Would you like to conclude analysis on today's date?:")
            endtoday= input("Please input Yes or No: ")
    end=dt.datetime.now() #assigns time now as end date
    if dt.datetime.strptime(start,"%Y-%m-%d")>dt.datetime.now(): #Prevents start date being in the future.
        print("This is an invalid date selection\nThe start date you have chosen is in the future thus data is not available yet\nIf you wish to view future price prediction this data is available in our prediction section")
        time.sleep(0.8)#Delays printing of time_select() function on screen
        time_select()

    print(f"Start date = {start}") #f" allows a variable to be printed in a string
    print(f"End date = {end}")
    print("\n")
    sub_menu3()
def endm():#End month selection
    global endmonth
    endmonth=input("Please input what month you would like to conclude analysis\nPlease only input numerical values (Example: June= 06)\nIf you wish to return to the previous page input b:  ").strip()
    while endmonth != "b":
        if endmonth == "01" or endmonth == "03" or endmonth == "05" or endmonth == "07" or endmonth == "08" or endmonth == "10" or endmonth == "12":
            calendar31()
            enddates31()
            date_error()
            sub_menu3()
        elif endmonth== "02":
            #Leap year detection
            if (int(endyear)%4) ==0:  # % shows remainder after dividing
                if (int(endyear)%100) == 0:
                    if (int(endyear)%400) ==0:
                        endfunctions_leap()
                    else:
                        endfunctions_feb()
                else:
                    endfunctions_leap()
            else:
                endfunctions_feb()

        elif endmonth == "04" or endmonth == "06" or endmonth == "09" or endmonth == "11":
            calendar30()
            enddates30()
            date_error()
            sub_menu3()

        else: #Invalid choice
            print("Invalid choice, please try again.")
            endmonth=input("Please input what month you would like to conclude analysis\nPlease only input numerical values (Example: June= 06)\nIf you wish to return to the previous page input b:  ").strip()
    endinput() #Returns to end date selection
def enddates31():  #Day selection for end date for months with 31 days
    global end
    global endday
    endday=input("Please input what day of the month you wish to conclude analysis\nIf you wish to return to end month selection input b: ").strip()
    while endday != "01" and endday != "02" and endday != "03" and endday !="04" and endday !="05" and endday !="06" and endday != "07" and endday !="08" and endday !="09"  and endday != "10" and endday != "11" and endday !="12" and endday !="13" and endday != "14" and endday !="15" and endday !="16"and endday != "17" and endday != "18" and endday !="19" and endday != "20" and endday != "21" and endday != "22" and endday != "23" and endday != "24" and endday != "25" and endday != "26" and endday != "27" and endday !="28"  and endday !="29"  and endday != "30" and endday !="31":
        if endday == "b":
            endinput()
        else:
            print("Invalid choice, please try again.")
            endday=input("Please input what day of the month you wish to conclude analysis: ").strip()
    end=f'{endyear}-{endmonth}-{endday}' #assigns end date
    print(f"Start date = {start}") #f" allows a variable to be printed in a string
    print(f"End date = {end}")
def enddates30(): #Day selection for end date for months with 30 days
    global end
    global endday
    endday=input("Please input what day of the month you wish to conclude analysis\nIf you wish to return to end month selection input b: ").strip()
    while endday != "01" and endday != "02" and endday != "03" and endday !="04" and endday !="05" and endday !="06" and endday != "07" and endday !="08" and endday !="09"  and endday != "10" and endday != "11" and endday !="12" and endday !="13" and endday != "14" and endday !="15" and endday !="16"and endday != "17" and endday != "18" and endday !="19" and endday != "20" and endday != "21" and endday != "22" and endday != "23" and endday != "24" and endday != "25" and endday != "26" and endday != "27" and endday !="28"  and endday !="29"  and endday != "30":
        if endday == "b":
            endinput()
        else:
            print("Invalid choice, please try again.")
            endday=input("Please input what day of the month you wish to conclude analysis: ").strip()
    end=f'{endyear}-{endmonth}-{endday}' #assigns end date
    print(f"Start date = {start}") #f" allows a variable to be printed in a string
    print(f"End date = {end}")
def enddatesfeb(): #Day selection for end date when month is February
    global end
    global endday
    endday=input("Please input what day of the month you wish to conclude analysis\nIf you wish to return to end month selection input b: ").strip()
    while endday != "01" and endday != "02" and endday != "03" and endday !="04" and endday !="05" and endday !="06" and endday != "07" and endday !="08" and endday !="09"  and endday != "10" and endday != "11" and endday !="12" and endday !="13" and endday != "14" and endday !="15" and endday !="16"and endday != "17" and endday != "18" and endday !="19" and endday != "20" and endday != "21" and endday != "22" and endday != "23" and endday != "24" and endday != "25" and endday != "26" and endday != "27" and endday !="28":
        if endday == "b":
            endinput()
        else:
            print("Invalid choice, please try again.")
            endday=input("Please input what day of the month you wish to conclude analysis: ").strip()#Day selection for end date for Feb
    end=f'{endyear}-{endmonth}-{endday}' #assigns end date
    print(f"Start date = {start}") #f" allows a variable to be printed in a string
    print(f"End date = {end}")
def end_dates_feb_leap():
    global end
    global endday
    endday=input("Please input what day of the month you wish to conclude analysis\nIf you wish to return to end month selection input b: ").strip()
    while endday != "01" and endday != "02" and endday != "03" and endday !="04" and endday !="05" and endday !="06" and endday != "07" and endday !="08" and endday !="09"  and endday != "10" and endday != "11" and endday !="12" and endday !="13" and endday != "14" and endday !="15" and endday !="16"and endday != "17" and endday != "18" and endday !="19" and endday != "20" and endday != "21" and endday != "22" and endday != "23" and endday != "24" and endday != "25" and endday != "26" and endday != "27" and endday !="28":
        if endday == "b":
            endinput()
        else:
            print("Invalid choice, please try again.")
            endday=input("Please input what day of the month you wish to conclude analysis: ").strip()#Day selection for end date for Feb
    end=f'{endyear}-{endmonth}-{endday}' #assigns end date
    print(f"Start date = {start}") #f" allows a variable to be printed in a string
    print(f"End date = {end}")
def functions_feb(): #Collection of functions used to process start date when month is February
    febcalendar()
    startdatesfeb()
    endinput()
def functions_leap():#Collection of functions used to process start date when February is chosen in is a leap year
    feb_leapyear_calendar()
    startdatesfeb_leapyear()
    endinput()
def endfunctions_feb(): #Collection of functions used to process end date when month is February
    febcalendar()
    enddatesfeb()
    date_error()
    sub_menu3()
def endfunctions_leap():
    feb_leapyear_calendar()
    end_dates_feb_leap()
    date_error()
    sub_menu3()
def date_error():
    #Prevents users selecting end dates earlier than start dates or selecting start and end dates in the future.
    if dt.datetime.strptime(start,"%Y-%m-%d")>dt.datetime.now() or dt.datetime.strptime(end, "%Y-%m-%d")>dt.datetime.now(): #dt.datetime.strptime formats start and end ,which are strings, into python datetime which allows it to be compared to dt.datetime.now()
        print("This is an invalid date selection\nThe date you have chosen is in the future thus data is not available yet\nIf you wish to view future price prediction this data is available in our prediction section")
        time_select()
    elif int(endyear)<int(startyear)or int(endyear)==int(startyear) and int(endmonth)<int(startmonth) or int(endyear)==int(startyear) and int(endmonth)==int(startmonth) and int(endday)< int(startday):
        print("This is an invalid date selection\nEnd date cannot be earlier than start date")
        time_select()
def sub_menu3():
    global Close, df
    df = pdr.get_data_yahoo(stock, start, end) # dataframe is data extracted from yahoo finance depending on stock chosen and start and end date chosen
    Close = df.Close #closes dataframe
    print("Would you like to see the statistical or visual description of past performance? \n 1. Statistics \n 2. Visuals\n 3. Back" )
    option = input("Please select option: ").strip()
    while option != "3":
        if option == "1":
            stats()
        elif option == "2":
            visuals()
        else:
            print("Invalid choice, please try again.\nPlease select the number corresponding to the option you wish to view.")
            option= input("Please select option: ").strip()
    sub_menu1()
def visuals(): # Visualisation of stock data
    print("1. Raw time series \n2. Trend lines \n3. Moving Averages \n4. Weighted Moving Averages \n5. Back")
    print("\nPlease close the graph window after viewing in order to proceed with further analysis\n")
    visual = input("Please select option: ").strip()
    while visual !="5":
        if visual =="1":
            plot = Close.plot()
            plt.ylabel("Price($)")
            plt.xlabel("Date")
            plt.title(f"Raw Time Series Of {stock} Stock Price")
            plt.show()
            print("\n")
            visuals()
        elif visual =="2":
            x = np.arange(Close.size)
            fit = np.polyfit(x, Close, 1)
            fit = np.squeeze(fit)
            fit_function = np.poly1d(fit)
            sns.lineplot(data=Close) ;
            sns.lineplot(x=Close.index, y=fit_function(x))
            plt.xlabel("Date")
            plt.ylabel("Price($)")
            plt.title(f"Trend Line Of {stock} Stock Price")
            plt.show()
            print("\n")
            visuals()
        elif visual =="3":
            n = input("How many days would you like the moving average to be calculated over(Max 100)?(Input b to return to visual selection): ").strip()
            while n != "b":
                try:
                    days=int(n)
                    if days<100 and days>0: #Prevents negative and values > 100 being inputted
                        mavg = Close.rolling(window=days).mean()
                        plt.plot(mavg)
                        plt.ylabel("Price($)")
                        plt.xlabel("Date")
                        plt.title(f"{n} Day Moving Average Of {stock} Stock Price")
                        plt.show()
                        print("\n")
                        visuals()
                    else:
                        print("Invalid choice please try again\nMaximum amount of days is 100")
                        n =input("How many days would you like the moving average to be calculated over(Max 100)?(Input b to return to visual selection): ").strip()
                except ValueError:#Prints error if string ,aside from b,is inputted
                    print("Invalid choice, Please input a number")
                    n = input("How many days would you like the moving average to be calculated over(Max 100)?(Input b to return to visual selection): ").strip()
            visuals()
        elif visual =="4":
            x = input("How many days do you want to calculate the exponentially weighted moving average over(Max 100)?(Input b to return to visual selection): ").strip()
            while x != "b":
                try:
                    period=int(x)
                    if period<100 and period>0:
                        wavg = df.Close.ewm(span=period, adjust = False).mean()
                        plt.plot(df.Close, label = 'Close')
                        plt.xlabel("Date")
                        plt.ylabel("Price($)")
                        plt.title(f"{x} Day Weighted Moving Average Of {stock} Stock Price")
                        plt.show()
                        print("\n")
                        visuals()
                    else:
                        print("Invalid choice please try again\nMaximum amount of days is 100")
                        x = input("How many days do you want to calculate the exponentially weighted moving average over(Max 100)?(Input b to return to visual selection): ").strip()
                except ValueError:
                    print("Invalid choice, Please input a number")
                    x = input("How many days do you want to calculate the exponentially weighted moving average over(Max 100)?(Input b to return to visual selection): ").strip()
            visuals()
        else:
            print("Invalid choice please try again")
            visuals()
    sub_menu3()
def quartiles():
    print("Which quartile would you like to view?\n1. Q1 \n2. Q2/median \n3. Q3\n4. Back")
    quartile = input("Please select option: " ).strip()
    while quartile != "4":
        if quartile == "1":
            print("\n")
            print("Quartile 1 for the period you have chosen is: ")
            print(Close.quantile(q=0.25)) # prints Q1 (the number halfway between lowest number and middle number)
            print("\n")
            time.sleep(0.8)
            quartiles()
        elif quartile == "2":
            print("\n")
            print("The median (quartile 2) for the period you have chosen is: ")
            print(Close.quantile(q=0.5)) # prints Q2/median (the middle number halfway between lowest and highest number)
            print("\n")
            time.sleep(0.8)
            quartiles()
        elif quartile == "3":
            print("\n")
            print("Quartile 3 for the period you have chosen is: ")
            print(Close.quantile(q=0.75)) # prints Q3 (the number halfway between middle number and highest number)
            print("\n")
            time.sleep(0.8)
            quartiles()
        else:
            print("Sorry, this is not an option")
            time.sleep(0.8)
            quartiles()
    stats()
def stats(): # Calculates statistics for chosen stock between chosen date range
    print("Statistics:")
    print("1. Mean \n2. Max \n3. Min \n4. Quartiles \n5. Standard Deviation \n6. Range \n7. Coefficient of Variation \n8. Back  ")
    type= input("Please select option: ").strip()
    while type != "8":
        if type == "1":
            print("\n")
            print("The mean stock price over the period you have chosen is: ")
            print(Close.mean()) # Calculates mean from dates selected
            print("\n")
            time.sleep(0.8)
            stats()
        elif type == "2":
            print("\n")
            print("The maximum stock price over the period you have chosen is: ")
            print(Close.max()) # Calculates maximum value from dates selected
            print("\n")
            time.sleep(0.8)
            stats()
        elif type == "3":
            print("\n")
            print("The minimum stock price over the period you have chosen is: ")
            print(Close.min()) # Calculates minimum value from dates collected
            print("\n")
            time.sleep(0.8)
            stats()
        elif type == "4":
            quartiles()
        elif type =="5":
            print("\n")
            print("The standard deviation of stock prices over the period you have chosen is: ")
            print(Close.std()) # Calculates standard deviation of stock prices for dates selected
            print("\n")
            time.sleep(0.8)
            stats()
        elif type== "6":
            print("\n")
            print("The range of stock prices over the period you have chosen is: ")
            print(float(Close.max()) - float(Close.min()))       # Calculates range of stock price for dates selected
            print("\n")
            time.sleep(0.8)
            stats()
        elif type == "7":
            print("\n")
            print("The coefficient of variation of stock prices over the period you have chosen is: ")
            print(Close.var())     # Calculates coefficient of variation of stock price for dates selected
            print("\n")
            time.sleep(0.8)
            stats()
        else:
            print("Invalid choice, please try again.\nPlease select the number corresponding to the option you wish to view.")
            type= input("Please select option: ").strip()
    sub_menu3()
def prediction():
        endnow = dt.datetime.now() #Pre assigning end of modelling period to now as we want to predict future price from now thus having training data including the most recent data will ensure greater accuracy
        df = pdr.get_data_yahoo(stock,start, endnow).reset_index(drop=False)
        df = df[['Close',]]
        prediction_days = input("How many days would you like this prediction to be for(Max 100)?(Input b to return to modelling period selection): ").strip() # Asks user how far in the future they want to predict the stock price for
        while prediction_days!= "b":
            try:
                future_days = int(prediction_days)# Asks user how far in the future they want to predict the stock price for
                if future_days<101 and future_days>0:
                    df['Prediction'] = df[['Close']].shift(-future_days)


                    X = np.array(df.drop(['Prediction'], axis=1))[:-future_days] # Creates x-variable data set using indexes, removes last {future_days} rows, and converts it to an array in numpy
                    y = np.array(df['Prediction'])[:-future_days] # Creates y-variable data set using indexes, removes last {future_days} rows, and converts it to an array in numpy


                    x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state = 0 , shuffle = True) # test_size = 0.25 makes 1/4 of our data be used to train our data and 3/4 of our data used to test the data


                    tree = DecisionTreeRegressor().fit(x_train, y_train) # Creates a decision tree regressor model and train it

                    lr = LinearRegression().fit(x_train, y_train) # Creates a decision tree regressor model and train it
                    predicted=lr.predict(x_test)
                    treepredicted=tree.predict(x_test)

                    pd.options.mode.chained_assignment = None
                    x_future = df.drop(['Prediction'], axis=1)[:-future_days]
                    x_future = x_future.tail(future_days) # Creates a dataset of last {future_days} rows
                    x_future = np.array(x_future) # Converts x_future to a numpy array


                    tree_prediction = tree.predict(x_future) # Createst dataset of the model tree predictions
                    lr_prediction = lr.predict(x_future) # Creates dataset of the Model linear regression predictions


                    modeltype = input("\nWould you like to view a Linear Regression Model or a Tree Regressor Model? \n1.Linear Regression Model \n2.Tree Regressor Model \n3.Return to time selection\nPlease select option: ").strip()
                    while modeltype != "3":
                        if modeltype=="1":
                            predictions=lr_prediction
                            choice=input("\nWould you like to see a statistical or visual represenation ?\n1.Statistics\n2.Visualisation\n3.Back\nPlease select option: ").strip()
                            while choice !="3":
                                if choice== "1":
                                    option=input("\nPrediction Statistics: \n1.Price prediction\n2.Error statistics\n3.Back\nPlease select option: ").strip()
                                    while option != "3":
                                        if option== "1":
                                            print("\n")
                                            print("The price($) of",stock,"stock",future_days,"days from now is predicted to be: ")
                                            print(lr_prediction[future_days-1])
                                            print("\n")
                                            time.sleep(0.8)
                                            option=input("\nPrediction Statistics: \n1.Price prediction\n2.Error statistics\n3.Back\nPlease select option: ").strip()

                                        elif option== "2":
                                            print("\n")
                                            print("Linear Regression Model Error Statistics:")
                                            print("Mean Absolute Error:" , metrics.mean_absolute_error(y_test, predicted))
                                            print("Mean Squared Error:" , metrics.mean_squared_error(y_test, predicted))
                                            print("Root Mean Squared Error:", math.sqrt(metrics.mean_squared_error(y_test, predicted)))
                                            print("\n")
                                            time.sleep(0.8)
                                            option=input("\nPrediction Statistics: \n1.Price prediction\n2.Error statistics\n3.Back\nPlease select option: ").strip()

                                        else:
                                            print("\n")
                                            print("Invalid choice please try again")
                                            time.sleep(0.8)
                                            option=input("\nPrediction Statistics: \n1.Price prediction\n2.Error statistics\n3.Back\nPlease select option: ").strip()
                                            print("\n")
                                    choice=input("\nWould you like to see a statistical or visual representation ?\n1.Statistics\n2.Visualisation\n3.Back\nPlease select option: ").strip()

                                elif choice=="2":
                                    print("\nPlease close the graph window after viewing in order to proceed with further analysis\n")
                                    valid = df[X.shape[0]:]
                                    valid['Predictions'] = predictions
                                    plt.figure()
                                    plt.title(f'{future_days} Day Linear Regression Model Price Prediction For {stock} Stock')
                                    plt.xlabel('Dates')
                                    plt.ylabel('Close')
                                    plt.plot(df['Close'])
                                    plt.plot(valid[['Close','Predictions']])
                                    plt.legend(['Original','Valid','Predicted'])
                                    plt.show()
                                    time.sleep(0.8)
                                    choice=input("Would you like to see a statistical or visual represenation ?\n1.Statistics\n2.Visualisation\n3.Back\nPlease select option: ").strip()

                                else:
                                    print("Invalid choice please try again")
                                    time.sleep(0.8)
                                    choice=input("\nWould you like to see a statistical or visual representation ?\n1.Statistics\n2.Visualisation\n3.Back\nPlease select option:").strip()

                            modeltype = input("\nWould you like to view a Linear Regression Model or a Tree Regressor Model? \n1.Linear Regression Model \n2.Tree Regressor Model \n3.Return to time selection\nPlease select option: ").strip()

                        elif modeltype=="2":
                            predictions=tree_prediction
                            select=input("\nWould you like to see a statistical or visual representation ?\n1.Statistics\n2.Visualisation\n3.Back\nPlease select option: ").strip()
                            while select != "3":
                                if select =="1":
                                    type=input("\nPrediction Statistics: \n1.Price prediction\n2.Error statistics\n3.Back\nPlease select option: ").strip()
                                    while type != "3":
                                        if type=="1":
                                            print("\n")
                                            print("The price($) of",stock,"stock",future_days,"days from now is predicted to be: ")
                                            print(tree_prediction[future_days-1])
                                            print("\n")
                                            time.sleep(0.8)
                                            type=input("\nPrediction Statistics: \n1.Price prediction\n2.Error statistics\n3.Back\nPlease select option: ").strip()

                                        elif type =="2":
                                            print("\n")
                                            print("Tree Regressor Model Error Statistics:")
                                            print("Mean Absolute Error:" , metrics.mean_absolute_error(y_test, treepredicted))
                                            print("Mean Squared Error:" , metrics.mean_squared_error(y_test, treepredicted))
                                            print("Root Mean Squared Error:", math.sqrt(metrics.mean_squared_error(y_test, treepredicted)))
                                            print("\n")
                                            time.sleep(0.8)
                                            type=input("\nPrediction Statistics: \n1.Price prediction\n2.Error statistics\n3.Back\nPlease select option: ").strip()

                                        else:
                                            print("\n")
                                            print("Invalid option please try again")
                                            time.sleep(0.8)
                                            type=input("\nPrediction Statistics: \n1.Price prediction\n2.Error statistics\n3.Back\nPlease select option: ").strip()
                                            print("\n")
                                    select=input("\nWould you like to see a statistical or visual represenation ?\n1.Statistics\n2.Visualisation\n3.Back\nPlease select option: ").strip()

                                elif select =="2":
                                    print("\nPlease close the graph window after viewing in order to proceed with further analysis\n")
                                    valid = df[X.shape[0]:]
                                    valid['Predictions'] = predictions
                                    plt.figure()
                                    plt.title(f'{future_days} Day Tree Regressor Model Price Prediction For {stock} Stock')
                                    plt.xlabel('Dates')
                                    plt.ylabel('Close')
                                    plt.plot(df['Close'])
                                    plt.plot(valid[['Close', 'Predictions']])
                                    plt.legend(['Original', 'Valid', 'Predicted'])
                                    plt.show()
                                    print("\n")
                                    time.sleep(0.8)
                                    select=input("Would you like to see a statistical or visual represenation ?\n1.Statistics\n2.Visualisation\n3.Back\nPlease select option: ").strip()
                                else:
                                    print("Invalid choice please try again")
                                    select=input("Would you like to see a statistical or visual represenation ?\n1.Statistics\n2.Visualisation\n3.Back\nPlease select option:").strip()
                            modeltype = input("\nWould you like to view a Linear Regression Model or a Tree Regressor Model? \n1.Linear Regression Model \n2.Tree Regressor Model \n3.Return to time selection\nPlease select option: ").strip()

                        else:
                            print("Invalid choice please try again")
                            time.sleep(0.8)
                            modeltype = input("\nWould you like to view a Linear Regression Model or a Tree Regressor Model? \n1.Linear Regression Model \n2.Tree Regressor Model \n3.Return to time selection\nPlease select option: ").strip()
                    time_select_prediction()
                else:#Invalid choice
                    print("Invalid choice please try again")
                    prediction()
            except ValueError:
                print("Invalid choice, Please input a number")
                prediction()
        time_select_prediction()
def quit_prog(): #Quit program function
    print("You have selected the quit option")
    quit = input("Are you sure you want to quit the program ? \n Please input Yes or No : ").strip()
    while quit != "Yes":
        if quit =="No":
            main_menu()
        else:#Invalid choice
            print("Invalid choice, please try again.")
            quit =input("Are you sure you want to quit the program ?\nPlease input Yes or No : ").strip()
    quit_moving_message()
    exit()
#Opening messgae
print("{:=^40}".format("Welcome to RRD Finance LTD"))
print("We are an industry leading financial analytics firm providing in depth analysis and statistics on our stock portfolio \nPlease avail of the information on our stocks below.")
main_menu()

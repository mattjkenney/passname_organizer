def isFalseAppName(name):

    print('')
    print('Choose an option from the following menu.')
    print('')
    print('____________________________________________')
    print('')
    print('             0: Add App')
    print('             1: Return to App Menu')
    print('____________________________________________')
    print('')
    ans = input()
    if ans == 0:
        addNew(name)
    elif ans == 1:
        pass
    else:
        print('')
        print('That is not a valid response.')

    return False
    

def appMenu(loc):

    global sf
    global p
    global appCL
    global loc2
    
    import pickle as p
    import ifSignFalse as sf
    import applicationClass as appCL
    
    loc2 = loc + '\\' + 'bah' + '.pickle'

    flag = False
    while flag == False:
        print('')
        print('')
        print('Choose an option from the following menu: ')
        print('__________________________________________________________________')
        print('')
        print('          0: Enter App Name')
        print('          1: Add New App')
        print('          2: Choose from List')
        print('          3: Search')
        print('          4: Quit Program')
        print('__________________________________________________________________')
        print('')
        ans = input()

        if ans == '0':
            print('')
            name = input('Enter the name of app you want to enter: ')
            try:
                df = open(loc2, 'rb')
            except:
                print('')
                print('')
                print('That app does not yet exist.')
                flag = isFalseAppName(name)
            else:
                appList = p.load(df)
                i = -1
                flag2 = False
                while flag2 == False:
                    i += 1
                    try:
                        appDictTry = appList[i]
                    except:
                        flag2 = True
                        print('')
                        print('')
                        print('That app does not yet exist.')
                        isFalseAppName(name)
                    else:
                        if appDictTry.get('title') == name:
                            flag2 = True
                            flag = True
                            appDict = appDictTry
                            df.close()
                            appObj = appCL.App(
                                appDict.get('name'),
                                appDict.get('url'),
                                appDict.get('username'),
                                appDict.get('password'))
        
        elif ans == '1':
            addNew(0)
        elif ans == '2':
            try:
                name = 'apps'
                df = open(loc2, 'rb')
            except:
                print('')
                print('')
                print('No apps yet exist.')
                flag = isFalseAppName(0)
            else:
                appList = p.load(df)
                df.close()
                print('')
                print('_________________________________________________')
                print('')
                num = 0
                if appList == []:
                    print('           No Apps Yet Exist')
                    print('_________________________________________________')
                    flag = isFalseAppName(0)
                else:
                    print('              0: Return to Main Menu')
                    for i in appList:
                        num += 1
                        print('             ', str(num) + ':', i.get('title'))
                    print('_________________________________________________')
                    print('')
                    print('')
                    numFlag = False
                    while numFlag == False:
                        appNum = input('Enter the number next to the app you need: ')
                        try:
                            appNum = int(appNum)
                        except:
                            print('')
                            print('Enter numbers only.  Such as "3", and not "three".')
                            print('')
                        else:
                            numFlag = True
                            if appNum == 0:
                                flag = True
                                appObj = 0
                            else:
                                flag = True
                                appNum -= 1
                                appDict = appList[appNum]
                                appObj = appCL.App(
                                    appDict.get('title'),
                                    appDict.get('url'),
                                    appDict.get('username'),
                                    appDict.get('password'))
                               
        elif ans == '3':
            print('')
            search = input('Enter the keyword you want to search: ')
            search = search.lower()
            print('')
            print('Choose the number from the list of results: ')
            print('_______________________________________________')
            print('')
            print('          0: Return to Main Menu')
            file = open(loc2, 'rb')
            appList = p.load(file)
            num = 0
            for i in appList:
                num += 1
                titleLower = i.get('title')
                if search in titleLower.lower():
                    print('         ', str(num) + ':', i.get('title'))
            print('_______________________________________________')
            print('')
            flag3 = False
            while flag3 == False:
                choose = input()
                try:
                    choose = int(choose)
                except:
                    print('')
                    print('Enter numbers only.')
                else:
                    flag3 = True
                    if choose == 0:
                        flag3 = True
                    else:
                        flag3 = True
                        flag = True
                        j = choose - 1
                        appDict = appList[j]
                        appObj = appCL.App(
                            appDict.get('title'),
                            appDict.get('url'),
                            appDict.get('username'),
                            appDict.get('password'))
            file.close()
            
        elif ans == '4':
            flag = True
            appObj = 'q'
            
        else:
            print('')
            print('That is not a valid response.')
                        
    return appObj

def addNewOther():
    
    print('')
    print('')
    url = input('Enter the url: ')
    print('')
    username = input('Enter the username: ')
    password = addNewPass()

    return url, username, password

def addNewPass():
    
    flag = False
    while flag == False:
        print('')
        print('How do you want to set the password?')
        print('___________________________________________')
        print('')
        print('            0: User Defined')
        print('            1: Randomly Generated')
        print('___________________________________________')
        print('')
        ans = input()

        if ans == '0':
            flag = True
            password = input('Enter the password: ')
            
        elif ans == '1':
            flag = True
            password = 'r'
            
        else:
            print('')
            print('That is not a valid response.')
        
    return password

def addNew(name):

    if name != 0:
        url, username, password = addNewOther()        
        
    elif name == 0:
        print('')
        print('')
        name = input('Enter the name of the application: ')
        url, username, password = addNewOther()

    newApp = appCL.App(name, url, username, password)

    newApp.record()
    print('')
    print('The following data was recorded: ')
    newApp.show()

    return


        
        
            
            

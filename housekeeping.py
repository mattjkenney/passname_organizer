def housekeeping(loc):

    global p
    global sf
    global loc2
    
    import pickle as p
    import ifSignFalse as sf
    
    loc2 = loc + '\\' + 'users' + '.pickle'

    access = False
    while access == False:
        print('WELCOME TO THE USERNAME AND PASSWORD PORTAL!')
        print('')
        print('')
        print('Choose an option from the following menu:')
        print('___________________________________')
        print('')
        print('        0: Sign In')
        print('        1: Add Member')
        print('        2: Quit Program')
        print('___________________________________')
        print('')
        ans = input()

        if ans == '0':
            access = signIn()

        elif ans == '1':
            ans = addMember()

        elif ans == '2':
            print('')
            print('')
            print('GoodBye!')
            access = True
        else:
            print('')
            print('')
            print('That is not a valid response.')
            
    return ans
    

def usernameSign():

    flag = False
    while flag == False:
        print('')
        print('')
        user = input('Enter your first name: ')
        try:
            user = user.lower()
        except:
            print('')
            print('')
            print('Enter letters only.  Numbers are not allowed.')
        else:
            try:
                df = open(loc2, 'rb')
            except:
                flag = sf.ifSignFalse()
                if flag == True:
                    user = 0
                    userDict = 0
            else:
                userDict = p.load(df)
                df.close()
                if user not in userDict.keys():
                    flag = sf.ifSignFalse()
                    if flag == True:
                        user = 0
                        userDict = 0
                else:
                    flag = True

    return user, flag, userDict


def signIn():

    flag = False
    while flag == False:
        user, flag, userDict = usernameSign()
    if user == 0:
        flag = True
        access = False

    else:      
        correctPass = userDict.get(user)
        flag = False
        while flag == False:
            print('')
            print('')
            password = input('Enter your password: ')
            if password != correctPass:
                ans = sf.ifSignFalse()
                if ans == True:
                    access = False
                    flag = True
            else:
                access = True
                flag = True

    return access

def addMember():

    flag = False
    while flag == False:
        print('')
        print('')
        user = input('Enter your first name: ')
        try:
            user = user.lower()
        except:
            print('')
            print('')
            print('Enter letters only.  Numbers are not allowed.')
        else:
            try:
                df = open(loc2, 'rb')
            except:
                print('')
                print('')
                password = input('Enter a password: ')
                newDict = {
                    user: password
                    }
                df = open(loc2, 'wb')
                p.dump(newDict, df)
                df.close()
                flag = True
                
            else:
                oldDict = p.load(df)
                df.close()
                isThere = user in oldDict.keys()
                if isThere == True:
                    print('')
                    print('')
                    print('Name already exist. Please choose a new name.')
                else:
                    print('')
                    print('')
                    password = input('Enter a password: ')
                    oldDict[user] = password
                    df = open(loc, 'wb')
                    p.dump(oldDict, df)
                    df.close()
                    flag = True
                    
    return False

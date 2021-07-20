#MAIN Program file
def main():

    global uM
    
    import housekeeping as hk
    import appMenu as am
    import editApp as ea
    import applicationClass as appCL
    import os
##    import userMod as uM

    loc = os.path.dirname(os.path.abspath(__file__))
   
##    ans = hk.housekeeping(loc)
##    while ans == False:
##        ans = hk.housekeeping(loc)
        
    appObj = 0
    while appObj == 0:
        appObj = am.appMenu(loc)
            
    while appObj != 'q':
        while appObj != 'n': 
            appObj = ea.editMain(appObj)
        appObj = am.appMenu(loc)

    print('Goodbye!')

def setup():

    print("Let's setup your Admin account.")
    print('')
    adminObj = uM.Admin(0, 0, 0, 0, 0, 0, 0, 0)
    adminObj.record()
    
def housekeeping():

    close = False
    access = False
    while access == False:
        print('WELCOME TO PASSWORD MANAGER!')
        print('')
        print('Choose from the Sign In Menu: ')
        print('_' * 10 + '_______________' + '_' * 10)
        print('')
        print(' ' * 10 + '0: Sign In     ' + ' ' * 10)
        print(' ' * 10 + '1: Add User    ' + ' ' * 10)
        print(' ' * 10 + '2: Exit Program' + ' ' * 10)
        print('_' * 10 + '_______________' + '_' * 10)
        print('')
        ans = input()

        if ans == '0':
            print('')
            userObj = uM.User(1, 0, 1, 1, 1, 1, 1, False)
            if userObj.isUser() == True:
                access = security(userObj)
                if access == True:
                    print('')
                    print('WELCOME!')
                else:
                    print('')
                    print('Sorry. Your Sign-in attempt failed.')
                    print('')

        elif ans == '1':
            print('')
            print('Please sign in as an Administrator. ')
            print('')
            userObj = uM.Admin(1, 0, 1, 1, 1, 1, 1, 1, 1, 1)
            if userObj.isUser == True:
                userObj = userObj.reset()
                if userObj.isAdmin == True:
                    userObj.createNewUser()
                else:
                    print('')
                    print('This user does not have administrator access.')

        elif ans == '2':
            access = True
            close = True

        return access, close
                
def security(userObj):

    secLevel = userObj.secLevel

    if secLevel[ :3] == '000':
        print('')
        pinTry = input('Enter your pin: ')
        if pinTry == userObj.pin:
            print('')
            passTry = input('Enter your password: ')
            if passTry == userObj.password:
                adminObj = userObj.findAdmin()
                rT = adminObj.sendMSG(userObj.email)
                print('')
                epinTry = input('Enter the pin from your email: ')
                if epinTry == rT:
                    access = True
                else:
                    access = False
            else:
                access = False
        else:
            access = False

    elif secLevel[ :3] == '100':
        print('')
        pinTry = input('Enter your pin: ')
        if pinTry == userObj.pin:
            access = True
        else:
            access = False

    elif secLevel[ :3] == '010':
        print('')
        passTry = input('Enter your password: ')
        if passTry == userObj.password:
            access = True
        else:
            access = False

    elif secLevel[ :3] == '001':
        adminObj = userObj.findAdmin()
        rT = adminObj.sendMSG(userObj.email)
        print('')
        epinTry = input('Enter the pin from your email: ')
        if epinTry == rT:
            access = True
        else:
            access = False

    elif secLevel[ :3] == '110':
        print('')
        pinTry = input('Enter your pin: ')
        if pinTry == userObj.pin:
            print('')
            passTry = input('Enter your password: ')
            if passTry == userObj.password:
                access = True
            else:
                access = False
        else:
            access = False

    elif secLevel[ :3] == '011':
        print('')
        passTry = input('Enter your password: ')
        if passTry == userObj.password:
            adminObj = userObj.findAdmin()
            rT = adminObj.sendMSG(userObj.email)
            print('')
            epinTry = input('Enter the pin from your email: ')
            if epinTry == rT:
                access = True
            else:
                access = False
        else:
            access = False

    elif secLevel[ :3] == '101':
        print('')
        pinTry = input('Enter your pin: ')
        if pinTry == userObj.pin:
            adminObj = userObj.findAdmin()
            rT = adminObj.sendMSG(userObj.email)
            print('')
            epinTry = input('Enter the pin from your email: ')
            if epinTry == rT:
                access = True
            else:
                access = False
        else:
            access = False

    elif secLevel[ :3] == '111':
        access = True

    return access
                                
main()

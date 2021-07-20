def editMain(appEdit):

    global appCL
    global am
    
    import applicationClass as appCL
    import appMenu as am

    flag = False
    while flag == False:
        print('')
        print('')
        print('Please choose from the following menu for ', appEdit.title, ': ')
        print('______________________________________')
        print('')
        print('         0: Open Web Page') 
        print('         1: Show Data')
        print('         2: Edit Data')
        print('         3: Delete')
        print('         4: Return to Main Menu')
        print('______________________________________')
        print('')
        ans = input('Enter the number next to the chosen option: ')
        try:
            ans = int(ans)
        except:
            print('')
            print('Enter number characters only, no letters.')
        else:
            if ans not in (0, 1, 2, 3, 4):
                print('')
                print('Please choose only numbers from the menu. ')
            else:
                flag = True
    if ans == 0:
        import webbrowser as wb
        wb.open(appEdit.url, new=1)
    elif ans == 1:
        appEdit.show()
    elif ans == 2:
        appEdit = changeApp(appEdit)
    elif ans == 3:
        flag = False
        while flag == False:
            print('')
            print("Are you sure you want to remove ", appEdit.title, " and all ",
                  "it's contents? ")
            print('')
            ready = input('Enter <y> for yes or <n> for no: ')
            if ready == 'y':
                flag = True
                appEdit.remove()
                print('')
                print(appEdit.title, ' was deleted.')
                appEdit = 'n'
            elif ready == 'n':
                flag = True
                print('')
                print(' All data for ', appEdit.title, ' was retained.')
            else:
                print('')
                print('That is not a valid response.')
    elif ans == 4:
        appEdit = 'n'      

    return appEdit
            
            

def changeApp(appEdit):
    
    flag = False
    while flag == False:
        print('')
        print('')
        print('What do you want to edit?  Choose from the following menu: ')
        print('_____________________________________')
        print('')
        print('          1: Title')
        print('          2: url')
        print('          3: username')
        print('          4: password')
        print('_____________________________________')
        print('')
        ans = input('Enter the number next to the chosen option: ')
        try:
            ans = int(ans)
        except:
            print('')
            print('Enter number characters only, no letters.')
        else:
            if ans not in (1, 2, 3, 4):
                print('')
                print('Please choose only numbers from the menu. ')
            else:
                flag = True

    editDict = {
        1: 'title',
        2: 'url',
        3: 'username',
        4: 'password'
        }

    print('')
    if ans == 4:
        appEdit.remove()
        newPassword = am.addNewPass()
        appEdit.password = newPassword
        appEdit.record()

    elif ans == 1:
        appEdit.remove()
        print('')
        name = input('Enter the new application title: ')
        appEdit.title = name
        appEdit.record()

    elif ans == 2:
        appEdit.remove()
        print('')
        url = input('Enter the new application url: ')
        appEdit.url = url
        appEdit.record()

    elif ans == 3:
        appEdit.remove()
        print('')
        username = input('Enter the new application username: ')
        appEdit.username = username
        appEdit.record()

    return appEdit

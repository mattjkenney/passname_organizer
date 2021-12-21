#MAIN Program file
def main():
    
    global mn
    global pk
    global appFile
    global App
    global getpass
    global pc
    global wb
    global random
    global tkinter

    import pickle as pk
    from menu import menu as mn
    from applicationClassv2 import App
    import getpass
    import pyperclip as pc
    import webbrowser as wb
    import random
    import tkinter

    print('''
WELCOME TO YOUR PASSWORD MANAGER!

Save and recall your login data for all your accounts
in this app.  For utmost security, save all these files
to a usb drive where it can be locked in a safe space.
''')
    

    appFile = 'bahv2.pickle'

    data = setup()

    ch = main_menu(data)
    while ch != 'Exit Program':
        if ch == 'Access App by Name':
            app = appByName(data)
        elif ch == 'Add New App':
            app, data = create_app(data)
        elif ch == 'Choose from List':
            app = chooseApp(data)
        elif ch == 'Search':
            app = searchApp(data)
        data = search_handling(app, data)
        ch = main_menu(data)

    print('Goodbye!')

def main_menu(data):

    if data == {}:
        ops = (
            'Add New App',
            'Exit Program')
    else:
        ops = (
            'Access App by Name',
            'Add New App',
            'Choose from List',
            'Search',
            'Exit Program'
            )
    print('\nWelcome to the Main Menu!\n')
    chI = mn(ops)
    ch = ops[chI]

    return ch

def setup():

    try:
        file = open(appFile, 'rb')
    except:
        file = open(appFile, 'wb')
        data = {}
        pk.dump(data, file)
    else:
        data = pk.load(file)
    file.close()

    return data

def record_save(data, app):

    file = open(appFile, 'wb')
    new_dict = {app.title: app}
    data.update(new_dict)
    pk.dump(data, file)
    file.close()

    return data

def save(data):

    file = open(appFile, 'wb')
    pk.dump(data, file)
    file.close()

    return

def create_app(data):

    pin = getpass.getpass('\nEnter a pin number for future access to this data: ')
    title = input('\nEnter the app title: ')
    username = input('\nEnter the username: ')
    url = input('\nEnter the url: ')
    
    app = App(pin, title, url, username)
    app = password_menu(app)
    
    data = record_save(data, app)

    return app, data

def appByName(appDict):

    titles = tuple(appDict.keys())
    this_title = input('Enter the app title: ')
    flag = False
    for i in titles:
        if i.lower() == this_title.lower():
            flag = True
            app = appDict.get(i)
            
    if not flag:
        app = None

    return app

def appMenu_1(app, data):

    print('\nApp Menu\ntitle: ' + app.title)

    ops = (
        'Copy Login Data and Open Web Page',
        'Edit Login Data',
        'Return to Main Menu'
        )
    chI = mn(ops)
    ch = ops[chI]
    while ch != 'Return to Main Menu':
        if ch == 'Copy Login Data and Open Web Page':
            app, data = appMenu_2(app, data)
        elif ch == 'Edit Login Data':
            app, data = appMenu_3(app, data)
        if app.title in tuple(data.keys()):
            print('\nApp Menu\ntitle: ' + app.title)
            chI = mn(ops)
            ch = ops[chI]
        else:
            ch = 'Return to Main Menu'

    return data

def appMenu_2(app, data):

    print('\nApp Menu\ntitle: ' + app.title)

    ops = (
        'Copy Username',
        'Copy Password',
        'Open Web Page',
        'Return to Previous Menu'
        )
    chI = mn(ops)
    ch = ops[chI]
     
    while ch != 'Return to Previous Menu':
        if ch == 'Copy Username':
            pc.copy(app.username)
            print('\nUsername Ready!\n')
        elif ch == 'Copy Password':
            pc.copy(app.password)
            print('\nPassword Ready!\n')
            input('When ready, hit enter to clear the clipboard! ')
            pc.copy('')
        elif ch == 'Open Web Page':
            wb.open(app.url, new=1)
        print('\nApp Menu\ntitle: ' + app.title)
        chI = mn(ops)
        ch = ops[chI]
    pc.copy('')

    return app, data

def appMenu_3(app, data):

    edit_pin_msg = '''
To edit the pin, you must delete the app and re-create
it.
'''

    print('''
Editing Login Data here only affects the data stored
in this program.  To edit login data for the website
you use, you must also change the login information
using the applicable website's procedures.
''')

    ops = (
        'Show Data',
        'Edit Data',
        'Delete App',
        'Return to Previous Menu'
        )
    print('\nApp Menu\ntitle: ' + app.title)
    chI = mn(ops)
    ch = ops[chI]
    while ch != 'Return to Previous Menu':
        if ch == 'Show Data':
            app.show()
        elif ch == 'Edit Data':
            data.pop(app.title)
            edit_ops = tuple(app.as_dict().keys())
            edit_chI = mn(edit_ops)
            edit_ch = edit_ops[edit_chI]
            if edit_ch == 'password':
                app = password_menu(app)
            elif edit_ch == 'pin':
                print(edit_pin_msg)
            else:
                new_val = input('\nEnter the ' + edit_ch +': ')
                if edit_ch == 'title':
                    app.title = new_val
                elif edit_ch == 'url':
                    app.url = new_val
                elif edit_ch == 'username':
                    app.username = new_val
            data = record_save(data, app)
        elif ch == 'Delete App':
            this_ans = binary_response(
                '\nAre you sure you want to remove ' + app.title +\
                ' and all of its contents?', 'yes', 'y', 'no', 'n')
            if this_ans == 'y':
                data.pop(app.title)
                save(data)
                print('\nApp Deleted: ' + app.title + '\n')
            elif this_ans == 'n':
                print('\nApp is Saved.\n')
        if ch != 'Delete App':
            print('\nApp Menu\ntitle: ' + app.title)
            chI = mn(ops)
            ch = ops[chI]
        elif this_ans == 'y':
            ch = 'Return to Previous Menu'
        else:
            print('\nApp Menu\ntitle: ' + app.title)
            chI = mn(ops)
            ch = ops[chI]

    return app, data

def chooseApp(appDict):

    ops = list(appDict.keys())
    if ops != []:
        chI = mn(ops)
        ch = ops[chI]
        app = appDict.get(ch)
    else:
        app = None

    return app

def searchApp(appDict):

    titles = tuple(appDict.keys())
    this_key = input('Enter a key word to search: ')
    these_ops = []
    for i in titles:
        if this_key.lower() in i.lower():
            these_ops.append(i)
    if these_ops != []:
        chI = mn(these_ops)
        app = appDict.get(these_ops[chI])
    else:
        app = None

    return app

def binary_response(msg, ch1, ch1_resp, ch2, ch2_resp):

    flag = False
    while flag == False:
        print(msg)
        this_ch = input('\nEnter ' + ch1_resp + ' for ' + ch1 + '.' +\
                        '\nEnter ' + ch2_resp + ' for ' + ch2 + ': ')
        if (this_ch == ch1_resp) or (this_ch == ch2_resp):
            flag = True
        else:
            print('\nEnter only ' + ch1_resp + ' or ' + ch2_resp + '. ')
    return this_ch

def search_handling(app, data):

    if app != None:
        data = appMenu_1(app, data)
    else:
        print('\nThis app does not exist.\n')

    return data

def password_menu(app):

    ops = (
        'User Defined',
        'Auto Generate'
        )
    print('\nHow do you want to create a password?\n')
    chI = mn(ops)
    ch = ops[chI]

    if ch == 'User Defined':
        app = enter_pass(app)
    elif ch == 'Auto Generate':
        new_pass = password_generator()
        app.password = new_pass

    return app

def password_generator():

    msg_1 = '\nEnter the total number of characters for your password: '
    msg_2 = '\nEnter the total number of characters to be capitalized: '
    msg_3 = '\nEnter the total number of single digit numbers to be ' +\
            'included: '
    ss = 'abcdefghijklmnopqrstuvwxyz'
    total_char = return_int(msg_1)
    special_chars = special_check()
    cap_chars = return_int(msg_2)
    total_nums = return_int(msg_3)
    
    this_pass = []
    if special_chars == '':
        x = 0
    else:
        x = len(special_chars)        
    for i in range(total_char - x - total_nums):
        rI = random.randint(0, (len(ss) - 1))
        next_r = ss[rI]
        this_pass.append(next_r)
    for i in range(cap_chars):
        rI = random.randint(0, (len(this_pass) - 1))
        next_cap = this_pass[rI].upper()
        this_pass[rI] = next_cap
    for i in range(x):
        next_s = special_chars[i]
        rI_put = random.randint(1, (total_char - 1))
        if rI_put < len(this_pass):
            this_pass.insert(rI_put, next_s)
        else:
            this_pass.append(next_s)
    for i in range(total_nums):
        rI = random.randint(0,9)
        rI_put = random.randint(0, (total_char - 1))
        if rI_put < len(this_pass):
            this_pass.insert(rI_put, str(rI))
        else:
            this_pass.append(str(rI))
    new_pass = ''
    for i in this_pass:
        new_pass += i
        
    return new_pass

def return_int(msg):

    flag = False
    while flag == False:
        num = input(msg)
        try:
            num = int(num)
        except:
            print('\nEnter whole numbers only.')
        else:
            flag = True
    return num

def special_check():

    flag = False
    while flag == False:
        print('''
Enter the special characters needed for your password.
No spaces are allowed.  For instance, if you want to
include "!" and "*", just enter !*.
If no special characters are needed, simply hit <enter>
''')
        sp_char = input()
        if sp_char != '':
            if ' ' in sp_char:
                print('No apaces are allowed. ')
            else:
                flag = True
        else:
            flag = True
            
    return sp_char

def enter_pass(app):
    
    def close_pass():

        txt_entry = txt_box.get(1.0, "end-1c")
        ws.destroy()
        app.password = txt_entry
        return
     
    lab_msg = 'Enter password'
    lab_msg_len = len(lab_msg)
    box_len = '300x90'
    ws = tkinter.Tk()
    ws.title('Your Private Password!')
    ws.geometry(box_len)
    icon = tkinter.PhotoImage(file='write.png')
    ws.iconphoto(True, icon)

    frame1= tkinter.Frame(ws, padx=5, pady=5)
    frame1.grid(row=0, column=1)
    tkinter.Label(frame1, text=lab_msg).pack()
    txt_box = tkinter.Text(frame1,height=1, width=35)
    txt_box.pack()
    tkinter.Button(ws, text='Enter', command=close_pass).grid(row=1, columnspan=5, pady=5)
    ws.eval('tk::PlaceWindow . center')
    ws.attributes('-topmost', True)
    ws.update()
    ws.attributes('-topmost', False)
    ws.mainloop()

    return app
                             
main()

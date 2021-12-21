#Application CLASS FILE

class App():
    global tkinter
    global hashlib
    global getpass
    
    import tkinter
    import hashlib
    import getpass

    def __init__(
        self,
        pin,
        title=None,
        url=None,
        username=None,
        password='None'
        ):

        self.pin = pin
        self.title = title
        self.url = url
        self.username = username
        self.password = password
        
    def as_dict(self):

        appDict = {
            'pin': self._pin,
            'title': self._title,
            'url': self._url,
            'username': self._username,
            'password': self._password
            }

        return appDict

    def show(self):

        these = (
            'Title:        ' + self._title,
            'url:          ' + self._url,
            'username:     ' + self._username,
            )

        lengths = [len(i) for i in these]
        longest = max(lengths)
        line = '_' * (20 + longest) + '\n'

        print('')
        print(line)
        for i in these:
            print(' ' * 10 + i + ' ' * 10)
        print(line)
        input('Hit enter to view password. ')
        self.show_pass()

    def show_pass(self):

        def close():
            ws.destroy()
        
        p_s = self.password
         
        lab_msg = 'password: ' + p_s
        lab_msg_len = len(lab_msg)
        box_len = str(7*lab_msg_len) + 'x75'
        ws = tkinter.Tk()
        ws.title('Your Private Password!')
        ws.geometry(box_len)
        icon = tkinter.PhotoImage(file='show.png')
        ws.iconphoto(True, icon)

        frame1= tkinter.Frame(ws, padx=5, pady=5)
        frame1.grid(row=0, column=1)
        tkinter.Label(frame1, text=lab_msg).pack()
        tkinter.Button(ws, text='Close', command=close).grid(row=1, columnspan=5, pady=5)
        ws.eval('tk::PlaceWindow . center')
        ws.attributes('-topmost', True)
        ws.update()
        ws.attributes('-topmost', False)
        ws.mainloop()

    def pin_check(self):
        
        pin = getpass.getpass(prompt= 'Enter your pin for ' + self.title + ': ')
        pin_hash = hashlib.sha256(pin.encode()).hexdigest()
        if pin_hash == self.pin:
            b = True
        else:
            b = False
        return b

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, title):
        self._title = title

    @property
    def url(self):
        return self._url

    @url.setter
    def url(self, url):
        self._url = url

    @property
    def username(self):
        return self._username

    @username.setter
    def username(self, username):
        self._username = username

    @property
    def password(self):

        if self.pin_check():
            p_s = ''
            for i in self._password:
                p_s += i
            return p_s
        else:
            return 'wrong get pin'

    @password.setter
    def password(self, password):

        if self.pin_check():
            p = list(password)
        else:
            p = 'Wrong set Pin'
        self._password = p

    @property
    def pin(self):
        return self._pin

    @pin.setter
    def pin(self, pin):

        pin_hashed = hashlib.sha256(pin.encode()).hexdigest()
        self._pin = pin_hashed



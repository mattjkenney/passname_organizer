#Application CLASS FILE

class App():

    import os

    global loc2

    loc = os.path.dirname(os.path.abspath(__file__))
    loc2 = loc + '\\' + 'bah' + '.pickle'

    def __init__(self, title, url, username, password):
        
        self.title = title
        self.url = url
        self.username = username
        self.password = password

    def asdict(self):

        t = self._title
        u = self._url
        un = self._username
        p = self._password

        appDict = {
            'title': t,
            'url': u,
            'username': un,
            'password': p
            }

        return appDict


    def record(self):

        import pickle

        try:
            file = open(loc2, 'rb')
        except:
            file = open(loc2, 'wb')
            data = [self.asdict()]
            pickle.dump(data, file)
            file.close()
        else:
            data = pickle.load(file)
            newDict = [self.asdict()]
            newData = data + newDict
            file.close()
            file = open(loc2, 'wb')
            pickle.dump(newData, file)
            file.close()
            
        return

    def remove(self):

        import pickle

        file = open(loc2, 'rb')
        data = pickle.load(file)
        flag = False
        i = -1
        while flag == False:
            i += 1
            try:
                appDict = data[i]
            except:
                print('')
                print('This application is not listed in the Dictionary.')
                flag = True
            else:
                if appDict.get('title') == self._title:
                    data.pop(i)
                    flag = True
        file.close()
        file = open(loc2, 'wb')
        pickle.dump(data, file)
        file.close()


    def show(self):

        print('')
        print('______________________________________________________________________')
        print('')
        print('     Title                  ', self._title)
        print('     url                    ', self._url)
        print('     username               ', self._username)
        print('     password               ', self._password)
        print('______________________________________________________________________')
        print('')
        
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

        return self._password

    @password.setter
    def password(self, password):

        import random

        if password != 'r':
            self._password = password

        else:

            print("Let's make a password...")
            print('')
            print('')
            length = input('Enter the number of characters required: ')
            print('')
            print('')
            print('What special characters are required? Choose from the menu...')
            print('___________________________________________')
            print('')
            print('              0: default')
            print('              1: custom')
            print('___________________________________________')
            print('')
            print('')
            
            charMenu = input('Enter the code inside the <> signs for your choice: ')
            flag = False
            while flag == False:
                if charMenu == '0':
                    flag = True
                    sampleSpace = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%&*(){}:<>?[];.+=-_'

                elif charMenu == '1':
                    flag = True
                    print('')
                    print('')
                    char = input('Enter the special characters allowed with no spaces: ')
                    sampleSpace = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ' + char

                else:
                    print('')
                    print('That is not a valid response.')
                    charMenu = input('Enter the code inside the <> signs for your choice: ')

            
            passNew = ''
            for i in range(int(length)):

                r = random.randint(0, len(sampleSpace))
                passNew += sampleSpace[r]

            self._password = passNew






    

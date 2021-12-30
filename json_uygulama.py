import json
import os

class User:
    def __init__(self,username,password,email):
        self.username = username
        self.password = password
        self.email = email




class userRepository:
    def __init__(self):
        self.users = []
        self.isLoggedIn= False
        self.currentuser = {}

        self.loadUsers()

    def loadUsers(self):
        if os.path.exists('users.json'):
            with open('users.json','r',encoding='utf-8') as file:
                users = json.load(file)
                for user in users:
                    user = json.loads(user)
                    newUser = User(username = user['username'],password = user['password'], email = user['email'])
                    self.users.append(newUser)

    def register(self, user: User):
        self.users.append(user)
        self.savetoFile()
        print('kullanıcı oluşturuldu..')

    def login(self, username,password):

        
        for user in self.users:
            if user.username == username and user.password == password:
                self.isLoggedIn = True
                self.currentuser = user
                print('login yapıldı..')
                break
    def logout(self):
        self.isLoggedIn = False
        self.currentuser = {} 
        print('çıkış yapıldı..')     

    def identity(self):
        if self.isLoggedIn:
            print(f'username: {self.currentuser.username}')
        else:
            print('giriş yapılamadı')

    def savetoFile(self):
        liste = []
        
        for user in self.users:
            liste.append(json.dumps(user.__dict__))

        with open('users.json','w') as file:
            json.dump(liste, file)


repository = userRepository()

while True:
    print('menü'.center(50,'*'))
    secim = input('1- register\n2- login\n3- logout\n4- identity\n5- exit\nseçiminiz: ')
    if secim=='5':
        break
    else:
        if secim=='1':
            username = input('username: ')
            password = input('password: ')
            email = input('email: ')

            user = User(username=username, password = password,email=email)
            repository.register(user)
        elif secim=='2':
            if repository.isLoggedIn:
                print('zaten login oldunuz.')
            else:
                username = input('username: ')
                password = input('password: ')
                repository.login(username, password)
        elif secim=='3':
            repository.logout()
        elif secim=='4':
            repository.identity()
        else:
            print('yanlış seçim')


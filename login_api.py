#Author:liming
Count = 0
Path = 'C:\\Users\\李明\\PycharmProjects\\untitled\\s14\\day01_project\\'
Userfile = "username&password"
Lock_user = 'lock_user'

f_lock = open(Path+Lock_user, 'r')
User_lock_list = f_lock.readlines()
f_lock.close()

f_user = open(Path+Userfile, 'r')
Username_password = f_user.readlines()
f_user.close()

while True:
    Username = input("Please input your username:")
    Password = input("Please input your password:")
    if Username+'\n' in User_lock_list:
        print("The user has been locked ")
        break
    else:
        for i in Username_password:
            if i.split(" ")[0] == Username and i.split(" ")[1] == Password+'\n':
                print("welcome " + Username + " login")
                exit()
        else:
            print("username or password was wrong")
            Count += 1
    if Count >= 3:
        open(Path+Lock_user, 'a').writelines(Username+'\n')
        break


user_status = False
def login(auth_type): #qq

    def outer(func): #henan
        print(auth_type)
        def inner(*args,**kwargs): #3p
            _username = "denny"
            _password = "abc123"
            global user_status
            if user_status == False:
                username = input("user:")
                password = input("pasword:")

                if username == _username and password == _password:
                    print("welcome login....")
                    user_status = True
                else:
                    print("wrong username or password!")
            else:
                print("Login Permitted !")

            if user_status:
                func(*args,*kwargs) #3p

        return inner
    return outer



def home():
    print("---首页----")

def america():
    print("----欧美专区----")

@login('wx')
def japan(style):
    print("----日韩专区----",style)


@login('qq') # henan = login('qq')(henan) = inner
def henan(style):
    print("----河南专区----",style)

japan('oooo')
henan('xxxx')

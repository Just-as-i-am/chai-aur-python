#variable named arguments

def login(**kwargs):
    if "username" in kwargs and "password" in kwargs:
        print("Login Successful!")
        for key, value in kwargs.items():
            print(f"{key}:{value}")  
    else:
        print("Missing credentials")
    
 
login(username ="Eshaan", password="221")
login(username= "broooooooo")
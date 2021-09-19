import json

#data = json.loads(open("data.json", "r").read())
#user = "sami"
#password = "sami"
#data[user] = {"password":password}

def save():
  global data
  open("data.json", "w").write(json.dumps(data))

try:
    data = json.loads(open("data.json", "r").read())
except:
    open("data.json", "w").write(json.dumps({}))
    data = {}

user = input("Username: ")

password = input("Password: ")
if user in data:
    if password == data[user[password]]:
        print("welcome back")
else:
    print("no user")
    data[user] = {"username": user, "password": password}
    save()
    print("made new user with name", user)
last_login = {}
last_logout = {}
user_total_time = {}
with open("logs.txt") as f:

    for line in f:
        login, action, time = line.split(";")
        time = int(time)
        if action == "LOGIN" :
            last_login[login] = time
        elif action == "LOGOUT":
            user_total_time[login] = user_total_time.get(login,0) + time - last_login[login]
for user, time in sorted(user_total_time.items(), key = lambda x: x[1]):
    print(user, time)

print(last_login)
print(last_logout)
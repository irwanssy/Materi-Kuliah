#dictionary
userlogin1 = {  
    "nama"    : "Irwansyah",
    "role"    : "Admin",
    "email"   : "irwanh@gmail.com",
    "No.telp" : "0882001032640"
}

userlogin2 = {
    "nama"    : "Naruto",
    "role"    : "User",
    "email"   : "jkw@gmail.com",
    "No.telp" : "0882001032640"
}

for key,value in userlogin1.items():
    print(key, userlogin1[key])

for key in userlogin1:
    if key in userlogin2:
        if userlogin1[key] == userlogin2[key]:
            print(f"{key} sama")
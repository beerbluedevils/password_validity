#Password Strength Checker
#test git pull
#test git pull to feature1
#Input Password
password = input("Enter The Password : ")

#Count each characters
lower, upper, num, s_char = 0, 0, 0, 0
special = "!@#$%^&*()-_+=/\{}[]';,|:?"

#Count each char in password
for i in password:
    #lower
    if i.islower():
        lower += 1
    #upper
    if i.isupper():
        upper += 1
    #number
    if i.isdigit():
        num += 1
    #special char
    if i in special:
        s_char += 1

if (lower >= 1 and upper >= 1 and num >= 1 and s_char >= 1 and (lower+upper+num+s_char) >= 8):
    print("Your password is Strong!")
elif (lower >= 1 and upper == 0 and num == 0 and s_char == 0) and (lower+upper+num+s_char) >= 8:
    print("Your password is weak.")
elif (lower == 0 and upper >= 1 and num == 0 and s_char == 0) and (lower+upper+num+s_char)>= 8:
    print("Your password is weak.")
elif (lower == 0 and upper == 0 and num >= 1 and s_char == 0) and (lower+upper+num+s_char) >= 8:
    print("Your password is weak.")
elif (lower == 0 and upper == 0 and num == 0 and s_char >= 1) and (lower+upper+num+s_char) >= 8:
    print("Your password is weak.")
elif (lower >= 1 or upper >= 1 or num >= 1 and s_char >= 0) and (lower+upper+num+s_char) >= 8:
    print("Your password is medium.")
else:
    print("Your password is too short!")





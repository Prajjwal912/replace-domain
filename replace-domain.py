def replace_domain(email,old_domain,new_domain):
    if "@" + old_domain in email:
        index= email.index("@"+old_domain)
        new_email= email[:index]+ "@" + new_domain
        return new_email
    return email
domain=str(input("What is the old domain of your company?\n"))
while True:
    email= str(input("Enter employee email:\n"))
    old_domain=domain
    new_domain=input("What's the new domain of your company?\n")
    print("Congrats! Your new employee email id is " + str(replace_domain(email,old_domain,new_domain)))

#Merging Emails

with open("Names.txt","r") as n_file:
    with open ("Messages.txt","r") as m_file:

        body = m_file.read()
        for name in n_file:

            mail = "Hello " + name + body
            with open(name.strip() +".txt","w") as m_file:

                  m_file.write(mail)
    
print("All done, Messages created and ready, take a look in your directory")
print("---------------------------------------------------------------------")
print("Here is an example of the messages created \n")

with open("Dave.txt", "r") as daves:
    print(daves.read())

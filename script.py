"""
What is the script is generally for :
1.to add user
2.Add group
3.Add user to group
4.Create directory
5.Assign user & group ownership to directory
6.Test if user or dir exists , if not create it
7.SSH in python
8.Fabric library
9.webserver provisioning
10.python virtual environment
11.Python for other scripting tasks

!! This can easily be done using ainsible the automation tool
"""
import os

userlist = ["alpha", "beta", "gamma"]

print("Adding users to system ")
print("############################################")


# Loop to add user from userlist
for user in userlist:
    exitcode = os.system("id {}".format(user))
    if exitcode != 0:
        print("User does not exist. Adding it.".format(user))
        print("############################################")
        print()
        os.system("useradd {} ".format(user))
    else:
        print("User already exist , skipping it.")
        print("##################################")
        print()
    exitcode = os.system("grep science etc/group")
    # Condition to check whether a group exist or not . If it doesnt add it
    if exitcode != 0:
        print("Group science does not exist . Adding it.")
        print("###################################")
        print()
        os.system("groupadd science ")
    else:
        print("Group already exist . Just skippiong it")
        print("######################################")
        print()

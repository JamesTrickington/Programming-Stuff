def getFormattedName(firstName, lastName, middleName = ""):
    if middleName:
        fullName = "%s %s %s" %(firstName, middleName, lastName)
        fullName = fullName.title()
        fullName = fullName.strip()
    else:
        fullName = "%s %s" %(firstName, lastName)
        fullName = fullName.title()
        fullName = fullName.strip()
    return fullName

usrFN = raw_input("What is your FIRST name?*  ")
usrLN = raw_input("What is your LAST name?*  ")
usrMN = raw_input("What is your MIDDLE name?  ")

if usrLN and usrFN:
    if usrMN:
        print getFormattedName(usrFN, usrLN, usrMN)
    else:
        print getFormattedName(usrFN, usrLN)
else:
    print "Sorry, you must enter a first and last name."
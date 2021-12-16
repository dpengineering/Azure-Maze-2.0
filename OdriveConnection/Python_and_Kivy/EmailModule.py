import GetEmail
from GetEmail import getMail
from SendMail import sendMail
from time import sleep
import random
subject = ' '
print(("STARTING THE PROJECT EMAIL SENSING< MIGHT BREAK< "))
def checkforEmail(username, password, targetbody, responsesubject, responsebody, bool):
    global subject
    getMail(username, password, 1)
    #sleep(1)
    try:
        if targetbody in GetEmail.passAndCommand[2].lower() and GetEmail.passAndCommand[1] != subject:
            sendMail(username, password, str(GetEmail.passAndCommand[0]), responsesubject, responsebody)
            print('sent response', responsesubject + ',\n' + responsebody, 'to', GetEmail.passAndCommand[0], '\ntarget=',targetbody)
            sendMail("dpeastudent7266", "dpea7266!?", "kineticmaze@gmail.com", "ERR_BLOCKING", "BLOCKING_MESSAGE_ANTI_SPAM")
            subject = GetEmail.passAndCommand[1]
            if bool == True:
                return True
            else:
                pass
        else:
            pass
    except Exception as e:
        print(e, 'in checkforEmail')
    GetEmail.passAndCommand.clear()

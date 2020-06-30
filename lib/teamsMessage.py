import pymsteams
import json

def sendMessage(hook, text):
    message = pymsteams.connectorcard(hook)
    message.text(text)

    myMessageSection = pymsteams.cardsection()
    myMessageSection.title("Section title")
    myMessageSection.activityTitle("my activity title")
    myMessageSection.activitySubtitle("my activity subtitle")
    myMessageSection.activityImage("http://i.imgur.com/c4jt321l.png")
    myMessageSection.activityText("This is my activity Text")
    myMessageSection.addFact("this", "is fine")
    myMessageSection.addFact("this is", "also fine")
    myMessageSection.text("This is my section text")
    myMessageSection.addImage("http://i.imgur.com/c4jt321l.png", ititle="This Is Fine")
    message.addSection(myMessageSection)

    message.send()

def grabEntries(fileName):
    hookList = []
    opened = open(fileName, "r")
    currentLine = opened.readline()
    while currentLine:
        hookList.append(currentLine.rstrip())
        currentLine = opened.readline()
    return hookList

def sendFromDirectory(fileName, text):
    hookList = grabEntries(fileName)
    print(hookList)
    for x in hookList:
        try:
            sendMessage(x, text)
        except:
            print("The message failed to send to the Webhook at " + x)


# Directory Editing & Handling
def checkForString(fileName, string):
    with open(fileName) as f:
        if string in f.read():
            f.close()
            return True
    f.close()
    return False

def addHookToDirectory(fileName, newHook):
    if checkForString(fileName, newHook):
        print("Hook already exists")
        return
    openFile = open(fileName, "a")
    openFile.write("\n" + newHook)
    openFile.close()
    return

def removeHook(fileName, hookToRemove):
    if not checkForString(fileName, hookToRemove):
        print("That hook does not exist")




# sendFromFile("hooks.txt", "Test Message -> Read from file")
# print(grabEntries("hooks.txt"))


sendMessage("https://outlook.office.com/webhook/d262c1e6-4556-40c1-a740-9d4154da9b3e@7b65f535-32b5-4d73-9282-1c761c779561/IncomingWebhook/70c931703e024464a7fe048c486f6e6c/7f2e5c23-c925-47a1-9d8c-644326c2a1d4", "top level text")
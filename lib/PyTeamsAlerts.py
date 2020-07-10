import pymsteams
import json

data = {}
data['sample_list'] = ["1", "2", "3"]

with open("hooks.json", "w") as json_file:
    json.dump(data, json_file)

with open("hooks.json") as json_file:
    newData = json.load(json_file)

for x in newData['sample_list']:
    print(x)

def sendMessage(hook, text):
    message = pymsteams.connectorcard(hook)
    message.text(text)
    message.send()

def pullList(fileName):
    with open(fileName) as json_file:
        data = json.load(json_file)
    return data

def pushList(fileName, data):
    with open(fileName, "w") as json_file:
        json.dump(data, json_file)

def sendFromDirectory(fileName, text):
    hooks = pullList(fileName)
    for x in hooks:
        try:
            sendMessage(x, text)
        except:
            print("The message failed to send to the Webhook at " + x)

def addHookToDirectory(fileName, newHook):
    hooks = pullList(fileName)
    for x in hooks:
        if x == newHook:
            print("That hook already exists.")
            return
    hooks.append(newHook)
    return




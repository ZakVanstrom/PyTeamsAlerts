import pymsteams

def sendAlert(hooks, title, text):
    for x in hooks:
        try:
            message = pymsteams.connectorcard(x)
            message.title(title)
            message.text(text)
            message.send()
        except:
            print("The message failed to send to the Webhook at " + x)
    return
import pymsteams

def sendAlert(hooks, title, text):
    if isinstance(hooks, str):
        try:
            message = pymsteams.connectorcard(hooks)
            message.title(title)
            message.text(text)
            message.send()
        except:
            print("The message failed to send to the Webhook at " + hooks)
        return
    for x in hooks:
        try:
            message = pymsteams.connectorcard(x)
            message.title(title)
            message.text(text)
            message.send()
        except:
            print("The message failed to send to the Webhook at " + x)
    return
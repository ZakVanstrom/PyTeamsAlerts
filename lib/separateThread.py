import pymsteams

def sendAlert(hooks, title, text):
    if isinstance(hooks, str):
        try:
            message = pymsteams.connectorcard(hooks)
            message.title(title)
            message.text(text)
            message.send()
        except pymsteams.TeamsWebhookException:
            print("The message failed to send to the Webhook at " + hooks)
            status_code = message.last_http_status.status_code
            print(status_code)
        return
    if isinstance(hooks, list):
        for x in hooks:
            try:
                message = pymsteams.connectorcard(x)
                message.title(title)
                message.text(text)
                message.send()
            except pymsteams.TeamsWebhookException:
                print("The message failed to send to the Webhook at " + x)
                status_code = message.last_http_status.status_code
                print(status_code)
        return
    else:
        print("WEBHOOK (first argument) is not a valid LIST OF STRINGS or STRING")
        return
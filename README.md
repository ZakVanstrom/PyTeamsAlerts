# Teams Alerts for Python

Python wrapper to send requests to Microsoft Teams Webhooks.

Application of library from PyMsTeams to simplify and integrate easily. 
    [Pymsteams GitHub](https://github.com/rveachkc/pymsteams)

This library uses Webhook Connectors for Microsoft Teams.  Please visit the following Microsoft Documentation link for instructions on how to obtain the correct url for your Channel: 
    [Microsoft WebHooks Documentation](https://dev.outlook.com/Connectors/GetStarted#creating-messages-through-office-365-connectors-in-microsoft-teams)
 
Please refer to the Microsoft Documentation for the most up to date screenshots. 
    [Teams Connectors Reference](https://dev.outlook.com/connectors/reference)

# Simple Use -> Without installing modules

## Simple Setup

This script simplifies pymsteams to streamline & standardize Microsoft Teams alerts

### 1st

Install pymsteams with pip:

```bash
pip install pymsteams
```

### 2nd
In your function definitions, drop the following def:

```python
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
```

## Simple Usage
 
Use sendAlert(hooks, title, text) to send a message. 

You must have a WEBHOOK (it's a URL) from the channel you're sending to. You must insert the WebHook into the hooks argument, which can be a list of strings or a single string

The title and text both accept any string. 

```python
import TeamsAlert

# sendAlert(hooks, title, text) --->   Single Hook Example (to send to a single channel)

TeamsAlert.sendAlert("https://outlook.office.com/webhook/asdfasdf/IncomingWebHook", "Example Title", "Example Text")


# sendAlert(hooks, title, text) --->   Multiple Hook Example (to send to multiple channels)

ListOfHooks = ["https://outlook.office.com/webhook/fdsafdsa/IncomingWebHook", "https://outlook.office.com/webhook/asdfasdf/IncomingWebHook"]

TeamsAlert.sendAlert(ListOfHooks, "Example Title", "Example Text")

```

# Demo
### Note : *Real WebHooks are much longer and should be kept confidential*
They're a direct link for anyone to message a channel

## PyCharm IDE - Working Code

![Working Code](https://github.com/ZakVanstrom/PyTeamsAlerts/blob/master/misc/Real-Example.png)

## Received Message in Microsoft Teams

![Example of Alert](https://github.com/ZakVanstrom/PyTeamsAlerts/blob/master/misc/Alert%20Example.png)

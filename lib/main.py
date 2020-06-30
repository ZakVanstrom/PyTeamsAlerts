import TeamsAlert

# teamsMessage.sendFromDirectory("hooks.txt", "Test Message -> Read from file, from a main file. Test 2 with Error Handling")

# teamsMessage.addHookToDirectory("hooks.txt", "this is a line")
#
# newDB = ToyDB.ToyDB("webhook_storage.json")
# randomNumber = random.randint(1, 500)
#
# for x in range(0, 10):
#     randomNumber = random.randint(1, 5000)
#     newDB.set(randomNumber, randomNumber)
#
# for x in newDB.db:
#     print(newDB.db[x])

TeamsAlert.sendAlert("https://outlook.office.com/webhook/d262c1e6-4556-40c1-a740-9d4154da9b3e@7b65f535-32b5-4d73-9282-1c761c779561/IncomingWebhook/70c931703e024464a7fe048c486f6e6c/7f2e5c23-c925-47a1-9d8c-644326c2a1d4", "test", "test text")
import json
from watson_developer_cloud import ConversationV1


conversation = ConversationV1(
    username='c68b470e-8a3c-4ce6-b7f9-69f5817f9241',
    password='QfsnOvJYW7dB',
    version='2016-09-20')

text = raw_input()
context = {}
response = conversation.message(workspace_id="5e6af393-75af-4272-be17-b63211195bca", message_input={
    'text': text})

print(json.dumps(response, indent=2))
import json

def scrap(pathway):
    canada = False

    with open(pathway) as f:
        data = json.load(f)
    
    # we know the json field in which the messages are found is: 'messages'
    for i in range(len(data['messages'])):
        for key in data['messages'][i]:
           if key == 'content':
              if 'Canada' in data['messages'][i][key] or 'canada' in data['messages'][i][key]:
                 #print('Canada found!')
                 #print('Text:',data['messages'][i][key])
                 canada = True
                 break
    return canada
  
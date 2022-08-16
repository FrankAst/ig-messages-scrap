import os
import function


path = '/media/frank/Elements/pinkpanda/Influencers/INF_analysis/inbox/'

listdir = os.listdir(path)
canadian = []

for file in listdir:
    pathw = path + file + '/message_1.json'
     
    if function.scrap(pathw):
        canadian.append(file)
        

print('total influencers revised:',len(listdir))
print('total infl from canada:',len(canadian))        
print('\n')
print(canadian)

with open(r'/media/frank/Elements/pinkpanda/Influencers/INF_analysis/results.txt', 'w') as fp:
    for item in canadian:
        #write each item on a new line
        fp.write("%s\n" %item)
    print('Done')



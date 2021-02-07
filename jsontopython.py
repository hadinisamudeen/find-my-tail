#Using the contents of the JSON file 
import json
jsonfile = open('filename.json','r')
userdata = jsonfile.read()
X_test = json.loads(userdata)

if x_test['where'] == 'indoor':
    x_test['where'] = 0
else:
    x_test['where'] = 1
    
if x_test['season'] == 'spring':
    x_test['season'] = 0
elif x_test['season'] == 'summer':
    x_test['season'] = 1
elif x_test['season'] == 'autumn':
    x_test['season'] = 2
else:
    x_test['season'] = 3
    
if x_test['occasions'] == 'other':
    x_test['occasions'] = 0
elif x_test['occasions'] == 'christmas':
    x_test['occasions'] = 1
elif x_test['occasions'] == 'holiday':
    x_test['occasions'] = 2
else:
    x_test['occasions'] = 3
    
X_test = np.array([X_test['sad_happy'],X_test['stressed_relaxed'],
                   X_test['lonely_romantic'],X_test['couchpotato_party'],X_test['where'],
                   X_test['season'],X_test['occasions']])

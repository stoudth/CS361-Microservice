import requests
import random

def choose_ppt():
    """Generates a random person, place, or thing using APIs."""
    ppt_choice = random.randrange(0, 3)
    if ppt_choice == 0:
        while True:
            rando = requests.get('https://random-word-form.herokuapp.com/random/noun')
            r = requests.get('https://api.dictionaryapi.dev/api/v2/entries/en/' + str(rando.json()[0]))
            if 'title' not in r.json():
                if r.json()[0]['meanings'][0]['partOfSpeech'] == 'noun':
                    return 'thing', rando.json()[0]
    elif ppt_choice == 1:
        while True:
            data = requests.get('http://geodb-free-service.wirefreethought.com/v1/geo/cities?hateoasMode=off')
            number = random.randrange(0, data.json()['metadata']['totalCount']-1)
            single = requests.get('http://geodb-free-service.wirefreethought.com/v1/geo/cities?limit=1&offset=' + str(number) + '&hateoasMode=off')
            place = random.randrange(0, 2)
            location = ''
            if place == 0:
                location = single.json()['data'][0]['city']
            else:
                location = single.json()['data'][0]['country']
            if location != '':
                return 'place', location
    else:
        while True:
            api_url2 = 'https://api.api-ninjas.com/v1/randomuser'
            response = requests.get(api_url2, headers={'X-Api-Key': 'Ae5uvvzxI0w9xuKKgqdcmg==ilSe5G7wHx1QF5Dt'})
            name = response.json()['name']
            new_name = ''
            index = 0
            while index < len(name) and name[index] != ' ':
                new_name += str(name[index])
                index += 1
            api_url = 'https://api.api-ninjas.com/v1/celebrity?name='+ str(new_name)
            response = requests.get(api_url, headers={'X-Api-Key': 'Ae5uvvzxI0w9xuKKgqdcmg==ilSe5G7wHx1QF5Dt'})

            for num in range(len(response.json())):
                rand_entry = random.randrange(0, len(response.json())-1)
                for key in response.json()[rand_entry]:
                    if key == 'occupation':
                        person = response.json()[rand_entry]['name']
                        person = person.title()
                        return 'person', person

while True:
    with open('SpinToWinInput.txt', 'r+') as input_file:
        input = input_file.readline()
        if input == 'get':
            input_file.seek(0)
            input_file.truncate()
            input_file.close()
            return_value = choose_ppt()
            with open('SpinToWinOutput.txt', 'w') as output_file:
                output_file.write(str(return_value))
                output_file.close()
        input_file.close()


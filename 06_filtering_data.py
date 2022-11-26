data = [
    {
        'name':'Dami',
        'age':27,
        'organization': 'Brainfood',
        'position': 'Data Engineer',
        'lenguage': 'python'
    },
    {
        'name':'Trini',
        'age':25,
        'organization': 'Cleary',
        'position': 'Software developer',
        'lenguage': 'ruby'
    },
    {
        'name':'Agustin Gomez',
        'age':29,
        'organization': 'Cleary',
        'position': 'Software developer',
        'lenguage': 'ruby'
    },
    {
        'name':'Marce',
        'age':56,
        'organization': 'Self-employed',
        'position': 'Psychologist',
        'lenguage': 'mind reading'
    }
]

def run():
    python_devs = [person['name'] for person in data if person['lenguage']=='python']
    all_youngs = [person.get('name') for person in data if person['age']<30]
    adults_objs = list(filter(lambda worker: worker['age']>18,data))
    adults = list(map(lambda worker: worker['name'], adults_objs))
    old_ppl = list(map(lambda worker: worker | {'old': worker['age']>70}, data))
    print(f'These know python:\n{python_devs}')
    print(f'These are young:\n{all_youngs}')
    print(adults)
    print(old_ppl)  #notice how there's a new 'old' attribute


if __name__ =='__main__':
    run()
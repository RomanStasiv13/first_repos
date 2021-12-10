import json

contact_book = {}
contact_book['title'] = 'Phone book'
contact_book['contacts'] = [
    {'name': 'michael',
     'surname': 'mayers',
     'full name': 'michael mayers',
     'number': '0961313131',
     'state': 'USA'},
    {'name': 'jason',
     'surname': 'voorhees',
     'full name': 'jason voorhees',
     'number': '0666666666',
     'state': 'Australia'},
    {'name': 'freddy',
     'surname': 'krueger',
     'full name': 'freddy krueger',
     'number': '0736661366',
     'state': 'Germany'},
]
with open('contact_book.json', 'w') as file_object:
    json.dump(contact_book, file_object)




# Write a Python program to count the values associated with key in a dictionary. Go to the editor
Sampledata = [{'id': 1, 'success': True, 'name': 'Lary'}, {
    'id': 2, 'success': False, 'name': 'Rabi'}, {'id': 3, 'success': True, 'name': 'Alex'}]
count = 0
for i in Sampledata:
    if 'success' in i.keys():
        if i['success'] == True:
            count += 1

print(count)

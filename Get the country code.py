Country_code = {'India' : '0091',
                'Aus':'0025',
                'BD':'0088',}

print('Country code for India is:', )
print(Country_code.get('India', 'Not found'))

print('Country code for Japan is:', )
print(Country_code.get('Japan', 'Not found'))

print('Country code for Bangladesh is:', )
print(Country_code.get('BD', 'Not found'))
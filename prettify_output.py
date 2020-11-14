import string
from random import choice
from pprint import pprint
from tabulate import tabulate
from operator import itemgetter


devices = []
addresses = []

for i in range(1, 21):
    device = {
        'hostname': (choice(string.ascii_letters) +
                     choice(string.ascii_letters) +
                     choice(string.ascii_letters) +
                     choice(string.ascii_letters) +
                     choice(string.ascii_letters)),
        'ip': '10.0.0.' + str(i),
        'os': choice(['ubuntu', 'redhat', 'windows'])
    }
    if device['os'] == 'ubuntu':
        device['version'] = choice(['16.04', '18.04', '20.04'])
    elif device['os'] == 'redhat':
        device['version'] = choice(['6', '7', '7.1', '7.2', '8'])
    elif device['os'] == 'windows':
        device['version'] = choice(['2012r2', '2016', '2019'])

    addresses.append(device['ip'])
    devices.append(device)

print('# Display all IPs')
print(addresses)
print('')

print('# Pretty display all IPs using pprint')
pprint(addresses, width=-1)
print('')

print('# Display a device information')
print(devices[0])
print('')

print('# Pretty display a device using pprint')
pprint(devices[0], width=-1)
print('')

print('# Display a list of all device')
print(devices)
print('')

print('# Pretty display a list of all devices using pprint')
pprint(devices, width=-1)
print('')

print('# Pretty display a list of all devices using dict.items() and F-strings')
for device in devices:
    for key, value in device.items():
        print(f'{key:>10s}: {value}')
    print('-' * 30)

print('# Pretty display a list of all devices using tabulate and itemgetter')
tabular_output = tabulate(sorted(devices, key=itemgetter('os', 'version')), headers='keys')
print(tabular_output)

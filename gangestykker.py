import random
import timeit
import sys
msg = ''

teller = 0
response = 0
svar = 'j'
riktig = 0


def gange(a, b):
    return a * b


# print(sys.executable)

antall = int(input('Hvor mange stykker vil du ha? '))
# if (type(antall)) == 'Int':
#    print('int')

#print('Antall regnestykker er {}'.format(antall))
start_time = timeit.default_timer()

while teller < antall:
    a = random.randint(1, 10)
    b = random.randint(1, 10)
    response = int(input('\t{} x {} ='.format(a, b)))
    teller += 1
    if gange(a, b) == response:
        riktig += 1
end_time = timeit.default_timer()

if riktig == antall:
    msg = 'Hurra!'
print('-' * 40)
print(msg + 'Antall riktige ble {} av {}'.format(riktig, antall))
print(start_time)
print(end_time)
# print 'runtime: %ss' % (end_time - start_time)
#time_used = end_time - start_time
time_used = (round(end_time - start_time, 2))
print('Du brukte {} sekunder på {} stykker!'.format(time_used, antall))
print('fin')

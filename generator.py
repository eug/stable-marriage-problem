# Generates random instances for the problem
import sys
import random

qwert = sorted(list('qwertyuiopasdfghjklzxcvbnm'))
l = qwert
u = list(map(lambda x: x.upper(), qwert))

sys.stdout.write('26\n')
sys.stdout.write(' '.join(l) + ' ' + ' '.join(u) + '\n')

for m in l:
    sys.stdout.write(m + ':')
    
    random.shuffle(u)
    for w in u:
        sys.stdout.write(w)
    sys.stdout.write('\n')

for w in sorted(u):
    sys.stdout.write(w + ':')
    
    random.shuffle(l)
    for m in l:
        sys.stdout.write(m)
    sys.stdout.write('\n')
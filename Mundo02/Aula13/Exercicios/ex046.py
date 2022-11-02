
from time import sleep

txt = ['Exercício 46','Contagem Regressiva']

print('='*35)
print('{:^35}'.format(txt[0]))
print('='*35)
print('{:^35}'.format(txt[1]))
print('='*35)

for cont in range(10,-1,-1):
    num = ['0','1','2','3','4','5','6','7','8','9','10']
    sleep(1)
    print('{:^35}'.format(num[cont]))

print('='*60)

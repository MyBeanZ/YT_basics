
""" trojte uvozovky """
'''
print(
"""skdfjksdjf

dlskfjksldfj
lksdjfkll""")

print(len("\N{SNOWMAN}"))

#vyber znaku'

print("neco ksdlfjlk"[:3]) '''

""" zmena pismena ve slove """
"""
slovo = input("zadej slovo:")
pozice = int(input("kterou pozici:"))
pismeno = input("jake pismeno:")
nove = slovo[:pozice] + pismeno +slovo[(pozice + 1):]
print("nove slovo: {}".format(nove))
"""
word = 'word'
for i in word:
    print(i)

if ('wo' in word):
    print('is here')

soucet = 34
print('soucet je:', soucet)
a = 4 + 5
format_str = f'neco {a},f skl {soucet}'
print(format_str)

sablona = 'ahoj:" {b} ,dsfsdf P`{c}'
print(sablona)
print('\033[1;33m=-=' * 8)
n = int(input('\033[1;34mGigite a tabuada deseja: \033[m'))
print('\033[1;33m=-=' * 8)
for c in range(1,11):
        print('\033[36m{} x {} = \033[1;33m{}  '.format(n,c,n * c))


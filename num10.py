a=open('inputt.txt', encoding='utf-8')

l=a.readlines()
print(l)

gl=['у', 'е', 'ы', 'а', 'о', 'э', 'ю', 'и', 'я']
z=[]
for g in l:
    for h in g.split():
        z.append(h)
for i in range(len(z)):
    for c in gl:
        z[i].replace(c, )
        
a.close()
        


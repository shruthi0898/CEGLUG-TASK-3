import csv

numbers = open('number.csv','r')
readn = csv.reader(numbers)

fruits = open('fruits.csv','r')
readf = csv.reader(fruits)

price = open('price.csv','r')
readp = csv.reader(price)

rotten = open('rotten.csv','r')
readr = csv.reader(rotten)

for row in readn:
    n=row

for row in readf:
	f=row

for row in readp:
    p=row

for row in readr:
    r=row

fl=[]
for i in range(100):
	if n[i]=="":
		if i%2==0:
			continue
		else:
			n[i]==i
	if f[i]=="":
		if i+10 < 100:
			f[i]=f[i+10]
		else:
			f[i]="Berry"
	if r[i]=="0":
		r[i]="False"
	if r[i]=="f":
		r[i]="False"
	if r[i]=="1":
		r[i]="True"
	if r[i]=="t":
		r[i]="True"
	if p[i]=="":
		if r[i]=="False":
			p[i]="0.00"
	if p[i].find(".")==-1:
		p[i]=p[i]+".00"
	l=[n[i],f[i],p[i],r[i]]
	fl.append(l)

csvfile = open('data.csv','w')
writer = csv.writer(csvfile, delimiter=',')
fieldnames = ['Number','Fruit','Price','Rotten']
writer.writerow(fieldnames)
for r in fl:
    writer.writerow(r)
csvfile.close()
import sys
import re


encutf8 = '"utf-8"'
encwin1251 = '"windows-1251"'
enckoi = '"koi8-r"'
encglob = '"utf-8"'

lost = [] #Список слов короновирус
covi = [] #Список слов covid
allw = [] #Список всех слов в документе
epic = [] #Список слов пандемия и эпидемия



c = "index.html"


f = open(c)

if f:
	r = f.readlines()


p = re.compile(r'[Кк]{1,1}ор[ао]{1,1}нав[iи]{1,1}рус[омау]{0,5}')
z = re.compile(r'[Cc]{1,1}[Oo]{1,1}[Vv]{1,1}[Ii]{1,1}[Dd]{1,1}')
v = re.compile(r'\b[А-Яа-я]{3,25}\b')
b = re.compile(r'[панэиe]{3,3}деми')

for s in r:
	
	x = p.findall(s)
	t = z.findall(s)
	u = v.findall(s)
	j = b.findall(s)
	lost.extend(x)
	covi.extend(t)
	allw.extend(u)
	epic.extend(j)
	

anum = len(lost)+len(covi)+len(epic)
fino = len(allw)/100
resw = anum/fino


print(lost)
print(covi)
print(epic)
print("CODIV-вирусная нагрузка страницы состовляет ",resw,"%")
f.close()



# -*- coding: utf-8 -*-
"""
Created on Fri Nov  4 15:14:45 2022

@author: tasu
"""

capital = {
'Uzbekistan':'Tashkent',
'Korea':'SEul',
'Rusiia':'Moscow',
'AQSH':'Washington'
}

poytaxt='\nDunyo poytaxtlari:'
print(poytaxt)
#for value in sorted(capital.values()):
   # print(value.title()) 
davlat= input('Which capital of country do you want know?\n')
poytaxt = capital.get(davlat)
if poytaxt == None:
        print('Sorry, not found')
else:
        print(f"{davlat.upper()}ning poytaxti {poytaxt.title()} shahri ")
        
   
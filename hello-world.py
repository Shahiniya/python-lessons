# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
#progs = ['python','css','html','react','js']
#for prog in progs:
    # print(f"Salom {prog}")
  
capital = {
'Uzbekistan':'Tashkent',
'Korea':'SEul',
'Rusiia':'Moscow',
'AQSH':'Washington'
}

#davlat = 'Dunyo davlatlari:'
#print(davlat)
#for key in sorted(capital.keys()):
  #  print(key.title())
    
#poytaxt='\nDunyo poytaxtlari:'
#print(poytaxt)
#for value in sorted(capital.values()):
  # print(value.title()) 
   
##poytaxt = capital.get(davlat)
#if poytaxt == None:
       # print('Sorry, not found')
#else:
        #print(f"{davlat.upper()}ning poytaxti {poytaxt.title()} shahri ")
    
car0 = {
        'model':'Tesla',
        'color':'red',
        'year':'2023',
        'korobka':'avtomat'
        }
car1 = {
        'model':'Tesla',
        'color':'red',
        'year':'2023',
        'korobka':'avtomat'
        }
car2 = {
                'model':'Tesla',
                'color':'red',
                'year':'2023',
                'korobka':'avtomat'
                }

cars = [car0,car1,car2]
for car in cars:
    print(
        f"{car['model'].title()},"
        f"{car['color']}"
        )
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  7 12:03:57 2022

@author: tasu
"""

# =============================================================================
# print(f"Kiritilgan sonni kvadratini qaytaruvchi dastur!")
# savol = 'Son kiriting!'
# savol += "Dasturni to'xtatish uchun 'exit' deb yozing!"
# =============================================================================
# qiymat = ''
# =============================================================================
# while  qiymat != 'exit':
#     qiymat = input(savol)
#     if qiymat != 'exit':
#         print(float(qiymat)**2)
# print('Dastur tugadi!')
# =============================================================================


# =============================================================================
# while  True:
#     qiymat = input(savol)
#     if qiymat == 'exit':
#         break
#     else:
#         print(float(qiymat)**2)
# print('Dastur toxtadi')
# =============================================================================

# =============================================================================
# sonlar = list(range(1,11))
# for son in sonlar:
#     if son == 5:
#         break
#     else:
#         print(f"{son}ning kvadrati {son**2} ga teng!")
# =============================================================================
# =============================================================================
# sonlar = list(range(1,11))
# for son in sonlar:
#     if son == 5:
#         continue
#     else:
#         print(f"{son}ning kvadrati {son**2} ga teng!")
#         
#         
# ====================================================================

def salom_ber(ism):
    """Salom beruvchi"""
    print(f"Assalomu alaykum {ism.lower()} ")


salom_ber("Olim")
        
        
def yosh_hisobla(t_yil,joriy_yil=2022):
    """Yosh hisoblash"""
    print(f"Siz {joriy_yil-t_yil} yoshdasiz")
yosh_hisobla(1989)       
        
        
def avto_info(model,rangi,yili,narxi=None):
    """avto ma'lumot"""
    avto={
        'model':model,
        'rangi':rangi,
        'yili':yili,
        'narxi':narxi
        }
    return avto

avto1 = avto_info('Tesla','qizil',2022)
avto2 = avto_info('Volvo','qizil',2023,25000)
avtolar=[avto1,avto2]
print(f"Uzbekistandagi mavjud avtolar:")
for avto in avtolar:
    if avto['narxi']:
        narxi = avto['narxi']
    else:
        narxi='None'
    print(f"{avto['model']} {avto['rangi']} Narxi:{narxi} ")
        
        
        
        
        
        
        
        
        
        
        
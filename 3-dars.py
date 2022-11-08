# -*- coding: utf-8 -*-
"""
Created on Mon Nov  7 12:03:57 2022

@author: tasu
"""

print(f"Kiritilgan sonni kvadratini qaytaruvchi dastur!")
savol = 'Son kiriting!'
savol += "Dasturni to'xtatish uchun 'exit' deb yozing!"
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
sonlar = list(range(1,11))
for son in sonlar:
    if son == 5:
        continue
    else:
        print(f"{son}ning kvadrati {son**2} ga teng!")
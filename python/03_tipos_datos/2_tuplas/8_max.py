# jade rojas
# 22-04-2025

# max en tuplas

tupla = (1, 2, 3, 4, 5)
print(tupla) # (1, 2, 3, 4, 5)
print(type(tupla)) # <class 'tuple'>
print(max(tupla)) # 5
print(max(tupla, key=lambda x: x)) # 5
print(max(tupla, key=lambda x: -x)) # 1
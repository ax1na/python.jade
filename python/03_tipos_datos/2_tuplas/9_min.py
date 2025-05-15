# jade rojas
# 22-04-2025

# min en tuplas

tupla = (1, 2, 3, 4, 5)
print(tupla) # (1, 2, 3, 4, 5)
print(type(tupla)) # <class 'tuple'>
print(min(tupla)) # 1
print(min(tupla, key=lambda x: x)) # 1
print(min(tupla, key=lambda x: -x)) # 5
# jade rojas 22-04-2025

# Sorted en tuplas

tupla = (5, 4, 3, 2, 1)
print(tupla) # (5, 4, 3, 2, 1)
print(type(tupla)) # <class 'tuple'>
print(sorted(tupla)) # [1, 2, 3, 4, 5]
print(sorted(tupla, reverse=True)) # [5, 4, 3, 2, 1]
print(sorted(tupla, key=lambda x: x)) # [1, 2, 3, 4, 5]
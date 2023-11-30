"""
Crea una función que encuentre todos los triples pitagóricos
(ternas) menores o iguales a un número dado.

  - La función únicamente recibe el número máximo que puede
    aparecer en el triple.

  - Ejemplo: Los triples menores o iguales a 10 están
    formados por (3, 4, 5) y (6, 8, 10).
"""

num = 10

def triple_pitagorico(num):
    
    a = num
    b = num 
    c = num
    triple_pitagorico_list = []

    for ai in range(1, a+1):
        s_ai = ai**2
        for bi in range(1, b+1):
            s_bi = bi**2
            for ci in range(1, c+1):
                s_ci = ci**2
                suma = s_ai + s_bi
                if suma == s_ci:
                    t = (ai, bi, ci)
                    triple_pitagorico_list.append(t)    

    return triple_pitagorico_list

print(triple_pitagorico(num))

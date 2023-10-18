# Add Two Numbers: You are given two non-empty linked lists representing two non-negative integers.
# The digits are stored in reverse order, and each of their nodes contains a single digit.
# Add the two numbers and return the sum as a linked list.
# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

# Example 1: Input:
l1 = [2,4,3]
# print(l1)
l2 = [5,6,4]
# print(l2)
# Output: [7,0,8]
# Explanation: 342 + 465 = 807.

# Example 2: Input: l1 = [0], l2 = [0]
# Output: [0]

# Example 3: Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
# Output: [8,9,9,9,0,0,0,1]

l1_1 = [2,4,3]
l2_1 = [5,6,4]

l1_2 = [0]
l2_2 = [0]

l1_3 = [9,9,9,9,9,9,9]
l2_3 = [9,9,9,9]

def addTwoNumbers(l1, l2):

    def convertir_listas_a_numeros_y_devolver_la_suma():
        # l1 y l2 son una una lista y las tengo que convertir a número
        # 1 - invertir las listas
        l1.reverse()
        #print(l1)
        l2.reverse()
        # print(l2)
        # 2 - convertir listas en números. Primero los convierto en un string y después los concateno.
        # l1_numero va a ser el número que sale de l1
        l1_string = []
        for l1_string_for in l1:
            l1_string.append(str(l1_string_for))
        # Concateno los elementos de l1_string y l2_string
        l1_numero = int("".join(l1_string))
        #print(l1_numero)
        #l2_numero va a ser el número que sale de l2
        l2_string = []
        for l2_string_for in l2:
            l2_string.append(str(l2_string_for))
        l2_numero = int("".join(l2_string))
        suma = l1_numero + l2_numero
        return suma

    suma = convertir_listas_a_numeros_y_devolver_la_suma()

    def convertir_el_numero_a_lista():
        #acá conveirto el resultado de la suma
        pasar_a_string = str(suma)
        ya_es_string = list(pasar_a_string)
        #print(ya_es_string)
        ya_es_string.reverse()
        return ya_es_string

    ya_es_string = convertir_el_numero_a_lista()
    return ya_es_string

hola = addTwoNumbers(l1, l2)
#print(hola)

print(f'resultado 1: "{addTwoNumbers(l1_1, l2_1)}"')
print(f'resultado 2: "{addTwoNumbers(l1_2, l2_2)}"')
print(f'resultado 3: "{addTwoNumbers(l1_3, l2_3)}"')
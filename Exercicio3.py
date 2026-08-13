#3 - Utilize um loop for para calcular a soma dos números ímpares de 1 a 10.

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

numeroImpar = 0

for numero in numeros:
    if numero % 2 !=0:
        numeroImpar = numeroImpar + numero
    
print (f"A soma dos numeros impares é: {numeroImpar}")
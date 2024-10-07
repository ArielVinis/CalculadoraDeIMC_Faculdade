def calcular_imc(peso, altura):
    try:
        imc = peso / (altura ** 2)
        return imc
    except ZeroDivisionError:
        return "A altura não pode ser zero!"
    except Exception as e:
        return f"Ocorreu um erro: {e}"

def classificar_imc(imc):
    if imc < 18.5:
        return "Abaixo do peso"
    elif 18.5 <= imc < 24.9:
        return "Peso normal"
    elif 25 <= imc < 29.9:
        return "Sobrepeso"
    elif 30 <= imc < 34.9:
        return "Obesidade Grau 1"
    elif 35 <= imc < 39.9:
        return "Obesidade Grau 2"
    else:
        return "Obesidade Grau 3"

# Solicitar peso e altura ao usuário
peso = float(input("Digite o seu peso (kg): "))
altura = float(input("Digite a sua altura (m): "))

# Calcular IMC
imc = calcular_imc(peso, altura)
print(f"Seu IMC é: {imc:.2f}")

# Classificar IMC
classificacao = classificar_imc(imc)
print(f"Classificação: {classificacao}")

while True:
    try:

        peso = float(input('Digite seu peso (em KG): '))
        altura = float(input('Digite sua altura (em metros): '))

        imc = peso / altura**2
       
        o_3 = f'Seu imc é {imc:.2f} e seu nível é: Obesidade grau 3'
        o_2 = f'Seu imc é {imc:.2f} e seu nível é: Obesidade grau 2'
        o_1 = f'O seu imc é {imc:.2f} e seu nível é: Obesidade grau 1'
        sp = f'O seu imc é {imc:.2f} e seu nível é: Sobrepeso'
        n = f'Seu imc é {imc:.2f} e seu nível é: Normal'
        abn = f'O seu imc é {imc:.2f} e seu nível é: Abaixo do normal'

        if(imc > 40.0):
         {
            print(o_3)
         }
        elif(40.0 > imc >= 35.0):
         {
            print(o_2)
         }
        elif(35.0 > imc >= 30.0):
         {
            print(o_1)
         }
        elif(30.0 > imc >= 25.0):
         {
            print(sp)
         }
        elif(25 > imc >= 18.6):
         {
            print(n)
         }
        elif(imc <= 18.5):
         {
            print(abn)
         }
        break
    except:
      print("Verifique se você digitou os dados de entrada corretamente.")


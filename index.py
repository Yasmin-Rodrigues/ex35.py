import datetime
nasc =int(input('Qual o ano do seu nascimento?'))
datetime =datetime.datetime.now()
date = datetime.date()
ano =int(date.strftime("%Y"))
idade = ano - nasc
if idade <= 9:
    print(f'Você tem {idade} anos, é um(a) atleta \033[35mMIRIM')
elif idade <=14:
    print(f'Você tem {idade} anos, é um(a) atleta \033[35mINFANTIL')
elif idade <=19:
    print(f'Você tem {idade} anos, é um(a) atleta \033[35mJUNIOR')
elif idade <=20:
    print(f'Você tem {idade} anos, é um(a) atleta \033[35mSÊNIOR')
else:
    print(f'Você tem {idade}, é um(a) atleta \033[35mMASTER')
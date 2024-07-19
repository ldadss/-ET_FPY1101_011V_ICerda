import json
def menu(titulo,lista):
    print('========================================')
    print(titulo.upper())
    print('========================================')
    while True:
        i=1
        for elem in lista:
            print(i,'.-',elem)
            i+=1
        print(i,'.- Salir')
        opc=input('Ingrese Opción: ')
        if opc.isdigit():
            opc_int=int(opc)
            if opc_int>=1 and opc_int<=i:
                return opc_int
            else:
                print('Debe Ingresar un Número entre 1 y ',i)
        else:
            print('Ingrese Sólo Números')

def lee_archivo_afp():
    with open("Afps.json", encoding="utf-8") as ar:
        afp= json.load(ar)
    return afp

def valida_rut(rut):
        lista=rut
        if lista.isdigit() and lista[8]== "k" or lista[8].isdigit:
           return True
        else:
           return False
def lee_rut():
    while True:
        rut=input('Ingrese rut: ')
        if valida_rut(rut):
            return rut
        else:
            print('rut erroneo')
def valida_nombre(nombre):
        n=nombre
        if n.isalpha():
           return True
        else:
           return False
def lee_nombre():
    while True:
        nom=input('Ingrese Nombre del afiliado: ')
        if valida_nombre(nom):
            return nom
        else:
            print('Nombre Erróneo') 
def valida_apellido(apellido):
        n=apellido
        if n.isalpha():
           return True
        else:
           return False
def lee_apellido():
    while True:
        ap=input('Ingrese Nombre del afiliado: ')
        if valida_nombre(ap):
            return ap
        else:
            print('Nombre Erróneo')               

def valida_edad(edad):
    if edad>21 and edad<120:
        return True
    else:
        return False

def lee_edad():
    while True:
        edad=input('Ingrese Edad del afiliado: ')
        if edad.isdigit():
            if valida_edad(int(edad)):
                return int(edad)
            else:
                print('Edad Fuera de Rango')
        else:
            print('Debe Ingresar un Número') 
def valida_nivel_estudios(tipo):
    if tipo in ['B','M','S','N']:
        return True
    else:
        return False          
def lee_estudios():
    while True:
        tip=input('Ingrese nivel de estudio (B=BASICA,M=MEDIA,S=SUPERIOR,N=SIN ESTUDIOS,): ')
        if valida_nivel_estudios(tip):
            return tip
        else:
            print('no existe ese nivel de estudio')          
def valida_saldo(saldo):
    if saldo>1000000:
        True
    else:
        False    
def lee_saldo():
    while True:
        saldo=input("ingrese saldo del afiliado")
        if saldo.isdigit():
                if valida_edad(int(saldo)):
                    True
                else:
                    print('el monto es muy pequeño')
        else:
            print("ingrese un digito")  
def lista_afp(nombre,sociedad):
    lista_temp=[]
    for nombre in lista_temp:
        if nombre.get('SOCIEDAD')==sociedad:
            lista_temp.append(nombre.get('SOCIEDAD'))
    return lista_temp


def crea_json(lista):
    with open('archivo.json', 'w') as archivo:
        json.dump(lista, archivo)            


# programa principal
            
lista_afiliados=[]


while True:
    opc=menu('menu PRINCIPAL',['Ingresar','buscar','generar_Informe','salir'])
    if opc==1:
        rut=lee_rut()
        nombre=lee_nombre()
        apellido=lee_apellido()
        edad=lee_edad()
        estudios=lee_estudios()
        saldo=lee_saldo()
        f=lee_archivo_afp()
        diccionario={}
        diccionario['rut']=rut
        diccionario['edad']=edad
        diccionario['nombre']=nombre
        diccionario['apellido']=apellido
        diccionario['estudios']=estudios
        diccionario['saldo']=saldo
        diccionario["antigua afo"]=f
        
        lista_afiliados.append(diccionario)
        print(lista_afiliados) 
    elif opc==2:

        pass   
    elif opc==3:
        crea_json(lista_afiliados)
    else:
        break


   


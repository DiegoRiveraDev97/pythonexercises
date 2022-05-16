#creacion de un diccionario 
family_dict = {
                        #con raya al piso la salida es completa con la raya
    "papa": ["mauricio" ,45_132_000],
    "mama": ["Delcy" ,45_134_000],
    "hermana": ["jennifer" ,22],
    "hermano": ["jeferson",26]
}

#insercion de una nueva clave con su respectivo valor
family_dict["abuela"]="marleny"
family_dict["abuela"]="lucila"

#bucle para retornar la claves y su respectivo valor dentro del diccionario
for objeto,valor in family_dict.items():
    print(f'en la familia tenemos {objeto} {valor}')
    
#comando para eliminar una clave con su respectivo valor
#del(family_dict["hermano"])

#como comprobar la existencia de una clave
#print("papa" in family_dict)
 

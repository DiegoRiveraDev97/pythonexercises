tabla_de_control = 'TRWAGMYFPDXBNUZSQVHLCKE'

nif ='12345678'
control_digital = tabla_de_control[int(nif)% 23]
whole_nif = nif + control_digital

print(whole_nif)
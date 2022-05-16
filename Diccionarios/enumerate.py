vocales = "aeiou"

enumerar_vocales = {}

for i, vocal in enumerate(vocales):
    enumerar_vocales[vocal] = i + 1
    
print( "a" in enumerar_vocales)
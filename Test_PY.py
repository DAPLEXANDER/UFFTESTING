name = "Dennious"
print("hello world my name is:",name)
ministerio = "El ministerio de los andares tontos"

print len("El ministerio de los andares tontos")
print  ministerio.upper()
'''La combinación de cadenas juntas de este modo se llama concatenación. Ahora vamos a probar concatenar unas cuantas cadenas juntas.
'''
print("Spam " + "y " + "huevos")
#str() convierte cosas que no son cadenas en cadenas
print "El valor de pi es alrededor de " + str(3.14)
#hagamos algunas preguntas
nombre = raw_input("Cual es tu nombre?")
mision = raw_input("Cual es tu mision?")
color = raw_input("Cual es tu color favorito?")

print "Ah, asi que tu nombre es %s, tu mision es %s, \
y tu color favorito es %s." % (nombre, mision, color)

#Ejemplo contar la longitud y escribirlo en mayuscula
mi_string = "Dennis es un genio"
print len(mi_string)
print mi_string.upper()
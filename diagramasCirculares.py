from cmu_graphics import *
#fondo
app.fondo='cian'
#mensajes en el lienzo
Rotulo('Religiones en el mundo',120,20,tamaño=20,negrito=True)
Rotulo('total de personas 7600',120,40,tamaño=20)
Rotulo('Porcentajes',120,60,tamaño=20)
#mensaje de los nombres de las religiones
Rotulo('Islan',100,80)
Rotulo('Cristianismo',100,90)
Rotulo('Budismo',100,100)
Rotulo('Hinduismo',100,110)
Rotulo('Religiones Tradicionales Chinas',120,120)
Rotulo('Religiones AfroAmericanas',100,130)
Rotulo('Personas Ateas',100,140)
#circulos para diferenciar el clor de cada religion
Círculo(10,80,2.5,relleno='naranja')
Círculo(10,90,2.5,relleno='rojo')
Círculo(10,100,2.5,relleno='verde')
Círculo(10,110,2.5,relleno='amarillo')
Círculo(10,120,2.5,relleno='azul')
Círculo(10,130,2.5,relleno='índigo')
Círculo(10,140,2.5,relleno='violeta')
#diagramas circulares
digrama1=Círculo(80,200,30,relleno='gris')
diagrama2=Círculo(320,80,30,relleno='gris')
diagrama3=Círculo(320,200,30,relleno='gris')
diagrama4=Círculo(200,200,30,relleno='gris')
diagrama5=Círculo(80,320,30,relleno='gris')
diagrama6=Círculo(200,320,30,relleno='gris')
diagrama7=Círculo(320,320,30,relleno='gris')
#total de la poblacion
poblacionTotal=7600
religion='cristianismo'
def dibujarArcos(religion):
    if religion=='cristianismo':
        muestra=2300
        resultado=(muestra * 360)/ poblacionTotal
        arco1=Arco(80,200,60,60,0,resultado,relleno='rojo',borde='blanco')
        porcentaje=(muestra * 100)/ poblacionTotal
        Rotulo(porcentaje,60,250)
        religion='islan'
    if religion=='islan':
        muestra=1900
        resultado=(muestra * 360)/ poblacionTotal
        arco2=Arco(320,80,60,60,0,resultado,relleno='naranja',borde='blanco')
        porcentaje=(muestra * 100)/ poblacionTotal
        Rotulo(porcentaje,320,130)
        religion='hinduismo'
    if religion=='hinduismo':
        muestra=1200
        resultado=(muestra * 360)/ poblacionTotal
        arco3=Arco(320,200,60,60,0,resultado,relleno='amarillo',borde='blanco')
        porcentaje=(muestra * 100)/ poblacionTotal
        Rotulo(porcentaje,340,250)
        religion='budismo'
    if religion=='budismo':
        muestra=520
        resultado=(muestra * 360)/ poblacionTotal
        arco4=Arco(200,200,60,60,0,resultado,relleno='verde',borde='blanco')
        porcentaje=(muestra * 100)/ poblacionTotal
        Rotulo(porcentaje,200,250)
        religion='religionesTradicionales'
    if religion=='religionesTradicionales':
        muestra=394
        resultado=(muestra * 360)/ poblacionTotal
        arco5=Arco(80,320,60,60,0,resultado,relleno='azul',borde='blanco')
        porcentaje=(muestra * 100)/ poblacionTotal
        Rotulo(porcentaje,60,370)
        religion='religionesAfroamericanas'
    if religion=='religionesAfroamericanas':
        muestra=100
        resultado=(muestra * 360)/ poblacionTotal
        arco6=Arco(200,320,60,60,0,resultado,relleno='índigo',borde='blanco')
        porcentaje=(muestra * 100)/ poblacionTotal
        Rotulo(porcentaje,200,370)
        religion='personasAteas'
    if religion=='personasAteas':
        muestra=1200
        resultado=(muestra * 360)/ poblacionTotal
        arco7=Arco(320,320,60,60,0,resultado,relleno='violeta',borde='blanco')
        porcentaje=(muestra * 100)/ poblacionTotal
        Rotulo(porcentaje,340,370)
    
dibujarArcos(religion)

cmu_graphics.run()
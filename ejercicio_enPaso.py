from cmu_graphics import *

def onMouseMove(x, y):
    

    app.fondo = 'negro'

Rótulo('*No a escala', 340, 370, relleno='blanco', tamaño=16)

sol = Estrella(200, 200, 35, 400, relleno=gradiente('naranja', 'amarillo', 'rojoNaranja'))
luna=Círculo(200,100,5,relleno='blanco')
luna.dirección='sentido-horario'

luna2=Círculo(200,35,5,relleno='blanco')
luna2.dirección='sentido-horario'
mercurio = Grupo(
    Círculo(200,200,40,relleno=None,borde='grisOscuro'),
    Círculo(200,160,6,relleno=gradiente('madera','trigo','madera','trigo','madera',inicio='derecha'))
    )
mercurio.dirección= 'sentido-horario'
venus = Grupo(
    Círculo(200,200,60,relleno=None,borde='grisOscuro'),
    Círculo(200,140,9,relleno=gradiente('marrónArenoso','naranjaMarrón','marrónArenoso','naranjaMarrón','marrónArenoso',inicio='derecha-superior'))
    )
venus.dirección= 'sentido-horario'
tierra = Grupo(
    Círculo(200, 200, 80, relleno=None, borde='grisOscuro'),
    Círculo(200, 120, 10, relleno=gradiente('verde', 'azulReal', inicio='izquierda-superior')),
    Círculo(200,120,20,relleno=None,borde='grisOscuro'),
    luna
    )
tierra.dirección = 'sentido-horario'
marte= Grupo(
    Círculo(200,200,100,relleno=None, borde='grisOscuro'),
    Círculo(200,100,8.4,relleno=gradiente('rojo','coral','rojo','coral','rojo','coral','rojo',inicio='izquierda-superior')),
    )
marte.dirección= 'sentido-horario'
jupiter= Grupo(
    Círculo(200,200,120,relleno=None,borde='grisOscuro'),
    Círculo(200,80,14,relleno=gradiente('latigoDePapaya','madera','marrónCuero','madera','latigoDePapaya',inicio='superior'))
)
jupiter.dirección='sentido_horario'
saturno= Grupo(
    Círculo(200,200,140,relleno=None,borde='grisOscuro'),
    Círculo(200,60,12,relleno=gradiente('bronceado','trigo','naranjaMarrón','bisque','bronceado',inicio='derecha-superior')),
    Círculo(200,60,24,relleno=None,borde='grisClaro'),
    luna2
)
saturno.dirección='sentido_horario'

urano= Grupo(
    Círculo(200,200,160,relleno=None,borde='grisOscuro'),
    Círculo(200,40,10,relleno='azulAceroClaro')
)
urano.dirección='sentido_horario'
neptuno= Grupo(
    Círculo(200,200,180,relleno=None,borde='grisOscuro'),
    Círculo(200,20,9,relleno='azulGandul')
)
neptuno.dirección='sentido_horario'
def enTeclaPresionada(tecla):
    # Cambie la dirección basado en la tecla.
    if (tecla == 'derecha'):
        tierra.dirección = 'sentido-horario'
    elif (tecla == 'izquierda'):
        tierra.dirección = 'sentido-antihorario'

def enPaso():
    # Si la dirección de la tierra es en sentido horario, agregue 3 al rotarÁngulo.
    # Si no, reste 3.
    if (tierra.dirección == 'sentido-horario'):
        #luna.rotarÁngulo +=4
        #luna2.rotarÁngulo +=4
        mercurio.rotarÁngulo +=4.5
        venus.rotarÁngulo +=4
        tierra.rotarÁngulo += 3
        marte.rotarÁngulo +=2.8
        jupiter.rotarÁngulo +=2.6
        saturno.rotarÁngulo +=2.4
        urano.rotarÁngulo +=2.2
        neptuno.rotarÁngulo +=2
    else:
        #luna.rotarÁngulo -=4
        #luna2.rotarÁngulo -=4
        mercurio.rotarÁngulo -=4.5
        venus.rotarÁngulo -=4
        tierra.rotarÁngulo -= 3
        marte.rotarÁngulo -=2.8
        jupiter.rotarÁngulo -=2.6
        saturno.rotarÁngulo -=2.4
        urano.rotarÁngulo -=2.2
        neptuno.rotarÁngulo -=2
    # Incremente el número de puntos del sol por 1.
    sol.puntos += 1

cmu_graphics.run()
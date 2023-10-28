from cmu_graphics import *
app.fondo='verde'
cuerpo=Círculo(200,200,150,relleno='bronceado',borde='negro',anchuraDeBorde=20)

norte=Rotulo('N',200,100,tamaño=50)
sur=Rotulo('S',200,300,tamaño=50)
este=Rotulo('W',300,200,tamaño=50)
oeste=Rotulo('E',100,200,tamaño=50)
brujula= Grupo(Ovalo(200,60,60,60,relleno='negro'),Círculo(200,0,40,relleno=None,borde='oro'),cuerpo,Estrella(200,200,80,4,redondez=20,relleno='oro'),Estrella(200,200,60,6,relleno='oro',redondez=20,opacidad=50),norte,sur,este,oeste,Línea(102,150,130,166),Línea(128,114,154,146),Línea(162,96,172,126),Línea(235,126,248,100),Línea(280,114,254,142),Línea(274,162,306,152),Línea(306,250,285,236),Línea(255,253,278,284),Línea(228,276,244,304),Línea(141,300,175,284),Línea(123,280,150,262),Línea(100,261,122,230))
manilla=Poligono(200,120,220,200,200,280,180,200,200,120,relleno=gradiente('rojo','azul',inicio='superior'))
def enRatónMovido(ratónX,ratónY):
    if ratónX<200:
        brujula.rotarÁngulo-=1
        manilla.rotarÁngulo-=1
    if ratónX>200:
        brujula.rotarÁngulo+=1
        manilla.rotarÁngulo+=1

cmu_graphics.run()
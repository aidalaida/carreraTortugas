import turtle

class Circuito(): #Es un objeto que continene 4 instancias (corredores) y otra instancia pantalla
    corredores = [] #lista vacia donde se meten 4 instancias del objeto circuito. Propiedad pública
    __posStartY = (-30, -10, 10, 30)
    __colorTurtle = ('red', 'blue', 'green', 'orange')
    
    def __init__(self, width, height): #inicializando Pantalla, creando el ciercuito
            
        self.__screen = turtle.Screen() #Atributo de curcuito. Que es un Objeto. cualquiera que tenga contacto con screen puede hacer lo que quiera, que nadie desde fuera me lo toque
        self.__screen.setup(width, height)
        self.__screen.bgcolor('lightgray')
        self.__startLine = -width/2 + 20
        self.__finishLine = width/2 -20
        
        self.__createRunners()
    
    def __createRunners(self): #inicializamos la creacion de jugadores
        for i in range(4): 
            new_turtle = turtle.Turtle()
            new_turtle.color(self.__colorTurtle[i])
            new_turtle.shape('turtle')
            new_turtle.penup() #quita la linea que pinta el boli
            new_turtle.setpos(self.__startLine, self.__posStartY[i])
            
            self.corredores.append(new_turtle)    
        
        

if __name__ == '__main__': #Para probarlo
    circuito = Circuito(640,480)
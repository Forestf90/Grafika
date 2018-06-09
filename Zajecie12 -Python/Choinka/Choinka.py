# Importujemy wszystkie konieczne biblioteki:
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys
# Deklarujemy wszystkie zmienne globalne
global xrot # wartość obracania wg kierunku x
global yrot # wartość obracania wg kierunku y
global ambient # oświetlanie otaczające
global greencolor # kolor igieł choinki
global treecolor # kolor badyla choinki
global lightpos # Lokalizacja źródła światła
# Procedura inicializacji
def init():
    global xrot # wartość obracania wg kierunku x
    global yrot # wartość obracania wg kierunku y
    global ambient # oświetlanie otaczające
    global greencolor # kolor igieł choinki
    global treecolor # kolor badyla choinki
    global lightpos # Lokalizacja źródła światła
    xrot = 0.0 # wartość obracania wg kierunku x = 0
    yrot = 0.0 # wartość obracania wg kierunku y = 0
    ambient = (1.0, 1.0, 1.0, 1) # Pierwsze trzy wartości określają kolor w postaci
    
    greencolor = (0.2, 0.8, 0.0, 0.8) # kolor zielony dla igieł
    treecolor = (0.9, 0.6, 0.3, 0.8) # kolor brązowy dla badyla
    lightpos = (1.0, 1.0, 1.0) # lokalizacja źródła światła wg osi xyz
    glClearColor(0.5, 0.5, 0.5, 1.0) # kolor szary dla zarysowania początkowego

    gluOrtho2D(-1.0, 1.0, -1.0, 1.0) # określamy krawędzi rysowania poziomo a
    
    glRotatef(-90, 1.0, 0.0, 0.0) # przesuniemy się wg osi Х na 90 stopni
    glLightModelfv(GL_LIGHT_MODEL_AMBIENT, ambient) # określamy bieżący model oświetlania
    glEnable(GL_LIGHTING) # włączamy oświetlanie
    glEnable(GL_LIGHT0) # włączamy jedne źródło światła
    glLightfv(GL_LIGHT0, GL_POSITION, lightpos) # określamy lokalizację źródła światła
    # procedura opracowania przycisków specjalnych
def specialkeys(key, x, y):
    global xrot
    global yrot
    # dla przucisków ze strzałkami
    if key == GLUT_KEY_UP: # przycisk dogóry
        xrot -= 2.0 # zmniejszajmy kąt obracania wg osi Х
    if key == GLUT_KEY_DOWN: # przucisk dodołu
        xrot += 2.0 # zwiększajmy kąt obracania wg osi Х
    if key == GLUT_KEY_LEFT: # w lewo
        yrot -= 2.0 # zmniejszajmy kąt obracania wg osi Y
    if key == GLUT_KEY_RIGHT: # na prawo
         yrot += 2.0 # zwiększajmy kąt obracania wg osi Y
    glutPostRedisplay() # wywołujemy procedurę przerysowania
    # Procedura przerysowania
def draw():
    global xrot
    global yrot
    global lightpos
    global greencolor
    global treecolor
    glClear(GL_COLOR_BUFFER_BIT) 
    glPushMatrix() # Zachowujemy bieżące położenie
   
    glRotatef(xrot, 1.0, 0.0, 0.0) # Obracamy po osi X na wielkość
   
    glRotatef(yrot, 0.0, 1.0, 0.0) # Obracamy po osi Y na wielkość
    
    glLightfv(GL_LIGHT0, GL_POSITION, lightpos) 
    # Rysujemy badyl choinki
    # Ustalamy materiał: rysować z 2 stron, światło otaczające, kolor brązowy
    glMaterialfv(GL_FRONT_AND_BACK, GL_DIFFUSE, treecolor)
    glTranslatef(0.0, 0.0, -0.7) # Przesuniemy się wzdłuż osi Z
    
    # Rysujemy Рисуем cylinder z radiusem 0.1, wysokością 0.2
    # Ostatnie dwie liczby określają ilość wielokątów
    glutSolidCylinder(0.1, 0.2, 20, 20)
    # Rysujemy gałęzi choinki
    # Ustalamy materiał: rysować z 2 stron, światło otaczające, kolor zielony
    glMaterialfv(GL_FRONT_AND_BACK, GL_DIFFUSE, greencolor)
    glTranslatef(0.0, 0.0, 0.2) # Przesuniemy się wzdłuż osi Z
   
    # Rysujemy dolne gałęzi (stożek) z radiusem 0.5, wysokością 0.5
    # Ostatnie dwie liczby okreslają ilość wielokątów

    glutSolidCone(0.5, 0.5, 20, 20)
    glTranslatef(0.0, 0.0, 0.1) # Przesuniemy się wzdłuż osi Z
   
    glutSolidCone(0.47, 0.47, 20, 20) # Stożek z radiusem 0.4,
   
    glTranslatef(0.0, 0.0, 0.1) # Przesuniemy się wzdłuż osi Z
    
    glutSolidCone(0.44, 0.44, 20, 20) # Stożek z radiusem 0.3,

    glTranslatef(0.0, 0.0, 0.1) # Przesuniemy się wzdłuż osi Z
   
    glutSolidCone(0.41, 0.41, 20, 20) # Stożek z radiusem 0.4,
   
    glTranslatef(0.0, 0.0, 0.1) # Przesuniemy się wzdłuż osi Z
    
    glutSolidCone(0.38, 0.38, 20, 20) # Stożek z radiusem 0.3,


    glTranslatef(0.0, 0.0, 0.1) # Przesuniemy się wzdłuż osi Z
   
    glutSolidCone(0.35, 0.35, 20, 20) # Stożek z radiusem 0.4,
   
    glTranslatef(0.0, 0.0, 0.1) # Przesuniemy się wzdłuż osi Z
    
    glutSolidCone(0.32, 0.32, 20, 20) # Stożek z radiusem 0.3,


    glTranslatef(0.0, 0.0, 0.1) # Przesuniemy się wzdłuż osi Z
   
    glutSolidCone(0.29, 0.29, 20, 20) # Stożek z radiusem 0.4,
   
    glTranslatef(0.0, 0.0, 0.1) # Przesuniemy się wzdłuż osi Z
    
    glutSolidCone(0.26, 0.26, 20, 20) # Stożek z radiusem 0.3,

    glTranslatef(0.0, 0.0, 0.1) # Przesuniemy się wzdłuż osi Z
   
    glutSolidCone(0.23, 0.23, 20, 20) # Stożek z radiusem 0.4,
   
    glTranslatef(0.0, 0.0, 0.1) # Przesuniemy się wzdłuż osi Z
    
    glutSolidCone(0.2, 0.2, 20, 20) # Stożek z radiusem 0.3,

    glTranslatef(0.0, 0.0, 0.1) # Przesuniemy się wzdłuż osi Z
   
    glutSolidCone(0.17, 0.17, 20, 20) # Stożek z radiusem 0.4,
   
    glTranslatef(0.0, 0.0, 0.1) # Przesuniemy się wzdłuż osi Z
    
    glutSolidCone(0.14, 0.14, 20, 20) # Stożek z radiusem 0.3,

    glTranslatef(0.0, 0.0, 0.1) # Przesuniemy się wzdłuż osi Z
   
    glutSolidCone(0.11, 0.11, 20, 20) # Stożek z radiusem 0.4,
   
    glTranslatef(0.0, 0.0, 0.1) # Przesuniemy się wzdłuż osi Z
    
    glutSolidCone(0.08, 0.08, 20, 20) # Stożek z radiusem 0.3,
    
    glPopMatrix() # Wracamy zachowane położenie
    
    glutSwapBuffers() # Wyprowadzamy wszystko
   
# Tutaj zaczanamy wykonywać program
# Wykorzystujemy podwójne buforowanie oraz kolory w postaci RGB (Czerwony, Zielony, Niebieski)
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
# Ustalamy początkowy rozmiar okna (szerokość, wysokość)
glutInitWindowSize(800, 1200)
# Ustalamy początkowe położenie okna stosunkowo lewego górnego kąta ekranu
glutInitWindowPosition(50, 50)
# Inicjalizacja OpenGl
glutInit(sys.argv)
# Tworzymy okno z nagłowkiem "Happy New Year!"
glutCreateWindow(b"Happy New Year!")
# Określamy procedurę odpowiedzalną za przerysowanie
glutDisplayFunc(draw)
# Określamy procedurę odpowiedzialną za opracowanie przycisków
glutSpecialFunc(specialkeys)
# Wywołujemy funkcję inicjalizacji
init()
# Uruchomimamy głuwną pętlę
glutMainLoop()
rint('Hello world, Python')

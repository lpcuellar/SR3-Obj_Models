##
##  UNIVERSIDAD DEL VALLE DE GUATEMALA
##  GRÁFICAS POR COMPUTADORA
##  SECCIÓN 20
##
##  SR3: Obj Models
##  LUIS PEDRO CUÉLLAR - 18220
##

class Object(object):
    def __init__(self, filename):
        with open(filename, 'r') as file:
            self.lines = [line for line in file.readlines() if line.strip()]

        self.vertices = []
        self.normals = []
        self.texcoords = []
        self.faces = []

        self.read()

    def read(self):
        for line in self.lines:
            if line:
                prefix, value = line.split(' ', 1)

                if prefix == 'v': # vertices
                    self.vertices.append(list(map(float,value.split(' '))))
                elif prefix == 'vn':
                    self.normals.append(list(map(float,value.split(' '))))
                elif prefix == 'vt':
                    self.texcoords.append(list(map(float,value.split(' '))))
                elif prefix == 'f':
                    if "//" in value:
                        self.faces.append([list(map(int,vert.split('//'))) for vert in value.split(' ')])

                    else:
                        self.faces.append([list(map(int,vert.split('/'))) for vert in value.split(' ')])

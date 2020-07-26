##
##  UNIVERSIDAD DEL VALLE DE GUATEMALA
##  GRÁFICAS POR COMPUTADORA
##  SECCIÓN 20
##
##  SR3: Obj Models
##  LUIS PEDRO CUÉLLAR - 18220
##

import struct

from object import Object

##  char --> 1 byte
def char(var):
    return struct.pack('=c', var.encode('ascii'))

##  word --> 2 bytes
def word(var):
    return struct.pack('=h', var)

##  dword --> 4 bytes
def dword(var):
    return struct.pack('=l', var)

def color(r, g, b):
    return bytes([int(b * 255), int(g * 255), int(r * 255)])

class Render(object):
    def __init__(self, width, height, background = None):
        self.glInit(width, height, background)
        self.current_color = color(1, 1, 1)

    ##  initiates the image with the width, height and background color
    def glInit(self, width, height, background):
        background = color(0, 0, 0) if background == None else background

        self.bg_color = background

        self.glCreateWindow(width, height)

    ##  creates the window with the given
    def glCreateWindow(self, width, height):
        self.width = width
        self.height = height
        self.glClear(self.bg_color)

    ##  colors the image with the background color
    def glClear(self, bg_color):
        self.bg_color = bg_color
        self.pixels = [ [ self.bg_color for x in range(self.width)] for y in range(self.height) ]

    ##  defines an area inside the window in which it can be drawn points and lines
    def glViewPort(self, x, y, width, height):
         self.vp_x = x
         self.vp_y = y
         self.vp_width = width
         self.vp_height = height

    ##   changes de background color of the image
    def glClearColor(self, r, g, b):
        self.r = r
        self.g = g
        self.b = b

        self.bg_color = color(self.r, self.g, self.b)

        self.glClear(self.bg_color)

    ##  draws a point in the image with the given NDC coordinates
    def glVertex(self, x, y):
        ver_x = int(((x + 1) * (self.vp_width / 2)) + self.vp_x)
        ver_y = int(((y + 1) * (self.vp_height / 2)) + self.vp_y)
        self.pixels[round(ver_y)][round(ver_x)] = self.current_color

    ##  draws a pint in the image with pixel coordinates
    def glVertex_coordinates(self, x, y):
        self.pixels[y][x] = self.current_color

    ##  changes the color of the points that can be drawn
    def glColor(self, r, g, b):
        self.current_color = color(r, g, b)

    ##  draws a straight line from (x0, y0) to (x1, y1)
    def glLine(self, x0, y0, x1, y1):
        x0 = round(( x0 + 1) * (self.vp_width  / 2 ) + self.vp_x)
        x1 = round(( x1 + 1) * (self.vp_width  / 2 ) + self.vp_x)
        y0 = round(( y0 + 1) * (self.vp_height / 2 ) + self.vp_y)
        y1 = round(( y1 + 1) * (self.vp_height / 2 ) + self.vp_y)

        dx = x1 - x0
        dy = y1 - y0

        steep = abs(dy) > abs(dx)

        if steep:
            x0, y0 = y0, x0
            x1, y1 = y1, x1

        if x0 > x1:
            x0, x1 = x1, x0
            y0, y1 = y1, y0

        dx = abs(x1 - x0)
        dy = abs(y1 - y0)

        offset = 0
        limit = 0.5

        m = dy/dx
        y = y0

        for x in range(x0, x1 + 1):
            if(steep):
                self.glVertex_coordinates(y, x)
            else:
                self.glVertex_coordinates(x, y)

            offset += m
            if offset >= limit:
                y += 1 if y0 < y1 else -1
                limit += 1

    ##  this function loads the model for it to be drawn
    def loadModel(self, filename, translate, scale):
        model = Object(filename)

        for face in model.faces:
            count_vertices = len(face)

            for vertex in range(count_vertices):
                v0 = model.vertices[face[vertex][0] - 1]
                v1 = model.vertices[face[(vertex + 1) % count_vertices][0] - 1]

                x0 = round(v0[0] * scale[0] + translate[0])
                y0 = round(v0[1] * scale[1] + translate[1])
                x1 = round(v1[0] * scale[0] + translate[0])
                y1 = round(v1[1] * scale[1] + translate[1])

                self.glLine_coordinates(x0, y0, x1, y1)

    ##  this function draws a line in between to pixel coordinates. Starts in (x0, y0) and ends in (x1, y1)
    def glLine_coordinates(self, x0, y0, x1, y1):
        dx = abs(x1 - x0)
        dy = abs(y1 - y0)

        steep = dy > dx

        if steep:
            x0, y0 = y0, x0
            x1, y1 = y1, x1

        if x0 > x1:
            x0, x1 = x1, x0
            y0, y1 = y1, y0

        dx = abs(x1 - x0)
        dy = abs(y1 - y0)

        offset = 0
        limit = 0.5

        try:
            m = dy/dx
        except ZeroDivisionError:
            pass
        else:
            y = y0

            for x in range(x0, x1 + 1):
                if steep:
                    self.glVertex_coordinates(y, x)
                else:
                    self.glVertex_coordinates(x, y)

                offset += m
                if offset >= limit:
                    y += 1 if y0 < y1 else -1
                    limit += 1

    ##  this function is used to write the image into the file, and saves it
    def glFinish(self, filename):
        file = open(filename, 'wb')

        ##  file header --> 14 bytes
        file.write(bytes('B'.encode('ascii')))
        file.write(bytes('M'.encode('ascii')))

        file.write(dword(14 + 40 + self.width * self.height * 3))
        file.write(dword(0))
        file.write(dword(14 + 40))

        ##  image header --> 40 bytes
        file.write(dword(40))
        file.write(dword(self.width))
        file.write(dword(self.height))
        file.write(word(1))
        file.write(word(24))
        file.write(dword(0))
        file.write(dword(self.width * self.height * 3))
        file.write(dword(0))
        file.write(dword(0))
        file.write(dword(0))
        file.write(dword(0))

        ##  pixels --> 3 bytes each

        for x in range(self.height):
            for y in range(self.width):
                file.write(self.pixels[x][y])

        file.close()

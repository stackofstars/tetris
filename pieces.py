class Coordinate(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return 'Coordinate({0.x:d}, {0.y:d})'.format(self)

class Piece:
    def __init__(self, type, position, orientation, falling):
        self.type = type #J, L, I, S, T, Z and O
        self.orientation = orientation #1(up), 2(down), 3(left), 4(right)
        self.falling = True

        if type == "J": #initializing position of the block
            self.position = [Coordinate(0, 0), Coordinate(1, 0), Coordinate(1, 1), Coordinate(1, 2)]
        else if type == "L":
            self.position = [Coordinate(2, 0), Coordinate(0, 1), Coordinate(1, 1), Coordinate(2, 1)]
        else if type == "I":
            self.position = [Coordinate(1, 0), Coordinate(1, 1), Coordinate(1, 2), Coordinate(1, 3)]
        else if type == "S":
            self.position = [Coordinate(0, 1), Coordinate(0, 2), Coordinate(1, 0), Coordinate(1, 1)]
        else if type == "T":
            self.position = [Coordinate(0, 1), Coordinate(1, 0), Coordinate(1, 1), Coordinate(1, 2)]
        else if type == "Z":
            self.position = [Coordinate(0, 0), Coordinate(0, 1), Coordinate(1, 1), Coordinate(1, 2)]
        else if type == "O":
            self.position = [Coordinate(0, 1), Coordinate(0, 2), Coordinate(1, 1), Coordinate(1, 2)]

    def getPosition():
        return position

    def isFalling():
        return falling

    def stopFalling():
        falling = False

    def Flip():
        if type == "J":
            if orientation == 1:
                position = [Coordinate(0, 1), Coordinate(0, 2), Coordinate(1, 1), Coordinate(2, 1)]
            else if orientation == 2:
                position = [Coordinate(1, 0), Coordinate(1, 1), Coordinate(1, 2), Coordinate(1, 3)]
            else if orientation == 3:
                position = [Coordinate(0, 1), Coordinate(1, 1), Coordinate(2, 0), Coordinate(2, 1)]
            else if orientation == 4:
                position = [Coordinate(0, 0), Coordinate(1, 0), Coordinate(1, 1), Coordinate(1, 2)]

        else if type == "L":
            if orientation == 1:
                position = [Coordinate(0, 1), Coordinate(1, 1), Coordinate(2, 1), Coordinate(0, 2)]
            else if orientation == 2:
                position = [Coordinate(1, 0), Coordinate(1, 1), Coordinate(1, 2), Coordinate(2, 2)]
            else if orientation == 3:
                position = [Coordinate(0, 1), Coordinate(1, 1), Coordinate(2, 1), Coordinate(2, 0)]
            else if orientation == 4:
                position = [Coordinate(2, 0), Coordinate(0, 1), Coordinate(1, 1), Coordinate(2, 1)]

        else if type == "I":
            if orientation == 1:
                position = [Coordinate(0, 2), Coordinate(1, 2), Coordinate(2, 2), Coordinate(3, 2)]
            else if orientation == 2:
                position = [Coordinate(2, 0), Coordinate(2, 1), Coordinate(2, 2), Coordinate(2, 3)]
            else if orientation == 3:
                position = [Coordinate(0, 1), Coordinate(1, 1), Coordinate(2, 1), Coordinate(3, 1)]
            else if orientation == 4:
                position = [Coordinate(1, 0), Coordinate(1, 1), Coordinate(1, 2), Coordinate(1, 3)]

        else if type == "S":
            if orientation == 1:
                position = [Coordinate(0, 1), Coordinate(1, 1), Coordinate(1, 2), Coordinate(2, 2)]
            else if orientation == 2:
                position = [Coordinate(1, 1), Coordinate(1, 2), Coordinate(2, 0), Coordinate(2, 1)]
            else if orientation == 3:
                position = [Coordinate(0, 0), Coordinate(1, 0), Coordinate(1, 1), Coordinate(2, 2)]
            else if orientation == 4:
                position = [Coordinate(0, 1), Coordinate(0, 2), Coordinate(1, 0), Coordinate(1, 1)]

        else if type == "T":
            if orientation == 1:
                position = [Coordinate(0, 1), Coordinate(2, 1), Coordinate(1, 1), Coordinate(1, 2)]
            else if orientation == 2:
                position = [Coordinate(2, 1), Coordinate(2, 1), Coordinate(1, 1), Coordinate(1, 2)]
            else if orientation == 3:
                position = [Coordinate(2, 1), Coordinate(2, 1), Coordinate(1, 1), Coordinate(0, 1)]
            else if orientation == 4:
                position = [Coordinate(0, 1), Coordinate(1, 0), Coordinate(1, 1), Coordinate(1, 2)]

        else if type == "Z":
            if orientation == 1:
                position = [Coordinate(0, 2), Coordinate(1, 1), Coordinate(1, 2), Coordinate(2, 1)]
            else if orientation == 2:
                position = [Coordinate(1, 0), Coordinate(1, 1), Coordinate(2, 1), Coordinate(2, 2)]
            else if orientation == 3:
                position = [Coordinate(0, 1), Coordinate(1, 0), Coordinate(1, 1), Coordinate(2, 0)]
            else if orientation == 4:
                position = [Coordinate(0, 0), Coordinate(0, 1), Coordinate(1, 1), Coordinate(1, 2)]

    def Fall():
        for i in position:
            position[i].y -= 1

    def moveLeft():
        for i in position:
            position[i].x -= 1

    def moveRight():
        for i in position:
            position[i].x += 1

class Vector2D:

    # Initialize your data structure here.
    # @param {integer[][]} vec2d
    def __init__(self, vec2d):
        self.x = 0
        self.y = -1
        self.vec = vec2d

    # @return {integer}
    def next(self):
        self.y += 1
        while self.x < len(self.vec) and self.y >= len(self.vec[self.x]):
            self.x += 1
            self.y = 0
        if self.x < len(self.vec):
            return self.vec[self.x][self.y]

    # @return {boolean}
    def hasNext(self):
        tempx = self.x
        tempy = self.y
        tempy += 1
        while tempx < len(self.vec) and tempy >= len(self.vec[tempx]):
            tempx += 1
            tempy = 0
        return tempx < len(self.vec)

# Your Vector2D object will be instantiated and called as such:
# i, v = Vector2D(vec2d), []
# while i.hasNext(): v.append(i.next())
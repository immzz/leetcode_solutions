class Solution(object):
    def wallsAndGates(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: void Do not return anything, modify rooms in-place instead.
        """
        for i in xrange(len(rooms)):
            for j in xrange(len(rooms[0])):
                if rooms[i][j] == 0:
                    current = [(i,j)]
                    d = 1
                    while current:
                        new_current = []
                        for p in current:
                            x,y = p[0],p[1]
                            if rooms[x][y] > d:
                                continue
                            if x > 0 and rooms[x-1][y] > d:
                                rooms[x-1][y] = d
                                new_current.append((x-1,y))
                            if x < len(rooms)-1 and rooms[x+1][y] > d:
                                rooms[x+1][y] = d
                                new_current.append((x+1,y))
                            if y > 0 and rooms[x][y-1] > d:
                                rooms[x][y-1] = d
                                new_current.append((x,y-1))
                            if y < len(rooms[0])-1 and rooms[x][y+1] > d:
                                rooms[x][y+1] = d
                                new_current.append((x,y+1))
                        current = new_current
                        d += 1
                            
                    
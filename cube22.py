'''
Created on 2014/08/27

@author: alchu
'''

class Cube22(object):
    '''
    2x2 size cube
    '''


    def __init__(self):
        '''
        Constructor
        '''
        self._data = ["XYZ"] * 8


        
    def __eq__(self, other):
        return self._data == other._data
        
    def __ne__(self, other):
        return not (self == other)
    
    def right(self, amount=1):
        self._op_rot(amount, [1,5,7,3], 0)

    def back(self, amount=1):
        self._op_rot(amount, [2,3,7,6], 1)
    
    def top(self, amount=1):
        self._op_rot(amount, [4,6,7,5], 2)
        
    def _op_rot(self, amount, cubes, dir_): 
        """operation rotate
        amount 0-3 1 means rotate 90 degree clockwise
        cubes list of rotate cubes 1,5,7,3 means 1 move to 5
        dir 0:Xaxis 1:Yaxis 2:Zaxis"""      
        while amount >0:
            amount -=1
            buf = self._pickup(cubes)
            buf = self._round_right(buf)
            for i in range(4):
                buf[i] = self._rot_color(buf[i], dir_)
            self._pickdown(buf, cubes)
    
    def _rot_color(self, s, pos):
        l = list(s)
        c1 = (pos +1) % 3
        c2 = (c1 + 1) % 3
        l[c1], l[c2] = l[c2], l[c1].swapcase()
        return "".join(l)
 
    def _pickup(self, piclist):
        buf = []
        for k in piclist:
            buf += [self._data[k]]
        return buf

    def _pickdown(self, buf, piclist):
        for k in piclist:
            self._data[k] = buf.pop(0)


    def _round_right(self, buf):
        buf = buf[-1:] + buf[:-1]
        return buf

    def tostr(self):
        return "".join(self._data)
    
    def horisearch(self, g):
        goal = Cube22()
        goal._data = g
        graph = {}
        route = []
        return ""
        
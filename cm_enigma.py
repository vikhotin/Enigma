import random

class Rotor:
    _rot_size = 256
    def __init__(self, seed, pos=0):
        random.seed(seed)
        self._permut = list(range(self._rot_size))
        random.shuffle(self._permut)
        self.rotate(pos)
    def __str__(self):
        return str(self._permut)
    def rotate(self, letter=None):
        self.pos = letter if letter is not None else (self.pos+1)%self._rot_size
        return True if self.pos==0 else False
    def _shift_fw(self, letter):
        ''' Here letter must be byte number '''
        return (letter+self.pos)%self._rot_size
    def _shift_bw(self, letter):
        ''' Here letter must be byte number '''
        ''' Returns needed letter '''
        return (letter-self.pos)%self._rot_size
    def encrypt(self, letter):
        return self._shift_bw(self._permut[self._shift_fw(letter)])
    def encrypt_back(self, letter):
        return self._shift_bw(self._permut.index(self._shift_fw(letter)))

class Reflector:
    _rot_size = 256
    def __init__(self):
        self._permut = list(range(self._rot_size))
        self._permut.reverse()
    def __str__(self):
        return str(self._permut)
    def encrypt(self, letter):
        return self._permut[letter]
    
class Enigma:
    def __init__(self):
        ''' right rotor is the closest to reflector '''
        self.lRotor = Rotor(1)
        self.mRotor = Rotor(2)
        self.rRotor = Rotor(3)
        self.reflector = Reflector()
    def _permut(self, m):
        if self.lRotor.rotate():
            if self.mRotor.rotate():
                self.rRotor.rotate()        
        c = self.lRotor.encrypt(m)
        c = self.mRotor.encrypt(c)
        c = self.rRotor.encrypt(c)
        c = self.reflector.encrypt(c)
        c = self.rRotor.encrypt_back(c)
        c = self.mRotor.encrypt_back(c)
        c = self.lRotor.encrypt_back(c)
        return c
    def encrypt(self, message):
        return [self._permut(x) for x in message]
    def decrypt(self, message):
        return self.encrypt(message)
    def setkey(self, a=0, b=0, c=0):
        self.lRotor.rotate(a)
        self.mRotor.rotate(b)
        self.rRotor.rotate(c)

if __name__=='__main__':
    enigma = Enigma()

    mess = (x%256 for x in range(512))

    enigma.setkey(97,98,99)
    mess = enigma.encrypt(mess)
    print(mess)
    
    enigma.setkey(97,98,99)
    mess = enigma.decrypt(mess)
    print(mess)

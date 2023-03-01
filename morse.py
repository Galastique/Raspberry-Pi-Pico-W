from machine import Pin
import utime

led = Pin("LED", Pin.OUT)
delayDot = 0.2
delayDash = delayDot * 3
sentence = "Hello World!"

#Delays
def dot():
    led.on()
    utime.sleep(delayDot)
    led.off()
    utime.sleep(delayDot)
    
def dash():
    led.on()
    utime.sleep(delayDash)
    led.off()
    utime.sleep(delayDot)
    
def endLetter():
    utime.sleep(delayDot)

def endWord():
    utime.sleep(delayDash)

def endSentence():
    utime.sleep(delayDot * 7)

#Letters
def a():
    dot()
    dash()

def b():
    dash()
    dot()
    dot()
    dot()

def c():
    dash()
    dot()
    dash()
    dot()

def d():
    dash()
    dot()
    dot()

def e():
    dot()

def f():
    dot()
    dot()
    dash()
    dot()

def g():
    dash()
    dash()
    dot()

def h():
    dot()
    dot()
    dot()
    dot()

def i():
    dot()
    dot()

def j():
    dot()
    dash()
    dash()
    dash()

def k():
    dash()
    dot()
    dash()

def l():
    dot()
    dash()
    dot()
    dot()

def m():
    dash()
    dash()

def n():
    dash()
    dot()

def o():
    dash()
    dash()
    dash()

def p():
    dot()
    dash()
    dash()
    dot()

def q():
    dash()
    dash()
    dot()
    dash()

def r():
    dot()
    dash()
    dot()

def s():
    dot()
    dot()
    dot()

def t():
    dash()

def u():
    dot()
    dot()
    dash()

def v():
    dot()
    dot()
    dot()
    dash()

def w():
    dot()
    dash()
    dash()

def x():
    dash()
    dot()
    dot()
    dash()

def y():
    dash()
    dot()
    dash()
    dash()

def z():
    dash()
    dash()
    dot()
    dot()

#Numbers
def n1():
    dot()
    dash()
    dash()
    dash()
    dash()
    
def n2():
    dot()
    dot()
    dash()
    dash()
    dash()
    
def n3():
    dot()
    dot()
    dot()
    dash()
    dash()
    
def n4():
    dot()
    dot()
    dot()
    dot()
    dash()
    
def n5():
    dot()
    dot()
    dot()
    dot()
    dot()
    
def n6():
    dash()
    dot()
    dot()
    dot()
    dot()
    
def n7():
    dash()
    dash()
    dot()
    dot()
    dot()
    
def n8():
    dash()
    dash()
    dash()
    dot()
    dot()
    
def n9():
    dash()
    dash()
    dash()
    dash()
    dot()
    
def n0():
    dash()
    dash()
    dash()
    dash()
    dash()
    
#Punctuation & special
def sPer():
    dot()
    dash()
    dot()
    dash()
    dot()
    dash()
    
def sCom():
    dash()
    dash()
    dot()
    dot()
    dash()
    dash()
    
def sApo():
    dot()
    dash()
    dash()
    dash()
    dash()
    dot()

def sQuo():
    dot()
    dash()
    dot()
    dot()
    dash()
    dot()

def sQue():
    dot()
    dot()
    dash()
    dash()
    dot()
    dot()

def sExc():
    dash()
    dot()
    dash()
    dot()
    dash()
    dash()

def sCol():
    dash()
    dash()
    dash()
    dot()
    dot()
    dot()

def sSem():
    dash()
    dot()
    dash()
    dot()
    dash()
    dot()

def sPa1():
    dash()
    dot()
    dash()
    dash()
    dot()

def sPa2():
    dash()
    dot()
    dash()
    dash()
    dot()
    dash()

def sAnd():
    dot()
    dash()
    dot()
    dot()
    dot()

def sPlu():
    dot()
    dash()
    dot()
    dash()
    dot()

def sMin():
    dash()
    dot()
    dot()
    dot()
    dash()

def sEqu():
    dash()
    dot()
    dot()
    dot()
    dash()

def sSla():
    dash()
    dot()
    dot()
    dash()
    dot()

def sUnd():
    dot()
    dot()
    dash()
    dash()
    dot()
    dash()

def sDol():
    dot()
    dot()
    dot()
    dash()
    dot()
    dot()
    dash()

def sAt():
    dot()
    dash()
    dash()
    dot()
    dash()
    dot()

chars = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0", ".", ",", "'", "\"", "?", "!", ":", ";", "(", ")", "&", "+", "-", "=", "/", "_", "$", "@"]
functions = [a, b, c, d, e, f, g, h, i, j, k, l, m, n, i, o, p, q, r, s, t, u, v, w, x, y, z, n1, n2, n3, n4, n5, n6, n7, n8, n9, n0, sPer, sCom, sApo, sQuo, sQue, sExc, sCol, sSem, sPa1, sPa2, sAnd, sPlu, sMin, sEqu, sSla, sUnd, sDol, sAt]

while True:
    for word in sentence:
        for letter in word:
            try:
                functions[chars.index(letter.lower())]()
                print(letter)
                functions[0]
            except:
                pass
            endLetter()
        endWord()
    endSentence()

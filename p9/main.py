"""
Zac Foteff, Wesley Muehlhausen
CPSC351: 01
Problem Set #9

Program simulates the behavior of a PDA that accepts when there is an 
equal amount of 0's and 1's
"""

class PDA ():
    def __init__(self,
                 q="q1", 
                 sigma=["0","1", ""],
                 gamma=["0", "$"],
                 delta={('q1', '', ''):('q2', '$'), 
                        ("q2", "0", "$"):('q2', '0'),
                        ("q2", "0", "0"):('q2', '0'), 
                        ("q2", "1", '0'):("q3", ""), 
                        ("q3", "1", "0"):("q3", ""), 
                        ("q3", "1", "$"):("q4", "")}, 
                 q0="q1", 
                 f=["q1", "q4"], 
                 w=""):
        self.Q = q
        self.sigma = sigma
        self.gamma = gamma
        self.delta = delta
        self.Q0 = q0
        self.F = f
        self.w = w
        self.stack = []
        
    #  --- Stack manipulation methods ---
    def getStackTop(self):
        return self.stack[-1]
    
    def popStackTop(self):
        if (len(self.stack) > 0):
            self.stack.pop()

    def pushStackTop(self, stackSymbol):
        self.stack.append(stackSymbol)
    
    def simulate(self):
        state = self.Q0
        state, newStackTop = self.delta[state, '', '']
        self.pushStackTop(newStackTop)
        
        #   Iterate through all the symbols in the input string 
        for symbol in self.w:
            try:
                state, newStackTop = self.delta[state, symbol, self.getStackTop()]
            except KeyError:
                print("Reject")
                return
            
            if newStackTop != '':
                self.pushStackTop(newStackTop)
            if newStackTop == '':
                self.popStackTop()
            if self.getStackTop() == '$':
                try:
                    state, newStackTop = self.delta[state, symbol, self.getStackTop()]
                except KeyError:
                    print("Reject")
                    return

        if state in self.F:
            print("Accept")
        else:
            print("Reject")
            
def main():
    while(True):
        w = input("Please input a string to test against the DFA, or q to quit: ")
        if w == "q":
            break
        
        pda = PDA (w=w)
        pda.simulate()

main()

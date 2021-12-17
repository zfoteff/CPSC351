"""
Zac Foteff, Wesley Muehlhausen
CPSC351: 01
Problem Set #8

Program simulates the behavior of a DFA that accepts when every odd position of the input
string is a one
"""

class DFA ():
    def __init__(self,
                 q="q0", 
                 sigma=["0","1"], 
                 delta={("q0", "0"):"q1", 
                        ("q0", "1"):"q2", 
                        ("q1", "0"):"q1", 
                        ("q1", "1"):"q1", 
                        ("q2", "0"):"q0", 
                        ("q2", "1"):"q0"}, 
                 q0="q0", 
                 f=["q0", "q2"], 
                 w=""):
        self.Q = q
        self.sigma = sigma
        self.delta = delta
        self.Q0 = q0
        self.F = f
        self.w = w
        
    def deltaTransition(self, currState, symbol):
        return self.delta[(currState, symbol)]
    
    def simulate(self):
        state = self.Q0

        if self.w == "":
            print("Reject")
            return
        
        for symbol in self.w: 
            if symbol not in self.sigma:
                print("Reject")
                return
            state = self.deltaTransition(state, symbol)
        
        if state in self.F:
            print("Accept")
        else:
            print("Reject")
            
def main():
    while(True):
        w = input("Please input a string to test against the DFA, or q to quit: ")
        if w == "q":
            break
        
        dfa = DFA (w=w)
        dfa.simulate()

main()

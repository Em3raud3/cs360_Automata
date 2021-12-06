# ! Ran on Python 3.8.10

class Machine:
    def __init__(self):
        self.Q = []
        self.Σ = []
        self.δ = {}  # we initialize � here
        self.q0 = ""
        self.qf = []

    def description(self):
        print(f"M = <Q, Σ, δ, {self.q0}, {self.qf} >")
        print(f"Q = {self.Q}")
        print(f"Σ = {self.Σ}")
        print(f"δ = {self.δ}")
        print(f"qo = {self.q0}")
        print(f"qf = {self.qf}")

    def addArrow(self, q1, symbol, q2):
        arrow = (q1, symbol)
        self.δ[arrow] = q2

    def removeArrow(self, q1, symbol, q2):
        arrow = (q1, symbol)
        del self.δ[arrow]



    def DFA(self, s_input):
        state = self.q0
        for s in s_input:
            state = self.δ[(state, s)]

        if state in self.qf:
            return print("Accepted")

        return print("Rejected")


def main():
    #! Question 2
    # d = Machine()
    # d.Q = ["qo", "q1", "q2"]
    # d.Σ = ["a", "b"]
    # d.q0 = "q0"
    # d.qf = ["q2"]

    # d.addArrow("q0", "a", "q0")
    # d.addArrow("q0", "b", "q1")
    # d.addArrow("q1", "a", "q1")
    # d.addArrow("q1", "b", "q2")
    # d.addArrow("q2", "a", "q2")
    # d.addArrow("q2", "b", "q2")

    # d.DFA("bbaab")

    #! Question 3

    d = Machine()

    Q = input("Enter a set of states: ")
    Q = Q.split(",")
    d.Q = Q

    Σ = input("Enter input alphabet: ")
    Σ = Σ.split(",")
    d.Σ = Σ

    arrows = input("Enter transition rules (seperated by \"-\"): ")
    arrows = arrows.split("-")  # This is a list of strings
    for i in arrows:
        arrow = i[1:-2] #removes parentheses
        arrow = arrow.split(",")
        d.addArrow(arrow[0], arrow[1], arrow[2])

    q0 = input("Enter the start state: ")
    d.q0 = q0

    qf = input("Enter the final state: ")
    d.qf = qf

    DFA = input("Enter input string: ")
    d.DFA(DFA)

    d.description()


if __name__ == "__main__":
    main()

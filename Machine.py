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


def main():
    d = Machine()
    d.Q = ["qo", "q1", "q2"]
    d.Σ = ["a", "b"]
    d.q0 = "q0"
    d.qf = ["q2"]

    d.addArrow("q0", "b", "q1")
    d.addArrow("q1", "a", "q1")
    d.addArrow("q1", "b", "q2")
    d.addArrow("q2", "b", "q2")
    d.addArrow("q2", "a", "q2")

    print(d.δ)

    d.removeArrow("q0", "b", "q1")
    d.removeArrow("q1", "a", "q1")
    d.removeArrow("q1", "b", "q2")
    d.removeArrow("q2", "b", "q2")
    d.removeArrow("q2", "a", "q2")

    print(d.δ)


if __name__ == "__main__":
    main()

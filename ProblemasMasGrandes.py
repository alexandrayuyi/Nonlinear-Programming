import cvxpy as cp

class ProblemaMasGrande():
    def __init__(self, **items) -> None:
        # Objetivos
        objectivos = cp.Minimize(items['f_value'])
        # Problema
        problema = cp.Problem(objectivos, items['restriccion'])
        #Resultado
        self.__result = problema.solve()
        ...

    def getSolver(self) -> float:
        return self.__result

def Sample() -> None:
    # Variables
    x = cp.Variable()
    problem = ProblemaMasGrande(f_value=x**2 + 4*x + 5, restriccion=[x >= 2, x <= 5])
    # Resultados
    print("Problema", problem.getSolver())
    print("Valor optimo de x",x.value)
    ...

if __name__ == "__main__":
    ...


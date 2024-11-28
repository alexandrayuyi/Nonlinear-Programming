from scipy.optimize import minimize

class Solver:
    def __init__(self, quan, x0=None):
        """
        Inicializa la clase con valores iniciales y atributos por defecto.
        
        :param x0: Lista con los valores iniciales de las variables [x, y, z, ...].
        """
        self.x0 = x0 if x0 else [0] * quan  # Valores iniciales por defecto
        self.solution = None
        self.optimal_value = None

    @staticmethod
    def objetivo(vars, coef):
        """
        Función objetivo: suma de cada variable elevada al cuadrado y multiplicada por su coeficiente.
        
        :param vars: Lista de variables [x, y, z, ...].
        :param coef: Lista de coeficientes correspondientes.
        :return: Valor de la función objetivo.
        """
        return sum(c * v ** 2 for c, v in zip(coef, vars))

    def solve(self, coef, restriccion):
        """
        Resuelve el problema de programación no lineal usando scipy.optimize.minimize.
        """
        restricciones = {'type': 'eq', 'fun': restriccion}
        resultado = minimize(self.objetivo, self.x0, args=(coef,), constraints=restricciones)
        self.solution = resultado.x
        self.optimal_value = resultado.fun

    def get_solution(self):
        """
        Obtiene la solución calculada.
        
        :return: Un diccionario con el valor mínimo y los valores óptimos de las variables.
        """
        return {'optimal_value': self.optimal_value, 'solution': self.solution}

# Ejemplo de uso
from scipy.optimize import minimize

def restriccion(vars):
    # Define tu restricción aquí, por ejemplo:
    return sum(vars) - 100

solver = Solver(3)  # Suponiendo que tenemos 3 variables
coef = [5, 3, 1]  # Coeficientes para las variables
solver.solve(coef, restriccion)
print(solver.get_solution())
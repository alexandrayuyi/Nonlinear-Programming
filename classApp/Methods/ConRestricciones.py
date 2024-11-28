from scipy.optimize import minimize
import numpy as np
import matplotlib.pyplot as plt

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
    
    def graficar(self, coef):
        """
        Grafica la curva de la función objetivo, marca los valores optimizados de las variables
        y señala el punto óptimo de la función objetivo.
        
        :param coef: Lista de coeficientes correspondientes a las variables.
        """
        if self.solution is None or self.optimal_value is None:
            raise ValueError("El problema no ha sido resuelto aún. Llame a 'solve' primero.")

        variables = self.solution
        n_vars = len(variables)

        # Crear gráficos para cada variable
        x = np.linspace(-10, 10, 500)  # Rango de valores para graficar
        fig, axes = plt.subplots(1, n_vars, figsize=(6 * n_vars, 5), squeeze=False)

        for i in range(n_vars):
            y = coef[i] * x**2  # Función cuadrática para cada variable
            axes[0, i].plot(x, y, label=f"Variable {i+1}")
            axes[0, i].scatter([variables[i]], [coef[i] * variables[i]**2], color='red', label="Óptimo")
            axes[0, i].set_title(f"Variable {i+1}")
            axes[0, i].set_xlabel("x")
            axes[0, i].set_ylabel("f(x)")
            axes[0, i].legend()

        # Mostrar el valor óptimo general
        plt.figure(figsize=(6, 5))
        plt.scatter([0], [self.optimal_value], color='blue', label="Óptimo de la función objetivo")
        plt.axhline(self.optimal_value, color='blue', linestyle='--', alpha=0.7)
        plt.title("Valor óptimo de la función objetivo")
        plt.xlabel("Iteración")
        plt.ylabel("Valor de la función objetivo")
        plt.legend()
        plt.show()
        

# Ejemplo de uso

def restriccion(vars):
    # Define tu restricción aquí, por ejemplo:
    return sum(vars) - 100

solver = Solver(3)  # Suponiendo que tenemos 3 variables
coef = [5, 3, 1]  # Coeficientes para las variables
solver.solve(coef, restriccion)
print(solver.get_solution())
solver.graficar(coef)

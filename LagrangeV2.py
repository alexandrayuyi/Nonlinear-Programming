import sympy as sp
from scipy.optimize import minimize
import numpy as np

class InvestmentOptimizer:
    def __init__(self):
        self.x, self.y, self.lambda1, self.lambda2 = sp.symbols('x y lambda1 lambda2')
        self.params = {}
        
    def set_parameters(self, a, b, c, d, e):
        self.params = {'a': a, 'b': b, 'c': c, 'd': d, 'e': e}
        
    def formulate_lagrange(self):
        a, b, c, d, e = self.params.values()
        
        # Función objetivo
        f = a * self.x + b * self.y
        
        # Restricciones
        g1 = self.x + self.y - 1
        g2 = c * self.x**2 + d * self.y**2 - e
        
        # Función de Lagrange
        L = f - self.lambda1 * g1 - self.lambda2 * g2
        
        # Derivadas parciales
        self.L_x = sp.diff(L, self.x)
        self.L_y = sp.diff(L, self.y)
        self.L_lambda1 = sp.diff(L, self.lambda1)
        self.L_lambda2 = sp.diff(L, self.lambda2)
        
        return L
    
    def print_lagrange_formulation(self):
        L = self.formulate_lagrange()
        print("Formulación de Lagrange:")
        print(f"L = {L}")
        print(f"∂L/∂x = {self.L_x}")
        print(f"∂L/∂y = {self.L_y}")
        print(f"∂L/∂λ1 = {self.L_lambda1}")
        print(f"∂L/∂λ2 = {self.L_lambda2}")
    
    def objective(self, vars):
        a, b = self.params['a'], self.params['b']
        return -(a * vars[0] + b * vars[1])
    
    def constraint1(self, vars):
        return vars[0] + vars[1] - 1
    
    def constraint2(self, vars):
        c, d, e = self.params['c'], self.params['d'], self.params['e']
        return e - (c * vars[0]**2 + d * vars[1]**2)
    
    def solve(self):
        cons = ({'type': 'eq', 'fun': self.constraint1},
                {'type': 'ineq', 'fun': self.constraint2})
        
        x0 = [0.5, 0.5]
        res = minimize(self.objective, x0, method='SLSQP', constraints=cons)
        
        return {
            'x': res.x[0],
            'y': res.x[1],
            'max_return': -res.fun,
            'success': res.success,
            'message': res.message
        }

def Sample() -> None:
    optimizer = InvestmentOptimizer()
    
    print("Bienvenido al Optimizador de Inversiones")
    print("Por favor, ingrese los siguientes parámetros:")
    
    a = float(input("a (coeficiente de x en la función objetivo): "))
    b = float(input("b (coeficiente de y en la función objetivo): "))
    c = float(input("c (coeficiente de x^2 en la restricción de riesgo): "))
    d = float(input("d (coeficiente de y^2 en la restricción de riesgo): "))
    e = float(input("e (límite de riesgo): "))
    
    optimizer.set_parameters(a, b, c, d, e)
    
    print("\nFormulación del problema:")
    optimizer.print_lagrange_formulation()
    
    print("\nResolviendo el problema de optimización...")
    result = optimizer.solve()
    
    print("\nResultados:")
    print(f"x óptimo: {result['x']:.4f}")
    print(f"y óptimo: {result['y']:.4f}")
    print(f"Rendimiento máximo: {result['max_return']:.4f}")
    print(f"Éxito: {result['success']}")
    print(f"Mensaje: {result['message']}")

    ...

if __name__ == "__main__":
    ...
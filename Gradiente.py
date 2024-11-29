import numpy as np
import matplotlib.pyplot as plt

class GradientDescentOptimizer:
    def __init__(self, objective_func, gradient_func, initial_point, learning_rate, iterations):
        self.objective_func = objective_func
        self.gradient_func = gradient_func
        self.point = np.array(initial_point)
        self.learning_rate = learning_rate
        self.iterations = iterations
        self.history = []

    def optimize(self):
        for _ in range(self.iterations):
            value = self.objective_func(*self.point)
            self.history.append(value)
            
            gradient = self.gradient_func(*self.point)
            self.point -= self.learning_rate * gradient

        return self.point, self.history

    def plot_history(self):
        plt.figure(figsize=(10, 6))
        plt.plot(range(self.iterations), self.history)
        plt.title('Evolución del valor de la función objetivo')
        plt.xlabel('Iteraciones')
        plt.ylabel('Valor de la función')
        plt.grid(True)
        plt.show()

# Función objetivo específica
def objective(x, y, z):
    return x**2 + y**2 + z**2 - 2*x*y + 3*z

# Gradiente de la función objetivo
def gradient(x, y, z):
    dx = 2*x - 2*y
    dy = 2*y - 2*x
    dz = 2*z + 3
    return np.array([dx, dy, dz])

# Entrada de usuario
x0 = float(input("Ingrese el valor inicial de x: "))
y0 = float(input("Ingrese el valor inicial de y: "))
z0 = float(input("Ingrese el valor inicial de z: "))
learning_rate = float(input("Ingrese el tamaño del paso (learning rate): "))
iterations = int(input("Ingrese el número de iteraciones: "))

# Crear y ejecutar el optimizador
optimizer = GradientDescentOptimizer(objective, gradient, [x0, y0, z0], learning_rate, iterations)
optimal_point, history = optimizer.optimize()

print(f"Punto óptimo encontrado: {optimal_point}")
print(f"Valor mínimo de la función: {objective(*optimal_point)}")

# Graficar la evolución de la función
optimizer.plot_history()
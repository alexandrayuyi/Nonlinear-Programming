import numpy as np
import matplotlib.pyplot as plt


class GradientDescentOptimizer:
    
    def __init__(self, **kwargs) -> None:
        self.object_fuc = kwargs['fuction']
        self.gradient_func = kwargs['gradient']
        self.point = np.array(kwargs['initial'])
        self.learning_rate = kwargs['learning_rate']
        self.iterations = kwargs['iterations']
        self.history = []
        ...

    def optimize(self):
        for _ in range(self.iterations):
            value = self.object_fuc(*self.point)
            self.history.append(value)
            
            gradient = self.gradient_func(*self.point)
            self.point -= self.learning_rate * gradient

        return self.point, self.history

    def plot_history(self) -> None:
        plt.figure(figsize=(10, 6))
        plt.plot(range(self.iterations), self.history)
        plt.title('Evolución del valor de la función objetivo')
        plt.xlabel('Iteraciones')
        plt.ylabel('Valor de la función')
        plt.grid(True)
        plt.show()
        ...

    def __str__(self) -> str:
        return "x**2 + y**2 + z**2 - 2*x*y + 3*z"
        
def Sample()-> None:
    def function(x, y, z):
        return x**2 + y**2 + z**2 - 2*x*y + 3*z
    
    def gradient(x, y, z): 
        return np.array([2*x-2*y, 2*y-2*x, 2*z +3])

    # Crear y ejecutar el optimizador
    optimizer = GradientDescentOptimizer(
        fuction=function,
        gradient=gradient,
        initial=[1.0, 1.0, 1.0],
        learning_rate=0.1,
        iterations=15
    )
    optimal_point, history = optimizer.optimize()
    print(f"Punto óptimo encontrado: {optimal_point}")
    print(f"Valor mínimo de la función: {function(*optimal_point)}")
    print(optimizer)

    # Graficar la evolución de la función
    optimizer.plot_history()
    ...
    
if __name__ == "__main__":
    ...


class Trabajo():

    __n: int
    __b: []
    __c1: int
    __c2: int
    __c3: int
    __memo: {}
    __best_decisions: {}

    def __init__(self, n=0, b=[], C1=0, C2=0, C2Mas=0) -> None:
        self.__n = n
        self.__b = b
        self.__c1 = C1
        self.__c2 = C2
        self.__c3 = C2Mas
 
    def optimize_workforce(self) -> dict:
        self.__memo = {}
        self.__best_decisions = {}
        
        def f(i, x_prev) -> float:
            if i > self.__n:
                return 0
                
            if (i, x_prev) in self.__memo:
                return self.__memo[(i, x_prev)]
                
            min_cost = float('inf')
            best_x = None
            
            for x_i in range(self.__b[i-1], max(self.__b) + 1):
                if x_i > x_prev:
                    # Costo fijo de 400 + 200 por cada trabajador nuevo
                    change_cost = self.__c2 + self.__c3 * (x_i - x_prev)
                elif x_i < x_prev:
                    change_cost = self.__c1 * (x_prev - x_i)
                else:
                    change_cost = 0
                    
                excess_cost = self.__c1 * max(0, x_i - self.__b[i-1])
                total_cost = change_cost + excess_cost + f(i + 1, x_i)
                
                if total_cost < min_cost:
                    min_cost = total_cost
                    best_x = x_i
                    
                if min_cost == total_cost:
                    self.__best_decisions[(i, x_prev)] = (best_x, total_cost - f(i + 1, x_i))
                    
            self.__memo[(i, x_prev)] = min_cost
            return min_cost
        
        optimal_cost = f(1, 0)
        
        workers = [0]
        costs = []
        decisions = []
        current_workers = 0
        
        for i in range(1, self.__n+1):
            next_workers, cost = self.__best_decisions[(i, current_workers)]
            workers.append(next_workers)
            costs.append(cost)
            
            if next_workers > current_workers:
                decision = f"Contratar {next_workers - current_workers} trabajadores"
                # El costo incluye el costo fijo (400) más el costo por trabajador (200 * número de nuevos)
                # más el costo por excedente si aplica
                excess = max(0, next_workers - self.__b[i-1])
                costs[-1] = self.__c2 + self.__c3 * (next_workers - current_workers) + self.__c1 * excess
            elif next_workers < current_workers:
                decision = f"Despedir {current_workers - next_workers} trabajadores"
                costs[-1] = self.__c1 * (current_workers - next_workers)
            else:
                decision = "Ningún cambio"
                costs[-1] = self.__c1 * max(0, next_workers - self.__b[i-1])
                
            decisions.append(decision)
            current_workers = next_workers

        print("\nResultados de la optimización:")
        print("-" * 80)
        print(f"{'Semana':^10} | {'Fuerza mínima':^15} | {'Fuerza real':^15} | {'Decisión':^20} | {'Costo ($)':^10}")
        print("-" * 80)
        
        for i in range(self.__n):
            print(f"{i+1:^10} | {self.__b[i]:^15} | {workers[i+1]:^15} | {decisions[i]:^20} | {costs[i]:^10}")
        
        print("-" * 80)
        print(f"\nEl costo total de mano de obra para el proyecto es de ${sum(costs)}")

        return {
            'costo_total': sum(costs),
            'trabajadores_por_semana': workers[1:],
            'decisiones': decisions,
            'costos_por_semana': costs
        }

# Ejemplo de uso
if __name__ == "__main__":
    n_semanas = 5
    trabajadores_requeridos = [5, 7, 8, 4, 6]  # b_i para cada semana
    costo_excedente = 300  # C1
    costo_contratacion = 400  
    costo_contratacion_EX = 200 # C2 (400 + 200)
    
    sample = Trabajo(n_semanas, trabajadores_requeridos, costo_excedente, costo_contratacion, costo_contratacion_EX)
    print("Modelo de tamaño de la fuerza de trabajo")
    print("----------------------------------------")
    resultado = sample.optimize_workforce()

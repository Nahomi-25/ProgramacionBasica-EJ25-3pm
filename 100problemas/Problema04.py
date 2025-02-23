def fibonacci(n):
    fib_sequence = [0, 1]  # Inicia con los dos primeros números de la serie.
    
    # Si n es 1, solo devuelve el primer número.
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    
    # Genera la serie hasta el número n.
    for i in range(2, n):
        next_fib = fib_sequence[-1] + fib_sequence[-2]  
        # Suma los dos últimos números.
        fib_sequence.append(next_fib)
    
    return fib_sequence

n = int(input("¿Cuántos números de la serie de Fibonacci quieres generar? "))
print(fibonacci(n))
import time


def factorial(n):
    """
    Function that calculates the factorial of a number using recursion.
    This function will be used to see the progress of the asymptotic complexity
    according to the size of n.
    """
    if n < 0:
        return "Invalid input"
    if n == 0 or n == 1:
        return 1
    
    else:
        return factorial(n - 1) * n


if __name__ == "__main__":
    numbers = [10, 100, 500, 750]

    print("Starting tests...\n")

    for n in numbers:
        start_time = time.time()
        factorial_n = factorial(n)
        end_time = time.time()

        execution_duration = end_time - start_time

        print(f"Factorial of {n}: {factorial_n}")
        print(f"Execution time: {execution_duration:.8f} seconds")

    print("\n--- Test Completed ---")
    print(f"""
--- Análise de Complexidade Assintótica ---
Esta função fatorial recursiva opera com complexidade de tempo $O(n)$, o que significa 
que o esforço computacional cresce linearmente conforme o valor da entrada aumenta. 
No entanto, o ponto crítico é a complexidade de espaço, também de $O(n)$: cada chamada 
fica 'pendurada' na pilha de execução (call stack) até que o caso base seja atingido. 
Portanto, dobrar o valor de $n$ não apenas dobra o tempo de execução, mas também o 
consumo de memória RAM, tornando esta abordagem arriscada para valores muito elevados 
devido ao limite de recursão do sistema.
-------------------------------------------
""")
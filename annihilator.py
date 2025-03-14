import random
import multiprocessing

def compute_randoms(iterations):
    results = []
    for _ in range(iterations):
        a = random.random()
        b = random.random()
        c = random.random()
        d = random.random()

        wynik1 = a * b + c * d
        wynik2 = a + b * c * d
        wynik3 = a + b + c * d
        wynik4 = a * b * c * d

        results.append((a, b, c, d, wynik1, wynik2, wynik3, wynik4))

    return results

def worker(iterations):
    return compute_randoms(iterations)

def main():
    iterations_per_process = 10_000_000  
    num_processes = multiprocessing.cpu_count()  

    with multiprocessing.Pool(processes=num_processes) as pool:
        results = pool.map(worker, [iterations_per_process] * num_processes)

    for result in results:
        for a, b, c, d, wynik1, wynik2, wynik3, wynik4 in result:
            print(f"a: {a}, b: {b}, c: {c}, d: {d}")
            print(f"wynik1: {wynik1}, wynik2: {wynik2}, wynik3: {wynik3}, wynik4: {wynik4}")

if __name__ == "__main__":
    multiprocessing.freeze_support()  
    main()

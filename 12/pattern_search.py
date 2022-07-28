from functools import wraps
from timeit import default_timer as timer
from typing import Tuple, List

index = int


def time_it(func):
    """ Dekorator do mierzenia czasu działania metod """
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = timer()
        result = func(*args, **kwargs)
        end = timer()
        return result, end - start

    return wrapper


def solution_printer(filename: str, pattern: str, method: callable):
    # przygotowanie danych wejściowych
    with open(filename, encoding='utf-8') as f:
        text = f.readlines()
    merged_string = ''.join(text).lower()
    pattern = pattern.lower()

    print("="*20)
    (matches, comparisons), time = method(merged_string, pattern)
    if isinstance(comparisons, tuple):
        comparisons, errors = comparisons
    else:
        errors = None
    print(f'W pliku {filename} znaleziono {len(matches)} pasujących wyrazów do wzorca "{pattern}".')
    print(f'Znalezione indeksy: {matches}.')
    print(f'Czas wykonania algorytmu wynosi {time*1000:.5f} ms.')
    print(f'Wykonano {comparisons} porównań.')
    if errors is not None:
        print(f'Funkcja hashująca spowodowała {errors} błędów.')
    print("=" * 20)


@time_it
def naive_method(merged_string: str, pattern: str) -> Tuple[List[index], int]:
    comparison_counter = 0
    found_instances: List[index] = []
    for m in range(len(merged_string) - len(pattern)):
        if pattern == merged_string[m:m+len(pattern)]:
            found_instances.append(m)
        comparison_counter += 1
    return found_instances, comparison_counter


def rolling_hash(substring: str) -> int:
    base = 256
    prime_modulus = 101
    hash_value = (ord(substring[0]) * base) % prime_modulus
    for letter in substring[1:]:
        hash_value = (hash_value * ord(letter)) % prime_modulus
    return hash_value


@time_it
def rabin_karp_method(merged_string: str, pattern: str) -> Tuple[List[index], Tuple[int, int]]:
    comparison_counter = 0
    found_instances: List[index] = []
    hashing_errors = 0
    pattern_hash = rolling_hash(pattern)
    for m in range(len(merged_string) - len(pattern)):
        substring = merged_string[m:m+len(pattern)]
        if pattern_hash == rolling_hash(substring):
            if pattern == substring:
                found_instances.append(m)
            else:
                hashing_errors += 1
            comparison_counter += 1
    return found_instances, (comparison_counter, hashing_errors)


def kmp_table(pattern: str):
    pos = 1
    cnd = 0
    T = [-1] + [0 for _ in range(len(pattern))]

    while pos < len(pattern):
        if pattern[pos] == pattern[cnd]:
            T[pos] = pattern[cnd]
        else:
            T[pos] = cnd
            while cnd >= 0 and pattern[pos] != pattern[cnd]:
                cnd = T[cnd]
        pos += 1
        cnd += 1
    T[pos] = cnd
    return T


@time_it
def knuth_morris_pratt_method(merged_string: str, pattern: str) -> Tuple[List[index], int]:
    comparison_counter = 0
    found_instances: List[index] = []
    j = 0
    k = 0
    T = kmp_table(pattern)
    while j < len(merged_string):
        comparison_counter += 1
        if pattern[k] == merged_string[j]:
            j += 1
            k += 1
            if k == len(pattern):
                found_instances.append(j - k)
                k = T[k]
        else:
            k = T[k]
            if k < 0:
                j += 1
                k += 1
    return found_instances, comparison_counter


print("Metoda naiwna")
solution_printer(filename='lotr.txt', pattern='time.', method=naive_method)
print("Metoda Rabin-Karp")
solution_printer(filename='lotr.txt', pattern='time.', method=rabin_karp_method)
print("Metoda Knuth-Morris-Pratt")
solution_printer(filename='lotr.txt', pattern='time.', method=knuth_morris_pratt_method)

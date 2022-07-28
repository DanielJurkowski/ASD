import time


def text_to_string(text):
    with open(text, encoding='utf-8') as f:
        opened_text = f.readlines()

    string = ' '.join(opened_text).lower()

    return string


def naive(string, template):
    M = len(string)
    N = len(template)

    matched = False

    m = 0
    counter = 0
    while m < M:
        if string[m:m + N] == template:
            matched = True
            counter += 1

        m += 1

    if matched is True:
        return counter, m

    else:
        return False


def hash(string, template_length):
    d = 256
    q = 101

    hash = 0
    for i in range(template_length):
        hash = (d * hash + ord(string[i])) % q

    return hash


def rabin_karp(string, template):
    M = len(string)
    N = len(template)

    compare = 0
    counter = 0
    different_string = 0

    d = 256
    q = 101

    h = 1
    for i in range(N - 1):
        h = (h * d) % q

    hash_T = hash(template, N)
    hash_S = hash(string[0:N], N)

    matched = False
    for m in range(0, M - N + 1):
        compare += 1
        if hash_S == hash_T:
            if string[m:m + N] == template:
                matched = True
                counter += 1

            else:
                different_string += 1

        if m + N < M:
            hash_S = (d * (hash_S - ord(string[m]) * h) + ord(string[m + N])) % q

            if hash_S < 0:
                hash_S += q

    if matched:
        return counter, compare, different_string

    if not matched:
        return False


def kmp_table(template):
    position = 1
    candidate = 0

    table = [0 for i in range(len(template))]
    table = [-1] + table

    while position < len(template):
        if template[position] == template[candidate]:
            table[position] = table[candidate]

        else:
            table[position] = candidate

            while candidate >= 0 and template[position] != template[candidate]:
                candidate = table[candidate]

        position += 1
        candidate += 1

    table[position] = candidate

    return table


def knuth_morris_pratt(string, template):
    compare = 0
    counter = 0

    m = 0
    i = 0
    table = kmp_table(template)

    while m < len(string):
        compare += 1
        if template[i] == string[m]:
            m += 1
            i += 1

            if i == len(template):
                counter += 1
                i = table[i]

        else:
            i = table[i]

            if i < 0:
                m += 1
                i += 1

    return counter, compare



def main():
    string_lotr = text_to_string("lotr.txt")
    template = "time."

    # metoda naiwna
    t_start = time.perf_counter()
    match_naive = naive(string_lotr, template)
    t_stop = time.perf_counter()
    print(match_naive, "| Czas obliczeń:", "{:.7f}".format(t_stop - t_start))

    # metoda Rabina-Karpa
    t_start = time.perf_counter()
    match_rabin_karp = rabin_karp(string_lotr, template)
    t_stop = time.perf_counter()
    print(match_rabin_karp, "| Czas obliczeń:", "{:.7f}".format(t_stop - t_start))

    # metoda Knuth_Morris_Pratt
    t_start = time.perf_counter()
    match_knuth_morris_pratt = knuth_morris_pratt(string_lotr, template)
    t_stop = time.perf_counter()
    print(match_knuth_morris_pratt, "| Czas obliczeń:", "{:.7f}".format(t_stop - t_start))

main()

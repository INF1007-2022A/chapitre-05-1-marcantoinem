#!/usr/bin/env python
# -*- coding: utf-8 -*-


from typing import List
import math

def convert_to_absolute(number: float) -> float:
    if number < 0:
        return -number
    return number


def use_prefixes() -> List[str]:
    prefixes, suffixe = 'JKLMNOPQ', 'ack'
    name = []
    for prefixe in prefixes:
        name.append(prefixe + suffixe)
    return name


def prime_integer_summation() -> int:
    max = 100
    primes = [True for _ in range(max+1)]
    for i in range(2, max // 2):
        prime = primes[i]
        if prime:
            for j in range(2, max // i + 1):
                primes[i*j] = False
    sum = 0
    for i in range(2,100):
        if primes[i]:
            sum += i
    return sum


def factorial(number: int) -> int:
    product = 1
    for n in range(2,number+1):
        product *= n
    return product


def use_continue() -> None:
    for i in range(1,11):
        if i == 5:
            continue
        print(i)


def verify_ages(groups: List[List[int]]) -> List[bool]:
    result = []
    for group in groups:
        if len(group) > 10 or len(group) <= 3:
            result.append(False)
            continue
        old = False
        fifty = False
        accepted = True
        for age in group:
            if age == 25:
                break
            elif age < 18:
                accepted = False
                break
            elif age == 50:
                fifty = True
                if old:
                    accepted = False
                    break
            elif age > 70:
                old = True
                if fifty:
                    accepted = False
                    break
        result.append(accepted)
    return result

def main() -> None:
    number = -4.325
    print(f"La valeur absolue du nombre {number} est {convert_to_absolute(number)}")

    print(f"La liste des noms générés avec les préfixes est: {use_prefixes()}")

    print(f"La somme des 100 premiers nombre premier est : {prime_integer_summation()}")

    number = 10
    print(f"La factiorelle du nombre {number} est: {factorial(number)}")
    
    print(f"L'affichage de la boucle est:")
    use_continue()

    groups = [
        [15, 28, 65, 70, 72], [18, 24, 22, 50, 70], [25, 2],
              [20, 22, 23, 24, 18, 75, 51, 49, 100, 18, 20, 20], [70, 50, 26, 28], [75, 50, 18, 25],
              [13, 25, 80, 15], [20, 30, 40, 50, 60], [75, 50, 100, 28]
    ]
    print(f"Les différents groupes sont: {groups}")
    print(f"L'acceptance des groupes est: {verify_ages(groups)}")


if __name__ == '__main__':
    main()

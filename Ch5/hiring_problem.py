"""
The average cost the of hiring problem is O(ln(n)) where n is the total num of candidates. Simulate the same.
The cost of the hiring problem is defined as being directly proportional to the number of replacements made 
to a position while interviewing n candidates
"""
import random


def hiring(talent_pool):
    best = -float("inf")
    n_replacements = 0
    for candidate in talent_pool:
        if candidate > best:
            best = candidate
            n_replacements += 1
    return n_replacements


def average(n_trials, n_candidates_per_trial):
    s = 0
    talent = list(range(1, n_candidates_per_trial + 1))
    for _ in range(n_trials):
        random.shuffle(talent)
        s += hiring(talent)
    return s / n_trials


if __name__ == "__main__":
    n_candidates = map(int, [1e5, 1e6])
    # the ratio of cost would be approx log(1e5)/log(1e6) = 0.8333
    n_trials = 100
    results = []
    for i in n_candidates:
        print(i)
        results.append(average(n_trials, i))
    print(results[0] / results[1])  # got 0.816 for a trial size of 100

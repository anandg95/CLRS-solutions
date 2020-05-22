"""Defined as the bins and balls problem - a process of throwing balls into b identical bins.
How many balls must we throw until every bin has atleast one ball. This can be rephrased as the
coupon collector's problem - Expected number of random coupons to be acquired so that he has atleast
1 coupon of `b` different kinds. The result is b(ln(b) + O(1))"""

import random


def problem(b: list):
    n_trials = 10000
    results = []
    for _ in range(n_trials):
        n_attempts_to_success = 0
        coupons_acquired = set()
        while True:
            n_attempts_to_success += 1
            c = random.choice(b)
            coupons_acquired.add(c)
            if len(coupons_acquired) == len(b):
                break
        results.append(n_attempts_to_success)
    ans = sum(results) / len(results)
    print(f"Number of attempts needed for {len(b)} coupons : {ans}")


problem(list(range(1000)))
"""
| n_coupons  | n_attempts |
|------------|------------|
|    10      |    29      |
|   100      |    517     |
|   100      |    7477    |

Comes to approximately b(ln(b) + 0.6)
"""

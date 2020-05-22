"""Part 1 - Number of people to be present at a party so that the expected number of pairs of people sharing
the same bday is at least 1 is 28"""
import random


def n_common(sample):
    "Number of non-unique elements in a list"
    return len(sample) - len(set(sample))


def problem1():
    bdays = list(range(1, 366))
    n_trials = 10000
    for n_people in bdays:
        print(n_people)
        sample_sum = 0
        for _ in range(n_trials):
            sample = [random.choice(bdays) for __ in range(n_people)]
            n_common_bdays = n_common(sample)
            sample_sum += n_common_bdays
        avg = sample_sum / n_trials
        if avg >= 1:
            print("The number of people needed = " + str(n_people))
            break
            # this indeed comes out to 28


"""Part 2 - The number of people to be present at a party so that the probability of atleast 2 people sharing the
same bday is greater than 50 %. This is the complement of all bdays being unique. The value comes to 23."""


def all_unique(sample):
    "True if there is at least one non unique element"
    return len(set(sample)) == len(sample)


def problem2():
    bdays = list(range(1, 366))
    n_trials = 10000
    for n_people in bdays:
        print(n_people)
        n_unique = 0
        for _ in range(n_trials):
            sample = [random.choice(bdays) for __ in range(n_people)]
            unique = all_unique(sample)
            n_unique += unique
        n_atleast_1_common = n_trials - n_unique
        if n_atleast_1_common / n_trials >= 0.5:
            print("The number of people needed = " + str(n_people))
            break
            # comes out to 23

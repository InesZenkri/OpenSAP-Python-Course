import random
import statistics

def gaussian_distribution():
    random_list = [random.gauss(100, 10) for n in range(1000)]
    print(random_list)
    return random_list

global_random_list = gaussian_distribution()

print("Mean:", statistics.mean(global_random_list))
print("Standard Deviation:", statistics.stdev(global_random_list))
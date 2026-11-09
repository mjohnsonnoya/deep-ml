from collections import defaultdict
def empirical_pmf(samples):
    """
    Given an iterable of integer samples, return a list of (value, probability)
    pairs sorted by value ascending.
    """
    # TODO: Implement the function
    n = len(samples)

    counts = defaultdict(int)

    for sample in samples:
        counts[sample] += 1
    
    ans = []

    for integer, count in counts.items():
        ans.append((integer, count/n))
    
    ans.sort(key=lambda x: x[0])

    return ans
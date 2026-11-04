import numpy as np
import math

def descriptive_statistics(data: list | np.ndarray) -> dict:
    """
    Calculate various descriptive statistics metrics for a given dataset.
    
    Args:
        data: List or numpy array of numerical values
    
    Returns:
        Dictionary containing mean, median, mode, variance, standard deviation,
        percentiles (25th, 50th, 75th), and interquartile range (IQR)
    """
    # Your code here
    length = len(data)

    mean = sum(data)/length
    median = (data[math.floor((length - 1) * 0.5)] + data[math.ceil((length - 1) * 0.5)]) / 2

    mode = data[0]
    maxfreq = 1

    count = {}
    for datum in data:
        if datum not in count:
            count[datum] = 0
        count[datum] += 1
    
        if count[datum] > maxfreq:
            mode = datum
            maxfreq = count[datum]
    
    variance = 1/length * sum((val - mean)**2 for val in data)
    standard_deviation = np.sqrt(variance)

    percentile_25 = (data[math.floor((length - 1) * 0.25)] + data[math.ceil((length - 1) * 0.25)]) / 2
    percentile_50 = median
    percentile_75 = (data[math.floor((length - 1) * 0.75)] + data[math.ceil((length - 1) * 0.75)]) / 2

    interquartile_range = percentile_75 - percentile_25

    return {
        'mean': mean,
        'median': median,
        'mode': mode,
        'variance': variance,
        'standard_deviation': standard_deviation,
        '25th_percentile': percentile_25,
        '50th_percentile': percentile_50,
        '75th_percentile': percentile_75,
        'interquartile_range': interquartile_range
    }



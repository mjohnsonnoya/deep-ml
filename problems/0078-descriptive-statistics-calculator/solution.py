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
    mean = sum(data)/len(data)

    median = (data[(len(data) - 1)//2] + data[math.ceil((len(data) - 1)/2)]) / 2

    count = {}

    mode = data[0]
    maxfreq = 1

    for value in data:
        if (value not in count):
            count[value] = 0
        
        count[value] += 1

        if count[value] > maxfreq:
            mode = value
            maxfreq = count[value]
    
    variance = sum((value - mean) ** 2 for value in data)/len(data)

    standard_deviation = math.sqrt(variance)

    percentile_25 = (data[math.floor((len(data) - 1)/4)] + data[math.ceil((len(data) - 1)/4)]) / 2

    percentile_50 = median
     
    percentile_75 = (data[math.floor((len(data) - 1) * 3/4)] + data[math.ceil((len(data) - 1)*3/4)]) / 2

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



    

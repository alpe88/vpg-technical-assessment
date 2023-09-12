def calculate_mean(temperatures):
    return sum(temperatures)/len(temperatures)


def find_median(temperatures):
    temperatures.sort()
    n = len(temperatures)

    # The median number is either the middle element of an odd length array or the average of the middle two when length is even
    if n % 2 == 1:
        return temperatures[n // 2]
    else:
        middle_left = temperatures[(n // 2) - 1]
        middle_right = temperatures[n // 2]
        return (middle_left + middle_right) / 2.0


def calculate_standard_deviation(temperatures):
    mean = calculate_mean(temperatures)
    squared_differences = [(x - mean) ** 2 for x in temperatures]
    variance = sum(squared_differences) / len(temperatures)
    standard_deviation = variance ** 0.5
    return standard_deviation

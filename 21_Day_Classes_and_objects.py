import statsmodels
##Day 21
##Level 1
#1
class Statistics:
    
    def __init__(self, data):
        self.data = data
        
    def count(self):
        return len(self.data)
    
    def min(self):
        return min(self.data)
    
    def max(self):
        return max(self.data)
    
    def range(self):
        return max(self.data) - min(self.data)
    
    def mean(self):
        return sum(self.data) / len(self.data)
    
    def median(self):
        sorted_data = sorted(self.data)
        n = len(sorted_data)
        mid = n // 2
        if n % 2 == 0:
            return (sorted_data[mid - 1] + sorted_data[mid]) / 2
        else:
            return sorted_data[mid]
        
    def mode(self):
        freq_dict = {}
        for item in self.data:
            if item in freq_dict:
                freq_dict[item] += 1
            else:
                freq_dict[item] = 1
        mode_freq = max(freq_dict.values())
        modes = [item for item, freq in freq_dict.items() if freq == mode_freq]
        return modes[0]
    
    def variance(self):
        mu = self.mean()
        return sum((x - mu) ** 2 for x in self.data) / len(self.data)
    
    def std_dev(self):
        return self.variance() ** 0.5
    
    def percentile(self, p):
        sorted_data = sorted(self.data)
        n = len(sorted_data)
        k = (n - 1) * (p / 100)
        f = math.floor(k)
        c = math.ceil(k)
        if f == c:
            return sorted_data[int(k)]
        else:
            d0 = sorted_data[int(f)] * (c - k)
            d1 = sorted_data[int(c)] * (k - f)
            return d0 + d1
    
    def frequency_distribution(self):
        freq_dict = {}
        for item in self.data:
            if item in freq_dict:
                freq_dict[item] += 1
            else:
                freq_dict[item] = 1
        return freq_dict


print("Count:", stats.count())
print("Min:", stats.min())
print("Max:", stats.max())
print("Range:", stats.range())
print("Mean:", stats.mean())
print("Median:", stats.median())
print("Mode:", stats.mode())
print("Variance:", stats.variance())
print("Standard Deviation:", stats.std_dev())
print("25th Percentile:", stats.percentile(25))
print("50th Percentile (Median):", stats.percentile(50))
print("75th Percentile:", stats.percentile(75))
print("Frequency Distribution:", stats.frequency_distribution())




























import pandas as pd
import matplotlib.pyplot as plt

class TrendAnalyzer:
    def __init__(self, data):
        self.data = pd.DataFrame(data)

    def calculate_trend(self):
        self.data['Trend'] = self.data['Value'].diff().apply(lambda x: 1 if x > 0 else -1)
        return self.data

    def plot_trend(self):
        plt.figure(figsize=(10, 6))
        plt.plot(self.data['Value'], label='Value')
        plt.plot(self.data['Trend'], label='Trend')
        plt.legend()
        plt.show()

def main():
    data = {
        'Date': ['2022-01-01', '2022-01-02', '2022-01-03', '2022-01-04', '2022-01-05'],
        'Value': [10, 15, 20, 18, 22]
    }
    analyzer = TrendAnalyzer(data)
    trend_data = analyzer.calculate_trend()
    print(trend_data)
    analyzer.plot_trend()

if __name__ == "__main__":
    main()
```

Kodda Trend Analyzer uchun quyidagi funksiyalar mavjud:

1. `calculate_trend`: Bu funksiya ma'lumotlar framening 'Trend' sifatida yangi stolni yaratadi. Ushbu stolda har bir qadamning o'zgarishi 0 dan katta bo'lsa, trend 1 ga teng bo'ladi, aks holda -1 ga teng bo'ladi.

2. `plot_trend`: Bu funksiya trendni grafikda ko'rsatadi. Grafikda ikkita chiziq mavjud bo'ladi: birinchisi ma'lumotlar framening 'Value' stolining qiymatlarini ko'rsatadi, ikkinchisi esa trendni ko'rsatadi.

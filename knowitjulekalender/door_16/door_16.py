from collections import defaultdict
import numpy as np
from itertools import cycle


def parse_chart(chart_file):
    with open(chart_file, 'r') as f:
        chart = []
        for _ in f:
            chart.append(list(_.rstrip("\n")))

    chart = chart[::-1]
    chart = np.transpose(chart)
    price_dict = defaultdict(list)

    for hour, price in zip(cycle(range(1, 25)), chart):
        price = ''.join(list(price))
        price = len(price) - len(price.lstrip())
        price_dict[hour].append(price)

    return price_dict


def main():
    chart_this_year = parse_chart('strømpriser.txt')
    chart_next_year = parse_chart('strømpriser_next.txt')

    chart_this_year_sum = {k: sum(v) for k, v in chart_this_year.items()}
    chart_next_year_sum = {k: sum(v) for k, v in chart_next_year.items()}

    cheapest_hour_this_year = min(chart_this_year_sum, key=chart_this_year_sum.get)

    # Strategy 1:
    sum_strategy_1 = chart_next_year_sum[cheapest_hour_this_year]

    # Strategy 2:
    sum_strategy_2 = 0
    skip = False
    for n, (hour_this_year, hour_next_year) in enumerate(zip(chart_this_year[cheapest_hour_this_year],
                                                             chart_next_year[cheapest_hour_this_year])):
        if skip:
            skip = False
            continue
        sum_strategy_2 += hour_next_year
        if chart_this_year[cheapest_hour_this_year][n + 1] > hour_this_year:
            skip = True
            sum_strategy_2 += chart_next_year[cheapest_hour_this_year + 1][n]

    # Result:
    winning_strategy = 1 if sum_strategy_1 < sum_strategy_2 else 2
    price_diff = abs(sum_strategy_1 - sum_strategy_2)

    print('%i,%i' % (winning_strategy, price_diff))


if __name__ == '__main__':
    main()

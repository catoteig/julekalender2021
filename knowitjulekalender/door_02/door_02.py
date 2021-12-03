import csv
from haversine import haversine

START_POSITION = (90, 0)


def csv_to_dict(csv_file):

    with open(csv_file, mode='r') as f:
        reader, result = csv.reader(f), {}
        next(reader)
        for city, coords in reader:
            coords = coords[6:-1].split()
            result[(float(coords[1]), float(coords[0]))] = city
    return result


def main():

    city_list = csv_to_dict('cities.csv')
    curr_pos, traveled = START_POSITION, 0

    while city_list:
        closest_distance, closest_city = float('inf'), None

        for city in city_list:
            this_distance = haversine(curr_pos, city)
            if this_distance < closest_distance:
                closest_distance = this_distance
                closest_city = city

        curr_pos = closest_city
        traveled += closest_distance
        city_list.pop(closest_city)

    traveled += haversine(curr_pos, START_POSITION)

    print(round(traveled))


if __name__ == '__main__':
    main()

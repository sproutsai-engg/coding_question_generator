##Question ID: 1455

def filter_restaurants(restaurants, vegan_friendly, max_price, max_distance):
    def custom_compare(a, b):
        if a[1] == b[1]:
            return b[0] - a[0]
        return b[1] - a[1]

    filtered_restaurants = [
        r for r in restaurants
        if (vegan_friendly == 0 or r[2] == vegan_friendly) and r[3] <= max_price and r[4] <= max_distance
    ]

    filtered_restaurants.sort(key=lambda r: (r[1], r[0]), reverse=True)

    return [r[0] for r in filtered_restaurants]

## Structure
def filter_restaurants(restaurants, vegan_friendly, max_price, max_distance):
    # Your code here

    pass
from urllib.request import urlopen
from urllib.parse import quote, urlencode

def neighbors(city: str, country: str, d: float, s: float) -> set[(str,str)]:
    """
    :param city: strictly string represent the city to start
    :param country: strictly string represent the country of a given city
    :param d: positive float
    :param s: positive float
    :return: list of tuples each contains city name and country of neighbours reachable from the
    city input within the distance d and s
    """
    # The left join method is used, because I noticed there are cities in city table  fulfill the distance conditions
    # but they do not exist in location table.
    q = "SELECT c2.Name, c2.Country FROM City c1 LEFT OUTER JOIN located l1 ON c1.Name = l1.City, City c2 LEFT OUTER " \
        "JOIN located l2 ON c2.Name = l2.City WHERE c1.Country = '" + country + "' AND c1.Name = '" + city + \
        "' AND ((c1.Province = c2.Province) OR (l1.River = l2.River) OR (l1.Lake = l2.Lake) " \
        "OR ((l1.Sea = l2.Sea) AND (ABS(c1.Latitude-c2.Latitude) + ABS(c1.Longitude-c2.Longitude) < " + str(
        s) + ")) OR (ABS(c1.Latitude-c2.Latitude) + ABS(c1.Longitude-c2.Longitude) < " + str(
        d) + ")) AND c1.Name <> c2.Name"
    "AND ((c1.Province = c2.Province) OR (l1.River = l2.River) OR (l1.Lake = l2.Lake) " \
    "OR ((l1.Sea = l2.Sea) AND (ABS(c1.Latitude-c2.Latitude) + ABS(c1.Longitude-c2.Longitude) < " + str(s) + ")) OR (ABS(c1.Latitude-c2.Latitude) + ABS(c1.Longitude-c2.Longitude) < " + str(d) + "))"

    eq = quote(q)
    url = "http://kr.unige.ch/phpmyadmin/query.php?db=mondial&sql="+eq
    query_results = urlopen(url)
    neighbors = set()
    for line in query_results:
        string_line = line.decode('utf-8').rstrip()
        if len(string_line) > 0:
            city, country = string_line.split("\t")
            neighbors.add((city, country))
    query_results.close()
    return neighbors

def reachable_cities(city: str, country: str, k: int, d: float, s: float) -> dict[int, set[(str,str)]]:
    """
    :param city: strictly string represent the city to start
    :param country: strictly string represent the country of a given city
    :param k: positive integer represent the numbers of step
    :param d: positive float
    :param s: positive float
    :return: dictionary where the keys represent the steps and the values are the reachable cities and
    their respective country codes
    """
    reachable = {}                             # a dictionary to store the reachable cities by step
    cities_to_visit = [(city, country, 0)]     # a list to store the cities to visit next
    visited_cities = set()                     # a set to store the visited cities

    for i in range(1, k + 1):
        reachable[i] = set()
    while cities_to_visit:                     # iterate while the list is not empty (all the cities have been checked )
        next_city, c_country, steps = cities_to_visit.pop(0)  # Use pop method for checking the neighbors of first city from the list
        if steps < k:                          # insuring that no shorter sequence
            for n in neighbors(next_city, c_country, d, s):   # Find the neighbors of the current city
                if n not in visited_cities:
                    visited_cities.add(n)
                    reachable[steps+1].add(n)
                    cities_to_visit.append((n[0], n[1], steps+1))
    return reachable
print(reachable_cities("Geneva","CH",5,2,4))


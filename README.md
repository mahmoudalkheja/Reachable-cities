# Reachable-cities
The objective of this project is to write a Python program that uses a database to find all the cities reachable from a given city in a given number of steps.
A city c′ is reachable from a city c in k steps if there is a sequence of cities (c0,c1,...,ck) that satisfies the following conditions: 
1. c0 =candck =c′
2. all the ci’s are different
3. ci+1 isintheneighborhoodN(ci)ofci (i=0,...,k−1). N(ci)isdefined as the set of cities that are
• in the same province as ci or
• on the same river or lake as ci or
• on the same sea but at a distance less than s or • anywhere at a distance less than d
where s and d are given parameters and the distance between ci and cj is defined as
|ci.latitude − cj .latitude| + |ci.longitude − cj .longitude| 4. no shorter sequence satisfies conditions 1, 2, and 3.
Input: a city name n and a country code c (this is necessary because several cities may have the same name), an integer k (the maximum number of steps), two real numbers d and s (the maximum distance and the maxi- mum distance on seas), and the mondial database that contains informa- tion about cities, countries, lakes, and rivers.
Output:
a list of all cities reachable from n in 1, 2, ..., k steps.

travel_log = [
{
  "country": "France",
  "visits": 12,
  "cities": ["Paris", "Lille", "Dijon"]
},
{
  "country": "Germany",
  "visits": 5,
  "cities": ["Berlin", "Hamburg", "Stuttgart"]
},
]

#difficult level nanii huwezi elewa😂👀😂- go and read bruh
#Write the function that will allow new countries
#to be added to the travel_log.
def add_new_country(name, visit_count, cities_visited):
#creating a new dictionary that will be added to that list
  new_country = {}
  new_country["country"] = name
  new_country["visits"] = visit_count
  new_country["cities"] = cities_visited
  travel_log.append(new_country)

add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)
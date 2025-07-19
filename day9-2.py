Travel_log=[
    {'country': 'France', 'visits': 12, 'cities': ['Paris', 'Lille', 'Dijon']},
    {'country': 'Germany', 'visits': 5, 'cities': ['Berlin', 'Hamburg', 'Stuttgart']}
]
def add_new_country(country_visited, time_visits, cities_visits):
    new_country={}
    new_country["country"]=country_visited
    new_country["visits"]=time_visits
    new_country["cities"]=cities_visits
    Travel_log.append(new_country)
add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(Travel_log)
# create a dictionary with two items.
# Each item contain a key (string) and a value (list of string)
projects = {"Project1": ["Sam", "Tom"], "Project2": ["Tim", "Cooper"]}
# print out the keys of the dictionary
print(projects.keys())
# print out all items of the dictionary as (key, value) tuple pairs
print(projects.items())
# print out the values of each item in the dictionary
print(projects.values())

# check if "Project1" is a key in the projects dictionary
"Project1" in projects

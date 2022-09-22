# implement County class here
class County:
    def __init__(self, init_name, init_population, init_voters):
        self.name = init_name
        self.population = init_population
        self.voters = init_voters


def highest_turnout(data):
    # implement the function here
    name = data[0].name
    highest_turnout = data[0].voters / data[0].population
    for County in data:
        turnout = County.voters / County.population
        if turnout > highest_turnout:
            highest_turnout = turnout
            name = County.name
    return (name, highest_turnout)  # modify this as needed


# your program will be evaluated using these objects
# it is okay to change/remove these lines but your program
# will be evaluated using these as inputs
allegheny = County("allegheny", 1000490, 645469)
philadelphia = County("philadelphia", 1134081, 539069)
montgomery = County("montgomery", 568952, 399591)
lancaster = County("lancaster", 345367, 230278)
delaware = County("delaware", 414031, 284538)
chester = County("chester", 319919, 230823)
bucks = County("bucks", 444149, 319816)
data = [allegheny, philadelphia, montgomery, lancaster, delaware, chester, bucks]

result = highest_turnout(data)  # do not change this line!
print(result)  # prints the output of the function
# do not remove this line!

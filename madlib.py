madlib = """This is a story of a famous {animal}.  This {animal}'s name is {name}.
Not only was this a {adjective} {animal}, but this {animal} could perform {skill}!
One day {name} the {animal} made a friend named {friend}.
{friend} was amazed that {name} the {animal} was so {adjective} at {skill}.
{name} served {friend} some {dessert} that proved to be {adjective}.
It was a {adjective} day afterall!
The end.
"""
print(madlib.format(animal=input("animal "), name=input("name "),
    adjective=input("adjective "), skill=input("skill "),friend=input("friend "), dessert=input("dessert ")))

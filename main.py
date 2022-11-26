#!/usr/bin/python

from marvel import Marvel

# "Data provided by Marvel. © 2014 Marvel"

m = Marvel(PUBLIC_KEY, PRIVATE_KEY)

characters = m.characters
#comics = m.comics
#creators = m.creators
#events = m.events
#series = m.series
#stories = m.stories

x = input("Type the name of a Marvel character: ")

allChars = characters.all(nameStartsWith=x)["data"]["results"]

for char in allChars:
    print(char["name"], "=", char["id"])

    for comics in char["comics"]["items"]:
        print(comics["name"])
    print("-----------------------------")

STORY = "This morning %s woke up feeling %s. 'It is going to be a %s day!' Outside, a bunch of %ss were protesting to keep %s in stores. They began to %s to the rhythm of the %s, which made all the %s s very %s. Concerned, %s texted %s, who flew %s to %s and dropped %s in a puddle of frozen %s. %s woke up in the year %s, in a world where %s s ruled the world." 

print("Mad Libs has started")

name = input("Enter a name : ")
adj1 = input("Enter an Adjective : ")
adj2 = input("Enter an Adjective : ")
adj3 = input("Enter an Adjective : ")
verb = input("Enter A Verb : ")
noun1 = input("Enter a Noun : ")
noun2 = input("Enter a Noun : ")
animal = input("Enter the name of an Animal : ")
food = input("Enter the name of a food : ")
fruit= input("Enter the name of a fruit : ")
superhero = input("Enter the name of a superhero : ")
country = input("Enter the name of a country : ")
dessert = input("Enter the name of a dessert : ")
year = input("Enter the name of a Year : ")



print(STORY % (name, adj1, adj2, animal, food, verb, noun1, fruit, adj3, name, superhero, name, country, name, dessert, name, year, noun2))

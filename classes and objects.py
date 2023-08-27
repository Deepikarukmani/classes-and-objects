class Goa:
    name = " "
    drink = " "
    def party (self):
        print("Let's party")
    def beach (self):
        print("Explore the Goa")

ramesh = Goa()
suresh = Goa()

ramesh.name="Ramesh"
suresh.name="suresh"

ramesh.drink = "Yes"
suresh.drink = "No"

print(ramesh.name)
print("drink", ramesh.drink)
print(suresh.name)
print("drink", suresh.drink)

ramesh.party()
suresh.beach()

class Team:
    name="Normal Team"

t1 = Team()
t2 = Team()
print Team.name, t1.name, t2.name

t1.name = 'R&D Team'
print Team.name, t1.name, t2.name

del t1.name
print Team.name, t1.name, t2.name
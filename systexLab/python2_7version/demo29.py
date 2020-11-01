class Course:
    def __init__(self, name, duration):
        self.name = name
        self.duration = duration

    def __str__(self):
        return '[%s](%d)' % (self.name, self.duration)

    def __repr__(self):
        return str(self)

    # def __hash__(self):
    #     return hash(str(self))

    def __eq__(self, other):
        return self.name == other.name \
               and self.duration == other.duration


c1 = Course('BDPY', 35)
c2 = c1
# s1 = {c1}
# s1.add(c1)
s1 = set()
s1.add(c1)
print s1
s1.add(c2)
print s1
c3 = Course('BDPY', 35)
s1.add(c3)
print s1
print hex(hash(c1)), hex(hash(c2)), hex(hash(c3))
c4 = Course('BDR', 35)
s1.add(c4)
print s1
c5 = Course('BDPY', 21)
s1.add(c5)
print s1

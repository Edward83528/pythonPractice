import demo31

print "demo32:", demo31.foo(5, 6)
print "demo32:", demo31.bar(7, 8)

import demo31 as d

print "d:", d.foo(9, 10)
print "d:", d.bar(11, 12)

from demo31 import foo, bar

print "direct:", foo(13, 14)
print "direct:", bar(15, 16)

from demo31 import foo as f, bar as b

print "acronym:", f(17, 18)
print "acronym:", b(19, 20)

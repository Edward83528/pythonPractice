def fix_function1(f1, f2, f3, f4):
    print "fix1=", f1
    print "fix2=", f2
    print "fix3=", f3
    print "fix4=", f4


fix_function1("sun", 'mon', '''tue''', 4)
a1 = [5, 6, 7]
fix_function1("array1", *a1)
a2 = (8, 9)
fix_function1("tuple", "ok", *a2)
fix_function1(*a2, f3="ken", f4="Tim")

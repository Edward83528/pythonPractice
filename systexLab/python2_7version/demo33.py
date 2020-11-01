def sample_variable_arguments(fix1, fix2, *args):
    print "fix part1=", fix1, fix2
    for e in args:
        print "variable part:", e


sample_variable_arguments("hello", "world1")
sample_variable_arguments("hello", "world2", "Sunday", "Monday", "Tuesday")
t1 = ("Sunday", "Monday", "Tuesday")
sample_variable_arguments("hello", "world3", t1)
sample_variable_arguments("hello", "world4", *t1)

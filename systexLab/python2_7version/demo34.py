def sample_key_value_variable_arguments(fix1, fix2, **kargs):
    print "fix part=", fix1, fix2
    for k, v in kargs.items():
        print "key=%s, value=%s" % (str(k), str(v))


sample_key_value_variable_arguments("hello", "world")
sample_key_value_variable_arguments("new", "course", title="Python&AI", duration="21hr", start="July-03")
course1 = {"title": "Python&AI", "duration": "21hr", "start": "July-03"}
sample_key_value_variable_arguments("another", "course", **course1)

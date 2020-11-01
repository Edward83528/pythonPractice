course1 = {"title": "Python&AI", "duration": "21hr", "start": "July-03"}


def showCourseInfo(title, duration, start):
    print "course title=", title
    print "course duration=", duration
    print "course start=", start

showCourseInfo(**course1)

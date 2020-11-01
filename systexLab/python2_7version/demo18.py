r = 2.0
a = r * r * 3.14159

print 'radius=%f, area=%f' % (r, a)
print 'radius=%.2f, area=%.4f' % (r, a)
print 'radius=%(radius).2f, area=%(area).4f' % {'radius': r, 'area': a}
print 'radius={}, area={}'.format(r, a)
print 'radius={:.2f}, area={:.4f}'.format(r, a)
print 'radius={0:.2f}, area={1:.4f}'.format(r, a)
print 'radius={1:.2f}, area={0:.4f}'.format(a, r)
print 'radius={radius:.2f}, area={area:.4f}'.format(area=a, radius=r)

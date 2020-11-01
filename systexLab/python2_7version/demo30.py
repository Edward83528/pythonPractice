sales = {'iphone6': 500, 'iphone6+': 400, 'iphone7': 300, 'iphoneX': 200}
print type(sales), sales
print sales['iphone7'], sales['iphoneX']
# print sales['xxxxxx']
sales['iphoneXS'] = 2000
print sales
print sales.get('iphone7'), sales.get('xxx')
print 'iphone6' in sales, 'xxxx' in sales
print [e for e in sales]
print [e for e in sales.keys()]
print [e for e in sales.values()]
for item in sales.items():
    print type(item), item
updateSales = {'iphone7':150, 'iphoneXR':1500}
sales.update(updateSales)
print sales
for item in sales.items():
    print item[0], item[1]
for i1, i2 in sales.items():
    print "i1=%s, i2=%s"%(i1, str(i2))

f = open('/root/alldb.sql', 'r')
filedata = f.read()
f.close()

newdata = filedata.replace("10.0.6.67","10.0.2.67")
f = open('/root/alldb.sql', 'w')
f.write(newdata)
f.close()

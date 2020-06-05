import bmemcached
client = bmemcached.Client(('10.10.10.190:11211', ), 'username','password');
f = open('big.txt', 'r')
lines = f.readlines()
for line in lines:
    cleanedline = line.strip()
    if str(client.get(cleanedline)) != "None":
        print "Matched:",  cleanedline, "\n", client.get(cleanedline)
f.close()

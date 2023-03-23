import os

for i in range(0, 20):
    os.system("python3 scrape.py chunk%d" % (i))

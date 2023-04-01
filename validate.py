import os

num_valid = 0
num_invalid = 0

def validate(thread):
    global num_valid, num_invalid
    valid = True
    text = open(thread + ".html").read()
    if not "</html>" in text:
        valid = False
        print(thread, "invalid html")
    os.system("gunzip -k " + thread + ".warc.warc.gz")
    warc = open(thread + ".warc.warc").read().strip()
    if warc.splitlines()[-1].strip() != "Content-Length: 0" or not "</html>" in warc:
        print(thread, "invalid warc")
        valid = False
    os.system("rm " + str(thread) + ".warc.warc")
    if '<link rel="next"' in text:
        next = text.split('<link rel="next" href="')[1].split('"')[0]
        next = next.strip()
        next_filename = next.replace("https://www.dpreview.com/forums/thread/", "").replace("?page=", "_")
        print(thread, "has next", next_filename)
        if not validate(next_filename):
            valid = False
            print("Incomplete paging / invalid", thread)
    if valid:
        num_valid += 1
    else:
        num_invalid += 1
    print(num_valid, num_invalid)
    return valid

for thread in range(4705000, 0, -1):
    validate(str(thread))

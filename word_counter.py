import re

def word_counter(fname):
    wc = {}
    try:
        f = open(fname, "r", encoding="utf-8")
        lines = f.readlines()
        for line in lines:
            wd = line.split(" ")

            for i in wd:
                j = i.strip("\n")
                j = j.lower()
                j = re.sub("[^a-zA-Z\s]", "", j)
                if j == "":
                    continue

                if j in wc:
                    wc[j] += 1
                else:
                    wc[j] = 1

    except FileNotFoundError:
        print("File not found")
        return
    except Exception as e:
        print(e)
        return
    finally:
        f.close()

    return wc

wc = word_counter("file_name.txt")
wc2 = dict(sorted(wc.items(), key=lambda x: x[1], reverse=True))
print(wc2)

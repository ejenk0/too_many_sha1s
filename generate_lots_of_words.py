from generate_sha import gen_sha1
import datetime

f = open("many_words.txt", "r")
words = f.readlines()
f.close()

doubled_f = open("lots_more_words.txt", "w")
doubled_f.writelines([])
doubled_f.close()

doubled_words = []
print("generating...")
doubled_f = open("lots_more_words.txt", "a")

origin, dt1 = datetime.datetime.today(), datetime.datetime.today()

print(f"Started: {origin}")
intervals = []

for count, i in enumerate(words):
    if count % 10 == 0:
        dt2 = datetime.datetime.today()
        print(f"Running for {(dt2 - origin)}")
        intervals.append(dt2-dt1)
        print(f"Estimated {(sum(intervals, datetime.timedelta(0))/len(intervals))*((len(words)/10)-(count/10))} remaining")
        print(f"word {count}...")
        dt1 = datetime.datetime.today()
    if count % 30 == 0:
        print(f"writing {len(doubled_words)} words to file...")
        doubled_f = open("lots_more_words.txt", "a")
        doubled_f.writelines(['{0}\n'.format(element) for element in doubled_words])
        doubled_words = []
        doubled_f.close()
    for j in words:
        doubled_words.append(i + " " + j)

doubled_f.close()


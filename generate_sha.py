import hashlib

def gen_sha1(list, count_freq=0):
    sums = []
    for i, word in enumerate(words):
        if i % count_freq == 0:
            if count_freq:
                print(i)

        sums.append(hashlib.sha1(bytes(word, 'utf-8')).hexdigest())
    return sums

if __name__ == "__main__":
    f = open("many_words.txt", "r")
    words = f.readlines()
    f.close()
    sums = gen_sha1(words, 10000)

    print("Writing to file...")
    sumsf = open("sums.txt", "w")
    sumsf.writelines(['{0}\n'.format(element) for element in sums])
    print("done")

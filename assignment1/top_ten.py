from __future__ import division
import sys
import json

def main():
    data = []
    with open(sys.argv[1]) as f:
        i = 0
        for line in f:
            i += 1
            d = json.loads(line)
            if 'entities' in d:
                data.append(json.loads(line))
    hashtags = {}
    for d in data:
        for h in d["entities"]["hashtags"]:
            if h["text"] in hashtags:
                hashtags[h['text']] += 1
            else:
                hashtags[h['text']] = 1
    hashtags = sorted(hashtags.items(), key=lambda x: x[1], reverse=True)
    for i in range(10):
        print("{} {}".format(hashtags[i][0], hashtags[i][1]))


if __name__ == '__main__':
    main()

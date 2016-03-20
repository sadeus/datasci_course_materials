from __future__ import division
import sys
import json


def main():
    words = {}
    with open(sys.argv[1]) as f:
        for line in f:
            data = json.loads(line)
            if "text" in data:
                for w in data['text'].split(' '):
                    try:
                        w = w.encode("ascii").strip(',;:."\'?')
                        if '\n' not in w:
                            if w in words:
                                words[w] += 1
                            else:
                                words[w] = 1
                    except:
                        pass
    num_terms = len(words)
    for w in words:
        print(w.encode("utf-8") + " " + str(words[w]/num_terms))

if __name__ == '__main__':
    main()
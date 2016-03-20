import sys
import json


def main():
    sent_file = sys.argv[1]
    scores = sentiment_dict(sent_file)
    with open(sys.argv[2]) as f:
        for line in f:
            jsdata = json.loads(line)
            if 'text' in jsdata:
                score = score_line(jsdata["text"].encode('utf-8'), scores)
                print(score)
            else:
                print(0)

def sentiment_dict(sent_file):
    afinnfile = open(sent_file)
    scores = {}
    for line in afinnfile:
        term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
        scores[term] = int(score)  # Convert the score to an integer.
    #print scores.items() # Print every (term, score) pair in the dictionary
    return scores


def score_line(line, scores):
    score = 0
    words = line.split(" ")
    for w in words:
        if w in scores:
            score += scores[w]
    return score

if __name__ == '__main__':
    main()

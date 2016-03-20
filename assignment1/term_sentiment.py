import sys

def hw():
    print 'Hello, world!'

def lines(fp):
    print str(len(fp.readlines()))

def main():
    sent_file = sys.argv[1]
    score = sentiment_score(sent_file)
    with open(sys.argv[2]) as f:
        for line in f:
            jsdata = json.loads(line)
            if 'text' in jsdata:
                score = score_line(jsdata["text"].encode('utf-8'), scores)
                print(score)
            else:
                print(0)

def get_scores(line, scores):
    score = 0
    words = line.split(" ")
    for i,w in enumerate(words):
        if w in scores:
            next_word = lines[i + 1 if i + 1 < len(words) else len(words) -  1]
            prev_word = lines[i - 1 if i - 1 > 0 else 0]
            scores[next_word] += scores[w]
            scores[prev_word] += scores[w]
    return scores



def sentiment_score(sent_file):
    afinnfile = open(sent_file)
    scores = {}
    for line in afinnfile:
        term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
        scores[term] = int(score)  # Convert the score to an integer.
    #print scores.items() # Print every (term, score) pair in the dictionary
    return scores

if __name__ == '__main__':
    main()

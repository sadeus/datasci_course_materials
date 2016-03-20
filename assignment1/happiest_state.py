from __future__ import division
import sys
import json

states = {
    'AK': 'Alaska',
    'AL': 'Alabama',
    'AR': 'Arkansas',
    'AS': 'American Samoa',
    'AZ': 'Arizona',
    'CA': 'California',
    'CO': 'Colorado',
    'CT': 'Connecticut',
    'DC': 'District of Columbia',
    'DE': 'Delaware',
    'FL': 'Florida',
    'GA': 'Georgia',
    'GU': 'Guam',
    'HI': 'Hawaii',
    'IA': 'Iowa',
    'ID': 'Idaho',
    'IL': 'Illinois',
    'IN': 'Indiana',
    'KS': 'Kansas',
    'KY': 'Kentucky',
    'LA': 'Louisiana',
    'MA': 'Massachusetts',
    'MD': 'Maryland',
    'ME': 'Maine',
    'MI': 'Michigan',
    'MN': 'Minnesota',
    'MO': 'Missouri',
    'MP': 'Northern Mariana Islands',
    'MS': 'Mississippi',
    'MT': 'Montana',
    'NA': 'National',
    'NC': 'North Carolina',
    'ND': 'North Dakota',
    'NE': 'Nebraska',
    'NH': 'New Hampshire',
    'NJ': 'New Jersey',
    'NM': 'New Mexico',
    'NV': 'Nevada',
    'NY': 'New York',
    'OH': 'Ohio',
    'OK': 'Oklahoma',
    'OR': 'Oregon',
    'PA': 'Pennsylvania',
    'PR': 'Puerto Rico',
    'RI': 'Rhode Island',
    'SC': 'South Carolina',
    'SD': 'South Dakota',
    'TN': 'Tennessee',
    'TX': 'Texas',
    'UT': 'Utah',
    'VA': 'Virginia',
    'VI': 'Virgin Islands',
    'VT': 'Vermont',
    'WA': 'Washington',
    'WI': 'Wisconsin',
    'WV': 'West Virginia',
    'WY': 'Wyoming'
}


def main():
    state_scores = {}
    scores = sentiment_dict(sys.argv[1])
    with open(sys.argv[2]) as f:
        for line in f:
            data = json.loads(line)
            if "text" in data:
                if data["place"] is not None and data["place"]["country_code"] == "US":
                    split_city = data["place"]["full_name"].split(", ")
                    state_code = split_city[1]
                    for code, state in states:
                        if state == split_city[0]:
                            state_code = code
                    if state_code in states:
                        score = score_line(data["text"], scores)
                        if state_code not in state_scores or state_scores[state_code] < score:
                            state_scores[state_code] = score
    max_score = 0
    max_state = ''
    for state, score in state_scores.items():
        if score > max_score:
            max_score = score
            max_state = state
    print max_state


def sentiment_dict(sent_file):
    afinnfile = open(sent_file)
    scores = {}
    for line in afinnfile:
        term, score = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
        scores[term] = int(score)  # Convert the score to an integer.
    # print scores.items() # Print every (term, score) pair in the dictionary
    return scores


def score_line(line, scores):
    score = 0
    n_words = 1
    words = line.split(" ")
    for w in words:
        if w in scores:
            score += scores[w]
            n_words += 1
    return score / n_words


if __name__ == '__main__':
    main()

if __name__ == '__main__':
    open('problema_1_submission.txt','w+')
    with open('three_minutes_tweets.json') as twf:
        with open('problem_1_submission.txt', 'w') as p1s:
            i = 0
            for line in twf:
                if i < 20:
                    p1s.write(line)
                    i += 1
                else:
                    break

import csv

tweets = []
with open('files/project_twitter_data.csv', mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        print(f'\t{row["tweet_text"]} was retweeted {row["retweet_count"]} times, and received {row["reply_count"]} replies.')
        line_count += 1
        tweets.append(row)
    print(f'Processed {line_count} lines.')
csv_file.close()

# We have provided some synthetic (fake, semi-randomly generated) twitter data in a csv file named
# project_twitter_data.csv which has the text of a tweet, the number of retweets of that tweet,
# and the number of replies to that tweet. We have also words that express positive sentiment
# and negative sentiment, in the files positive_words.txt and negative_words.txt.
# Your task is to build a sentiment classifier, which will detect how positive or negative each tweet is.
# You will create a csv file, which contains columns for the Number of Retweets, Number of Replies, Positive Score
# (which is how many happy words are in the tweet), Negative Score (which is how many angry words are in the tweet),
# and the Net Score for each tweet. At the end, you upload the csv file to Excel or Google Sheets, and produce a graph
# of the Net Score vs Number of Retweets.
# To start, define a function called strip_punctuation which takes one parameter, a string which represents a word,
# and removes characters considered punctuation from everywhere in the word.
# (Hint: remember the .replace() method for strings.)
punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']
def strip_punctuation(str):
    for punc_char in punctuation_chars:
        str = str.replace(punc_char, '')
    return str

# Next, copy in your strip_punctuation function and define a function called get_pos which takes one parameter,
# a string which represents one or more sentences, and calculates how many words in the string are considered
# positive words. Use the list, positive_words to determine what words will count as positive.
# The function should return a positive integer - how many occurrences there are of positive words in the text.
# Note that all of the words in positive_words are lower cased, so you’ll need to convert all the words in the
# input string to lower case as well.
# punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']
# list of positive words to use
positive_words = []
with open("files/positive_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            positive_words.append(lin.strip())

# cannot use sentences.count() for each positive_words because
# 'won' will hit on 'wonderful' and 'wonderful' will hit on 'wonderfully'
def get_pos(sentences):
    sentences = strip_punctuation(sentences).lower()
    cnt = 0
    for word in sentences.split():
        if word in positive_words:
            cnt += 1
    return cnt

pos_cnt = get_pos(tweets[0]['tweet_text'])
print(pos_cnt)
pos_cnt = get_pos("what a truly Wonderful day it is today! #Incredible")
print(pos_cnt)

# Next, copy in your strip_punctuation function and define a function called get_neg which takes one parameter,
# a string which represents one or more sentences, and calculates how many words in the string are considered
# negative words. Use the list, negative_words to determine what words will count as negative. The function should
# return a positive integer - how many occurrences there are of negative words in the text.
# Note that all of the words in negative_words are lower cased, so you’ll need to convert all the words
# in the input string to lower case as well.
# punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']
negative_words = []
with open("files/negative_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            negative_words.append(lin.strip())
def get_neg(sentences):
    sentences = strip_punctuation(sentences).lower()
    cnt = 0
    for word in sentences.split():
        if word in negative_words:
            cnt += 1
    return cnt

neg_cnt = get_neg(tweets[0]['tweet_text'])
print(pos_cnt)
neg_cnt = get_neg("what a truly Wonderful day it is today! #Incredible")
print(pos_cnt)

# Finally, copy in your previous functions and write code that opens the file project_twitter_data.csv
# which has the fake generated twitter data (the text of a tweet, the number of retweets of that tweet,
# and the number of replies to that tweet). Your task is to build a sentiment classifier, which will detect
# how positive or negative each tweet is. Copy the code from the code windows above,
# and put that in the top of this code window. Now, you will write code to create a csv file called resulting_data.csv,
# which contains the Number of Retweets, Number of Replies,
# Positive Score (which is how many happy words are in the tweet),
# Negative Score (which is how many angry words are in the tweet),
# and the Net Score (how positive or negative the text is overall) for each tweet.
# The file should have those headers in that order. Remember that there is another component to this project.
# You will upload the csv file to Excel or Google Sheets and produce a graph of the Net Score vs Number of Retweets.
# Check Coursera for that portion of the assignment, if you’re accessing this textbook from Coursera.

with open('resulting_data.csv', mode='w') as csv_file:
    fieldnames = ['Number of Retweets', 'Number of Replies', 'Positive Score', 'Negative Score', 'Net Score']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

    writer.writeheader()
    for tweet in tweets:
        pos_cnt = get_pos(tweet['tweet_text'])
        neg_cnt = get_neg(tweet['tweet_text'])
        writer.writerow({
            'Number of Retweets': tweet['retweet_count'],
            'Number of Replies': tweet['reply_count'],
            'Positive Score': pos_cnt,
            'Negative Score': neg_cnt,
            'Net Score': pos_cnt - neg_cnt
        })
csv_file.close()

# alternate technique w/o csv module
with open('resulting_data.csv', 'w') as csv_out_file:
    csv_out_file.write('Number of Retweets, Number of Replies, Positive Score, Negative Score, Net Score')
    csv_out_file.write('\n')
    with open('files/project_twitter_data.csv', 'r') as csv_in_file:
        tweets = csv_in_file.readlines()
        tweets.pop(0)
        for tweetRaw in tweets:
            tweet = tweetRaw.strip().split(',')
            pos_cnt = get_pos(tweet[0])
            neg_cnt = get_neg(tweet[0])
            csv_out_file.write("{}, {}, {}, {}, {}".format(
                tweet[1], tweet[2], pos_cnt, neg_cnt, pos_cnt - neg_cnt
            ))
            csv_out_file.write("\n")
csv_in_file.close()
csv_out_file.close()



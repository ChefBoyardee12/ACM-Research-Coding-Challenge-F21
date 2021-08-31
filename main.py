import string
import nltk.data
import matplotlib.pyplot as plt
from nltk.tokenize import sent_tokenize
nltk.download('punkt')
from afinn import Afinn
from textblob import TextBlob

# Maximum absolute value given to a singular word through AFINN scoring
MAX_AFINN_VALUE = 5

# Make string that splits input text by sentences
sentence_split = nltk.tokenize.sent_tokenize(open('input.txt').read().replace("\n", ""))


# Create an array of every sentence in the input file unedited
sentences = []
sentences = sent_tokenize(open("input.txt").read().replace("\n", " "))

# Make string that converts input text into lower case and removes all punctuation
# Cleaned input text is then split by word
clean = open('input.txt').read().lower().translate(str.maketrans('', '', string.punctuation))
tokenized_words = clean.split()

# Converts every word in every sentence into lowercase and removes punctuation
tokenized_sentences = []
for element in sentence_split:
  clean = element.lower().translate(str.maketrans('', '', string.punctuation))
  tokenized_sentences.append(clean)
 
# General list of stop words that do not add any sentimental meaning to the text
stop_words = ["i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you", "your", "yours", "yourself", "yourselves", "he", "him", "his", "himself", "she", "her", "hers", "herself", "it", "its", "itself", "they", "them", "their", "theirs", "themselves", "what", "which", "who", "whom", "this", "that", "these", "those", "am", "is", "are", "was", "were", "be", "been", "being", "have", "has", "had", "having", "do", "does", "did", "doing", "a", "an", "the", "and", "but", "if", "or", "because", "as", "until", "while", "of", "at", "by", "for", "with", "about", "against", "between", "into", "through", "during", "before", "after", "above", "below", "to", "from", "up", "down", "in", "out", "on", "off", "over", "under", "again", "further", "then", "once", "here", "there", "when", "where", "why", "how", "all", "any", "both", "each", "few", "more", "most", "other", "some", "such", "no", "nor", "not", "only", "own", "same", "so", "than", "too", "very", "s", "t", "can", "will", "just", "don", "should", "now", "im"] 

# Sets Afinn language as english
afinn = Afinn(language='en')

# Counts the values of Afinn and TextBlob assigned words per sentences
# after removing generic stop words.
# Additionally prints every sentence in the input file along with its TextBlob and AFINN sentiment
# scores respectively. Adds sentiment score values to array to be plotted.
total_countA = 0
total_countT = 0
xVal = []
yValT = []
yValA = []
for x in range(0, len(sentences)):
  my_valence = TextBlob(tokenized_sentences[x])
  print(sentences[x] + '\n\n' + str(my_valence.sentiment) + '\n' + afinn.score(sentences[x] + '\n')
  tokenized = tokenized_sentences[x].split()
  xVal.append(x)
  yValT.append(my_valence.sentiment.polarity)
  yValA.append(afinn.score(tokenized_sentences[x]))
  for word in tokenized:
    if word not in stop_words:
      final_words = []
      final_words.append(word)
      count = 0
      count2 = 0
      for word in final_words:
        count = count + (afinn.score(word))
        count2 = count2 + TextBlob(word).sentiment.polarity
      total_countA += count
      total_countT += count2

# Prints values of the sentiment analysis including total value of every word in the text, 
# average score per sentence in the text, and average score per word in the text.

print ('The aggregated value of every word in the text through AFINN is '
      + str(total_countA) + ' in a  range of (' 
      + str(len(tokenized_words) * MAX_AFINN_VALUE * -1)
      + ', ' + str(len(tokenized_words) * MAX_AFINN_VALUE) + ').\n')

print ('The average score per sentence in the text through AFINN is ' 
      + str((total_countA) / len(tokenized_sentences)) + '.\n')

print ('the average score per word in the text through AFINN is '
      + str(round(total_countA / len(tokenized_words), 3))
      + ' in a range of (' + str(-1 * MAX_AFINN_VALUE) 
      + ', ' + str(MAX_AFINN_VALUE) + ').\n')

print ('The aggregated value of every word in the text through TextBlob is '
      + str(total_countT) + ' in a  range of (' 
      + str(len(tokenized_words) * -1)
      + ', ' + str(len(tokenized_words)) + ').\n')

print ('The average score per sentence in the text through TextBlob is ' 
      + str((total_countT) / len(tokenized_sentences)) + '.\n')

print ('the average score per word in the text through TextBlob is '
      + str(round(total_countT / len(tokenized_words), 3))
      + ' in a range of (' + str(-1 ) 
      + ', ' + str(1) + ').\n')


# Plots graph of sentiment scores through AFINN and TextBlob

plt.figure()
plt.subplot(1, 2, 1)
plt.plot(xVal, yValT, 'ro')
plt.title('Sentiment Score Per Sentence Through TextBlob')
plt.xlabel('Sentence Number for TextBlob Scoring')
plt.ylabel('Sentiment Score')
plt.savefig('textblob', bbox_inches = 'tight')

plt.subplot(1, 2, 2)
plt.plot(xVal, yValA, 'bo')
plt.title('Sentiment Score Per Sentence Through AFINN')
plt.xlabel('Sentence Number for AFINN scoring')
plt.ylabel('Sentiment Score')
plt.savefig('AFINN', bbox_inches = 'tight')

plt.tight_layout() 
plt.show()




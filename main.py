import string
import nltk.data
import matplotlib.pyplot as plt
nltk.download('punkt')
from nltk.tokenize import sent_tokenize
from afinn import Afinn
from textblob import TextBlob

# Maximum absolute value given to a singular word through AFINN scoring
MAX_AFINN_VALUE = 5

# Create an array of every sentence in the input file unedited
sentences = []
sentences = sent_tokenize(open("input.txt").read().replace("\n", " "))

# Make string that converts input text into lower case and removes all punctuation
# Cleaned input text is then split by word
clean = open('input.txt').read().lower().translate(str.maketrans('', '', string.punctuation))
tokenized_words = clean.split()

# Converts every word in every sentence into lowercase and removes punctuation
tokenized_sentences = []
for element in sentences:
  clean = element.lower().translate(str.maketrans('', '', string.punctuation))
  tokenized_sentences.append(clean)


# Sets Afinn language as english
afinn = Afinn(language='en')

# Counts the values of Afinn and TextBlob assigned words per sentences
# after removing generic stop words.
# Additionally prints every sentence in the input file along with its TextBlob and AFINN sentiment
# scores respectively. Adds sentiment score values to array to be plotted.

xVal = [];
yValA = [];
yValT = [];
final_words = [];
total_countA = 0;
total_countT = 0;
for element in tokenized_sentences:
  split_words = element.split()
  ToAdd = "";
  for word in split_words:
    if word not in open('stopwords.txt').read():
      ToAdd += word + " "
  final_words.append(ToAdd)

for x in range (0, len(sentences)):
  my_valence = TextBlob(tokenized_sentences[x])
  print ("\n\n" + sentences[x] + '\n\nTextBlob Score: ' + str(my_valence.sentiment))
  print ('\nAFINN Score: ' + str(afinn.score(final_words[x])))
  xVal.append(x)
  yValT.append(my_valence.sentiment.polarity)
  yValA.append(afinn.score(final_words[x]))
  total_countA += afinn.score(final_words[x])
  total_countT += my_valence.sentiment.polarity


# Prints values of the sentiment analysis including total value of every word in the text, 
# average score per sentence in the text, and average score per word in the text.

print ('\n\nThe aggregated value of every word in the text through AFINN is '
      + str(total_countA) + '.\n')

print ('The aggregated value of every word in the text through TextBlob is '
      + str(round((total_countT), 5)) + '.\n')

print ('The average score per sentence in the text through AFINN is ' 
      + str(round(total_countA / len(sentences), 5)) + '.\n')

print ('The average score per sentence in the text through TextBlob is ' 
      + str(round(total_countT / len(sentences), 5)) + '.\n')

print ('The average score per word in the text through AFINN is '
      + str(round(total_countA / len(tokenized_words), 5))
      + ' in a range of (' + str(-1 * MAX_AFINN_VALUE) 
      + ', ' + str(MAX_AFINN_VALUE) + ').\n')

print ('The average score per word in the text through TextBlob is '
      + str(round(total_countT / len(tokenized_words), 5))
      + ' in a range of (' + str(-1 ) 
      + ', ' + str(1) + ').\n')

# Plots graph of sentiment scores through AFINN and TextBlob

plt.figure()

plt.subplot(1, 2, 1)
plt.plot(xVal, yValT, 'ro')
plt.title('TextBlob Score Per Sentence')
plt.xlabel('Sentence Number')
plt.ylabel('Sentiment Score')

plt.subplot(1, 2, 2)
plt.plot(xVal, yValA, 'bo')
plt.title('AFINN Score Per Sentence')
plt.xlabel('Sentence Number')
plt.ylabel('Sentiment Score')

plt.tight_layout() 
plt.show()




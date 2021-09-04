# **ACM Research Coding Challenge (Fall 2021) - Shahrukh Showkath**

## Introduction to Approach

When conducting sentiment analysis, the three main methods of analysis are rule-based, automatic, or hybrid. When using an automatic or hybrid model, it is imperative to train the data, or to teach the model to associate an input with a corresponding sentiment output. Due to the lack of trained data, it is difficult to teach the model how to evaluate sentiments in text. Thus, a rule-based model that uses man made rules to analyze the text was used for this project. To do this, AFINN lexicon and TextBlob library were used. 

## Background On Tools Used
The AFINN lexicon is a list of over 3,300 positive negative words that have an assigned value ranging from -5 to 5, with the lower end being words classified as more negative and the higher end to be classified as more positive. The TextBlob library is similar in that it has a normalized polarity score scale with a range of -1.0 to 1.0. However, the TextBlob library additionally provides a subjectivity score ranging from 0.0 to 1.0, with 0.0 being very objective and 1.0 being very subjective. Both of these tools were used for this project to have two overall references for the text's sentiment value.

## Approach
Firstly, the data was cleaned then parsed. The data that is given is rather noisy, so by removing punctuation and converting the entire text to lowercase, it is easier to analyze due to its uniformity. Furthermore, certain "stop" words were removed from the text. Stop words are common words that do not aid in sentiment analysis, such as "and", "or", "to", etc. This further cleans the data to be analyzed. Once the data was cleaned, a loop was used to iterate through the text and the TextBlob library was used to print out the polarity and subjectivity of every sentence in the text and pasted in the output to show a sentiment value for every sentence. The AFINN library was also used to keep track of the values per word and sentence. The AFINN score per sentence was not pasted due to its inability to portray the subjectivity of the sentence. Once the values per tool was totaled, the total value of the words, the average value of each sentence, and the average value per word are outputted. To further aid in the visualization of the data, a side-by-side graph is portrayed to show the value per sentence calculated by the two tools.

## Results and Analysis
The program calculated the sentiment scores through different categories as follows: 
  - The overall sentiment score of the text through AFINN was `19.0` and `3.19269` through TextBlob, both meaning `positive`. This was done by summing the value of every word in the text together.


  -  Further results indicate that the average sentence score through AFINN was `0.59375` and `0.09977`through TextBlob, both meaning `slightly positive`. 

  - Finally, the average word scores for AFINN and TextBlob were `0.02802` and `0.00471` respectively, both meaning `barely positive but essentially neutral`. 
  
At first, I felt that these scores were not what I expected, but further deliberation induced me to agree with the results. I was initially inclined to disagree with the outcome due to the extreme negativity of the first paragraph, denoting a fierce argument between two characters with words such as "rage", "dreary chaos", "bleed", and "murderer". However, the sheer positivity of the last paragraph, describing an individual with an "excellent constitution", "ingenious" mind, "sound understanding and solid judgement", and shown a "good deal of respect". With the overwhelming positivity of the latter half of the text, the outcome was shifted to being positive overall. 

A similar conclusion is derived when analyzing the graphs. Although varying overall, there is a slight pattern indicating a general increase in positivity as the text goes on. The graphs indicate that the most positive sentiment scores appear later on in the text and the more negative scores appear earlier, paralleling the above analysis. This is seen much clearer when evaluating the AFINN graph.

## Conclusion
In essence, this program concluded that on average, the text is sentimentally positive.

 However, this data could have been affected by many factors as there was not a robust amount of training data for this text. When using AFINN and TextBlob, certain scenarios are not able to be counted for. For example, instances of sarcasm or negated text are not able to be appropriately scored due to the limitations of the tools used. Additionally, if a word is used that is not defined under the TextBlob or AFINN library, it may not be appropriately scored as well. This is seen by the numerous `0.0` scores throughout the program, even with objectively negative sentences such as "Carcasses bleed at the sight of the murderer!"

However, by using a predefined library, the program is able to provide a decent insight into the sentiment score of the text as a whole in a quick manner without any training data.

***Thank you for taking the time to look through this project. I learned many new concepts and had fun while doing so. I hope to be able to conduct more projects in the future with ACM.***

## Libraries

- String
- NLTK
- Matplotlib
- AFINN
- TextBlob

## Sources
- [Emotion and Sentiment Analysis: A Practitioner’s Guide to NLP](https://www.kdnuggets.com/2018/08/emotion-sentiment-analysis-practitioners-guide-nlp-5.html)
- [Word Lists and Sentiment Analysis](https://nealcaren.org/lessons/wordlists/)
- [Sentiment analysis with tidy data](https://www.tidytextmining.com/sentiment.html)
- [Stop words list (courtesy of GitHub user jimmyjames177414)](https://gist.github.com/sebleier/554280)

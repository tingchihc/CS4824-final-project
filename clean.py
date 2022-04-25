import string
import re
import nltk
nltk.download('wordnet')
nltk.download('stopwords')

from nltk.corpus import stopwords
from nltk.stem.wordnet import WordNetLemmatizer 

from wordcloud import WordCloud

def data_preprocessing(text):
  #lower case normalizing 
  text=text.lower()
  #remove punctuations
  punctuations = string.punctuation
  #remove stopwords
  stop_words = set(stopwords.words("english"))
  

  words=text.split(" ")
  words = [WordNetLemmatizer().lemmatize(word, "v") for word in words]
  words = [w for w in words if w not in stop_words and w not in punctuations]

  clean = " ".join(words)
  #remove any non alphanum, digit character
  clean = re.sub("\W+", " ", clean)
  #remove numbers
  clean = re.sub(r'[0-9]+', '', clean)
  #remove single letter
  clean = re.sub('\s+\S\s+', '', clean)
  
  clean = re.sub("  ", " ", clean)
  return clean
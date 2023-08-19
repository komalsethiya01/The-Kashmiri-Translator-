import pandas as pd
# from pygame import mixer  # Load the popular external library
import numpy as np
import nltk
nltk.download('stopwords')
nltk.download('punkt')
nltk.download('wordnet')
nltk.download('omw-1.4')
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import requests
import time
from gtts import gTTS

import os
from pydub import AudioSegment

result = "that child is a troubled child"
"""# ***English to Kashmiri***"""
lis = []
for words in result.split(" "):
  lis.append(words.lower())

stop_words = set(stopwords.words("english"))
filtered_sentence = [word for word in lis if word.lower() not in stop_words]

stop_words = set(stopwords.words("english"))
d = pd.DataFrame(stop_words)
unique_words = list(set(filtered_sentence))

def get_root_word(word_list):
    lemmatizer = WordNetLemmatizer()
    root_words = [lemmatizer.lemmatize(word) for word in word_list]
    return root_words

root_words = get_root_word(unique_words)

df = pd.read_csv('Kashmiri_dictionary - S_Hassan_dictionary (1).csv')

new_df = pd.DataFrame(df.meaning.str.split(',').tolist(), index=df.word).stack()
new_df = new_df.reset_index([0, 'word'])
new_df.columns = ['word', 'meaning']

new_df.to_csv("new_dictionary.csv")
df_new1 = pd.read_csv("Stopwords - Sheet1.csv")

new_df = pd.read_csv('new_dictionary.csv', skipinitialspace=True)

new_df.drop(columns='Unnamed: 0', inplace=True)

frames = [new_df,df_new1]
df1 = pd.concat(frames)

df1.drop(['newmeaning'],axis=1,inplace=True)

df1.to_csv('finalset.csv')

def Diff(li1, li2):
    li_dif = [i for i in li1 + li2 if i not in li1 or i not in li2]
    return li_dif

df1 = pd.read_csv('finalset.csv')

meaning = []

# Looping through the words
for word in lis:
    # Searching the word in the "Words" column of the DataFrame
    if word in df1["meaning"].values:
        # Getting the index of the matching word
        index = df1[df1["meaning"] == word].index[0]

        # Printing the corresponding meaning from the "Meanings" column
        mean = df1.at[index, 'word']
        meaning.append(index)

df1.reset_index(drop=True,inplace=True)

new1 = []
for i in meaning:
  new1.append(df1['word'][i])

word_url = df[['word','file_urls']]

df_new1.drop(['newmeaning'],axis=1,inplace=True)
df_new1.dropna(inplace =True)
df_new1.reset_index(inplace=True)
df_new1.to_csv('newstops.csv')

# stop = pd.read_csv('newstops.csv')

# stop_url = stop[['word','urls']]

stop_urls = pd.read_csv("newstopurl (1).csv")
stop_urls.drop({"Unnamed: 0"},axis=1,inplace=True)

frames = [word_url,stop_urls]
urls = pd.concat(frames)

urls.reset_index(inplace=True)

urls.drop(['index'],axis=1,inplace=True)

urls.head()

urls.isnull().sum()

url_list = []

for temp in new1:    
    if temp in urls['word'].values:
        index = urls[urls["word"] == temp].index[0]
        url_list.append(urls["file_urls"][index])

chunk_size = 512  # Number of bytes to download at a time
delay = 2.0  # Number of seconds to wait between downloading chunks

for i in range(len(url_list)):
  response = requests.get(url_list[i], stream=True)
  filename = 'song'+str(i)+'.mp3'

  with open(filename, 'wb') as f:
      for chunk in response.iter_content(chunk_size=chunk_size):
        f.write(chunk)
        time.sleep(delay)

combined = AudioSegment.from_file("song0.mp3", format="mp3")

for i in range(1,len(url_list)):
   combined += AudioSegment.from_file('song'+str(i)+'.mp3', format="mp3")
# sound2 = AudioSegment.from_file("song1.mp3", format="mp3")
# sound3 = AudioSegment.from_file("song2.mp3", format="mp3")
# sound4 = AudioSegment.from_file("song3.mp3", format="mp3")
# sound5 = AudioSegment.from_file("song4.mp3", format="mp# sound6 = AudioSegment.from_file("song5.mp3", format="mp3")

# combined = sound1 + sound2 + sound3 + sound4 + sound5 + sound6
combined.export("combined.mp3", format="mp3")

string =''
string = ' '.join([str(elem) for elem in new1])
# mixer.init()
# mixer.music.load('combined.mp3')
# mixer.music.play()



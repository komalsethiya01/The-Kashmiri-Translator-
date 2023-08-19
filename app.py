from flask import Flask, render_template,request,Markup,redirect,url_for,jsonify
import jinja2
import pandas as pd
import numpy as np
import speech_recognition as sr
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import nltk
nltk.download('punkt')
nltk.download('wordnet')
nltk.download('omw-1.4')
from nltk.stem import WordNetLemmatizer
import requests
import time
from gtts import gTTS
import os
from pydub import AudioSegment

#import requests
app = Flask(__name__)

if __name__ == '__main__':
    app.run()
global result
global final
"""@app.route('/')
def hello():
    
    return 'Success'"""
@app.route('/index')
def index():
  return render_template('index.html')

@app.route('/eng')
def test():
  print("inside first app route")
  return render_template('english_kashmiri.html',english_out='Hello world')

@app.route('/eng',methods=['POST'])
def eng():
  '''if not request.data:
    print("inside if")
    return render_template('english_kashmiri.html')'''


  result = request.form['result']
  
  print("Reached in python")
  print(result)

  #   #to get input as recorded audio file
  #   # import speech_recognition as sr

  #   # Initialize recognizer class (for recognizing the speech)
  #   # r = sr.Recognizer()

  #   # Reading Microphone as source
  #   # listening the speech and store in audio_text variable

  #   # result = 'i play harmonium'

  #   #to split the sentences into words
  #   # ***English to Kashmiri***
  # #  print(request)
    
   #result=request.form['var1']
   #ks=request.form['var2']
  
  lis = []
  for words in result.split(" "):
    lis.append(words.lower())

  nltk.download('stopwords')

    #to remove the stop words


  stop_words = set(stopwords.words("english"))

    # Removing stop words from the list
  filtered_sentence = [word for word in lis if word.lower() not in stop_words]

    # Printing filtered words
    # print(filtered_sentence)


  stop_words = set(stopwords.words("english"))
    # len(stop_words)

  d = pd.DataFrame(stop_words)

    # d

    #d.to_csv('stopwords.csv')

    #to get list of unique words
  unique_words = list(set(filtered_sentence))
    # print(unique_words)

    #to find the root word 
  global df
  def get_root_word(word_list):
    lemmatizer = WordNetLemmatizer()
    root_words = [lemmatizer.lemmatize(word) for word in word_list]
    return root_words

  root_words = unique_words
    # print(root_words)
  
  df = pd.read_csv(r'C:\\Users\\Ritika\\Desktop\\flask_app\\flask_app\\Kashmiri_dictionary - S_Hassan_dictionary (1).csv')

    # df.head()

    # df.columns

    # df.head()

    # df.shape[0]

    # df["meaning"].values

  new_df = pd.DataFrame(df.meaning.str.split(',').tolist(), index=df.word).stack()
  new_df = new_df.reset_index([0, 'word'])
  new_df.columns = ['word', 'meaning']

  new_df.to_csv('new_dictionary.csv')
  global df_new1
  df_new1 = pd.read_csv(r'C:\\Users\\Ritika\\Desktop\\flask_app\\flask_app\\Stopwords - Sheet1 (2).csv')
   # df_new1 C:\\Users\\Ritika\\Desktop\\flask_app\\flask_app\\Stopwords - Sheet1 (2).csv

  new_df = pd.read_csv('new_dictionary.csv', skipinitialspace=True)

  new_df.drop(columns='Unnamed: 0', inplace=True)

    # new_df

  frames = [new_df,df_new1]
  df1 = pd.concat(frames)

    # df1

  df1.drop(['newmeaning'],axis=1,inplace=True)

    # df1

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

    # meaning
  global new1
  new1 = []
  for i in meaning:
    new1.append(df1['word'][i])

  final = ' '.join(new1)
  print(final)
    # new1
  output = 'My name is Ritika'
  return jsonify({'result': final}) 
  #return render_template('english_kashmiri.html',english_out=final,result=result)


  ################ Audio generation for english to kashmiri ##################################################

"""   word_url = df[['word','file_urls']]
  df_new1.drop(['newmeaning'],axis=1,inplace=True)
  df_new1.dropna(inplace =True)
  df_new1.reset_index(inplace=True)
  df_new1.to_csv('newstops.csv')
  stop = pd.read_csv('newstops.csv')
  stop_urls = pd.read_csv(r'C:\\Users\\Ritika\\Desktop\\flask_app\\flask_app\\newstopurl.csv')
  stop_urls.drop({"Unnamed: 0"},axis=1,inplace=True)
  frames = [word_url,stop_urls]
  urls = pd.concat(frames)

  urls.reset_index(inplace=True)

  urls.drop(['index'],axis=1,inplace=True)
  url_list = []

  for temp in new1:    
   if temp in urls['word'].values:
    index = urls[urls["word"] == temp].index[0]
    url_list.append(urls["file_urls"][index])
  chunk_size = 512  # Number of bytes to download at a time
  delay = 2.0
  for i in range(len(url_list)):
    response = requests.get(url_list[i], stream=True)
    filename = 'song'+str(i)+'.mp3'
    with open(filename, 'wb') as f:
      for chunk in response.iter_content(chunk_size=chunk_size):
        f.write(chunk)
        time.sleep(delay)
  combined = AudioSegment.empty()
  directory = "C:/Users/Ritika/Desktop/flask_app/flask_app"

  mp3_files = [file for file in os.listdir(directory) if file.endswith(".mp3")]
  for file in mp3_files:
    audio = AudioSegment.from_mp3(os.path.join(directory, file))
    combined += audio



  combined = AudioSegment.empty()
  for file in mp3_files:
   audio = AudioSegment.from_mp3(os.path.join(directory, file))
   combined += audio

  combined.export(os.path.join(directory, "combined.mp3"), format="mp3")

  combined = AudioSegment.from_file("C:/Users/Ritika/Desktop/flask_app/flask_app/song0.mp3", format="mp3")

  for i in range(1,len(url_list)):
    combined += AudioSegment.from_file('song'+str(i)+'.mp3', format="mp3")
      
  combined.export("C:/Users/Ritika/Desktop/flask_app/static\\js\\combined.mp3", format="mp3")
  return jsonify({'result': final}) aur 180 pe tha ye line"""
  #  string =''
  #  string = ' '.join([str(elem) for elem in new1])
    # string
############################################## KASHMIRI TO ENGLISH ################################################################# 

@app.route('/kash')
def kashtest():
  print("inside first app route of kash")
  return render_template('kashmiri_english.html')

@app.route('/kash',methods=['POST'])
def kash():
    
  # ***Kashmiri to English***"""
   ks = request.form['result']
   #ks = 'हु dɔdι baci छु akh diltang dɔdι baci'
   print(ks)
   lis1 = []
   for words in ks.split(" "):
    lis1.append(words.lower())

    # lis1

   eng = []
   df1 = pd.read_csv('finalset.csv')
   df1.reset_index(drop=True,inplace=True)

    # Looping through the words
   for word in lis1:
     # Searching the word in the "Words" column of the DataFrame
     if word in df1["word"].values:
       # Getting the index of the matching word
       index = df1[df1["word"] == word].index[0]

       # Printing the corresponding meaning from the "Meanings" column
       mean = df1.at[index, 'meaning']
       eng.append(index)

    # eng

   new2 = []
   for i in eng:
    new2.append(df1['meaning'][i])

    # new2

   string1 =''
   string1 = ' '.join([str(elem) for elem in new2])
    # string1
   language = 'en'

   myobj = gTTS(text=string1, lang=language, slow=False)

   myobj.save("welcome.mp3")

   os.system("mpg321 welcome.mp3")

    

   """  a=str('हु dɔdι baci छु akh diltang dɔdι baci')
    print(a) """
   return jsonify({'result': string1})
  #  return "Hello"
   #return render_template('kashmiri_english.html',kashmiri_out=string1)



  #  word_url = df[['word','file_urls']]

    # word_url

  #  df_new1.drop(['newmeaning'],axis=1,inplace=True)
  #  df_new1.dropna(inplace =True)
  #  df_new1.reset_index(inplace=True)
  #  df_new1.to_csv('newstops.csv')

  #  stop = pd.read_csv('newstops.csv')

    # stop

    # stop.columns

  #  stop_urls = pd.read_csv(r'C:\\Users\\Ritika\\Desktop\\flask_app\\flask_app\\newstopurl.csv')

  #  stop_urls.drop({"Unnamed: 0"},axis=1,inplace=True)

    # stop_urls

  #  frames = [word_url,stop_urls]
  #  urls = pd.concat(frames)

  #  urls.reset_index(inplace=True)

  #  urls.drop(['index'],axis=1,inplace=True)

    # urls.head()

  #  urls.isnull().sum()

  #  url_list = []

  #  for temp in new1:    
  #   if temp in urls['word'].values:
  #     index = urls[urls["word"] == temp].index[0]
  #     url_list.append(urls["file_urls"][index])

    # url_list

  #  urls['word'][1182]

    # len(url_list)


  #  chunk_size = 512  # Number of bytes to download at a time
  #  delay = 2.0

  #  for i in range(len(url_list)):
  #   response = requests.get(url_list[i], stream=True)
  #   filename = 'song'+str(i)+'.mp3'
  #   with open(filename, 'wb') as f:
  #     for chunk in response.iter_content(chunk_size=chunk_size):
  #       f.write(chunk)
  #       time.sleep(delay)

    

  #  directory = "C:/Users/Ritika/Desktop/flask_app/flask_app"

  #  mp3_files = [file for file in os.listdir(directory) if file.endswith(".mp3")]

  #  combined = AudioSegment.empty()
  #  for file in mp3_files:
  #     audio = AudioSegment.from_mp3(os.path.join(directory, file))
  #     combined += audio

  #  combined.export(os.path.join(directory, "combined.mp3"), format="mp3")

  #  combined = AudioSegment.from_file("C:/Users/Ritika/Desktop/flask_app/flask_app/song0.mp3", format="mp3")

  #  for i in range(1,len(url_list)):
  #   combined += AudioSegment.from_file('song'+str(i)+'.mp3', format="mp3")
      
  #  combined.export("C:/Users/Ritika/Desktop/flask_app/static\\js\\combined.mp3", format="mp3")

  #  string =''
  #  string = ' '.join([str(elem) for elem in new1])
    # string





  
  








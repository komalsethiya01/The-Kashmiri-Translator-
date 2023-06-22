# तरजमअ् :The-Kashmiri-Translator
The Kashmiri Translator aims to translate English into Kashmiri language and vice versa. It takes audio/text input from the user and gives the corresponding translation in audio/text format.It is based on machine learning algorithms and  uses various Natural Language Processing techniques such as Word lemmatization, tokenization, etc. It utilizes a dataset of parallel corpora for training the model.
This project can perform two actions, one being to convert from English to Kashmiri and visa-versa. If the input to the translator is in the speech/audio format, the speech is first converted into text using python's speech recognition library. 
The next step uses NLP technique called Word Tokenization and Word Lemmatization whch breaks down the sentence into it's root words to get the root meaning of the words. Then the corresponding sentence in Kashmiri is generated which has the same meaning as the root words.
The most important and difficult step is to generate the audio output in Kashmiri language. Due to the limited Kashmiri dataset, manaually a dataset is created which contains the audio files of Kashmiri words and stop words.
These audio files are hosted on the web browser and the model later uses these audio files to generate a complete meaningful audio file of the Kashmiri sentence.
Hence, the translator provides the Kashmiri translation in both the format i.e text translation and audio translation.

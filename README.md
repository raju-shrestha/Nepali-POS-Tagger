## Literature Review Research

Parts of Speech Tagger for Nepali Text Using SVM is an application that assigns the appropriate parts of speech like noun, pronoun, verb, adverb, adjective etc. and other lexical tags to each word written in Nepali language based on its definition as well as context. The parts of speech tagger is build using the supervised machine leaning algorithm namely Support Vector Machine. The model uses 14 million Nepali words and the corpus consists of written text from 15 different genres with 2000 words each published between 1990 and 1992 and the texts from a wide range of sources such as internet webs, newspapers, or books. And, the model is trained with 80,000 lemmatized words collected from the Nepali National Monolingual Written Corpus. 
 
The Parts of Speech tagger for Nepali text has a wide range of scope in research and NLP applications such as machine translation, speech recognition, speech synthesis, grammar checker, information retrieval, and extraction. 
 
Nepali is a  morphologically rich language and one has to consider many features to build the language model. The SVM based POS tagger construct the feature vectors for each word in input and classify the word into one of the two classes (One Vs Rest). 
 
The performance analysis includes different components such as known words, unknown words, and the size of the training data. The average accuracy obtained for lemmatized text and unprocessed raw text is 88% and 72% respectively. 
  
  
Steps to run:
1. Place the nnc_updated_ah folder at the correct location
2. Run the ParseXMLCorpus.py to parse the tags from Nelralac 
3. Run ExtractFeatures.py to extract the features from tagset
4. Run getFeatures.py to get the extracted features of tagset
5. Run test.py to test the result
6. Run pou-ui.py to display in the browser

import re 
import string 
import nltk
import numpy as np
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
from joblib import load 

nltk.download("wordnet")
nltk.download('stopwords')

# change these file locations as required 
#model_fn = 'Logreg.joblib'
model_fn = 'MultNB.joblib'
#model_fn = 'SGD.joblib'
vect_fn = 'vect.joblib'

# remove certain pronouns from stop words to give more context 
sw_nltk = stopwords.words('english')
pronouns = ['i', 'me', 'myself', 'my','you','your','yours','yourself', 
            'yourselves','he','him','his','himself','she',"she's",'her',
            'hers','herself']
sw_nltk = [w for w in sw_nltk if w not in pronouns]

# lemmatizer
lem = WordNetLemmatizer()

# load model and vectorizer
model = load(model_fn)
vect = load(vect_fn)

#pre processing function for receiving input strings
def text_pre_processing(input_string):
    """ Given a document (a string) preprocess the document 
    by removing punctuation, extra whitespace, and stop words 
    and return the preprocessed document. """

    stop_words = set(sw_nltk)
    pattern = r'\b(' + r'|'.join(stop_words) + r')\b\s*'


    # remove punctuation
    text = re.sub('[%s]' % re.escape(string.punctuation), ' ', input_string)

    # remove stopwords
    words = re.sub(pattern, '', text.lower(), flags=re.IGNORECASE)

    # remove extra whitespace
    words = re.sub('\s+', ' ', words).strip()

    words = words.split()
    words = ' '.join([lem.lemmatize(w) for w in words])
    
    return words

def handle_response(message) -> str:
    #so message here is what is SENT by the person,
    #can preprocess the message and then maybe run the model on it
    p_message = text_pre_processing(message)

    #convert to a numpy array so that it can be transformed
    list_message = [p_message]
    #list_message = np.asarray([p_message])
    print(p_message, type(p_message), type(list_message))
    pred = model.predict(vect.transform(list_message))

    #based on what the model returns,
    #we prefix the message with 0 (no problem), 1 (hate), or 2 (depressive)
    p_message = "" + str(pred[0]) + message
    return p_message
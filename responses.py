import re 
import string 
import nltk
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
from joblib import load 

nltk.download("wordnet")
nltk.download('stopwords')

model_fn = '/Users/eerinahaque/projects/scu/coen140/COEN140-group-project/data/model.joblib'

# remove certain pronouns from stop words to give more context 
sw_nltk = stopwords.words('english')
pronouns = ['i', 'me', 'myself', 'my','you','your','yours','yourself', 
            'yourselves','he','him','his','himself','she',"she's",'her',
            'hers','herself']
sw_nltk = [w for w in sw_nltk if w not in pronouns]

# lemmatizer
lem = WordNetLemmatizer()

# load model 
model = load(model_fn)

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
    
    #based on what the model returns,
    #we prefix the message with 0 (no problem), 1 (hate), or 2 (depressive)
    p_message = '0' + p_message
    return p_message
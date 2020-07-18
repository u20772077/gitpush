import nltk
import warnings
warnings.filterwarnings("ignore")
nltk.download() # for downloading packages
#import tensorflow as tf
import numpy as np
import random
import string # to process standard python strings

f=open('mathematicstheorem.txt','r',errors = 'ignore')
m=open('helpernowledge.txt','r',errors = 'ignore')
#checkpoint = "./chatbot_weights.ckpt"
#session = tf.InteractiveSession()
#session.run(tf.global_variables_initializer())
#saver = tf.train.Saver()
#saver.restore(session, checkpoint)

raw=f.read()
thehelp=m.read()
raw=raw.lower()# converts to lowercase
helper=thehelp.lower()# converts to lowercase
nltk.download('punkt') # first-time use only
nltk.download('wordnet') # first-time use only




sent_tokens = nltk.sent_tokenize(raw)# converts to list of sentences 
word_tokens = nltk.word_tokenize(raw)# converts to list of words
sent_tokenshelp = nltk.sent_tokenize(helper)# converts to list of sentences 
word_tokenshelp = nltk.word_tokenize(helper)# converts to list of words


sent_tokens[:2]
sent_tokenshelp[:2]

word_tokens[:5]
word_tokenshelp[:5]

lemmer = nltk.stem.WordNetLemmatizer()
def LemTokens(tokens):
    return [lemmer.lemmatize(token) for token in tokens]
remove_punct_dict = dict((ord(punct), None) for punct in string.punctuation)
def LemNormalize(text):
    return LemTokens(nltk.word_tokenize(text.lower().translate(remove_punct_dict)))

Introduce_Ans = ["My name is Buddy.","Hi  buddy wanna lean something new?."," Hello i am buddy and im your friend ","Hello ....:)"]
GREETING_INPUTS = ("hello", "hi","hi hi", "8ta", " Awe ","greetings", "sup", "what's up","hey")
GREETING_RESPONSES = ["hi", "hey", "hii there", "hi there", "hello", "Hi buddy", "buddy", " buuuudyy"," budeee"]
Basic_Q = ("who made youand what is your purpose", " what is your purpose"," stete your purpose?" ,"state your purpose please."," state purpose? ", "purpose? ")
baddy_Q =("Do you wanna learn something new?", "Do you love math  ? ... well you will love this..") 
Basic_Ans = "I was made to assist students understand their strengh and weaknesses , help them figure out their career path with an acceptable confidence"

ANSWERPOS = ( "yeah" ,"ok", "alright", "ait", "sure", "go for it", "yes")
ANSWERNEG = [ "No ", " i dont think i do ", " nope", "not really sorry", " eehh" ,"eish can we try that again ", "No" , "i dont think so" ,"No", " Nah"," mmmhmmmh"]
agree = ["you got it ?"," understnd ?", "everything clear so far?"," We good?"," everything fine at this point?"]
#   engage response


#recheck =[ "do you get it?","get it?"," understand?", " got itb ?... "," is that comprihensible ? "]

line1 = [ " The Idea here really is to prove that angle x  = angle y .First start by construction,That is draw a straight line passing throught the origin O to a point on the circumference C ,and a line from B to C. This makes a new angle, call it z."]
line2 = ["Now ,let angle(OAB) be a ,OCB be z"]
line3  = ["From the previous statement we can say a + x = 90"]
line4 = ["Now , triangle ABC ( sum of interior angles  = 180), which means a + z + n = 180"]
line5 = ["Following this argument , we can say z + a = 90"]
line6 = ["We have z = 90 - a , and  x = 90 - a"]
line7 =["By lemma : An angle subtended by the same"]


# Checking for greetings
def greeting(sentence):
    """If user's input is a greeting, return a greeting response"""
    for word in sentence.split():
        if word.lower() in GREETING_INPUTS:
            return random.choice(GREETING_RESPONSES)

# Checking for Basic_Q
def basic(sentence):
    for word in Basic_Q:
        if sentence.lower() == word:
            return Basic_Ans


     
         
# Checking for Basic_QM
def basicM(sentence):
    """If user's input is a greeting, return a greeting response"""
    for word in Basic_Om:
        if sentence.lower() == word:
            return random.choice(Basic_AnsM)
        
# Checking for Introduce
def IntroduceMe(sentence):
    return random.choice(Introduce_Ans)


from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


# Generating response
def response(user_response):
    robo_response=''
    sent_tokens.append(user_response)
    TfidfVec = TfidfVectorizer(tokenizer=LemNormalize, stop_words='english')
    tfidf = TfidfVec.fit_transform(sent_tokens)
    vals = cosine_similarity(tfidf[-1], tfidf)
    idx=vals.argsort()[0][-2]
    flat = vals.flatten()
    flat.sort()
    req_tfidf = flat[-2]
    if(req_tfidf==0):
        robo_response=robo_response+"I am sorry! I don't understand you"
        return robo_response
    else:
    
        robo_response = robo_response+sent_tokens[idx]
        return robo_response

 
# Generating response


'''
def responsehelper(user_response):
    robo_response=''
    sent_tokensone.append(user_response)
    TfidfVec = TfidfVectorizer(tokenizer=LemNormalize, stop_words='english')
    tfidf = TfidfVec.fit_transform(sent_tokensone)
    vals = cosine_similarity(tfidf[-1], tfidf)
    idx=vals.argsort()[0][-2]
    flat = vals.flatten()
    flat.sort()
    req_tfidf = flat[-2]
    if(req_tfidf==0):
        robo_response=robo_response+"I am sorry! I don't understand you"
        return robo_response
    else:
        robo_response = robo_response+sent_tokensone[idx]
        return robo_response
'''


def buddycommand(sentence):
    for word in sentence.split():
        if word in ANSWERPOS:
           return
  
            
            
   
        elif word in ANSWERNEG:
            return "please input your next request"

    

      
# theorem responce
def reresponse(rewinder):
    robo_re_response=''
    sent_tokens.append(rewinder)
    TfidfVec = TfidfVectorizer(tokenizer=LemNormalize, stop_words='english')
    tfidf = TfidfVec.fit_transform(sent_tokenshelp)
    vals = cosine_similarity(tfidf[-1], tfidf)
    idx=vals.argsort()[0][-2]
    flat = vals.flatten()
    flat.sort()
    req_tfidf = flat[-2]
    if(req_tfidf==0):
        robo_re_response=robo_re_response+"I am sorry! I don't understand you"
        return robo_re_response
    else:

        
        robo_re_response = robo_re_sponse+sent_tokenshelp[idx]

        
        return robo_re_response









 # proceed with providing information



def continued(lineancor):
    robo_response=''
    sent_tokens.append(cont)
    TfidfVec = TfidfVectorizer(tokenizer=LemNormalize, stop_words='english')
    tfidf = TfidfVec.fit_transform(sent_tokens)
    vals = cosine_similarity(tfidf[-1], tfidf)
    idx=vals.argsort()[0][-2]
    flat = vals.flatten()
    flat.sort()
    req_tfidf = flat[-2]
    if(req_tfidf==0):
        robo_response=robo_response+"I didnt get that , try to be more informative"
        return robo_response
    else:
        robo_response = robo_response+sent_tokens[idx]
        return robo_response     













def talk(user_response):
   
    user_response=user_response.lower()
    keyword = " Tangent theorem "
    keywordone = "line "
    keywordsecond = " lemma"
    




    if(user_response!='bye'):
        if(user_response=='thanks' or user_response=='thank you' ):
            flag=False
            #print("ROBO: You are welcome..")
            return "You are welcome.."
        elif(basicM(user_response)!=None):
            return basicM(user_response)
        else:
            if(user_response.find(keyword) != -1 or user_response.find(keywordone) != -1 or user_response.find(keywordsecond) != -1):
                #print("ROBO: ",end="")
                #print(responseone(user_response))
                '''
                return responsehelper(user_response)
                sent_tokensone.remove(user_response)
                '''
            elif(greeting(user_response)!=None):
                #print("ROBO: "+greeting(user_response))
                   return greeting(user_response)
            elif(user_response.find("Who are you") != -1 or user_response.find(" you are") != -1 or user_response.find(" and you are ") != -1 or user_response.find(" your name ") != -1):
                     return IntroduceMe(user_response)
            elif(basic(user_response)!=None):
                    return basic(user_response)
          
            else:
                #print("ROBO: ",end="")
                #print(response(user_response))
                return response(user_response) 
                sent_tokens.remove(user_response)
                
    else:
        flag=False
        
        return " i hope i was helpful today ...."



def test(user_response):
    import pyodbc
    questn_num = user_response[:2]
    cntn=pyodbc.connect('Driver={SQL Server};Server=LAPTOP-DG9KS6R0\SQLEXPRESS2019;Database=Buddydb;Trusted_Connection=yes;')
    cur = cntn.cursor()
    cur.execute("select answer from dbo.mathquestions where id = "+str(questn_num))
    
    row = cur.fetchone() 
    ans = row[0]
    if ans is None :
        ans = "True"
    #ans=ans.lower()
   
   
    user_response = user_response[3:]
    
    if user_response == ans:
        
        cur.execute("select ratings from dbo.mathquestions where id = "+str(questn_num))
        row = cur.fetchone() 
        ans = row[0]
        if ans is None:
            ans = 0
        grade = ans
        
        s  =grade +1
        input = (s)
        cur.execute("UPDATE dbo.mathquestions SET ratings = ? WHERE id = "+str(questn_num), (s))
        
        cntn.commit()
        return "The Answer You Provided is correct...Try the next one"
    else:
        
        cur.execute("select ratings from dbo.mathquestions where id = "+str(questn_num))
        row = cur.fetchone() 
        ans = row[0]
        if ans is None:
            ans = 0
        grade = ans
        s  =grade - 1
        input = (s)
        cur.execute( "UPDATE dbo.mathquestions SET ratings = ? WHERE id = "+str(questn_num),(s))
        
        cntn.commit()
        return "Your answer does not match the one we have....You can try again"

def ava():
    cur.execute("SELECT AVG(ratings) AS average FROM dbo.mathquestions")
    results = cur.fetchall()
    for i in results:
        ave = float(i[0])
    return ave

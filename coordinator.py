import pandas as pd
import numpy as np
import matplotlib.pyplot as plt                                                 #Подключаем Matplotlib
import re
import pickle
import pymorphy2
import json
from flask import Flask, jsonify, request
import string
log_file_coordinator='logs_coordinator.txt'
with open('./key_words_coordinator.json', 'r') as fp:
    key_words = json.load(fp)

def converter(sentence):
    list = []
    words = sentence.split()
    for item in words:
        list.append(pymorphy2.MorphAnalyzer().parse(item)[0].normal_form)
    return ' '.join(list)


def clear_text(new_text):

  pattern_number=r'[0-9]'
  new_text=re.sub(pattern_number,'',new_text)
  new_text=' '.join( [w for w in new_text.split() if len(w)>1] )
  new_text=re.compile("[" + re.escape(string.punctuation) + "]").sub("", new_text)
  return new_text



def predict_tags(a):
  
  a=clear_text(a)
  a=converter(a)
  keys=[ key_words[i] for i in key_words.keys() if i in a.lower()]
  return set(keys)

app = Flask(__name__)

@app.route('/', methods=['POST'])
def main():
    with open (log_file_coordinator, mode='a',encoding='utf8') as f:
        try:
            # print(request)
            data = request.form.get('key')
            print('text from student ', data,file=f)
            result=list(predict_tags(data))
            res={}
            for i,tag in enumerate(result):
                res.update({i:tag})
            print(res,file=f)
            return json.dumps(res,ensure_ascii=False).encode('utf8')

        except Exception as e:
            print(type(e),e,file=f)
if __name__ == '__main__':
    app.run(debug=False, port=2248)

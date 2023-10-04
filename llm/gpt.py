# -*- coding: utf-8 -*-
import os
import openai

class Gpt:
    
    def __init__(self):        
        
        openai.api_key = os.environ.get("OPENAI_API_KEY", None)        
        if openai.api_key is None:
            raise Exception("openai's key is None")
    
    def post_proc(self, txt):
        try:
            model_name = os.environ.get("CHAT_MODEL_DEPLOYMENT_NAME")
            completion = openai.ChatCompletion.create(
                 model=model_name,
                 messages=[{"role": "user", "content": txt},
                          ],
                 timeout=5,         
                 )                
             
            txt = completion.choices[0].message['content']
            txt = txt.encode('unicode_escape').decode('unicode_escape')
        except Exception as e:
            print('chatgpt is timeout')
            txt = ''        
        return txt            
        
if __name__ == "__main__":    
    pq = Gpt()    
    question = '杜甫的雪景的句子'
    res = pq.post_proc(question)
    print(res)
   
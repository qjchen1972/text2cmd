# -*- coding: utf-8 -*-
from transformers import AutoTokenizer, AutoModelForCausalLM, AutoModel
import torch
import os

class Glm:

    def __init__(self):
    
        model_path = '../models/glm' 
        model_path = os.path.join(os.path.dirname(__file__), model_path)
        self.tokenizer = AutoTokenizer.from_pretrained(
                      model_path, 
                      trust_remote_code=True)
        model = AutoModel.from_pretrained(
                      model_path,
                      trust_remote_code=True)
                      
        device = torch.cuda.current_device()\
                     if torch.cuda.is_available() else "cpu"              
        model = model.half().to(device) #cuda()
        self.model = model.eval()     
    
    def post_proc(self, txt):
        response, history = self.model.chat(self.tokenizer, 
                     txt, history=[])
        return response
        
    
        
if __name__ == "__main__":  

    import time  
    pq = Glm()    
    question = '杜甫的雪景的句子'
    start = time.time()
    res = pq.post_proc(question)
    print(time.time() - start, res)
 
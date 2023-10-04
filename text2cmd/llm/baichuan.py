# -*- coding: utf-8 -*-
from transformers import AutoTokenizer, AutoModelForCausalLM, AutoModel
from transformers.generation.utils import GenerationConfig
import torch
import os

# install bitsandbytes-0.40.1 in windows
# pip install https://github.com/jllllll/bitsandbytes-windows-webui/releases/download/wheels/bitsandbytes-0.40.1.post1-py3-none-win_amd64.whl
class Baichuan:    
    
    def __init__(self):
        model_path = '../models/baichuan13b'
        model_path = os.path.join(os.path.dirname(__file__), model_path)
        
        self.tokenizer = AutoTokenizer.from_pretrained(
                      model_path,
                      use_fast=False, 
                      trust_remote_code=True)                
        self.model = AutoModelForCausalLM.from_pretrained(
                      model_path, 
                      device_map="auto", 
                      torch_dtype=torch.bfloat16, 
                      trust_remote_code=True)
                      
        self.model.generation_config = GenerationConfig.from_pretrained(
                      model_path)

    def post_proc(self, txt):
        messages = []
        messages.append({"role": "user", "content": txt})
        response = self.model.chat(self.tokenizer, messages)
        return response
    
        
if __name__ == "__main__":
    import time
    
    pq = Baichuan()
    
    question = '杜甫的雪景的句子'
    start = time.time()
    res = pq.post_proc(question)
    print(time.time() - start, res)

# -*- coding: utf-8 -*-
import time
import os
import text2cmd as tc
        
if __name__ == "__main__":
    
    path = './template_prompt'
    name = 'post_wav_prompt.txt'
    usemodel = tc.Gpt()
    pq = tc.PostQuery(path, name, usemodel=usemodel)    
    
    start = time.time() 
    question = 'du huo miao xie mei nv de shi ge'
    res = pq.post_proc(question=question)
    print(time.time() - start, res, len(res))

# -*- coding: utf-8 -*-
import time
import os
from text2cmd import PostQuery
        
if __name__ == "__main__":
    
    path = './template_prompt'
    name = 'post_wav_prompt.txt'
    usemodel = tc.Gpt()
    pq = PostQuery(path, name, usemodel=usemodel)    
    
    start = time.time() 
    question = 'du huo miao xie mei nv de shi ge'
    res = pq.post_proc(question)
    print(time.time() - start, res, len(res))

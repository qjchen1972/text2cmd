# -*- coding: utf-8 -*-
from jinja2 import Environment, FileSystemLoader
import os
import tiktoken
from .llm.baichuan import Baichuan
from .llm.glm import Glm
from .llm.gpt import Gpt
from dotenv import load_dotenv

load_dotenv(os.path.join(os.path.dirname(__file__), ".env"))


class PostQuery:
    
    def __init__(self, template_path, template_name, usemodel):        
        
        self.template = Environment(
           loader=FileSystemLoader(template_path)
        ).get_template(template_name)  
        
        self.model = usemodel
        '''
        if use == 'gpt':
            self.model = Gpt()
        elif use == 'glm':
            self.model = Glm()
        elif use == 'baichuan':
            self.model = Baichuan()
        else:
            raise Exception("model init Error")
        '''    
            
    def count_token(self, text: str) -> int:
        encoding = tiktoken.get_encoding("cl100k_base")
        return len(encoding.encode(text))
    
    def render_with_token_limit(self, **kwargs):
        text = self.template.render(**kwargs)
        token_count = self.count_token(text)
        token_limit = os.environ.get("PROMPT_TOKEN_LIMIT", 1024)
        token_limit = int(token_limit)
        if token_count > token_limit:
            message = f"token count {token_count} exceeds limit {token_limit}"
            assert False, message
        return text       
        
    def post_proc(self, txt):    
        prompt = self.render_with_token_limit(question=txt)
        res = self.model.post_proc(prompt)
        return res        
        


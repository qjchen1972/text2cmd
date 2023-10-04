# text2cmd

# Configure and download some large models that support Chinese(optional)

* chagpt
  
  build .env:  
  OPENAI_API_KEY='your api key'  
  CHAT_MODEL_DEPLOYMENT_NAME=gpt-3.5-turbo  
  PROMPT_TOKEN_LIMIT=2000  
  MAX_COMPLETION_TOKENS=256

* chatglm2
  
  1. [download](https://huggingface.co/THUDM/chatglm2-6b)
  2. Place the downloaded model and configuration files in the directory: models/glm
 
* baichuan

  1. [download](https://huggingface.co/baichuan-inc/Baichuan2-13B-Chat-4bits)
  2.  Place the downloaded model and configuration files in the directory: models/baichuan13b
  3.  Possible troubles: install bitsandbytes-0.40.1 in windows
      pip install https://github.com/jllllll/bitsandbytes-windows-webui/releases/download/wheels/bitsandbytes-0.40.1.post1-py3-none-win_amd64.whl

# test

$ python test_text2cmd.py
  

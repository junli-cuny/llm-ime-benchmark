### how to run this file?
# before run: go to current folder
# python -m venv venv
#. venv/bin/activate

### case1: Please make sure the IME has been set to Pinyin_Simplified if Input is Chinese Words or Simplified Chinese Sentences
### case2: Please make sure the IME has been set to Pinyin_Traditional if Input is Tradtional Chinese Sentences

# python -u System_Pinyin_IME.py

import subprocess

def activate_chinese_input():
    script = 'tell application "System Events" to keystroke "space" using {control down, shift down}'
    subprocess.run(['osascript', '-e', script])

# Call the function to activate the Chinese input method
activate_chinese_input()


import pandas as pd
import numpy as np
import time
from pynput.keyboard import Key, Controller
import keyboard as ky
import re
from time import process_time
import string
from zhon.hanzi import punctuation
from simhash import Simhash


def simhash_demo(text_a, text_b):
    """
    Get two texts' similarity
    :param text_a:
    :param text_b:
    :return:
    """
    a_simhash = Simhash(text_a)
    b_simhash = Simhash(text_b)
    max_hashbit = max(len(bin(a_simhash.value)), len(bin(b_simhash.value)))
    # Hamming Distance
    distince = a_simhash.distance(b_simhash)
    print(distince)
    similar = 1 - distince / max_hashbit
    return similar



def type_chinese_pinyin(pinyin_text):
    keyboard = Controller()

    # Type the Pinyin text
    keyboard.type(pinyin_text)
    
    ky.press_and_release('space')
    time.sleep(0.5) 
    ky.press_and_release('enter')
    time.sleep(1) 


# Call the function to type Chinese characters using Pinyin

## Take Chinese Words.df as an example 
df=pd.read_excel("Chinese_Words.xlsx",sheet_name="wl=2to9")

for i in range(df.shape[0]):
    text_no_spaces =  df.pinyin.iloc[i].replace(" ", "")
    t1_start=time.time()
    df.sys_pinyin_gen.iloc[i]=input(type_chinese_pinyin(text_no_spaces))
    t1_stop=time.time()
    df.sys_pinyin_time.iloc[i]=t1_stop-t1_start-1.5
    print("No",i,df.sys_pinyin_gen.iloc[i])
    print("No",i,df.sys_pinyin_time.iloc[i])


# Text Similarity 
for i in range(df.shape[0]):
        gen_text=''.join(filter(lambda x: x not in punctuation, df["sys_pinyin_gen"].iloc[i]))
        org_text=''.join(filter(lambda x: x not in punctuation, df.hanzi.iloc[i]))
        df.sys_simhash_textsim.iloc[i]=simhash_demo(gen_text,org_text)

df.to_csv("system_Pinyin_IME_gen.csv",index=False) 
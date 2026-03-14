### how to run this file?
# before run: go to current folder
# python -m venv venv
#. venv/bin/activate

### case1: Please make sure the IME has been set to Hiragana(Google) if AI_type=="Kanji" or "Hira" in "Japanese_Words"
### case2: Please make sure the IME has been set to Katagana(Google) if AI_type=="kata" in "Japanese_Words"
### case3: Please make sure the IME has been set to Hiragana(Google) if input is the romanji of "Japanese Sentence"

# python -u System_Pinyin_IME.py

import subprocess

def activate_japanese_input():
    script = 'tell application "System Events" to keystroke "space" using {control down, shift down}'
    subprocess.run(['osascript', '-e', script])

# Call the function to activate the Japanese input method
activate_japanese_input()


import pandas as pd
import numpy as np
import time
from pynput.keyboard import Key, Controller
import keyboard as ky
import re
from time import process_time
import string
from zhon.hanzi import punctuation



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

#Change current IME to hiragana
def type_japanese_kanji(romanji_text):
    keyboard = Controller()
    # Type the Pinyin text
    keyboard.type(romanji_text) 
    #ky.press_and_release('space')
    ky.press_and_release('down')
    time.sleep(0.5) 
    ky.press_and_release('enter')
    time.sleep(1) 
    keyboard.type('\n') 
# Change current IME to hiragana/katagana before running following function.
def type_japanese_kana(romanji_text):
    keyboard = Controller()
    keyboard.type(romanji_text)
    time.sleep(0.5) 
    ky.press_and_release('enter')
    time.sleep(1) 
    keyboard.type('\n') 
# Call the function to type Chinese characters using Pinyin

## Case 1: Romanji as Input and generate result is the kanji
df=pd.read_excel("Japanese_Words.xlsx",sheet_name="N1_N5")

def kotoeri_jw_kanji(df):
#lst=['zuratto','akarasama','akudoi','akudoi','asoko','ano','ikanimo','iyani','mondai demo？','mata ame da.','konnani nagai kan matasetegomennasai.','karera ha watashitachi wo yuushoku nimotenashitekureta.']
    for i in range(df.shape[0]):
        if df["AI_type"].iloc[i]=="kanji":
            t1_start=time.time()
            df.sys_gen.iloc[i]=input(type_japanese_kanji(df.romanji.iloc[i]))
            t1_stop=time.time()
            df.sys_time.iloc[i]=t1_stop-t1_start-1.5
            print("No",i,df.sys_gen.iloc[i])
            print("No",i,t1_stop-t1_start-1.5)
    ## Case 2: Romanji as Input and generate result is the hiragana or input is the Japanese Sentences
        elif df["AI_type"].iloc[i]=="hira":
            t1_start=time.time()
            df.sys_gen.iloc[i]=input(type_japanese_kana(df.romanji.iloc[i]))
            t1_stop=time.time()
            df.sys_time.iloc[i]=t1_stop-t1_start-1.5
            print("No",i,df.sys_gen.iloc[i])
            print("No",i,t1_stop-t1_start-1.5)

## Case3: Romanji as Input and generate result is the katagana with IME is set to Katagana(Google)
def kotoeri_jw_kana(df):
    for i in range(df.shape[0]):
        if df["AI_type"].iloc[i]=="kata":
            t1_start=time.time()
            df.sys_gen.iloc[i]=input(type_japanese_kana(df.romanji.iloc[i]))
            t1_stop=time.time()
            df.sys_time.iloc[i]=t1_stop-t1_start-1.5
            print("No",i,df.sys_gen.iloc[i])
            print("No",i,t1_stop-t1_start-1.5)
# Text Similarity 
# Japanese words
for i in range(df.shape[0]):
  gen_text=''.join(filter(lambda x: x not in punctuation, df["sys_gen"].iloc[i]))
  if df.AI_type.iloc[i]=="kanji":
    org_text=''.join(filter(lambda x: x not in punctuation, df.kanji.iloc[i]))
    df.sys_simhash_textsim.iloc[i]=simhash_demo(gen_text,org_text)
  else:
    org_text=''.join(filter(lambda x: x not in punctuation, df.kana.iloc[i]))
    df.sys_simhash_textsim.iloc[i]=simhash_demo(gen_text,org_text)       

## Japanese Sentences
for i in range(df.shape[0]):
    org_text=''.join(filter(lambda x: x not in punctuation, df.org_sentence.iloc[i]))
    gen_text=''.join(filter(lambda x: x not in punctuation, df["sys_gen"].iloc[i]))
    df.sys_simhash_textsim.iloc[i]=simhash_demo(gen_text,org_text)

df.to_csv("Kotoeri_IME_gen.csv",index=False) 
# Chinese Phonetic (Pinyin) Error Dataset

## Overview
This directory contains the **Chinese Phonetic (Pinyin) Error Dataset**, introduced in the LREC 2026 paper: *"Benchmarking Large Language Models for Text Input in Chinese and Japanese"*. 

This dataset is designed for evaluating the error correction capabilities of Input Method Editor (IME) systems and Large Language Models.

## Dataset Details
- **Language**: Chinese (zho)
- **Derived From**: CSCD-IME Corpus
- **File**: `chinese_error_dataset.csv`
- **Content**: A corpus of Chinese sentences featuring programmatically introduced errors designed to mimic human typing mistakes on a QWERTY keyboard. 
- **Error Types**:
  - **Invalid Pinyin (Phonetic Errors)**: Common typing mistakes including *Missing* (dropped character), *Addition* (extra character), *NearbyKey Typo* (wrong key pressed), and *TwoKey Misorder* (swapped adjacent keys).
  - **Valid Pinyin (Semantic Errors)**: Phonetically valid Pinyin sequences that resolve to incorrect Chinese characters due to homophone ambiguity.

## Usage
This dataset serves as the standard benchmark for Task 2 (Textual Error Correction) evaluated in our paper. It provides a robust testbed for measuring how well models can disentangle both phonetic typos and contextual semantic errors.

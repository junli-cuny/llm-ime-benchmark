# Japanese Phonetic (Romaji) Error Dataset

## Overview
This directory contains the **Japanese Phonetic (Romaji) Error Dataset**, introduced in the LREC 2026 paper: *"Benchmarking Large Language Models for Text Input in Chinese and Japanese"*. 

This dataset is specifically constructed to evaluate the phonetic error correction capabilities of Input Method Editors (IMEs) and language models handling Japanese input.

## Dataset Details
- **Language**: Japanese (jpn)
- **Derived From**: Snow Simplified Japanese Corpus
- **File**: `japanese_error_dataset.csv`
- **Content**: A large corpus of Japanese sentences featuring programmatically introduced Romaji typing errors.
- **Error Types**:
  Errors were injected simulating typical QWERTY keyboard mistakes:
  - **Missing**: A randomly deleted character.
  - **Addition**: A randomly added character.
  - **NearbyKey Typo**: Replacing a character with an adjacent keyboard key.
  - **TwoKey Misorder**: Swapping two adjacent characters.

## Usage
This dataset constitutes the Japanese phonetic typo evaluation for Task 2 (Textual Error Correction) in our benchmark. It tests a model's ability to reconstruct the intended Romaji sequence and subsequently map it to the correct Hiragana/Katakana/Kanji characters despite noisy input.

# Benchmarking Large Language Models for Chinese and Japanese IMEs: Phonetic-to-Character Generation and Textual Error Correction

This repository contains the data, code, evaluation results, and the camera-ready LaTeX source for the paper **"Benchmarking Large Language Models for Chinese and Japanese IMEs: Phonetic-to-Character Generation and Textual Error Correction"** (LREC 2026).

## Overview

Efficient text entry for complex writing systems like Chinese and Japanese relies on Input Method Editors (IMEs). This benchmark evaluates the performance of various Large Language Models (LLMs) compared to traditional baseline systems on two primary tasks:
1. **Phonetic-to-Character Generation**: Converting Pinyin (Chinese) and Romaji (Japanese) inputs into character sequences.
2. **Textual Error Correction**: Detecting and resolving phonetic and semantic errors in text inputs.

## Repository Structure

- `data/`: Contains final evaluation results (`Overall LLMs Result_Final.xlsx`) and our newly created error correction datasets.
  - [`chinese_error_dataset/`](data/chinese_error_dataset/): Chinese Phonetic (Pinyin) Error Dataset.
  - [`japanese_error_dataset/`](data/japanese_error_dataset/): Japanese Phonetic (Romaji) Error Dataset.
- `code/`: Contains the scripts used throughout our methodology:
  - `error_generation/`: Scripts to programmatically inject phonetic errors into clean corpora.
  - `preprocessing/`: Data cleaning and preparation scripts.
  - `experiments/`: Scripts used to run the LLM inferences.
  - `evaluation/`: Scripts calculating metrics (Text Similarity, Word Error Rate, TPS, Completion Time, etc.).
- `figures/`: PDF figures generated from our experiments and utilized within the manuscript.
- `paper/`: The complete, camera-ready LaTeX source code and bibliography for the LREC 2026 submission.

## Datasets

The newly created textual error correction datasets introduced in our paper are publicly available in this repository under the `data/` directory. For the clean base corpora used in our generation tasks (Phrase Pinyin Data, SIGHAN 2015, Yomichan JLPT, and Snow Simplified Japanese Corpus), please refer to the links in our paper's references.

## License & Citation

This repository is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

If you use our datasets or code, please cite our LREC 2026 paper:

```bibtex
@inproceedings{zou2026benchmarking,
  title     = {Benchmarking Large Language Models for Chinese and Japanese IMEs: Phonetic-to-Character Generation and Textual Error Correction},
  author    = {Zou, Yuchun and Lee, Tedd and Fan, Xiaodi and Li, Jun},
  booktitle = {Proceedings of the Language Resources and Evaluation Conference (LREC)},
  year      = {2026}
}
```

# Book Genre Prediction Model

This model will use book titles, summaries, title length, and summary length
to determine the genre of a book. It utilizes the logistic regression ML technique

## TOC

1. `data`: Add all data sets in this folder.
2. `models`: Save all model files `.pkl` in here with the `pickle` module

## Basic Architecture

```
|__ data
    |__ .keep
    |__ data.csv
|__ figures
    |__ .keep
    |__ confusion_matrix_sum_title.png
    |__ confusion_matric_summary.png
    |__ confusion_matrix_title.png
    |__ length_of_sum_title_vs_accuracy.png
    |__ length_of_summary_vs_accuracy.png
    |__ length_of_title_vs_accuracy.png
    |__ prediction_distribution_sum_title.png
    |__ prediction_distribution_summary.png
    |__ prediction_distribution_title.png
|__ models
    |__ .keep
    |__ Model_Revised.ipynb
    |__ book_genre_model_tfidf_sum_title.pkl
    |__ book_genre_model_tfidf_summary.pkl
    |__ book_genre_model_tfidf_title.pkl
    |__ book_genre_transformer_tfidf_sum_title.pkl
    |__ book_genre_transformer_tfidf_summary.pkl
    |__ book_genre_transformer_tfidf_title.pkl
|__ EDA_Revised.ipynb
|__ Data Sheet.pdf
|__ Model Card.pdf
|__ Team Reflection Memo.pdf
|__ dataset-brainstorming.docx
|__ README.md
```

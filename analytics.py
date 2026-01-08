import spacy
from collections import Counter
from experience_levels import EXPERIENCE
import pandas as pd
from stop_words import STOP_WORDS




def analys_data_frames_popular_words(data_frames):
    nlp = spacy.load("ru_core_news_sm", disable=['ner'])
    all_text_requirements = ' '.join(text.lower() for dataFrame in data_frames for text in dataFrame['requirement'].dropna().astype(str))
    doc = nlp(all_text_requirements)

    words = [
        token.lemma_.lower()
        for token in doc
        if token.pos_ in {"NOUN", "PROPN"}
        and not token.is_stop
        and token.lemma_.lower() not in STOP_WORDS              
        and not token.is_punct              
        and not token.is_digit              
        and len(token) > 2                  
    ]

    popular_words = Counter(words).most_common(10)

    return popular_words



def stats_by_experience(data_frames):
    vacancy_information = {}
    for ex, data_frame in zip(EXPERIENCE, data_frames):
        mean_salary = data_frame['salary'].mean()
        avg_salary = 0 if pd.isna(mean_salary) else mean_salary
        num_vacancies = len(data_frame)

        vacancy_information[ex] = {
            'avg_salary': avg_salary,
            'num_vacancies': num_vacancies
        }
    return vacancy_information
    





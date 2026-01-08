import matplotlib.pyplot as plt
from experience_levels import EXPERIENCE
 

def plot_salaries_and_vacancies(info_vacancies, top_words):
    experiences = EXPERIENCE
    avg_salaries = [v['avg_salary'] for v in info_vacancies.values()]
    num_vacancies = [v['num_vacancies'] for v in info_vacancies.values()]

   
    fig = plt.figure(figsize=(14, 8))
    gs = fig.add_gridspec(2, 2, height_ratios=[2, 1])


    ax1 = fig.add_subplot(gs[0, 0])
    ax1.bar(experiences, avg_salaries, color='#3498db')
    ax1.set_title("Средняя зарплата по опыту", fontsize=18)
    ax1.set_xlabel("Опыт", fontsize=14, labelpad=30)
    ax1.set_ylabel("Зарплата, ₽", fontsize=14, labelpad=30)
    ax1.margins(x=0.05)  


    ax2 = fig.add_subplot(gs[0, 1])
    ax2.bar(experiences, num_vacancies, color='#e67e22')
    ax2.set_title("Количество вакансий по опыту", fontsize=18)
    ax2.set_xlabel("Опыт", fontsize=14, labelpad=30)
    ax2.set_ylabel("Количество вакансий", fontsize=14, labelpad=30)
    ax2.margins(x=0.05)  


    ax3 = fig.add_subplot(gs[1, :])
    ax3.axis('off')  
    words_text = ", ".join([f"{word}" for word, _ in top_words])
    ax3.text(0.5, 0.4, words_text, ha='center', va='top', fontsize=14)
    ax3.text(0.5, 0.5,"Часто встречающиеся слова", ha='center', va='center', fontsize=16, fontweight='bold')

    plt.tight_layout(pad=1) 
    plt.show()


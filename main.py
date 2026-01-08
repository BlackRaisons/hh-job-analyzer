import aiohttp
import asyncio
from data import get_data
from dataFrames import create_data_frames
from analytics import analys_data_frames_popular_words, stats_by_experience
from experience_levels import EXPERIENCE
from graphs import plot_salaries_and_vacancies
from async_requests import fetch_hhru_api, fetch_valute_api



async def main():

    id_city, vacancie = get_data()

    async with aiohttp.ClientSession() as session:
        valute_task =  asyncio.create_task(fetch_valute_api(session, 'https://www.cbr-xml-daily.ru/daily_json.js'))
        task_list = [fetch_hhru_api(session=session, url_api='https://api.hh.ru/vacancies', params={'text': vacancie,
                                                             'area': id_city,
                                                             'only_with_salary': 'false',
                                                             'per_page': 100,
                                                             'search_field': 'name',
                                                             'experience': experience}) for experience in EXPERIENCE]


        vacancies_data = await asyncio.gather(*task_list)
        valute_response = await valute_task



    
    data_frames = create_data_frames(vacancies_data, valute_response)
    popular_words = analys_data_frames_popular_words(data_frames)
    vacancy_information = stats_by_experience(data_frames)

    plot_salaries_and_vacancies(vacancy_information, popular_words)

    
    
    


if __name__ == '__main__':
    asyncio.run(main())

    
    
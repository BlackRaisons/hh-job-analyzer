import pandas as pd


def create_data_frames(vacancie_data, valute_response):
    data_frames = []
    

    for data in  vacancie_data:
        template_data_frame = {'id': [], 'name': [],'requirement': [] , 'salary': [], 'currency': [],'experience_id': [],  'professional_roles_id': []}

        for info in data.get('items', {}):

            name = info.get('name')
            salary_from = info.get('salary').get('from') if info.get('salary') else None
            salary_to = info.get('salary').get('to') if info.get('salary') else None
            
            salary = None
            if salary_from is not None and salary_to is not None:
                salary = (salary_from + salary_to) / 2
            elif salary_from is not None:
                salary = salary_from
            elif salary_to is not None:
                salary = salary_to
            
            id = info.get('id')
            currency = info.get('salary').get('currency') if info.get('salary') else None
            requirement = info.get('snippet').get('requirement')
            professional_roles_id = info.get('professional_roles')[0].get('id')
            experience_id = info.get('experience').get('id')


            template_data_frame['id'].append(id)
            template_data_frame['name'].append(name)
            template_data_frame['salary'].append(salary)
            template_data_frame['experience_id'].append(experience_id)
            template_data_frame['requirement'].append(requirement)
            template_data_frame['professional_roles_id'].append(professional_roles_id)
            template_data_frame['currency'].append(currency)
        
        data_frame = pd.DataFrame(template_data_frame).drop_duplicates(subset="id")

        valute = valute_response.get('Valute') or {}  
        USD = valute.get('USD', {}).get('Value', 1)  
        EUR = valute.get('EUR', {}).get('Value', 1)  

        data_frame.loc[data_frame['currency'] == 'USD', 'salary'] *= USD
        data_frame.loc[data_frame['currency'] == 'EUR', 'salary'] *= EUR
        data_frame.loc[data_frame['currency'] != 'RUR', 'currency'] = 'RUR'

        data_frames.append(data_frame)

    return data_frames
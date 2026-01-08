async def fetch_hhru_api(session, url_api, params):
    try:
        async with session.get(url_api, params=params) as response:
            if response.status != 200:
                print(f'Ошибка запроса(API-HH-RU): {params}, cтатус: {response.status}')
                return {}
            data = await response.json()
            return data
    except Exception as e:
        print(f'Ошибка при получении данных(API-HH-RU), параметры: {params}, ошибка: {e}')
        return {}

    


async def fetch_valute_api(session, url_api):
    try:
        async with session.get(url_api) as response:
            if response.status != 200:
                print('Ошибка запроса(API-VALUTE)')
                return {}
            return await response.json(content_type=None)
    except Exception as e:
        print(f'Ошибка при получении данных(API-VALUTE), ошибка: {e}')
        return {}
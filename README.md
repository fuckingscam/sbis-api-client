# Описание
sbis-api-client — это Python-библиотека, предназначенная для удобной работы с API СБИС. Она предоставляет простой и интуитивно понятный интерфейс для взаимодействия с различными сервисами СБИС, такими как документооборот, бухгалтерия, CRM и другие.

# Возможности (в разработке)
* Подключение и аутентификация к API СБИС (✔️)
* Отправка запросов к различным сервисам СБИС (❌)
* Получение и обработка данных в удобном формате (❌)
* Работа с документами, контрагентами, задачами и другими объектами (❌)
* Поддержка всех доступных методов API СБИС (❌)

# Установка
Вы можете установить sbis-api-client через pip:
```sh
pip install sbis-api-client
```

# Пример кода
```py
from sbis import SbisClient

client = SbisClient(
    clientId="7760676789310629",
    secret="RWHREDMVWJDHYFZO0CM83MHF",
    secretKey="B9PT47e2j3JGwsswHAzHaU5ssyzoqHsIYFHLjtZYQhlqV8U7eIkF5VIYluyrGwugVv7g1dWRcbSnoCzk10gq961GdzfpUD7INYZiS0wR8K1lrbVwkMjvqi"
)

client.authenticate() # Выполняет аутентификацию пользователя и сохраняет полученный токен и сессионный ID (sid).
client.data() # Выводит данные текущего состояния клиента.
    
points = client.get_points() # Возвращает список точек продаж с учетом заданных параметров.
pricelist = client.get_priceList(pointId=206, actualDate='2020-09-07') # Запрос возвращает информацию о действующих прайс-листах. Чтобы запрос работал корректно, настройте прайс-лист с типом «Выбранные наименования».
nomenclatures = client.get_nomenclatureList(pointId=123, priceListId=555) # Запрос возвращает информацию о товарах и услугах по действующему прайс-листу.
nomenclature_balances = client.get_nomenclature_balances(nomenclatures=[123, 321], warehouses=[456, 789], companies=444) # Запрос возвращает информацию об остатках товаров на складе.
bonus_user = client.get_bonus_client(phone=89207444555, pointId=332)
    
client.logout() # Выполняет выход пользователя из системы, завершая использование текущего токена доступа.
```

# Лицензия
Этот проект распространяется под лицензией MIT. Подробности см. в файле LICENSE.

# Обратная связь
Если у вас возникли вопросы или предложения по улучшению библиотеки, пожалуйста, откройте issue в репозитории на GitHub или свяжитесь с автором (discord: @juzyram)

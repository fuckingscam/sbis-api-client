from sbis import SbisClient

client = SbisClient(
    clientId="7760676789310629",
    secret="RWHREDMVWJDHYFZO0CM83MHF",
    secretKey="B9PT47e2j3JGwsswHAzHaU5ssyzoqHsIYFHLjtZYQhlqV8U7eIkF5VIYluyrGwugVv7g1dWRcbSnoCzk10gq961GdzfpUD7INYZiS0wR8K1lrbVwkMjvqi"
)

client.authenticate() # Выполняет аутентификацию пользователя и сохраняет полученный токен и сессионный ID (sid).
client.data() # Выводит данные текущего состояния клиента.
    
points = client.get_points() # Возвращает список точек продаж с учетом заданных параметров.
pricelist = client.get_priceList(pointId=332, actualDate='21.06.24') # Запрос возвращает информацию о действующих прайс-листах. Чтобы запрос работал корректно, настройте прайс-лист с типом «Выбранные наименования».
nomenclatures = client.get_nomenclatureList(pointId=332, priceListId=33) # Запрос возвращает информацию о товарах и услугах по действующему прайс-листу.
response = client.get_nomenclature_balances(nomenclatures=[123, 321], warehouses=[456, 789], companies=444) # Запрос возвращает информацию об остатках товаров на складе.

bonus_user = client.get_bonus_client(phone=89207444555, pointId=332)
    
client.logout() # Выполняет выход пользователя из системы, завершая использование текущего токена доступа.
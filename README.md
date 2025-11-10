# 2gis_diplom
API-тесты для сервиса, который хранит избранные места пользователей. Используемый стек: Python + requests

2GIS Automation Testing Project — это дипломный проект, цель которого — продемонстрировать навыки автоматизации тестирования API и UI для реального веб-приложения.
В данном случае выбирается 2GIS (веб-версия + Web API) и проверяется:

API:

- Тест создания токена, использования протухшего токена
- Создание места с валидными данными и невалидными
- Создание места с разными параметрами

Используемый стек:
Рекомендации для запуска проекта:

1. Склонируйте проект к себе в репозиторий git clone 
2. Включите виртуальное окружение python -m venv my-first-env
3. Установите зависимости pip install -r requirements.txt

![report.PNG](Reports/diplom_api.PNG)
![report_allure.PNG](Reports/auth.PNG)
Используемый стек: 
<p align="center">
  <img src="https://camo.githubusercontent.com/90220a7692675205d6140ce1112dd5bbf21ebbecf9e882e2c6438823611345a1/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f54656c656772616d2d426f742d626c75653f6c6f676f3d74656c656772616d266c6f676f436f6c6f723d7768697465" />
  <img src="https://camo.githubusercontent.com/8808c5d8c007245cad1166a49f9ac31bc7ab8ede5889206829dea607f333baa8/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f4a656e6b696e732d626c75653f6c6f676f3d6a656e6b696e73266c6f676f436f6c6f723d7768697465" />
  <img src="https://camo.githubusercontent.com/0d62659f4a090a47f5f44e16a0a12ccc47f905e9bf6f9dfd86dd55be1081f1ba/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f416c6c7572652532305265706f72742d322e31352d7265643f6c6f676f3d616c6c757265266c6f676f436f6c6f723d7768697465" />
   <img src="https://camo.githubusercontent.com/3e715d68238077f084e084640eb79ea064e67fcb0f1a28c8b668a14edad02398/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f507974686f6e2d332e31312d626c75653f6c6f676f3d707974686f6e266c6f676f436f6c6f723d7768697465" />
   <img src="https://camo.githubusercontent.com/45142cc7af013644acd8a7cc81c1e53f1eab9493f2cb6a213eb70c66242c4935/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f53656c656e652d322e302d6f72616e67653f6c6f676f3d73656c656e69756d266c6f676f436f6c6f723d7768697465">
</p>
Джоба Jenkins: https://jenkins.autotests.cloud/job/C21-Crunchy_fox-API_tests/
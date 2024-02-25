# Тестовое задание на вакансию "Стажер автоматического тестирования/AQA" от комании SIA Konomic

В задании реализован автотест открывающий страницу https://exchange.konomik.com/ , затем
происходит переход на страницу регистрации и тестируются негативные сценарии для полей на странице Регистрация


## Стэк технологий
- Python
- Selenium Webdirver for Chrome browser
- Pytest

## Как запустить сервис
### * Для корректной работы должен быть обязательно установлен chromedriver последней версии и выполнены настройки разрешащие запускать chromedriver как исполняемый файл
1. git clone https://github.com/EATataris/konomic_test_task

2. cd /konomic_test_task

3. python -m venv vevn - создайте виртуальное окружение

4. - ./venv/bin/activate - активируйте виртуальное окружение (Linux)
   - venv\Scripts\activate.bat (Windows)
   - source selenium_env/bin/activate (macOS)

5. pip install -r requirements.txt - установить все необходимые пакеты
6. pytest -s test_task.py - Запускаем тестовый файл
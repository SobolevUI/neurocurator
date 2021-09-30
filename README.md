# neurocurator

coordinator.py - файл для запуска API координатор
curator.py - файл для запуска API куратор
key_words_coordinator.json - словарь тегов координатор
key_words_curator.json - словарь тегов куратор
logs_coordinator.txt - файл ошибок координатор
logs_curator.txt - - файл ошибок куратор

Для запуска API вводится запрос в следующем виде:
r = requests.post(номер хоста, data = {'key':'текст вопроса от студента'})

Пример: r = requests.post('http://localhost:2248/', data = {'key':'можно ли по шаг отлаживать программу?'})

Для получения результата вводится команда r.json()

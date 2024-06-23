# Использование %:
team1_num = 5
team2_num = 6
print('В команте Мастера кода участников: %s' % (team1_num))
print("Итого сегодня в командах участников: %s и %s!" % (team1_num, team2_num))

# Использование format():
score_2 = 40
team1_time = 8015.2
print("Команда Волшебники данных решила задач: {0}!".format(score_2))
print(" Волшебники данных решили задачи за {} с!".format(team1_time))

# Использование f-строк:
score_1 = 40
score_2 = 42
print(f'Команды решили {score_1} и {score_2} задач.')
challenge_result = 'победа команды Мастера кода'
print(f'Результат битвы: {challenge_result}!')
tasks_total = 82
time_avg = 350.4
print(f'Сегодня было решено {82} задач, в среднем по {350.4} секунды на задачу!')

# coding: utf-8
# license: GPLv3
from enemies import *
from hero import *

def annoying_input_int(message =''):
    answer = None
    while answer == None:
        try:
            answer = input(message)
        except ValueError:
            print('Вы ввели недопустимые символы')
    return answer


def game_tournament(hero, enemy_list):
    for enemy in enemy_list:
        print('Вышел', enemy._type)
        while enemy.is_alive() and hero.is_alive():
            print('Вопрос:', enemy.question())
            answer = annoying_input_int('Ответ:')

            if enemy.check_answer(answer):
                hero.attack(enemy)
                print('Верно!')
                print('**', enemy._type, 'кричит от боли **')
                print('Вы нанесли', hero._attack, 'урона... ', 'У противника осталось', enemy._health, 'очков здоровья!')
            else:
                enemy.attack(hero)
                print('Ошибка! \n** Противник бьёт вас (в следующий раз будьте внимательней) **')
                print('Вам нанесено', enemy._attack, 'урона... ', 'У вас осталось', hero._health, 'очков здоровья!')
        if enemy.is_alive():
            break

        hero.gain_exp(enemy)

        print(enemy._type, 'повержен!\n')

    if hero.is_alive():
        print('Поздравляем! Вы победили!')
        print('Ваш накопленный опыт:', hero._experience)
    else:
        print('К сожалению, Вы проиграли...')

def start_game():

    try:
        print('Добро пожаловать в арифметико-ролевую игру с драконами и троллями!')
        print('Представьтесь, пожалуйста: ', end = '')
        hero = Hero(input())

        enemy_number = 3
        enemy_list = generate_enemy_list(enemy_number)
        assert(len(enemy_list) == 3)
        print('У Вас на пути', enemy_number, 'противников!')
        game_tournament(hero, enemy_list)

    except EOFError:
        print('Поток ввода закончился. Извините, принимать ответы более невозможно.')

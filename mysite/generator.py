import random
import math
from topic.models import Problem, Answer


def operation(m, n, sign):
    if sign == '+':
        return n + m
    elif sign == '-':
        return m - n
    elif sign == '*':
        return m * n
    elif sign == ':':
        return m / n
    elif sign == '^':
        return m ** n


# for i in range(100):
#     a = random.randint(5, 20)
#     b = random.randint(3, 55)
#     res = a / b
#     res_str = str(res)
#     dot_ind = res_str.find('.')
#     res_len_after_coma = abs(dot_ind - len(res_str)) - 1
#     n = random.randint(1, 6)
#     if res_len_after_coma > 6:
#         if res_str[dot_ind + 3] != res_str[dot_ind + 2] and res_str[dot_ind + 3] != res_str[dot_ind + 4] \
#                 and res_str[dot_ind + 1] != res_str[dot_ind + 2] and res_str[dot_ind + 1] != res_str[dot_ind + 3]:
#             ans = round(res, n)
#             if n == 1:
#                 end = 'а'
#             else:
#                 end = 'ов'
#             prob = Problem.objects.create(title='Округлите число',
#                                           condition=f'Округлите число {res} до {n} знак{end} после запятой.',
#                                           answer=ans, theme='rounding')
#             answer = Answer.objects.create(answer=ans)


# answers = []
# for _ in range(50):
#     a, b, c, r, s, q = [], [], [], [], [], []
#     seq1 = [-6, -5, -4, -3, -2, -1, 1, 2, 3, 4, 5, 6]
#     seq2 = [-5, -4, -3, 3, 4, 5, 6, 7, 8]
#     m = [random.randint(1, 6) for _ in range(8)]
#     ans = None
#     x, y, z = random.choice(seq1), random.choice(seq1), random.choice(seq1)
#     n = random.choice([-2, -1, 1, 2])
#     for _ in range(2):
#         temp = random.choice(seq2)
#         a.append(temp)
#         a.append(temp - n)
#     n = random.randint(-2, 2)
#     for _ in range(2):
#         temp = random.choice(seq2)
#         b.append(temp)
#         b.append(temp - n)
#     n = random.randint(-2, 2)
#     for _ in range(2):
#         temp = random.choice(seq2)
#         c.append(temp)
#         c.append(temp - n)
#
#     ans = ((m[6] * m[0] * x ** a[0] * m[1] * y ** b[0] * m[2] * z ** c[0]) / (x ** a[1] * y ** b[1] * z ** c[1])) + (
#             (m[7] * m[3] * x ** a[2] * m[4] * y ** b[2] * m[5] * z ** c[2]) / (x ** a[3] * y ** b[3] * z ** c[3]))
#
#     if int(ans * 1000 % 1000) == 0:
#         ans = int(ans)
#     else:
#         ans = round(ans, 2)
#     for el in a:
#         r.append('{' + str(el) + '}')
#     for el in b:
#         s.append('{' + str(el) + '}')
#     for el in c:
#         q.append('{' + str(el) + '}')
#
#     res = f'{m[6]}' + '\\dfrac{' + f'{m[0]}x^{r[0]}~{m[1]}y^{s[0]}~{m[2]}z^{q[0]}' + '}{' + \
#           f'x^{r[1]}~y^{s[1]}~z^{q[1]}' + '}+' + f'{m[7]}' + '\\dfrac{' + \
#           f'{m[3]}x^{r[2]}~{m[4]}y^{s[2]}~{m[5]}z^{q[2]}' + '}{' + f'x^{r[3]}~y^{s[3]}~z^{q[3]}' + '}'
#
#     cond = '\(\\text{Упростите выражение }' + f'{res}' + '\\text{ и найдите его значение при }' + \
#            f'x = {x}, y = {y}, z = {z}.' + '\)$$\\\\$$ \(\text{ При необходимости округлите ответ до 2 цифр после ' \
#                                            'запятой.' + '}\) '
#
#     if ans not in answers:
#         answers.append(ans)
#         prob = Problem.objects.create(title='Рациональная дробь', condition=cond, answer=ans, theme='rational')
#         answer = Answer.objects.create(answer=ans)


# answers = []
# for _ in range(50):
#     percent = random.randint(3, 95)
#     number = random.randint(100, 2500)
#     res = percent * number / 100
#     ans = int(res)
#     while res != ans:
#         percent = random.randint(3, 95)
#         number = random.randint(100, 2500)
#         res = percent * number / 100
#         ans = int(res)
#
#     cond1 = '\(\\text{Какое число составляет }' + f'{percent}\%' + '\\text{ от }' + f'{number}?' + '\) '
#     cond2 = '\(\\text{Сколько процентов от числа }' + f'{number}' + '\\text{ составляет число }' + f'{ans}?' + \
#             '\) $$\\\\$$ \(\\text{В ответ запишите только число.} \)'
#
#     if ans not in answers:
#         answers.append(ans)
#         prob = Problem.objects.create(title='Процент', condition=cond1, answer=ans, theme='percent')
#         answer = Answer.objects.create(answer=ans)
#         prob = Problem.objects.create(title='Процент', condition=cond2, answer=percent, theme='percent')
#         answer = Answer.objects.create(answer=percent)


# answers = []
# for _ in range(50):
#     powers = [-4, -3, -2, 3, 4, 5, 6]
#     power = random.choice(powers)
#     mantiss = random.randint(100, 1000) / 100
#     if power > 0:
#         number = int(round(mantiss, 2) * math.pow(10, power))
#     else:
#         number = round(round(mantiss, 2) / math.pow(10, 0 - power), 0 - power + 2)
#     ans = round(power + mantiss, 2)
#
#     cond = '\(\\text{Приведтие число }' + f'{number}' + '\\text{ к стандартному виду. }' + '\) ' + \
#            '\(\\text{В ответ запишите сумму мантиссы и порядка.} \)'
#
#     if ans not in answers:
#         answers.append(ans)
#         prob = Problem.objects.create(title='Стандартный ыид числа', condition=cond, answer=ans, theme='standard')
#         answer = Answer.objects.create(answer=ans)


# answers = []
# for _ in range(100):
#     number = random.randint(-10, 10)
#     n = random.randint(-10, 10)
#     m = random.randint(-10, 10)
#     sign = random.choice(['*', ':', '^'])
#     if sign == '*':
#         while 0 > m + n or m + n > 5:
#             n = random.randint(-10, 10)
#             m = random.randint(-10, 10)
#         cond = '\(\\text{Вычислите }' + f'{number}^' + '{' + f'{n}' + '}\cdot' + f'{number}^' + '{' + f'{m}' + '}.' + '\) '
#         ans = number ** (m + n)
#     elif sign == ':':
#         while 0 > m - n or m - n > 5:
#             n = random.randint(-10, 10)
#             m = random.randint(-10, 10)
#         cond = '\(\\text{Вычислите }' + f'{number}^' + '{' + f'{m}' + '}:' + f'{number}^' + '{' + f'{n}' + '}.' + '\) '
#         ans = number ** (m - n)
#     elif sign == '^':
#         while 0 > m * n or m * n > 6:
#             n = random.randint(-6, 6)
#             m = random.randint(-6, 6)
#         cond = '\(\\text{Вычислите }' + f'({number}^' + '{' + f'{n}' + '}' + ')^{^{' + f'{m}' + '}}.\) '
#         ans = number ** (m * n)


# answers = []
# for _ in range(40):
#     # add and mult
#     a = random.randint(-15, 15)
#     while a == 0:
#         a = random.randint(-15, 15)
#     b = round(random.randint(1, 100) / random.randint(1, 100), 2)
#     c = round(random.randint(1, 100) / random.randint(1, 100), 1)
#     d = round(random.randint(1, 50) / random.randint(5, 10), 2)
#     if int(b) == b:
#         b = int(b)
#     if int(c) == c:
#         c = int(c)
#     if int(d) == d:
#         d = int(d)
#     sign1 = random.choice(['+', '-', '*', ':'])
#     sign2 = random.choice(['+', '-', '*', ':'])
#     sign3 = random.choice(['+', '-'])
#     cond = '\(\\text{Вычислите }' + f'{a}{sign1}({b}{sign2}{c}){sign3}{d}.\) ' + \
#            '\(\\text{При необходимости округлите ответ до сотых.}\) '
#     ans = operation(b, c, sign2)
#     ans = operation(a, ans, sign1)
#     ans = operation(ans, d, sign3)
#     ans = round(ans, 2)
#
#     print(cond)
#     print(ans)
#
#     if ans not in answers:
#         answers.append(ans)
#         prob = Problem.objects.create(title='Арифметика', condition=cond, answer=ans, theme='count')
#         answer = Answer.objects.create(answer=ans)


# answers = []
# for _ in range(15):
#     r = round(10 * random.randint(10, 100) / random.randint(1, 100), 1)
#     if r == int(r):
#         r = int(r)
#     area = round(3.14 * math.pow(r, 2), 4)
#     length = round(6.28 * r, 3)
#     cond = '\(\\text{Найдите площадь круга с радиусом }' + f'r = {r}' + \
#            '\\text{ и длину его окружности. В ответ запишите сумму этих двух чисел}.\) '
#     ans = round(area + length, 4)
#
#     print(cond)
#     print(r, area, length, ans)
#
#     if ans not in answers:
#         answers.append(ans)
#         prob = Problem.objects.create(title='Площадь', condition=cond, answer=ans, theme='area')
#         answer = Answer.objects.create(answer=ans)

answers = []
for _ in range(20):
    r = random.randint(1, 12) * 3
    cond = '\(\\text{Найдите объем шара с радиусом }' + f'r = {r}' + '.\) '
    ans = round(4 / 3 * 3.14 * math.pow(r, 3), 2)

    print(cond)
    print(ans)

    if ans not in answers:
        answers.append(ans)
        prob = Problem.objects.create(title='Объем', condition=cond, answer=ans, theme='volume')
        answer = Answer.objects.create(answer=ans)

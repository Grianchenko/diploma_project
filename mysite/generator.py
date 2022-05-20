import random
import math
from topic.models import Problem, Answer


# def operation(m, n, sign):
#     if sign == '+':
#         return n + m
#     elif sign == '-':
#         return m - n
#     elif sign == '*':
#         return m * n
#     elif sign == ':':
#         return m / n
#     elif sign == '^':
#         return m ** n


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

# answers = []
# for _ in range(20):
#     r = random.randint(1, 12) * 3
#     cond = '\(\\text{Найдите объем шара с радиусом }' + f'r = {r}' + '.\) '
#     ans = round(4 / 3 * 3.14 * math.pow(r, 3), 2)
#
#     print(cond)
#     print(ans)
#
#     if ans not in answers:
#         answers.append(ans)
#         prob = Problem.objects.create(title='Объем', condition=cond, answer=ans, theme='volume')
#         answer = Answer.objects.create(answer=ans)


# answers = []
# for _ in range(50):
#     b = random.randint(1, 270)
#     a = random.randint(1, 270)
#
#     while a + b > 360:
#         b = random.randint(1, 270)
#         a = random.randint(1, 270)
#
#     cond = '\(\\text{Найдите сумму углов } \\angle A=' + f'{a}' + '^{\circ},~\\angle B=' + f'{b}' + '^{\circ}.\) '
#     ans = a + b
#
#     print(cond)
#     print(ans)
#
# if ans not in answers:
#     answers.append(ans)
#     prob = Problem.objects.create(title='Угол', condition=cond, answer=ans, theme='angle')
#     answer = Answer.objects.create(answer=ans)


# answers = []
# for _ in range(20):
#     b = random.randint(1, 120)
#     a = random.randint(1, 120)
#     c = a + b
#
#     while c > 155:
#         b = random.randint(1, 120)
#         a = random.randint(1, 120)
#         c = a + b
#
#     cond = '\(\\text{Углы } \\angle C \\text{ и } \\angle D \\text{ накрест лежащие. Найдите угол } \\angle D, \\text{ если } \\angle C = \\angle A + \\angle B, ~\\angle A=' + f'{a}' + '^{\circ},~\\angle B=' + f'{b}' + '^{\circ}.\) '
#     ans = c
#
#     print(cond)
#     print(ans)
#
#     if ans not in answers:
#         answers.append(ans)
#         prob = Problem.objects.create(title='Угол', condition=cond, answer=ans, theme='angle')
#         answer = Answer.objects.create(answer=ans)

#
# answers = []
# for _ in range(20):
#     # b = random.choice([30, 45, 60, 90, 120, 135, 150, 180, 210, 225, 240, 270, 315, 300, 330, 360])
#     # a = b / 180
#     # if b in [30, 150, 210, 330]:
#     #     a = '\\dfrac{' + f'{int(b / 30)}' + '}{6}'
#     # elif b in [60, 120, 240, 300]:
#     #     a = '\\dfrac{' + f'{int(b / 60)}' + '}{3}'
#     # elif b in [45, 135, 225, 315]:
#     #     a = '\\dfrac{' + f'{int(b / 45)}' + '}{4}'
#     # elif b in [90, 270]:
#     #     a = '\\dfrac{' + f'{int(b / 90)}' + '}{2}'
#
#     # cos = 0
#     # if b == 30 or b == 150:
#     #     cos = 0.5
#     # elif b == 45 or b == 135:
#     #     cos = 0.71
#     # elif b == 60 or b == 120:
#     #     cos = 0.87
#     # elif b == 180 or b == 360:
#     #     cos = 0
#     # elif b == 90:
#     #     cos = 1
#     # elif b == 210 or b == 330:
#     #     cos = -0.5
#     # elif b == 225 or b == 315:
#     #     cos = -0.71
#     # elif b == 240 or b == 300:
#     #     cos = -0.87
#     # elif b == 270:
#     #     cos = -1
#
#     xa = random.randint(-10, 10)
#     xb = random.randint(-10, 10)
#     ya = random.randint(-10, 10)
#     yb = random.randint(-10, 10)
#
#     # a = random.randint(2, 20)
#     alpha = random.choice([30, 45, 60, 90, 120, 135, 150, 180, 210, 225, 240, 270, 315, 300, 330, 360])
#     # oss = random.choice(['OX', 'OY'])
#     # if oss == 'OX':
#     #     proec = a * math.cos(alpha / 180 * math.pi)
#     # else:
#     #     proec = a * math.sin(alpha / 180 * math.pi)
#
#     a = random.randint(1, 12)
#     b = random.randint(1, 12)
#
#     cond = '\(\\text{Вычислите скалярное произведение векторов } \\vec{a} \\text{ и } \\vec{b}, \\text{ если } ' \
#            '\\vec{a}=' + f'({xa}, {ya}),~' + '\\vec{b}=' + f'({xb}, {yb})' + '.\)'
#     cond2 = '\(\\text{Вычислите скалярное произведение векторов } \\vec{a} \\text{ и } \\vec{b}, \\text{ если } ' \
#             '|\\vec{a}| =' + f'{a},~' + '|\\vec{b}| =' + f'{b},' + '\\text{ а угол между ними } \\alpha=' + f'{alpha}' \
#             + '^{\circ}.\)' + '\(\\text{Ответ округлите до десятых.} \)'
#
#     ans = xa * xb + ya * yb
#     ans2 = round(a * b * math.cos(alpha / 180 * math.pi), 1)
#
#     print(cond)
#     print(cond2)
#     print(ans)
#     print(ans2)
#
#     if cond not in answers:
#         answers.append(cond)
#         answers.append(cond2)
#         prob = Problem.objects.create(title='Вектор', condition=cond, answer=ans, theme='vector')
#         prob2 = Problem.objects.create(title='Вектор', condition=cond2, answer=ans2, theme='vector')
#         answer = Answer.objects.create(answer=ans)
#         answer2 = Answer.objects.create(answer=ans2)

#
# answers = []
# for _ in range(30):
#
#     x = random.randint(-1000, 1000) / 100
#     y = random.randint(-1000, 1000) / 100
#     a = random.choice([-10, -9, -8, -7, -6, -5, -4, -3, -2, 2, 3, 4, 5, 6, 7, 8, 9, 10])
#     b = random.choice([-10, -9, -8, -7, -6, -5, -4, -3, -2, 2, 3, 4, 5, 6, 7, 8, 9, 10])
#     c = round(a * x + b * y, 2)
#     e = random.choice([-10, -9, -8, -7, -6, -5, -4, -3, -2, 2, 3, 4, 5, 6, 7, 8, 9, 10])
#     d = random.choice([-10, -9, -8, -7, -6, -5, -4, -3, -2, 2, 3, 4, 5, 6, 7, 8, 9, 10])
#     f = round(d * y + e * x, 2)
#
#     if b > 0 and e > 0:
#         cond = '\(\\text{Решите систему уравнений: }\)' + '\\begin{equation*}\\begin{cases}' \
#                                                           f'{a}x+{b}y={c}  \\\\' \
#                                                           f'{d}y+{e}x={f} ' \
#                                                           '\end{cases}\end{equation*}' + \
#                '\(\\text{В ответ запишите сумму корней, округленную до сотых.}\) '
#     elif b > 0 and e < 0:
#         cond = '\(\\text{Решите систему уравнений: }\)' + '\\begin{equation*}\\begin{cases}' \
#                                                           f'{a}x+{b}y={c}  \\\\' \
#                                                           f'{d}y{e}x={f} ' \
#                                                           '\end{cases}\end{equation*}' + \
#                '\(\\text{В ответ запишите сумму корней, округленную до сотых.}\) '
#     elif b < 0 and e > 0:
#         cond = '\(\\text{Решите систему уравнений: }\)' + '\\begin{equation*}\\begin{cases}' \
#                                                           f'{a}x{b}y={c}  \\\\' \
#                                                           f'{d}y+{e}x={f} ' \
#                                                           '\end{cases}\end{equation*}' + \
#                '\(\\text{В ответ запишите сумму корней, округленную до сотых.}\) '
#     else:
#         cond = '\(\\text{Решите систему уравнений: }\)' + '\\begin{equation*}\\begin{cases}' \
#                                                           f'{a}x{b}y={c}  \\\\' \
#                                                           f'{d}y{e}x={f} ' \
#                                                           '\end{cases}\end{equation*}' + \
#                '\(\\text{В ответ запишите сумму корней, округленную до сотых.}\) '
#
#     ans = round(x + y, 2)
#     # ans2 = round((a * b - d) / c, 2)
#
#     print(cond)
#     # print(cond2)
#     print(x, y, ans)
#     # print(ans2)
#
#     if ans not in answers:
#         answers.append(ans)
#         prob = Problem.objects.create(title='Уравнения', condition=cond, answer=ans, theme='equation')
#         answer = Answer.objects.create(answer=ans)


# answers = []
# for _ in range(30):
#
#     x = random.randint(-1000, 1000) / 100
#     k = random.randint(2, 10)
#     a = random.randint(1, 20)
#     b = random.choice([-10, -9, -8, -7, -6, -5, -4, -3, -2, 2, 3, 4, 5, 6, 7, 8, 9, 10])
#     c = round(k * abs(x - a) + b, 2)
#     x1 = round((c - b) / k + a, 2)
#     x2 = round(- ((c - b) / k - a), 2)
#
#     if b > 0:
#         cond = '\(\\text{Решите уравнение: }' + f'{k}\cdot|x-{a}|+{b}={c}\)' + \
#                '\(\\text{В ответ запишите сумму корней, округленную до сотых.}\) '
#     else:
#         cond = '\(\\text{Решите уравнение: }' + f'{k}\cdot|x-{a}|{b}={c}\)' + \
#                '\(\\text{В ответ запишите сумму корней, округленную до сотых.}\) '
#
#     ans = x
#     # ans2 = round((a * b - d) / c, 2)
#
#     print(cond)
#     # print(cond2)
#     print(ans, x1, x2)
#
#     if ans not in answers:
#         answers.append(ans)
#         prob = Problem.objects.create(title='Уравнения', condition=cond, answer=ans, theme='equation')
#         answer = Answer.objects.create(answer=ans)


# answers = []
# for _ in range(30):
#
#     xa, xb = random.randint(-1000, 1000) / 100, random.randint(-1000, 1000) / 100
#     xc = random.randint(-1000, 1000) / 100
#     k = random.randint(-10, 10)
#     b = random.randint(-20, 20)
#     while k == 0 or b == 0:
#         k = random.randint(-10, 10)
#         b = random.randint(-20, 20)
#     ya = round(k * xa + b, 2)
#     yb = round(k * xb + b, 2)
#     yc = round(k * xc + b, 2)
#
#     choice = random.choice([True, False])
#     if choice:
#         cond = '\(\\text{Точки } ' + f'A({xa};{ya}),~B({xb};{yb})' + '\\text{ и }' + f'C({xc};y)' + \
#                '\\text{ принадлежат одному графику линейной функции}.\)' + \
#                '\(\\text{Найдите } y.\\text{ Ответ округлите до сотых.}\) '
#         ans = yc
#     else:
#         cond = '\(\\text{Точки } ' + f'A({xa};{ya}),~B({xb};{yb})' + '\\text{ и }' + f'C(x;{yc})' + \
#                '\\text{ принадлежат одному графику линейной функции}.\)' + \
#                '\(\\text{Найдите } x.\\text{ Ответ округлите до сотых.}\) '
#         ans = xc
#
#     choice2 = random.choice([True, False])
#     if choice2:
#         cond2 = '\(\\text{Точки } ' + f'A({xa},{ya})' + '\\text{ и }' + f'B({xb},{yb})' + \
#                '\\text{ принадлежат одному графику линейной функции}.\)' + \
#                '\(\\text{Найдите коэффициент при аргументе}.\\text{ Ответ округлите до сотых.}\) '
#         ans2 = k
#     else:
#         cond2 = '\(\\text{Точки } ' + f'A({xa},{ya})' + '\\text{ и }' + f'B({xb},{yb})' + \
#                '\\text{ принадлежат одному графику линейной функции}.\)' + \
#                '\(\\text{Найдите свободный член}.\\text{ Ответ округлите до сотых.}\) '
#         ans2 = b
#
#     print(cond)
#     print(ans)
#     print(cond2)
#     print(ans2)
#
#     if ans not in answers:
#         answers.append(ans)
#         prob = Problem.objects.create(title='Функция', condition=cond, answer=round(ans, 2), theme='function')
#         answer = Answer.objects.create(answer=ans)
#
#     if cond2 not in answers:
#         answers.append(cond2)
#         prob2 = Problem.objects.create(title='Функция', condition=cond2, answer=ans2, theme='function')
#         answer2 = Answer.objects.create(answer=ans2)


# answers = []
# for _ in range(30):
#
#     xa = random.randint(-20, 20)
#     while xa == 0:
#         xa = random.randint(-20, 20)
#     temp = random.choice([-5, -4, -3, -2, -1, 2, 3, 4, 5, 6])
#     temp2 = random.choice([-5, -4, -2, -1, 2, 4, 5])
#     while temp2 == temp:
#         temp2 = random.choice([-5, -4, -2, -1, 2, 4, 5])
#     xb = xa * temp
#     xc = xa * temp2
#     yb = random.randint(-20, 20)
#     b = random.randint(-20, 20)
#     while yb == b:
#         b = random.randint(-20, 20)
#
#     k = (yb - b) * xb
#     ya = int(k / xa + b)
#     yc = k / xc + b
#     if yc == int(yc):
#         yc = int(yc)
#
#     choice = random.choice([True, False])
#     if choice:
#         cond = '\(\\text{Точки } ' + f'A({xa};{ya}),~B({xb};{yb})' + '\\text{ и }' + f'C({xc};y)' + \
#                '\\text{ принадлежат одному графику обратной пропорциональности, }\) ' \
#                '\(\\text{заданной уравнением } y=\\dfrac{k}{x}+b.~\)' + \
#                '\(\\text{Найдите } y.\) '
#         ans = yc
#     else:
#         cond = '\(\\text{Точки } ' + f'A({xa};{ya}),~B({xb};{yb})' + '\\text{ и }' + f'C(x;{yc})' + \
#                '\\text{ принадлежат одному графику обратной пропорциональности, }\) ' \
#                '\(\\text{заданной уравнением } y=\\dfrac{k}{x}+b.~\)' + \
#                '\(\\text{Найдите } x.\) '
#         ans = xc
#
#     choice2 = random.choice([True, False])
#     if choice2:
#         cond2 = '\(\\text{Точки } ' + f'A({xa},{ya})' + '\\text{ и }' + f'B({xb},{yb})' + \
#                '\\text{ принадлежат одному графику обратной пропорциональности, }\) ' \
#                '\(\\text{заданной уравнением } y=\\dfrac{k}{x}+b.~\)' + \
#                '\(\\text{Найдите коэффициент } k.\) '
#         ans2 = k
#     else:
#         cond2 = '\(\\text{Точки } ' + f'A({xa},{ya})' + '\\text{ и }' + f'B({xb},{yb})' + \
#                '\\text{ принадлежат одному графику обратной пропорциональности, }\) ' \
#                '\(\\text{заданной уравнением } y=\\dfrac{k}{x}+b.~\)' + \
#                '\(\\text{Найдите свободный член}.\) '
#         ans2 = b
#
#     print(cond)
#     print(ans)
#     print(cond2)
#     print(ans2)
#
#     if ans not in answers:
#         answers.append(ans)
#         prob = Problem.objects.create(title='Функция', condition=cond, answer=round(ans, 2), theme='function')
#         answer = Answer.objects.create(answer=ans)
#
#     if cond2 not in answers:
#         answers.append(cond2)
#         prob2 = Problem.objects.create(title='Функция', condition=cond2, answer=ans2, theme='function')
#         answer2 = Answer.objects.create(answer=ans2)


# answers = []
# for _ in range(30):
#
#     xa, xb, xc, xd = random.randint(-10, 10), random.randint(-10, 10), random.randint(-10, 10), random.randint(-10, 10)
#     a = random.randint(-5, 5)
#     b = random.randint(-20, 20)
#     c = random.randint(-100, 100)
#     while a == 0:
#         a = random.randint(-5, 5)
#
#     ya, yb, yc = a * xa ** 2 + b * xa + c, a * xb ** 2 + b * xb + c, a * xc ** 2 + b * xc + c
#     yd = a * xd ** 2 + b * xd + c
#
#     choice = random.choice([True, False])
#     if choice:
#         cond = '\(\\text{Точки } ' + f'A({xa}; {ya}),~B({xb}; {yb}),~C({xc}; {yc})' + '\\text{ и }' + f'D(x;{yd})' + \
#                '\\text{ принадлежат одному графику квадратичной функции}.~\)' + \
#                '\(\\text{Найдите } x.\) '
#         ans = xd
#     else:
#         cond = '\(\\text{Точки } ' + f'A({xa};{ya}),~B({xb}; {yb}),~C({xc}; {yc})' + '\\text{ и }' + f'D({xd};y)' + \
#                '\\text{ принадлежат одному графику квадратичной функции}.~\)' + \
#                '\(\\text{Найдите } y.\) '
#         ans = yd
#
#     cond2 = '\(\\text{Точки } ' + f'A({xa};{ya}),~B({xb}; {yb})' + '\\text{ и }' + f'C({xc};{yc})' + \
#             '\\text{ принадлежат одному графику квадратичной функции}.~\)' + \
#             '\(\\text{Найдите ординату вершины параболы. Ответ округлите до сотых}.\) '
#     ans2 = round(c - (b ** 2 / 2 / a), 2)
#
#     print(cond)
#     print(ans)
#     print(cond2)
#     print(ans2)
#
#     if ans not in answers:
#         answers.append(ans)
#         prob = Problem.objects.create(title='Функция', condition=cond, answer=round(ans, 2), theme='function')
#         answer = Answer.objects.create(answer=ans)
#
#     if cond2 not in answers:
#         answers.append(cond2)
#         prob2 = Problem.objects.create(title='Функция', condition=cond2, answer=ans2, theme='function')
#         answer2 = Answer.objects.create(answer=ans2)


# answers = []
# for _ in range(30):
#
#     k = random.randint(-10, 10)
#     b = random.randint(1, 10)
#     while k == 0:
#         k = random.randint(-10, 10)
#
#     choice = random.choice([-6, -5, -4, -3, -2, -1, 2, 3, 4, 5, 6])
#     x = choice * math.pi / 2
#     ourX = choice / 2 * 3.14
#     func = random.choice(['cos', 'sin'])
#     if func == 'cos':
#         y = k * math.cos(x) + b
#     else:
#         y = k * math.sin(x) + b
#
#     ourX = round(ourX, 2)
#     y = int(y)
#
#     if func == 'cos':
#         cond = '\(\\text{Точка } ' + f'A({ourX};y)' + '\\text{ принадлежат графику функции }' + \
#                f'y={k}\cdot\cos(x)+{b}.\)' + \
#            '\(\\text{Найдите }y.~\\text{Считайте, что }\pi=3.14. \\text{ Ответ округлите до целых.}\) '
#         ans = y
#     else:
#         cond = '\(\\text{Точка } ' + f'A({ourX};y)' + '\\text{ принадлежат графику функции }' + \
#                f'y={k}\cdot\sin(x)+{b}.\)' + \
#            '\(\\text{Найдите }x.~\\text{Считайте, что }\pi=3.14. \\text{ Ответ округлите до целых.}\) '
#         ans = y
#
#     print(cond)
#     print(ans)
#
#     if ans not in answers:
#         answers.append(ans)
#         prob = Problem.objects.create(title='Функция', condition=cond, answer=round(ans, 2), theme='function')
#         answer = Answer.objects.create(answer=ans)

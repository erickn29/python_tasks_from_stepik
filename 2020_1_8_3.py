'''
Катя узнала, что ей для сна надо XX минут. В отличие от Коли, Катя ложится спать после полуночи в HH часов
и MM минут. Помогите Кате определить, на какое время ей поставить будильник, чтобы он прозвенел ровно
через XX минут после того, как она ляжет спать.

На стандартный ввод, каждое в своей строке, подаются значения XX, HH и MM. Гарантируется,
что Катя должна проснуться в тот же день, что и заснуть. Программа должна выводить время,
на которое нужно поставить будильник: в первой строке часы, во второй — минуты.
'''

t = int(input()) #time
h = int(input()) #hours
m = int(input()) #mins
hm = h*60 + m #часы в минуты
s = hm + t #общее время
hours = s // 60
minutes = s % 60
print(hours)
print(minutes)
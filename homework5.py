#котреж-неизменяемый список
immutable_var= 1,'Роман',['green','green','blue'], False
print(immutable_var)
immutable_var[2][0] = 'red' #можем изменить данные только в одном элементе кортежа - внутри списка.
# Остальные элементы неизменны - в этом суть котрежа
print(immutable_var)

#изменяемый список
multable_list = ['Воскреснье','Вторник','Среда']
print(multable_list)
multable_list.append('Четверг')  #добавили элемент в конец
print(multable_list)
multable_list.extend(['Пятница','Суббота',14,'Воскресенье']) #добавили 4 элемента в конец
print(multable_list)
multable_list.remove(14) #удалили элемент 14
multable_list[0]='Понедельник' #заменили элемент Воскресенье на Понедельник
print(multable_list)
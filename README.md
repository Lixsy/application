## Описание:
Для проверки вашего уровня знаний, предлагается решить следующее задание.
Как только вы перенесете файлы проекта на свой локальный репозиторий и запустите его
на локальном сервере Flask, вы увидите одну html страничку содержащую форму.
Необходимо заполнить эту форму и сохранить введенную информацию в БД  по клику на кнопку 
"Сохранить". 
Для этого необходимо использовать следующие вещи и придерживаться ограничений:  
1) SQLalchemy
2) Flask + Python 3.9
3) любой фраймворк JS или сам ванильный JS (Обязательно используйте, даже если вам кажется, что тут можно обойтись без него)
4) работать необходимо в созданной виртуальной среде, если что-то необходимо доустановить
устанавливаете, все зависимости по завершению работы сохранить в файл "pipList.txt".
5) пароли ни в коем случае нельзя пушить в репозиторий
6) русские буквы в базу не вставлять

Желательно придумать универсальный способ соединения с базой. В частности можно использовать декораторы
или ООП. 

БД включает в себя две таблицы:

Первая таблица поля: user_id, name, middle_name, bornDate, gender
Вторая таблица поля: user_id, education, comment, citizenship
Первая и вторая таблица должны быть связаны
Логин и пароль от БД, будет выслан вам на почту.
При работе с базой вы должны создать отдельную данных

 

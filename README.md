# <p align="center"> ![image](https://github.com/HunterBjj/rait_scan_birds/assets/64096687/2e616eee-d915-4dca-bef9-c51a0db2bfde) </p>
# Тестовое задание компании РайтСкан


Для запуска приложение необходимо:
- git clone https://github.com/HunterBjj/rait_scan_birds;
- провеcти миграции python manage.py makemigrations, python manage.py migrate;
- запустить локальный сервер python manage.py runserver.

  Приложение состоит из пяти html страниц:
  ![image](https://github.com/HunterBjj/rait_scan_birds/assets/64096687/91718111-901c-41ab-ad04-a3f0b0d8f28a)
   <p align="center"> Рисунок 1 - Авторизация </p>
   
  ![image](https://github.com/HunterBjj/rait_scan_birds/assets/64096687/6d0997ff-8cce-4ac3-b6f5-1e95d3589711)
    <p align="center"> Рисунок 2 - Регистрация </p>
    
  ![image](https://github.com/HunterBjj/rait_scan_birds/assets/64096687/3ad58ada-8f93-4749-b67f-abb7c177be63)
    <p align="center"> Рисунок 3 - Просмотр птиц </p>
  
  ![image](https://github.com/HunterBjj/rait_scan_birds/assets/64096687/2c4e3478-68e8-409c-a5eb-a0b69f357294)
    <p align="center"> Рисунок 4 - Регистрация птицы </p>

  ![image](https://github.com/HunterBjj/rait_scan_birds/assets/64096687/a0aa5852-1c14-49e2-8f5a-05910f8dc3c3)
    <p align="center"> Рисунок 5 - Просмотренны птицы (избранные) </p>

      База данных SQLlite состоит из трех таблиц:
    - User (пользователи);
    - Birds (птицы);
    - ViwedUser (избранные птицы - они же просмотренные).

      
    <p align="center"> Заключение </p>
    
>  Данное приложене хорошо подойдёт для орнитологов, если использовать его для большого количества пользователей, которые будут одновременно работать с БД, тогда необходимо выбрать иную подходящую для этого СУБД. Благодаря выполненому тестовому заданию были сформированны навыки работы с фреймворком Django, это очень хороший фреймворк со своими тонкостями и подводными камнями, аналог ralavel на PHP, имеет ряд преимущест, достаточно понятен и прост, но были и проблемы с SQL с сырыми запросами, если обращатья к первичному ключу, то необходимо добавлять к полю данную строку "_id", также необходимо добавлять перед именами таблицы имя приложение и разделять их нижним подчеркиванием. 

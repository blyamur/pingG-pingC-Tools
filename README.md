# pingG-pingC
Python script for ping remote resources through the list every with a check interval (with and without color labels)
> Скрипт на Python для пинга удаленных ресурсов по списку, с заданным интервалом проверки (с цветными метками и без них)

### Description
> Описание

This script is written using the python 3 language. Its main task is to check the availability of remote resources, according to a prepared list, with a given check interval. When the script is launched, the resources from the back list are pinged, and based on the response time results, the availability status is generated. Ping repeats through the list at a specified time interval. If there is no connection, it is written to a text log file (in the case of a Windows system, there is also a sound notification).

> Данный скрипт написан с использованием языка python 3. Основаная его задача проверка доступности удаленных ресурсам, по подготовленному списку, с заданным  интервалом проверки. При запуске скрипта, ресурсы из заднного списка, пингуются, а по результатам времени ответа, формируется статус доступности. Пинг повторяется по списку через заданный интервал времени. При отсутствии подключения, производится запись в текстовый log файл ( в случае системы виндовс еще и звуковое оповещение).

### Settings
> Настройки

In the script, you can manually set the parameters:
```
sleep_interval = 30  # (In seconds) Check Interval
source = {'8.8.8.8': 'Google',  #list of addresses and names. For example 'IP or domain': 'Source name',
           'yandex.ru': 'ya.ru'}
```
>В скрипте можно вручную задать следующие параметры:
```
sleep_interval = 30  # (В секундах) Интервал проверки
source = {'8.8.8.8': 'Google',  #список в виде "адрес и название". Для примера 'IP адресили домен': 'Название ресурса',
           'yandex.ru': 'ya.ru'}
```


![pingG-pingC](https://github.com/blyamur/pingG-pingC/blob/master/images/icon.jpg)

### Copyrights and Licenses
Not for commercial use.

2020  [Mons](https://blog.mons.ws)


### Did you find this useful?!
> Вы нашли это  полезным ?!

Happy to hear that :) *If You want to help me, you can support me on [PayPal](https://paypal.me/enkonu)*

> Рад это слышать :) Если вы хотите мне помочь, вы можете поддержать меня материально


*Thanks for reading :heart_eyes_cat:*
> Спасибо за чтение!

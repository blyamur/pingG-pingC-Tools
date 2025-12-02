# pingC
Python script for ping remote resources through the list every with a check interval (with and without color labels)
> Скрипт на Python для пинга удаленных ресурсов по списку, с заданным интервалом проверки (с цветными метками и без них)

### Description | Описание

This script is written using the python 3 language. Its main task is to check the availability of remote resources, according to a prepared list, with a given check interval. When the script is launched, the resources from the back list are pinged, and based on the response time results, the availability status is generated. Ping repeats through the list at a specified time interval. If there is no connection, it is written to a text log file (in the case of a Windows system, there is also a sound notification).

> Данный скрипт написан с использованием языка python 3. Основная его задача проверка доступности удаленных ресурсам, по подготовленному списку, с заданным  интервалом проверки. При запуске скрипта, ресурсы из заднного списка, пингуются, а по результатам времени ответа, формируется статус доступности. Пинг повторяется по списку через заданный интервал времени. При отсутствии подключения, производится запись в текстовый log файл ( в случае системы виндовс еще и звуковое оповещение).

pingC.py - color-coded variant (requires module [colorama](https://github.com/tartley/colorama))

[![pingC](https://raw.githubusercontent.com/blyamur/pingG-pingC-Tools/refs/heads/master/images/pingc.jpg)](https://github.com/blyamur/pingG-pingC)

> pingC.py - вариант с цветными метками (необходим модуль [colorama](https://github.com/tartley/colorama))

-----

Fill in the list of checked resources, it can be both sites and computers and servers in your local network. Set the check interval. After that, simply run the script with administrator rights (in windows, CMD.exe must be run as administrator) this is due to the peculiarity of the operation of the services that do the ping. During the scan, the scan results will be displayed in the console.
> Заполняете список проверяемых ресурсов, это могут быть как сайты, так и компьютеры и серверы в вашей локальной сети. Задаете интервал проверки. После чего просто запускаете скрипт с правами администратора (в системе windows, CMD.exe должна быть запущена от имени администратора) это связанно с особенностью работы служб, которые делают пинг. В ходе проверки в консоли будут выводиться результаты проверки. 

### Start | Запуск 

Before starting the script for the first time, you need to install the following modules for Python:
> Перед первым запуском скрипта, необходимо установить следующие модули для Python:

[pythonping](https://github.com/alessandromaggio/pythonping) (pip install pythonping)

datetime (pip install datetime)

time (pip install time)

os (pip install os)

pyautogui (pip install PyAutoGUI)

[colorama](https://github.com/tartley/colorama) (pip install colorama)  

### Settings | Настройки

In the script, you can manually set the parameters:
```
sleep_interval = 30  # (In seconds)
```
> В скрипте можно вручную задать следующие параметры:
```
sleep_interval = 30  # (В секундах) Интервал проверки
```

Настройки хостов доступность которых будет прверяться хранится в файле settings.xml в формате:
```
ya.ru: ya.ru №
```
IP or domain|IP или домен: 'Source name|Имя источника'



The general process is simple and is performed only once if the list of verified resources does not change
> Общий процесс прост и выполняется только один раз, если список проверяемых ресурсов не изменяется

1. Download the script. | Скачиваете скрипт.
2. Install the required modules. | Устанавливаете необходимые модули.
3. Fill out the address list. | Заполняете список адресов.
4. Run the script. | Запускаете скрипт. 


This script does not claim to be original or correct. It is provided as is, the main thing is that it completely allows you to solve the tasks.
> Данный скрипт не претендует на оригинальность и правильность. Предоставляется как есть, главное он вполне позволяет решать поставленные задачи.

### Copyrights and Licenses
Not for commercial use.


### Did you find this useful?! | Вы нашли это  полезным ?!

Happy to hear that :) *If You want to help me, you can buy me a cup of coffee :coffee: ( [yoomoney](https://yoomoney.ru/to/41001158104834) or [ko-fi](https://ko-fi.com/monseg), [boosty.to](https://boosty.to/monseg) )* 

> Рад это слышать :) Если вы хотите мне помочь, вы можете угостить меня чашечкой кофе 

*Thanks for reading :heart_eyes_cat:*
> Спасибо за чтение!


© 2022

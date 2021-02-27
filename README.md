# Factory

Проект представляет собой две программы и базу данных.

Предназначение: Использование на производстве. Конкретно в данном случае это цех листового металла (есть возможность апдейта до любого производства).
Пример продукции: металлические шкафы для электронники, корпуса оборудования, кронштейны, полки etc.

Смысл заключается в следующем. На рабочем месте устанваливается либо комп, либо сенсорный терминал (считай тотже ПК только с сенсорным экраном и всё в одном корпусе).

#### Система выглядит следующим образом: 

1.  Разрабатывается специальное программное обеспечение ввода данных, фиксирующее время работы и время простоев; 
2.  Это программное обеспечение внедряется на каждое рабочее место; 
3.  Рабочие обязаны фиксировать время работы и время простоев с помощью этой программы; 
4.  Создаётся база данных, хранящая данные о времени; 
5.  Разрабатывается специально программное обеспечение, позволяющее считывать данные с сервера и предоставлять их в удобном виде руководству предприятия.

#### Первая программа

При включении программа находится в ждущем режиме, все кнопки заблокированы, кроме кнопки начала смены.
По нажатии на кнопку начала смены начинается отсчёт смены и появляется возможность взаимодействовать со всеми остальными кнопками, обозначающими причины простоев.
По нажатии на одну из таких кнопок появляется ещё один параллельный счётчик.
Все остальные кнопки при этом становятся неактивными, при повторном нажатии на эту кнопку произойдёт остановка этого отсчёта.
При нажатии на кнопку завершения смены основной отсчёт останавливается, и программа переходит в ждущий режим.
Также при каждом нажатии на любую кнопку, несмотря на её основное действие по включении отсчёта, происходит отправка данных в БД.




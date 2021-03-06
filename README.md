# Генератор текстов для задания по курсу АНД

## Условие
Изначальное условие было следующим:

Написать программу - "сочинитель" текста заданного вида. Требуется изменить заданный текст по определенным правилам:
Из текста выбираются фразы, соответствующие заданному виду, стилю (длина, части речи, длина слов и т.п.).
В каждой фразе несколько слов заменяются на более подходящие (формально, по стилю, например, на более длинные). Слова берутся из неиспользованных фраз текста, ставятся в нужной форме. Должно четко выполняться соответствие по морфологическим характеристикам (понятно, 
что семантически может быть бессмыслица, но грамматически текст должен быть верным).
Можно то же безобразие проделать с разными текстами: некоторые слова одного текста заменить на слова из другого. Пример "Петя рисует дом" - "Интеграл усиливает простуду".
Отчет:  краткое описание возможностей и особенностей реализованной программы, программа с комментариями, проведенные тесты.

Потом выяснилось, что я немного неумный и неверно прочитал задание и сделал просто генератор текстов на основе словарей. Так что условие того задания, что было сделано, можно сформулировать вот так:

Написать программу - "сочинитель" текста заданного вида. Требуется изменить заданный текст в соответствии с заданным стилем. Должно четко выполняться соответствие по морфологическим характеристикам (понятно, что семантически может быть бессмыслица, но грамматически текст должен быть верным).
Отчет:  краткое описание возможностей и особенностей реализованной программы, программа с комментариями, проведенные тесты.

## Что внутри этих странных папок?

Внутри папки `dict` находятся пять словарей. Внутри папки `text` находятся тексты. Про остальное написано в следующем абзаце.

## Алгоритм

В файле `format.py` есть код, которым я приводил словари в удобный для меня вид. Фактически, я открывал файл, токенизировал слова, клал в `set` начальные формы токенезированных слов и записывал получившееся в нужные файлы. Программа чисто служебная, но если есть интерес, то я её приложил.
В файле `dict_reader.py` есть класс `Dict_reader`, в котором есть три метода и конструктор. Методы - `get_name()`, `get_word()`, `get_simple()`, `get_standart()` и `get_hard()`, которые возвращают списки из N слов, где N задаётся параметрами.
В файле `text_gen.py` находится, собственно, генератор текста. Первым делом, мы создаём пустой `dict`, куда мы будем записывать словарь перевода из нормального русского языка в тот, который получается после наших извращений. Мы берём первое слово из введённого текста, оно приводится в начальную форму, его теги сохраняются в буфер. Затем мы проверяем, есть ли слово в нашем словаре. Если есть, оно заменяется, если нет, то в цикле из словаря достаются слова до тех пор, как мы не достанем слово, которое совпадает по неизменяемым признакам со словом из текста. Мы записываем в `dict` начальные формы нашего слова из текста и слова, полученного из словаря в формате `{ "text_word" : "dict_word" }`, заменяем в тексте изначальное слово на склонённое в нужную форму слово из словаря и идём дальше. 
В файле `demo.py` находится демо программы. Запускайте и радуйтесь.

## Инструкция по установке:

Программа теоретически должна работать и на Windows, и на Linux, и на MacOS, но реально на Windows питон работает слишком медленно. При сравнении на моём железе (Intel Core i5-8250U, 16 GB ОЗУ) один и тот же текст в Linux сгенерировался где-то за 1 секундe, на MacOS - столько же, на Windows - через полчаса мне надоело ждать. Есть вероятность, что это какие то локальные виндовские приколы с питоном, но мне, если честно, не очень интересно разбираться. Я пишу под линуксом, так что проще сказать, что под виндой оно не работает.

Сначала просто в терминале (заменить pip на pip3 в случае MacOS):
```
pip install nltk --user
pip install pymorphy2 --user
```
Затем в питоновской командной строке:
```
import nltk
nltk.download('stopwords')
nltk.download('punkt')
```

Для запуска необходимо запустить файл `demo.py` и следовать указаниям на экране.

Важно: стихотворение - это такая задачка на подумать для программы. Пережёвывать оно его может достаточно долго, так что если ничего не происходит - сходите, налейте себе чаю.

## Результаты работы программы

```
Input: Если любишь – люби, но не лги. Если веришь – то верь, но всегда. Ненавидишь – скажи, но напрямую. А если смеёшься – то смейся в глаза. 
Output: Если лепишь – лепи, но не вырабатывай. Если картавишь – то картавь, но всегда. Стыкуешь – растрепли, но всухую. А если прелюбодействуешь – то прелюбодействуй в глаза.
```

Остальное можете попробовать сами с помощью запуска `demo.py`.

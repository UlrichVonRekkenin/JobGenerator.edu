JobGenerator.edu
================

Генератор заданий для изучающих иностранный язык.


Зависимости:  
1. python (https://www.python.org/downloads/);  
2. PyQt4 (http://www.lfd.uci.edu/~gohlke/pythonlibs/#pyqt).


HOWTO:

1. "Расположить буквы в словах в случайном порядке".  
Каждое слово (словосочетание) на отдельной строке.  
Пример:  

sometimes  
summertime

Variant #1  
Place the letters on correct order.  
NAME:  
CLASS:  
1) mumimtsere  
2) omesimtes  


================================================================================


2. "Зменить часть букв нижним подчеркиванием".  
Каждое слово (словосочетание) на отдельной строке.  
Параметр: "Часть пропущенных букв, %" указывает какую часть необходимо заменить символом "_".
Пример:  

sometimes  
summertime  

Variant #1  
Insert the correct letters.  
NAME:  
CLASS:  
1)  __ um __  __  __ t __ me  
2) s __ met __  __ e __  


================================================================================


3. "Пропустить определенные буквы в слове".  
Каждое слово (словосочетание) на отдельной строке.  
Параметр: "Пропустить эти буквы" указывает какие буквы будут заменены символом "_".

Пример:  
sometimes  
summertime  

Variant #1  
Insert correct letters: "u, m"  
NAME:  
CLASS:  
1) s _ _ _ e r t i _ e  
2) s o _ e t i _ e s  


================================================================================


4. "Сопоставить слова".  
Каждая пара, разделенная знаком ":" на отдельной строке.  
Примечание: для достижения лучшей рандомизации рекомендуется
использовать более 3-х пар выражений.  

Пример:  
sometimes:иногда  
summertime:летний сезон  
anybody:кто бы то ни было, кто-нибудь  

Variant #1  
Match the words.  
NAME:  
CLASS:  
1) anybody	  	1) кто бы то ни было, кто-нибудь  
2) summertime		2) летний сезон  
3) sometimes		3) иногда  


================================================================================


5. "Расположить слова в предложении в случайном порядке".  
В каждом предложении, заканчивающемся знаками ".!?",  
слова ставятся в случайном порядке.  
Все слова приводятся к нижнему регистру.  

Пример:  
This is the 1st sentence! And another one.  

Variant #1  
Place the words in sentences on correct order.  
NAME:  
CLASS:  
1) the 1st is this sentence!  
2) another one  and.  


================================================================================


6. "Расположить предложения в случайном порядке".  
Все предложения, оканчивающееся знаками ".!?",  
ставятся в случайном порядке.  

Пример:  
This is the 1st sentence! And another one. Is it the 3rd sentence?

Variant #1  
Place the sentences on correct order.  
NAME:  
CLASS:  
1)  Is it the 3rd sentence?  
2)  And another one.  
3) This is the 1st sentence!  


================================================================================


7. "Выбрать глаголы из списка".  
В каждом предложении, ничинающемся с новой строки,  
сдучайно выбирается один из элементов  
в двойных кавычках, разделенных обратной косой чертой "/".  
Примечание: признаком глагола является наличие частицы "to /not to "  
(обязательно с пробелом после "to").  
Глаголы заменяются на нижнее подчеркивание, в скобках рядом указывается форма  
глагола в инфинитиве.  
Все остальные слова (такие как: местоимения, существительные, признаки времени...)  
выбираются из множества в двойных кавычках, разделенных симолом обратной косой черты "/"  
и вставляются в преложение как есть.  

Пример:  
"I/He/She/We" "to walk/not to go/to sleep" "yesterday/today/tomorrow/never" there.  
"I/He/She/We" "to walk/not to go/to sleep" "yesterday/today/tomorrow/never" there.  
"I/He/She/We" "to walk/not to go/to sleep" "yesterday/today/tomorrow/never" there.  
"I/He/She/We" "to walk/not to go/to sleep" "yesterday/today/tomorrow/never" there.  
"to go/not to walk" "you/she" with me "yesterday/tomorrow" to the "zoo/circus"?  
"to go/not to walk" "you/she" with me "yesterday/tomorrow" to the "zoo/circus"?  

Variant #1  
Write the correct form of the verbs in bracket.  
NAME:  
CLASS:  
1) She ____________________ (to walk) tomorrow there.  
2) I ____________________ (to walk) tomorrow there.  
3) We ____________________ (not to go) never there.  
4) She ____________________ (to walk) tomorrow there.  
5) ____________________ (not to walk) she with me yesterday to the circus?  
6) ____________________ (to go) you with me yesterday to the zoo?  


================================================================================


8. "Пропустить слова в предложении".  
Заменяет все слова, указанные в параметре "Пропусить слова" (регистронезависимо),  
на нижнее подчеркивание.  
Примечание: возвращает только один вариант.  

Пример:  
Omit this and that words.  
NAME:  
CLASS:  
Insert correct words: This,  that  

Omit _______________ and _______________ words.  

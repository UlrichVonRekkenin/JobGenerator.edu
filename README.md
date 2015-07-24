# HOWTO:

## **Расположить буквы в словах в случайном порядке**
Каждое слово (словосочетание) на отдельной строке. Порядок слов/словосочетаний для каждого варианта случаен.  
Пример:

| Исходный текст               | Задание     |
| :-------------               | :------------- |
| 1. some word and another one | Variant #n+1 |
| 2. sometimes                 | Place the letters on correct order. |
| 3. summertime                | NAME:
|                              | CLASS:|
|                              | 1) emrmetuism|
|                              | 2) ostiseemm|
|                              | 3) omes wodr dan nhaerto eno|

## **Заменить часть букв нижним подчеркиванием**
Каждое слово (словосочетание) на отдельной строке. Параметр: "*Часть пропущенных букв, %*" указывает какую часть необходимо заменить символом "*_*". Порядок слов/словосочетаний для каждого варианта случаен.  
Пример:

| Исходный текст               | Задание     |
| :-------------               | :------------- |
| 1. some word and another one | Variant #n+1 |
| 2. sometimes                 | Insert the correct letters. |
| 3. summertime                | NAME:
|                              | CLASS:|
|                              | 1) \_\_ \_\_ met \_\_ mes |
|                              | 2) so \_\_ e \_\_ ord a \_\_ d \_\_ \_\_ other o \_\_ e |
|                              | 3) su \_\_ me \_\_ t \_\_ me |


## **Пропустить определенные буквы в слове**
Каждое слово (словосочетание) на отдельной строке. Параметр: "*Пропустить эти буквы*" указывает какие буквы будут заменены символом "*_*". Порядок слов/словосочетаний для каждого варианта случаен.  
Пример:

| Исходный текст               | Задание     |
| :-------------               | :------------- |
| 1. some word and another one | Variant #n+1 |
| 2. sometimes                 | Insert correct letters: "u, m" |
| 3. summertime                | NAME:
|                              | CLASS:|
|                              | 1) s \_ m \_ \_ i m \_ s |
|                              | 2) s \_ m \_ w \_ r d a n d a n \_ \_ \_ \_ r \_ n \_ |
|                              | 3) s u m m \_ r \_ i m \_ |


## **Сопоставить слова**
Каждая пара, разделенная знаком "`:`" на отдельной строке. Примечание: для достижения лучшей рандомизации рекомендуется использовать более 3-х пар выражений.  
Пример:

| Исходный текст                           | Задание     |
| :-------------                           | :------------- |
| 1. sometimes:иногда                      | Variant #n+1 |
| 2. summertime:летний сезон               | Match the words. |
| 3. anybody:кто бы то ни было, кто-нибудь | NAME:
|                                          | CLASS:|
|                                          | 1) anybody	  	1) кто бы то ни было, кто-нибудь |
|                                          | 2) summertime	2) летний сезон|
|                                          | 3) sometimes		3) иногда |


## **Расположить слова в предложении в случайном порядке**
В каждом предложении, заканчивающемся знаками `.!?`, слова ставятся в случайном порядке. Все слова приводятся к нижнему регистру.  
Пример:


| Исходный текст                              | Задание     |
| :-------------                              | :------------- |
| This is the 1st sentence! And another one.  | Variant #n+1 |
|                                             | Place the words in sentences on correct order.|
|                                             | NAME:
|                                             | CLASS:|
|                                             | 1) the 1st is this sentence! |
|                                             | 2) another one  and.|


## **Расположить предложения в случайном порядке**
Все предложения, оканчивающееся знаками `.!?`, ставятся в случайном порядке.  
Пример:

| Исходный текст                              | Задание     |
| :-------------                              | :------------- |
| This is the 1st sentence!                   | Variant #n+1 |
| And another one.                            | Place the sentences on correct order.|
|  Is it the 3rd sentence?                    | NAME:
|                                             | CLASS:|
|                                             | 1)  And another one.|
|                                             | 2) another one  and.|
|                                             | 3) This is the 1st sentence!|


## **Выбрать глаголы из списка**
В каждом предложении, ничинающемся с новой строки, сдучайно выбирается один из элементов в двойных кавычках, разделенных обратной косой чертой `/`. Примечание: признаком глагола является наличие частицы "to /not to " (*обязательно с пробелом после "to"*). Глаголы заменяются на нижнее подчеркивание, в скобках рядом указывается форма глагола в инфинитиве. Все остальные слова (такие как: местоимения, существительные, признаки времени...) выбираются из множества в двойных кавычках, разделенных симолом обратной косой черты `/` и вставляются в преложение как есть.  
Пример:
* "I/He/She/We" "to walk/not to go/to sleep" "yesterday/today/tomorrow/never" there.
* "I/He/She/We" "to walk/not to go/to sleep" "yesterday/today/tomorrow/never" there.
* "I/He/She/We" "to walk/not to go/to sleep" "yesterday/today/tomorrow/never" there.
* "I/He/She/We" "to walk/not to go/to sleep" "yesterday/today/tomorrow/never" there.
* "to go/not to walk" "you/she" with me "yesterday/tomorrow" to the "zoo/circus"?
* "to go/not to walk" "you/she" with me "yesterday/tomorrow" to the "zoo/circus"?

На выходе:  

Variant \#n+1  
Write the correct form of the verbs in bracket.  
NAME:  
CLASS:  
1. She  \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ (to walk) tomorrow there.
2. I \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ (to walk) tomorrow there.
3. We \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ (not to go) never there.
4. She \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ (to walk) tomorrow there.
5. \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ (not to walk) she with me yesterday to the circus?
6. \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ (to go) you with me yesterday to the zoo?**

## **Пропустить слова в предложении**
Заменяет все слова, указанные в параметре "*Пропусить слова*" (регистронезависимо), на нижнее подчеркивание. Примечание: возвращает только один вариант. Пример:  
*Omit this and that words.*  
На выходе:  
***Insert correct words: This,  that***  

*Omit \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ and \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ words.*

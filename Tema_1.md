# Тема 1. Работа с Git
Отчет по теме 1 выполнила:
- Мансурова Елена Ильгизовна 
- ПИЭ-23-1

| Задание | Лаб_раб |
|---------|---------|
| Задание 1 | + |
| Задание 2 | + |
| Задание 3 | + |
| Задание 4 | + |
| Задание 5 | + |
| Задание 6 | + |
| Задание 7 | + |
| Задание 8 | + |
| Задание 9 | + |
| Задание 10 | + |
| Задание 11 | + |
| Задание 12 | + |
| Задание 13 | + |
| Задание 14 | + |
| Задание 15 | + |

знак "+" - задание выполнено; знак "-" - задание не выполнено;

## Лабораторная работа №1
### Установка.

``` git
git --version
```
### Результат.
![Меню](https://raw.githubusercontent.com/VernVen/SoftwareEngineering/main/pic/Рисунок1.png
)

## Выводы
Git успешно установлен

## Лабораторная работа №2
### Настройка.

``` git
git config --global user.name "VernVen"
git config --global user.email "mailelenda@mail.ru"
git config --global core.editor "code --wait"
git config –list
git config --global core.editor "code --wait"


```
### Результат.
![Меню](https://github.com/VernVen/SoftwareEngineering/blob/theme_1/pictures/%D0%A0%D0%B8%D1%81%D1%83%D0%BD%D0%BE%D0%BA2.png)

## Выводы
Установлено имя и почта пользователя, успешна пройдена проверка конфига, в качестве эдитора коммитов устновлен VSCode

## Лабораторная работа №3
### Создание нового репозитория.

``` git
cd "/c/Users/user/Documents/Software_Engineering"
git init

```
### Результат.
![Меню](https://github.com/VernVen/SoftwareEngineering/blob/theme_1/pictures/%D0%A0%D0%B8%D1%81%D1%83%D0%BD%D0%BE%D0%BA3.png)

## Выводы
Создан пустой репозиторий по указанному пути

## Лабораторная работа №4
### Подготовка файлов.

``` git
git add proba.txt
git status

```
### Результат.
![Меню](https://github.com/VernVen/SoftwareEngineering/blob/theme_1/pictures/%D0%A0%D0%B8%D1%81%D1%83%D0%BD%D0%BE%D0%BA4.png)

## Выводы
Файл proba.txt подготовлен к коммиту

## Лабораторная работа №5
### Фиксация изменений.

``` git
user@DESKTOP-NSD61J0 MINGW64 ~/Documents/Software_Engineering (master)
$ git commit -m "Первый коммит"
[master (root-commit) 796c4a7] Первый коммит
 1 file changed, 0 insertions(+), 0 deletions(-)
 create mode 100644 proba.txt

user@DESKTOP-NSD61J0 MINGW64 ~/Documents/Software_Engineering (master)
$ git log
commit 796c4a7f7b25e51e230a8c84ee8776b236ecd6ea (HEAD -> master)
Author: VervVen <mailelenda@mail.ru>
Date:   Sun Sep 14 20:18:48 2025 +0500

    Первый коммит

user@DESKTOP-NSD61J0 MINGW64 ~/Documents/Software_Engineering (master)
$ git log -n 5
commit 796c4a7f7b25e51e230a8c84ee8776b236ecd6ea (HEAD -> master)
Author: VervVen <mailelenda@mail.ru>
Date:   Sun Sep 14 20:18:48 2025 +0500

    Первый коммит

user@DESKTOP-NSD61J0 MINGW64 ~/Documents/Software_Engineering (master)
$ git log --oneline
796c4a7 (HEAD -> master) Первый коммит

user@DESKTOP-NSD61J0 MINGW64 ~/Documents/Software_Engineering (master)
$ git log --graph
* commit 796c4a7f7b25e51e230a8c84ee8776b236ecd6ea (HEAD -> master)
  Author: VervVen <mailelenda@mail.ru>
  Date:   Sun Sep 14 20:18:48 2025 +0500

      Первый коммит

user@DESKTOP-NSD61J0 MINGW64 ~/Documents/Software_Engineering (master)

```
### Результат.
![Меню](https://github.com/VernVen/SoftwareEngineering/blob/theme_1/pictures/%D0%A0%D0%B8%D1%81%D1%83%D0%BD%D0%BE%D0%BA5.png)

## Выводы
Коммит осуществляется командой git commit -m комментарий. Также есть несколько способов посмотреть лог коммитов: -n (кол-во), --oneline (в одну линию), --graph

## Лабораторная работа №6
### Подключение к удалённому репозиторию

``` git
user@DESKTOP-NSD61J0 MINGW64 ~/Documents/Software_Engineering (master)
$ git pull origin main
remote: Enumerating objects: 3, done.
remote: Counting objects: 100% (3/3), done.
remote: Compressing objects: 100% (2/2), done.
remote: Total 3 (delta 0), reused 3 (delta 0), pack-reused 0 (from 0)
Unpacking objects: 100% (3/3), 262 bytes | 16.00 KiB/s, done.
From https://github.com/VernVen/SoftwareEngineering
 * branch            main       -> FETCH_HEAD
 * [new branch]      main       -> origin/main
fatal: refusing to merge unrelated histories

user@DESKTOP-NSD61J0 MINGW64 ~/Documents/Software_Engineering (master)
$ git stash
No local changes to save

user@DESKTOP-NSD61J0 MINGW64 ~/Documents/Software_Engineering (master)
$ git stash apply
No stash entries found.

user@DESKTOP-NSD61J0 MINGW64 ~/Documents/Software_Engineering (master)
$ git stash pop
No stash entries found.

```
### Результат.
![Меню](https://github.com/VernVen/SoftwareEngineering/blob/theme_1/pictures/%D0%A0%D0%B8%D1%81%D1%83%D0%BD%D0%BE%D0%BA6.png)

## Выводы
С помощью git remote add можно связать локальный репозиторий гит с удаленным репозиторием, например GitHub. Также можно добавить все незафиксированные изменения в стэш, чтобы было удобно переключаться с одной ветки на другую с незафиксипованными изменениями

## Лабораторная работа №7
### Ветвление

``` git
user@DESKTOP-NSD61J0 MINGW64 ~/Documents/Software_Engineering (master)
$ git branch TestBranch

user@DESKTOP-NSD61J0 MINGW64 ~/Documents/Software_Engineering (master)
$ git checkout TestBranch
Switched to branch 'TestBranch'

user@DESKTOP-NSD61J0 MINGW64 ~/Documents/Software_Engineering (TestBranch)
$ git switch TestBranch
Already on 'TestBranch'

user@DESKTOP-NSD61J0 MINGW64 ~/Documents/Software_Engineering (TestBranch)
$ git checkout TestBranch
Already on 'TestBranch'

user@DESKTOP-NSD61J0 MINGW64 ~/Documents/Software_Engineering (TestBranch)
$ git merge feature
merge: feature - not something we can merge

```
### Результат.
![Меню](https://github.com/VernVen/SoftwareEngineering/blob/theme_1/pictures/%D0%A0%D0%B8%D1%81%D1%83%D0%BD%D0%BE%D0%BA7.png)

## Выводы
Ветвление происходит с помощью команды git branch. Для работы непосредственно с ветками нужно провести checkout имя_ветки.

## Лабораторная работа №8
### Фетч

``` git
user@DESKTOP-NSD61J0 MINGW64 ~/Documents/Software_Engineering (TestBranch)
$ git fetch https://github.com/VernVen/SoftwareEngineering.git
From https://github.com/VernVen/SoftwareEngineering
 * branch            HEAD       -> FETCH_HEAD

```
### Результат.
![Меню](https://github.com/VernVen/SoftwareEngineering/blob/theme_1/pictures/%D0%A0%D0%B8%D1%81%D1%83%D0%BD%D0%BE%D0%BA8.png)

## Выводы
Фетч является предварительной операцией перед слиянием или преобразованием. Позволяет проверить конфликтность перед изменениями.

## Лабораторная работа №9
### Удаление файлов, веток, локальных и удаленных репозиториев.

``` git
user@DESKTOP-NSD61J0 MINGW64 ~/Documents/Software_Engineering (TestBranch)
$ git rm proba.txt
rm 'proba.txt'
user@DESKTOP-NSD61J0 MINGW64 ~/Documents/Software_Engineering (TestBranch)
$ git checkout main
branch 'main' set up to track 'origin/main'.
Switched to a new branch 'main'
user@DESKTOP-NSD61J0 MINGW64 ~/Documents/Software_Engineering (main)
$ git branch -D TestBranch
Deleted branch TestBranch (was 796c4a7).

```
### Результат.
![Меню](https://github.com/VernVen/SoftwareEngineering/blob/theme_1/pictures/%D0%A0%D0%B8%D1%81%D1%83%D0%BD%D0%BE%D0%BA9.png)

## Выводы
Есть много способов удалить файл / ветку, в том числе: git rm --cached file.txt (удаляет файл только из индекса) и различие -d (безопасное удаление ветки - проверяет что ветка была слита перед удалением) и -D (принудительное удаление ветки)

## Лабораторная работа №10
### Отслеживание изменений в коммитах

``` git
user@DESKTOP-NSD61J0 MINGW64 ~/Documents/Software_Engineering (main)
$ git log
commit 1cabb1e433b1ccfc0857a24f77dbf0f2589c30ba (HEAD -> main, origin/main)
Author: VernalisVentus <mailelenda@mail.ru>
Date:   Sun Sep 14 16:58:47 2025 +0500

    Initial commit

user@DESKTOP-NSD61J0 MINGW64 ~/Documents/Software_Engineering (main)
$ git diff



```
### Результат.
![Меню](https://github.com/VernVen/SoftwareEngineering/blob/theme_1/pictures/%D0%A0%D0%B8%D1%81%D1%83%D0%BD%D0%BE%D0%BA10.png)

## Выводы
Можно посмотреть изменения в коммитах с помощью git log и git diff коммит1 коммит2 (различия между коммитами). Также можно просматривать изменения с помощью GitHub Desktop.

## Лабораторная работа №11
### Возвращение файла к предыдущему состоянию.

``` git
user@DESKTOP-NSD61J0 MINGW64 ~/Documents/Software_Engineering (main)
$ git checkout 886b7c7 -- proba.txt

user@DESKTOP-NSD61J0 MINGW64 ~/Documents/Software_Engineering (main)
$ git commit -m "Восстановление файла к текущему состоянию"
On branch main
Your branch is up to date with 'origin/main'.

nothing to commit, working tree clean


```
### Результат.
![Меню](https://github.com/VernVen/SoftwareEngineering/blob/theme_1/pictures/%D0%A0%D0%B8%D1%81%D1%83%D0%BD%D0%BE%D0%BA11.png)

## Выводы
Команда git checkout main --path заменит текущую версию файла на состояние из указанного коммита

## Лабораторная работа №12
### Возвращение к предыдущему коммиту

``` git
user@DESKTOP-NSD61J0 MINGW64 ~/Documents/Software_Engineering (main)
$ git reset --soft HEAD^


```
### Результат.
![Меню](https://github.com/VernVen/SoftwareEngineering/blob/theme_1/pictures/%D0%A0%D0%B8%D1%81%D1%83%D0%BD%D0%BE%D0%BA12.png)

## Выводы
Работает примерно как Ctrl+Z в программах редакторах. Есть несколько вариантов отката --hard хэш_коммита, --hard, --soft (с сохранением изменений текущей директории)

## Лабораторная работа №13
### Установка.

``` git
user@DESKTOP-NSD61J0 MINGW64 ~/Documents/Software_Engineering (main)
$ git commit --amend
[main f10c14a] Initial commit
 Author: VernalisVentus <mailelenda@mail.ru>
 Date: Sun Sep 14 16:58:47 2025 +0500
 2 files changed, 2 insertions(+)
 create mode 100644 .gitattributes
 create mode 100644 proba.txt

```
### Результат.
![Меню](https://github.com/VernVen/SoftwareEngineering/blob/theme_1/pictures/%D0%A0%D0%B8%D1%81%D1%83%D0%BD%D0%BE%D0%BA13.png)

## Выводы
--amend открывает редактор (в моем случае VSCode, так, как настроил в начале). Можно исправить параметры коммита. git rebase -i HEAD~3 исправить коммит два коммита назад

## Лабораторная работа №14
### Разрешение конфликтов при слиянии

``` git
user@DESKTOP-NSD61J0 MINGW64 ~/Documents/Software_Engineering (TestBranch2)
$ git merge master
fatal: refusing to merge unrelated histories

user@DESKTOP-NSD61J0 MINGW64 ~/Documents/Software_Engineering (TestBranch2)
$ git merge master --allow-unrelated-histories
Merge made by the 'ort' strategy.

user@DESKTOP-NSD61J0 MINGW64 ~/Documents/Software_Engineering (TestBranch2)
$ git push origin TestBranch2
Enumerating objects: 4, done.
Counting objects: 100% (4/4), done.
Delta compression using up to 8 threads
Compressing objects: 100% (2/2), done.
Writing objects: 100% (3/3), 423 bytes | 211.00 KiB/s, done.
Total 3 (delta 0), reused 0 (delta 0), pack-reused 0 (from 0)
remote:
remote: Create a pull request for 'TestBranch2' on GitHub by visiting:
remote:      https://github.com/VernVen/SoftwareEngineering/pull/new/TestBranch2
remote:
To https://github.com/VernVen/SoftwareEngineering.git
 * [new branch]      TestBranch2 -> TestBranch2

user@DESKTOP-NSD61J0 MINGW64 ~/Documents/Software_Engineering (TestBranch2)
$ git checkout TestBranch2
Already on 'TestBranch2'

user@DESKTOP-NSD61J0 MINGW64 ~/Documents/Software_Engineering (TestBranch2)
$ git branch -d master
Deleted branch master (was 796c4a7).

user@DESKTOP-NSD61J0 MINGW64 ~/Documents/Software_Engineering (TestBranch2)
$



```
### Результат.
![Меню](https://github.com/VernVen/SoftwareEngineering/blob/theme_1/pictures/%D0%A0%D0%B8%D1%81%D1%83%D0%BD%D0%BE%D0%BA14.png)

## Выводы
Для того, чтобы разрешить конфликты при слиянии (merge) необходимо:

1. Запустить команду слияния
2. Открыть файлы с конфликтами с помощью метки '<<<<<<<HEAD'и '>>>>>>>имя_ветки'
3. Разрешить конфликты, оставить только код, который должен остаться
4. Добавить измененные файлы
5. Продолжить операцию слияния
6. Завершить слияние

## Лабораторная работа №15
### Настройка .gitignore

``` git
*.log
node_modules/
.env
temp/*
```
### Результат.
![Меню](https://github.com/VernVen/SoftwareEngineering/blob/theme_1/pictures/%D0%A0%D0%B8%D1%81%D1%83%D0%BD%D0%BE%D0%BA15.png)

## Выводы
С помощью .gitignore можно исключить ненужные файлы, сократить размер репозитория, улучшить безопасность и сохранить чистоту репозитория.

## Общие выводы по теме
Гит - наиболее популярный инструмент управления версиями. Его ключевые аспекты:
- Управление версиями кода. Можно сохранять историю изменений, откатывать код
- Совместная работа. Множество разработчиков может работать над одним проектом
- Ветвление и слияние
- История изменений
- Восстановление данных
- Работа в оффлайне
- Эффективное управление конфликтами
- Открытый исходный код

Общая ценность Git заключается в увеличении эффективности разработки ПО.


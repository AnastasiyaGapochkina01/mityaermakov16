1) В домашней директории своего пользователя создать директорию `linux-home-works`, в ней создать
- директорию `library`
- в директории `library` создать директории `division` и `authors`
- перейти в директорию `division`, создать в нем директории `fiction`, `detective`, `textbook`
- не переходя в директорию `authors` создать в ней директории `bradbury_r`, `tanenbaum_s`, `christie_a`
- не переходя в директорию `authors/tanenbaum_s`, создать файл `computer_networks` и записать в него текст
```text
ISBN-13: 978-0-13-212695-3
ISBN-10: 0-13-212695-8
Computer networks / Andrew S. Tanenbaum
```
- в директории `christie_a` создать файл `crooked_house` с текстом
```text
ISBN: -
Agatha Christie Limited Edition
```
- в директории `bradbury_r` создать файл `the_martian_chronicles` с текстом
```text
ISBN: 978-1-4516-7819-2
Ray Bradbury
```
2) В директории `linux-home-works` создать директорию `storage`, в ней создать
- директории `foodstuff`, `household_chemicals`, `toys`
- перейти в директорию `foodstuff`
- создать в `foodstuff` директории `fruits`, `groceries`, `milk_products`
- не выходя из `foodstuff` содать в `household_chemicals` директории `cosmetic`, `laundry_products`, `cleaning_products`
- не выходя из `foodstuff` содать в `toys` директории `educational_toys`, `soft_toys`
- перейти в каталог `storage`
- в директории `foodstuff/fruits` создать файл с именем `apples` и содержимым
```text
Golden
Gala
Caramel
Fuji
Red
```
- в директории `household_chemicals/cleaning_products` создать файл с именем `floor_products` и содержимым
```text
Mr Proper
Grass
Synergetic
```
- в директории `household_chemicals/laundry_product`s создать файл с именем `powders` и содержимым
```text
Persil
Laska
Tide
Ariel
```
- перейти в директорию `household_chemicals/cleaning_products`; создать в `household_chemicals/cosmetic` файл с именем `lipsticks` и содержимым
```text
Beloris
Luxvisage
Novo Small
```
- не выходя из `household_chemicals/cleaning_products` создать в `toys/educational_toys` файл с именем `constructors` и содержимым
```text
Arduino
Lego
Не выходя из storage/household_chemicals/cleaning_products создать в storage/toys/soft_toys файл с именем all_products и содержимым
Bear
Gouse
Lion
Tiger
```
- перейти в директорию `toys/soft_toys`
- не выходя из `toys/soft_toys` скопировать файл с именем `all_products` в `toys/`
- не выходя из `/toys/soft_toys` создать РЯДОМ с директорией `storage` директорию `reservations`
- не выходя из `toys/soft_toys` скопировать файл `foodstuff/fruits/apples` в директорию `reservations`
- не выходя из `toys/soft_toys` скопировать файл `household_chemicals/cleaning_products/floor_products` в директорию `reservations`
- скопировать директорию `storage/toys/` в директорию reservations
- скопировать содержимое `household_chemicals` в директорию `reservations/chemicals`
- создать рядом с директориями `storage` и `reservations` директорию `shipping`
- создать символическую ссылку `shipping/cleaning`, ведущую на файл `household_chemicals/cleaning_products/powders`
- создать символическую ссылку `shipping/lipsticks`, ведущую на файл `household_chemicals/cosmetic/lipsticks`
- вывести полное дерево каталога `linux-home-works`

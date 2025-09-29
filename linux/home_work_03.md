1) Создать пользователя `devops` с домашней директорией и комментарием `"DevOps Engineer"`; установить ему пароль `qwerty123`
2) Создать группу `admins` и добавить туда пользователя `devops`
3) Проверить, что `devops` дейтсвительно стал членом группы `admins` (два способа)
4) Установить `zsh` (https://github.com/ohmyzsh/ohmyzsh/wiki/Installing-ZSH)
5) Изменить основной `shell` для `devops` на `/bin/zsh`
6) Создать директорию `/opt/srv/backups` с владельцем `root` и группой владельцев `admins`; назнчить ей права, при которых
- владелец может делать все
- группа может делать все
- все остальные не могут ничего
7) Создать пользователя `backup`, добавить его в группу `admins`
8) Создать группу `web-users`
9) Переключиться на пользователя `backup` и проверить доступ к директории `/opt/srv/backups` создав там файл `test-bkp` с содержимым `Test backup`
10) Создать директорию `/opt/srv/nginx`, установить владельцем директории `www-data`, а группой `web-users`; назначить права на директорию
- владелец можем все
- группа может читать и исполнять
- все остальные не могут ничего
11) Создать пользователя `designer` и добавить его в группу `web-users`
12) Переключиться на пользователя `designer` и проверить доступ к директории `/opt/srv/nginx` - создать в ней файл `server.conf` с любым содержимым
Выйти из под пользователя `designer` и добавить группе `web-users` права на запись в `/opt/srv/nginx`; снова переключиться на `designer` и попробовать создать `server.conf` с любым содержимым
13) Создать сервисного (служебного) пользователя `backend` без возможности входа в систему
14) Переименовать пользователя `backend` в `apps-user`. Изменился ли UID?
15) Из файла `/etc/passwd` вывести имена и UID всех добавленных в задании пользователей
16) В директории `linux-home-works` (создали в первой домашке) создать директорию `bash-scripts`; в директории `bash-scripts` создать файл `gen_go_project.sh` с содержимым
```bash
#!/bin/bash

PROJECT=$1
if [ -z "$PROJECT" ]; then
  echo "Usage: $0 <project-name>"
  exit 1
fi
mkdir -p $PROJECT/{cmd/$PROJECT,internal,pkg}
cd $PROJECT
echo "# $PROJECT" > README.md
echo -e "bin/\n*.exe\n*.log\nvendor/" > .gitignore

cat <<EOF > cmd/$PROJECT/main.go
package main

import "fmt"

func main() {
    fmt.Println("Hello, $PROJECT!")
}
EOF

echo "Project files generated successfully."
```
17) Сделать файл `gen_go_project.sh` исполняемым и запустить командой `./gen_go_project.sh ecommerce`
18) Посмотреть, создалась ли рядом с скриптом директория `ecommerce`; вывести ее содержимое в виде дерева
19) Удалить всех созданных ранее пользователей (`devops`, `backup`, `designer`, `apps-user`) и группы (`admins`, `web-users`)
20) Удалить директории `/opt/srv/nginx` и `/opt/srv/backups`
21) Создать пользователя `logger` с домашней директорией `/var/logger`
22) Создать пользователей `gitlab-runner` и `jenkins`
23) Создать группу `deploy`, добавить в нее пользователей `jenkins` и `gitlab-runner`
24) В директории `ecommerce` создать директорию `logs`
25) Назначить группой владельцев директории `logs` группу `logger`; разрешить группе полные права на эту директорию
26) Изменить владельца и группу для всей директории `ecommerce` (кроме `logs`) на `root:deploy`

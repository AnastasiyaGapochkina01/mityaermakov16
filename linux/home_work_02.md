1) В директории `linux-home-works`, которую создали в первой домашке, создать директорию `text_processing`
2) В директории `text_processing` cоздать файл `info.csv` с таким содержимым
```csv
Name:Company:Price:Ganre:Multiplayer
Item1:Company1:60000$:Ganre1:Yes
Item2:Company2:70000$:Ganre2:Yes
Item3:Company3:90000$:Ganre1:Yes
Item4:Company4:90000$:Ganre1:No
Item5:Company5:110000$:Ganre1:Yes
Item6:Company6:410000$:Ganre2:Yes
Item7:Company1:60000$:Ganre1:Yes
Item8:Company4:40000$:Ganre2:No
Item9:Company3:90000$:Ganre1:Yes
```
3) В файле `info.csv` с помощью `grep` найти
- строки, которые содержат слово `No`
- строки, в которых встречается слово `Ganre2`
- строки, в которых встречается слово `Ganre2` и вывести для них только третье поле
4) Создать файл `metrics` с содержимым
```csv
metric_name:metric_type:interval
cache_disk_use:gauge:1
cache_use:gauge:0
key_buffer_bytes_used:byte:3
table.rows.read:count:10
disk_use:gauge:10
data_size:gauge:1
rows_deleted:count:1
bytes_received:byte:1
```
5) В файле `metrics`найти
- строки, в которых встречается слово `gauge` и вывести только первое поле
- строки, в которых встречается слово `byte` и вывести только третье поле
- строки, в которых встречается слово `disk` и вывести только второе поле
6) Из файла `/proc/meminfo` получить все строки. относящиеся к `HugePages`
7) Отфильтровать вывод команды `free -h` так, чтобы получить количество доступной (Available) оперативной памяти
8) В директории `text_processing` создать файл `logs` с содержимым
```
# Cron logs
Oct 20 06:24:01 server1 CRON[1349677]: (user1) CMD (   /usr/bin/python3 /home/user1/update.py)
Oct 20 06:25:01 server3 CRON[1349678]: (user2) CMD (   /usr/bin/python3 /home/user2/report.py)
Oct 20 06:26:01 server2 CRON[1349679]: (root) CMD (   /usr/bin/cleanup.sh)
Oct 20 06:27:01 server3 CRON[1349680]: (user3) CMD (   /usr/bin/backup.sh)
Oct 20 06:28:01 server1 CRON[1349681]: (user4) CMD (   /usr/bin/monitor.sh)

# Error logs
Oct 20 06:30:00 server1 sshd[12345]: Failed password for invalid user admin from 192.168.0.10 port 22 ssh2
Oct 20 06:31:00 server3 sshd[12346]: Failed password for invalid user guest from 192.168.0.11 port 22 ssh2
Oct 20 06:32:00 server1 sshd[12347]: Accepted password for user2 from 192.168.0.12 port 22 ssh2
Oct 20 06:33:00 server1 sshd[12348]: Failed password for invalid user test from 192.168.0.13 port 22 ssh2

# Warning logs
Oct 20 06:35:00 server1 kernel: [123456] Warning! CPU temperature is high.
Oct 21 09:10:00 server2 kernel: [123458] Warning! High CPU usage detected on process ID 5678.
Oct 21 09:11:00 server2 systemd[1]: Warning! Service myservice.service is taking too long to start.
Oct 21 09:12:00 server2 sshd[23461]: Warning! Multiple failed login attempts from 192.168.0.25.
Oct 21 09:13:00 server2 application[34571]: Warning! Disk space on /home is below 10% remaining.

# Info logs
Oct 21 09:02:00 server2 application[34569]: INFO User1 logged in successfully.
Oct 21 09:03:00 server2 application[34570]: INFO User3 logged out.
Oct 21 09:14:00 server2 application[34572]: INFO User4 logged in successfully from 192.168.0.26.
Oct 21 09:15:00 server2 application[34573]: INFO Backup completed successfully at /backup/user4_backup.tar.gz.
Oct 21 09:16:00 server2 systemd[1]: INFO Service myservice.service started successfully.
Oct 21 09:17:00 server2 sshd[23462]: INFO User1 logged out from session on terminal pts/0.
```
9) В файле logs.txt найти
- записи, которые содержат `application`
- записи о запусках `cron` на сервере `server3`
- запись о сервисе `myservice`
- записи, содержащие `ssh` и вывести для них название сервера
10) Из вывода команды `lscpu` получить значение `Vendor ID`
11) Вывести на экран файл `/etc/ssh/sshd_config` без комментариев (комментарий это строка, начинающаяся с символа `#`)

---

1) В директории `text_processing` создать файл `ssh_list.txt`, содержимым которого будет результат команды `ls -l /etc/ssh/`
2) Выполнить команду `cat ssh_list.txt nosuchfile.txt`;  стандартный поток ошибок (stderr) перенаправить в файл `errors.log`
3) Выполнить команду `cat ssh_list.txt nosuchfile.txt`, но теперь ОБА потока (stdout и stderr) перенаправить в файл `output.log`
4) В файле `ssh_list.txt` найти все строки, содержащие `config` и одновременно вывести результат на экран, и в файл `ssh_confs.txt`
5) С помощью `cat` создать файл `hello_cat` с содержимым
```
Hello,

This is a multi-line message
created using a here-document.

Best regards.
```

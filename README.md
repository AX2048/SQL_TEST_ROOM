![](.gitcontent/title_new.png)

Подробности проекта смотри в моём Notion:

https://www.notion.so/ax2048/SQL-TEST-ROOM-a0124781bee14005a6f0ddd1e02acf27?pvs=4

# Запуск

В начале нужно создать директории `data-mysql` и `data-postgres` в корне проекта.

Далее в директории с `docker-compose.yml` нужно выполнить:

```
docker compose up --build
```

Далее можно запускать так:
```
docker compose up -d
```

`ps`

```
PS C:\\Users\\xxxxxx\\Documents\\CODE\\SQL_TEST_ROOM> docker compose ps
NAME                       IMAGE                  COMMAND                  SERVICE             CREATED              STATUS              PORTS
sql_test_room-adminer-1    adminer                "entrypoint.sh php -…"   adminer             About a minute ago   Up About a minute   0.0.0.0:8080->8080/tcp
sql_test_room-mysql-1      mysql:latest           "docker-entrypoint.s…"   mysql               About a minute ago   Up About a minute   0.0.0.0:3306->3306/tcp, 33060/tcp
sql_test_room-postgres-1   postgres:latest        "docker-entrypoint.s…"   postgres            About a minute ago   Up About a minute   0.0.0.0:5432->5432/tcp
sql_test_room-python-1     sql_test_room-python   "python ./while_true…"   python              About a minute ago   Up About a minute
```

## Управление

`docker compose up` - развёртывает сервисы веб-приложений и создаёт из docker-образа новые контейнеры, а также сети, тома и все конфигурации, указанные в файле Docker Compose. Добавляя флаг -d, вы выполняете команду в раздельном или фоновом режиме, сохраняя возможность управления терминалом (чуть ниже рассмотрим примеры для наглядности). 

`docker compose down` - останавливает все сервисы, связанные с определённой конфигурацией Docker Compose. В отличие от команды stop, она также удаляет все контейнеры и внутренние сети, связанные с этими сервисами — но НЕ указанные внутри тома. Чтобы очистить и их, надо дополнить команду down флагом -v.

`docker compose stop` - останавливает все сервисы, связанные с определённой конфигурацией Docker Compose. Она НЕ удаляет ни контейнеры, ни связанные с ними внутренние тома и сети.

`docker compose start` - запускает любые остановленные сервисы в соответствии с параметрами остановленной конфигурации, указанными в том же файле Docker Compose.

`docker exec -it sql_test_room-mysql-1 bash` - подключится к контейнеру sql_test_room-mysql-1 . Т.е. выполнить команду `bash` в контейнере - перейти в `bash` контейнера. Аналогично для `sql_test_room-postgres-1` и `sql_test_room-python-1`.

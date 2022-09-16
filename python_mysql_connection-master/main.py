import pymysql
from config import host, user, password, db_name
import csv


try:
    connection = pymysql.connect(
        host=host,
        port=3306,
        user=user,
        password=password,
        database=db_name,
        cursorclass=pymysql.cursors.DictCursor
    )
    print("successfully connected...")
    print("#" * 20)

    try:
        cursor = connection.cursor()

        #create table(Создание таблицы)
        # with connection.cursor() as cursor:
        #     create_table_query = "CREATE TABLE `users_and_vacancy`(id int AUTO_INCREMENT," \
        #                          " name varchar(32)," \
        #                          " Name_vacancy varchar(120), PRIMARY KEY (id));"
        #     cursor.execute(create_table_query)
        #     print("Table created successfully")

        #Transfer from Csv in Sql (перенос данных из Csv в базу данных (Sql my admin))
        # with open("data.csv", newline='',encoding="Cp1251") as csvfile:
        #     reader = csv.DictReader(csvfile, delimiter=",")
        #     for row in reader:
        #         name = row['name']
        #         url = row['url']
        #         print(name)
        #         print(url)
        #         with connection.cursor() as cursor:
        #              insert_query = f"INSERT INTO `vacancy` (Name,Url) VALUES ('{name}','{url}');"
        #              cursor.execute(insert_query)
        #              connection.commit()

        # Transfer from Sql in Csv (перенос данных из (Sql my admin) в csv)
        # with connection.cursor() as cursor:
        #     select_all_rows = "SELECT * FROM `users_and_vacancy`"
        #     cursor.execute(select_all_rows)
        #     rows = cursor.fetchall()
        #     for row in rows:
        #          name = row['name']
        #          vacancy = row['Name_vacancy']
        #          with open("Tests_data.csv", "a") as file:
        #             writer = csv.writer(file)
        #             writer.writerow((name, vacancy))
        #     print("#" * 20)

        # #insert data (Заполнение строки)
        # with connection.cursor() as cursor:
        #     insert_query = "INSERT INTO `users` (name, password, email) VALUES ('Anna', 'qwerty', 'anna@gmail.com');"
        #     cursor.execute(insert_query)
        #     connection.commit()

        # with connection.cursor() as cursor:
        #     insert_query = "INSERT INTO `users` (name, password, email) VALUES ('Victor', '123456', 'victor@gmail.com');"
        #     cursor.execute(insert_query)
        #     connection.commit()

        # with connection.cursor() as cursor:
        #     insert_query = "INSERT INTO `users` (name, password, email) VALUES ('Oleg', '112233', 'olegan@mail.ru');"
        #     cursor.execute(insert_query)
        #     connection.commit()
        #
        # with connection.cursor() as cursor:
        #     insert_query = "INSERT INTO `users` (name, password, email) VALUES ('Oleg', 'kjlsdhfjsd', 'ole2gan@mail.ru');"
        #     cursor.execute(insert_query)
        #     connection.commit()

        # with connection.cursor() as cursor:
        #     insert_query = "INSERT INTO `users` (name, password, email) VALUES ('Oleg', '889922', 'olegan3@mail.ru');"
        #     cursor.execute(insert_query)
        #     connection.commit()

        # update data (Обновить данные)
        # with connection.cursor() as cursor:
        #     update_query = "UPDATE `users` SET password = 'xxxXXX' WHERE name = 'Oleg';"
        #     cursor.execute(update_query)
        #     connection.commit()

        # delete data(Удалить данные)
        # with connection.cursor() as cursor:
        #     delete_query = "DELETE FROM `users` WHERE id = 5;"
        #     cursor.execute(delete_query)
        #     connection.commit()

        # drop table(Удалить таблицу)
        # with connection.cursor() as cursor:
        #     drop_table_query = "DROP TABLE `users`;"
        #     cursor.execute(drop_table_query)

        # drop table(Удалить стобец)
        # with connection.cursor() as cursor:
        #     drop_table_query = "ALTER TABLE vacancy DROP COLUMN Name_hr;"
        #     cursor.execute(drop_table_query)

        # select all data from table (Вывести данные из таблицы в лог)
        # with connection.cursor() as cursor:
        #     select_all_rows = "SELECT * FROM `users`"
        #     cursor.execute(select_all_rows)
        #     rows = cursor.fetchall()
        #     for row in rows:
        #         print(row)
        #     print("#" * 20)

        # Сombining strings (Обединение строк c разных таблиц и вывести их в лог)
        # with connection.cursor() as cursor:
        #     select_all_rows = "SELECT users.name,vacancy.Name FROM users JOIN vacancy ON users.id = vacancy.id_hr;"
        #     cursor.execute(select_all_rows)
        #     rows = cursor.fetchall()
        #     for row in rows:
        #         print(row)
        #     print("#" * 20)

        # Сombining strings load in new tables (Обединение строк c разных таблиц и загрузка в новую таблицу)
        # with connection.cursor() as cursor:
        #     select_all_rows = "SELECT users.name,vacancy.Name FROM users JOIN vacancy ON users.id = vacancy.id_hr;"
        #     cursor.execute(select_all_rows)
        #     rows = cursor.fetchall()
        #     for row in rows:
        #         print(row)
        #         name = row['name']
        #         nameV = row['Name']
        #         with connection.cursor() as cursor:
        #           insert_query = f"INSERT INTO `users_and_vacancy` (name, Name_vacancy) VALUES ( '{name}', '{nameV}');"
        #           cursor.execute(insert_query)
        #           connection.commit()
        #     print('Все данные загружены в новую таблицу')

    finally:
        connection.close()

except Exception as ex:
    print("Connection refused...")
    print(ex)

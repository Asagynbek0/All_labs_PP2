import psycopg2
import csv

# Подключение к базе данных
conn = psycopg2.connect(
    database="postgres",
    user="postgres",
    password="12345678",
    host="localhost",
    port="5432"
)

cur = conn.cursor()

# Создание таблицы 
def create_table():
    cur.execute("DROP TABLE IF EXISTS phonebook")
    cur.execute("""
        CREATE TABLE phonebook (
            id SERIAL PRIMARY KEY,
            first_name VARCHAR(100),
            number VARCHAR(20)
        )
    """)
    conn.commit()

# Вставка пользователя вручную
def insert_user_input():
    name = input("Введите имя: ")
    phone = input("Введите номер телефона: ")
    cur.execute("INSERT INTO phonebook (first_name, number) VALUES (%s, %s)", (name, phone))
    conn.commit()
    print("Запись добавлена.")

# Загрузка данных из contacts.csv
def insert_from_contacts_csv(file_path):
    with open(file_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            cur.execute(
                "INSERT INTO phonebook (first_name, number) VALUES (%s, %s)",
                (row['first_name'], row['number'])
            )
    conn.commit()
    print("Data in csv file successful upploadded")


# Обновление записи
def update_data():
    name = input("Введите имя, которое нужно обновить: ")
    new_name = input("Новое имя (оставьте пустым, если не нужно менять): ")
    new_phone = input("Новый номер (оставьте пустым, если не нужно менять): ")

    if new_name:
        cur.execute("UPDATE phonebook SET first_name = %s WHERE first_name = %s", (new_name, name))
    if new_phone:
        cur.execute("UPDATE phonebook SET number = %s WHERE first_name = %s", (new_phone, new_name or name))
    conn.commit()
    print(" Updated ")

# Поиск данных
def query_data():
    print("Фильтрация:")
    filter_type = input("Фильтр по (name/phone/all): ").lower()

    if filter_type == "name":
        name = input("Введите имя: ")
        cur.execute("SELECT * FROM phonebook WHERE LOWER(first_name) = LOWER(%s)", (name,))

    elif filter_type == "number":
        number = input("Введите номер: ")
        cur.execute("SELECT * FROM phonebook WHERE number = %s", (number,))
    else:
        cur.execute("SELECT * FROM phonebook")

    rows = cur.fetchall()
    if rows:
        for row in rows:
            print(row)
    else:
        print("Nothing found")

# Удаление записи
def delete_data():
    field = input("Удалить по (name/phone): ").lower()

    if field == "name":
        name = input("Введите имя: ")
        cur.execute("DELETE FROM phonebook WHERE first_name = %s", (name,))
    elif field == "phone":
        phone = input("Введите номер: ")
        cur.execute("DELETE FROM phonebook WHERE number = %s", (phone,))

    conn.commit()
    print("Data deleted")

# Главное меню
def menu():
    create_table()

    # Автоматическая загрузка из contacts.csv один раз при старте
    insert_from_contacts_csv(r'C:\Users\alinu\Documents\new_folder\labs\lab10\contacts.csv')

    while True:
        print("\n Меню:")
        print("1 - Input user")
        print("2 - Update data")
        print("3 - find")
        print("4 - removing")
        print("0 - quite")

        choice = input("Choose option: ")

        if choice == "1":
            insert_user_input()
        elif choice == "2":
            update_data()
        elif choice == "3":
            query_data()
        elif choice == "4":
            delete_data()
        elif choice == "0":
            break
        else:
            print(" wrong choice")

    # Завершение соединения
    cur.close()
    conn.close()
    print(" Program ended")

# Запуск
if __name__ == "__main__":
    menu()

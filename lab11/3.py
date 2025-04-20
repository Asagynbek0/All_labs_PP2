import psycopg2
import csv

# Подключение к базе данных PostgreSQL
conn = psycopg2.connect(
    database="postgres",
    user="postgres",
    password="12345678",
    host="localhost",
    port="5432"
)
cur = conn.cursor()

# Процедура: вставка нового пользователя или обновление существующего
drop_delete_user_by_name_or_phone_p = """
    CREATE OR REPLACE PROCEDURE delete_user_by_name_or_phone(pattern VARCHAR)
    LANGUAGE plpgsql
    AS $$ 
    BEGIN
      DELETE FROM phonebook WHERE first_name ILIKE '%' || pattern || '%'
        OR number ILIKE '%' || pattern || '%';
    END;
    $$;
    """
    
def create_procedure():
    # Создаем процедуру один раз, если она не существует
    cur.execute(drop_delete_user_by_name_or_phone_p)
    conn.commit()

def drop_delete_user_by_name_or_phone(pattern):
    # Вызываем процедуру для удаления
    cur.execute("CALL delete_user_by_name_or_phone(%s)", (pattern,))
    conn.commit()
    print(f"Пользователь '{pattern}' удалён.")

# Создание таблицы
def create_table():
    cur.execute("""
        CREATE TABLE IF NOT EXISTS phonebook (
            id SERIAL PRIMARY KEY,
            first_name VARCHAR(100),
            number VARCHAR(20)
        )
    """)
    conn.commit()

# Загрузка из CSV
def insert_from_csv(file_path):
    with open(file_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            if len(row) != 2:
                continue
            cur.execute("INSERT INTO phonebook (first_name, number) VALUES (%s, %s)", (row[0], row[1]))
    conn.commit()
    print("Данные из CSV добавлены.")

# Меню
def menu():
    create_table()
    create_procedure()  # Создаем процедуру один раз

    while True:
        print("\nМеню:")
        print("1 - Загрузить из CSV")
        print("2 - Удалить по имени или номеру")
        print("0 - Выход")
        choice = input("Выберите действие: ")

        if choice == "1":
            path = input("Введите путь к CSV файлу: ")
            insert_from_csv(path)
        elif choice == "2":
            pattern = input("Введите имя или номер для удаления: ")
            drop_delete_user_by_name_or_phone(pattern)
        elif choice == "0":
            break
        else:
            print("Неверный выбор!")

    cur.close()
    conn.close()

if __name__ == "__main__":
    menu()

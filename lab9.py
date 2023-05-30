import mysql.connector
import tkinter as tk

connection1 = mysql.connector.connect(
    host='localhost',
    user='root',
    password='sifrem'
)
myCursor=connection1.cursor()
myCursor.execute("CREATE DATABASE IF NOT EXISTS MarvelDatabase")

connection = mysql.connector.connect(
    host='localhost',
    user='root',
    password='sifrem',
    database='MarvelDatabase'
)
cursor = connection.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS movies(
                  ID int(10) NOT NULL,
                  Movie varchar(100) NOT NULL,
                  DateInfo varchar(100) NOT NULL,
                  Mcu_Phase varchar(100))''')

with open('marvel.txt', 'r') as file:
    next(file)
    for line in file:
        line = line.strip()
        data = line.split('\t')

        movie_id = int(data[0])
        movieTitle = data[1]
        releaseDate = data[2]
        mcuPhase = data[3]

        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='sifrem',
            database='MarvelDatabase'
        )
        cursor = connection.cursor()

        # Task 3
        insertQuery = """
            INSERT INTO movies (ID, Movie, DateInfo, Mcu_Phase)
            VALUES (%s, %s, %s, %s)
        """
        values = (movie_id, movieTitle, releaseDate, mcuPhase)
        cursor.execute(insertQuery, values)

        connection.commit()
        cursor.close()
        connection.close()

master = tk.Tk()
master.title('Marvel Movies')

def functionDropD(event):
    selected_id = dropdown_var.get()
    textBox.delete('1.0', tk.END)
    textBox.insert(tk.END, f"Selected ID: {selected_id}")

labelDropdown = tk.Label(master, text='Select ID:')
labelDropdown.pack()

dropdown_var = tk.StringVar(master)
dropdown = tk.OptionMenu(master, dropdown_var, *range(1, 100), command=functionDropD)
dropdown.pack()

def functionEntry():
    entryMaster = tk.Toplevel()
    entryMaster.title('Add Entry')
buttonAdd = tk.Button(master, text='Add', command=functionEntry)
buttonAdd.pack()

def functionAll():
    textBox.delete('1.0', tk.END)

    connection = mysql.connector.connect(
        host='localhost',
        user='root',
        password='sifrem',
        database='MarvelDatabase'
    )
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM movies")
    rows = cursor.fetchall()

    for row in rows:
        entry = f"ID: {row[0]}\n"
        entry += f"Movie: {row[1]}\n"
        entry += f"Date: {row[2]}\n"
        entry += f"MCU Phase: {row[3]}\n\n"
        textBox.insert(tk.END, entry)
    cursor.close()
    connection.close()

buttonListAll = tk.Button(master, text='LIST ALL', command=functionAll)
buttonListAll.pack()

textBox = tk.Text(master)
textBox.pack()

master.mainloop()
import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QTableWidgetItem
from PyQt6.uic import loadUi
import sqlite3

class CoffeeApp(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi("main.ui", self)
        self.load_data()

    def load_data(self):
        connection = sqlite3.connect("coffee.sqlite")
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM coffee")
        rows = cursor.fetchall()

        self.tableWidget.setRowCount(len(rows))
        self.tableWidget.setColumnCount(7)

        for i, row in enumerate(rows):
            for j, item in enumerate(row):
                self.tableWidget.setItem(i, j, QTableWidgetItem(str(item)))

        connection.close()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CoffeeApp()
    window.show()
    sys.exit(app.exec())

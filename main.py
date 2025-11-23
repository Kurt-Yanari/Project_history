import istorya
import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, 
                            QPushButton, QLabel, QListWidget, QTextEdit, 
                            QMessageBox, QLineEdit, QHBoxLayout, QScrollArea)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont

# Списки для хранения данных о периодах и правителей (остаются те же самые)
periods = [
    "Начало правления Рюриковичей в Киеве 862-1157 годы",
    "Правление Рюриковичей во Владимире 1125-1263", 
    "Правление Рюриковичей в Москве 1263-1598",
    "Правители периода Смутного времени 1598-1613",
    "Династия Романовых 1613-1917",
    "Советский период. СССР 1917-1991",
    "Российская Федерация. РФ 1991- настоящее время"
]

kiev_rulers = [
    ("Рюрик", "862–879", "rurik"),
    ("Олег Вещий", "879–912", "oleg"),
    ("Игорь Старый", "912–945", "igorold"),
    ("Ольга", "945-964", "olga"),
    ("Святослав Игоревич", "946-972", "svyatigor"),
    ("Владимир I Красное Солнышко", "978–1015", "vladsvyat"),
    ("Ярослав Мудрый", "1019–1054", "yarik"),
    ("Владимир Всеволодович Мономах", "1113–1125", "vladmono"),
    ("Мстислав Владимирович Великий", "1125–1132", "mstislav")
]

vladimir_rulers = [
    ("Юрий Владимирович Долгорукий", "1125–1157", "yradolg"),
    ("Андрей Юрьевич Боголюбский", "1157–1174", "andreybog"),
    ("Всеволод Юрьевич Большое гнездо", "1176–1212", "vsevolod"),
    ("Александр Ярославич Невский", "1252–1263", "nevskiy")
]

moscow_rulers = [
    ("Даниил Александрович", "1263–1303", "danil"),
    ("Иван Данилович Калита", "1325–1340", "ivankal"),
    ("Дмитрий Иванович Донской", "1359–1389", "dimadon"),
    ("Василий Дмитриевич", "1389–1425", "vasya1"),
    ("Василий II Васильевич Тёмный", "1425–1462", "vasya2"),
    ("Иван III Васильевич Великий", "1462–1505", "vanya3"),
    ("Василий III Иванович", "1505–1533", "vasya3"),
    ("Иван IV Васильевич Грозный + правление Елены Глинской", "1533–1584", "glinskaya"),
    ("Фёдор I Иванович", "1584–1598", "fedya")
]

romanov_rulers = [
    ("Михаил Фёдорович", "1613–1645", "misha"),
    ("Алексей Михайлович Тишайший", "1645–1676", "alesha"),
    ("Фёдор III Алексеевич", "1676–1682", "fedyaaleks"),
    ("Иван V Алексеевич и Пётр I Алексеевич (совместно)", "1682–1696", "petya1"),
    ("Пётр Алексеевич Великий", "1696–1725", "katya1"),
    ("Екатерина I", "1725–1727", "petya2"),
    ("Пётр II", "1727–1730", "anna"),
    ("Анна Иоанновна", "1730–1740", "liza"),
    ("Елизавета Петровна", "1741–1761", "petya3"),
    ("Пётр III", "1761–1762", "katya2"),
    ("Екатерина II Великая", "1762–1796", "pavel1"),
    ("Павел I", "1796–1801", "sasha1"),
    ("Александр I", "1801–1825", "kolyan1"),
    ("Николай I", "1825–1855", "sanya2"),
    ("Александр II Освободитель", "1855–1881", "sanya3"),
    ("Александр III Миротворец", "1881–1894", "kolya2"),
    ("Николай II", "1894–1917", "kolya2")
]

soviet_rulers = [
    ("Владимир Ильич Ленин", "1917–1924", "lenin"),
    ("Иосиф Виссарионович Сталин", "1924–1953", "stalin"),
    ("Никита Сергеевич Хрущёв", "1953–1964", "hrushev"),
    ("Леонид Ильич Брежнев", "1964–1982", "brejnev"),
    ("Юрий Владимирович Андропов", "1982–1984", "andropov"),
    ("Михаил Сергеевич Горбачёв", "1985–1991", "gorbachev")
]

rf_rulers = [
    ("Борис Николаевич Ельцин", "1991-1999", "elcin"),
    ("Владимир Владимирович Путин", "2000-2008", "putin"),
    ("Дмитрий Анатольевич Медведев", "2008-2012", "medved"),
    ("Владимир Владимирович Путин", "2012-настоящее время", "putin")
]

class HistoryApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Справочник исторических личностей")
        self.setGeometry(100, 100, 800, 600)
        self.show_main_menu()
    
    def clear_layout(self, layout):
        if layout is not None:
            while layout.count():
                child = layout.takeAt(0)
                if child.widget():
                    child.widget().deleteLater()
    
    def show_main_menu(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)
        
        title = QLabel("Добро пожаловать в справочник исторических личностей")
        title.setFont(QFont("Arial", 16, QFont.Bold))
        title.setAlignment(Qt.AlignCenter)
        layout.addWidget(title)
        
        menu_options = [
            ("Период", self.show_periods),
            ("Церковные личности", self.show_church_figures),
            ("Поиск по дате", self.show_date_search),
            ("Незнакомые термины", self.show_unknown_terms),
            ("Современники", self.show_contemporaries),
            ("Выход", self.close)
        ]
        
        for text, command in menu_options:
            btn = QPushButton(text)
            btn.setFont(QFont("Arial", 12))
            btn.clicked.connect(command)
            layout.addWidget(btn)
    
    def show_periods(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)
        
        title = QLabel("Выберите период:")
        title.setFont(QFont("Arial", 14, QFont.Bold))
        layout.addWidget(title)
        
        scroll = QScrollArea()
        scroll_widget = QWidget()
        scroll_layout = QVBoxLayout(scroll_widget)
        
        # Используем цикл for для создания кнопок периодов
        for i, period in enumerate(periods):
            btn = QPushButton(period)
            btn.setFont(QFont("Arial", 11))
            btn.clicked.connect(lambda checked, idx=i+1: self.handle_period_selection(idx))
            scroll_layout.addWidget(btn)
        
        scroll.setWidget(scroll_widget)
        layout.addWidget(scroll)
        
        back_btn = QPushButton("Назад")
        back_btn.clicked.connect(self.show_main_menu)
        layout.addWidget(back_btn)
    
    def handle_period_selection(self, period_num):
        rulers_map = {
            1: kiev_rulers,
            2: vladimir_rulers, 
            3: moscow_rulers,
            5: romanov_rulers,
            6: soviet_rulers,
            7: rf_rulers
        }
        
        if period_num == 4:
            QMessageBox.information(self, "Информация", "Раздел в разработке...")
            return
        
        if period_num in rulers_map:
            self.show_rulers(rulers_map[period_num], periods[period_num-1])
        else:
            QMessageBox.critical(self, "Ошибка", "Неверный выбор периода")
    
    def show_rulers(self, rulers_list, period_name):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)
        
        title = QLabel(f"{period_name}\nВыберите правителя:")
        title.setFont(QFont("Arial", 14, QFont.Bold))
        layout.addWidget(title)
        
        self.rulers_list = rulers_list
        self.list_widget = QListWidget()
        
        # Используем цикл for для заполнения списка
        for name, years, _ in rulers_list:
            self.list_widget.addItem(f"{name} ({years})")
        
        layout.addWidget(self.list_widget)
        
        btn_layout = QHBoxLayout()
        info_btn = QPushButton("Показать информацию")
        info_btn.clicked.connect(self.show_ruler_info)
        back_btn = QPushButton("Назад")
        back_btn.clicked.connect(self.show_periods)
        
        btn_layout.addWidget(info_btn)
        btn_layout.addWidget(back_btn)
        layout.addLayout(btn_layout)
    
    def show_ruler_info(self):
        current_row = self.list_widget.currentRow()
        if current_row == -1:
            QMessageBox.warning(self, "Предупреждение", "Выберите правителя из списка")
            return
        
        ruler_name, years, attr_name = self.rulers_list[current_row]
        
        if hasattr(istorya, attr_name):
            info = getattr(istorya, attr_name)
            self.show_info_window(ruler_name, years, info)
        else:
            QMessageBox.critical(self, "Ошибка", f"Информация о {ruler_name} не найдена")
    
    def show_info_window(self, name, years, info):
        info_window = QMainWindow(self)
        info_window.setWindowTitle(name)
        info_window.setGeometry(150, 150, 700, 500)
        
        central_widget = QWidget()
        info_window.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)
        
        title = QLabel(name)
        title.setFont(QFont("Arial", 16, QFont.Bold))
        layout.addWidget(title)
        
        years_label = QLabel(f"Годы правления: {years}")
        years_label.setFont(QFont("Arial", 12, QFont.Bold))
        layout.addWidget(years_label)
        
        text_edit = QTextEdit()
        text_edit.setPlainText(info)
        text_edit.setReadOnly(True)
        layout.addWidget(text_edit)
        
        close_btn = QPushButton("Закрыть")
        close_btn.clicked.connect(info_window.close)
        layout.addWidget(close_btn)
        
        info_window.show()
    
    def show_church_figures(self):
        QMessageBox.information(self, "Информация", "Церковные личности - раздел в разработке...")
    
    def show_date_search(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)
        
        title = QLabel("Поиск по дате")
        title.setFont(QFont("Arial", 14, QFont.Bold))
        layout.addWidget(title)
        
        instruction = QLabel("Введите год:")
        layout.addWidget(instruction)
        
        self.year_entry = QLineEdit()
        layout.addWidget(self.year_entry)
        
        btn_layout = QHBoxLayout()
        search_btn = QPushButton("Искать")
        search_btn.clicked.connect(self.search_date)
        back_btn = QPushButton("Назад")
        back_btn.clicked.connect(self.show_main_menu)
        
        btn_layout.addWidget(search_btn)
        btn_layout.addWidget(back_btn)
        layout.addLayout(btn_layout)
    
    def search_date(self):
        year = self.year_entry.text()
        if year.isdigit():
            QMessageBox.information(self, "Поиск", f"Поиск событий за {year} год...\nФункция в разработке...")
        else:
            QMessageBox.critical(self, "Ошибка", "Введите корректный год")
    
    def show_unknown_terms(self):
        QMessageBox.information(self, "Информация", "Словарь терминов - раздел в разработке...")
    
    def show_contemporaries(self):
        QMessageBox.information(self, "Информация", "Поиск современников - раздел в разработке...")

def main():
    app = QApplication(sys.argv)
    window = HistoryApp()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
import istorya
import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, 
                            QPushButton, QLabel, QListWidget, QTextEdit, 
                            QMessageBox, QLineEdit, QHBoxLayout, QScrollArea,
                            QTableWidget, QTableWidgetItem, QHeaderView)
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

# Данные для поиска по дате (пример)
historical_events = {
    "862": "Призвание варягов и начало правления Рюрика",
    "882": "Объединение Киева и Новгорода под властью Олега",
    "988": "Крещение Руси князем Владимиром",
    "1147": "Первое упоминание Москвы в летописи",
    "1242": "Ледовое побоище - победа Александра Невского",
    "1380": "Куликовская битва - победа Дмитрия Донского",
    "1480": "Стояние на Угре - конец монголо-татарского ига",
    "1547": "Венчание Ивана IV на царство",
    "1613": "Избрание Михаила Романова на царство",
    "1703": "Основание Санкт-Петербурга",
    "1812": "Отечественная война с Наполеоном",
    "1861": "Отмена крепостного права",
    "1917": "Февральская и Октябрьская революции",
    "1945": "Победа в Великой Отечественной войне",
    "1991": "Распад СССР и создание Российской Федерации"
}

# Словарь терминов
historical_terms = {
    "Варяги": "Скандинавские воины-купцы, приглашенные на Русь в 862 году",
    "Вече": "Народное собрание в древней Руси для решения важных вопросов",
    "Дружина": "Княжеское войско в Древней Руси",
    "Удел": "Часть княжества, выделенная одному из младших членов правящей династии",
    "Бояре": "Высший слой феодалов в древней Руси",
    "Поместье": "Земельное владение, даваемое за военную службу",
    "Опричнина": "Политика террора, проводимая Иваном Грозным",
    "Самодержавие": "Форма правления с неограниченной властью монарха",
    "Сенат": "Высший орган государственной власти в Российской империи",
    "Коллегии": "Центральные органы управления в России XVIII века",
    "Земство": "Орган местного самоуправления в Российской империи",
    "Дума": "Законодательное собрание в России"
}

# Церковные личности
church_figures = [
    ("Владимир I Святой", "Князь, креститель Руси", "978-1015"),
    ("Ольга Святая", "Первая христианская правительница Руси", "945-964"),
    ("Митрополит Иларион", "Первый русский митрополит, автор 'Слова о Законе и Благодати'", "1051-1054"),
    ("Сергий Радонежский", "Основатель Троице-Сергиевой лавры, благословил Дмитрия Донского", "1314-1392"),
    ("Митрополит Алексий", "Фактический правитель Руси при малолетнем Дмитрии Донском", "1354-1378"),
    ("Патриарх Никон", "Провел церковную реформу, приведшую к расколу", "1652-1666"),
    ("Протопоп Аввакум", "Лидер старообрядцев, противник реформ Никона", "1620-1682"),
    ("Иоанн Кронштадтский", "Известный проповедник и духовный писатель", "1829-1908")
]

# Современники (примеры)
contemporaries_data = {
    "Петр I": ["Карл XII (Швеция)", "Август II Сильный (Польша)", "Екатерина I"],
    "Екатерина II": ["Фридрих II (Пруссия)", "Мария-Терезия (Австрия)", "Вольтер", "Дидро"],
    "Александр I": ["Наполеон Бонапарт", "М.И. Кутузов", "Михаил Сперанский"],
    "Николай II": ["В.И. Ленин", "Григорий Распутин", "П.А. Столыпин"]
}

class HistoryApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Справочник исторических личностей")
        self.setGeometry(100, 100, 900, 700)
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
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)
        
        title = QLabel("Церковные личности в истории России")
        title.setFont(QFont("Arial", 16, QFont.Bold))
        title.setAlignment(Qt.AlignCenter)
        layout.addWidget(title)
        
        # Создаем таблицу для отображения церковных деятелей
        table = QTableWidget()
        table.setColumnCount(3)
        table.setHorizontalHeaderLabels(["Имя", "Деятельность", "Годы жизни"])
        
        # Заполняем таблицу данными
        table.setRowCount(len(church_figures))
        for i, (name, activity, years) in enumerate(church_figures):
            table.setItem(i, 0, QTableWidgetItem(name))
            table.setItem(i, 1, QTableWidgetItem(activity))
            table.setItem(i, 2, QTableWidgetItem(years))
        
        # Настраиваем внешний вид таблицы
        table.horizontalHeader().setSectionResizeMode(0, QHeaderView.ResizeToContents)
        table.horizontalHeader().setSectionResizeMode(1, QHeaderView.Stretch)
        table.horizontalHeader().setSectionResizeMode(2, QHeaderView.ResizeToContents)
        table.setSortingEnabled(True)
        
        layout.addWidget(table)
        
        back_btn = QPushButton("Назад")
        back_btn.clicked.connect(self.show_main_menu)
        layout.addWidget(back_btn)

    def show_date_search(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)
        
        title = QLabel("Поиск исторических событий по дате")
        title.setFont(QFont("Arial", 16, QFont.Bold))
        title.setAlignment(Qt.AlignCenter)
        layout.addWidget(title)
        
        instruction = QLabel("Введите год (от 800 до 2024):")
        instruction.setFont(QFont("Arial", 12))
        layout.addWidget(instruction)
        
        self.year_entry = QLineEdit()
        self.year_entry.setPlaceholderText("Например: 1812, 1945...")
        self.year_entry.setFont(QFont("Arial", 12))
        layout.addWidget(self.year_entry)
        
        search_btn = QPushButton("Найти события")
        search_btn.setFont(QFont("Arial", 12))
        search_btn.clicked.connect(self.search_date)
        layout.addWidget(search_btn)
        
        self.result_label = QLabel("")
        self.result_label.setFont(QFont("Arial", 11))
        self.result_label.setWordWrap(True)
        layout.addWidget(self.result_label)
        
        # Показываем примеры дат
        examples_label = QLabel("Примеры дат для поиска: 862, 988, 1147, 1242, 1380, 1480, 1703, 1812, 1917, 1945")
        examples_label.setFont(QFont("Arial", 10))
        examples_label.setStyleSheet("color: gray;")
        layout.addWidget(examples_label)
        
        back_btn = QPushButton("Назад")
        back_btn.clicked.connect(self.show_main_menu)
        layout.addWidget(back_btn)

    def search_date(self):
        year = self.year_entry.text()
        if year.isdigit() and 800 <= int(year) <= 2024:
            if year in historical_events:
                event = historical_events[year]
                self.result_label.setText(f"📅 {year} год:\n{event}")
                self.result_label.setStyleSheet("color: green; font-weight: bold;")
            else:
                self.result_label.setText(f"Для {year} года события не найдены в базе данных.\nПопробуйте другую дату.")
                self.result_label.setStyleSheet("color: orange;")
        else:
            self.result_label.setText("❌ Пожалуйста, введите корректный год от 800 до 2024")
            self.result_label.setStyleSheet("color: red;")

    def show_unknown_terms(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)
        
        title = QLabel("Словарь исторических терминов")
        title.setFont(QFont("Arial", 16, QFont.Bold))
        title.setAlignment(Qt.AlignCenter)
        layout.addWidget(title)
        
        instruction = QLabel("Выберите термин для просмотра определения:")
        instruction.setFont(QFont("Arial", 12))
        layout.addWidget(instruction)
        
        # Создаем список терминов
        self.terms_list = QListWidget()
        for term in historical_terms.keys():
            self.terms_list.addItem(term)
        layout.addWidget(self.terms_list)
        
        # Область для отображения определения
        self.definition_text = QTextEdit()
        self.definition_text.setReadOnly(True)
        self.definition_text.setPlaceholderText("Выберите термин из списка чтобы увидеть его определение...")
        layout.addWidget(self.definition_text)
        
        # Подключаем выбор элемента списка
        self.terms_list.currentItemChanged.connect(self.show_term_definition)
        
        back_btn = QPushButton("Назад")
        back_btn.clicked.connect(self.show_main_menu)
        layout.addWidget(back_btn)

    def show_term_definition(self, current, previous):
        if current:
            term = current.text()
            definition = historical_terms.get(term, "Определение не найдено")
            self.definition_text.setText(f"📚 {term}:\n\n{definition}")

    def show_contemporaries(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)
        
        title = QLabel("Исторические современники")
        title.setFont(QFont("Arial", 16, QFont.Bold))
        title.setAlignment(Qt.AlignCenter)
        layout.addWidget(title)
        
        instruction = QLabel("Выберите историческую личность чтобы увидеть её современников:")
        instruction.setFont(QFont("Arial", 12))
        layout.addWidget(instruction)
        
        # Создаем список личностей
        self.person_list = QListWidget()
        for person in contemporaries_data.keys():
            self.person_list.addItem(person)
        layout.addWidget(self.person_list)
        
        # Область для отображения современников
        self.contemporaries_text = QTextEdit()
        self.contemporaries_text.setReadOnly(True)
        self.contemporaries_text.setPlaceholderText("Выберите историческую личность из списка...")
        layout.addWidget(self.contemporaries_text)
        
        # Подключаем выбор элемента списка
        self.person_list.currentItemChanged.connect(self.show_contemporaries_list)
        
        back_btn = QPushButton("Назад")
        back_btn.clicked.connect(self.show_main_menu)
        layout.addWidget(back_btn)

    def show_contemporaries_list(self, current, previous):
        if current:
            person = current.text()
            contemporaries = contemporaries_data.get(person, [])
            if contemporaries:
                text = f"👥 {person} был современником:\n\n"
                for contemporary in contemporaries:
                    text += f"• {contemporary}\n"
                self.contemporaries_text.setText(text)
            else:
                self.contemporaries_text.setText(f"Информация о современниках {person} не найдена.")

def main():
    app = QApplication(sys.argv)
    window = HistoryApp()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
from PyQt5 import QtCore, QtWidgets

import splitter


class Ui:
    def __init__(self, main_window):
        # main window elements
        self.main_window = main_window
        self.central_widget = QtWidgets.QWidget(self.main_window)
        self.status_bar = QtWidgets.QStatusBar(self.main_window)
        self.setup_main_window()

        # input output elements
        self.line_edit_input = QtWidgets.QLineEdit(self.central_widget)
        self.button_input = QtWidgets.QPushButton(self.central_widget)
        self.line_edit_output = QtWidgets.QLineEdit(self.central_widget)
        self.button_output = QtWidgets.QPushButton(self.central_widget)
        self.setup_input_output()

        # scroll area elements
        self.scroll_area = QtWidgets.QScrollArea(self.central_widget)
        self.scroll_area_widget_contents = QtWidgets.QWidget()
        self.gridLayout = QtWidgets.QGridLayout(self.scroll_area_widget_contents)
        self.setup_scroll_area()

        # arrays making reference to ui elements
        self.line_e_section_arr = []
        self.line_e_begin_doc_arr = []
        self.line_e_end_doc_arr = []
        self.line_e_name_doc_arr = []
        self.setup_dynamic_docs_area()

        # buttons to add or remove elements dynamically
        self.button_add = QtWidgets.QPushButton(self.central_widget)
        self.button_remove = QtWidgets.QPushButton(self.central_widget)
        self.button_reset = QtWidgets.QPushButton(self.central_widget)
        self.setup_dynamic_buttons()

        # preview area elements
        self.label_preview = QtWidgets.QLabel(self.central_widget)
        self.button_previous = QtWidgets.QPushButton(self.central_widget)
        self.current_page = QtWidgets.QLineEdit(self.central_widget)
        self.label_separator = QtWidgets.QLabel(self.central_widget)
        self.last_page = QtWidgets.QLineEdit(self.central_widget)
        self.button_next = QtWidgets.QPushButton(self.central_widget)
        self.setup_preview()

        self.progress_bar = QtWidgets.QProgressBar(self.central_widget)
        self.setup_progress_bar()

        self.button_start = QtWidgets.QPushButton(self.central_widget)
        self.setup_button_start()

        # setting docs
        self.reset_docs()

        # connecting ui to backend
        # input output
        self.button_input.clicked.connect(self.select_file)
        self.button_output.clicked.connect(self.select_folder)

        # add or remove dynamically
        self.button_add.clicked.connect(self.add_doc_fields)
        self.button_remove.clicked.connect(self.remove_doc_fields)
        self.button_reset.clicked.connect(self.reset_docs)

        # preview
        self.button_previous.clicked.connect(self.load_previous_page)
        self.button_next.clicked.connect(self.load_next_page)

        # start
        self.button_start.clicked.connect(self.split)

    def setup_main_window(self):
        self.main_window.resize(800, 600)
        self.main_window.setMinimumSize(QtCore.QSize(800, 600))
        self.main_window.setMaximumSize(QtCore.QSize(800, 600))
        self.main_window.setCentralWidget(self.central_widget)
        self.main_window.setStatusBar(self.status_bar)

    def setup_input_output(self):
        self.line_edit_input.setGeometry(QtCore.QRect(20, 30, 270, 25))
        self.line_edit_input.setMinimumSize(QtCore.QSize(270, 25))
        self.line_edit_input.setMaximumSize(QtCore.QSize(270, 25))
        self.line_edit_input.setToolTip('caminho para o pdf')

        self.button_input.setGeometry(QtCore.QRect(300, 30, 75, 25))
        self.button_input.setMinimumSize(QtCore.QSize(75, 25))
        self.button_input.setMaximumSize(QtCore.QSize(75, 25))
        self.button_input.setText('select file')
        self.button_input.setToolTip('selecionar pdf')

        self.line_edit_output.setGeometry(QtCore.QRect(20, 65, 270, 25))
        self.line_edit_output.setMinimumSize(QtCore.QSize(270, 25))
        self.line_edit_output.setMaximumSize(QtCore.QSize(270, 25))
        self.line_edit_output.setToolTip('pasta onde o pdf será salvo')

        self.button_output.setGeometry(QtCore.QRect(300, 65, 75, 25))
        self.button_output.setMinimumSize(QtCore.QSize(75, 25))
        self.button_output.setMaximumSize(QtCore.QSize(75, 25))
        self.button_output.setText('select folder')
        self.button_output.setToolTip('selecionar pasta destino')

    def setup_button_start(self):
        self.button_start.setGeometry(QtCore.QRect(380, 550, 50, 25))
        self.button_start.setMinimumSize(QtCore.QSize(50, 25))
        self.button_start.setMaximumSize(QtCore.QSize(50, 25))
        self.button_start.setText('start')
        self.button_start.setToolTip('separar pdf')

    def setup_progress_bar(self):
        self.progress_bar.setGeometry(QtCore.QRect(240, 520, 350, 20))
        self.progress_bar.setMinimumSize(QtCore.QSize(350, 20))
        self.progress_bar.setMaximumSize(QtCore.QSize(350, 20))
        self.progress_bar.setValue(0)

    def setup_scroll_area(self):
        self.scroll_area.setGeometry(QtCore.QRect(20, 110, 350, 370))
        self.scroll_area.setMinimumSize(QtCore.QSize(350, 370))
        self.scroll_area.setMaximumSize(QtCore.QSize(350, 370))
        self.scroll_area.setWidgetResizable(True)
        self.scroll_area_widget_contents.setGeometry(QtCore.QRect(0, 0, 350, 370))
        self.scroll_area.setWidget(self.scroll_area_widget_contents)

    def setup_dynamic_docs_area(self):
        for i in range(0, 12):
            self.line_e_section_arr.append(QtWidgets.QLineEdit(self.scroll_area_widget_contents))
            self.line_e_section_arr[-1].setMinimumSize(QtCore.QSize(25, 25))
            self.line_e_section_arr[-1].setMaximumSize(QtCore.QSize(25, 25))
            self.line_e_section_arr[-1].setAlignment(QtCore.Qt.AlignCenter)
            self.line_e_section_arr[-1].setToolTip('seção do documento')

            self.gridLayout.addWidget(self.line_e_section_arr[-1], i, 0, 1, 1)

            self.line_e_begin_doc_arr.append(QtWidgets.QLineEdit(self.scroll_area_widget_contents))
            self.line_e_begin_doc_arr[-1].setMinimumSize(QtCore.QSize(25, 25))
            self.line_e_begin_doc_arr[-1].setMaximumSize(QtCore.QSize(25, 25))
            self.line_e_begin_doc_arr[-1].setAlignment(QtCore.Qt.AlignCenter)
            self.line_e_begin_doc_arr[-1].setToolTip('página inicial do documento')

            self.gridLayout.addWidget(self.line_e_begin_doc_arr[-1], i, 1, 1, 1)

            self.line_e_end_doc_arr.append(QtWidgets.QLineEdit(self.scroll_area_widget_contents))
            self.line_e_end_doc_arr[-1].setMinimumSize(QtCore.QSize(25, 25))
            self.line_e_end_doc_arr[-1].setMaximumSize(QtCore.QSize(25, 25))
            self.line_e_end_doc_arr[-1].setAlignment(QtCore.Qt.AlignCenter)
            self.line_e_end_doc_arr[-1].setToolTip('página final do documento')

            self.gridLayout.addWidget(self.line_e_end_doc_arr[-1], i, 2, 1, 1)

            self.line_e_name_doc_arr.append(QtWidgets.QLineEdit(self.scroll_area_widget_contents))
            self.line_e_name_doc_arr[-1].setMinimumSize(QtCore.QSize(215, 25))
            self.line_e_name_doc_arr[-1].setMaximumSize(QtCore.QSize(215, 25))
            self.line_e_name_doc_arr[-1].setToolTip('nome do documento')

            self.gridLayout.addWidget(self.line_e_name_doc_arr[-1], i, 3, 1, 1)

    def setup_dynamic_buttons(self):
        self.button_add.setGeometry(QtCore.QRect(20, 480, 25, 25))
        self.button_add.setMinimumSize(QtCore.QSize(25, 25))
        self.button_add.setMaximumSize(QtCore.QSize(25, 25))
        self.button_add.setText('+')
        self.button_add.setToolTip('adiciona novos campos')

        self.button_remove.setGeometry(QtCore.QRect(50, 480, 25, 25))
        self.button_remove.setMinimumSize(QtCore.QSize(25, 25))
        self.button_remove.setMaximumSize(QtCore.QSize(25, 25))
        self.button_remove.setText('-')
        self.button_remove.setToolTip('remove os últimos campos adicionados')

        self.button_reset.setGeometry(QtCore.QRect(320, 480, 50, 25))
        self.button_reset.setMinimumSize(QtCore.QSize(50, 25))
        self.button_reset.setMaximumSize(QtCore.QSize(50, 25))
        self.button_reset.setText('reset')
        self.button_reset.setToolTip('redefine os 12 primeiros campos')

    def setup_preview(self):
        self.label_preview.setGeometry(QtCore.QRect(410, 30, 360, 450))
        self.label_preview.setMinimumSize(QtCore.QSize(360, 450))
        self.label_preview.setMaximumSize(QtCore.QSize(360, 450))
        self.label_preview.setToolTip('preview do pdf')

        self.button_previous.setGeometry(QtCore.QRect(530, 480, 25, 25))
        self.button_previous.setMinimumSize(QtCore.QSize(25, 25))
        self.button_previous.setMaximumSize(QtCore.QSize(25, 25))
        self.button_previous.setText('<')
        self.button_previous.setToolTip('página anterior')

        self.last_page.setEnabled(False)
        self.last_page.setGeometry(QtCore.QRect(600, 480, 25, 25))
        self.last_page.setMinimumSize(QtCore.QSize(25, 25))
        self.last_page.setMaximumSize(QtCore.QSize(25, 25))
        self.last_page.setToolTip('última página')

        self.current_page.setGeometry(QtCore.QRect(560, 480, 25, 25))
        self.current_page.setMinimumSize(QtCore.QSize(25, 25))
        self.current_page.setMaximumSize(QtCore.QSize(25, 25))
        self.current_page.setToolTip('página atual')

        self.label_separator.setGeometry(QtCore.QRect(590, 480, 5, 25))
        self.label_separator.setMinimumSize(QtCore.QSize(5, 25))
        self.label_separator.setMaximumSize(QtCore.QSize(5, 25))
        self.label_separator.setAlignment(QtCore.Qt.AlignCenter)
        self.label_separator.setText('/')

        self.button_next.setGeometry(QtCore.QRect(630, 480, 25, 25))
        self.button_next.setMinimumSize(QtCore.QSize(25, 25))
        self.button_next.setMaximumSize(QtCore.QSize(25, 25))
        self.button_next.setText('>')
        self.button_next.setToolTip('próxima página')

    def select_file(self):
        splitter.select_file(self.line_edit_input, self.label_preview, self.current_page, self.last_page)

    def select_folder(self):
        splitter.select_folder(self.line_edit_output)

    def load_next_page(self):
        splitter.load_next_page(self.line_edit_input.text(), self.current_page, self.last_page, self.label_preview)

    def load_previous_page(self):
        splitter.load_previous_page(self.line_edit_input.text(), self.current_page, self.last_page, self.label_preview)

    def reset_docs(self):
        for i in range(0, len(self.line_e_section_arr)):
            if i == 0:
                self.line_e_section_arr[i].setText('1')
                self.line_e_name_doc_arr[i].setText('requerimento de matricula')
            elif i == 1:
                self.line_e_section_arr[i].setText('1')
                self.line_e_name_doc_arr[i].setText('contrato de prestação de serviço')
            elif i == 2:
                self.line_e_section_arr[i].setText('2')
                self.line_e_name_doc_arr[i].setText('certidão de nascimento')
            elif i == 3:
                self.line_e_section_arr[i].setText('2')
                self.line_e_name_doc_arr[i].setText('rg')
            elif i == 4:
                self.line_e_section_arr[i].setText('2')
                self.line_e_name_doc_arr[i].setText('cpf')
            elif i == 5:
                self.line_e_section_arr[i].setText('2')
                self.line_e_name_doc_arr[i].setText('titulo de eleitor')
            elif i == 6:
                self.line_e_section_arr[i].setText('2')
                self.line_e_name_doc_arr[i].setText('carteira de reservista')
            elif i == 7:
                self.line_e_section_arr[i].setText('2')
                self.line_e_name_doc_arr[i].setText('comprovante de residencia')
            elif i == 8:
                self.line_e_section_arr[i].setText('2')
                self.line_e_name_doc_arr[i].setText('declaração de quitação eleitoral')
            elif i == 9:
                self.line_e_section_arr[i].setText('3')
                self.line_e_name_doc_arr[i].setText('histórico escolar de ensino médio')
            elif i == 10:
                self.line_e_section_arr[i].setText('3')
                self.line_e_name_doc_arr[i].setText('certificado de conclusão de ensino médio')
            elif i == 11:
                self.line_e_section_arr[i].setText('4')
                self.line_e_name_doc_arr[i].setText('forma de ingresso')
            else:
                self.line_e_section_arr[i].setText('')
                self.line_e_name_doc_arr[i].setText('')

            self.line_e_begin_doc_arr[i].setText('')
            self.line_e_end_doc_arr[i].setText('')

        self.progress_bar.setValue(0)

    def add_doc_fields(self):
        splitter.add_doc_fields(self.line_e_section_arr, self.line_e_begin_doc_arr, self.line_e_end_doc_arr, self.line_e_name_doc_arr,
                                self.scroll_area_widget_contents, self.gridLayout)

    def remove_doc_fields(self):
        splitter.remove_doc_fields(self.line_e_section_arr, self.line_e_begin_doc_arr, self.line_e_end_doc_arr, self.line_e_name_doc_arr,
                                   self.scroll_area_widget_contents.layout())

    def split(self):
        splitter.split(self.line_edit_input.text(), self.line_edit_output.text(), self.line_e_section_arr, self.line_e_begin_doc_arr,
                       self.line_e_end_doc_arr, self.line_e_name_doc_arr, self.progress_bar)

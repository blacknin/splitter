import os
import re
import sys

import fitz
from PyQt5 import QtCore, QtGui, QtWidgets

import ui


def select_file(line_e_input, label_preview, line_e_current_page, line_e_last_page):
    file = QtWidgets.QFileDialog.getOpenFileName(QtWidgets.QFileDialog(), 'Select Pdf', '', 'pdf (*.pdf)')

    path = file[0]

    if is_valid_path(path):
        line_e_input.setText(path)
        load_preview(path, 0, label_preview, line_e_current_page, line_e_last_page)
    else:
        line_e_input.setText('')


def select_folder(line_e_output):
    path = QtWidgets.QFileDialog.getExistingDirectory(QtWidgets.QFileDialog(), 'Select Folder')

    if is_valid_path(path):
        line_e_output.setText(path)
    else:
        line_e_output.setText('')


def load_previous_page(path, line_e_current_page, line_e_last_page, label_preview):
    current_page = line_e_current_page.text()
    last_page = line_e_last_page.text()

    if are_valid_pages(current_page, last_page):
        current_page = int(current_page)
        current_page -= 1
        last_page = int(last_page)

        if 0 < current_page <= last_page:
            line_e_current_page.setText(str(current_page))
        elif current_page <= 0:
            current_page = 1
            line_e_current_page.setText(str(current_page))
        elif current_page > last_page:
            current_page = last_page
            line_e_current_page.setText(str(last_page))

        load_preview(path, current_page - 1, label_preview, line_e_current_page, line_e_last_page)


def load_next_page(path_pdf, line_e_current_page, line_e_last_page, label_preview):
    current_page = line_e_current_page.text()
    last_page = line_e_last_page.text()

    if are_valid_pages(current_page, last_page):
        current_page = int(current_page)
        current_page += 1
        last_page = int(last_page)

        if 0 < current_page < last_page:
            line_e_current_page.setText(str(current_page))
        elif current_page <= 0:
            current_page = 1
            line_e_current_page.setText(str(current_page))
        elif current_page > last_page:
            current_page = last_page
            line_e_current_page.setText(str(last_page))

        load_preview(path_pdf, current_page - 1, label_preview, line_e_current_page, line_e_last_page)


def load_preview(path_pdf, page_number, label_preview, line_e_current_page, line_e_last_page):
    pdf = fitz.open(path_pdf)

    page = pdf.loadPage(page_number)
    pix = page.getPixmap(alpha = False)
    fmt = QtGui.QImage.Format_RGBA8888 if pix.alpha else QtGui.QImage.Format_RGB888
    qt_img = QtGui.QImage(pix.samples, pix.width, pix.height, pix.stride, fmt)

    label_preview.setPixmap(QtGui.QPixmap.fromImage(qt_img))
    line_e_current_page.setText(str(page_number + 1))
    line_e_last_page.setText(str(pdf.pageCount))

    pdf.close()


def add_doc_fields(line_e_section_arr, line_e_begin_doc_arr, line_e_end_doc_arr, line_e_name_doc_arr, scroll_area_widget_contents, grid_layout):
    # sector
    line_e_section_arr.append(QtWidgets.QLineEdit(scroll_area_widget_contents))
    # begin page
    line_e_begin_doc_arr.append(QtWidgets.QLineEdit(scroll_area_widget_contents))
    # end page
    line_e_end_doc_arr.append(QtWidgets.QLineEdit(scroll_area_widget_contents))
    # doc name
    line_e_name_doc_arr.append(QtWidgets.QLineEdit(scroll_area_widget_contents))

    # sector
    line_e_section_arr[-1].setMinimumSize(QtCore.QSize(25, 25))
    line_e_section_arr[-1].setMaximumSize(QtCore.QSize(25, 25))
    line_e_section_arr[-1].setAlignment(QtCore.Qt.AlignCenter)

    # begin page
    line_e_begin_doc_arr[-1].setMinimumSize(QtCore.QSize(25, 25))
    line_e_begin_doc_arr[-1].setMaximumSize(QtCore.QSize(25, 25))
    line_e_begin_doc_arr[-1].setAlignment(QtCore.Qt.AlignCenter)

    # end page
    line_e_end_doc_arr[-1].setMinimumSize(QtCore.QSize(25, 25))
    line_e_end_doc_arr[-1].setMaximumSize(QtCore.QSize(25, 25))
    line_e_end_doc_arr[-1].setAlignment(QtCore.Qt.AlignCenter)

    # doc name
    line_e_name_doc_arr[-1].setMinimumSize(QtCore.QSize(215, 25))
    line_e_name_doc_arr[-1].setMaximumSize(QtCore.QSize(215, 25))

    row = len(line_e_section_arr)

    # sector
    grid_layout.addWidget(line_e_section_arr[-1], row, 0, 1, 1)
    # begin page
    grid_layout.addWidget(line_e_begin_doc_arr[-1], row, 1, 1, 1)
    # end page
    grid_layout.addWidget(line_e_end_doc_arr[-1], row, 2, 1, 1)
    # doc name
    grid_layout.addWidget(line_e_name_doc_arr[-1], row, 3, 1, 1)


def remove_doc_fields(line_e_section_arr, line_e_begin_doc_arr, line_e_end_doc_arr, line_e_name_doc_arr, scroll_area_widget_contents_layout):
    if len(line_e_section_arr) > 0:
        # sector
        scroll_area_widget_contents_layout.removeWidget(line_e_section_arr[-1])
        line_e_section_arr[-1].deleteLater()

        # begin page
        scroll_area_widget_contents_layout.removeWidget(line_e_begin_doc_arr[-1])
        line_e_begin_doc_arr[-1].deleteLater()

        # end page
        scroll_area_widget_contents_layout.removeWidget(line_e_end_doc_arr[-1])
        line_e_end_doc_arr[-1].deleteLater()

        # doc name
        scroll_area_widget_contents_layout.removeWidget(line_e_name_doc_arr[-1])
        line_e_name_doc_arr[-1].deleteLater()

        line_e_section_arr.pop()
        line_e_begin_doc_arr.pop()
        line_e_end_doc_arr.pop()
        line_e_name_doc_arr.pop()


def split(input_path, output_path, line_e_section_arr, line_e_begin_doc_arr, line_e_end_doc_arr, line_e_name_doc_arr, progress_bar):
    progress_bar.setValue(0)

    if is_valid_path(input_path) and is_valid_path(output_path):
        # create array from input path
        dest_folder = input_path.split('/')
        # get file with extension
        dest_folder = dest_folder[-1]
        # remove .pdf extension
        dest_folder = dest_folder[:-4]
        # path to new folder where pdf will be saved in
        dest_folder = output_path + '/' + dest_folder

        if not os.path.exists(dest_folder):
            os.mkdir(dest_folder)

        increment = 100 / len(line_e_section_arr)
        percentage = 0

        for i in range(0, len(line_e_section_arr)):
            if not split_doc(input_path, dest_folder, line_e_section_arr[i].text(), line_e_begin_doc_arr[i].text(), line_e_end_doc_arr[i].text(),
                             line_e_name_doc_arr[i].text()):
                print(f'warning - Faltando argumentos no {i}º documento')

            percentage += increment
            progress_bar.setValue(percentage)

        progress_bar.setValue(100)


def is_valid_section(section_txt):
    if re.match(r"-?[0-9]+", section_txt):
        return True
    else:
        return False


def split_doc(input_path, dest_folder, section_str, begin_page_str, end_page_str, doc_name):
    if is_valid_path(input_path) and is_valid_path(dest_folder) and are_valid_pages(begin_page_str, end_page_str) and is_valid_section(section_str):
        begin_page_str = int(begin_page_str)
        end_page_str = int(end_page_str)

        doc_name = replace_invalid_chars(doc_name)

        pdf_a = dest_folder + '/' + section_str + '_' + doc_name + '.pdf'
        pdf = dest_folder + '/' + section_str + '_' + doc_name + '_not_pdf_a.pdf'

        if not os.path.exists(dest_folder):
            os.mkdir(dest_folder)

        begin_page_str -= 1
        end_page_str -= 1

        document_1 = fitz.open(input_path)
        document_2 = fitz.open()

        document_2.insertPDF(document_1, from_page = begin_page_str, to_page = end_page_str)

        document_2.save(pdf)

        document_1.close()
        document_2.close()

        gs_path = 'C:/splitter/dependencies/gs9.20/bin/gswin32c'
        pdf_a_def_path = 'C:/splitter/dependencies/PDFA_def.ps'
        gs_args = f'-dPDFA -dNOOUTERSAVE -sProcessColorModel=DeviceRGB -dUseCIEColor -sDEVICE=pdfwrite -o {pdf_a} -dPDFACompatibilityPolicy=1 {pdf_a_def_path}'

        os.system(f'{gs_path} {gs_args} {pdf}')

        os.remove(pdf)

        return True

    else:
        return False


def replace_invalid_chars(name):
    name = name.replace(' ', '_')
    name = name.replace('ç', 'c')
    name = name.replace('ã', 'a')
    name = name.replace('õ', 'o')
    name = name.replace('á', 'a')
    name = name.replace('é', 'e')
    name = name.replace('í', 'i')
    name = name.replace('ó', 'o')
    name = name.replace('ú', 'u')
    name = name.upper()

    return name


def are_valid_pages(begin_page_txt, end_page_txt):
    if begin_page_txt is not None and end_page_txt is not None:
        if re.match(r"-?[0-9]+", begin_page_txt) and re.match(r"-?[0-9]+", end_page_txt):
            begin_page_txt = int(begin_page_txt)
            end_page_txt = int(end_page_txt)

            if 0 < begin_page_txt <= end_page_txt:
                return True
            else:
                return False
        else:
            return False
    else:
        return False


def is_valid_path(path):
    if path is not None and path != '':
        if " " in path:
            error_dialog = QtWidgets.QMessageBox()
            error_dialog.setWindowTitle('Error')
            error_dialog.setText('Arquivo não pode conter espaço em branco no nome')
            error_dialog.setStandardButtons(QtWidgets.QMessageBox.Ok | QtWidgets.QMessageBox.Cancel)
            error_dialog.exec_()
            return False
        else:
            return True
    else:
        return False


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    main_window = QtWidgets.QMainWindow()
    ui = ui.Ui(main_window)
    main_window.setWindowTitle('splitter')
    main_window.show()
    sys.exit(app.exec_())

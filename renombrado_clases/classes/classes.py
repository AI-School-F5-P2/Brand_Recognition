import os
import re
import shutil
from forms.ui_main import Ui_MainWindow
from PySide6.QtWidgets import QMainWindow, QFileDialog, QMessageBox

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setup_connections()  # Establece las conexiones de señales y slots
        # Las variables de los comboboxes
        self.ClaseAntigua = None
        self.ClaseNueva = None

    def select_labels_directory(self):
        # Restablecer el estado inicial antes de seleccionar un nuevo directorio
        self.reset_ui_elements()

        directory = QFileDialog.getExistingDirectory(self, "Seleciona el directorio de etiquetas")
        if directory:  # Verifica si el usuario ha seleccionado un directorio
            self.ui.labelsDir.setText(directory)  # Actualiza el QLineEdit con la ruta seleccionada
            self.ui.labelsDir.setReadOnly(True)  # Asegura que el QLineEdit sea de solo lectura
            if not self.validate_labels_directory():
                self.ui.labelsDir.clear()  # Limpia el QLineEdit si la validación falla

    def setup_connections(self):
        # Conectar el botón para seleccionar el directorio de etiquetas
        self.ui.SelectLabelsDir.clicked.connect(self.select_labels_directory)
        # Poner los valores de los comboboxes en las variables.
        self.ui.OrigenComboBox.currentIndexChanged.connect(self.update_old_class)
        self.ui.DestinoComboBox.currentIndexChanged.connect(self.update_new_class)
        # Cambiar las clases en las etiquetas
        self.ui.cambiarButton.clicked.connect(self.change_classes_in_labels)

    ### VALIDACIÓN DEL DIRECTORIO DE LABELS ESCOGIDO
    def validate_labels_directory(self):
        directory = self.ui.labelsDir.text()
        if not directory:
            return False

        # Eliminar .DS_Store y __pycache__ si existen
        self.remove_unwanted_files(directory, ['.DS_Store', '__pycache__'])

        # Verificar la existencia de labels.txt
        if not os.path.exists(os.path.join(directory, 'labels.txt')):
            self.show_error_message("El archivo labels.txt no se encuentra en el directorio seleccionado.")
            self.ui.labelsDir.clear()
            return False

        # Obtener todos los archivos en el directorio
        all_files = os.listdir(directory)

        # Verificar si hay archivos que no son de etiquetas y no permitidos
        non_label_files = [f for f in all_files if not (f.endswith('.txt') or f in ['labels.txt', '.DS_Store'])]
        if non_label_files:
            self.show_error_message("Hay archivos no permitidos en el directorio: " + ", ".join(non_label_files))
            self.ui.labelsDir.clear()
            return False

        # Verificar la existencia de archivos .txt de etiquetas
        label_files = [f for f in all_files if f.endswith('.txt') and f != 'labels.txt']
        if not label_files:
            self.show_error_message("No se encontraron archivos de etiquetas en el directorio seleccionado.")
            self.ui.labelsDir.clear()
            return False

        # Validar el formato de los archivos de etiquetas
        for label_file in label_files:
            if not self.validate_label_format(os.path.join(directory, label_file)):
                self.show_error_message(f"Formato inválido en el archivo de etiquetas: {label_file}")
                self.ui.labelsDir.clear()
                return False

        # Cargar etiquetas a los comboboxes después de las validaciones exitosas
        self.load_labels_to_comboboxes()

        # Todo es correcto
        return True

    def validate_label_format(self, file_path):
        try:
            with open(file_path, 'r') as file:
                for line in file:
                    parts = line.strip().split()
                    # Verificar que hay 5 partes y que la primera es un dígito y las restantes son flotantes
                    if len(parts) != 5 or not parts[0].isdigit() or not all(self.is_float(part) for part in parts[1:]):
                        return False
            return True
        except Exception as e:
            print(f"Error al leer el archivo {file_path}: {e}")
            return False

    def is_float(self, string):
        try:
            float(string)
            return True
        except ValueError:
            return False

    def remove_unwanted_files(self, directory, unwanted_items):
        for item in unwanted_items:
            path = os.path.join(directory, item)
            if os.path.exists(path):
                if os.path.isfile(path):
                    os.remove(path)  # Eliminar el archivo
                elif os.path.isdir(path):
                    shutil.rmtree(path)  # Eliminar el directorio de forma recursiva

    def show_error_message(self, message):
        QMessageBox.warning(self, "Error de Validación", message)
    ### FIN DE LA VALIDACIÓN DEL DIRECTORIO DE LABELS ESCOGIDO

    #### ESTABLECER LOS COMBOBOXES
    def load_labels_to_comboboxes(self):
        directory = self.ui.labelsDir.text()
        labels_file_path = os.path.join(directory, 'labels.txt')
        
        if os.path.exists(labels_file_path):
            with open(labels_file_path, 'r') as file:
                labels = file.read().splitlines()

            # Comprobar si hay solo una clase en el archivo labels.txt
            if len(labels) <= 1:
                self.show_error_message("El archivo labels.txt debe contener más de una clase.")
                self.ui.labelsDir.clear()
                return False

            self.ui.OrigenComboBox.clear()
            self.ui.DestinoComboBox.clear()

            for index, label in enumerate(labels):
                item_text = f"({index}) {label}"
                self.ui.OrigenComboBox.addItem(item_text)
                self.ui.DestinoComboBox.addItem(item_text)

            self.ui.OrigenComboBox.setEnabled(True)
            self.ui.DestinoComboBox.setEnabled(True)
            return True
        return False

    def update_old_class(self, index):
        self.ClaseAntigua = index
        self.check_comboboxes_and_toggle_button()

    def update_new_class(self, index):
        self.ClaseNueva = index
        self.check_comboboxes_and_toggle_button()

    ### RESETEAR LOS ELEMENTOS DE LA GUI
    def reset_ui_elements(self):
        self.ui.labelsDir.setText("")  # Actualiza el QLineEdit con la ruta seleccionada
        self.ui.labelsDir.setReadOnly(True)  # Asegura que el QLineEdit sea de solo lectura

        # Limpia y deshabilita los comboboxes
        self.ui.OrigenComboBox.clear()
        self.ui.OrigenComboBox.setEnabled(False)
        self.ui.DestinoComboBox.clear()
        self.ui.DestinoComboBox.setEnabled(False)

        # Restablece las variables a None
        self.ClaseAntigua = None
        self.ClaseNueva = None

        # Deshabilita el botón cambiarButton
        self.ui.cambiarButton.setEnabled(False)

    def check_comboboxes_and_toggle_button(self):
        # Habilita el botón si los índices seleccionados son diferentes
        if self.ClaseAntigua is not None and self.ClaseNueva is not None and self.ClaseAntigua != self.ClaseNueva:
            self.ui.cambiarButton.setEnabled(True)
        else:
            self.ui.cambiarButton.setEnabled(False)

    #### Cambio de indice en las etiquetas.
    def change_classes_in_labels(self):
        directory = self.ui.labelsDir.text()
        label_files = [f for f in os.listdir(directory) if f.endswith('.txt') and f != 'labels.txt']

        for label_file in label_files:
            self.modify_label_file(os.path.join(directory, label_file))

        # Mostrar mensaje modal al finalizar
        QMessageBox.information(self, "Cambio Completado", "El cambio de clases se ha completado con éxito.")
        # Restablecer la interfaz de usuario a su estado inicial
        self.reset_ui_elements()

    def modify_label_file(self, file_path):
        with open(file_path, 'r') as file:
            lines = file.readlines()

        with open(file_path, 'w') as file:
            for line in lines:
                parts = line.strip().split()
                if len(parts) == 5 and parts[0].isdigit():
                    class_id = int(parts[0])
                    if class_id == self.ClaseAntigua:
                        parts[0] = str(self.ClaseNueva)
                file.write(' '.join(parts) + '\n')



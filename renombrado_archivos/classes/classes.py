import os
import re
from forms.ui_main import Ui_MainWindow
from PySide6.QtWidgets import QMainWindow, QFileDialog, QMessageBox

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setup_connections()

    def setup_connections(self):
        self.ui.ImagesDirSelect.clicked.connect(lambda: self.select_directory(self.ui.ImagesDirTextLine))
        self.ui.LabelsDirSelect.clicked.connect(lambda: self.select_directory(self.ui.LabesDirTextLine))
        # Nuevas conexiones para verificar los campos
        self.ui.ImagesDirTextLine.textChanged.connect(self.check_inputs_and_toggle_button)
        self.ui.LabesDirTextLine.textChanged.connect(self.check_inputs_and_toggle_button)
        self.ui.prefixName.textChanged.connect(self.check_inputs_and_toggle_button)
        self.ui.DigitsSpin.valueChanged.connect(self.check_inputs_and_toggle_button)
        # Al pulsar el botón se ejecuta el renombrado
        self.ui.Renombrar.clicked.connect(self.rename_files)

    def reset_ui_controls(self):
        self.ui.ImagesDirTextLine.clear()
        self.ui.LabesDirTextLine.clear()
        self.ui.prefixName.clear()
        self.ui.DigitsSpin.setValue(1)

    def select_directory(self, line_edit):
        directory = QFileDialog.getExistingDirectory(self, "Select Directory")
        if directory:
            line_edit.setText(directory)

    def check_inputs_and_toggle_button(self):
        images_dir = self.ui.ImagesDirTextLine.text().strip()
        labels_dir = self.ui.LabesDirTextLine.text().strip()
        prefix = self.ui.prefixName.text().strip()
        digits = self.ui.DigitsSpin.value()

        # Activar el botón si todos los campos tienen contenido
        self.ui.Renombrar.setEnabled(bool(images_dir and labels_dir and prefix and digits))

    # Función para obtener la extensión del archivo
    def get_extension(self, file_name):
        return file_name.split('.')[-1]

    def rename_files(self):
        image_dir = self.ui.ImagesDirTextLine.text()
        label_dir = self.ui.LabesDirTextLine.text()
        prefix = self.ui.prefixName.text()
        num_digits = self.ui.DigitsSpin.value()

        # Lista de archivos en los directorios
        image_files = sorted([f for f in os.listdir(image_dir) if f.endswith(('.jpg', '.jpeg', '.png', '.bmp', '.gif', '.webp'))])
        # La función os.listdir(image_dir) obtiene una lista de todos los archivos en el directorio especificado.
        # La expresión f.endswith(...) se utiliza para filtrar esta lista, incluyendo solo los archivos que terminan con las extensiones de archivo dadas.
        # La función sorted(...) se usa para ordenar alfabéticamente los archivos resultantes.
        label_files = sorted([f for f in os.listdir(label_dir) if f.endswith('.txt') and f != 'labels.txt'])
        # Aquí, os.listdir(label_dir) lista los archivos en el directorio de etiquetas.
        # La condición f.endswith('.txt') y f != 'labels.txt' asegura que solo los archivos de texto (excepto 'labels.txt') sean incluidos.
        # La lista resultante también se ordena alfabéticamente.


        # Proceso de renombrado
        for i, file_name in enumerate(image_files, start = 1):
            # Nuevo nombre base
            new_base_name = f"{prefix}_{str(i).zfill(num_digits)}"

            # Renombrar imagen
            new_image_name = f"{new_base_name}.{self.get_extension(file_name)}"
            os.rename(os.path.join(image_dir, file_name), os.path.join(image_dir, new_image_name))

            # Renombrar etiqueta (si existe)
            label_name = re.sub(r'\.[^\.]+$', '.txt', file_name)
            if label_name in label_files:
                new_label_name = f"{new_base_name}.txt"
                label_path = os.path.join(label_dir, label_name)
                if os.path.exists(label_path):
                    os.rename(label_path, os.path.join(label_dir, new_label_name))

        # Eliminar archivos de etiquetas que no tienen una imagen correspondiente
        for label_file in label_files:
            if label_file == "labels.txt":
                continue  # Omite este archivo

            corresponding_image = re.sub(r'\.txt$', '', label_file)
            # Buscar la imagen correspondiente con cualquier extensión
            if not any(corresponding_image + '.' + ext == image_file for ext in ['jpg', 'jpeg', 'png'] for image_file in image_files):
                os.remove(os.path.join(label_dir, label_file))

        # Mostrar cuadro de diálogo al finalizar
        QMessageBox.information(self, "Renombrado Completado", "El proceso de renombrado ha finalizado.")

        # Restablecer los controles de la interfaz
        self.reset_ui_controls()




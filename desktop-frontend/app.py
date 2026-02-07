import sys
import requests
import pandas as pd
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QPushButton,
    QFileDialog, QLabel, QTableWidget, QTableWidgetItem
)
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

API_BASE = "http://127.0.0.1:8000/api/"
USERNAME = "jaysh"
PASSWORD = "Jassu2309!"


class App(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Chemical Equipment Visualizer")
        self.layout = QVBoxLayout()

        self.upload_btn = QPushButton("Upload CSV")
        self.upload_btn.clicked.connect(self.upload_csv)

        self.summary_label = QLabel("Summary will appear here")

        self.table = QTableWidget()

        self.figure = Figure()
        self.canvas = FigureCanvas(self.figure)

        self.layout.addWidget(self.upload_btn)
        self.layout.addWidget(self.summary_label)
        self.layout.addWidget(self.table)
        self.layout.addWidget(self.canvas)

        self.setLayout(self.layout)

    def upload_csv(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Open CSV", "", "CSV Files (*.csv)")
        if not file_path:
            return

        with open(file_path, 'rb') as f:
            response = requests.post(
                API_BASE + "upload/",
                files={'file': f},
                auth=(USERNAME, PASSWORD)
            )

        data = response.json()

        self.summary_label.setText(
            f"Total: {data['total_count']} | "
            f"Avg Flow: {data['avg_flowrate']:.2f} | "
            f"Avg Pressure: {data['avg_pressure']:.2f} | "
            f"Avg Temp: {data['avg_temperature']:.2f}"
        )

        self.plot_chart(data['type_distribution'])
        self.load_table(file_path)

    def plot_chart(self, dist):
        self.figure.clear()
        ax = self.figure.add_subplot(111)
        ax.bar(dist.keys(), dist.values())
        ax.set_title("Equipment Type Distribution")
        self.canvas.draw()

    def load_table(self, path):
        df = pd.read_csv(path)
        self.table.setRowCount(len(df))
        self.table.setColumnCount(len(df.columns))
        self.table.setHorizontalHeaderLabels(df.columns)

        for i in range(len(df)):
            for j in range(len(df.columns)):
                self.table.setItem(i, j, QTableWidgetItem(str(df.iloc[i, j])))


app = QApplication(sys.argv)
window = App()
window.show()
sys.exit(app.exec_())

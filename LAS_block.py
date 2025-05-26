import lasio


class LasToExcelConverter:
    def __init__(self, las_file):
        self.las_file = las_file
        self.dataframe = None

    def load_data(self):
        # Используем lasio для чтения LAS файла
        las = lasio.read(self.las_file)
        # Получаем таблицу данных ASCII в виде pandas DataFrame
        self.dataframe = las.df()

    def save_to_excel(self, excel_file):
        if self.dataframe is None:
            raise ValueError(
                "Data not loaded. Call load_data() before saving."
                )
        # Сохраняем DataFrame в Excel файл без индексов
        self.dataframe.to_excel(excel_file, index=False)


if __name__ == "__main__":
    # Пример использования класса
    converter = LasToExcelConverter("2409.las")
    converter.load_data()
    converter.save_to_excel("output.xlsx")

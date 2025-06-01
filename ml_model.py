import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix


class AsciiAnalyzer:
    def __init__(self, file_name):
        self.file_name = file_name
        self.data = pd.read_csv(file_name, sep='\t')    

    def prepare_data(self):
        X = self.data.iloc[:, :-1].values
        y = self.data.iloc[:, -1].values

        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=0.2,
            random_state=42
            )

        return X_train, X_test, y_train, y_test

    def train_model(self, X_train, y_train):
        model = RandomForestClassifier(n_estimators=100, random_state=42)

        # Обучите модель
        model.fit(X_train, y_train)

        return model

    def evaluate_model(self, model, X_test, y_test):
        # Предскажите значения для тестовой выборки
        y_pred = model.predict(X_test)

        # Оцените качество модели
        accuracy = accuracy_score(y_test, y_pred)
        report = classification_report(y_test, y_pred)
        matrix = confusion_matrix(y_test, y_pred)

        return accuracy, report, matrix

    def analyze(self):
        X_train, X_test, y_train, y_test = self.prepare_data()
        model = self.train_model(X_train, y_train)
        accuracy, report, matrix = self.evaluate_model(model, X_test, y_test)

        print(f'Точность модели: {accuracy}')
        print(f'Отчет о классификации:\n{report}')
        print(f'Матрица ошибок:\n{matrix}')


analyzer = AsciiAnalyzer('2409.ascii')
analyzer.analyze()

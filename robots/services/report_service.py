from datetime import timedelta, date
from django.utils import timezone
import openpyxl
from django.db.models import Count

from robots.models import Robot


class ReportsService:

    def generate_robots_report(self):

        # Получаем данные
        one_week_ago = timezone.now() - timedelta(weeks=1)

        data = Robot.objects.filter(created__gte=one_week_ago) \
                   .values('model', 'version') \
                   .annotate(count=Count('id'))

        # Создаем книгу
        wb = openpyxl.Workbook(write_only=True)

        # Добавляем листы по модели
        models = set(r['model'] for r in data)
        sheets = {m: wb.create_sheet(m) for m in models}

        # Заполняем данными
        for model, ws in sheets.items():

            ws.append(['Модель', 'Версия', 'Количество'])

            for row in data:
                if row['model'] == model:
                    ws.append([model, row['version'], row['count']])

        # Форматируем
        for ws in sheets.values():
            ws.column_dimensions['A'].width = 20
            ws.column_dimensions['B'].width = 10

        # Сохраняем
        wb.save('report.xlsx')

        # Читаем байты
        with open('report.xlsx', 'rb') as f:
            data = f.read()

        return data
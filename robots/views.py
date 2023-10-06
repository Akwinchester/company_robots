from django.contrib import messages
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.mixins import UserPassesTestMixin
from django.http import HttpResponse
from django.shortcuts import render, redirect

from datetime import date

from django.views.generic import FormView

from .forms import RobotForm

from .services.robot_service import RobotService
from .services.report_service import ReportsService


class RobotCreateView(UserPassesTestMixin, FormView):
    """
    View для создания нового робота
    """
    form_class = RobotForm
    template_name = 'create_robot.html'

    # def post(self, request):
    #     """
    #     Обрабатывает POST запрос на создание робота
    #     """
    #     robot_service = RobotService()
    #     if request.content_type == 'application/json':
    #         json_data = request.body
    #         robot_service.create_from_json(json_data)
    #         return HttpResponse('Робот успешно добавлен в БД.')
    #     else:
    #         return super().post(request)

    def form_valid(self, form):
        """
        Сохраняет данные формы в БД
        """
        robot_service = RobotService()
        robot_service.create_from_form(form.cleaned_data)
        messages.success(self.request, 'Робот успешно добавлен')
        return redirect('create_robot')

    def get(self, request):
        """
        Отдает страницу с формой
        """
        form = RobotForm
        return render(request, 'create_robot.html', {'form': form})

    def test_func(self):
        """
        Проверяет, что пользователь в группе технических специалистов
        """
        if self.request.user.groups.filter(name='Технические специалисты').exists():
            return True

        return False


def download_report(request):
    """
    Возвращает сгенерированный отчет в Excel
    """
    file = ReportsService().generate_robots_report()
    response = HttpResponse(file, content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = f'attachment; filename=report_{date.today()}.xlsx'
    return response


@user_passes_test(lambda u: check_user_group(u, 'Менеджмент'))
def get_report(request):
    """
    Отдает страницу для получения отчета
    """
    return render(request, template_name='get_report.html')


def check_user_group(user, group_name):
    """
    Проверяет, что пользователь состоит в указанной группе
    """
    if user.groups.filter(name=group_name).exists():
        return True

    return False
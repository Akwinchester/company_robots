import json
from datetime import timezone, datetime

from django.utils.timezone import make_aware

from robots.models import Robot


class RobotService:

    def create_robot(self, data):
        robot = Robot(**data)
        robot.clean_and_validate(data)
        robot.save()

    def create_from_json(self, json_data):
        data = json.loads(json_data.decode())

        created = make_aware(datetime.strptime(data['created'], '%Y-%m-%d %H:%M:%S'))
        data['created'] = created.isoformat()
        data['serial'] = data['model'] + '-' + data['version']
        self.create_robot(data)

    def create_from_form(self, data):
        data['model'] = data['serial'].split('-')[0]
        data['version'] = data['serial'].split('-')[1]
        data['created'] = str(data['created'])
        self.create_robot(data)

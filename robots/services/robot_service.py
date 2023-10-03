import json

from robots.models import Robot


class RobotService:

    def create_from_json(self, json_data):
       data = json.loads(json_data.decode())
       data['serial'] = data['model'] + '-' + data['version']

       robot = Robot(**data)
       robot.clean_and_validate(data)
       robot.save()



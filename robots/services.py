import json


class RobotService:

    def create_from_json(self, json_data):
       data = json.loads(json_data.decode())
       data['serial'] = data['model'] + '-' + data['version']
       return data

    def serialize_robot(self):
        return 'Ok'
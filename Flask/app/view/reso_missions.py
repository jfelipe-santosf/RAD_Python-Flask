from flask_restful import Resource, reqparse
from flask import jsonify
from app.models.missions import Missions

#ADD MISSION
args = reqparse.RequestParser()
args.add_argument('name', type=str)
args.add_argument('release_date', type=str)
args.add_argument('destination', type=str)
args.add_argument('mission_state', type=int)
args.add_argument('crew', type=str)
args.add_argument('payload', type=str)
args.add_argument('mission_duration', type=str)
args.add_argument('mission_cost', type=float)
args.add_argument('description', type=str)

#UPDATE MISSION
args_update = reqparse.RequestParser()
args_update.add_argument('id', type=int)
args_update.add_argument('release_date', type=str)
args_update.add_argument('destination', type=str)
args_update.add_argument('mission_state', type=int)
args_update.add_argument('crew', type=str)
args_update.add_argument('payload', type=str)
args_update.add_argument('mission_duration', type=str)
args_update.add_argument('mission_cost', type=float)
args_update.add_argument('description', type=str)

#DEL MISSION
args_delete = reqparse.RequestParser()
args_delete.add_argument('id', type=int)

#LIST BY ID
args_listid = reqparse.RequestParser()
args_listid.add_argument('id', type=int)

#LIST BY date range
args_list = reqparse.RequestParser()
args_list.add_argument('date_min', type=str)
args_list.add_argument('date_max', type=str)

class Index(Resource):
    def get(self):
        return jsonify("Bem vindo a aplicacao Flask")

class Missions_list(Resource):
    def get(self):
        try:
            mission = Missions.list_all(self)
            if mission:
                return mission
        except Exception as e:
                return jsonify({'status': 500, 'msg': f'{e}'}), 500

class MissionById(Resource):   
    def get(self):
            try:
                datas = args_listid.parse_args()
                mission = Missions.list_id(self, datas['id'])
                if mission:
                    return mission
            except Exception as e:
                return jsonify({'status': 500, 'msg': f'{e}'}), 500
            
class MissionByDate(Resource):
    def get(self):
        try:
            datas = args_list.parse_args()
            mission = Missions.list_by_date_range(self, datas['date_min'], datas['date_max'])
            if mission:
                return mission
        except Exception as e:
                return jsonify({'status': 500, 'msg': f'{e}'}), 500
            
class MissionDelete(Resource):
    def delete(self):
        try:
            datas = args_delete.parse_args()
            Missions.delete_mission(self, datas['id']) 
            return {"message": 'Product create successfully!'}, 200
        except Exception as e:
            return jsonify({'status':500,'msg':f'{e}'}), 500
        
class MissionUpdate(Resource):
    def put(self):
        try:
            datas = args_update.parse_args()
            Missions.update_mission(self, datas['id'], datas['release_date'], datas['destination'], datas['mission_state'], datas['crew'], datas['payload'], datas['mission_duration'], datas['mission_cost'], datas['description'])
            return {"message": 'Product update successfully!'}, 200
        except Exception as e:
            return jsonify({'status':500,'msg':f'{e}'}), 500
        
class MissionCreate(Resource):
    def post(self):
        try:
            datas = args.parse_args()
            Missions.save_mission(self, datas['name'], datas['release_date'], datas['destination'], datas['mission_state'], datas['crew'], datas['payload'], datas['mission_duration'], datas['mission_cost'], datas['description'])
            return {"message": 'Product create successfully!'}, 200
        except Exception as e:
            return jsonify({'status':500,'msg':f'{e}'}), 500
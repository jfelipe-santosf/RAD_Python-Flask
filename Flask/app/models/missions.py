from app import db
from datetime import datetime

class Missions(db.Model):
    __tablename__ = 'missions'
    __tableargs__ = {'sqlite_autoincrement': True}
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    release_date = db.Column(db.Date)
    destination = db.Column(db.String(255))
    mission_state = db.Column(db.Integer)
    crew = db.Column(db.String(255))
    payload = db.Column(db.String(255))
    mission_duration = db.Column(db.String)
    mission_cost = db.Column(db.Float)
    description = db.Column(db.String(255))

    def __init__(self, name, release_date, destination, mission_state, crew, payload, mission_duration, mission_cost, description):
        self.name = name
        self.release_date = release_date
        self.destination = destination
        self.mission_state = mission_state
        self.crew = crew
        self.payload = payload
        self.mission_duration = mission_duration
        self.mission_cost = mission_cost
        self.description = description

    def list_all(self):
        try:
            missions = db.session.query(Missions).all()
            missions_dict = [{'id': mission.id, 'name': mission.name, "release_date": mission.release_date.strftime('%d %m %Y'), 'destination': mission.destination, 'mission_state': mission.mission_state} for mission in missions]
            return missions_dict
        except Exception as e:
            print(e)
    
    def list_id(self, mission_id):
        try:
            missions = db.session.query(Missions).filter(Missions.id == mission_id).all()
            missions_dict = [{'id': mission.id, 'name': mission.name, "date": mission.release_date.strftime('%d %m %Y'), 'destination': mission.destination, 'state': mission.mission_state, 'crew': mission.crew, 'payload': mission.payload, "mission_duration": mission.mission_duration, "mission_cost": mission.mission_cost, "description": mission.description} for mission in missions]
            return missions_dict
        except Exception as e:
            print(e)

    def list_by_date_range(self, date_min, date_max):
        try:
            search_date_min = datetime.strptime(date_min, '%d %m %Y').date()
            search_date_max = datetime.strptime(date_max, '%d %m %Y').date()
            missions = db.session.query(Missions).filter(Missions.release_date >= search_date_min, Missions.release_date <= search_date_max).all()
            missions_dict = [{'id': mission.id, 'name': mission.name, "date": mission.release_date.strftime('%d %m %Y'), 'destination': mission.destination, 'mission_state': mission.mission_state} for mission in missions]
            return missions_dict
        except Exception as e:
            print(e)

    def save_mission(self, name, release_date, destination, mission_state, crew, payload, mission_duration, mission_cost, description):
        try:
            save_date = datetime.strptime(release_date, '%d %m %Y').date()
            add_banco = Missions(name, save_date, destination, mission_state, crew, payload, mission_duration, mission_cost, description)
            db.session.add(add_banco)
            db.session.commit()
        except Exception as e:
            print(e)

    def update_mission(self, id, release_date, destination, mission_state, crew, payload, mission_duration, mission_cost, description):
        try:
            update_date = datetime.strptime(release_date, '%d %m %Y').date()
            db.session.query(Missions).filter(Missions.id == id).update({'release_date': update_date, 'destination': destination, 'mission_state': mission_state, 'crew': crew, 'payload': payload, 'mission_duration': mission_duration, 'mission-cost': mission_cost, 'description': description})
            db.session.commit()
        except Exception as e:
            print(e)
        
    def delete_mission(self, id):
        try:
            db.session.query(Missions).filter(Missions.id == id).delete()
            db.session.commit()
        except Exception as e:
            print(e)

    
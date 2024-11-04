from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api
from flask_cors import CORS

app = Flask(__name__)
CORS(app) 
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///crud.db' #URI do banco de dados
api = Api(app)
db = SQLAlchemy(app)

from app.models.missions import Missions
with app.app_context(): #contexto da aplicação
    db.create_all()

from app.view.reso_missions import Index, MissionCreate, MissionById, MissionByDate, MissionUpdate, Missions_list, MissionDelete
api.add_resource(Index, "/")
api.add_resource(Missions_list, "/list")
api.add_resource(MissionByDate, "/listbydate")
api.add_resource(MissionCreate, "/create")
api.add_resource(MissionUpdate, "/update")
api.add_resource(MissionDelete, "/delete")
api.add_resource(MissionById, '/searchid')
from flask import Flask
from flask_cors import CORS

from src.core.Core import Core
from src.statistics.StatisticsModule import StatisticsModule
from src.statistics.config.config import get_upload_dir_path, get_assets_url


app = Flask(__name__, static_url_path=get_assets_url(), static_folder=get_upload_dir_path(),)
cors = CORS(app)

core = Core(app)
core.initModule(StatisticsModule())



# app.run(debug=True)



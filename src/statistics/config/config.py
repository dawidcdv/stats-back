import os



def get_postgres_uri():
    host = os.environ.get('DB_HOST', 'localhost')
    port = 5431 if host == 'localhost' else 5432
    password = os.environ.get('DB_PASSWORD', 'not_secure_passw0rd')
    user, db_name = 'statistics', 'statistics'
    return f"postgresql://{user}:{password}@{host}:{port}/{db_name}"
    #return 'sqlite:///statistics/stats.db'

def get_api_url():
    host = os.environ.get('API_HOST', 'localhost')
    port = 5005 if host == 'localhost' else 80
    return f"http://{host}:{port}"


def get_upload_dir_path():
    return os.path.abspath('/uploads')

def get_assets_url():
    return "/"

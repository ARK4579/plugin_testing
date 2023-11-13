import json

_settings = {
    "DATABSE_NAME": "",
    "DB_USER_NAME": "",
    "DB_USER_PASS": "",
    "ADMIN_NAME": "",
    "ADMIN_PASS": "",
    "HTDOCS_PATH": "",
    "WORDPRESS_ZIP_FILE": "",
}
try:
    with open("settings.json") as f:
        _settings = json.load(f)
except FileNotFoundError:
    print("No _settings found. Falling back to default settings!")

DATABSE_NAME = _settings.get("DATABSE_NAME", "")
DB_USER_NAME = _settings.get("DB_USER_NAME", "")
DB_USER_PASS = _settings.get("DB_USER_PASS", "")
ADMIN_NAME = _settings.get("ADMIN_NAME", "")
ADMIN_PASS = _settings.get("ADMIN_PASS", "")
HTDOCS_PATH = _settings.get("HTDOCS_PATH", "")
WORDPRESS_ZIP_FILE = _settings.get("WORDPRESS_ZIP_FILE", "")

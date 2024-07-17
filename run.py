from app import app

from app.models import *


if __name__ == "__main__":
    print(app.url_map)
    app.run()

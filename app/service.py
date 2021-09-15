from sanic import Sanic
from .routes import blueprint_group

app = Sanic(__name__)
app.blueprint(blueprint_group)

if __name__ == "__main__":
    app.run()
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from vocabulary_catalogue.models.model import db
from run import create_app

app = create_app('config')

migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)


if __name__ == '__main__':
    manager.run()

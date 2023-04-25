from flask import Flask, request, jsonify
from flask_restful import Resource, Api
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tasks.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(200), nullable=True)

    def __repr__(self):
        return f'Task {self.id}: {self.title}'


def create_db():
    with app.app_context():
        db.create_all()
create_db()

class TaskResource(Resource):
    def get(self, task_id=None):
        if task_id:
            task = Task.query.get_or_404(task_id)
            return jsonify({'id': task.id, 'title': task.title, 'description': task.description})
        tasks = Task.query.all()
        return jsonify([{'id': task.id, 'title': task.title, 'description': task.description} for task in tasks])

    def post(self):
        task_data = request.get_json()
        new_task = Task(title=task_data['title'], description=task_data.get('description', None))
        db.session.add(new_task)
        db.session.commit()
        return jsonify({'id': new_task.id, 'title': new_task.title, 'description': new_task.description})

    def put(self, task_id):
        task_data = request.get_json()
        task = Task.query.get_or_404(task_id)
        task.title = task_data['title']
        task.description = task_data.get('description', None)
        db.session.commit()
        return jsonify({'id': task.id, 'title': task.title, 'description': task.description})

    def delete(self, task_id):
        task = Task.query.get_or_404(task_id)
        db.session.delete(task)
        db.session.commit()
        return jsonify({'result': 'Task deleted'})

api.add_resource(TaskResource, '/tasks', '/tasks/<int:task_id>')

if __name__ == '__main__':
    app.run(debug=True)

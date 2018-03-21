from flask import Flask, Blueprint, render_template, redirect, url_for

def create_project_app(config):
    project = Flask(__name__)
    project.config.from_object(config)

    from .project_manager import project_blueprint
    project.register_blueprint(project_blueprint, url_prefix='/project')

    # Add a default root route.
    @project.route("/project")
    def index():
        return redirect(url_for('project_manager.list_projects'))
    return project

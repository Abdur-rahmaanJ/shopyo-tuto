from shopyo.api.module import ModuleHelp
from shopyo.api.templates import yo_render
from flask import render_template

from .models import Note 


mhelp = ModuleHelp(__file__, __name__)
globals()[mhelp.blueprint_str] = mhelp.blueprint
module_blueprint = globals()[mhelp.blueprint_str]


@module_blueprint.route("/")
def index():
    notes = Note.query.all()
    return render_template('notes/index.html', notes=notes)

# @module_blueprint.route("/")
# def index():
#     notes = Note.query.all()
#     context = {
#         'notes': notes
#     }
#     return yo_render('notes/index.html', context)
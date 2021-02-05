from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user    # for handling logging in and out
from .models import Note
from . import db    # import from current package (folder) the db object
import json    # for deleting notes

views = Blueprint('views', __name__)    # blueprint for flask application


@views.route('/', methods=['GET', 'POST'])
@login_required    # cannot access this page/route unless user is logged in
def home():
    # return "<h1>Tim Test</h1>"
    if request.method == 'POST':
        note = request.form.get('note')
        
        if len(note) < 1:
            flash('Note is too short!', category='error')
        else:
            new_note = Note(data=note, user_id=current_user.id)
            db.session.add(new_note)
            db.session.commit()
            flash('Note added!', category='success')
    return render_template("home.html", user=current_user)

@views.route('/delete-note', methods=['POST'])
def delete_note():
    note = json.loads(request.data)
    noteId = note['noteId']
    note = Note.query.get(noteId)
    if note:
        if note.user_id == current_user.id:
            db.session.delete(note)
            db.session.commit()
            flash('Note deleted!', category='success')
    return jsonify({})
    
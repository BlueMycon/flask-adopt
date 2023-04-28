"""Models for adopt app."""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Pet(db.Model):
    __tablename__ = "pets"

    # id: auto-incrementing integer
    id = db.Column(
        db.Integer,
        primary_key=True,
        autoincrement=True,
    )
    # name: text, required
    name = db.Column(
        db.String(50),
        nullable=False,
    )
    # species: text, required
    species = db.Column(
        db.String(50),
        nullable=False,
    )
    # photo_url: text, required (we’ll make it '' if they don’t give us one)
    photo_url = db.Column(
        db.Text,
        nullable=False,
        default='',
    )
    # age: text, (baby, young, adult, senior) required
    age = db.Column(
        db.String(20),
        nullable=False,
    )
    # notes: text, optional
    notes = db.Column(
        db.Text,
    )
    # available: true/false, required, should default to available
    available = db.Column(
        db.Boolean,
        nullable=False,
        default=True,
    )

def connect_db(app):
    """Connect this database to provided Flask app.

    You should call this in your Flask app.
    """

    app.app_context().push()
    db.app = app
    db.init_app(app)

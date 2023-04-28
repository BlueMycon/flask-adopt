from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Pet(db.Model):
    """Pet model."""

    __tablename__ = "pets"

    id = db.Column(
        db.Integer,
        primary_key=True,
        autoincrement=True,
    )

    name = db.Column(
        db.String(50),
        nullable=False,
    )

    species = db.Column(
        # TODO: longest species name
        db.String(50),
        nullable=False,
    )

    photo_url = db.Column(
        db.Text,
        nullable=False,
        default='',
    )

    age = db.Column(
        # TODO: longest age name
        db.String(20),
        nullable=False,
    )

    notes = db.Column(
        db.Text,
        nullable=False,
        default=""
    )

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

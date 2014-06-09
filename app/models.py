from app import db

class Telescope(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nickname = db.Column(db.String(64), index=True, unique=True)
    location = db.Column(db.String(64), index=True)
    images = db.relationship('Image', backref='taken_with')

    def __repr__(self):
        return '<Telescope %r>' % (self.nickname)

class Image(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    filename = db.Column(db.String(128), index=True, unique=True)
    timestamp = db.Column(db.DateTime)
    telescope_id = db.Column(db.Integer, db.ForeignKey('telescope.id'))
    astrometry_id = db.Column(db.Integer, db.ForeignKey('astrometrics.id'))
    weather_id = db.Column(db.Integer, db.ForeignKey('weather.id'))
    celestial_object_id = db.Column(db.Integer, db.ForeignKey('celestial_object.id'))
    settings_id = db.Column(db.Integer, db.ForeignKey('settings.id'))
    alt_coords = db.Column(db.String(64))
    azim_coords = db.Column(db.String(64))

    def __repr__(self):
        return '<Image %r>' % (self.filename)

class Settings(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    camera = db.Column(db.String(64))
    field_of_view = db.Column(db.String(64))
    exposure_seconds = db.Column(db.Integer)
    filter = db.Column(db.String(64))
    focus_value = db.Column(db.Integer)
    zoom = db.Column(db.Integer)

class CelestialObject(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    designation = db.Column(db.String(64))
    right_ascension_coords = db.Column(db.String(64))
    declination_coords = db.Column(db.String(64))
    images = db.relationship('Image', backref='image_of')

class Astrometry(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    #TODO (add stuff here)

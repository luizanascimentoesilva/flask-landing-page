class UserComments(db.Model):
    _tablename_= 'userComments'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    email = db.Colum(db.String)
    commentary = db.Column(db.String)
    created_at = db.Column(db.DateTime(timezone=True),
                           server_default=func.now())

    def _init_ (self, name, email, commentary):
        self.name = name
        self.commentary = commentary
        self.email = email


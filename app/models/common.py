from app import db


class BaseDBModel(db.Model):
    """contain common shared functions for database interaction"""
    def save(self):
        """writes the model data into the database"""
        db.session.add(self)
        db.session.commit()

    def refresh_from_db(self):
        """gets the updated model from the database using the object is

        Returns
        ------
        BaseDBModel
            instance of the object from the db
        """
        return db.session.query(self.__class__).filter_by(id=str(self.id))

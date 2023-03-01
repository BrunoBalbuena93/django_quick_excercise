
class SessionsProviderRouter:

    # A router to control all database operations on models in the sessions   #
    # application                                                             #

    # Attempts to read sessions models go to users_db_read                    #

    def db_for_read (self, model, **hints):

        if model._meta.app_label == 'sessions':

            return 'project_admin_auth_users_db'

        return None

    # Attempts to write sessions models go to users_db_write                  #

    def db_for_write (self, model, **hints):

        if model._meta.app_label == 'sessions':

            return 'project_admin_auth_users_db'

        return None

    # Allow relations if a model in the sessions app is involved              #

    def allow_relation(self, obj1, obj2, **hints):

        if obj1._meta.app_label == 'sessions' or \
           obj2._meta.app_label == 'sessions':

            return True

        return None

    # Make sure the sessions app only appears in the users_db_write database  #

    def allow_migrate(self, db, app_label, model_name=None, **hints):

        if app_label == 'sessions':

            return db == 'project_admin_auth_users_db'

        return None

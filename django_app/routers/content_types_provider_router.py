
class ContentTypesProviderRouter:

    # A router to control all database operations on models in the            #
    # contenttypes application                                                #

    # Attempts to read contenttypes models go to users_db_read                #

    def db_for_read (self, model, **hints):

        if model._meta.app_label == 'contenttypes':

            return 'project_admin_auth_users_db'

        return None

    # Attempts to write contenttypes models go to users_db_write              #

    def db_for_write (self, model, **hints):

        if model._meta.app_label == 'contenttypes':

            return 'project_admin_auth_users_db'

        return None

    # Allow relations if a model in the contenttypes app is involved          #

    def allow_relation(self, obj1, obj2, **hints):

        if obj1._meta.app_label == 'contenttypes' or \
           obj2._meta.app_label == 'contenttypes':

            return True

        return None

    # Make sure the contenttypes app only appears in the users_db_write       #
    # database                                                                #

    def allow_migrate(self, db, app_label, model_name=None, **hints):

        if app_label == 'contenttypes':

            return db == 'project_admin_auth_users_db'

        return None

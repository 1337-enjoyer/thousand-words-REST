class WordsDBRouter:
    def db_for_read(self, model, **hints):
        if model._meta.model_name == 'words':
            return 'words_db'
        return None
    
    def db_for_write(self, model, **hints):
        if model._meta.model_name == 'words':
            return 'words_db'
        return None
    
    def allow_relation(self, obj1, obj2, **hints):
        if obj1._meta.model_name == 'words' or obj2._meta.model_name == 'words':
            return True
        return None
    
    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if model_name == 'words':
            return db == 'words_db'
        return None
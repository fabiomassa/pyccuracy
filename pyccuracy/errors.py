class TestFailedError(Exception):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return unicode(self.message)

class ActionFailedError(Exception):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return unicode(self.message)
        
class InvalidScenarioError(Exception):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return unicode(self.message)
        
    def __unicode__(self):
        return self.message
        
class LanguageParseError(Exception):
    def __init__(self, culture, file_path, error_message = "The language file for %s could not be parsed at %s!"):
        self.culture = culture
        self.error_message = error_message
        self.file_path = file_path

    def __str__(self):
        return unicode(self.error_message) % (self.culture, self.file_path)
        
class SelectOptionError(Exception):
    def __init__(self, message):
        self.message = message
        print message

    def __str__(self):
        return unicode(self.message)
        
    def __unicode__(self):
        return self.message

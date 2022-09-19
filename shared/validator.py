
class Validator():

    errors = []


    def validate(self, events) -> str:
        pass

    def isValid(self):
        if len(self.errors) > 0:
            return False
        
        return True
    
    def validateField(self, value):
        if value in [None,""]:
            return False
        return True

    def addError(self,variable_name, error):

        self.errors.append({variable_name,error})
        

    

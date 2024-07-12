class BaseTemplate:
    def __init__(self, recipient):
        self.recipient = recipient
       
 
    def generate_subject(self):
        raise NotImplementedError("Subclasses implement this method.")
 
    def generate_body(self):
        raise NotImplementedError("Subclasses implement this method.")
 
    def generate_email(self):
        subject = self.generate_subject()
        body = self.generate_body()
        return subject, body
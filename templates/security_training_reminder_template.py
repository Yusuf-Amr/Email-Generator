from .base_template import BaseTemplate

class SecurityTrainingReminderTemplate(BaseTemplate):
    def __init__(self, date,recipient, training_session_date, training_session_time, training_location, additional_instructions):
        self.date = date
        super().__init__(recipient)
        self.training_session_date = training_session_date
        self.training_session_time = training_session_time
        self.training_location = training_location
        self.additional_instructions = additional_instructions

    @staticmethod
    def required_inputs():
        return ["recipient","date", "training_session_date", "training_session_time", "training_location", "additional_instructions"]

    def generate_subject(self):
        return "[System Notification] Security Awareness Training Reminder"

    def generate_body(self):
        return f"""
Dear {self.recipient},

This is a reminder for the upcoming security awareness training session. The details are as follows:

- Training Session Date: [{self.training_session_date}]
- Training Session Time: [{self.training_session_time}]
- Training Location: [{self.training_location}]

Additional Instructions:
{self.additional_instructions}

Please make sure to attend the session to stay informed about the latest security practices and protocols. Your participation is crucial in maintaining the security of our organization.

Thank you for your attention to this matter.

Sincerely,
"""

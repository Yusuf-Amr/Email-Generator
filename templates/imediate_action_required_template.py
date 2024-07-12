from .base_template import BaseTemplate

class ImmediateActionTemplate(BaseTemplate):
    def __init__(self, date, recipient, system_name, issue_description, action_required):
        self.date = date
        super().__init__(recipient)
        self.system_name = system_name
        self.issue_description = issue_description
        self.action_required = action_required

    @staticmethod
    def required_inputs():
        return ["recipient","date", "system_name", "issue_description", "action_required"]

    def generate_subject(self):
        return "[Immediate Action Required] System Issue Detected"

    def generate_body(self):
        return f"""
Dear {self.recipient},

An immediate action is required regarding a critical issue detected in the {self.system_name}. As of [{self.date}], the following issue has been identified:

- Issue Description: {self.issue_description}

Action Required: {self.action_required}

Please address this issue as soon as possible to ensure the security and functionality of the system.

Thank you for your prompt attention to this matter.

Sincerely,
"""

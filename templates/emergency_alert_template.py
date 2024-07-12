from .base_template import BaseTemplate

class EmergencyAlertTemplate(BaseTemplate):
    def __init__(self, date,recipient, incident_description, affected_systems, immediate_actions):
        self.date = date
        super().__init__(recipient)
        self.incident_description = incident_description
        self.affected_systems = affected_systems
        self.immediate_actions = immediate_actions

    @staticmethod
    def required_inputs():
        return ["recipient","date", "incident_description", "affected_systems", "immediate_actions"]

    def generate_subject(self):
        return "[Emergency Alert] Security Incident Detected"

    def generate_body(self):
        return f"""
Dear {self.recipient},

This is an emergency alert regarding a security incident detected on [{self.date}]. The following incident has been identified:

- Incident Description: {self.incident_description}
- Affected Systems: {self.affected_systems}

Immediate Actions Required: {self.immediate_actions}

Please address this issue with the highest priority to ensure the security and integrity of our systems.

Thank you for your prompt attention to this critical matter.

Sincerely,
"""



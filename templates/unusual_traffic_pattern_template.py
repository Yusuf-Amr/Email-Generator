from .base_template import BaseTemplate

class NetworkAlertTemplate(BaseTemplate):
    def __init__(self, date,recipient, unusual_traffic_details, affected_networks, recommended_actions):
        self.date = date
        super().__init__(recipient)
        self.unusual_traffic_details = unusual_traffic_details
        self.affected_networks = affected_networks
        self.recommended_actions = recommended_actions

    @staticmethod
    def required_inputs():
        return ["recipient","date", "unusual_traffic_details", "affected_networks", "recommended_actions"]

    def generate_subject(self):
        return "[Network Alert] Unusual Traffic Pattern Detected"

    def generate_body(self):
        return f"""
Dear {self.recipient},

This is a network alert regarding an unusual traffic pattern detected on [{self.date}]. The following details have been observed:

- Unusual Traffic Details: {self.unusual_traffic_details}
- Affected Networks: {self.affected_networks}

Recommended Actions: {self.recommended_actions}

Please take the necessary actions to investigate and mitigate any potential threats to our network security. Your prompt attention to this matter is crucial.

Thank you for your cooperation.

Sincerely,
"""


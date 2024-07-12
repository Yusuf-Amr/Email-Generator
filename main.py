
from templates.base_template import BaseTemplate
from templates.imediate_action_required_template import ImmediateActionTemplate
from templates.security_training_reminder_template import SecurityTrainingReminderTemplate
from templates.emergency_alert_template import EmergencyAlertTemplate
from templates.unusual_traffic_pattern_template import NetworkAlertTemplate
 
def main():
    while True:
        print("Select the type of email you want to generate:")
        email_types = {
            '1': ('Emergency Alert Template', EmergencyAlertTemplate),
            '2': ('Network Alert Template', NetworkAlertTemplate),
            '3': ('Immediate Action Template', ImmediateActionTemplate),
            '4': ('Security Training Reminder Template', SecurityTrainingReminderTemplate),
            'q': ('Quit', None)
        }
        for key, value in email_types.items():
            print(f"{key}. {value[0]}")
 
        choice = input("Enter the number corresponding to your choice (or 'q' to quit): ").strip().lower()
        if choice == 'q':
            break
        elif choice not in email_types:
            print("Invalid choice.")
            continue
 
        selected_email_type = email_types[choice][1]
        if not selected_email_type:
            print("Exiting program.")
            break
 
        required_inputs = selected_email_type.required_inputs()
        inputs = {}
 
        for input_name in required_inputs:
            inputs[input_name] = input(f"Enter the {input_name.replace('_', ' ')}: ")

        template = selected_email_type(**inputs)
        subject = template.generate_subject()
        body = template.generate_body()
 
        print("\nGenerated Email:")
        print(f"\nSubject:{subject}")
        print(body)
        print()
 
if __name__ == "__main__":
    main()
 

 
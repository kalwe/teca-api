from tortoise import fields
from typing import List, Protocol

from app.core.models.base_entity import BaseEntity

class Notifiable(Protocol):
    """
    A protocol for all notification services, allowing for extensibility.
    """
    def send_notification(self, message: str, recipient: str) -> None:
        """ Sends a notification to a given recipient """
        pass

class AlertEvent:
    """
    Represents an event (alert) to be triggered in the system.
    This event will be listened to by one or more notification services.
    """
    def __init__(self, alert_type: str, alert_message: str, recipient_email: str):
        self.alert_type = alert_type
        self.alert_message = alert_message
        self.recipient_email = recipient_email

    def __str__(self):
        return f"Alert for {self.alert_type} to {self.recipient_email}"


class Alert(BaseEntity):
    """
    Represents an alert to be sent to an employee, using an injectable notifier.
    """
    alert_type = fields.CharField(max_length=100, description="Type of alert (e.g., Birthday, Contract Expiry)")
    alert_message = fields.TextField(description="The content of the alert")
    recipient_email = fields.CharField(max_length=255, description="Email address of the recipient")

    def __str__(self):
        return f"Alert for {self.alert_type} to {self.recipient_email}"

    def trigger_event(self, event_emitter: 'EventEmitter') -> None:
        """
        Triggers the alert event to be handled by the event emitter (which notifies observers).
        """
        alert_event = AlertEvent(self.alert_type, self.alert_message, self.recipient_email)
        event_emitter.emit(alert_event)

class EventEmitter:
    """
    A class that emits events and notifies registered observers (notification services).
    Implements the 'Observer Pattern'.
    """
    def __init__(self):
        self._observers: List[Notifiable] = []

    def register_observer(self, observer: Notifiable) -> None:
        """
        Registers an observer (notification service) to listen for events.
        """
        self._observers.append(observer)

    def unregister_observer(self, observer: Notifiable) -> None:
        """
        Removes an observer from the list of listeners.
        """
        self._observers.remove(observer)

    def emit(self, event: AlertEvent) -> None:
        """
        Emits an event, notifying all registered observers (notification services).
        """
        for observer in self._observers:
            observer.send_notification(event.alert_message, event.recipient_email)


# usage ex
# class EmailNotifier(Notifiable):
#     """
#     An example of a concrete observer (notification service) that sends email notifications.
#     """
#     def send_notification(self, message: str, recipient: str) -> None:
#         # Simulate sending an email.
#         print(f"Sending Email to {recipient}: {message}")

# def main():
#     # Create the event emitter
#     event_emitter = EventEmitter()

#     # Create different notification services (observers)
#     email_notifier = EmailNotifier()

#     # Register observers with the event emitter
#     event_emitter.register_observer(email_notifier)

#     # Create an alert
#     alert = Alert(alert_type="Contract Expiry", alert_message="Your contract is about to expire!", recipient_email="employee@example.com")

#     # Trigger the event (alert)
#     alert.trigger_event(event_emitter)

# if __name__ == "__main__":
#     main()

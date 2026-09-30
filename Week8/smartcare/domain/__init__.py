"""Domain layer: the clinic's core classes and rules. Doesn't import anything from the other layers."""

from .appointment import Appointment
from .patient import Patient
from .practitioner import Practitioner
from .status import AppointmentStatus, InvalidStatusTransitionError

__all__ = ["Appointment", "Patient", "Practitioner", "AppointmentStatus", "InvalidStatusTransitionError"]

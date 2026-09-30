"""Appointment status and the error for illegal status changes."""

from enum import Enum


class AppointmentStatus(Enum):
    """The only three statuses an appointment can have (FR-05)."""
    BOOKED = "booked"
    CANCELLED = "cancelled"
    COMPLETED = "completed"


class InvalidStatusTransitionError(Exception):
    """Raised when someone tries to change an appointment's status in a way that isn't allowed."""

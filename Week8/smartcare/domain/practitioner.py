"""Practitioner (GP) domain class."""

from __future__ import annotations

from datetime import datetime
from typing import TYPE_CHECKING

from .status import AppointmentStatus
from .validation import check_id, check_text

if TYPE_CHECKING:
    from .appointment import Appointment


class Practitioner:
    """A GP who works at the clinic (FR-01, FR-03, FR-04, FR-08)."""

    def __init__(self, practitioner_id: int, name: str, specialty: str = "General Practice") -> None:
        """Sets up a new GP. The ID, name and specialty have to be valid."""
        self._practitioner_id = check_id(practitioner_id, "Practitioner")
        self._name = check_text(name, "Practitioner name")
        self._specialty = check_text(specialty, "Specialty")
        self._available_times: list[datetime] = []
        self._appointments: list[Appointment] = []

    @property
    def practitioner_id(self) -> int:
        """The GP's ID (read only)."""
        return self._practitioner_id

    @property
    def name(self) -> str:
        """The GP's name. Change it with update_details()."""
        return self._name

    @property
    def specialty(self) -> str:
        """The GP's specialty. Change it with update_details()."""
        return self._specialty

    @property
    def appointments(self) -> list[Appointment]:
        """A copy of this GP's appointments."""
        return list(self._appointments)

    def update_details(self, name: str, specialty: str | None = None) -> None:
        """Updates the GP's name, and specialty if one is given (FR-03)."""
        new_name = check_text(name, "Practitioner name")
        new_specialty = self._specialty if specialty is None else check_text(specialty, "Specialty")
        self._name = new_name
        self._specialty = new_specialty

    def add_available_time(self, date_time: datetime) -> None:
        """Adds a time when the GP is free (FR-04)."""
        if not isinstance(date_time, datetime):
            raise ValueError("Available time must be a datetime")
        if date_time in self._available_times:
            raise ValueError("That time is already in the GP's free times")
        self._available_times.append(date_time)

    def add_appointment(self, appointment: Appointment) -> None:
        """Adds an appointment to this GP's list, as long as it's actually with this GP."""
        if appointment.practitioner is not self:
            raise ValueError("This appointment is with a different GP")
        if appointment in self._appointments:
            raise ValueError("This appointment is already in the GP's list")
        self._appointments.append(appointment)

    def is_available(self, date_time: datetime) -> bool:
        """Checks the GP works at that time and nobody is booked in, so there's no double booking (FR-01, FR-09).
        Cancelled appointments don't count, so the slot is free again after a cancel (FR-06)."""
        if date_time not in self._available_times:
            return False
        for appointment in self._appointments:
            if appointment.date_time == date_time and appointment.status != AppointmentStatus.CANCELLED:
                return False
        return True

    def get_availability(self) -> list[datetime]:
        """Gives back the GP's free times that aren't booked yet, in order (FR-04)."""
        return sorted(t for t in self._available_times if self.is_available(t))

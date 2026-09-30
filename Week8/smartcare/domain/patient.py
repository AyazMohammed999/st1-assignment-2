"""Patient domain class."""

from __future__ import annotations

from datetime import datetime
from typing import TYPE_CHECKING

from .validation import check_id, check_text

if TYPE_CHECKING:
    from .appointment import Appointment


class Patient:
    """A patient at the clinic (FR-02, FR-07, FR-10)."""

    def __init__(self, patient_id: int, name: str) -> None:
        """Sets up a new patient. The ID and name have to be valid."""
        self._patient_id = check_id(patient_id, "Patient")
        self._name = check_text(name, "Patient name")
        self._appointments: list[Appointment] = []

    @property
    def patient_id(self) -> int:
        """The patient's ID (read only)."""
        return self._patient_id

    @property
    def name(self) -> str:
        """The patient's name (read only)."""
        return self._name

    @property
    def appointments(self) -> list[Appointment]:
        """A copy of this patient's appointments, so the real list can't be changed from outside."""
        return list(self._appointments)

    def add_appointment(self, appointment: Appointment) -> None:
        """Adds an appointment to this patient's list, as long as it's actually for this patient."""
        if appointment.patient is not self:
            raise ValueError("This appointment is for a different patient")
        if appointment in self._appointments:
            raise ValueError("This appointment is already in the patient's list")
        self._appointments.append(appointment)

    def get_past_appointments(self, now: datetime | None = None) -> list[Appointment]:
        """Gives back appointments that have already happened, including cancelled ones (FR-07).
        The current time can be passed in, which makes this easy to test. It uses the real time if not."""
        if now is None:
            now = datetime.now()
        return [a for a in self._appointments if a.date_time < now]

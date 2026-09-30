"""Appointment domain class."""

from __future__ import annotations

from datetime import datetime

from .patient import Patient
from .practitioner import Practitioner
from .status import AppointmentStatus, InvalidStatusTransitionError
from .validation import check_id


class Appointment:
    """One patient seeing one GP at a set time (FR-05, FR-06, FR-09)."""

    def __init__(self, appointment_id: int, patient: Patient,
                 practitioner: Practitioner, date_time: datetime) -> None:
        """Sets up a new appointment. Every appointment starts off as BOOKED."""
        if not isinstance(patient, Patient):
            raise ValueError("An appointment needs a proper Patient")
        if not isinstance(practitioner, Practitioner):
            raise ValueError("An appointment needs a proper Practitioner")
        if not isinstance(date_time, datetime):
            raise ValueError("Appointment time must be a datetime")

        self._appointment_id = check_id(appointment_id, "Appointment")
        self._patient = patient
        self._practitioner = practitioner
        self._date_time = date_time
        self._status = AppointmentStatus.BOOKED

    @property
    def appointment_id(self) -> int:
        return self._appointment_id

    @property
    def patient(self) -> Patient:
        return self._patient

    @property
    def practitioner(self) -> Practitioner:
        return self._practitioner

    @property
    def date_time(self) -> datetime:
        return self._date_time

    @property
    def status(self) -> AppointmentStatus:
        """The current status (FR-05). Read only, so it can only change through cancel() or complete()."""
        return self._status

    def cancel(self) -> None:
        """Cancels a booked appointment (FR-06). The object stays so the history is kept (FR-07).
        The GP's slot frees up because is_available() ignores cancelled appointments."""
        if self._status != AppointmentStatus.BOOKED:
            raise InvalidStatusTransitionError(
                f"Can't cancel an appointment that is already {self._status.value}")
        self._status = AppointmentStatus.CANCELLED

    def complete(self) -> None:
        """Marks a booked appointment as completed after the visit (FR-05)."""
        if self._status != AppointmentStatus.BOOKED:
            raise InvalidStatusTransitionError(
                f"Can't complete an appointment that is already {self._status.value}")
        self._status = AppointmentStatus.COMPLETED

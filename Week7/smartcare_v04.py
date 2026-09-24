"""SmartCare v0.4 - domain layer (Stage 4, Week 7)."""

from __future__ import annotations

from datetime import datetime
from enum import Enum


class AppointmentStatus(Enum):
    """The only three statuses an appointment can have (FR-05)."""
    BOOKED = "booked"
    CANCELLED = "cancelled"
    COMPLETED = "completed"


class InvalidStatusTransitionError(Exception):
    """Raised when someone tries to change an appointment's status in a way that isn't allowed."""


def _check_id(value: int, label: str) -> int:
    """Makes sure an ID is a positive whole number. True/False don't count, even though Python treats them as 1/0."""
    if isinstance(value, bool) or not isinstance(value, int) or value <= 0:
        raise ValueError(f"{label} ID must be a positive whole number")
    return value


def _check_text(value: str, label: str) -> str:
    """Makes sure a name or specialty isn't blank, and trims extra spaces."""
    if not isinstance(value, str) or not value.strip():
        raise ValueError(f"{label} can't be empty")
    return value.strip()


class Patient:
    """A patient at the clinic (FR-02, FR-07, FR-10)."""

    def __init__(self, patient_id: int, name: str) -> None:
        """Sets up a new patient. The ID and name have to be valid."""
        self._patient_id = _check_id(patient_id, "Patient")
        self._name = _check_text(name, "Patient name")
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

    def get_past_appointments(self) -> list[Appointment]:
        """Gives back appointments that have already happened, including cancelled ones (FR-07)."""
        now = datetime.now()
        return [a for a in self._appointments if a.date_time < now]


class Practitioner:
    """A GP who works at the clinic (FR-01, FR-03, FR-04, FR-08)."""

    def __init__(self, practitioner_id: int, name: str, specialty: str = "General Practice") -> None:
        """Sets up a new GP. The ID, name and specialty have to be valid."""
        self._practitioner_id = _check_id(practitioner_id, "Practitioner")
        self._name = _check_text(name, "Practitioner name")
        self._specialty = _check_text(specialty, "Specialty")
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
        new_name = _check_text(name, "Practitioner name")
        new_specialty = self._specialty if specialty is None else _check_text(specialty, "Specialty")
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

        self._appointment_id = _check_id(appointment_id, "Appointment")
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

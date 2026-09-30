"""Service layer: runs the booking steps in the right order. The actual rules stay in the domain classes."""

from __future__ import annotations

from datetime import datetime

from smartcare.domain import Appointment, Patient, Practitioner
from smartcare.repositories import AppointmentRepository


class AppointmentService:
    """Coordinates booking, cancelling and completing appointments (FR-01, FR-05, FR-06, FR-09)."""

    def __init__(self, repository: AppointmentRepository) -> None:
        self._repository = repository

    def book_appointment(self, patient: Patient, practitioner: Practitioner, date_time: datetime) -> Appointment:
        """Books an appointment, but only if the GP is free at that time (FR-01, FR-09)."""
        if not practitioner.is_available(date_time):
            raise ValueError("The GP isn't available at that time")

        appointment = Appointment(self._repository.next_id(), patient, practitioner, date_time)
        patient.add_appointment(appointment)
        practitioner.add_appointment(appointment)
        self._repository.add(appointment)
        return appointment

    def cancel_appointment(self, appointment_id: int) -> Appointment:
        """Finds the appointment and cancels it. Appointment decides if that's allowed (FR-06)."""
        appointment = self._find(appointment_id)
        appointment.cancel()
        return appointment

    def complete_appointment(self, appointment_id: int) -> Appointment:
        """Finds the appointment and marks it as completed. Appointment decides if that's allowed (FR-05)."""
        appointment = self._find(appointment_id)
        appointment.complete()
        return appointment

    def _find(self, appointment_id: int) -> Appointment:
        """Looks up an appointment, or raises an error if it doesn't exist."""
        appointment = self._repository.get_by_id(appointment_id)
        if appointment is None:
            raise LookupError(f"No appointment with ID {appointment_id}")
        return appointment

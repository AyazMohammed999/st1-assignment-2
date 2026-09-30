"""Persistence layer: keeps appointments in memory for now."""

from __future__ import annotations

from smartcare.domain import Appointment
from smartcare.repositories import AppointmentRepository


class InMemoryAppointmentRepository(AppointmentRepository):
    """Stores appointments in a dictionary, keyed by ID. Everything is lost when the program closes."""

    def __init__(self) -> None:
        self._appointments: dict[int, Appointment] = {}
        self._last_id = 0

    def next_id(self) -> int:
        self._last_id += 1
        return self._last_id

    def add(self, appointment: Appointment) -> None:
        if appointment.appointment_id in self._appointments:
            raise ValueError("An appointment with that ID is already saved")
        self._appointments[appointment.appointment_id] = appointment

    def get_by_id(self, appointment_id: int) -> Appointment | None:
        return self._appointments.get(appointment_id)

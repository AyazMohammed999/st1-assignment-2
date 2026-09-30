"""The contract for storing and finding appointments. Only has what the current use cases need."""

from __future__ import annotations

from abc import ABC, abstractmethod

from smartcare.domain import Appointment


class AppointmentRepository(ABC):
    """What the service needs to do with stored appointments. It doesn't say how they're stored."""

    @abstractmethod
    def next_id(self) -> int:
        """Gives back an ID that no other appointment is using yet."""

    @abstractmethod
    def add(self, appointment: Appointment) -> None:
        """Saves a new appointment."""

    @abstractmethod
    def get_by_id(self, appointment_id: int) -> Appointment | None:
        """Finds an appointment by its ID, or gives back None if there isn't one."""

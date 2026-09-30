"""Starts SmartCare v0.5. Creates each layer and connects them. This is the only place that knows about all of them."""

from datetime import datetime

from smartcare.domain import Patient, Practitioner
from smartcare.persistence import InMemoryAppointmentRepository
from smartcare.presentation import Menu
from smartcare.services import AppointmentService


def main() -> None:
    repository = InMemoryAppointmentRepository()
    service = AppointmentService(repository)

    # Sample data for now, since there's no way to add patients or GPs from the menu yet
    patients = {1: Patient(1, "Sara Khan"), 2: Patient(2, "Tom Walker")}
    gp = Practitioner(1, "Dr Amy Lee")
    for hour in (9, 10, 11):
        gp.add_available_time(datetime(2026, 10, 5, hour, 0))
    practitioners = {1: gp}

    Menu(service, patients, practitioners).run()


if __name__ == "__main__":
    main()

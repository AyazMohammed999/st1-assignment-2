"""Presentation layer: reads what the user types and prints results. No booking rules or storage in here."""

from __future__ import annotations

from datetime import datetime

from smartcare.domain import InvalidStatusTransitionError, Patient, Practitioner
from smartcare.services import AppointmentService

DATE_FORMAT = "%Y-%m-%d %H:%M"


class Menu:
    """A simple text menu for reception staff."""

    def __init__(self, service: AppointmentService,
                 patients: dict[int, Patient], practitioners: dict[int, Practitioner]) -> None:
        self._service = service
        self._patients = patients
        self._practitioners = practitioners

    def run(self) -> None:
        while True:
            print("\n1. Book appointment\n2. Cancel appointment\n3. Complete appointment\n4. Show GP free times\n0. Quit")
            choice = input("Choose an option: ").strip()
            if choice == "0":
                print("Bye!")
                return
            actions = {"1": self._book, "2": self._cancel, "3": self._complete, "4": self._show_free_times}
            action = actions.get(choice)
            if action is None:
                print("That's not an option, try again.")
                continue
            try:
                action()
            except (ValueError, LookupError, InvalidStatusTransitionError) as error:
                print(f"Sorry, that didn't work: {error}")

    def _book(self) -> None:
        patient = self._pick(self._patients, "Patient ID: ")
        practitioner = self._pick(self._practitioners, "GP ID: ")
        date_time = datetime.strptime(input("Date and time (YYYY-MM-DD HH:MM): ").strip(), DATE_FORMAT)
        appointment = self._service.book_appointment(patient, practitioner, date_time)
        print(f"Booked! Appointment {appointment.appointment_id}: {patient.name} with "
              f"{practitioner.name} at {date_time.strftime(DATE_FORMAT)}")

    def _cancel(self) -> None:
        appointment = self._service.cancel_appointment(self._read_id("Appointment ID: "))
        print(f"Appointment {appointment.appointment_id} is now {appointment.status.value}.")

    def _complete(self) -> None:
        appointment = self._service.complete_appointment(self._read_id("Appointment ID: "))
        print(f"Appointment {appointment.appointment_id} is now {appointment.status.value}.")

    def _show_free_times(self) -> None:
        practitioner = self._pick(self._practitioners, "GP ID: ")
        times = practitioner.get_availability()
        if not times:
            print(f"{practitioner.name} has no free times.")
        for t in times:
            print(" -", t.strftime(DATE_FORMAT))

    def _read_id(self, prompt: str) -> int:
        text = input(prompt).strip()
        if not text.isdigit():
            raise ValueError("IDs have to be numbers")
        return int(text)

    def _pick(self, items: dict, prompt: str):
        item_id = self._read_id(prompt)
        if item_id not in items:
            raise LookupError(f"Nothing found with ID {item_id}")
        return items[item_id]

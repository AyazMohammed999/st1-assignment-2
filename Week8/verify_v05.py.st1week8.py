"""Checks that v0.5 still does everything v0.4 did, now going through the service."""

from datetime import datetime

from smartcare.domain import (Appointment, AppointmentStatus, InvalidStatusTransitionError,
                              Patient, Practitioner)
from smartcare.persistence import InMemoryAppointmentRepository
from smartcare.services import AppointmentService

service = AppointmentService(InMemoryAppointmentRepository())
patient = Patient(1, "Sara Khan")
gp = Practitioner(1, "Dr Amy Lee")
time = datetime(2026, 10, 5, 9, 0)
gp.add_available_time(time)


def check(label, passed):
    print(("PASS  " if passed else "FAIL  ") + label)


# Same checks as v0.4
for bad in [(0, "Sara"), (2, ""), ("3", "Sara"), (True, "Sara")]:
    try:
        Patient(*bad)
        check(f"invalid patient {bad} rejected", False)
    except ValueError:
        check(f"invalid patient {bad} rejected", True)

appointment = service.book_appointment(patient, gp, time)
check("booking starts as BOOKED", appointment.status == AppointmentStatus.BOOKED)
check("booking gets ID 1 from the repository", appointment.appointment_id == 1)
check("GP not free while booked", not gp.is_available(time))

try:
    service.book_appointment(patient, gp, time)
    check("double booking blocked", False)
except ValueError:
    check("double booking blocked", True)

service.cancel_appointment(1)
check("cancel works", appointment.status == AppointmentStatus.CANCELLED)
check("GP free again after cancel", gp.is_available(time))
check("cancelled appointment kept in patient history", appointment in patient.appointments)
check("patient list, GP list and repository all point to the same appointment",
      appointment in patient.appointments and appointment in gp.appointments
      and service._repository.get_by_id(1) is appointment)

try:
    service.cancel_appointment(1)
    check("cancelling twice blocked", False)
except InvalidStatusTransitionError:
    check("cancelling twice blocked", True)

try:
    service.complete_appointment(1)
    check("completing a cancelled one blocked", False)
except InvalidStatusTransitionError:
    check("completing a cancelled one blocked", True)

try:
    appointment.status = AppointmentStatus.BOOKED
    check("status can't be changed directly", False)
except AttributeError:
    check("status can't be changed directly", True)

# New in v0.5
second = service.book_appointment(patient, gp, time)
check("slot can be rebooked after a cancel, with a new ID", second.appointment_id == 2)
service.complete_appointment(2)
check("complete works through the service", second.status == AppointmentStatus.COMPLETED)

try:
    service.cancel_appointment(99)
    check("unknown appointment ID rejected", False)
except LookupError:
    check("unknown appointment ID rejected", True)

check("past appointments work with a set 'now'",
      patient.get_past_appointments(now=datetime(2026, 10, 6)) == [appointment, second])
check("nothing is 'past' before it happens",
      patient.get_past_appointments(now=datetime(2026, 10, 4)) == [])

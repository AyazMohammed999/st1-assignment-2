from datetime import datetime
from smartcare_v04 import (Patient, Practitioner, Appointment,
                           AppointmentStatus, InvalidStatusTransitionError)

# 1. Create valid objects
patient = Patient(1, "Sara Khan")
gp = Practitioner(1, "Dr Amy Lee")
time = datetime(2026, 10, 5, 9, 0)
gp.add_available_time(time)

appointment = Appointment(1, patient, gp, time)
patient.add_appointment(appointment)
gp.add_appointment(appointment)
print("1. Created:", patient.name, "|", gp.name, "|", appointment.status)

# 2. Test invalid input
for bad in [(0, "Sara"), (2, ""), ("3", "Sara"), (True, "Sara")]:
    try:
        Patient(*bad)
        print("2. No error for", bad)
    except ValueError as e:
        print("2. Rejected", bad, "->", e)

try:
    Appointment(2, "Sara", gp, time)
except ValueError as e:
    print("2. Rejected appointment with text instead of a Patient ->", e)

# 3. Double booking check
print("3. GP free at 9am while booked?", gp.is_available(time))

# 4. Cancel a booked appointment
appointment.cancel()
print("4. Status after cancel:", appointment.status)
print("4. GP free at 9am after cancel?", gp.is_available(time))
print("4. Still in patient's list?", appointment in patient.appointments)

# 5. Try an illegal repeated transition
try:
    appointment.cancel()
except InvalidStatusTransitionError as e:
    print("5. Cancel again ->", e)
try:
    appointment.complete()
except InvalidStatusTransitionError as e:
    print("5. Complete after cancel ->", e)

# 6. Try to change status directly
try:
    appointment.status = AppointmentStatus.BOOKED
except AttributeError as e:
    print("6. Direct status change ->", e)

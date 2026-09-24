# Assignment 2-Case Study

## Stage 4 Lab Activities

**Implementing the SmartCare Domain Layer**

DESIGN FIRST -> AI PAIR PROGRAMMING -> REVIEW -> VERIFY | 1hour

# A - Revisit Approved UML

Confirm responsibilities, attributes and relationships before coding.

| Class | Attributes | What it does | Links to |
|---|---|---|---|
| Patient | Patient_id, name, Appointment | Keeps its own ID and Name, and its list of appointments so it can show past ones (FR-02, FR-07, FR-10) | Can have 0 or more Appointments |
| Practitioner | Practitioner_id, name, Available_times, Appointments | Keeps the GP’s details, when they’re Free, and checks if a time already taken (FR-01, FR-03, FR-04) | Can have 0 or more Appointments |
| Appointment | Appointment_id, Patient, practitioner, date_time, status | Knows who it’s for and when, and looks After its own status, so it can cancel or Complete itself (FR-05, FR-06, FR-09) | Always 1 patient and 1 GP |

Before I started coding I had another look at my Week 6 UML to make sure it still made sense.

Most of it was fine, but a few things needed changing once I actually thought about turning it into code.

The big one was status. In Week 6 it was just a string that started as "booked", so honestly anyone could set it to anything, even a typo. I'm changing it to an enum so it can only ever be BOOKED, CANCELLED or COMPLETED (FR-05). I stuck with "booked" because that's the word my requirements use.

I also noticed everything in my UML was public, which means any code could just go in and change an appointment's status. So I'm making status private, and the only way to change it will be cancel() or complete(). Once something's cancelled or completed it shouldn't change again, so if you try, you'll get an error.

Cancelled appointments won't be deleted either. They'll just stay as cancelled so the patient's history is still there (FR-07).

The last thing was how the GP's slot frees up after a cancel (FR-06). My first thought was that cancel() should go into Practitioner and add the time back. But then Appointment is messing with another class's data, which didn't feel right. It's way simpler if is_available() just skips cancelled appointments, so the time counts as free again straight away.

I'm not touching Clinic this week because the lab only asks for the three main classes.

# B - Implement Patient: AI OFF

Implement Patient with type hints and basic validation.

```python
from __future__ import annotations
from datetime import datetime


class Patient:
    """A patient at the clinic (FR-02, FR-07, FR-10)."""

    def __init__(self, patient_id: int, name: str) -> None:
        """Sets up a new patient. The ID and name have to be valid."""
        if not isinstance(patient_id, int) or patient_id <= 0:
            raise ValueError("Patient ID must be a positive whole number")
        if not isinstance(name, str) or not name.strip():
            raise ValueError("Patient name can't be empty")
        self._patient_id = patient_id
        self._name = name.strip()
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
```

I started with my Week 6 skeleton and filled it in. First I added type hints to everything, so it's clear what each method takes in and gives back.

For validation I kept it pretty basic. The patient ID has to be a positive number and the name can't be empty or just spaces. If either one is wrong it throws a ValueError straight away, so you can't end up with a patient that's missing something. I also trim any extra spaces off the name.

I made the attributes private (with an underscore) and added read-only properties so you can still look at the ID and name, but you can't change them from outside the class. The appointments list gives back a copy, which means nobody can sneak something into the real list without going through add_appointment().

add_appointment() checks two things before it adds anything: that the appointment is actually for this patient, and that it isn't already in the list. I didn't want an appointment ending up on the wrong person's record.

For get_past_appointments() I just return anything with a time before now. I decided to include cancelled ones too, because FR-07 is about seeing a patient's history, and a cancellation is still part of that.

To check it worked, I made a normal patient and then tried some bad ones, like an ID of 0, a negative ID, the ID as text, and a blank name. They all got rejected like they should. I also tried changing the name directly and it wouldn't let me.

# C - Implement Practitioner: AI OFF

Implement Practitioner with identifier, name and specialty; no database logic.

```python
class Practitioner:
    """A GP who works at the clinic (FR-01, FR-03, FR-04, FR-08)."""

    def __init__(self, practitioner_id: int, name: str, specialty: str = "General Practice") -> None:
        """Sets up a new GP. The ID, name and specialty have to be valid."""
        if not isinstance(practitioner_id, int) or practitioner_id <= 0:
            raise ValueError("Practitioner ID must be a positive whole number")
        if not isinstance(name, str) or not name.strip():
            raise ValueError("Practitioner name can't be empty")
        if not isinstance(specialty, str) or not specialty.strip():
            raise ValueError("Specialty can't be empty")
        self._practitioner_id = practitioner_id
        self._name = name.strip()
        self._specialty = specialty.strip()
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
        if not isinstance(name, str) or not name.strip():
            raise ValueError("Practitioner name can't be empty")
        if specialty is not None and (not isinstance(specialty, str) or not specialty.strip()):
            raise ValueError("Specialty can't be empty")
        self._name = name.strip()
        if specialty is not None:
            self._specialty = specialty.strip()

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
```

Practitioner is pretty similar to Patient. It has type hints everywhere, and the ID, name and specialty all get checked when a GP is created. A bad ID or a blank name or specialty throws a ValueError. The lab asked for a specialty, which I didn't have in Week 6, so I added it with "General Practice" as the default since that's what most doctors at a GP clinic will be.

The difference from Patient is that a GP's details can change (FR-03), so I made update_details() the only way to do that. It checks the new name and specialty the same way the constructor does, so you can't sneak a blank name in through the update. The ID never changes.

For availability, add_available_time() only takes a proper datetime and won't let you add the same time twice. is_available() checks two things: that the GP actually works at that time, and that nobody else is booked in then. The important part is that it ignores cancelled appointments. That's how the slot frees up again after a cancel (FR-06), without Appointment having to go in and change the GP's data. get_availability() just gives back all the free times that aren't taken, in order.

There's no database stuff in here at all. The class only keeps the GP's own details in memory, which is what the lab asked for.

When I tested it, a normal GP got made fine and updating the name and specialty worked. A bad ID, a blank name, a blank specialty, a time that wasn't a datetime and a duplicate time all got rejected. I couldn't test the double booking part yet because Appointment isn't done, so I'll check that in Part F.

# D - Implement Appointment: AI ON

Give AI the approved Appointment UML, business rules and explicit constraints. Ask it to implement only Appointment and agreed enum/exception.

**Prompt I gave the AI:**

Act as a Python pair programmer. Implement only the Appointment class from the approved SmartCare UML. Use type hints and an AppointmentStatus enum. Cancelled appointments remain as objects. Do not add database, UI, notification or service classes. Protect status transitions and explain any decision not directly visible in the UML.

Approved UML for Appointment: appointment_id: int, patient: Patient, practitioner: Practitioner, date_time: datetime, status, cancel(), complete(), get_status(). Each appointment has exactly 1 patient and 1 practitioner.

Business rules: status can only be booked, cancelled or completed (FR-05). A booked appointment can be cancelled or completed, but once it's cancelled or completed it can't change again. Cancelling frees up the GP's time slot (FR-06), but Practitioner's is_available() already ignores cancelled appointments, so Appointment shouldn't change the GP's data. Booking and checking if the GP is free is Clinic's job (FR-09), not Appointment's.

```python
from enum import Enum


class AppointmentStatus(Enum):
    """The only three statuses an appointment can have (FR-05)."""
    BOOKED = "booked"
    CANCELLED = "cancelled"
    COMPLETED = "completed"


class InvalidStatusTransitionError(Exception):
    """Raised when someone tries to change an appointment's status in a way that isn't allowed."""


class Appointment:
    """One patient seeing one GP at a set time (FR-05, FR-06, FR-09)."""

    def __init__(self, appointment_id: int, patient: Patient,
                 practitioner: Practitioner, date_time: datetime) -> None:
        """Sets up a new appointment. Every appointment starts off as BOOKED."""
        if not isinstance(appointment_id, int) or appointment_id <= 0:
            raise ValueError("Appointment ID must be a positive whole number")
        if not isinstance(patient, Patient):
            raise ValueError("An appointment needs a proper Patient")
        if not isinstance(practitioner, Practitioner):
            raise ValueError("An appointment needs a proper Practitioner")
        if not isinstance(date_time, datetime):
            raise ValueError("Appointment time must be a datetime")
        self._appointment_id = appointment_id
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
        """The current status. Read only, so it can only change through cancel() or complete()."""
        return self._status

    def get_status(self) -> AppointmentStatus:
        """Gives back the current status (FR-05)."""
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
```

For this part I used AI like the lab said. I didn't just use the suggested prompt on its own. I also gave it my Appointment UML from Week 6, the status rules and the decisions I'd made in Part A. I especially wanted it to know that booking belongs to Clinic and that cancelling shouldn't mess with the GP's data, because I figured if I didn't say that, it would probably try to do everything inside Appointment.

It gave me the Appointment class, an AppointmentStatus enum with BOOKED, CANCELLED and COMPLETED, and a custom error for illegal status changes. It kept to what I asked. There was no database or notification stuff, and it made status private so it can only change through cancel() or complete(). It also explained the things it added that weren't in my UML, like the custom error and the read-only properties. I didn't just accept it straight away though. I went through all of it in Part E first.

# E - Review Generated Code

Check model consistency, unsupported features, public state mutation, unnecessary inheritance, invented dependencies and error handling.

| Check | What I found in the AI's code | Fix needed? |
|---|---|---|
| Model consistency | Has everything from my UML (all five attributes, cancel(), complete(), get_status()). Status became an enum and the attributes are private, which are changes from the UML | No, but I'll explain them in workbook section 5 |
| Unsupported features | Nothing extra. No database, UI, notifications or service classes, like I asked | No |
| Public state mutation | Status is private with no setter, so it can't be changed from outside. I tried appointment.status = ... and it got blocked | No |
| Unnecessary inheritance | Only the enum inherits from Enum and the error from Exception, which Python needs. Nothing like Appointment inheriting from Patient | No |
| Invented dependencies | Only uses datetime and enum, which are built into Python | No |
| Error handling | Illegal status changes raise the custom error, and bad inputs raise ValueError. But the ID check lets True and False through, because Python counts them as numbers | Yes, fix in G |
| Duplicate method | get_status() and the status property do exactly the same thing | Yes, decide in G |

I went through the AI's code with the checklist from the lab. Honestly, it did pretty well, which I think is because I gave it such a specific prompt. There was nothing I hadn't asked for, no weird inheritance, and it didn't make up any dependencies. The status was properly protected too.

It still wasn't perfect though. When I tested it I found you could make an appointment with True as the ID, because Python treats True as 1. The AI didn't think of that. It also ended up with both get_status() and a status property that do the same thing, just because I had get_status() in my UML. I'll sort both of these out in Part G

# F - Manual Behaviour Checks

Create valid objects, test invalid input, cancel a scheduled appointment and attempt an illegal repeated transition.

```python
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
```

| Check | What I did | Expected | What happened | Pass? |
|---|---|---|---|---|
| Valid objects | Made a patient, a GP and an appointment | All created, appointment starts as BOOKED | Worked, status was BOOKED | Yes |
| Invalid ID | Patient with ID 0 and ID "3" | Rejected | Both rejected with a ValueError | Yes |
| Blank name | Patient with an empty name | Rejected | Rejected with a ValueError | Yes |
| True as ID | Patient with True as the ID | Rejected | Not rejected, the patient got made | No, fix in G |
| Bad patient | Appointment with text instead of a Patient | Rejected | Rejected with a ValueError | Yes |
| Double booking | Checked if the GP is free at 9am while booked | Not free | Not free | Yes |
| Cancel | Cancelled the booked appointment | Becomes CANCELLED, slot is free again, still in history | All three happened | Yes |
| Cancel twice | Cancelled the same appointment again | Error | InvalidStatusTransitionError | Yes |
| Complete after cancel | Tried to complete the cancelled appointment | Error | InvalidStatusTransitionError | Yes |
| Change status directly | Did appointment.status = BOOKED | Blocked | Blocked, no setter | Yes |

I wrote a small script to test everything instead of just reading through the code. It makes a patient, a GP and an appointment, then tries to break them.

Most of it worked how I wanted. Bad IDs and blank names got rejected, and so did making an appointment with plain text instead of a real patient. The double booking check worked too. While the appointment was booked the GP showed as not free at that time, and as soon as I cancelled it the time came free again. The cancelled appointment was still in the patient's list, so the history isn't lost.

The status rules held up as well. Cancelling the same appointment twice gave an error, completing a cancelled one gave an error, and trying to change the status directly got blocked.

The one fail was True as an ID, which got through like I found in Part E. I'm leaving it as a fail here on purpose, because this is what the code did before I fixed it. I'll fix it in Part G and run the script again to check.

# G - Refactor

Remove unnecessary code and make implementation simpler and design-consistent.

**New Helper function:**

```python
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
```

**Before(patient):**

```python
        if not isinstance(patient_id, int) or patient_id <= 0:
            raise ValueError("Patient ID must be a positive whole number")
        if not isinstance(name, str) or not name.strip():
            raise ValueError("Patient name can't be empty")
        self._patient_id = patient_id
        self._name = name.strip()
```

**After(patient):**

```python
        self._patient_id = _check_id(patient_id, "Patient")
        self._name = _check_text(name, "Patient name")
```

**Before(appointment) removed:**

```python
    def get_status(self) -> AppointmentStatus:
        """Gives back the current status (FR-05)."""
        return self._status
```

After testing I had three things to sort out from Part E and F. The first was the True as an ID bug. I made a small helper called \_check_id() that specifically rejects True and False before checking the number, and now all three classes use it for their IDs.

While I was doing that I realised I'd written the same checks over and over. The ID check was in all three classes and the blank name check was in three spots. So I made a second helper, \_check_text(), for names and the specialty. Now each check only lives in one place, and if I ever need to change a rule I only have to change it once. Practitioner and Patient got a lot shorter too.

The last thing was get_status(). It was in my Week 6 UML, but the status property already does exactly the same thing, so having both was just extra code. I kept the property since is_available() already uses it, and deleted get_status(). That's a small change to the UML, so I'll note it in the updated UML section.

I ran my Part F script again after all this and everything passed, including True as an ID, which now gets rejected. The rest still worked exactly the same, so the refactor didn't break anything.

# H - AI Engineering Log

Record prompt, generated contribution, decisions and verification evidence.

**Prompt I gave the AI:**

Act as a Python pair programmer. Implement only the Appointment class from the approved SmartCare UML. Use type hints and an AppointmentStatus enum. Cancelled appointments remain as objects. Do not add database, UI, notification or service classes. Protect status transitions and explain any decision not directly visible in the UML.

Approved UML for Appointment: appointment_id: int, patient: Patient, practitioner: Practitioner, date_time: datetime, status, cancel(), complete(), get_status(). Each appointment has exactly 1 patient and 1 practitioner.

Business rules: status can only be booked, cancelled or completed (FR-05). A booked appointment can be cancelled or completed, but once it's cancelled or completed it can't change again. Cancelling frees up the GP's time slot (FR-06), but Practitioner's is_available() already ignores cancelled appointments, so Appointment shouldn't change the GP's data. Booking and checking if the GP is free is Clinic's job (FR-09), not Appointment's

| What the AI generated | My decision | Why | How I checked it |
|---|---|---|---|
| AppointmentStatus enum with BOOKED, CANCELLED, COMPLETED | Accepted | It's exactly what FR-05 says, and stops status being any random string | Status started as BOOKED and only ever changed to the other two in my Part F tests |
| InvalidStatusTransitionError | Accepted | Makes it obvious when a status change isn't allowed | Cancelling twice and completing a cancelled appointment both raised it (Part F) |
| Private attributes with read-only properties | Accepted | Stops status being changed from outside, which was the whole point of the lab | appointment.status = BOOKED got blocked (Part F) |
| Input checks in the constructor | Modified | The ID check let True and False through | Found it in Part F, fixed it with \_check_id() in Part G, reran the script and it passed |
| Both get_status() and a status property | Modified | They did the same thing, so one was extra code | Deleted get_status() in Part G, reran the script and nothing broke |
| Appointment doesn't check availability or add itself to lists | Accepted | Booking is Clinic's job in my UML (FR-09) | Checked it against my Week 6 UML and CRC cards |

Overall the AI was useful for getting Appointment written quickly, but I don't think it would've been as good if I hadn't given it my UML and rules first. Most of what it made I kept, because it matched my design and the requirements. I changed two things. The True as an ID bug was something the AI missed and I only caught it by actually testing, and get_status() was only there because it was in my UML, even though the property already did the job. I didn't reject anything outright, mostly because the prompt already told it not to add things like a database or notifications. For evidence I ran my Part F test script before and after my changes, and everything passed after the refactor.

# Suggested AI prompt

Act as a Python pair programmer. Implement only the Appointment class from the approved SmartCare UML. Use type hints and an AppointmentStatus enum. Cancelled appointments remain as objects. Do not add database, UI, notification or service classes. Protect status transitions and explain any decision not directly visible in the UML.

# Reflection

Which AI-generated part did you modify or reject? Why? How did the approved design constrain the AI?

**Which AI-generated part did I modify or reject, and why?**

I didn't reject anything completely, but I changed two things. The first one was the ID check. It looked fine when I read it, but when I tested it, True got accepted as an ID because Python counts it as 1. The AI missed that, and to be honest I probably would have too if I hadn't tested it. So I made a helper that doesn't let True or False through.

The other one was get_status(). The AI kept it because it was in my UML, but it also made a status property that does the exact same thing. There was no point having both, so I got rid of get_status().

**How did the approved design constrain the AI?**

Giving it my UML and rules made a big difference. It didn't try to add a database or notifications, and it didn't make Appointment do the booking. In Week 6, when I only gave it the requirements, it added heaps of extra classes, so this time was way better. I think the main thing I learnt is that the AI only sticks to what you tell it. My design kept it on track, but I still had to test it myself to find the stuff it got wrong.

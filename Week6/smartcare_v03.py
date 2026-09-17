# SmartCare v0.3 - class skeletons for Stage 3
# Only the structure for now. The actual logic gets added in a later stage.

from datetime import datetime


class Patient:
    """A patient at the clinic (FR-02, FR-07, FR-10)."""

    def __init__(self, patient_id, name):
        """Sets up a new patient with an ID, a name and no appointments yet."""
        self.patient_id = patient_id
        self.name = name
        self.appointments = []

    def add_appointment(self, appointment):
        """Adds an appointment to this patient's list."""
        pass

    def get_past_appointments(self):
        """Gives back this patient's past appointments (FR-07)."""
        pass


class Practitioner:
    """A GP who works at the clinic (FR-03, FR-04, FR-08)."""

    def __init__(self, practitioner_id, name):
        """Sets up a new GP with an ID, a name, no free times and no appointments yet."""
        self.practitioner_id = practitioner_id
        self.name = name
        self.available_times = []
        self.appointments = []

    def update_details(self, name):
        """Updates the GP's details (FR-03)."""
        pass

    def add_available_time(self, date_time):
        """Adds a time when the GP is free (FR-04)."""
        pass

    def get_availability(self):
        """Gives back the times the GP is free (FR-04)."""
        pass

    def is_available(self, date_time):
        """Checks if the GP is free at a time so there's no double booking (FR-01, FR-09)."""
        pass


class Appointment:
    """One patient seeing one GP at a set time (FR-05, FR-06, FR-09)."""

    def __init__(self, appointment_id, patient, practitioner, date_time):
        """Sets up a new appointment. Every appointment starts off as booked."""
        self.appointment_id = appointment_id
        self.patient = patient
        self.practitioner = practitioner
        self.date_time = date_time
        self.status = "booked"  # can only be booked, cancelled or completed (FR-05)

    def cancel(self):
        """Cancels the appointment and frees up the GP's time slot (FR-06)."""
        pass

    def complete(self):
        """Marks the appointment as completed (FR-05)."""
        pass

    def get_status(self):
        """Gives back the current status (FR-05)."""
        pass


class Clinic:
    """Keeps all the patients, GPs and appointments in one place."""

    def __init__(self):
        """Sets up an empty clinic."""
        self.patients = []
        self.practitioners = []
        self.appointments = []

    def add_patient(self, name):
        """Adds a new patient (FR-02)."""
        pass

    def add_practitioner(self, name):
        """Adds a new GP (FR-03)."""
        pass

    def book_appointment(self, patient, practitioner, date_time):
        """Books an appointment, but only if the GP is free (FR-01, FR-09)."""
        pass

    def search_patients_by_name(self, name):
        """Finds patients by their name (FR-10)."""
        pass

    def appointments_per_practitioner(self):
        """Counts how many appointments each GP has (FR-08)."""
        pass


# Quick test to make sure the classes link up properly
if __name__ == "__main__":
    gp = Practitioner(1, "Dr Smith")
    patient = Patient(1, "Alex Lee")
    appt = Appointment(1, patient, gp, datetime(2026, 9, 21, 10, 0))
    print(appt.patient.name, "is booked with", appt.practitioner.name, "-", appt.status)

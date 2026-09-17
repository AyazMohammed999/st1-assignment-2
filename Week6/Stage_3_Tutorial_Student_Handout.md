# Assignment 2 - Case Study

## Stage 3 Tutorial Activities

**From Requirements to Domain Models**

Week 6 \| 60 minutes

# Candidate Concepts

| Candidate | Class? | Reason |
|---|---|---|
| Patient | Yes | The clinic needs to store patients and look them up (FR-02, FR-10) |
| Practitioner | Yes | We need to keep each GP’s details and when they’re free (FR-03, FR-04) |
| Appointment | Yes | It’s the main thing being booked, cancelled and completed (FR-05, FR-09) |
| Name | No | It’s just a detail about a patient or GP, so it’s an attribute |
| Clinic | Yes | Booking, searching and reports need to see everyone, so it makes sense to have one class that holds everything (FR-08, FR-09, FR-10) |
| Database | No | That’s how the data gets saved (NFR-03), not something in the clinic’s world. It’s a tech detail, not a domain class |
| Cancellation | No | It’s something that happens to an appointment, so it’s a cancel() method that changes the status (FR-06) |
| Status | No | It’s just booked, cancelled or completed, so it works as an attribute on a appointment (FR-05) |

# CRC Cards

## Patient

| Responsibilities                                   | Collaborators |
|----------------------------------------------------|---------------|
| Keep the patient’s ID and name (FR-02, FR-10)      | None          |
| Keep their appointments and show past ones (FR-07) | Appointments  |

## Practitioner

| Responsibilities                                                                       | Collaborators |
|----------------------------------------------------------------------------------------|---------------|
| Keep the GP’s ID and name, and update them when needed (FR-03)                         | None          |
| Keep track of when the GP is free and check if a time is already booked (FR-01, FR-04) | Appointments  |

## Appointment

| Responsibilities                                                                                  | Collaborators         |
|---------------------------------------------------------------------------------------------------|-----------------------|
| Know which patient and GP it’s for, and the date and time (FR-09)                                 | Patient, practitioner |
| Keep its status (booked, cancelled or completed) and free up the slot if cancelled (FR-05, FR-06) | practitioner          |

# Relationship Reasoning

**Patient to Appointment: which relationship and why?**

It's just a normal association. A patient has appointments, but an appointment isn't a kind of patient and it's not really "part" of one either. A patient can have a bunch of appointments or none yet, but each appointment is only for one patient, so it's 1 to 0..* (FR-07, FR-09).

**Practitioner to Appointment: what multiplicity?**

Also 1 to 0..*. A GP could have loads of appointments, or zero if they're new, but every appointment is only ever with one GP (FR-01, FR-09).

**Should Appointment inherit from Patient?**

No. Inheritance is for "is a" relationships, and an appointment definitely isn't a patient, it just points to one. If it inherited from Patient, every appointment would get its own patient ID and name, which would be pretty weird.

**Does Clinic need to own every object?**

I don't think so. Clinic just keeps track of all the patients, GPs and appointments so it can handle booking, searching and reports. A patient doesn't stop existing just because of the clinic class, so I went with aggregation (hollow diamond) instead of composition. I also kept Clinic small so it doesn't turn into one giant class that does everything.

# AI Model Critique

Critique AI proposals: PatientManager, PractitionerManager, AppointmentManager, ClinicController, NotificationManager, ScheduleEngine.

| AI proposal         | My take | Why                                                                                                                                                                                                                        |
|---------------------|---------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| PatientManager      | Reject  | Adding and searching patients is already covered by Clinic (FR-02, FR-10). A whole extra class just to manage patients feels like too much for a small clinic                                                              |
| PractitionerManager | Reject  | Same thing. Clinic already adds GPs, and Practitioner handles its own details and availability (FR-03, FR-04)                                                                                                              |
| AppointmentManager  | Reject  | Clinic already does the booking (FR-09), and Appointment can cancel and complete itself (FR-05, FR-06). This would just split the same jobs into another class                                                             |
| ClinicController    | Modify  | This one's kind of like my Clinic class, so I get the idea. But "controller" sounds like it would run everything, so I kept it as a small Clinic class that only does booking, searching and reports (FR-08, FR-09, FR-10) |
| NotificationManager | Reject  | Reminders and notifications are only provisional, the clinic hasn't confirmed them, so there's no requirement for this                                                                                                     |
| ScheduleEngine      | Reject  | Way too much. FR-04 just needs to show when a GP is free, which a list of free times on Practitioner handles. We also don't know who sets GP hours yet (Open Question 2)                                                   |

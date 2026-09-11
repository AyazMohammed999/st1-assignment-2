# SmartCare Requirements Specification v0.2

## 1. Problem and Scope

SmartCare is a small community clinic that still runs everything on
spreadsheets, paper records and manual processes. This is causing real
problems. Patients get double-booked and end up waiting, staff struggle
to find patient records, and appointment statuses don't always match up,
so patients sometimes turn up for appointments that were cancelled.
There's also no reliable appointment history, and cancelling is done by
hand, so free slots often go to waste. Management wants a simple system
that's easy to maintain and handles patients, practitioners and
appointments. They don't want a big, complicated hospital system.

**In scope:** stopping double bookings, storing and searching patient
records, showing when each GP is free, tracking appointment status,
cancelling appointments and freeing up the slot, keeping appointment
history, and producing basic reports.

**Out of scope:** billing and payments, prescriptions, and test results.

**Provisional (not confirmed yet):** patients booking online themselves,
and appointment reminders.

## 2. Stakeholders

| Stakeholder              | Need                                                                          | Evidence                                                                         |
|--------------------------|-------------------------------------------------------------------------------|----------------------------------------------------------------------------------|
| Patients                 | Reliable appointments without long waits or turning up for cancelled bookings | Brief: duplicate bookings, inconsistent appointment status                      |
| Practitioners (GPs)      | Quick access to patient details and past appointments                         | Brief: difficulty finding patient records, limited appointment history           |
| Reception/staff          | An easy way to book, cancel and see GP availability                         | Case study: manual cancellation, limited visibility of practitioner availability |
| Clinic Management        | A simple, maintainable system with basic reports                              | Brief: “small, maintainable system”                                              |
| Junior Software engineer | Clear, testable requirements to build from                                    | Case study: hired to develop the system in stages                                 |

## 3. Functional Requirements

**FR-01:** The system shall prevent a patient from being booked with a
practitioner at a time that is already taken.

**FR-02:** The system shall allow reception staff to add new patients.

**FR-03:** The system shall allow staff to add and update practitioner
details.

**FR-04:** The system shall display each practitioner’s availability.

**FR-05:** The system shall record the status of each appointment as
booked, cancelled or completed.

**FR-06:** The system shall allow reception staff to cancel an
appointment and make the time slot available again.

**FR-07:** The system shall allow reception staff and practitioners to
view a patient's past appointments.

**FR-08:** The system shall allow management to generate basic reports,
such as the number of appointments per practitioner.

**FR-09:** The system shall allow reception staff to book an appointment
for a patient with a practitioner at an available time.  
**FR-10:** The system shall allow reception staff to search for existing
patient records by name.

## 4. Non-Functional Requirements

**NFR-01 (Usability):** Reception staff shall be able to book an
appointment in under 2 minutes.

**NFR-02 (Data Integrity):** When an appointment's status changes, the
updated status shall appear the same for all users immediately.

**NFR-03 (Reliability):** The system shall save all patient and
appointment data so that nothing is lost if the system crashes or
restarts.

**NFR-04 (Maintainability):** Every function in the system's code shall
include a comment explaining what it does.

## 5. User Stories

US-01: As a receptionist, I want to see which GPs are free, so that I
can book an appointment quickly.

US-02: As a GP, I want to view a patient’s past appointments, so that I
can see when they last visited and which GP they saw.

US-03: As a patient, I want my appointment status to be accurate, so
that I don’t turn up for a cancelled appointment.

US-04: As a Clinic Manager, I want to generate basic reports, so that I
can see how many appointments each GP has.

## 6. Acceptance Criteria

**US-01 (negative)**  
GIVEN Dr Smith already has an appointment at 10am  
WHEN the receptionist tries to book another patient at 10am  
THEN the system rejects the booking and shows a message that the slot is
taken

**US-03**  
GIVEN a patient has a booked appointment on Monday  
WHEN reception cancels the appointment  
THEN the status changes to cancelled and the time slot becomes available
again

**US-04**  
GIVEN Dr Smith has 5 completed appointments this week  
WHEN the manager generates a weekly report  
THEN the report shows Dr Smith with 5 appointments

## 7. Assumptions and Open Questions

**Assumptions**

1.  Reception staff should be able to book an appointment in under 2
    minutes, but this hasn't been confirmed by the clinic.

2.  Staff will search for patients by name.

3.  Only reception staff will book appointments, since the brief doesn't
    mention patients booking online.

**Open questions for the client**

1.  How quickly should reception be able to book an appointment?

2.  Who enters and updates each GP's working hours?

3.  Who is allowed to update practitioner details?

4.  What should staff be able to search for patients by, besides name?

5.  Who marks an appointment as completed, and when?

6.  What reports does management need?

7.  Should patients be able to book online or get reminders?

8.  Who should be able to log in and see patient records?

## 8. AI Requirements Review Record

| AI suggestion                      | Evidence?                                                                            | Decision   | Reason                                                                       | Verification                                                          |
|------------------------------------|--------------------------------------------------------------------------------------|------------|------------------------------------------------------------------------------|-----------------------------------------------------------------------|
| Add an FR for booking appointments | Yes: US-01 needs booking, and the brief asks for appointment management              | Accepted   | US-01 depends on booking, but no FR covered it                               | Checked FR-01 to FR-08; added FR-09                                   |
| NFR-02 repeats FR-01               | Yes: FR-01 and NFR-02 in my own document say the same                                | Modified   | Both prevented double bookings                                               | Rewrote NFR-02 to cover consistent appointment status, from the brief |
| NFR-04 isn’t testable              | Yes: the brief asks for a “maintainable” system, but my wording couldn’t be measured | Accepted   | “Organised and simple” can’t be measured                                     | Changed to: every function must have a comment                        |
| “2 minutes” not from the brief     | No: assumption; the brief gives no time target                                      | Unverified | No stakeholder gave a time target                                            | Checked the brief; listed as an open question                         |
| US-02 claims “health history”      | Yes: the brief says the clinic doesn’t want a complex hospital system                | Accepted   | Past appointments only show visits, the client doesn’t want a complex system | Reworded US-02                                                        |
| Tell patients about cancellations | No: not in the brief; reminders were only provisional | Rejected | The client never asked for notifications | Checked the brief; reminders stay provisional |

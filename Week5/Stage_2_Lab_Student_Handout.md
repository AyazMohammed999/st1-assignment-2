# Assignment 2 – Case Study Lab
## Stage 2 Lab Activities: SmartCare Requirements Engineering

AI OFF -\> AI ON -\> VERIFY \| 1 hour

# Learning objectives

- Analyse the SmartCare client brief.

- Identify stakeholders and scope.

- Write functional and non-functional requirements.

- Develop user stories and Given-When-Then acceptance criteria.

- Use AI to critique requirements without allowing it to invent
  stakeholder needs.

- Produce SmartCare Requirements Specification v1.0.

# Part A - Client Brief: AI OFF

SmartCare uses spreadsheets and paper records. Staff report duplicate
bookings, difficulty finding patient information, inconsistent
appointment status and limited appointment history. Management wants a
small, maintainable patient, practitioner and appointment system.

- SmartCare is a small community clinic that currently manages patients
  and appointments using a combination of spreadsheets, paper records,
  and manual processes.

- Staff have reported several problems, including duplicate appointment
  bookings that cause long waiting times, difficulty finding patient
  records, inconsistent appointment status information that can lead to
  patients arriving for cancelled appointments, and manual cancellations
  that leave slots unused and waste practitioners’ time.

- Management wants a system that is simple and can initially support
  patients, practitioners, and appointment management.

- The clinic does not want a complex hospital information system.

# Part B - Stakeholders and Scope: AI OFF

Identify at least four stakeholders. Create In Scope and Out of Scope
lists. Label uncertain features as provisional rather than confirmed.

- Patients: They want appointments they can rely on, so they’re not
  stuck waiting around or showing up for something that’s been
  cancelled.

- Practitioners (GPs): They need to find a patient’s details quickly when
  they’re seeing them.

- Reception/staff: They need an easy way to book appointments.

- Clinic Management: They want a system that’s simple and easy to keep
  running.

**In Scope**

1.  Prevent double bookings. The app stops two patients being booked
    with the same GP at the same time.

2.  Store and search patient records. The app keeps patients’ details in
    one place so staff and GPs can find them quickly.

3.  Show practitioner availability. The app shows when each GP is free,
    so reception can book patients quickly.

4.  Track appointment status. Each appointment is marked as booked,
    cancelled or completed, so everyone sees the same up-to-date
    information.

5.  Cancel appointments and free up the slots. When an appointment is
    cancelled, the time slot becomes available again for another
    patient.

6.  Keep appointment history. The app saves a record of each patient’s
    past appointments, so staff and GPs can look back at previous
    visits.

7.  Produce basic reports. For example, how many appointments each GP
    had, or how many were cancelled, so management can see how the
    clinic is running.

**Out of Scope**

1.  Billing and payments. The system won’t deal with charging patients
    or processing claims.

2.  Prescriptions. Managing medication isn’t part of a simple booking
    system.

3.  Test results. Lab or blood test results are left out to keep the
    system small.

**Provisional (not confirmed by the client)**

1.  Online booking by patients. The brief doesn’t say whether patients
    can book themselves or only reception can.

2.  Appointment reminders. Reminders by text or email might be useful,
    but the client hasn’t asked for them.

# Part C - Functional Requirements: AI OFF

Write 8-12 numbered functional requirements using FR-01, FR-02 and so
on. Each should describe one observable capability.

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

# Part D - Non-Functional Requirements: AI OFF

Write 4-6 numbered non-functional requirements covering appropriate
qualities such as reliability, maintainability, usability, data
integrity or testability.

**NFR-01 (Usability):** Reception staff shall be able to book an
appointment in under 2 minutes.

**NFR-02 (Data Integrity):** When an appointment's status changes, the
updated status shall appear the same for all users immediately.

**NFR-03 (Reliability):** The system shall save all patient and
appointment data so that nothing is lost if the system crashes or
restarts.

**NFR-04 (Maintainability):** Every function in the system's code shall
include a comment explaining what it does.

# Part E - User Stories and Acceptance Criteria: AI OFF

Write 4-6 user stories. For at least three, create Given-When-Then
acceptance criteria including one negative or failure scenario.

**US-01:** As a receptionist, I want to see which GPs are free, so that
I can book an appointment quickly.

**US-01 acceptance criteria (positive):**

- Given Dr Smith is free at 10am

- When the receptionist books a patient at 10am

- Then the appointment is confirmed and 10am shows as taken

**US-01 acceptance criteria (negative):**

- Given Dr Smith already has an appointment at 10am

- When the receptionist tries to book another patient at 10am

- Then the system rejects the booking and shows a message that the slot
  is taken

**US-02:** As a GP, I want to view a patient's past appointments, so
that I can see when they last visited and which GP they saw.

**US-03:** As a patient, I want my appointment status to be accurate, so
that I don’t turn up for a cancelled appointment.

**US-03 acceptance criteria:**

- Given a patient has a booked appointment on Monday

- When reception cancels the appointment

- Then the status changes to cancelled and the time slot becomes
  available again

**US-04:** As a clinic manager, I want to generate basic reports, so
that I can see how many appointments each GP has.

**US-04 acceptance criteria:**

- Given Dr Smith has 5 completed appointments this week

- When the manager generates a weekly report

- Then the report shows Dr Smith with 5 appointments

# Part F - AI Requirements Review: AI ON

Prompt: Act as a software requirements reviewer. Review the SmartCare
requirements for ambiguity, inconsistency, missing clarification
questions and testability. Do NOT invent new client requirements. For
every suggestion, state whether it is based on evidence or is only a
question/assumption requiring validation.

**Part F – AI Requirements Review**  
*Prompt used: the handout's Part F prompt. Each suggestion is tagged*
**\[Evidence\]** *(based on the brief or on the document) or*
**\[Question\]** *(an assumption to confirm with the client).*

**1. Missing FR for booking an appointment (gap)**  
FR-01 prevents double bookings, but no FR says staff can actually
*create* a booking. US-01 and NFR-01 both depend on booking.  
Suggestion: add an FR for booking a patient with a practitioner at a
chosen time. **\[Evidence\]** The brief asks for appointment management,
and US-01 relies on it.

**2. NFR-02 repeats FR-01 (inconsistency)**  
Both say no double bookings. Preventing double bookings is something the
system *does*, so it's functional.  
Suggestion: keep FR-01, and replace NFR-02 with a different quality,
e.g. testability. **\[Evidence\]** Comparing FR-01 and NFR-02.

**3. NFR-04 isn't testable (ambiguity)**  
"Organized," "simple" and "easily" can't be measured.  
Suggestion: add a measurable check, e.g. code comments on every
function, or a new developer can make a small change within a set time.
**\[Evidence\]** The brief asks for "maintainable." **\[Question\]** The
exact measure needs agreeing.

**4. NFR-01's "2 minutes" isn't from the brief**  
The number is reasonable, but no stakeholder gave it.  
Suggestion: confirm the target with reception staff. **\[Question\]**

**5. FR-02 combines two capabilities**  
Adding patients and searching records are separate things. The handout
says each FR should describe one capability.  
Suggestion: split it into two FRs. Also, search by what (name, date of
birth)? **\[Evidence\]** The handout rule. **\[Question\]** The search
fields.

**6. FR-04 "availability" isn't defined**  
Where do GP working hours come from, and who sets them? No FR covers
entering a GP's schedule.  
Suggestion: clarify whether FR-03's "practitioner details" include
working hours. **\[Question\]**

**7. "Staff" is inconsistent**  
FR-02 and FR-06 say "reception staff," FR-03 and FR-07 just say "staff."
Does "staff" include GPs? US-02 needs GPs to view past appointments, but
FR-07 doesn't clearly allow it.  
Suggestion: name the exact role in each FR. **\[Evidence\]** Comparing
FR-07 and US-02.

**8. US-02 may overreach**  
Past appointments show *when* a patient visited, not their "health
history." Medical notes would push toward the complex hospital system
the client doesn't want.  
Suggestion: reword to "see when the patient last visited and with which
GP." **\[Evidence\]** The brief excludes complex hospital systems.

**9. FR-05 "completed": who marks it?**  
There's no FR for changing status to completed, or saying when that
happens.  
Suggestion: ask the client who updates it. **\[Question\]**

**10. FR-08 reports are vague**  
"Basic reports, such as..." isn't testable without knowing which reports
are required.  
Suggestion: confirm the report list with management. **\[Question\]**
The brief only says "basic operational reports."

**11. US-03: how does the patient find out?**  
The acceptance criteria test the status changing in the system, but not
that the patient knows about it. This links to the provisional
reminders.  
Suggestion: ask the client how patients should be told about
cancellations. **\[Question\]**

**12. Privacy and access not mentioned**  
Patient records are sensitive, but nothing covers who can log in or see
them. Not added as a requirement.  
Suggestion: raise it as an open question. **\[Question\]** It's not in
the brief.

**Minor wording fixes:** "Billings" → "Billing"; "appointments data" →
"appointment data"; "practitioners availability" → "practitioner
availability"; capitalise "The" in FR-03 and FR-04.

# Part G - VERIFY the AI Review

Classify each significant AI suggestion as Accepted, Modified, Rejected,
or Unverified. Explain the evidence used.

**Point 1 – Accepted:** None of FR-01 to FR-08 lets staff book an
appointment, even though US-01 depends on it. I will add FR-09: The
system shall allow reception staff to book an appointment for a patient
with a practitioner at an available time.

**Point 2 – Modified:** I agree NFR-02 repeats FR-01, since both only
prevent double bookings. Instead of replacing it with testability, I
will rewrite NFR-02 as a data integrity requirement linked to the
brief's "inconsistent appointment status" problem: NFR-02 (Data
Integrity): When an appointment's status changes, the updated status
shall appear the same for all users immediately.

**Point 3 – Accepted:** "Organized" and "simple" can't be measured, so
NFR-04 can't be tested as written. The brief does ask for a maintainable
system, so I will keep the requirement but make it testable: NFR-04
(Maintainability): Every function in the system's code shall include a
comment explaining what it does.

**Point 4 – Unverified:** The brief never gives a time target, so "2
minutes" is my own assumption, not stakeholder evidence. I will keep
NFR-01 for now but list it as an open question to confirm with reception
staff.

**Point 5 – Accepted:** FR-02 combines two capabilities, adding patients
and searching records, but the handout says each FR should describe one.
I will split it into FR-02: The system shall allow reception staff to
add new patients, and FR-10: The system shall allow reception staff to
search for existing patient records by name. Searching by name is my
assumption, so I will confirm the search fields with the client.

**Point 6 – Unverified:** The brief doesn't say how GP availability is
set or where working hours come from, so FR-04 relies on information I
don't have. I will keep FR-04 and list "Who enters each GP's working
hours?" as an open question for the clinic.

**Point 7 – Modified:** I agree "staff" is unclear, especially since
US-02 needs GPs to view past appointments but FR-07 doesn't clearly
allow it. I will change FR-07 to: The system shall allow reception staff
and practitioners to view a patient's past appointments. I will leave
FR-03 as "staff" for now, because the brief doesn't say who updates
practitioner details, and I will add that as an open question.

**Point 8 – Accepted:** Past appointments only show when a patient
visited and which GP they saw, not their health history. Storing medical
notes would move toward the complex hospital system the client doesn't
want. I will reword US-02 to: As a GP, I want to view a patient's past
appointments, so that I can see when they last visited and which GP they
saw.

**9. (Part F Point 11) – Rejected:** US-03 is about the appointment
status being accurate in the system, and the acceptance criteria already
test that. Telling patients about cancellations would need
notifications, which the client hasn't asked for. I listed reminders as
provisional in Part B, so I won't add a notification requirement without
client evidence.

# Part H - Finalise SmartCare v0.2

Submit stakeholder analysis, scope, 8-12 FRs, 4-6 NFRs, 4-6 user
stories, acceptance criteria, assumptions/open questions and selected AI
review evidence.

This is SmartCare Requirements Specification v0.2. It brings together
the stakeholders and scope, 10 functional requirements, 4 non-functional
requirements, and 4 user stories with acceptance criteria, all updated
after the AI review. The AI review and my decisions on each suggestion
are included in Parts F and G.

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

# Reflection

In 150-250 words: What did AI notice that you missed? What did AI invent
or overreach on? Which requirement changed after review? Why must
requirements have evidence?

Honestly, the AI caught something I completely missed. I didn't have a
requirement for actually booking an appointment, which is kind of the
main point of the system. Even my user story US-01 needed it. I think I
was so busy fixing the clinic's problems, like double bookings and
cancellations, that I forgot the basic stuff. But the AI also went too
far once. It said patients should get told when their appointment is
cancelled. That sounds like a good idea, but the client never asked for
it, and I'd already put reminders as provisional in Part B. So, I
rejected it, because I didn't want to make up requirements the
client never gave. I changed a few things after the review. The one that
helped most was NFR-04. Before, it just said the code should be
"organized and simple," but you can't really test that. Now every
function needs a comment, which is easy to check. I also changed US-02
so it doesn't say it shows a patient's health history. This lab taught
me that requirements need evidence. If they don't, you might build stuff
the client doesn't want, waste time and money, and make the system way
too complicated.

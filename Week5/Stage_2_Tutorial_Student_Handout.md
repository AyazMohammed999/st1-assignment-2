# Stage 2 Tutorial – SmartCare Requirements

Week 5 \| 60 minutes

# Learning goals

- Analyse stakeholders.

- Distinguish functional and non-functional requirements.

- Recognise ambiguity and unsupported requirements.

- Define scope.

- Develop user stories and acceptance criteria.

- Critique AI-generated requirements.

# Activity 1 - Stakeholder Map

| Stakeholder         | Need                                                 | Potential conflict                                                            |
|---------------------|------------------------------------------------------|-------------------------------------------------------------------------------|
| Patients            | Reliable appointments without long waits             | May want online booking or reminders, but management wants a simple system    |
| Practitioners (GPs) | Quick access to patients’ details and their schedule | May want detailed patient notes, which pushes toward a complex system         |
| Reception staff     | Fast, easy booking and cancelling                    | May want to squeeze in urgent patients, but the system blocks double bookings |
| Clinic management   | A simple, maintainable system with reports           | Wants to keep it small, while staff may ask for more features                 |
| Software engineer   | Clear, testable requirements                         | Stakeholders often describe needs vaguely, like “easy to use”                 |

# Activity 2 - Functional or Non-Functional?

☒ Functional □ Non-functional The system shall
allow staff to cancel an appointment.

□ Functional ☒ Non-functional The system
should remain responsive for the course-scale dataset.

☒ Functional □ Non-functional The system shall
retain cancelled appointments.

□ Functional ☒ Non-functional Core business
logic should be independently testable.

☒ Functional □ Non-functional The system shall
search for a patient by ID.

# Activity 3 - Repair Ambiguous Requirements

The system should be easy to use.

Problem: “easy” can’t be measured.  
Clarification question: How long
should it take a new receptionist to book an appointment?

Patient search should be fast.

Problem: “fast” isn’t defined.  
Clarification question: How many seconds
should search results take to appear?

The system should securely manage data.

Problem: “Securely” doesn’t say what’s protected or from whom.
Clarification question: Who should be allowed to see and change patient
records?

Appointments should normally be easy to cancel.

Problem: “normally” suggests exceptions that aren’t stated.
Clarification question: Are there times cancelling isn’t allowed, like
on the same day?

# Activity 4 - AI Requirements Audit

Classify each suggestion: Confirmed / Assumption requiring validation /
Unsupported / Out of scope.

| AI suggestion                             | Classification                   | Evidence / reason                                                               |
|-------------------------------------------|----------------------------------|---------------------------------------------------------------------------------|
| Patients receive SMS reminders.           | Assumption requiring validation | Might help with cancellations, but the client never asked for it                |
| Facial recognition login.                 | Unsupported                      | Nothing in the brief; far too complex for a small clinic                         |
| Receptionists create appointments.        | Confirmed                        | The brief asks for appointment management                                       |
| Online payment.                           | Out of scope                     | Billing isn’t part of the brief, and the client doesn’t want a complex system   |
| Practitioners view schedules.             | Confirmed                        | The brief lists limited visibility of practitioner availability                 |
| AI recommends treatments.                 | Out of scope                     | That’s clinical decision-making, like a hospital system the client doesn’t want |
| Cancelled appointments remain in history. | Confirmed                        | The brief lists inconsistent status and lack of reliable appointment history    |

# Exit question

Why is 'AI suggested it' not sufficient evidence for a requirement?

Just because the AI suggested something doesn’t mean the client actually
needs it. The AI doesn’t know the clinic, so it can come up with stuff
that sounds good but nobody asked for, like facial recognition or online
payments. If we added those, we’d waste time and money and end up with a
way more complicated system than the clinic wants. Requirements should
come from the brief or real stakeholders, so anything the AI suggests
needs to be checked first.

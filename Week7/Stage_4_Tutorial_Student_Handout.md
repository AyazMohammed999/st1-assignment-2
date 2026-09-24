# Assignment 2 – Case Study

## Stage 4 Tutorial Activities

**Object-Oriented Design Decisions**

Week 7 | 60 minutes

# Activity 1 - Encapsulation Review

| Class | Protected state / invariant | Public operations |
|---|---|---|
| Patient | ID, name and appointment list are private. The ID has to be positive and the name can't be blank. The list only has their own appointments | add_appointment(), get_past_appointments(), and read-only patient_id, name and appointments |
| Practitioner | ID, name, specialty, free times and appointment list are private. The ID has to be positive, the name and specialty can't be blank, and a GP can't be double booked | update_details(), add_available_time(), add_appointment(), is_available(), get_availability(), and read-only practitioner_id, name, specialty and appointments |
| Appointment | ID, patient, GP, time and status are private. Status can only be BOOKED, CANCELLED or COMPLETED, and once it's cancelled or completed it can't change | cancel(), complete(), and read-only appointment_id, patient, practitioner, date_time and status |

# Activity 2 - Composition or Inheritance?

Appointment and Patient -> ☑ Composition/association  □ Inheritance  Reason: An appointment isn’t a patient, it just has one. One patient can have heaps of appointments but each appointment is only for one person

Appointment and Practitioner -> ☑ Composition/association  □ Inheritance  Reason: Same idea as patient. The appointment is with a GP, it’s not a type of GP. And the GP doesn’t go anywhere if the appointment gets cancelled

Doctor and Practitioner (hypothetical) -> □ Composition/association  ☑ Inheritance  Reason: A doctor is a kind of practitioner, so this one actually works as inheritance. I’d only bother though if a Doctor had to do something different. If it’s just a different title, the specialty attribute already does that.

Clinic and Appointment -> ☑ Composition/association  □ Inheritance  Reason: Clinic just keeps track of the appointments so it can book them and count them for reports. An appointment isn’t a kind of clinic, so inheritance doesn’t make sense here.

# Activity 3 - Responsibility Allocation

Who decides whether SCHEDULED can become CANCELLED?

The Appointment itself. It knows what its status is, so cancel() checks it's still booked first. If it's already cancelled or done, it just throws an error. (I called it BOOKED in my code, not SCHEDULED, but it's the same thing.)

Who validates a patient name?

Patient. It checks the name when the patient gets made, and if it's blank you get an error, so there's never a patient without a name.

Should Appointment execute SQL? Why?

No. Appointment should only worry about its own stuff, like its status. Saving to a database is a whole different job. If the SQL was in there, every time the database changed I'd have to go back and change Appointment too, and it'd be a pain to test.

Should the UI decide whether a status transition is legal?

No. The UI is just there to show things and send through what the user clicks. If the rule lived in the UI, anything that didn't go through the UI could get around it. Having it in Appointment means it always gets checked.

# Activity 4 - AI Code Critique

AI generates an Appointment class with public status mutation, SQL inside cancel(), a NotificationManager dependency and inheritance from PatientRecord. Identify at least five design problems and corrections.

| Problem | Why it's a problem | How I'd fix it |
|---|---|---|
| Status is public | Anyone can just do appointment.status = whatever, even a typo or an illegal change like cancelled back to booked | Make status private and only let it change through cancel() and complete() |
| No checks on status changes | Because anything can set the status, nothing stops you cancelling the same appointment twice | Put the rules in cancel() and complete() so they only work from BOOKED, and throw an error otherwise |
| SQL inside cancel() | Appointment shouldn't be talking to the database. Now it's doing two jobs, and it's hard to test without a real database | Take the SQL out. Saving can be handled somewhere else later, and Appointment just changes its own status |
| Depends on NotificationManager | Notifications aren't even a confirmed requirement, they're still provisional. It also means you can't make an Appointment without dragging this other class in | Get rid of it. If notifications get confirmed later, something outside Appointment can handle them |
| Inherits from PatientRecord | An appointment isn't a patient record, so it fails the "is a" test. It'd also end up with patient stuff like names that it shouldn't have | Remove the inheritance and just store a link to the Patient instead |
| cancel() does way too much | Changing status, running SQL and sending notifications all in one method makes it messy, and if one part breaks the whole cancel breaks | Keep cancel() tiny so it just checks and changes the status |

# Exit question

Why can code be object-oriented syntactically but still have poor object-oriented design?

Just because something has classes and methods doesn't mean it's designed well. You can have a class where everything's public so anything can mess with it, or a class that does way too much, like the AI's Appointment running SQL and sending notifications. You can also use inheritance where it doesn't make sense, like Appointment inheriting from PatientRecord when an appointment obviously isn't a patient record. It still looks like OO code, but it's messy and pretty easy to break.

For me good OO design is more about each class looking after its own stuff and only doing its own job, and only using inheritance when something actually is a type of something else. I found that with my own code too. Writing the classes was the easy bit. Working out what each one should and shouldn't do was the hard part.

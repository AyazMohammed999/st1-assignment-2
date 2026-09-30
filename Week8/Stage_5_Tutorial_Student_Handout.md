# Assignment 2- Case Study (8995-G level Task)

## Stage 5 Tutorial Activities

**Architecture and Responsibility**

Week 8 | 60 minutes

# Activity 1 - Where Does This Belong?

| Responsibility | Layer | Reason |
|---|---|---|
| Read menu input | Presentation | Reading what the user types is the menu's thing. Nothing else should be calling input() |
| Check appointment status transition | Domain | Appointment knows its own status, so it's the one that decides if it can be cancelled or completed |
| Coordinate booking use case | Service | Booking is a few steps in a row, like checking the GP's free, making the appointment and saving it. That's what the service is for |
| Execute SQLite INSERT | Persistence | Saving stuff to the database is a storage job, so it goes in the class that actually stores things |
| Format confirmation message | Presentation | How the message looks is up to the menu. The service just gives back the appointment and the menu makes it look nice |
| Find appointment by ID | Repository | That's literally get_by_id() in the contract. The persistence class does the actual searching |

# Activity 2 - Architecture Smell Hunt

A SmartCare file contains input(), SQL, appointment conflict rules, printing and validation. Identify at least five architecture problems and propose a layer for each responsibility.

| Problem | Why it's bad | Where it should go |
|---|---|---|
| input() is mixed in with the logic | You can't test the booking without someone typing stuff in, and you can't reuse it anywhere else | Presentation |
| SQL is written straight into the file | If the database changes, you have to dig through all the other code to fix it | Persistence, behind a repository |
| Appointment conflict rules are in the same file | The "is this GP already booked" rule is buried with everything else, so it's easy to break when changing something unrelated | Domain (is_available()), with the service calling it |
| print() everywhere | The results can only ever be shown one way, and it's mixed in with the actual work | Presentation |
| Validation is done in the file instead of the classes | Other parts of the code could skip it and create bad data | Domain, checked when the object gets created |
| One file doing all of it | Every little change means touching the same file, which is a massive pain and easy to mess up | Split across the five layers |

# Activity 3 - SOLID Without Overengineering

ClinicManager handles every use case. Which principle is threatened?

SRP. If one class is doing booking, cancelling, searching and reports, it's got way too many jobs. Every time you change one thing, you risk breaking something else in there. My Week 6 Clinic idea was heading the same way, which is why I split it up into a service and a repository.

AppointmentService imports sqlite3 directly. What dependency concern exists?

That's a DIP problem. The service would be stuck with SQLite forever, and you couldn't even test it without a real database. It should just talk to the repository, and let the persistence class worry about sqlite3.

A repository interface has 20 methods but a client needs two. What concern exists?

ISP. The client is stuck depending on 18 methods it doesn't even use, and whatever implements it has to write all 20 anyway. That's why I kept mine to just three.

Should every class have an interface? Explain.

No. It's only worth it if you might actually swap something out, like the repository, since that could be a database later. My AppointmentService only has one version, so an interface would just be another file sitting there. Putting them on everything just makes the code harder to read for no reason.

# Activity 4 - AI Architecture Critique

AI proposes microservices, an event bus, six interfaces and a dependency-injection framework. Decide what to reject, defer or keep using current requirements.

| AI proposal | Decision | Why |
|---|---|---|
| Microservices | Reject | SmartCare is one small clinic app. Splitting it into separate services would mean networking, deployment and way more stuff to go wrong, for no real benefit |
| Event bus | Defer | Nothing in SmartCare needs to react to events right now. If appointment reminders get confirmed later, it might be worth looking at, but not yet |
| Six interfaces | Keep one, reject the rest | The AppointmentRepository interface makes sense since storage could change. The others would just be extra files for classes that only have one version |
| Dependency-injection framework | Reject | main.py already plugs everything together in like five lines. A whole framework for that is massive overkill |

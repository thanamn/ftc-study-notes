# 2110473 Fault Tolerant Computing — Full Slide Corpus

> Extracted from born-digital lecture PDFs with PyMuPDF (exact text, no OCR).

> Every slide is tagged; `visual: true` slides have a rendered image in `images/` so diagrams and tables stay readable.

# FTC_Weekly_plan

> Source: `2026S1_FTC_Weekly_plan-9294-17857197396820.pdf` — 1 slides. `visual: true` slides have a rendered image in `images/`.

## Slide 1: Date 1  *(visual)*
Week Chapter Class Assignment
2026-08-03 1 Adminstrative issues Eng3-421
2026-08-10 2 FTC01 Dependable Computing TBA 1
2026-08-17 3 FTC02 Fault Tolerant Systems TBA 2
2026-08-24 4 FTC02plus Checkpointing and Recovery TBA 3
2026-08-31 5 FTC03 Coding Theory TBA 4
2026-09-07 6 FTC04 Self Checking TBA 5
2026-09-14 7 FTC05 Fault Masking and Recovery TBA 6
2026-09-21 8 Midterm week
2026-09-28 9 Review ZOOM
2026-10-05 10 Review ZOOM
2026-10-12 11 MIDTERM TEST TBA
2026-10-19 12 TDC01 Overview of Testing Digital Circuits ZOOM 7
2026-10-26 13 TDC02 Delay Fault Testing ZOOM 8
2026-11-02 14 TDC03 Digital Circuit Testing Issues ZOOM 9
2026-11-09 15 TDC04 Asynchronous Circuit Testing ZOOM 10
2026-11-16 16 Review ZOOM FINAL ASSIGNMENT
2026-11-23 Final week (as of Aug.03, 2025)
![FTC_Weekly_plan slide 1](images/FTC_Weekly_plan_s001.png)


---

# FTC01_Dependable_Computing

> Source: `2110473_2026S1_FTC01_Dependable_Computing-9294-17866170220682.pdf` — 72 slides. `visual: true` slides have a rendered image in `images/`.

## Slide 1  *(visual)*
1
![FTC01_Dependable_Computing slide 1](images/FTC01_Dependable_Computing_s001.png)

## Slide 2: Contact
• MyCourseVille:

 2110473(2026/1) FAULT TOLERANT COMPUTING [Section21&51]
 passwd: 2110473
 • Discord:
 https://discord.gg/q7uGHkGSw
 • Office Hours:
 room: #18-04, Bld: Eng.no.4, Fri 9.30-11.00
 • Others:
 arthit.t@chula.ac.th
 FB messenger: Arthit Thongtak

## Slide 3: Weekly Plan (tentative)  *(visual)*
Date 1 Week Chapter Class Assignment
2026-08-03 1 Adminstrative issues Eng3-421
2026-08-10 2 FTC01 Dependable Computing TBA 1
2026-08-17 3 FTC02 Fault Tolerant Systems TBA 2
2026-08-24 4 FTC02plus Checkpointing and Recovery TBA 3
2026-08-31 5 FTC03 Coding Theory TBA 4
2026-09-07 6 FTC04 Self Checking TBA 5
2026-09-14 7 FTC05 Fault Masking and Recovery TBA 6
2026-09-21 8 Midterm week
2026-09-28 9 Review ZOOM
2026-10-05 10 Review ZOOM
2026-10-12 11 MIDTERM TEST TBA
2026-10-19 12 TDC01 Overview of Testing Digital Circuits ZOOM 7
2026-10-26 13 TDC02 Delay Fault Testing ZOOM 8
2026-11-02 14 TDC03 Digital Circuit Testing Issues ZOOM 9
2026-11-09 15 TDC04 Asynchronous Circuit Testing ZOOM 10
2026-11-16 16 Review ZOOM FINAL ASSIGNMENT
2026-11-23 Final week (as of Aug.03, 2025)
![FTC01_Dependable_Computing slide 3](images/FTC01_Dependable_Computing_s003.png)

## Slide 4: Dependable Computing
*
 Concepts, Limits, Challenges

 2110473 Fault Tolerant Computing

* Jean-Claude Laprie, Invited Paper to FTCS-25, CAL USA, Jun27-30, 1995, Special Issue pp.42-54

## Slide 5: Introduction
• Increasingly Depended on Computing Systems
• However, This Dependency felt upon Failures
 - Telephone Outage in USA, 1990
 - Credit Card Denial of Authorization in FRA, 1993
 - London Ambulance Service Failure, 1992 etc
• Computing finally resulted in both Benefits &
 Costs

• "What are the Limits of Computing Systems
 Dependability?"
• "What are the Challenges?"

## Slide 6: Dependability Concept
• Definitions of Dependability
 - [classic '60] The Probability that a System will
 operate when needed
 - [review '95] Integrative Concept
 - The Property of a Computer System such that
 • Delivery of Service that can justifiably be Trusted
 - Availability, reliability, safety, confidentiality, integrity,
 maintainability, that are then attributes of dependability
 • Avoidance of Service failures that are unacceptably
 frequent or severe
 - Frequency & severity, criterion, dependability failure

 Basic Concepts and Taxonomy of Dependable and Secure Computing; Avizienis, Laprie, Randell,
 and Landwehr; IEEE Trans.on Dependable and Secure Computing, Vol.1, No.1 6

## Slide 7: Avoidance of Service Failures
• Failure Frequency & Severity
 Risk Assessment & Management
• Criterion for System Dependable even of
 Service Failures
• Unacceptably Frequent or Severe Service
 Failures
 Dependability Failure, Connected to
 Development Process Failure

## Slide 8: Classifications of Dependability
• Properties which are expected from the
 Systems:
 - Dependability Attributes
• Methods/Techniques to provide the Abilities:
 - Dependability Means
• Causes or Resulting from Un-Dependability:
 - Dependability Threats/Impairments

## Slide 9: Dependability:  *(visual)*
Attributes, Means and Impairments
![FTC01_Dependable_Computing slide 9](images/FTC01_Dependable_Computing_s009.png)

## Slide 10: Dependability Attributes
• Property-based Attributes
 - Availability, Reliability, Safety, Confidentiality,
 Integrity, Maintainability
• Event-based Attributes
 - Robustness, Survivability, Resilience
• Attributes based on meta-information
 - Accountability, Authenticity, Non-Repudiability

## Slide 11: Property-based Attributes
• Availability
 - The Readiness for Usage
• Reliability
 - The Continuity of Service
• Safety
 - The Non-occurrence of Catastrophic on the environment
• Confidentiality
 - The Non-occurrence of Unauthorized Disclosure of information
• Integrity
 - The Non-occurrence of Improper Alterations of Information
• Maintainability
 - The ability to Undergo Repairs & Evolutions

 ** Security: Availability & Integrity wt respect to Authorized Actions,
 together wt Confidentiality

## Slide 12: Examples of Attributes  *(visual)*
Type Availability Reliability Safety Integrity Maintainab
 of ility
 system

Aircraft
 X X X X Xsystems

Nuclear
 X X X Xreactor

Internet
 X X X XNews page

Smart
 X X X XPhone
Pace Maker X X X X

Automobile
 X X X XSystem
![FTC01_Dependable_Computing slide 12](images/FTC01_Dependable_Computing_s012.png)

## Slide 13: Historical Evolution  *(visual)*
13
![FTC01_Dependable_Computing slide 13](images/FTC01_Dependable_Computing_s013.png)

## Slide 14: Dependability and Security  *(visual)*
14
![FTC01_Dependable_Computing slide 14](images/FTC01_Dependable_Computing_s014.png)

## Slide 15: Availability
• a ratio of the expected value of the uptime of
 a system to the aggregate of the expected
 values of up and down time

## Slide 16: Example of Availability
- If we are using equipment which has a mean time to
 failure (MTTF) of 81.5 years and mean time to
 repair (MTTR) of 1 hour:
- MTTF in hours = 81.5*365*24=713940 (This is a
 reliability parameter and often has a high level of
 uncertainty!)
- Inherent Availability (Ai) = MTTF/(MTTF+MTTR) =
 713940/713941 =99.999859%
- Inherent Unavailability = 0.000141%
- Outage due to equipment in hours per year = 1/rate =
 1/MTTF = 0.01235 hours per year

## Slide 17: Nines of Availability  *(visual)*
17
![FTC01_Dependable_Computing slide 17](images/FTC01_Dependable_Computing_s017.png)

## Slide 18: Reliability  *(visual)*
• The ability of an item to perform a required
 function under stated conditions up until
 specified time
![FTC01_Dependable_Computing slide 18](images/FTC01_Dependable_Computing_s018.png)

## Slide 19: Reliability vs Availability
• They are not the same …
• Example:
 A system that fails, on average, once per
hour but which restarts automatically in ten
mil.secs.
 Non-reliable
 but highly available

## Slide 20: Failure Metrics  *(visual)*
20
![FTC01_Dependable_Computing slide 20](images/FTC01_Dependable_Computing_s020.png)

## Slide 21: Design Tradeoffs  *(visual)*
21
![FTC01_Dependable_Computing slide 21](images/FTC01_Dependable_Computing_s021.png)

## Slide 22: Safety
• "The most important things cannot be
 measured." - W. Edwards Deming
• "Not everything that counts can be counted,
 and not everything that can be counted
 counts." - Albert Einstein
• Lost time injury/incident frequency rates
 (LTIFR)

 ( Number of lost time injuries in accounting period )
 ( Total hours worked in accounting period )

## Slide 23: Safety (cont.)  *(visual)*
23
![FTC01_Dependable_Computing slide 23](images/FTC01_Dependable_Computing_s023.png)

## Slide 24: Risk  *(visual)*
24
![FTC01_Dependable_Computing slide 24](images/FTC01_Dependable_Computing_s024.png)

## Slide 25: Reliability vs Availability vs Safety
• They are not the same …
• Example:
 A system that is turned off …
 not reliable, not available, but safe

## Slide 26: CIA Triad
• A model designed to guide policies for
 information security within an organization

 • Confidentiality is a set of rules
 that limits access to information
 • Integrity is the assurance that the
 information is trustworthy and
 accurate
 • Availability is a guarantee of
 reliable access to the information
 by authorized people

## Slide 27: Confidentiality
• Prevent sensitive information from reaching the
 wrong people, while making sure that the right
 people can in fact get it
• Confidentiality →Information; Privacy →People
• Confidentiality methods (Social Engineering):
 - Data encryption, IDs and passwords
 - Two-factor authentication
 - Biometric verification
 - Security tokens, Key fobs or soft tokens

## Slide 28: Integrity
• Integrity involves maintaining the consistency,
 accuracy, and trustworthiness of data over its entire
 life cycle
• Data Integrity →Overall aspects
 Data Security →Unauthorized parties
• Physical Integrity:
 - Redundant hardware, UPS
 - RAID, Error-correcting codes
 - Cryptographic hash function, Watchdog timer
• Logical Integrity:
 - File permission, Access control, Version control
 - Referential integrity and entity integrity in a relational database
 - Software bugs, Design flaws, Human errors 28

## Slide 29: Data Quality VS Data Integrity
• Data Quality: refer to whether data is useful
 - Completeness - The data present is a large percentage of the total amount of data
 needed.
 - Uniqueness - Unique data sets are free of redundant or extraneous entries.
 - Validity - Data conforms to the syntax and structure defined by the business
 requirements.
 - Timeliness - Data is up to date or relevant to the timelines referenced by the business
 requirements.
 - Accuracy - Data accurately describes the real-world context it refers to.
 - Consistency - Data is consistent throughout the dataset.
• Data Integrity: refer to whether data is trustworthy
 - Physical Integrity - Utilizing data is difficult when there are problems either storing or
 retrieving it. It raises questions about the data's completeness, accuracy, and validity.
 The physical integrity of data hardware can become compromised due to age,
 malfunction, maintenance problems, natural disasters, or power outages.
 - Logical Integrity - Data becomes illogical when it is incorrect or irrational in some way.
 Data has to "make sense" for its context. Otherwise, it distorts the perspective of
 anyone basing decisions off the data. Logical problems can happen because of design
 flaws, human errors, or software bugs.

## Slide 30: RAM/RMA
• Reliability + Availability + Maintainability
• System design attributes that impacts on the
 sustainment or total Life Cycle Costs (LCC) of a
 developed system
• Test Data under RAM concept includes:
 - Software Functionality
 - Operational Quality
 - Known Remaining Defects (defect density)
 - Testing Scope and Stability
 - Reliability

## Slide 31: Classification of Maintenance
• Breakdown Maintenance/ Repair
 - Perform system maintenance/repair after breakdown
• Time-based (Preventive) Maintenance
 - Perform system maintenance periodically
• Condition-based (Preventive) Maintenance
 - Perform system maintenance upon the specified
 conditions
• Predictive Maintenance
 - Predict the life of system components in order to
 perform system maintenance before breakdown

## Slide 32: Event-based Attributes
• Robustness
 - Persistence of Dependability wrt External Faults
• Survivability
 - Persistence of Dependability in the presence of
 Active Fault(s)
• Resilience
 - Persistence of Dependability when facing
 Functional, Environmental, or Technological
 Changes

## Slide 33: Robustness & Stability
• Commonalities:
 - Defined for specified features of a given system, with specified
 perturbations being applied to the system
 - Both are concerned with the persistence
• Differences:
 - Robustness addresses behavior in a more varied class of
 systems, perturbations, & features of persistence
 - Robustness lies outside the purview of stability including
 organizational architecture, interplay btw organization &
 dynamics, relation to evolvability in the past and future, ability
 of the system to switch among multiple functionalities, & so on

 Robustness beyond Stability

## Slide 34: Characteristics of Resilient Systems  *(visual)*
• Latitude: the maximum amount a
 system can be changed before losing
 its ability to recover (before crossing a
 threshold which, if breached, makes
 recovery difficult or impossible)
 • Resistance: the ease or difficulty of
 changing the system; how "resistant"
 it is to being changed
 • Precariousness: how close the current
 state of the system is to a limit or
 "threshold"
 • Panarchy: the degree to which a
 certain hierarchical level of an
 ecosystem is influenced by other levels

 Closely linked to Adaptive Capacity
![FTC01_Dependable_Computing slide 34](images/FTC01_Dependable_Computing_s034.png)

## Slide 35: Attributes based on meta-information
• Accountability
 - Availability and Integrity of the Person who
 performed an Operation
• Authenticity
 - Integrity of Message Content & Origin, & Possibly
 some other info, such as Time of Emission
• Non-Repudiability
 - Availability & Integrity of the Identity of the
 Sender of a Message, or of the Receiver

## Slide 36: Dependability:  *(visual)*
Attributes, Means and Impairments
![FTC01_Dependable_Computing slide 36](images/FTC01_Dependable_Computing_s036.png)

## Slide 37: Exercise  *(visual)*
37
![FTC01_Dependable_Computing slide 37](images/FTC01_Dependable_Computing_s037.png)

## Slide 38: Answer  *(visual)*
38
![FTC01_Dependable_Computing slide 38](images/FTC01_Dependable_Computing_s038.png)

## Slide 39: Dependability Means
• Fault Prevention
 - To Prevent Fault Occurrence or Introduction
• Fault Tolerance
 - To Ensure a service upto Fulfilling the System's
 Function in the Presence of Faults
• Fault Removal
 - To Reduce the Presence of Faults
• Fault Forecasting
 - To Estimate the Present Number, Future Incidence, &
 the Consequences of Faults

## Slide 40: Examples
Consider a space mission that has to be deployed for
long periods of time (say a few years)
• Fault Prevention: Use of reliable coding practices,
 (e.g., defensive programming) and safe languages
• Fault Tolerance: Provide ability to detect and repair
 failed components during missions
• Fault Removal: Remove the faults at runtime or
 record the commonly observed faults for later
 removal
• Fault Forecasting: Predict how likely a future mission
 is to succeed based on the lessons learned

## Slide 41: Fault Tolerance Techniques  *(visual)*
41
![FTC01_Dependable_Computing slide 41](images/FTC01_Dependable_Computing_s041.png)

## Slide 42: Fault Tolerance
The ability to provide continued correct operation
 despite the presence of faults
• Encompasses a broad rage of techniques ranging
 from low-level devices to application software
• Important to ensure that the service behaves as
 expected provided fault belongs to fault-model
• There is no such thing as perfect fault-tolerance.
 Every fault-tolerance technique has a coverage
 and a fault-model over which it is evaluated

## Slide 43: Error Detection
• Concurrent detection during normal
 operation
 - Watchdog timer
 - Software assertions
 - Process pairs
• Preemptive detection preempts the failure
 - Spare checking
 - Memory scrubbing
 - Software rejuvenation

## Slide 44: Error Recovery
• Rollback
 Restore the state of the system to one before the
 fault. Useful for transient and intermittent faults
• Rollforward
 Correct the fault and allow system to make forward
 progress, if possible
• Compensation
 Leverage natural redundancy of the system to mask
 the error

## Slide 45: Fault Avoidance
• Diagnosis
 - Identify the root cause of the fault (location, type)
• Isolation
 - Physically/Logically exclude faulty component
• Reconfiguration
 - Switch in non-faulty components and remap the tasks
 to the non-faulty components
• Reintialization
 - Record the new system state and update the external
 entities that interface with the system (if necessary)

## Slide 46: Example: Hardware Fault Tolerance
• Multicore system experiences a fault on one
 of the cores. Error is detected through a
 concurrent check. What are the possible
 recovery actions that can be taken?

## Slide 47: Example: Software Fault Tolerance
• Two identical copies of a software program
 are run concurrently to check each other. If
 the output of one differs from the output of
 the other, what recovery actions can be
 taken?

## Slide 48: Coverage
• Every fault-tolerance technique has associated
 coverage, i.e., the probability that it detects/
 corrects a fault, given that a fault has occurred
 - Coverage can be reduced by defects in the fault-
 tolerance mechanism's implementation ("Who
 will check the checker?")
 - Coverage can be reduced because of common
 mode failures or because assumptions made
 during the FTM's design are violated in practice

## Slide 49: Dependability:  *(visual)*
Attributes, Means and Impairments
![FTC01_Dependable_Computing slide 49](images/FTC01_Dependable_Computing_s049.png)

## Slide 50: Dependability Threats/Impairments
• Faults
 - The adjudged or hypothesized Cause of an error
• Errors
 - Part of the System state that may lead to a
 Subsequent Failure
• Failures
 - Delivered Service Deviates from the Correct
 Service

## Slide 51: Dependability Impairments  *(visual)*
51
![FTC01_Dependable_Computing slide 51](images/FTC01_Dependable_Computing_s051.png)

## Slide 52: Fault Masking and Benign Errors
• Not all faults lead to errors
 - Faults can be masked because they are not
 activated (e.g., faults in unread locations)
 - Faults can also be corrected before they lead to
 errors (e.g., memory scrubbing in ECC)
• Not all errors lead to failures (Benign errors)
 - Error may affect inconsequential system state
 - System may have redundancy to correct error

## Slide 53: Anatomy of an Error  *(visual)*
53
![FTC01_Dependable_Computing slide 53](images/FTC01_Dependable_Computing_s053.png)

## Slide 54: Inter‐connected Systems  *(visual)*
• One system's failure (system A) may be
 another one's fault/error (system B)
![FTC01_Dependable_Computing slide 54](images/FTC01_Dependable_Computing_s054.png)

## Slide 55: Fault Classification
Temporal Origin
• Transient • Physical faults
 - Occur only once at a - Occur due to physical
 location phenomena such as EM
 - E.g., cosmic ray strikes effects, threshold, effects
 etc. or due to
• Intermittent environmental conditions
 - Periodically recur at a such as temperature or
 location workload
 - E.g., timing violations • Human‐made faults
• Permanent • Programming errors, mis‐
 - Continuous and stable configuration, human
 occurrence at a location operator errors, etc
 - E.g., stuck‐at‐faults

## Slide 56: Classification of Failures  *(visual)*
Criteria Classification 1 Classification 2
Nature Halt (fail‐stop) Erratic (Babbling)
Detection Signaled Un-signaled (fail
 silent)
Consistency Consistent Inconsistent
Severity Minor Catastrophic
![FTC01_Dependable_Computing slide 56](images/FTC01_Dependable_Computing_s056.png)

## Slide 57: Classification of Errors  *(visual)*
Criteria Classification 1 Classification 2
Domain Timing Content
Detection Detected Latent
Consistency Consistent Inconsistent
Severity Minor Catastrophic
![FTC01_Dependable_Computing slide 57](images/FTC01_Dependable_Computing_s057.png)

## Slide 58: Dependability Threats  *(visual)*
58
![FTC01_Dependable_Computing slide 58](images/FTC01_Dependable_Computing_s058.png)

## Slide 59: 59  *(visual)*
![FTC01_Dependable_Computing slide 59](images/FTC01_Dependable_Computing_s059.png)

## Slide 60: 60  *(visual)*
![FTC01_Dependable_Computing slide 60](images/FTC01_Dependable_Computing_s060.png)

## Slide 61: 61  *(visual)*
![FTC01_Dependable_Computing slide 61](images/FTC01_Dependable_Computing_s061.png)

## Slide 62: 62  *(visual)*
![FTC01_Dependable_Computing slide 62](images/FTC01_Dependable_Computing_s062.png)

## Slide 63: Limits of Dependability
• Limits in term of Fault Classes
 - Physical Faults
 - Design/Development Faults
 - Interaction Faults
• Software Reliability
 - Current Bottleneck of Computing Systems
• Fault Tolerance Effectiveness

## Slide 64: Failure Sources & Frequencies for  *(visual)*
Computing Systems
![FTC01_Dependable_Computing slide 64](images/FTC01_Dependable_Computing_s064.png)

## Slide 65: User Outage in Non-Fault-Tolerant  *(visual)*
[Wood 94] Client-Server Networks
![FTC01_Dependable_Computing slide 65](images/FTC01_Dependable_Computing_s065.png)

## Slide 66: Primary Cause of Accident of Domestic  *(visual)*
[Ruegger 90] Flights in US
![FTC01_Dependable_Computing slide 66](images/FTC01_Dependable_Computing_s066.png)

## Slide 67: Results of Fault-Injection Experiments  *(visual)*
[Arlat et al.91] in Delta-4
![FTC01_Dependable_Computing slide 67](images/FTC01_Dependable_Computing_s067.png)

## Slide 68: Challenges of Dependability
• Reducing Cost of Computer Failures
• Extending Fault Tolerance from Products to
 their Production Processes

## Slide 69: Cost of Computer Failures in FRA as  *(visual)*
compared to the Revenue
![FTC01_Dependable_Computing slide 69](images/FTC01_Dependable_Computing_s069.png)

## Slide 70: FTC incidents in 2025  *(visual)*
Incident (2025) What Happened Fault Tolerance Lesson

 A configuration change introduced a null-pointer crash loop in
 Global replication without staged rollout created a common-
 Google Service Control, causing failures across many Google
Google Cloud Outage (June 12, 2025) mode failure. Better fault tolerance would include feature
 Cloud services. The faulty configuration propagated globally
 flags, canary deployments, and regional isolation.
 within seconds. (The Economic Times)

 A DNS-related failure in the US-East-1 region caused
 Even highly redundant cloud systems can fail if a critical
 cascading failures across DynamoDB and many AWS
AWS DynamoDB/DNS Outage (October 20, 2025) dependency becomes a single point of failure. Multi-region
 services, affecting thousands of applications worldwide.
 and multi-cloud architectures improve resilience.
 (TechRadar)

 A configuration update prevented Azure Front Door nodes Geographic redundancy cannot help when every region
Microsoft Azure Front Door Outage (October 29,
 from loading correctly worldwide until Microsoft rolled back the receives the same faulty configuration. Progressive rollouts
2025)
 change. (ThousandEyes) and automated rollback mechanisms are essential.

 A maintenance action overloaded database systems, causing Fault tolerance must cover backend databases as well as
Slack Database Outage (February 26, 2025) messaging failures for several hours despite healthy network network infrastructure. Monitoring should detect application-
 connectivity. (Network World) layer failures, not just network health.

 Two configuration-related incidents caused service disruptions
Asana Consecutive Outages (February 5-6, Small configuration errors can cascade. Canary deployments
 after server logs overwhelmed systems. Afterward, Asana
2025) and gradual rollouts are effective fault-tolerance practices.
 adopted staged configuration rollouts. (ThousandEyes)

 A latent software bug triggered by a routine configuration
 Hidden software defects can bypass redundant infrastructure.
Cloudflare Outage (November 18, 2025) change caused widespread degradation affecting numerous
 Extensive testing and automatic rollback reduce the impact.
 Internet services. (CIO)

 Maintenance temporarily reduced redundancy, and an Maintenance windows can weaken fault tolerance. Critical
Equinix Singapore Data Center Outage (May 31,
 equipment fault caused two data halls to go offline. (Data infrastructure should preserve sufficient redundancy during
2025)
 Center Frontier) planned work.
![FTC01_Dependable_Computing slide 70](images/FTC01_Dependable_Computing_s070.png)

## Slide 71: Assignment HW#01
• Answer the following question in one page (A4), and
 submit via myCourseVille by 17 Aug 2026
• Show a Threat Chain on Machine Learning system.
 Please select one incident and explain it in detail.
• Example: Threat on Server Hardware & Cloud Database
 - Fault: A memory chip (RAM) inside a cloud server
 degrades over time and suffers a hardware defect.
 - Error: Data bits stored in that specific RAM location flip
 from 1 to 0 (Data Corruption).
 - Failure: A user tries to download their profile photo, but
 the website displays a broken image icon and a "500
 Internal Server Error" message.

## Slide 72: The ML Threat
Chain

[Fault] [Error] [Failure]
Root Defect Internal State Visible Misbehavior
- Bad training data - Corrupted weights - Hallucinatory output
- Hidden bias - Out-of-distribution - Catastrophic system
- Poisoned dataset - Overfitting


---

# FTC02_Fault_Tolerant_Systems

> Source: `2110473_2026S1_FTC02_Fault_Tolerant_Systems-9294-17869528285980.pdf` — 51 slides. `visual: true` slides have a rendered image in `images/`.

## Slide 1: Fault Tolerant Systems - Overview
(Fault Tolerance in Distributed Systems)

 2110473 Fault Tolerant Computing

## Slide 2: Contents
• Introduction
• Terminology of Fault Tolerance
• Failure Rate and Reliability
• Reliability and MTTF, MTTR
• Availability
• Strategies to handle Faults
• Redundancy Techniques
• Practice Cases in Fault Tolerance
 - RAID, TMR, Space Shuttle, S/W Faults, Fault Tolerance in
 Process Group, Reliable Client-Server Communication,
 Checkpointing & Recovery

## Slide 3: Introduction
❑Fault Tolerance
 ▪Ability of system to continue Error-free operation in
 presence of unexpected fault
❑Important in mission-critical applications
 ▪E.g., medical, aviation, banking, etc.
 ▪Errors very costly
❑Becoming important in mainstream applications
 ▪Technology scaling causing circuit behavior to become less
 predictable and more trends to failures
 ▪Needing fault tolerance to keep Failure rate within
 acceptable levels

## Slide 4: Concepts of Fault Tolerance
• Hardware, software and networks cannot be totally free from
 failures
• Fault tolerance is a non-functional (QoS) requirement that
 requires a system to continue to operate, even in the
 presence of faults
• Fault tolerance should be achieved with minimal involvement
 of users or system administrators
• Distributed systems can be more fault tolerant than
 centralized systems, but with more processor hosts generally
 the occurrence of individual faults is likely to be more
 frequent

## Slide 5: Attributes, Consequences and  *(visual)*
Strategies
Attributes
 What is a
• Availability
 Dependable
• Reliability system?
• Safety
 How to• Confidentiality
 distinguish
• Integrity
 Consequences faults?
• Maintainability • Fault
 • Error How to
 handle • Failure
 faults?
 Strategies
 • Fault prevention
 • Fault tolerance
 • Fault recovery
 • Fault forecasting
![FTC02_Fault_Tolerant_Systems slide 5](images/FTC02_Fault_Tolerant_Systems_s005.png)

## Slide 6: Terminology of Fault Tolerance
Fault causes Error results in Failure

• Fault - is a defect within the system

• Error - is observed by a deviation from the expected
 behavior of the system

• Failure occurs when the system can no longer
 perform as required (does not meet spec)

• Fault Tolerance - is ability of system to provide a
 service, even in the presence of errors

## Slide 7: Types of Fault
(wrt time) Types of Fault

Permanent (Hard) Fault - repeatable error, e.g. failed
 component, Wearout failures, power fail, fire, flood, design
 error (usually software), sabotage

Soft Fault
Transient - occurs once or seldom, often due to unstable
 environment (e.g. bird flies past microwave transmitter)
Intermittent - occurs randomly, but where factors
 influencing fault are not clearly identified, e.g. unstable
 component
Operator error - human error

## Slide 8: Types of Fault  *(visual)*
(wrt attributes)
(Failure Mode of Distributed Systems)
![FTC02_Fault_Tolerant_Systems slide 8](images/FTC02_Fault_Tolerant_Systems_s008.png)

## Slide 9: Failure Rate  *(visual)*
❑(t) = Component failure rate
 - Measured in FITS (failures per 109 hours)

 e.g. NASA Flight = 1 FIT, Computers = 105-106 FITs, Human Life (85yrs) = 1,343 FITs

 Infant Working life Wearout
 mortality

 rate Overall curve
 Random failures Failure
 Early Wearout
 failures failures

 Time
![FTC02_Fault_Tolerant_Systems slide 9](images/FTC02_Fault_Tolerant_Systems_s009.png)

## Slide 10: Bathtub curve for software reliability  *(visual)*
10
![FTC02_Fault_Tolerant_Systems slide 10](images/FTC02_Fault_Tolerant_Systems_s010.png)

## Slide 11: Reliability Modeling  *(visual)*
11
![FTC02_Fault_Tolerant_Systems slide 11](images/FTC02_Fault_Tolerant_Systems_s011.png)

## Slide 12: Reliability Block Diagram  *(visual)*
• Series system works if all component work
• Parallel system works if @least one work
![FTC02_Fault_Tolerant_Systems slide 12](images/FTC02_Fault_Tolerant_Systems_s012.png)

## Slide 13: Series-Parallel System  *(visual)*
13
![FTC02_Fault_Tolerant_Systems slide 13](images/FTC02_Fault_Tolerant_Systems_s013.png)

## Slide 14: Minimal Path Set  *(visual)*
• A subset of the system components such that
 the operation of all the components in the
 subset implies the operation of the system.
![FTC02_Fault_Tolerant_Systems slide 14](images/FTC02_Fault_Tolerant_Systems_s014.png)

## Slide 15: Minimal Cut Set  *(visual)*
• A subset of the system components, such that
 the failure of all components in the subset
 does not imply the operation of the system
![FTC02_Fault_Tolerant_Systems slide 15](images/FTC02_Fault_Tolerant_Systems_s015.png)

## Slide 16: System Failure Rate
❑System constructed from components
❑No Fault Tolerance
 - Any component fails, whole system fails

 k
  =  sys c , i 
 i =1

## Slide 17: Reliability
❑If component working at time 0
 - R(t) = Probability still working at time t
❑Exponential Failure Law
 - If failure rate assumed constant
 • Good approximation if past infant mortality period

 −t R (t ) = e

## Slide 18: Reliability for Series System
❑Series System
 - All components need to work for system to work

 A B C

 R = R R R sys A B C

## Slide 19: How to make more Reliable
Reliability of n-Component system, each having
failure rate :

 𝑅𝑡= 𝑒−𝑛𝜆𝑡

• Reduce Failure Rate 
• Reduce Number of Components n
• Reduce Time t
Alternative:
• Introduce Redundancy

## Slide 20: System Reliability with Redundancy  *(visual)*
❑System reliability with component B in Parallel
 - Can tolerate one component B failing

 B
 A C
 B

 R = R 1 − 1( − R ) 2 R = R ( 2 R − R 2 ) R sys A  B  C A B B C
![FTC02_Fault_Tolerant_Systems slide 20](images/FTC02_Fault_Tolerant_Systems_s020.png)

## Slide 21: System Reliability
• Series System
 𝑁
 𝑅𝑜𝑣𝑒𝑟𝑎𝑙𝑙= ෑ 𝑅𝑖
 𝑖=1
• Parallel System
 𝑁
 𝑅𝑜𝑣𝑒𝑟𝑎𝑙𝑙= 1 −ෑ 1 −𝑅𝑖
 𝑖=1

## Slide 22: Some Simple Probability Distributions  *(visual)*
• Cumulative distribution function: CDF 𝑓𝑡= 𝑝𝑟𝑜𝑏𝑡≤𝑥≤𝑡+𝑑𝑡 = 𝑑𝐹(𝑡)/𝑑𝑡 𝑑𝑡
• Probability density function: pdf 𝐹𝑡= 𝑝𝑟𝑜𝑏𝑥≤𝑓= ׬ 𝑡𝑓𝑥𝑑𝑥 0
![FTC02_Fault_Tolerant_Systems slide 22](images/FTC02_Fault_Tolerant_Systems_s022.png)

## Slide 23: Reliability and MTTF  *(visual)*
23
![FTC02_Fault_Tolerant_Systems slide 23](images/FTC02_Fault_Tolerant_Systems_s023.png)

## Slide 24: Mean-Time-to-Failure (MTTF)
❑Average time before system fails
 - Equal to area under reliability curve

 
 MTTF = R (t )dt 
 0

❑For Exponential Failure Law

 
 t 1 MTTF = e −dt =   0

## Slide 25: Comparing Reliabilities  *(visual)*
25
![FTC02_Fault_Tolerant_Systems slide 25](images/FTC02_Fault_Tolerant_Systems_s025.png)

## Slide 26: Repair Rate and MTTR
❑= rate at which system repaired
 - constant for the exponential case
 - analogous to failure rate 
❑Maintainability often modeled as
 − t M (t ) =1 − e

❑Mean-Time-to-Repair (MTTR) = 1/

## Slide 27: Availability  *(visual)*
❑System Availability
 - Fraction of time system is operational

 MTTF
 system availability =
 MTTF + MTTR

 S Normal system operation
 1

 0

 t0 t1 t2 t3 t4 t

 failures
![FTC02_Fault_Tolerant_Systems slide 27](images/FTC02_Fault_Tolerant_Systems_s027.png)

## Slide 28: Availability (cont.)
❑Telephone Systems
 - Required to have system availability of 0.9999
 ("four nines")
❑High-Reliability Systems
 - May require 7 or more nines
❑Fault-Tolerant Design
 - Needed to achieve such high availability from less
 reliable components

## Slide 29: Availability in Series  *(visual)*
• A = Ax Ay
![FTC02_Fault_Tolerant_Systems slide 29](images/FTC02_Fault_Tolerant_Systems_s029.png)

## Slide 30: Availability in Parallel  *(visual)*
• A = )2 1-(1-Ax
![FTC02_Fault_Tolerant_Systems slide 30](images/FTC02_Fault_Tolerant_Systems_s030.png)

## Slide 31: Simply Calculating Availability
for Redundant Systems
• A is the probability that the system will be up (its availability)
• F is the probability that the system will be down
• a is the availability of a node
• n is the number of nodes in the system
• s is the number of spare nodes in the system
• f is the number of ways that all of the spares plus one other node
 can fail (that is, the number of node failures that will cause the
 system to fail)

 Clearly, A = 1 - F

 Simply, A = 1 - f ( 1 - a ) s+1

## Slide 32: Dual Node Single Spare
• The probability F for the failure of the system
 F = (1 - a)2
• The availability of the system, A, is
 A = 1 - F = 1 - (1 - a)2

Note:
If the node availability is 0.99,
the probability of one node down is 0.01.
Thus, the both nodes down probability is 0.012 = 0.0001
The system availability is 1 - 0.0001 = 0.9999 (four 9s)

## Slide 33: Multiple Nodes Single Spare  *(visual)*
• The number of Failure modes, f, is

• The probability of failure of the system, F, is
 the probability that any two nodes will fail

• System Availability, A, is

Note:
For Five-node system (node availability is 0.99),
The number of failure modes is ??
The availability of this five-node system is ??
![FTC02_Fault_Tolerant_Systems slide 33](images/FTC02_Fault_Tolerant_Systems_s033.png)

## Slide 34: Multiple Nodes Single Spare  *(visual)*
• The number of Failure modes, f, is
 the number of failure modes is ten
• The probability of failure of the system, F, is
 the availability of a five-node system is the probability that any two nodes will fail
 [1 - 10(.01)2], or .999. This is three 9s of
 availability
• System Availability, A, is

Note:
For Five-node system (node availability is 0.99),
The number of failure modes is ??
The availability of this five-node system is ??
![FTC02_Fault_Tolerant_Systems slide 34](images/FTC02_Fault_Tolerant_Systems_s034.png)

## Slide 35: Multiple Nodes Multiple Spares  *(visual)*
• The number of failure modes, f, is
the number of ways that s+1 nodes
out of n nodes can fail

• The probability of failure is

• The system availability is

Note:
For Six-node system wt Two-spare (node availability is 0.99),
The number of failure modes is ?? => 20
The availability of this six-node system is ?? =>1-20*(1-0.99)^3 = 0.99998
![FTC02_Fault_Tolerant_Systems slide 35](images/FTC02_Fault_Tolerant_Systems_s035.png)

## Slide 36: Relationship Between Availability and Reliability  *(visual)*
Reliability Maintainability Availability
 Constant Decrease ?
 Constant Increase ?
 Increase Constant ?
 Decrease Constant ?

Notes:
• Reliability represents the probability of components, parts and systems to perform their required
 functions for a desired period of time without failure in specified environments with a desired
 confidence.
• Availability represents the probability that the system is capable of conducting its required
 function when it is called upon given that it is not failed or undergoing a repair action.
• An increase in maintainability implies a decrease in the time it takes to perform maintenance
 actions.

• Therefore, not only is availability a function of reliability, but it is also a function of
 maintainability. 36
![FTC02_Fault_Tolerant_Systems slide 36](images/FTC02_Fault_Tolerant_Systems_s036.png)

## Slide 37: Difference Between Reliability and Availability
• Availability is a measure of the % of time the equipment is in an
 operable state
• While reliability is a measure of how long the item performs its
 intended function

• For example, the machine is down 6 minutes every hour.
 - This translates into an availability of 90% but a reliability of less than 1
 hour
 - That may be okay in some circumstances but what if this is a paper
 machine?
 - It may take at least 30 minutes of run time to get to the point that we
 are producing good paper

• Generally speaking a reliable machine has high availability but an
 available machine may or may not be very reliable

## Slide 38: Check Yourself 1  *(visual)*
• Calculate the Reliability of TMR system (Triple
 Modular Redundant system)
 - Reliability of U1 = U2 = U3 = RU, Voter = RV
![FTC02_Fault_Tolerant_Systems slide 38](images/FTC02_Fault_Tolerant_Systems_s038.png)

## Slide 39: Check Yourself 1 - Solution  *(visual)*
• Calculate the Reliability of TMR system (Triple
 Modular Redundant system)
 - Reliability of U1 = U2 = U3 = RU, Voter = RV

 𝑅𝑈3 + 3𝑅𝑈2 1 −𝑅𝑈 𝑅𝑉= (3𝑅𝑈2−2𝑅𝑈3)𝑅𝑉𝑅𝑡𝑚𝑟=
![FTC02_Fault_Tolerant_Systems slide 39](images/FTC02_Fault_Tolerant_Systems_s039.png)

## Slide 40: Check Yourself 2  *(visual)*
• Parallel-to-series interconnection scheme and Series-to-
 parallel interconnection scheme
• Find the both reliabilities, 𝑅𝑃𝑆and 𝑅𝑆𝑃
• If each subsystem reliability is 𝑅, find 𝑅𝑃𝑆and 𝑅𝑆𝑃and
 which one is more reliable?

 A B A B

 A B A B

 PS scheme SP scheme 40
![FTC02_Fault_Tolerant_Systems slide 40](images/FTC02_Fault_Tolerant_Systems_s040.png)

## Slide 41: Check Yourself 2 - Solution  *(visual)*
• Parallel-to-series interconnection scheme and Series-to-parallel interconnection scheme
• Find the both reliabilities, 𝑅𝑃𝑆and 𝑅𝑆𝑃
• If each subsystem reliability is 𝑅, find 𝑅𝑃𝑆and 𝑅𝑆𝑃and which one is more reliable?

 A B A B

 A B A B

 PS scheme SP scheme

 RPS = [ 1 - ( 1 - RA )^2 ] [ 1 - ( 1 - RB )^2] = R^4 - 4 R^3 + 4 R^2

 RSP = [ 1 - ( 1 - RA RB ) ( 1 - RA RB ) ] = 2 R^2 - R^4

 RPS > RSP
![FTC02_Fault_Tolerant_Systems slide 41](images/FTC02_Fault_Tolerant_Systems_s041.png)

## Slide 42: Highly Dependable Computer Systems
Long-life systems: Fail-slow, Rugged, High-reliability
Spacecraft with multiyear missions, systems in inaccessible locations
Methods: Replication (spares), error coding, monitoring, shielding

Safety-critical systems: Fail-safe, Sound, High-integrity
Flight control computers, nuclear-plant shutdown, medical monitoring
Methods: Replication with voting, time redundancy, design diversity

Non-stop systems: Fail-soft, Robust, High-availability
Telephone switching centers, transaction processing, e-commerce
Methods: HW/info redundancy, backup schemes, hot-swap, recovery

## Slide 43: Strategies to Handle Faults
Actions to identify and
• Fault avoidance remove errors:
 Techniques aim to prevent faults from • Design reviews
 • Testingentering the system during design stage
 • Use certified tools
• Fault removal • Analysis:
 •Hazard analysis Methods attempt to find faults within a
 •Formal methods -
system before it enters service
 proof & refinement
• Fault detection
 Techniques used during service to detect
faults within the operational system
• Fault tolerant No non-trivial system can be guaranteed free from error
 Techniques designed to tolerant faults,
 Must have an expectation of
i.e. to allow the system operate correctly failure and make appropriate
in the presence of faults. provision

## Slide 44: Redundancy Techniques
◼Hardware redundancy
 −Replicate hardware and compare outputs
 −Detects both permanent and temporary faults
 −Little or no performance impact/ Need area and power
◼Information redundancy
 −Encode outputs with error detecting or correcting
 −Less hardware/ Complexity in design
◼Temporal (time) redundancy
 −Repeating calculations and comparing results
 −For transient faults (cannot detect permanent faults)
 −Less hardware overhead/ Impacts system performance

## Slide 45: Architectural approaches
Dissimilar systems are alsoSimplex systems
 known as "diverse" systems
 •highly reliable components
 in which an operation is
 performed in a different
Dual Systems way in the hope that the
 •twin identical same fault will not be
 •twin dissimilar present in different
 implementations •control + monitor

N-way Redundant systems
 •identical / dissimilar The basic approach to
 achieve fault tolerance is •self-checking / voting
 redundancy

## Slide 46: RAID  *(visual)*
(Redundant Array of Independent Disks)

 RAID has been classified into several levels: 0, 1, 2, 3, 4, 5, 6, 10, 50,
 each level provides a different degree of fault tolerance
![FTC02_Fault_Tolerant_Systems slide 46](images/FTC02_Fault_Tolerant_Systems_s046.png)

## Slide 47: Failure Masking by TMR  *(visual)*
(a) Original circuit
 (b) Triple modular redundancy (TMR)
![FTC02_Fault_Tolerant_Systems slide 47](images/FTC02_Fault_Tolerant_Systems_s047.png)

## Slide 48: Space Shuttle
❑Uses 5 identical computers which can be assigned to redundant operation
 under program control

❑During critical mission phases - boost, re-entry and loading - 4 of its 5
 computers operate an NMR configuration, receiving the same inputs and
 executing identical tasks When a failure is detected the computer
 concerned is switched out of the system leaving a TMR arrangement

❑The fifth computer is used to perform non-critical tasks in a simplex
 mode, however, under extreme cases may take over critical functions. The
 unit has "diverse" software and could be used if a systematic fault was
 discovered in the other four computers

❑The shuttle can tolerate up to two computer failures; after a second
 failure it operates as a duplex system and uses comparison and self-test
 techniques to survive a third fault

## Slide 49: Software Faults
❑Program code (may) contains bugs if actual behavior disagrees with
the intended specification. These faults may occur from:
▪specification error
▪design error
▪coding error, e.g. use on un-initialized variables
▪integration error
▪run time error e.g. operating system stack overflow, divide by zero
❑Software failure is (usually) deterministic, i.e. predictable, based on
the state of the system. There is no random element to the failure -
unless the system state cannot be specified precisely. A non-
deterministic fault behavior usually indicates that the relevant system
state parameters have not been identified.

❑Fault coverage - defines the fraction of possible faults that can be
detected by testing (statement, condition or structural analysis)

## Slide 50: Software Fault Tolerance
N-version programming
◼Use several different implementations of the same specification
◼The versions may run sequentially on one processor or in
 parallel on different processors.
◼They use the same input and their results are compared.
 −In the absence of a disagreement, the result is output.
 −When produced different results:
 ◼If there are 2 routines:
 ◼the routines may be repeated in case this was a transient error;
 ◼to decide which routine is in error.
 ◼If there are 3 or more routines,
 ◼voting may be applied to mask the effects of the fault.

## Slide 51: HW02: System Reliability  *(visual)*
• Find Minimal Path Set (MPS) and Minimal Cut Set (MCS)
 of each scheme (PP and AP)
• Find the both reliabilities, 𝑅𝑃𝑃and 𝑅𝐴𝑃
• If each subsystem reliability is 𝑅, find 𝑅𝑃𝑃and 𝑅𝐴𝑃and
 which one is more reliable?

 A B C A B C

 A B C A B C

 A B C A B C

 PP scheme AP scheme 51
![FTC02_Fault_Tolerant_Systems slide 51](images/FTC02_Fault_Tolerant_Systems_s051.png)


---

# FTC03_Byzantine_Fault_Tolerance

> Source: `2110473_2026S1_FTC03_Byzantine_Fault_Tolerance-9294-17875577778080.pdf` — 36 slides. `visual: true` slides have a rendered image in `images/`.

## Slide 1: Home Exercise: Reliability  *(visual)*
R1 R2 B2 R3 R4 Sys Probability
 PP scheme 1 1 1 1 1 1

 1 1 1 1 0 1
 R1R2
 - - - - - -

 1 1 0 0 0 1

 1 0 1 1 1 1 R1R2'B2R3R4

 1 0 1 1 0 0 0

 1 0 1 0 1 1 R1R2'B2R3'R4
 Bridge 1 0 1 0 0 0 0
R1 R2 - - - - - -

 0 0 0 0 0 0 0

 R1 = (1-(1-RA)2) Rbridge = R1R2 + R1R2'B2R4 +
 R2 = RBRC R1'R2B2R3 + R1'R2B2'R3R4 +R3 R4
 R3 = RARB R1'R2'R3R4
 R4 = (1-(1-RC)2) 1
![FTC03_Byzantine_Fault_Tolerance slide 1](images/FTC03_Byzantine_Fault_Tolerance_s001.png)

## Slide 2: Byzantine Fault Tolerance
(Fault Tolerance in Distributed Systems)

 2110473 Fault Tolerant Computing

 Several sources

## Slide 3: Contents
• Process Groups
• Fault Tolerance in Process Groups
• Byzantine Generals Problem
• Oral Message Algorithm
• Blockchain
• Reliable Client-Server Communication

## Slide 4: Process Groups  *(visual)*
➢All members of a group receive a message sent to the group
 ➢If one process fails, others can take over
 ➢Can be dynamic; processes can have multiple memberships

(a) Communication in a flat group: No Single Point-of-Failure, Complicated Decision Making
(b) Communication in a hierarchical group: Single Point-of-Failure, Quick Decision Making
![FTC03_Byzantine_Fault_Tolerance slide 4](images/FTC03_Byzantine_Fault_Tolerance_s004.png)

## Slide 5: Process Group Architecture  *(visual)*
Central Authority Consensus Protocol
 (Agreement)
![FTC03_Byzantine_Fault_Tolerance slide 5](images/FTC03_Byzantine_Fault_Tolerance_s005.png)

## Slide 6: Centralized & Distributed Ledger  *(visual)*
6
![FTC03_Byzantine_Fault_Tolerance slide 6](images/FTC03_Byzantine_Fault_Tolerance_s006.png)

## Slide 7: Process Group Resilience
❑Organize several identical processes into a group
❑When a message is send to a group, all members of the
 group receives it
❑If one process in a group fails (no matter what reason),
 hopefully some other process can take over for it
❑The purpose of introducing groups is to allow processes
 to deal with collections of processes as a single
 abstraction.
❑Important design issue is how to reach agreement within
 a process group when one or more of its members cannot
 be trusted to give correct answers.

## Slide 8: Fault Tolerance in Process Groups
❑A system is k fault tolerant if it can survive faults in k components and
 still meet its specification
❑If failures are safe (silent), then k+1 processes are sufficient to get k
 fault tolerance
❑In case of arbitrary failures, 2k+1 processes are required (since k failing
 processes can all generate the same result by chance)
 ❑This assumes that each process reaches its decision independently
 ❑What if processes gang up to produce wrong results? General
 problem is having a process group reach an agreement
 ❑In this case you need 2k+1 correctly functioning processes, for a
 total of 3k+1 processes
❑In both cases we assume that communication failures do not occur

## Slide 9: Byzantine Generals Problem  *(visual)*
9
![FTC03_Byzantine_Fault_Tolerance slide 9](images/FTC03_Byzantine_Fault_Tolerance_s009.png)

## Slide 10: Agreement: Byzantine Generals Problem (1)  *(visual)*
How does a process group deal with a faulty member?

❑The "Byzantine Generals Problem" for 3 loyal generals and 1 traitor.
a) The generals announce their troop strengths to the other members of the group by
 sending a message.
b) The vectors that each general assembles based on (a), each general knows their own
 strength. They then send their vectors to all the other generals.
c) The vectors that each general receives in step 3. It is clear to all that General 3 is the
 traitor. In each 'column', the majority value is assumed to be correct.
![FTC03_Byzantine_Fault_Tolerance slide 10](images/FTC03_Byzantine_Fault_Tolerance_s010.png)

## Slide 11: Agreement: Byzantine Generals Problem (2)  *(visual)*
Warning: the algorithm does not always work! ⇒Two-Army Problem

• The same algorithm as in previous slide, except now with 2 loyal generals
 and 1 traitor. Note: It is no longer possible to determine the majority value
 in each column, and the algorithm has failed to produce agreement.
• It has been shown that for the algorithm to work properly, more than two-
 thirds of the processes have to be working correctly. That is: if there are M
 faulty processes, we need 2M + 1 functioning processes to reach agreement.
![FTC03_Byzantine_Fault_Tolerance slide 11](images/FTC03_Byzantine_Fault_Tolerance_s011.png)

## Slide 12: Oral Messages
Byzantine Agreement (n nodes, m faults)
 - can be reached using Oral Messages,
 if n >= 3m+1

Assumptions:
• Every message is delivered correctly
• Receiver knows who sent message
• Absence of message can be detected

## Slide 13: Oral Message Algorithm
OM(0)
1. Commander sends his value to every lieutenant
2. Each lieutenant uses the received value or "retreat" if no
 value received

OM(m)
1. Commander sends his value to every lieutenant
2. Everyone runs OM(m-1) and acts as the commander to
 send the value received in step 1 to all the other lieutenant
3. Each lieutenant uses the majority value out of the values
 received
 Recursive Algorithm
 (No solution with fewer than 3m+1 generals can cope with m traitors)

## Slide 14: Example: Bad Lieutenant  *(visual)*
Scenario: m=1, n=4, traitors=L3
![FTC03_Byzantine_Fault_Tolerance slide 14](images/FTC03_Byzantine_Fault_Tolerance_s014.png)

## Slide 15: Example: Bad Commander  *(visual)*
Scenario: m=1, n=4, traitors=C
![FTC03_Byzantine_Fault_Tolerance slide 15](images/FTC03_Byzantine_Fault_Tolerance_s015.png)

## Slide 16: Bigger BFT (Bad Lieutenants )  *(visual)*
Scenario: m=2, n=7, traitors=L5,L6

Decision??

 https://github.com/AnantJoshiCZ/Byzantine
 https://github.com/AnantJoshiCZ/Byzantine
![FTC03_Byzantine_Fault_Tolerance slide 16](images/FTC03_Byzantine_Fault_Tolerance_s016.png)

## Slide 17: Bigger BFT (Bad Commander+ )  *(visual)*
17
![FTC03_Byzantine_Fault_Tolerance slide 17](images/FTC03_Byzantine_Fault_Tolerance_s017.png)

## Slide 18: Decision with Bad Commander+  *(visual)*
18
![FTC03_Byzantine_Fault_Tolerance slide 18](images/FTC03_Byzantine_Fault_Tolerance_s018.png)

## Slide 19: Next Step of Algorithm  *(visual)*
19
![FTC03_Byzantine_Fault_Tolerance slide 19](images/FTC03_Byzantine_Fault_Tolerance_s019.png)

## Slide 20: Check Yourself  *(visual)*
Imagine there are 1 loyal commander, 1 traitor lieutenant, and 4 loyal
lieutenants. Please provide a concrete example where Oral Message
algorithm is used among these soldiers, yet the loyal lieutenants all are
able to follow the commander's command.
 You need to briefly describe the process of Oral Message algorithm in
your example.

 A A LIEUTENANT COMMANDER LIEUTENANT

 A A A

 LIEUTENANT LIEUTENANT LIEUTENANT

 - The red ellipse represents the faulty nodes, while the blue one for the normal nodes
 - The commander sends the "Attack" order to all lieutenants to which it connects.
 - When each lieutenant act as a commander, a loyal lieutenant sends the original order, "Attack",
 while the traitor sends "Retreat". 20
![FTC03_Byzantine_Fault_Tolerance slide 20](images/FTC03_Byzantine_Fault_Tolerance_s020.png)

## Slide 21: Check Yourself - Solution (1/3)  *(visual)*
A A LIEUTENANT COMMANDER LIEUTENANT

 A A A

 LIEUTENANT LIEUTENANT LIEUTENANT

 A AOM(1) L C L
 A A A
 L L L
![FTC03_Byzantine_Fault_Tolerance slide 21](images/FTC03_Byzantine_Fault_Tolerance_s021.png)

## Slide 22: Check Yourself - Solution (2/3)  *(visual)*
A AOM(1) L C L L5
 A A A
 L L L

OM(0)

 R AC L L L L L A A
R R R A
 A A A
 L L L C L A L L C L

 A L L L C A A A

 L A L A C L A L A L
![FTC03_Byzantine_Fault_Tolerance slide 22](images/FTC03_Byzantine_Fault_Tolerance_s022.png)

## Slide 23: Check Yourself - Solution (3/3)  *(visual)*
Lieute Value Frm Frm Frm Frm Frm Majority
 nant frm C L1 L2 L3 L4 L5 Vote
 L1 A - A A A R A
 L2 A A - A A R A
 L3 A A A - A R A
 L4 A A A A - R A
 L5 x x x x x - x
![FTC03_Byzantine_Fault_Tolerance slide 23](images/FTC03_Byzantine_Fault_Tolerance_s023.png)

## Slide 24: Number of Messages
Number of Messages
 = (n-1)*(n-2)*…*(n-m-1)
 = O(nm)

 Exponential in number of Traitors!!

• Practical Byzantine Fault Tolerance
• Signed Message Solution

## Slide 25: Practical BFT  *(visual)*
- Client waits for m+1 replies from different replicas with
 same answer
- If primary is faulty, select new primary
- Many optimizations to reduce overhead
![FTC03_Byzantine_Fault_Tolerance slide 25](images/FTC03_Byzantine_Fault_Tolerance_s025.png)

## Slide 26: Blockchain
• A solution to the Byzantine Fault Tolerance
 - For any m, Algorithm OM(m) reaches consensus if
 there are more than 3m generals and at
 most m traitors.
• Remove the middleman while providing a trusted
 exchange
• Power of Blockchain
 - Decentralized, self-governing network (no middleman)
 - Trusted network despite a lack of central governance
• Proof of Work/ Proof of Stake Algorithm

## Slide 27: Proof of Work in Bitcoin  *(visual)*
27
![FTC03_Byzantine_Fault_Tolerance slide 27](images/FTC03_Byzantine_Fault_Tolerance_s027.png)

## Slide 28: BlockChain: Proof of Work  *(visual)*
28
![FTC03_Byzantine_Fault_Tolerance slide 28](images/FTC03_Byzantine_Fault_Tolerance_s028.png)

## Slide 29: BlockChain: Proof of Work  *(visual)*
29
![FTC03_Byzantine_Fault_Tolerance slide 29](images/FTC03_Byzantine_Fault_Tolerance_s029.png)

## Slide 30: Reliable Client-Server Communication
❑Fault Tolerance in DS considers Communication Failures
 o masking crash and omission failures
❑Reliable Point-to-Point (P2P) communication is established
by a reliable transport protocol, such as TCP
 o P2P TCP masks omission failures by guarding against lost messages
 using ACKs and retransmissions
 o But perform poorly when a crash occurs
❑In client/server model, In the case of process failure the
following situations need to be dealt with:
 ➢Client unable to locate server
 ➢Client request to server is lost
 ➢Server crash after receiving client request
 ➢Server reply to client is lost
 ➢Client crash after sending server request

## Slide 31: Lost Request Messages when Server Crashes  *(visual)*
A server in client-server communication
a) Normal case
b) Crash after execution
c) Crash before execution
![FTC03_Byzantine_Fault_Tolerance slide 31](images/FTC03_Byzantine_Fault_Tolerance_s031.png)

## Slide 32: Solutions to Handle Server Failures (1)
➢Client unable to locate server, e.g. server down, or
server has changed
Solution:
 - Use an exception handler - but this is not always
possible in the programming language used

➢Client request to server is lost
Solution:
 - Use a timeout to await server reply, then re-send - but
be careful about idempotent operations (no side effects
when re-send)
 - If multiple requests appear to get lost assume 'cannot
locate server' error

## Slide 33: Solutions to Handle Server Failures (2)
➢Server crash after receiving client request
 Problem may be not being able to tell if request was carried out (e.g.
client requests print page, server may stop before or after printing,
before acknowledgement)
Solutions:
 - rebuild server and retry client request (assuming 'at least once'
semantics for request)
 - give up and report request failure (assuming 'at most once'
semantics), what is usually required is exactly once semantics, but this
difficult to guarantee

➢Server reply to client is lost

 Client can simply set timer and if no reply in time assume server
down, request lost or server crashed during processing request.

## Slide 34: Solutions to Handle Client Failures
➢Client crash after sending server request : Server unable to reply to
client (orphan request)

Options and Issues:
 - Extermination: client makes a log of each RPC, and kills orphan after
reboot. Expensive.
 - Reincarnation. Time divided into epochs (large intervals). When
client restarts it broadcasts to all, and starts a new time epoch. Servers
dealing with client requests from a previous epoch can be terminated.
Also unreachable servers (e.g. in different network areas) may later reply,
but will refer to obsolete epoch numbers.
 - Gentle reincarnation, as above but an attempt is made to contact the
client owner (e.g. who may be logged out) to take action
Expiration, server times out if client cannot be reached to return reply

## Slide 35: Reliable Communication Systems
Examine Assumptions:

➢Synchronous Communication
➢Absence of message can be detected
➢Every message that is sent is delivered correctly
➢Receiver of a message knows who sent it
➢A loyal general's signature cannot be forged, and any
 alteration of the contents of his signed message can be
 detected
➢Anyone can verify the authenticity of a general's signature

## Slide 36: HW03: BFT  *(visual)*
Imagine there are 1 loyal commander, 2 traitor lieutenants, and 5
loyal lieutenants. Please provide a concrete example where Oral
Message algorithm is used among these soldiers, yet the loyal
lieutenants all are able to follow the commander's command.
 You need to briefly describe the process of Oral Message algorithm in
your example.

 A A LIEUTENANT COMMANDER LIEUTENANT
 A A
 LIEUTENANT A A A LIEUTENANT

 LIEUTENANT LIEUTENANT LIEUTENANT

 - The red ellipse represents the faulty nodes, while the blue one for the normal nodes
 - The commander sends the "Attack" order to all lieutenants to which it connects.
 - When each lieutenant act as a commander, a loyal lieutenant sends the original order, "Attack",
 while the traitor sends "Retreat". 36
![FTC03_Byzantine_Fault_Tolerance slide 36](images/FTC03_Byzantine_Fault_Tolerance_s036.png)


---

# FTC04_Rollback_Recovery

> Source: `2110473_2026S1_FTC04_Rollback_Recovery-9294-17881367582371.pdf` — 51 slides. `visual: true` slides have a rendered image in `images/`.

## Slide 1: Home Exercise: BFT (1/2)  *(visual)*
OM(2): Commander sends A (Attack) to all 7 lieutenants (incl. traitors)

 A A TRAITOR1 COMMANDER LIEUTENANT3
 A A
 TRAITOR2 A A A LIEUTENANT4

 LIEUTENANT1 LIEUTENANT2 LIEUTENANT5

OM(1): Every lieutenant (incl. traitor) acts as commander
 R A
 C L T C
 R R R R R A A A A
 T L T L
 A

 L L L L L L 1
![FTC04_Rollback_Recovery slide 1](images/FTC04_Rollback_Recovery_s001.png)

## Slide 2: Home Exercise: BFT (2/2)  *(visual)*
OM(0): Every lieutenant (incl. traitor) relays the message

 R A
 C L T C
 R R R R A A A
 L T
 A

 L L L L L L

Lieute Value frm Frm Frm Frm Frm Frm Frm Frm Majority
 nant C L1 L2 L3 L4 L5 T1 T2 Vote

 L1 A - A A A A R R A

 L2 A A - A A A R R A

 L3 A A A - A A R R A

 L4 A A A A - A R R A

 L5 A A A A A - R R A

 T1 X X X X X X - X X
 2 T2 X X X X X X X - X
![FTC04_Rollback_Recovery slide 2](images/FTC04_Rollback_Recovery_s002.png)

## Slide 3: Rollback Recovery
(Fault Tolerance in Distributed Systems)

 2110473 Fault Tolerant Computing

## Slide 4: Contents
• Fault Tolerance & Recovery
• Rollback Recovery
• System Model:
 - Messages
 - Consistent State (Cuts)
• Rollback Issues:
 - Domino Effect
 - Livelocks
• Recovery Techniques
 - Coordinated checkpointing
 - Pessimistic Logging

## Slide 5: Fault Tolerance & Recovery  *(visual)*
fault
 causes

 Recovery erroneous state error

 leads to
 valid state
 failure

• An error is a manifestation of a fault that can lead to a failure.
• Failures:
 - Process failure: Deadlocks, protection violation, erroneous user input.
 - System failure: Full/partial amnesia.
 - Secondary storage failure: data inaccessible.
 - Communication failure: network inaccessible.
![FTC04_Rollback_Recovery slide 5](images/FTC04_Rollback_Recovery_s005.png)

## Slide 6: Recovery
Failure of a site/node in a distributed system causes
inconsistencies in the state of the system

Recovery: bringing back the failed node in step with other
nodes in the system
 • Restart process/processor
 • Reclaim resources
 • Undo/finish incomplete transactions
Distributed/Concurrency make things harder

Focus on Message-Passing Model in Distributed Systems

## Slide 7: Failure Recovery
After a failure, restoring the system to its "normal" state
• Forward recovery
 - Assess damages that could be caused by faults, remove
 those damages (errors), and help processes continue
 - TMR is one of Forward recovery
 - Sacrifices cost to achieve availability
• Backward (Rollback) recovery
 - Operation-based (do/undo/redo logs)
 - State-based (Checkpointing/Logging)
 - Sacrifices performance to achieve availability

## Slide 8: System Design Space  *(visual)*
8
![FTC04_Rollback_Recovery slide 8](images/FTC04_Rollback_Recovery_s008.png)

## Slide 9: Forward Recovery
• Repair and go ahead
• Goal: To restore system from erroneous state
 to error-free state
• If nature of error is completely known
 - Remove error from state
 - Proceed with execution from error-free state
• Rarely possible to do

## Slide 10: Forward Recovery (Exception)
◼Exceptions
 −System states that should not occur
 −Exceptions can be defined either
 ◼predefined (e.g. array-index out of bounds, divide by zero)
 ◼explicitly declared by the programmer
◼Raising an exception
 −When such a state is detected in the execution of the
 program
 −The action of indicating occurrence of such as state
◼Exception handler
 −Code to be executed when an exception is raised
 −Declared by the programmer
 −For recovery action
◼Supported by several programming languages
 −Ada, ISO Modula-2, Delphi, Java, C++.

## Slide 11: Backward/Rollback Recovery
• Repairing is not possible so Go back!
• When error source unknown
 - Restore state to previous error-free state; restart
 - Independent of fault, errors causing fault
 - Problems
 • Performance penalty
 • No guarantee fault will not reoccur
 • Possible unrecoverable component of state
• Recovery point: state used to replace error
• Can not be applied to irreversible operations, e.g.
 Print out, ATM withdrawal

## Slide 12: Basic of Rollback Recovery
• Rollback Recovery Protocols
 - Restore the system back to a Consistent State after a failure
 - Achieve Fault Tolerance by periodically saving the state of a process
 during the failure-free execution
 - Treat a distributed system application as a collection of processes that
 communicate over a network
• Checkpoints
 - The Saved States of a process
• Why Rollback Recovery is complicated?
 - Messages induce inter-process dependencies during failure-free
 operation
• Rollback Propagation
 - The dependencies may force some of the processes that did not fail to
 roll back
 - This phenomenon is called "Domino Effect"

## Slide 13: Rollback Recovery
• State based
 - Checkpointing
 • Uncoordinated checkpointing
 • Coordinated checkpointing
 - Blocking, Non-blocking
 • Communication induced checkpointing
 - Model based, Index based
• Log based
 - Pessimisstic logging
 - Optimistic logging
 - Casual logging

## Slide 14: Checkpointing
• Checkpoint recover is the saving and
 restoration of the system state.
• By saving the current state of the system
 periodically, it provides the information
 needed for the restoration of the lost state,
 when the system fails

## Slide 15: Checkpointing issues in
Distributed Environment
• Consistency: if P1 checkpoints and then sends
 a message to P2, we can no longer roll P1 back
 to before the message was sent unless P2 rolls
 back to before the message's receipt
• Expensive: We don't want checkpoint more
 than necessary, but also don't want to have to
 rollback too far
• Communication with the outside world
 doesn't get undone

## Slide 16: System Model  *(visual)*
Basic approaches
 - Checkpointing : copying/restoring the state of a process
 - Logging : recording/replaying messages
![FTC04_Rollback_Recovery slide 16](images/FTC04_Rollback_Recovery_s016.png)

## Slide 17: Stable storage - a prerequisite for recovery
• In a system that tolerates only a single failure,
 stable storage may consist of the volatile
 memory of another process
• In a system that wishes to tolerate an arbitrary
 number of transient failures, stable storage may
 consist of a local disk in each host.
• In a system that tolerates non-transient failures,
 stable storage must consist of a persistent
 medium outside the host on which a process is
 running. A replicated file system is a possible
 implementation in such systems

## Slide 18: Rollback Recovery Principles  *(visual)*
1. Checkpointing
 checkpoint (stored local state)

Inside the cut Outside the cut
 P0

 P1

 P2

 P3

 Recovery line (cut)
 Restart all, or almost all, processes from a consistent cut and
 let a new execution run
![FTC04_Rollback_Recovery slide 18](images/FTC04_Rollback_Recovery_s018.png)

## Slide 19: Rollback Recovery Principles  *(visual)*
2. Message Logging
 checkpoint (stored local state)

 P0

 P1

 P2

 P3

 Only one (or a few) process recover and use message
 information to replay the previous execution until reaching the
 failure point
![FTC04_Rollback_Recovery slide 19](images/FTC04_Rollback_Recovery_s019.png)

## Slide 20: Rollback Recovery Principles  *(visual)*
20
![FTC04_Rollback_Recovery slide 20](images/FTC04_Rollback_Recovery_s020.png)

## Slide 21: Implementation of Rollback Recovery  *(visual)*
On top of a reliable Directly on top of unreliable
 communication protocol communication channels
![FTC04_Rollback_Recovery slide 21](images/FTC04_Rollback_Recovery_s021.png)

## Slide 22: Garbage Collection
• Checkpoints and event logs consume storage
 resources
• Stored Information may become useless for
 Recovery
• Garbage Collection:
 - The deletion of such useless recovery information
 - Common approach is to identify the most recent
 consistent set of checkpoints (Recovery line)
 - And discard all information relating to events that
 occurred before that line

## Slide 23: Messages
• In-transit message
 - messages that have been sent but not yet received
• Lost messages
 - messages whose 'send' is done but 'receive' is undone due to rollback
• Delayed messages
 - messages whose 'receive' is not recorded because the receiving
 process was either down or the message arrived after rollback
• Orphan messages
 - messages with 'receive' recorded but message 'send' not recorded
 - do not arise if processes roll back to a consistent global state
• Duplicate messages
 - arise due to message logging and replaying during process recovery

## Slide 24: In-transit message  *(visual)*
messages that have been sent but not yet received
• If message delivery is not guaranteed, they are not a problem!
• But if the communication protocol is reliable, they must be
 taken into account
![FTC04_Rollback_Recovery slide 24](images/FTC04_Rollback_Recovery_s024.png)

## Slide 25: Lost message  *(visual)*
• Due to the failure in process, the message cound not reach the
 process and so it is lost on the way
• Different from In-transit message

 Rollback
 C1 C2 failure
 P1
 m1
 P2

- Due to the failure in P1, m1 could not reach P1 and lost on the way
- P1 rollback to C2 to recover its old status to continue the task
![FTC04_Rollback_Recovery slide 25](images/FTC04_Rollback_Recovery_s025.png)

## Slide 26: Delayed message  *(visual)*
• The lost messages may reach the destination process after
 recovered, ie. messages arrived after rollback

 Rollback
 m1 reached P1 after
 C0 recovered from failure
 P0
 m5 Rollback
 m5 also delayed
 m1 message C1
 P1
![FTC04_Rollback_Recovery slide 26](images/FTC04_Rollback_Recovery_s026.png)

## Slide 27: Orphan messages  *(visual)*
messages with 'receive' recorded but message 'send' not recorded
• If P2 fails and restarts from the
 cut, the message will be re-
 emitted and received twice by
 P1
 - Either avoid using inconsistent
 cuts (in general for
 checkpointing)
 - Or avoid re-emitting the message
 (in general for message logging)
 and replay the same execution
![FTC04_Rollback_Recovery slide 27](images/FTC04_Rollback_Recovery_s027.png)

## Slide 28: Duplicate message  *(visual)*
• The message which already received has been re-sent after
 recovery

 Rollback

 C1 failure
 P0
 m1

 P1
![FTC04_Rollback_Recovery slide 28](images/FTC04_Rollback_Recovery_s028.png)

## Slide 29: Messages - example  *(visual)*
• In-transit
 - 𝑚1, 𝑚2
• Lost
 - 𝑚1
• Delayed
 - 𝑚1, 𝑚5
• Orphan
 - none
• Duplicated
 - 𝑚4, 𝑚5
![FTC04_Rollback_Recovery slide 29](images/FTC04_Rollback_Recovery_s029.png)

## Slide 30: Consistent State
• A global state of a distributed system
 - a collection of the individual states of all participating processes and the states of
 the communication channels
• Consistent global state
 - a global state that may occur during a failure-free execution of distribution of
 distributed computation
 - if a process's state reflects a message receipt, then the state of the corresponding
 sender must reflect the sending of the message
• A global checkpoint
 - a set of local checkpoints, one from each process
• A consistent global checkpoint
 - a global checkpoint such that no message is sent by a process after taking its local
 point that is received by another process before taking its checkpoint

"A fundamental goal of any rollback-recovery protocol is to
bring the system into a consistent state when
inconsistencies occur because of a failure"

## Slide 31: Consistent/Inconsistent State  *(visual)*
In-transit messages Inconsistent state

 P0

 P1

 P2

 P3

 Consistent State
Orphan message Strongly
 consistent state
![FTC04_Rollback_Recovery slide 31](images/FTC04_Rollback_Recovery_s031.png)

## Slide 32: Domino Effect  *(visual)*
Cascaded rollback which causes the system to roll back to too far
in the computation (even to the beginning), in spite of all the
checkpoints

 failure

 Suppose Y rolls back to y2
 • m is orphan message
 • Process X must rollback to x2
 Suppose Z rolls back to z2
 • Y rolls back to y1
 32 • Force X, Z to roll back to x1, z1
![FTC04_Rollback_Recovery slide 32](images/FTC04_Rollback_Recovery_s032.png)

## Slide 33: Livelocks  *(visual)*
x1
 X n1
 y1 m1
 Y
 failure
 x1
 X n2 n1 y1 m2
 Y
 2nd Rollback

• Y crashes before receiving n1. Y rolls back to Y1 -> X to x1.
• Y recovers, receives n1 and sends m2.
• X recovers, sends n2 but has no record of sending n1
• Hence, Y is forced to rollback second time. X also rolls back as it has
 received m2 but Y has no record of m2.
• Above sequence can repeat indefinitely, causing a livelock.
![FTC04_Rollback_Recovery slide 33](images/FTC04_Rollback_Recovery_s033.png)

## Slide 34: Consistent Checkpoints  *(visual)*
• Overcoming domino effect and livelocks: checkpoints should
 not have messages in transit.
• Consistent checkpoints: no message exchange between any
 pair of processes in the set as well as outside the set during
 the interval spanned by checkpoints.
• {x1,y1,z1} is a strongly consistent checkpoint.

 x1 x2 x3
 X
 m y1 y2
 Y

 Z z1 z2
![FTC04_Rollback_Recovery slide 34](images/FTC04_Rollback_Recovery_s034.png)

## Slide 35: Recovery Techniques  *(visual)*
Rollback-Recovery

 checkpointing logging

uncoordinated coordinated communication pessimistic optimistic causal
 -induced

 blocking non-blocking model-based index-based
![FTC04_Rollback_Recovery slide 35](images/FTC04_Rollback_Recovery_s035.png)

## Slide 36: Techniques that avoid Domino effect
• Coordinated checkpointing rollback recovery
 - processes coordinate their checkpoints to form a system-wide
 consistent state
• Communication-induced checkpointing rollback
 recovery
 - forces each process to take checkpoints based on information
 piggybacked on the application
• Log-based rollback recovery
 - combines checkpointing with logging of non-deterministic events
 - relies on piecewise deterministic (PWD) assumption

## Slide 37: Coordinated/Blocking Protocols  *(visual)*
Rollback-Recovery

 checkpointing x1 x2
 X
 m
 y1 y2
 Y
 coordinated z1 z2
 Z

blocking

 • no messages can be in transit during checkpointing
 • {x1, y1, z1} forms "recovery line"
![FTC04_Rollback_Recovery slide 37](images/FTC04_Rollback_Recovery_s037.png)

## Slide 38: Blocking & Non-blocking Coordinated
Checkpointing
• Blocking Checkpointing
 - After a process takes a local checkpoint, to prevent orphan
 messages, it remains blocked until the entire
 checkpointing activity is complete
 - Disadvantages
 • the computation is blocked during the checkpointing
• Non-blocking Checkpointing
 - The processes need not stop their execution while taking
 checkpoints
 - A fundamental problem in coordinated checkpointing is to
 prevent a process from receiving application messages
 that could make the checkpoint inconsistent.

## Slide 39: Coordinated checkpointing  *(visual)*
• There is an initiator process for the checkpointing
 - Only one (or 2) checkpoint per process (always consistent)
 - large latency: processed blocked until checkpoint is
 finished

 P0: initiator
 checkpoint requests
 P1

 P2

 inconsistency if communications P3
 are not blocked until the end of
 the checkpointing phase
![FTC04_Rollback_Recovery slide 39](images/FTC04_Rollback_Recovery_s039.png)

## Slide 40: Coordinated checkpointing (2)
• Algorithm:
 - block communications while the protocol executes
 - An initiator takes a checkpoint and broadcasts a request
 message to all processes
 - When a process receives this message, it
 • stops its execution,
 • flushes all the communication channels,
 • takes a tentative checkpoint, and
 • sends an acknowledgment message back
 - the coordinator receives acknowledgments from all
 processes, and broadcasts a commit message
 - After receiving the commit each process removes the old
 checkpoint, the new one becomes permanent

## Slide 41: Coordinated Checkpointing (3)  *(visual)*
Overall execution graph
![FTC04_Rollback_Recovery slide 41](images/FTC04_Rollback_Recovery_s041.png)

## Slide 42: Checkpoint inconsistency  *(visual)*
• message m is sent by 𝑃0 after
 receiving a checkpoint request
 from the checkpoint coordinator
 • Assume m reaches 𝑃1 before the
 checkpoint request
 • This situation results in an
 inconsistent checkpoint since
 checkpoint 𝐶1,𝑥shows the
 receipt of message m from 𝑃0,
 while checkpoint 𝐶0,𝑥does not
 show m being sent from 𝑃0
![FTC04_Rollback_Recovery slide 42](images/FTC04_Rollback_Recovery_s042.png)

## Slide 43: Checkpoint inconsistency:  *(visual)*
a solution with FIFO channels

• If channels are FIFO, this
problem can be avoided by
preceding the first post-
checkpoint message on each
channel by a checkpoint request,
forcing each process to take a
checkpoint before receiving the
first post-checkpoint message
![FTC04_Rollback_Recovery slide 43](images/FTC04_Rollback_Recovery_s043.png)

## Slide 44: Uncoordinated checkpointing
• Each process has autonomy in deciding when to take checkpoints
• Advantages
 - The lower runtime overhead during normal execution
• Disadvantages
 - Domino effect during a recovery
 - Recovery from a failure is slow because processes need to iterate to find a
 consistent set of checkpoints
 - Each process maintains multiple checkpoints and periodically invoke a garbage
 collection algorithm
 - Not suitable for application with frequent output commits
• The processes record the dependencies among their checkpoints
 caused by message exchange during failure-free operation

## Slide 45: Communication-induced Checkpointing
• Two types of checkpoints
 - autonomous and forced checkpoints
• Communication-induced checkpointing piggybacks protocol- related
 information on each application message
• The receiver of each application message uses the piggybacked
 information to determine if it has to take a forced checkpoint to
 advance the global recovery line
• The forced checkpoint must be taken before the application may
 process the contents of the message
• In contrast with coordinated checkpointing, no special coordination
 messages are exchanged
• Two types of communication-induced checkpointing
 - model-based checkpointing and index-based checkpointing.

## Slide 46: Log-based Rollback Recovery
• A log-based rollback recovery makes use of deterministic
 and nondeterministic events in a computation.
• Deterministic and Non-deterministic events
 - Non-deterministic events can be the receipt of a message from another
 process or an event internal to the process
 - a message send event is not a non-deterministic event.
 - the execution of process 𝑃0 is a sequence of four deterministic intervals
 - Log-based rollback recovery assumes that all non-deterministic events can
 be identified and their corresponding determinants can be logged into the
 stable storage
 - During failure-free operation, each process logs the determinants of all
 non-deterministic events that it observes onto the stable storage

## Slide 47: Pessimistic Logging
• piecewise determinism = all non-deterministic events can be
 identified and their determinants can be stored on stable
 storage.
• An execution is a sequence of deterministic events (replayed)
 and non-deterministic events (logged and simulated from log)
• determinants of non-deterministic events are stored during
 failure-free execution
• + checkpoints to avoid recovering from the start
• Additional hypothesis: It is possible to prevent a message
 from being sent or received

## Slide 48: Pessimistic Logging
• A process is orphan if it depends on the execution of a non-logged
 non-deterministic event
• Determinant: the information need to "replay" the occurrence of a
 non-deterministic event (e.g., message reception)
• always-no-orphans condition:
 - Stable(e) set of processes with e logged on stable storage
 - Depend(e) set of processes affected by event e
 - Log(e) = set of processes locally storing the event e

else the process is said orphan

## Slide 49: Pessimistic message logging  *(visual)*
• orphan processes are never created but requires a lot of
 synchronizations with the stable storage
• Logs the determinant of ND events before executing them
 synchronous logging (stronger condition)
 Only 1 process
 restarts
 P0

 P1

 P2

 P3
 message resent during recovery
 logged message reception (might have to be cancelled) 49
![FTC04_Rollback_Recovery slide 49](images/FTC04_Rollback_Recovery_s049.png)

## Slide 50: Other Issues
• Output commit
 - the state from which messages are sent to the "outside world"
 can be recovered
 - affects latency of message delivery to "outside world" and
 overhead of checkpoint/logging

• Stable storage
 - survives process failures
 - contains checkpoint/logging information

• Garbage collection
 - removal of checkpoints/logs no longer needed

## Slide 51: HW04: Checkpointing  *(visual)*
▪ Find the consistent cuts in the figure below (passing by ▓)

▪ The recovery line that you found is consistent, strongly consistent or
 inconsistent?
![FTC04_Rollback_Recovery slide 51](images/FTC04_Rollback_Recovery_s051.png)


---

# FTC05_Coding_Theory

> Source: `2110473_2026S1_FTC05_Coding_Theory-9294-17893470140015.pdf` — 92 slides. `visual: true` slides have a rendered image in `images/`.

## Slide 1: Home Exercise: Checkpointing  *(visual)*
▪ Find the consistent cuts in the figure below (passing by ▓)

▪ The recovery line that you found is consistent, strongly consistent or
 inconsistent?
![FTC05_Coding_Theory slide 1](images/FTC05_Coding_Theory_s001.png)

## Slide 2: Coding Theory
(Information Redundancy)

 2110473 Fault Tolerant Computing

Code Design for Dependable Systems, Eiji Fujiwara, JOHN WILEY & SONS, ISBN-13 978-0-471-75618-7, 2006
Notes on Coding Theory, J.I.Hall, Michigan State University, 2010
and Several Sources

## Slide 3: Contents
• Introduction
• Definition of Code
• Hamming Distance
• Linear/Cyclic Codes & Implementation
• Error Controls for Digital Systems
• Error Correcting Code
• Error Detecting Code: Checksum Code,
 Residue Code, Berger Code, Unordered Code

## Slide 4: Introduction
❑Coding Theory
 ▪The study of the properties of codes and their
 fitness for a specific application
 - Data Compression
 - Error Correction/ Error Control
 - Cryptography
 - Network Coding

## Slide 5: Various Stages of Data Processing  *(visual)*
5
![FTC05_Coding_Theory slide 5](images/FTC05_Coding_Theory_s005.png)

## Slide 6: Reliable Communication  *(visual)*
• In practice, most media are not perfect, Noisy channels:
 - Fiber-optic line, Satellite link, Hard disk, …
• Can we recover the original message (without errors)
 from a noisy code string?
• We focus two things:
 - Length of the code string
 - Probability of error
![FTC05_Coding_Theory slide 6](images/FTC05_Coding_Theory_s006.png)

## Slide 7: Coding Theory
• Coding theory - theory of error correcting codes - is one of the
 most interesting and applied part of mathematics and
 informatics
• All real communication systems that work with digitally
 represented data, as CD players, TV, fax machines, internet,
 satellites, mobiles, require to use error correcting codes
 because all real channels are, to some extent, noisy - due to
 interference caused by environment
 - Coding theory problems are therefore among the very basic and most
 frequent problems of storage and transmission of information
 - Coding theory results allow to create reliable systems out of unreliable
 systems to store and/or to transmit information
 - Coding theory methods are often elegant applications of very basic
 concepts and methods of (abstract) algebra

## Slide 8: Coding Theory/ Cryptography/ Steganography
❑Coding Theory
 ▪Methods to protect information against a noise
 ▪Theory of Error Correcting Codes (Error Control Codes)
 ❑Cryptography
 ▪Methods how to protect information against an
 enemy (or an unauthorized user)
 ▪Battles between codemakers and codebreakers
 ❑Steganography
 ▪Methods to hide important information in innocently
 looking information (and that can be used to protect
 intellectual properties)

## Slide 9: Basic Concept  *(visual)*
Error-correcting codes are used to correct messages when they are
transmitted through noisy channels

 Error correcting framework
Example

A code C over an alphabet is a subset of *(C *)
A q -nary code is a code over an alphabet of q -symbols
A binary code is a code over the alphabet {0,1}

Examples of codes C1 = {00, 01, 10, 11} C2 = {000, 010, 101, 100}
 C3 = {00000, 01101, 10111, 11011}
![FTC05_Coding_Theory slide 9](images/FTC05_Coding_Theory_s009.png)

## Slide 10: Transmission through Channel
• Physical medium through which information is transmitted
 (ex. Telephone lines, the atmosphere)
• Noise: may be caused by sunspots, lighting, meteor
 showers, random radio disturbance, poor typing, poor
 hearing, . . . .
• Transmission Goals
 - Fast encoding of information
 - Easy transmission of encoded messages
 - Fast decoding of received messages
 - Reliable correction of errors introduced in the channel
 - Maximum transfer of information per unit time
• BASIC METHOD OF FIGHTING ERRORS: REDUNDANCY!!!
 0 is encoded as 00000 and 1 is encoded as 11111

## Slide 11: Claude Elwood Shannon  *(visual)*
"The father of Information Theory"
 American mathematician, electrical
 engineer, and cryptographer
 (Apr.30, 1916 - Feb.24, 2001)
![FTC05_Coding_Theory slide 11](images/FTC05_Coding_Theory_s011.png)

## Slide 12: Shannon's Theorem
• Noisy-channel coding theorem
• Given a noisy channel with channel capacity C and the
 information transmitted at the rate R
 - If R < C, it is possible to transmit information nearly without error at any rate
 below a limiting rate
 - If R > C, an arbitrarily small probability of error is not achievable
• Channel capacity: the highest information rate that can be achieved with
 arbitrarily small error probability
 𝑺
 𝑪= 𝑩𝐥𝐨𝐠𝟐(𝟏+ 𝑵)

## Slide 13: Channel Capacity
• Channel Capacity C: Probabilistic properties of the channel
• Encoding messages of b bits into code words of b/R bits,
 for some rate 0 < R < 1
• Error is the event that the original message cannot be
 correctly decoded from the received code word
• R is achievable using a channel, if there is an encoding such
 that the probability of error goes to zero as b increases

• The Source Coding (Shannon's 2nd Theorem):
 Rate R is achievable if R < C,
 and not achievable if R > C

## Slide 14: Binary Symmetric Channel
• The probability of error 𝑝< ½
• If 𝑛symbols are transmitted,
then the probability of 𝑡errors is
 𝑝𝑡(1 −𝑝)𝑛−𝑡𝑛
 𝑡
• Consider 𝐶= {000,111},
 = 1 −((1 −𝑝)3+3𝑝(1 −𝑝)2) 𝑃𝑒𝑟𝑟(𝐶)

• If p = 0.01, then (C) = 0.000298 and only one Perr
 word in 3555 will reach the user with an error

## Slide 15: Binary symmetric channel (BSC) capacity
• Error rate p:
 Pr[𝑦= 1|𝑥= 0] = Pr[𝑦= 0|𝑥= 1] = 𝑝
 where x is the transmitted and y the received bit
• Channel capacity C(p):

 1 1
𝐶𝑝= 1 −𝐻𝑝= 1 −[𝑝log2 𝑝+ (1 −𝑝) log2 1−𝑝]
 (H: binary entropy function)
• For instance, 𝐶(0.1) ≈0.53, Ratio about 1:2

## Slide 16: Channel Coding Theorem, … So what?
• Assume you want to transmit data with
 probability of error 10-15 over a BSC, p = 0.1
• Using a repetition code, we need to make the
 message 63 times as long as the source string
 (binomial distribution)

• Shannon's result says twice as long is enough!
• If you want probability of error 10-100, Shannon's
 result still says that twice is enough!!
• However the messages you encode need to be
 sufficiently long!

## Slide 17: Example
The encoding

 0→000 1 →111

 1
The probability of the bit error 𝑝 and the majority 2,
voting decoding

 000, 001, 010, 100 →000, 111, 110, 101, 011 →111
The probability of an erroneous message is
 3𝑝2 1 −𝑝+ 𝑝3 = 3𝑝2 −2𝑝3 < 𝑝

## Slide 18: enemy territory  *(visual)*
Coding of a path avoiding an
 enemy territory

Story: Alice and Bob share an
identical map gridded as shown.
Only Alice knows the route
through which Bob can reach
her avoiding the enemy territory.
Alice wants to send Bob the
following information about the
safe route he should take

NNWNNWWSSWWNNNNWWN
![FTC05_Coding_Theory slide 18](images/FTC05_Coding_Theory_s018.png)

## Slide 19: NNWNNWWSSWWNNNNWWN
Three ways to encode
• = {00, 01, 10, 11} C1
 - 000001000001011111010100000000010100
 - Any error in the code word would be a disaster
• = {000, 011, 101, 110} C2
 - A single error in encoding each of N, W, S, E could be
 detected
• {00000, 01101, 10110, 11011} C3=
 - A single error in decoding each of N, W, S, E could be
 corrected

## Slide 20: Definition of Code
• A code 𝐶over an alphabet Σ is a subset of
 Σ∗(C ⊆Σ∗)
• A q-nary code is a code over alphabet of q symbols
• A binary code is a code over the alphabet {0,1}

## Slide 21: Richard Wesley Hamming  *(visual)*
"Hamming Distance"
American mathematician
"The purpose of computing is insight,
not numbers"
(Feb.11, 1915 - Jan.7, 1998)
![FTC05_Coding_Theory slide 21](images/FTC05_Coding_Theory_s021.png)

## Slide 22: Hamming Weight
• Hamming Weight w(𝑐):
 - the number of nonzero components in the
 codeword

 ex.
 w(00000) = 0
 w(11111) = 5
 w(1022001) = 4
 w(1011001) = 4

## Slide 23: Hamming Distance  *(visual)*
• Hamming Distance ℎ(𝑥, 𝑦):
 - The number of positions where words x and y differs
 ex: ℎ10101; 01100 = 3, ℎ(𝑓𝑜𝑢𝑟𝑡ℎ; 𝑒𝑖𝑔ℎ𝑡ℎ) = 4
• Properties:
 - ℎ𝑥, 𝑦= 0 ⇔𝑥= 𝑦
 - ℎ𝑥, 𝑦= ℎ𝑦, 𝑥
 - ℎ𝑥, 𝑧≤ℎ𝑥, 𝑦+ ℎ(𝑦, 𝑧) triangle inequality
• Minimal distance:
 ℎ𝐶= min ℎ𝑥, 𝑦𝑥, 𝑦∈𝐶, 𝑥≠𝑦

 Code 𝐶can detect up to 𝑠errors if ℎ(𝐶) ≥𝑠+ 1
 Code 𝐶can correct up to 𝑡errors if ℎ𝐶≥2𝑡+ 1
![FTC05_Coding_Theory slide 23](images/FTC05_Coding_Theory_s023.png)

## Slide 24: Hamming VS Shannon  *(visual)*
Hamming Shannon
Focus on codewords itself Directly deal wt encoding and
 decoding functions
 Look at explicit codes Not explicit at all

 Fundamental trade off: Fundamental trade off:
 rate vs distance rate vs error
 (easy to handle)

 Worst case errors Stochastic errors
![FTC05_Coding_Theory slide 24](images/FTC05_Coding_Theory_s024.png)

## Slide 25: Power of Parity Bits
• Let all 211 of binary words of length 11 be codewords
• Let the probability of an error be 10 -8
• Let bits be transmitted at the rate 107 bits per second

• The probability that a word is transmitted incorrectly is approximately
 10 11 11 p (1 −p )  .
 108
 11• Therefore 8  10117 = 1.0 of words per second (every 10 seconds) are 10
 transmitted incorrectly
• Let one parity bit be added Any single error can be detected
• The probability of at least two errors is:
 12 11 12 10 2 66 1 − (1 − p ) − 12(1 − p ) p  ( 2 )(1 − p ) p  16
 7 10 66• Therefore approximately 16  1012  5.5  10 −9 words per second 10
 are transmitted with an undetectable error
• Corollary One undetected error occurs only every 2000 days! (2000 
 109/(5.5 86400).) 25

## Slide 26: Two-Dimensional Parity Code
• The two-dimensional parity code arranges the
 data into a two-dimensional array and then to
 each row (column) parity bit is attached
ex. 10001011000100101111

 1 0 0 0 1 0
 1 0 0 0 1
 0 1 1 0 0 0
 0 1 1 0 0
 → 0 1 0 0 1 0
 0 1 0 0 1
 0 1 1 1 1 0
 0 1 1 1 1
 1 1 0 1 1 0

## Slide 27: Notation
An (n,M,d) - code C is a code such that
• n - is the length of codeword
• M - is the number of codeword
• d - is the minimum distance in C

ex.
C1 = {00, 01, 10, 11} is a (2,4,1) - code
C2 = {000, 011, 101, 110} is a (3,4,2) - code
C3 = {00000, 01101, 10110, 11011} is a (5,4,3) - code

 A good (n,M,d) code has small n and large M and d

## Slide 28: Optimization
A good (n,M,d) -code has small n, large M and large d
Notation: Aq(n,d) is the largest M such that there is an
 q-nary (n,M,d)-code
Theorem: (a) Aq(n,1) = qn
 (b) Aq(n,n) = q

ex. A2(8, d) for d = 1 and d = 2
1. d = 1. A2(8, 1) = 28. Code C contains all binary words of the length
 eight
2. d = 2. A2(8, 2) = A2(7, 1) = 27. Code C contains all binary words of
 the length seven with the parity bit added

## Slide 29: Design of one code from another code
•If d is odd, then (n,d) = (n +1,d +1) A2 A2
•If d is even, then (n,d) = (n -1,d -1) A2 A2

 = 4ex. A2(5,3) = 4 A2(6,4)
 (5,4,3)-code (6,4,4)-code

## Slide 30: Equivalence
• Two q-nary codes are equivalent if one can be
 obtained from the other by a combination of
 following operations:
1. permutation of the positions of the code
2. permutation of symbols at the fixed positions

## Slide 31: Linear Codes
• Binary Linear Codes
 - A binary linear code C of length n is a set of binary
 n-tuples such that the componentwise modulo 2
 sum of any two codewords is contained in C

ex.5 (4,4,2)-code: {0000,0101,1010,1111}

 (7,16,3)-code: { ?? }
 {0000000,0001111,0010110,0011001,0100101,0101010,0110011,011
 1100,1000011{0000000,0001111,0010110,0011001,0100101,0101010
 ,0110011,0111100,1000011,1001100,1010101,1011010,1100110,110
 1001,1110000,1111111}
 31
 ,1001100,1010101,1011010,1100110,1101001,1110000,1111111}

## Slide 32: Cyclic Codes
A code C is cyclic if
1. C is a linear code
2. any cyclic shift of a codeword is also a codeword

ex1. The ternary code C = {0000,1212,2121} is cyclic
1. Linear: c1+c2=c2, c1+c3=c3, c2+c3=c1, c2+c2=c3, c3+c3=c2
2. Cyclic: c1 →c1, c2 →c3 →c2

ex2. The binary code C = {000,110,011,101} is cyclic
ex3. 5-bit cyclic code C = {00000,00011,00110,01100,11000,10001,
00101,01010,10100,01001,10010,01111,11110,11101,11011,10111}

## Slide 33: Check yourself 1
• Use nearest neighbor decoding to determine
 which code word was sent from the code C =
 {0000, 1110, 1011} if 0110 is received?

 d(0110,0000)=?
 d(0110,1110)=?
 d(0110,1011)=?

## Slide 34: Check yourself 2
• Suppose that when a bit is sent over a binary
 symmetric channel the probability it is
 received incorrectly is 0.01. What is the
 probability that the bit string 100010 is
 received when the bit string 000000 is sent?

 Maximum likelihood decoding:
 Prob (4 correct & 2 incorrect) =
• (0.99)4(0.01)2 = 0.000096059601

## Slide 35: Check yourself 3
• Find the minimum distance of the code;
 C = {00000, 01110, 10011, 11111}

 All combinations
 d(00000, 01110) = ?
 d(00000, 10011) = ?
 d(00000, 11111) = ?
 d(01110, 10011) = ?
 d(01110, 11111) = ?
 d(10011, 11111) = ?

## Slide 36: Check yourself 4
• Let C = {00000000, 11111000, 01010111,
 10101111},
How many errors can C detect and how many
can it correct?

 Minimum distance C {00000000, …, 10101111} = ?
 Detect upto = (minimum distance - 1) = ?
 Correct upto = | (minimum distance - 1) / 2 | = ?

## Slide 37: Cyclic Codes - Theory
• k - number of bits of data that are encoded
• Encoded word of length n bits
 - obtained by multiplying the given k data bits by a number
 that is n-k+1 bits long
• The multiplier is represented as a polynomial
 - the generator polynomial
• 1s and 0s in the n-k+1-bit multiplier are treated as
 coefficients of an (n-k) -degree polynomial
• Example: multiplier is 11001 - generator polynomial is
 G(x)=1X0 + 0X1 + 0X2 + 1X3 + 1X4 = 1 + X3 + X4

## Slide 38: Cyclic codes
• Definition: Any cyclic shift of a codeword produces another codeword
• A k-bit data word corresponds to a polynomial of degree k-1
 Data = 1101001: d(x) = 1 + x + x3 + x6 (modulo-2 sum)
 (n, k) cyclic code has a generator polynomial of degree r = n-k

 g(x) = 1 + x + x3
 To encode data (1101001), multiply its associated polynomial by g(x)

• Detect all burst errors of width less than n-k

## Slide 39: An (n,k) Cyclic Code
• Using a generator polynomial of degree n-k and total
 number of encoded bits n
• An (n,k) cyclic code can detect all single errors and all runs
 of adjacent bit errors shorter than n-k
• For a polynomial to be a generator polynomial for an (n,k)
 cyclic code it must be a factor of Xn-1 (=Xn+1)
• 1+X3+X4 is a factor of X15-1 →(15,11) code
 X15-1=(X+1)(X2+X+1)(X4+X+1)(X4+X3+1)(X4+X3+X2+X+1)
• For the 5-bit code, (X+1) - generator polynomial
 X5-1 = (X+1)(X4+X3+X2+X+1)
• Multiply {0000,….,1111} by (X+1) to obtain all codewords of
 the (5,4) code

## Slide 40: Factorization of X  *(visual)*
n-1 (Xn+1)
![FTC05_Coding_Theory slide 40](images/FTC05_Coding_Theory_s040.png)

## Slide 41: Modulo-2 Multiplication  *(visual)*
• The 5th bit of the product is
 the modulo-2 sum of the
 corresponding bits of the
 multiplicand shifted 0 times, 3
 times, and 4 times
• If multiplicand is fed in serially
 - we add the shifted
 multiplicand
• Shifting done by delay
 elements
• This cyclic code is not
 separable - data and check
 bits within 110000100011101
 are not separable
![FTC05_Coding_Theory slide 41](images/FTC05_Coding_Theory_s041.png)

## Slide 42: Operation of Encoding Code  *(visual)*
• i3 is the input to the O3
 delay element

 110000100011101

 10001100101
![FTC05_Coding_Theory slide 42](images/FTC05_Coding_Theory_s042.png)

## Slide 43: Decoding Through Division by  *(visual)*
Generator Polynomial

 error!!

• Division by 11001
• Subtraction modulo-2 - identical to addition
• Zero remainder indicates no error detected
• If a single error occurs - 110000100111101 - non-zero remainder
![FTC05_Coding_Theory slide 43](images/FTC05_Coding_Theory_s043.png)

## Slide 44: Three Bit Errors  *(visual)*
• 110000111010101 instead of 1100000100011101 - zero remainder
 - errors not detected (erroneously)
• If errors are adjacent - 110000011011101 - non-zero remainder
 indicates an error 44
![FTC05_Coding_Theory slide 44](images/FTC05_Coding_Theory_s044.png)

## Slide 45: Cyclic code implementation
• Multiply K bit data by (n-k+1) bit multiplier ((n-k) degree
 polynomial), the result is n bit encoded data: (n,k) cyclic code
• Shift register circuit for multiplying by generator polynomial,
 g(x) = g0+g1x+· · ·+grxr
• An encoder for an (n, k) cyclic code with generator polynomial
 g(x), with r = n-k

## Slide 46: Implementing a Divider Circuit
• Division can be done by multiplication in the feedback
 loop
• Example: Encoded word - polynomial E(X), generator
 polynomial - G(X), original data word - polynomial D(X)
• If no bit errors exist - we will receive E(X) and calculate
 D(X) by D(X)=E(X)/G(X) - remainder will be zero
• Example: E(X)=D(X)G(X)=D(X)(1+X3+X4)
 = D(X)+D(X)(X3+X4)
• D(X)=-E(X)+D(X)(X3+X4)=E(X)+D(X)(X3+X4)
 ∗(since addition = subtraction in mod-2 arithmetic)

## Slide 47: Generator Polynomial
• (n,k) cyclic code:

• If n = 5: x5 + 1 = (x + 1)(x4 + x3 + x2 + x + 1)
 example 1: k = 4, g(x) = (x + 1)

• If n = 7: x7 + 1 = (x + 1)(x3 + x + 1)(x3 + x2 + 1)
 example 2: k = 4, g(x) = (x3 + x + 1)

## Slide 48: Cyclic code
encoding example 1

• k = (0111), g(x) = (1 + x)

 x 1 1 1 0 →
 + 1 0 0 1 0 →= (01001)

 1 1 1 0 → D
 1 1 1 0 x →

## Slide 49: Cyclic code
decoding example 1

• k(x) = e(x)/g(x) - Remainder (zero if no error)
• E = (01001), g(x) = (1 + x) k(x) = e(x) + k(x)*x

 0 1 0 0 1
 + 0 1 0 0 1

 0 1 1 1 0 D

 x 0 1 1 1

## Slide 50: Cyclic code
decoding example 1

• K(X) = E(X)/G(X) - Remainder (non-zero if error)
• E = (01101), g(x) = (1 + x) K(X) = E(X) + K(X)*X

 0 1 1 0 1
 + 0 1 1 0 1

 0 1 0 0 1 D
 x 0 1 0 0

## Slide 51: Cyclic code  *(visual)*
encoding example 2
 • K = (0111), g(x) = (1 + x + x3)

 0111 A1 A3 E 1 1 0 0 0 1 0 → + +
 1101 E = (0100011)
 0111 K
 1 1 1 0 → D1 D2 D3 0111
0111
0100011 K D1 A1 D2 D3 A3 (E)

 0 x 0 x x 0

 1 0 1 x x 1

 1 1 0 0 x 0

 1 1 0 1 0 0

 0 1 1 1 1 0

 0 0 0 1 1 1

 0 0 0 0 1 1 51
![FTC05_Coding_Theory slide 51](images/FTC05_Coding_Theory_s051.png)

## Slide 52: Cyclic code  *(visual)*
decoding example 2
 • E = (0100011), g(x) = (1 + x + x3) K(X) = E(X) + K(X)(X + X3)

0100011 A1 E0 1 0 0 0 1 1 0 1 1 1 K A3 + + 1101 :01
 10111
 D3 D2 D1 1101 :1
 1101
 1101 :1 E D1 D2 D3 A1 A3 (K)
 000
 0 x x x 0 0

 1 0 x x 1 1

 0 1 0 x 1 1

 0 1 1 0 1 1

 0 1 1 1 1 0

 1 0 1 1 1 0

 1 0 0 1 1 0 52
![FTC05_Coding_Theory slide 52](images/FTC05_Coding_Theory_s052.png)

## Slide 53: Cyclic code  *(visual)*
decoding example 2
 • E = (0101011), g(x) = (1 + x + x3) K(X) = E(X) + K(X)(X + X3)

0101011
 E0 1 0 1 0 1 1 0 1 1 0 K A3 A1 + + 1101 :01
 11111
 D3 D2 D1 1101 :1
 0101
 0000 :0 E D1 D2 D3 A1 A3 (K)
 101
 0 x x x 0 0

 1 0 x x 1 1

 0 1 0 x 1 1

 1 1 1 0 0 0

 0 0 1 1 0 1

 1 1 0 1 0 1

 1 1 0 0 0 0 53
![FTC05_Coding_Theory slide 53](images/FTC05_Coding_Theory_s053.png)

## Slide 54: Code Rate
• For 𝑞-nary (𝑛, 𝑀, 𝑑) - code we define code rate, or
 information rate, 𝑅, by
 log𝑞𝑀
 𝑅=
 𝑛
• The code rate represents the ratio of the number of
 needed input data symbols to the number of
 transmitted code symbols

• Code rate is an important parameter for real
 implementations, because it shows what fraction of
 the bandwidth is being used to transmit actual data

## Slide 55: Error Detection  *(visual)*
55
![FTC05_Coding_Theory slide 55](images/FTC05_Coding_Theory_s055.png)

## Slide 56: Error Detection
• Error detection is much more modest aim than error
 correction
• Error detection is suitable in the cases that channel is
 so good that probability of error is small and if an error
 is detected, the receiver can ask to renew the
 transmission
• For example, two main requirements for many
 telegraphy codes used to be:
 - Any two codewords had to have distance at least 2;
 - No codeword could be obtained from another codeword
 by transposition of two adjacent letters

## Slide 57: Evaluation of error-detecting codes
• Redundancy: k data bits encoded in n = k+r bits (r redundant bits)
• Encoding: Complexity (cost / time) to form codeword from data
 word
• Decoding: Complexity (cost / time) to obtain data word from
 codeword
 Separable codes have computation-free decoding
• Capability: Classes of error that can be detected
 Greater detection capability generally involves more redundancy
 To detect d bit-errors, a minimum code distance of d+ 1 is
required
 Examples of code detection capabilities:
 Single, double, b-bit burst, byte, unidirectional, . . . errors
• Closure: Arithmetic and other operations done directly on
 codewords
 (rather than in 3 stages: decode, operate, and encode)

## Slide 58: Further Readings
(Out-of-scope)

• Other Properties of Codes
• ISBN Code
• Data Compression
 - ZIP Code, Reed-Solomon Code
• Cryptography
• Information Theory

## Slide 59: HW05: Cyclic code
• Generate (7,4) Cyclic code from the data
 (0101, 1001, 0010, 1110, 0000), and its
 hardware implementation.

## Slide 60: Home Exercise: Cyclic code 1/4
(calculation)
• Generate (7,4) Cyclic code from the data
 (0101, 1001, 0010, 1110, 0000), and its
 hardware implementation.

 Ans: when m = [0101]
 (7,4) Cyclic code: N = 7, N - K = 3, then
 x7 + 1 = (x+1)(x3+x+1)(x3+x2+1)
 for m = [0101] m(x) = x+x3
 c(x) = m(x)g(x) = (x+x3)(x3+x2+1) = x+x4+x5+x6
 Hence, c = [0100111]
 m(0101, 1001, 0010, 1110, 0000) 
 c(0100111,1010011,0010110,1100010,0000000)

## Slide 61: (Encoding)  *(visual)*
Home Exercise: Cyclic code 2/4
 (Encoding)
 • m = (0101), g(x) = (1 + x2 + x3)

 0101 A0 A2 A3 E 1 1 1 0 0 1 0 → + +
 1011 E = (0100111)
 0101 K
 1 0 1 0 → D1 D2 D3 0101
0101
0100111 K (A0) D1 D2 A2 D3 A3 (E)

 0 x x 0 x 0

 1 0 x 1 x 1

 0 1 0 0 x 0

 1 0 1 0 0 0

 0 1 0 0 1 1

 0 0 1 1 0 1

 0 0 0 0 1 1
![FTC05_Coding_Theory slide 61](images/FTC05_Coding_Theory_s061.png)

## Slide 62: Implementing a Divider Circuit
• Division can be done by multiplication in the feedback
 loop
• Example: Encoded word - polynomial E(X), generator
 polynomial - G(X), original data word - polynomial D(X)
• If no bit errors exist - we will receive E(X) and calculate
 D(X) by D(X)=E(X)/G(X) - remainder will be zero
• Example: E(X)=D(X)G(X)=D(X)(1+X3+X4)
 = D(X)+D(X)(X3+X4)
• D(X)=-E(X)+D(X)(X3+X4)=E(X)+D(X)(X3+X4)
 ∗(since addition = subtraction in mod-2 arithmetic)

## Slide 63: Cyclic code  *(visual)*
decoding example 3/4
 • E = (0100011), g(x) = (1 + x2 + x3) K(X) = E(X) + K(X)(X2 + X3)

0100011 K A3 A1 E0 1 0 0 0 1 1 0 1 1 1 + + 1101 :01
 10111
 D3 D2 D1 1101 :1
 1101
 1101 :1 E D1 D2 D3 A1 A3 (K)
 000
 0 x x x 0 0

 1 0 x x 1 1

 0 1 0 x 1 1

 0 1 1 0 1 1

 0 1 1 1 1 0

 1 0 1 1 1 0

 1 0 0 1 1 0 63
![FTC05_Coding_Theory slide 63](images/FTC05_Coding_Theory_s063.png)

## Slide 64: Error Controls for Digital Systems  *(visual)*
Data
 Transmission
 Corrected
 Digital Systems Corrector Output

 Data
Operation

 Error
 Checker Signal
![FTC05_Coding_Theory slide 64](images/FTC05_Coding_Theory_s064.png)

## Slide 65: Error Model
• Symmetric / Asymmetric error
 - Both/Only one type of Known 0→1 and 1→0 errors
 can occur wt equal probability in a codeword
• Single / Multiple error
 - One/More than one Bit error
• Unidirectional error
 - Both Unknown 0→1 and 1→0 errors can occur, but
 they do not occur simultaneously in any codeword
• Byte error
 - Multiple error in K-Byte (K: constant)

## Slide 66: Error Control Codes
• Error Correcting Code
 - Overlapped Parity Code
• Error Detection Code
 - Checksum Code
 - Residue Code
 - Unordered Code
 • m-of-n Code
 • Berger Code
 • Dual Rail Code

## Slide 67: Error Correcting Code Function  *(visual)*
67
![FTC05_Coding_Theory slide 67](images/FTC05_Coding_Theory_s067.png)

## Slide 68: Overlapped Parity Code  *(visual)*
• Single Error Correcting (SEC)/ 8-Data bits wt 4-Check bits
![FTC05_Coding_Theory slide 68](images/FTC05_Coding_Theory_s068.png)

## Slide 69: Overlapped Parity Syndrome
• Syndrome is derived from comparing, i.e. XOR,
 transmitted and received/recomputed check bits
• Syndrome has following characteristics (previous
 example)
 - if syndrome contains all 0's
 • no error has been detected
 - if syndrome contains one and only one bit set to 1
 • error has occurred in one of the 4 check bits
 - if syndrome contains more than one bit set to 1
 • numerical value of the syndrome indicates the position of
 the data-bit error
 • this bit is then inverted for correction

## Slide 70: Compute Check  *(visual)*
70
![FTC05_Coding_Theory slide 70](images/FTC05_Coding_Theory_s070.png)

## Slide 71: Example of Overlapped Parity
• Data sent is 1110 0001 and transmitted check bits
 are 1110
• Assume received data is: 01100001
• Received check bits are: 1110
• Recomputed check bits are: 0010
• Syndrome 11000010 = 1100

## Slide 72: Applying Syndrome  *(visual)*
Syndrome 1100 detects D8 as faulty
![FTC05_Coding_Theory slide 72](images/FTC05_Coding_Theory_s072.png)

## Slide 73: Check yourself 5
• ECC using Venn Diagram

 A B A B

 1 1

 1 1
 1 0 1X 0 0

 C C

## Slide 74: BCH Code
• Bose-Chaudhuri-Hocquenghem codes (1959)
• A class of Cyclic error-correcting codes
• Using polynomials over a finite field (also called Galois
 field)
• Possible to design binary BCH codes that can correct
 multiple bit errors
• BCH codes is easy to be decoded, namely, via
 an algebraic method known as syndrome decoding
• Widely used in applications such as satellite
 communications, compact disc players, DVDs, disk
 drives, solid-state drives and two-dimensional bar
 codes

## Slide 75: Checksum Code
• Separable code to achieve error detection capability
• Checksum is the sum of the original data
• Single-precision checksum
 - 𝐶= 𝑥1 + 𝑥2 + ⋯𝑥𝑛
 - overflow problem, i.e. adding n bits modulo-2n
• Double-precision checksum
 - use double precision, i.e. compute 2n-bit checksum from n-bit words
 using modulo-22n arithmetic
• Residue checksum
 - like single-precision checksum, but overflow is now fed back as carry
• Honeywell checksum
 - compose word of double length by concatenating 2 consecutive words
 - compute checksum on these double words

## Slide 76: Checksum Code
• Single precision checksum: modulo-2d addition
• Double precision checksum: modulo-22d addition
• Residue checksum: end-around carry addition
• Honeywell checksum: pair checksum

 example: SP DP RC HC
 0000 0000 0000
 0101 0101 0101
 1111 1111 1111 00000101
 0010 0010 0010 11110010
 0110 00010110 0111 11110111

## Slide 77: Checksum Code Example
• 16 bits block is to be sent using 8 bits checksum
• 10101001 00111001
 Addition 10101001
 00111001
 Sum 11100010
 Checksum 00011101 (complement)
• The pattern sent is 10101001 00111001 00011101

• How about 10101001 00111001 11001100 00011001?

## Slide 78: Constant-weight codes
• Definition: All non-separable codewords have the
 same number of 1s (m-out of-n code)
 - Can detect all unidirectional errors
 - Maximum number of codewords obtained when the weight is n/2

 A weight-2 code: A weight-1 code A weight-3 code
 00011 000001 000111
 10100 000010 001110
 00110 000100 011100
 01001 001000 111000
 01010 010000 001011
 01100 100000 010110
 10001 101100
 10010 …
 10100 110100
 11000 111000

## Slide 79: Arithmetic weight errors  *(visual)*
errornous carry of 1

• Arithmetic weight errors: Minimum number of signed powers of 2 that
 must be added to the correct value to turn it into the erroneous result
 (contrast with Hamming weight of an error)
![FTC05_Coding_Theory slide 79](images/FTC05_Coding_Theory_s079.png)

## Slide 80: Codes for arithmetic operations
• Arithmetic error-detecting codes:
 - characterized by arithmetic weights of detectable errors
 - allow direct arithmetic on coded operands
• Two classes of arithmetic error-detecting codes, based
 on a check modulus A (usually a small odd number)
 Product or AN codes
 Represent the value N by the number AN
 Residue (or inverse residue) codes
 Represent the value N by the pair (N, C),
 where C is N mod A or (N-N mod A) mod A

## Slide 81: Residue Code  *(visual)*
• If 𝑀𝑚𝑜𝑑𝐴= 0, then
 𝑋∗𝑌𝑚𝑜𝑑𝑀𝑚𝑜𝑑𝐴= 𝑋𝑚𝑜𝑑𝐴∗𝑌𝑚𝑜𝑑𝐴 𝑚𝑜𝑑𝐴
• Preserve code after operation

 X
 Result 𝑋∗𝑌𝑚𝑜𝑑𝑀 Y

 𝑀𝑜𝑑𝐺𝑒𝑛𝑒𝑟𝑎𝑡𝑜𝑟

 XmodA Detection
 𝑋∗𝑌𝑚𝑜𝑑𝐴 𝐶𝑜𝑚𝑝𝑎𝑟𝑎𝑡𝑜𝑟 Signal YmodA
![FTC05_Coding_Theory slide 81](images/FTC05_Coding_Theory_s081.png)

## Slide 82: Low-cost Residue codes
• Represent N by separable code of the pair (N, C(N)),
 where C(N) = N mod A
 Low-cost residue codes use A = 2a-1
• To compute N mod (2a-1), add a-bit segments of N,
 modulo 2a-1 (no division is required)

Example: Compute 0101 1101 1010 1110 mod 15
 0101 + 1101 = 0011 (addition with end-around carry)
 0011 + 1010 = 1101
 1101 + 1110 = 1100 The final residue mod 15

## Slide 83: Low-Cost Residue Code
• Complex Hardware of 𝑋𝑚𝑜𝑑𝐴
• If 𝐴= 2𝑏−1, then
 𝑛−1
 𝑋𝑚𝑜𝑑2𝑏−1 = ෍ 𝑋𝑖𝑚𝑜𝑑(2𝑏−1)
 𝑖=0
• Use b bit End-around carry Adder
ex. 𝑏= 3, 𝐴= 7,and 𝑋= 110100011

 𝑋𝑚𝑜𝑑7 = 419 𝑚𝑜𝑑7 = 110 + 100 + 011 = 110 = 6

## Slide 84: Arithmetic on Residue-coded operands  *(visual)*
• Add/subtract: Data and check parts are handled separately
 (x, C(x)) ± (y, C(y)) = (x±y, (C(x) ±C(y)) mod A)
• Multiply:
 (a, C(a)) × (x, C(x)) = (a×x, (C(a)×C(x)) mod A)
• Divide/square-root: difficult
![FTC05_Coding_Theory slide 84](images/FTC05_Coding_Theory_s084.png)

## Slide 85: Unordered Code
• A Code in which no codeword is covered by any
 other codeword
• Unidirectional error cannot transform one codeword
 to another codeword

• 𝑋(𝑥1, 𝑥2, … , 𝑥𝑘) covers 𝑌(𝑦1, 𝑦2, … , 𝑦𝑘) is 𝑋𝑌
• 𝑋= 101010 and 𝑌= 101000 then 𝑋𝑌
• If 𝑋𝑌, then ℎ(𝑌, 𝑋) = 0
• If 𝑋≱𝑌and 𝑌≱𝑋, then 𝑋and 𝑌are Unordered

## Slide 86: m-of-n Code
• All codewords are n bits in length and contain exactly
 m 1s
• Non-separable and Constant Weight Code

• Simple implementation:
 - add/append second data word
 - select word such that code word contains m 1s
 - code is separable
 - 100% overhead
• Hamming distance is 2
 - e.g. 1st error sets bit, 2nd error resets other bit

## Slide 87: Berger Code
• Separable Code which corresponding to the number
 of 1s in Data bits, and appending the bit-by-bit
 complement binary Check bits
• Can detect all unidirectional errors
• 𝑘Data bits wt 𝑐check bits of 𝑛bits Berger code:
 𝑐= 𝑙𝑜𝑔2(𝑘+ 1) and 𝑛= 𝑘+ 𝑐

ex. 𝑘= 0101000 = 2 1𝑠, 𝑐= 010 = 101

 𝑋= 0101000101

## Slide 88: Berger Code example
A Berger code (k=6, c=3):

 w=0 000000 111
 w=1 000001 110
 w=1 000010 110
 w=2 000011 101
 . . .
 w=4 100111 001
 w=2 101000 101
 . . .
 w=5 111110 010 Check bit
 w=6 111111 000

## Slide 89: Dual Rail Code  *(visual)*
x z
• 1-of-2 Code X Z x' z'
 {0,1} {01,10} x z X Z
• Easy Implementation x' z'
 (Encoder/Decoder) x
 z
• Preserve code after X Z y
 operation Y x' z'
 y'• Non-Inverter Circuit
 x
 z X
 Z y
 x'
 Y
 z'
 y'
![FTC05_Coding_Theory slide 89](images/FTC05_Coding_Theory_s089.png)

## Slide 90: Dual Rail Code example  *(visual)*
𝐹= ത𝑎𝑏+ 𝑏ҧ𝑐+ 𝑎𝑐

ത𝐹= 𝑎+ ത𝑏 ത𝑏+ 𝑐 ത𝑎+ ҧ𝑐
![FTC05_Coding_Theory slide 90](images/FTC05_Coding_Theory_s090.png)

## Slide 91: Applications: Error detection in UPC-A  *(visual)*
• Checksum codes: Given a data vector x1, x2, . . . , xn,
encode the data by attaching the checksum xn+1 to the end
 (Σj=1 to n+1wjxj = 0 mod A)
 (Weight vector wj elements are predetermined constants)
• Capabilities: All single-digit errors; Most transposition errors
Example: For the UPC-A checksum scheme,
• w = 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1; A= 10
• Checking: Verify that weighted mod-10 sum of all 12
digits is 0
• 12-digit UPC-A universal product code:
 Sum odd indexed digits: 0+6+0+2+1+5 = 14
 Multiply by 3: 14×3 = 42
 Add even-indexed digits: 42+3+0+0+9+4 = 58
 Compute check digit: 60 -58 = 2
![FTC05_Coding_Theory slide 91](images/FTC05_Coding_Theory_s091.png)

## Slide 92: Applications: JPEG Huffman Coding  *(visual)*
• Huffman codes are widely used and very effective technique
 for compression data; saving of 20% to 90%
• JPEG compression standard

 Original image Reconstructed image Reconstructed image
 under Huffman code table error wt error detection/correction
![FTC05_Coding_Theory slide 92](images/FTC05_Coding_Theory_s092.png)


---

# FTC06_Self_Checking

> Source: `2110473_2026S1_FTC06_Self_Checking-9294-17893470503977.pdf` — 78 slides. `visual: true` slides have a rendered image in `images/`.

## Slide 1: Schedule
• Mon 14 Sep, FTC06 Self Checking✓
• Mon 21 Sep, No Class
• Mon 28 Sep, FTC07 Fault Masking
• Mon 05 Oct, Review
• Mon 12 Oct, Midterm (Fault Tolerant Computing)
 - 13.30-16.30 -TBD-
 - Open any Books including notebooks!!
• Mon 19 Oct, TDC01 Overview of Testing Digital Circuits
• Mon 26 Oct, TDC02 Delay Fault Testing
• Mon 02 Nov, TDC03 Digital Circuit Testing Issues
• Mon 09 Nov, TDC04 Asynchronous Circuit Testing
• Mon 16 Nov, Review

## Slide 2: Fault Tolerant System Implementation
(Self Checking Circuits)

 2110473 Fault Tolerant Computing

 Eiji Fujiwara, Code Design for Dependable Systems, JOHN WILEY & SONS, 2006

## Slide 3: Contents
• Self Checking Concept
• Fault Secure and Self Testing
• Totally Self Checking and Strongly Fault Secure
• Error Secure and Error Preserving
• Strongly Code Disjoint
• Self Checking Logic Network
• Types of Checker
• Self Checking Checker
• Implementations of Checker
• Implementations of Functional Units

## Slide 4: Error Control  *(visual)*
• Fault Masking Scheme

 Error Control
 Codes
 Corrected
 Functional Unit Corrector Output

Error Control Overlapped
 Codes Parity
 Syndrome

 Checker Status
![FTC06_Self_Checking slide 4](images/FTC06_Self_Checking_s004.png)

## Slide 5: Self Checking Model  *(visual)*
• Concurrent Fault/Error Detection Scheme

 G Output Input Functional
 Unit L X Y
 W
 Checker
 CK

 Error Indicator Z
![FTC06_Self_Checking slide 5](images/FTC06_Self_Checking_s005.png)

## Slide 6: Self Checking Concept
• Self Checking is an approach for Concurrent error
 detection (CED) that allows:
 - detection of both temporary and permanent faults
 - early detection of errors so that corrective action can
 be initiated before data corruption
 - easy identification of the field replaceable unit (eg. a
 chip or a board)
• The use of a CED scheme in order to achieve the
 high reliability requirement of modern systems is
 becoming an important design technique

## Slide 7: Error Detecting Codes
• Design of Self Checking logic circuits is based
 on error detecting codes
• Error detecting codes - specific presentation of
 symbols which enables error detection inside
 codeword
• Most frequently used error detecting codes:
 - Separable:- Parity code, Berger Code
 - Non-Separable:-m-of-n Code, Dual Rail Code (Two
 Rail Code)

## Slide 8: Basic Idea of Self Checking
• Digital circuit has a self checking property if it is able to
 detect internal faults immediately after its occurrence,
 without using external test signals
• Information redundancy (Error Control Coding), which
 require an additional hardware, is introduced
 - The outputs of function units must satisfy specific features
• Function unit designed in a way that
 faults/errors/malfunctions manifest themselves as
 invalid (error-space) outputs, which are detectable by
 an external code checker

## Slide 9: Four possibilities of
Functional Unit & Checker

 Input
 Functional Unit Output

 Checker Indicator

1. Both functional unit and checker okay
2. Only functional unit okay
 - false alarm may be raised, but this is safe
3. Only checker okay
 - we have either no output error or a detectable error
4. Neither functional unit nor checker okay
 - use 2-output checker; a single check signal stuck-at-okay
 goes undetected, leading to fault accumulation

## Slide 10: Code Space and Error Space  *(visual)*
Encoded Functional Encoded
 input unit output

 Self-checking
Implementation of the desired
 code checker
functionality with coded values
 Status

 Codespace f1 Codespace
 f2

 f3
 f4
 Error ? Error
 space space

 Input Output
![FTC06_Self_Checking slide 10](images/FTC06_Self_Checking_s010.png)

## Slide 11: Cascade of Self Checking Modules  *(visual)*
Encoded
 Encoded Functional output Functional
 input unit 1 unit 2

 Self-checking Self-checking
 checker checker

 Codespace f Codespace
 f

 Error Error
 space space

 Input Output
![FTC06_Self_Checking slide 11](images/FTC06_Self_Checking_s011.png)

## Slide 12: Definition of Fault Secure and Self Testing
• A circuit 𝐿is Fault Secure (FS) for an input set
 𝑁and a fault set 𝐹, if for input 𝑋in 𝑁and for
 any fault 𝑓in 𝐹,
 𝑌𝑋, 𝑓= 𝑌𝑋, 𝜆 𝑜𝑟𝑌(𝑋, 𝑓) ∉𝑆
• A circuit L is Self Testing (ST) for an input set 𝑁
 and a fault set 𝐹, if for every fault 𝑓in 𝐹there
 is some input 𝑋in 𝑁such that 𝑌(𝑋, 𝑓) is not
 in 𝑆
 S: Output Codespace, : Null Fault

## Slide 13: Characteristics of SC circuits  *(visual)*
• Fault Secure (FS)
 - The property to ensure that for any possible fault,
 the circuit output is either a correct codeword or
 non-codeword

 codeword
 correct

 ffs(icw) ync
 icw ycc

 yic

 incorrect
 non-codeword 13
![FTC06_Self_Checking slide 13](images/FTC06_Self_Checking_s013.png)

## Slide 14: Characteristics of SC circuits  *(visual)*
• Self Testing (ST)
 - The property to ensure that for every possible
 fault, there is at least one input codeword for
 which the resulting output is a non-codeword
 codeword
 correct

 fst(icwt) ync
 icwt yi icwi
 fst(icwi)

 incorrect
 non-codeword 14
![FTC06_Self_Checking slide 14](images/FTC06_Self_Checking_s014.png)

## Slide 15: Self Testing & Fault Secure  *(visual)*
• Self Testing: ?
• Fault Secure: ?
• Undetectable Fault: ?

 

 
![FTC06_Self_Checking slide 15](images/FTC06_Self_Checking_s015.png)

## Slide 16: Self Testing & Fault Secure  *(visual)*
• Self Testing:
- Y(X1,f2), Y(X2,f1), Y(X2,f2)
• Fault Secure:
- Y(X1,f1), Y(X2,f1), Y(X1,f2), Y(X2,f2)
• Undetectable Fault:
- Y(X2,f3)

 

 
![FTC06_Self_Checking slide 16](images/FTC06_Self_Checking_s016.png)

## Slide 17: Self Testing & Fault Secure EXOR circuit  *(visual)*
• Fault Secure
 • Self Testing
 • Code Preserving
![FTC06_Self_Checking slide 17](images/FTC06_Self_Checking_s017.png)

## Slide 18: Totally Self Checking (TSC)
• A circuit is totally self checking if it is both Self
 Testing and Fault Secure
• An Ideal property but;
 - Not every fault can be detected by codeword
 - Undetectable faults in redundant circuits

• Even FS but undetectable fault is existing; the
 next coming faults may invalidate FS property

## Slide 19: Strongly Fault Secure (SFS)
• A circuit is Strongly Fault Secure if 1 or 2;
 1. TSC for fault {𝑓},
 2. Both FS for fault {𝑓} AND SFS for 𝐹−{𝑓}

• In case the fault 𝑓1 ∈{𝑓} is not be detected, still
 guarantee that the next fault 𝑓2 ∈𝐹−{𝑓} also
 satisfy 1 or 2
• The first output error is non-codeword

## Slide 20: Strongly Fault Secure  *(visual)*
for m faults
![FTC06_Self_Checking slide 20](images/FTC06_Self_Checking_s020.png)

## Slide 21: Example of SFS Circuit  *(visual)*
N: Input Codespace S: Output Codespace

 𝑥1 0 0 1 • For Input 𝑁= = , ,
 𝑥2 0 1 0
 • Fault Secure for the fault sequence 𝑓1, 𝑓2, 𝑓3
 𝑌𝑋, 𝑓1, 𝑓2, 𝑓3 = (𝑌𝑋, 𝜆 𝑓𝑜𝑟𝑎𝑙𝑙𝑋∈𝑁)
 0 0
 ∈ , • For Input 𝑋1 0 1
 • Strongly Fault Secure for 𝑓1, 𝑓2, 𝑓3, 𝑓4
 1
 𝑌𝑋1, 𝑓1, 𝑓2, 𝑓3, 𝑓4 = ∉𝑆
 21 0
![FTC06_Self_Checking slide 21](images/FTC06_Self_Checking_s021.png)

## Slide 22: Error Secure
• Considering the behavior of the circuits (self-
 checking checkers) for non-codeword inputs
• A Circuit 𝐿with output codespace 𝑆is Error
 Secure (ES) for noncodespace (input) 𝛺𝑋−𝑁
 if for any input 𝑋𝑞in 𝛺𝑋−𝑁, where 𝑋𝑞=
 𝑋𝑝+ 𝐸, 𝑋𝑝∈𝑁, 𝐸≠0

 𝑌𝑋𝑞, 𝜆∉𝑆𝑜𝑟𝑌𝑋𝑞, 𝜆= 𝑌(𝑋𝑝, 𝜆)

 N: Input Codespace, E: Input Error, S: Output Codespace, : Null Fault

## Slide 23: Error Secure Circuits  *(visual)*
• Error Secure (ES)
 - The property to ensure that for any non-codeword
 input, the circuit output will be either a correct
 codeword (Fault Masking) or non-codeword

 codeword
 correct

 fes(icw) ycw icw

 fes(inc) inc ync
 incorrect
 non-codeword 23
![FTC06_Self_Checking slide 23](images/FTC06_Self_Checking_s023.png)

## Slide 24: Error Preserving/Code Disjoint
• Synonymous with Code Disjoint (CD)
• A Circuit 𝐿with output codespaces 𝑆is Error
 Preserving for noncodespaces 𝛺𝑋−𝑁, if for
 any input 𝑋in 𝛺𝑋−𝑁

 𝑌𝑋, 𝜆∉𝑆

## Slide 25: Code Disjoint Circuits  *(visual)*
• Code Disjoint (CD)
 - The property of fault-free circuits to ensure that
 for any codeword/ non-codeword input, the
 output will be a correct codeword/ non-codeword

 codeword
 correct

 fcd(icw) ycw icw

 fcd(inc) inc ync
 incorrect
 non-codeword 25
![FTC06_Self_Checking slide 25](images/FTC06_Self_Checking_s025.png)

## Slide 26: Strongly Code Disjoint
• A circuit is Strongly Code Disjoint (SCD),
 if 1 or 2
 1. CD before the fault 𝑓occur; and ST for fault {𝑓}
 2. CD before the fault 𝑓occur; and SCD for 𝐹−{𝑓}
 when the fault 𝑓occur

## Slide 27: Strongly Code Disjoint  *(visual)*
for m faults
![FTC06_Self_Checking slide 27](images/FTC06_Self_Checking_s027.png)

## Slide 28: 1.  *(visual)*
codeword{ A, B), (C, D , X, Y } ∈{ 0,0), (0,1 , 1,0 }
1. วงจรนี้เป็น CD? ในกรณีFault-free
2. วงจรนี้เป็น FS? ST? สำหรับ {f1} ในกรณีเกิด Stuck-at-0 Fault
3. วงจรนี้เป็น FS? ST? สำหรับ {f2} ในกรณีเกิด Stuck-at-0 Fault
4. วงจรนี้เป็น FS? ST? สำหรับ {f3} ในกรณีเกิด Stuck-at-1 Fault
![FTC06_Self_Checking slide 28](images/FTC06_Self_Checking_s028.png)

## Slide 29: 1.  *(visual)*
codeword{ A, B), (C, D , X, Y } ∈{ 0,0), (0,1 , 1,0 }
1. วงจรนี้เป็น CD? ในกรณีFault-free
2. วงจรนี้เป็น FS? ST? สำหรับ {f1} ในกรณีเกิด Stuck-at-0 Fault
3. วงจรนี้เป็น FS? ST? สำหรับ {f2} ในกรณีเกิด Stuck-at-0 Fault
4. วงจรนี้เป็น FS? ST? สำหรับ {f3} ในกรณีเกิด Stuck-at-1 Fault
![FTC06_Self_Checking slide 29](images/FTC06_Self_Checking_s029.png)

## Slide 30: Self Checking Logic Network  *(visual)*
31
![FTC06_Self_Checking slide 30](images/FTC06_Self_Checking_s030.png)

## Slide 31: Theorem & Corollary
Theorem:
 "If the subnetwork 𝐿𝐼consisting of the output
interface circuit blocks is SFS and SCD for fault set FI, and
if the remaining subnetwork LII consisting of the internal
circuit blocks is SFS for fault set FII, then the total network
is SFS for all fault sequences in FI and FII"

Corollary:
 "If the subnetwork 𝐿𝐼consisting of the output
interface circuit blocks is SFS and CD, and if the remaining
subnetwork LII consisting of the internal circuit blocks is
SFS, then the total network is SFS for all fault sequences
in either LI or LII, but not in both"

 32

## Slide 32: Inverter-free Network
Theorem:
• "A network that consists of only Inverter-free
 combinational circuit blocks and in which the
 block input/output interfaces are encoded
 with unidirectional error detecting codes (eg.,
 the m-out-of n code and the Berger code) is
 SFS with respect to unidirectional faults"

 33

## Slide 33: Cascaded Inverter-free Network  *(visual)*
• SFS for the unidirectional fault sequence < 𝑓1, 𝑓2 >
 and for restricted inputs
• Each circuit block is not always CD
• Non-codewords can appear at embedded interfaces
 of the network before a non-codeword is produced
 as the first erroneous output
 34
![FTC06_Self_Checking slide 33](images/FTC06_Self_Checking_s033.png)

## Slide 34: Error Secure and Error Propagating
• A circuit block interface is Error Secure* (ES) at a
 given fault stage if any error that can occur at the
 interface never causes an incorrect codeword at any
 observable interface during the fault stage
• A circuit block interface is Error Propagating (EP) at a
 given fault stage if any error that can occur at the
 interface eventually produces a non-codeword at
 some observable interface during the fault stage

• Former ES: Block interfaces that may include some faults within them
• Latter ES*: Fault-free circuit blocks

 35

## Slide 35: Checkers  *(visual)*
Self Checking Model

 G Output Input Functional
 Unit L X Y
 W
 Checker
 CK

 Error Indicator Z

 36
![FTC06_Self_Checking slide 35](images/FTC06_Self_Checking_s035.png)

## Slide 36: Types of Checker  *(visual)*
• Code Checker/ Output encoded Checker

• Prediction Checker/ Output Non-encoded Checker
 • Duplication checker, Parity prediction checker, Input
 regeneration checker

 37
![FTC06_Self_Checking slide 36](images/FTC06_Self_Checking_s036.png)

## Slide 37: Duplication Checkers  *(visual)*
• The functional circuit L is duplicated, and the
 outputs are compared

 38
![FTC06_Self_Checking slide 37](images/FTC06_Self_Checking_s037.png)

## Slide 38: Parity Prediction Checkers  *(visual)*
• Output parity prediction P from input X
• Output parity generator from output Y
• Compare both output

 39
![FTC06_Self_Checking slide 38](images/FTC06_Self_Checking_s038.png)

## Slide 39: Input Regeneration Checkers  *(visual)*
• Regenerate inputs from outputs by inverse
 logic
• Then compare wt the original inputs

 40
![FTC06_Self_Checking slide 39](images/FTC06_Self_Checking_s039.png)

## Slide 40: Simplified Regeneration Checkers  *(visual)*
• Select only 1 input to check

 𝑥1 = 𝑦0⨁𝑦1 ∙𝑦2

 41
![FTC06_Self_Checking slide 40](images/FTC06_Self_Checking_s040.png)

## Slide 41: Self Checking Checker
Lemmas:
1. For single faults it is necessary that any
 checker must have at least two outputs and
 that no outputs take constant values
2. The Fault Secure property is not necessary
 for a checker

 42

## Slide 42: Self Checking Checker Properties
• 2 output lines
• Code-Disjoint (CD)
 - Codeword inputs generate only codeword outputs
 - Non-codeword inputs generate only non-codeword
 outputs
• Self Testing

• Strongly Code-Disjoint (SCD) if 1 or 2
 1. CD before the fault 𝑓occur; and ST for fault {𝑓}
 2. CD before the fault 𝑓occur; and SCD for 𝐹−{𝑓}
 when the fault 𝑓occur

 43

## Slide 43: Input and Output Space of Checkers  *(visual)*
• Code Checker

• Prediction Checker

 44
![FTC06_Self_Checking slide 43](images/FTC06_Self_Checking_s043.png)

## Slide 44: What's wrong?  *(visual)*
Conventional code checker
Input Code Example: 5-input odd-parity checker
 space f Output

 0

 1

 e
 Error f
 space

 45
![FTC06_Self_Checking slide 44](images/FTC06_Self_Checking_s044.png)

## Slide 45: Non-Self Testing Parity Code Checker  *(visual)*
Conventional code checker
Input Code Example: 5-input odd-parity checker
 space f Output
 s-a-0 fault
 0 on output?

 1

 e
 Error f
 space

 • Single output line
 • Code-Disjoint
 • non-Self Testing

 46
![FTC06_Self_Checking slide 45](images/FTC06_Self_Checking_s045.png)

## Slide 46: Totally Self Checking Error Signal  *(visual)*
Combining
 Encoded
 outputEncoded Function Function In Out
 input unit 1 unit 2 0 0 0 0 0 0
 0 0 0 1 0 0
 Self-checking Self-checking 0 0 1 0 0 0Simplified truth table checker checker
 0 0 1 1 0 0if we denote
 0 1 0 0 0 001 and 10 as G, 0 1 0 1 0 1
00 and 11 as B 0 1 1 0 1 0
 0 1 1 1 1 1
 In Out 1 0 0 0 0 0
 1 0 0 1 1 0B B B
 1 0 1 0 0 1B G B
 1 0 1 1 1 1G B B Circuit to combine 1 1 0 0 0 0
G G G error signals 1 1 0 1 1 1
 (two-rail code checker) 1 1 1 0 1 1
 1 1 1 1 1 1
Show that this circuit is self-testing
 47
![FTC06_Self_Checking slide 46](images/FTC06_Self_Checking_s046.png)

## Slide 47: Implementations of Checker
• Parity Code Checker
• Two Rail Code Checker
• 1-of-n Code Checker
• m-of-2m Code Checker
• TSC Checker for k-out-of-n Code
• TSC Checker for Separable Codes
• Generalized Prediction Checker (GPC)

 48

## Slide 48: Parity Code Checker
• Using Exclusive-OR gates in a Tree Structure
• Dividing inputs into Two Parity-Tree
Theorem:
• The parity-tree circuit that is divided into two
 independent parity-tree subcircuits is a self-
 testing checker for all odd-parity encoded
 inputs and for all single faults

 49

## Slide 49: Self Testing Parity Code Checker  *(visual)*
• 2 output lines
• (C1,C0) = {(0,1),(1,0)} = codeword
• (C1,C0) = {(0,0),(1,1)} = non-codeword
Ex. 8 bit data bit + 1 bit odd-parity bit

 x8
 x6 C0
 x4 • 2 output lines
 x2
 • Code-Disjoint x0
 x7 • Self Testing C1 x5
 x3 (number of 1s is even)
 x1
 Self Testing Checker
 50
![FTC06_Self_Checking slide 49](images/FTC06_Self_Checking_s049.png)

## Slide 50: Two Rail Code Checker  *(visual)*
• Duplication/ Comparison Check

 51
![FTC06_Self_Checking slide 50](images/FTC06_Self_Checking_s050.png)

## Slide 51: Example of Two Rail Code Checker  *(visual)*
• 2 output lines
• (C1,C0) = {(0,1),(1,0)} = codeword
• (C1,C0) = {(0,0),(1,1)} = non-codeword
Ex. 2-Pair Two Rail Code Checker: Input = {x1x0, y1y0}
x1

 C0x0 • 2 output lines
 • Code-Disjoint
 • Self Testingy1
 C1 {0101,0110,1001,1010}
y0

 Self Testing Checker 52
![FTC06_Self_Checking slide 51](images/FTC06_Self_Checking_s051.png)

## Slide 52: n-Pair Two Rail Code Checker
• n=6 using Tree-Structure 2-Pair Two Rail Code Checker

 2PTRC

 53

## Slide 53: Two Rail Code Sequence  *(visual)*
Timing/
Sequence 1 2 3 4
 x1
 C1 R 01 01 10 10 x0 2PTRC y1 C0
 S 01 10 01 10 y0
 T 01 10 10 01 Self Testing for all Stuck-at Faults

 IO/
 Timing x1 x0 y1 y0 C1 C0
 1 0 1 0 1 0 1
 2 0 1 1 0 1 0
 3 1 0 0 1 1 0
 4 1 0 1 0 0 1
 R S T
 54
![FTC06_Self_Checking slide 53](images/FTC06_Self_Checking_s053.png)

## Slide 54: Self Testing for 6-Pair Two Rail Code  *(visual)*
Checker

R Using RST sequence combination
 T regardless n data bit sizeS

 RS 0011
 1100 0110
 1001 T 0101
 1010
R S

S T
R

 55
![FTC06_Self_Checking slide 54](images/FTC06_Self_Checking_s054.png)

## Slide 55: 1-of-n Code Checker  *(visual)*
• Decode 𝑛to 𝑘(𝑘= 𝑛) and connect to Tree- log2
 Structure k-Pair Two Rail Code Checkers

 a1
 b1 1
 a2 2 b2 Two Rail C1
 Decoder Code
 C0
 Checker
 ak
 n bk

 Ex. n=8, k=3; Decoder function:
 a1 = (1 v 2 v 3 v 4), b1=(5 v 6 v 7 v 8)
 a2 = (1 v 2 v 5 v 6), b2=(3 v 4 v 7 v 8)
 a3 = (1 v 3 v 5 v 7), b3=(2 v 4 v 6 v 8)
 56
![FTC06_Self_Checking slide 55](images/FTC06_Self_Checking_s055.png)

## Slide 56: Self Testing 1-of-n Code Checker (n≠2  *(visual)*
k)

 • Connect pair (1,k) to Two Rail Code Checker (C1) and
 other pairs to k-2 Pair Two Rail Code Checker (C2)
 • All Checkers have {00,01,10,11} inputs Self Testing

 ai/Lip a1 a2 … ak-1 ak
 a1 C1 C11 1 0 0 … 0 1 b1
2 a2 C3 C0 2 0 0 … 1 0
 b2 3 0 0 … 1 1
 Decoder 2k-1 1 0 … 0 0 C2
 ak-1
 bk-1 2k-1+1 1 0 … 0 1
n ak … … … … … …
 bk

 57
![FTC06_Self_Checking slide 56](images/FTC06_Self_Checking_s056.png)

## Slide 57: m-of-2m Code Checker  *(visual)*
Divide the 2m bits into two disjoint subsets A and B of m bits each
Let v and w be the weight of (number of 1s in) A and B, respectively
Implement the two code checker outputs e0 and e1 as follows:

 m
 i)(w m - i) C0 = (v
 i = 0 v 1s w 1s
 (i even)

 m bits m bits m
 j)(w m - j) Subset A Subset B C1 = (v
 j = 1
 (j odd)
 v 1s w 1s

 Ex. 3-out-of-6 code checker, m = 3, A = {a, b, c}, B = {f, g, h}
 C0 = (v 0)(w 3) (v 2)(w 1) = fgh (ab bc ca)(f g h)
 C1 = (v 1)(w 2) (v 3)(w 0) = (a b c)(fg gh hf) abc
 Always satisfied

 58
![FTC06_Self_Checking slide 57](images/FTC06_Self_Checking_s057.png)

## Slide 58: Another TSC  *(visual)*
m-out-of-2m Code Checker

Cellular realization, due to J. E. Smith:
This design is testable with only 2m inputs,
all having m consecutive 1s (in cyclic order)

 m - 1 stages

 . . . .
 . . . .
 . . . .

 59
![FTC06_Self_Checking slide 58](images/FTC06_Self_Checking_s058.png)

## Slide 59: Using 2-out-of-4 Checkers as Building Blocks  *(visual)*
Building m-out-of-2m TSC checkers, 3 m 6, from 2-out-of-4 checkers
(construction due to Lala, Busaba, and Zhao):

Ex. 3-out-of-6 and 4-out-of-8 TSC checkers are depicted below
(only the structure is shown; some design details are missing)

 1 2 3 4 5 6 1 2 3 4 5 6 1 2 3 4 5 6 7 8 3 4 7 8 1 2 5 6

 2-out-of-4 2-out-of-4 2-out-of-4 2-out-of-4 2-out-of-4 2-out-of-4

 2-out-of-4 2-out-of-4 2-out-of-4 2-out-of-4

 Slightly different
 from an ordinary
 2-out-of-4 checker
 2-rail checker 2-rail checker
 3-out-of-6 4-out-of-8

 60
![FTC06_Self_Checking slide 59](images/FTC06_Self_Checking_s059.png)

## Slide 60: TSC Checker for  *(visual)*
k-out-of-n Code

 2-out-of-5
One design strategy is to proceed in 3 stages: 5 bits
 n
 10 AND gatesConvert the k-out-of-n code to a 1-out-of-( ) code 1-out-of-10 k
Convert the latter code to an m-out-of-2m code 10 bits

 6 OR gatesCheck the m-out-of-2m code using a TSC checker 3-out-of-6
 6 bitsThis approach is impractical for many codes
 TSC checker

A procedure due to Marouf and Friedman: m
 j)(w m - j)Implement 6 functions of the general form e0 = (v
 j = 1
 (these have different subsets of bits as (j even)
 inputs and constitute a 1-out-of-6 code)
 e0 e1 e2 e3 e4 e5
Use a TSC 1-out-of-6 to 2-out-of-4 converter
 1-out-of-6
Use a TSC 2-out-of-4 code checker 6 bits

 OR gates 2-out-of-4The process above works for 2k + 2 n 4k
It can be somewhat simplified for n = 2k + 1 4 bits
 TSC checker

 61
![FTC06_Self_Checking slide 60](images/FTC06_Self_Checking_s060.png)

## Slide 61: TSC Checker for Separable Codes  *(visual)*
Here is a general strategy for designing totally-self-checking checkers
for separable codes

 Complement n - k
 k data bits of check bits
 Two-rail generator C0
 checker C1 n - k n - k
 check bits
 Input Checker
 TSC code checker word outputs

• For many codes, direct synthesis will produce a faster and/or
 more compact totally-self-checking checker
• Require full combination of Two-rail Checker Inputs ST
• No need to consider about ST in Complement of Check Bits
 62
 Generator
![FTC06_Self_Checking slide 61](images/FTC06_Self_Checking_s061.png)

## Slide 62: Berger Code Checker  *(visual)*
n - k
 k data bits Number of 1s
 in Binary Two-rail C0
 checker C1 n - k n - k
 check bits
 Input Checker
 TSC code checker word outputs

Ex. Complement of Check bit Generator of (15,4) Berger Code

 1bit FA 1bit FA 1bit FA 1bit FA

 2bit FA 2bit FA

 3bit FA 63
![FTC06_Self_Checking slide 62](images/FTC06_Self_Checking_s062.png)

## Slide 63: Generalized Prediction Checker (GPC)  *(visual)*
• Self-testing checker of the combinational circuits
 having non-encoded inputs and outputs

 64
![FTC06_Self_Checking slide 63](images/FTC06_Self_Checking_s063.png)

## Slide 64: TSC Functional Unit
• TSC MUX
 - Non-inverter parity code data MUX is TSC for
 unidirectional faults
• Dual-Rail Logic
 - Dual-Rail Logic converted from Non-Redundant
 Single Rail Logic is TSC for unidirectional faults

 TSC Function Unit is Costly!!

 65

## Slide 65: Dual Rail Logic  *(visual)*
x z
• 1-of-2 Code X Z x' z'
 {0,1} {01,10} x z X Z
• Easy Implementation x' z'
 (Encoder/Decoder) x
 z
• Preserve code after X Z y
 operation Y x' z'
 y'• Non-Inverter Circuit
 x
 z X
 Z y
 x'
 Y
 z'
 y'

 66
![FTC06_Self_Checking slide 65](images/FTC06_Self_Checking_s065.png)

## Slide 66: Check Yourself: TSC Functional Unit  *(visual)*
• Dual-Logic implementation
 for
 𝐹= ത𝑎𝑏+ 𝑏ҧ𝑐+ 𝑎𝑐
• Assume one stuck-at-fault,
 - Find the property of each input
 - Conclude the property of circuit

 67
![FTC06_Self_Checking slide 66](images/FTC06_Self_Checking_s066.png)

## Slide 67: Check Yourself: TSC Functional Unit  *(visual)*
• 𝐹= ത𝑎𝑏+ 𝑏ҧ𝑐+ 𝑎𝑐; ത𝐹= (𝑎+ ത𝑏)(ത𝑏+ 𝑐)(ത𝑎+ ҧ𝑐)

 The property of circuit = FS + ST = TSC

 68
![FTC06_Self_Checking slide 67](images/FTC06_Self_Checking_s067.png)

## Slide 68: Contraction Circuits  *(visual)*
Definition: Contraction Circuit G'
• Circuit G' that remove signal lines and gate outputs
 which are fixed by a given fault f in the original circuit G

 S-a-0

 69
![FTC06_Self_Checking slide 68](images/FTC06_Self_Checking_s068.png)

## Slide 69: SFS to TSC
Theorem
• Circuit G is SFS for faults F. If no any codeword can
 detect the fault f, and G' is a contraction circuit of G
 for the fault f, and F' is an f contraction set of F, then;
 - G' is SFS for F', and
 - When no fault, Both G and G' generate the same
 outputs against all codeword inputs

 Consider Function Unit as SFS!!

 70

## Slide 70: SFS Functional Unit
• Function unit is SFS when;
 -Non-redundant and
 -Non-inverter circuit and
 -Output Coding wt Unordered Codes

 71

## Slide 71: TSC Design with Parity Prediction  *(visual)*
Parity prediction as an alternative to duplication

 Parity
 /
 generator k
Parity- Parity-
encoded Parity encoded ALU /
inputs predictor k output

 / Ordinary ALU
 k Error
 signal

 If the parity predictor produces the complement of the output parity, and
 the XOR gate is removed, we have a self-checking design

 To ensure the TSC property, we must also verify that the parity predictor
 is testable only with input codewords

 72
![FTC06_Self_Checking slide 71](images/FTC06_Self_Checking_s071.png)

## Slide 72: TSC Design with Residue Encoding  *(visual)*
Residue checking is applicable directly to addition, subtraction, and
multiplication, and with some extra effort to other arithmetic operations

 x, x mod A y, y mod A To make this scheme TSC:

 Modify the "Find mod A" box
 to produce the complement
 of the residue
 Add Add mod A
 Use two-rail checker instead of
 comparator

 Find Compare Verify the self-testing property
 mod A if the residue channel is not
 Not completely independent of the
 equal
 main computation (not needed
 s, s mod A Error for add/subtract and multiply)

 73
![FTC06_Self_Checking slide 72](images/FTC06_Self_Checking_s072.png)

## Slide 73: Self-Checking Design with FPGAs
LUT-based FPGAs can suffer from the following fault types:
 Single s-a faults in RAM cells
 Single s-a faults on signal lines
 Functional faults in a multiplexer within a single CLB LUT
 Functional faults in a D flip-flop within a single CLB
 Single s-a faults in pass transistors connecting CLBs

Synthesis algorithm:
(1) Use scripts in the Berkeley synthesis tool SIS to decompose an SOP
expression into an optimal collection of parts with 4 or fewer variables
(2) Assign each part to a functional cell that produces a 2-rail output
(3) Connect the outputs of a pair of intermediate functional cells to the
inputs of a checker cell and find the output equations for that cell
(4) Cascade the checker cells to form a checker tree

Ref.: P.K. Lala, and A.L. Burress, IEEE Trans. Instrumentation and Measurement,
Vol. 52, No. 5, pp. 1391-1398, October 2003

 74

## Slide 74: Synthesis of TSC Systems from TSC Modules
System consists of a set of modules, with interconnections modeled
by a directed graph

Theorem 1: A sufficient condition for a system to be TSC with respect
to all single-module failures is to add checkers to the system such that
if a path leads from a module Mi to itself (a loop), then it encounters at
least one checker

Theorem 2: A sufficient condition for a system to be TSC with respect
to all multiple module failures in the module set A = {Mi} is to have no
loop containing two modules in A in its path and at least one checker
in any path leading from one module in A to any other module in A

Optimal placement of checkers to satisfy these condition

Easily solved, when checker cost is the same at every interface

 75

## Slide 75: Partially Self-Checking Units  *(visual)*
Some ALU functions, such as logical operations, cannot be checked
using low-redundancy codes

Such an ALU can be made partially self-checking by circumventing
the error-checking process in cases where codes are not applicable

 01, 10 = G (top) Self-checking ALU
 Residue-check 01=D,10=C(bottom) with residue code error signal ALU error
 indicator 00, 11 = B

 0 1
 1 0 In Out
 Do not check Check X B B
 B C BThe check/do-not-check indicator
 B D Gis produced by the control unit
 Normal G C G 01
 operation G D G 10

 76
![FTC06_Self_Checking slide 75](images/FTC06_Self_Checking_s075.png)

## Slide 76: Self-Checking State Machines  *(visual)*
Design method for Moore-type machines, due to Diaz and Azema:

Inputs and outputs are encoded using two-rail code
States are encoded as n/2-out-of-n codewords

Fact: If the states are encoded using a k-out-of-n code, one can
express the next-state functions (one for each bit of the next state)
via monotonic expressions; i.e., without complemented variables

Monotonic functions can be realized with only AND and OR gates,
hence the unidirectional error detection capability

 Input Output Input Output
State x = 0 x = 1 z State x = 01 x = 10 z

 A C A 1 0011 1010 0011 10
 B D C 1 0101 1001 1010 10
 C B D 0 1010 0101 1001 01
 D C A 0 1001 1010 0011 01
 77
![FTC06_Self_Checking slide 76](images/FTC06_Self_Checking_s076.png)

## Slide 77: Further Studies
• Self-Checking Processor
• Fault Masking Scheme
• System Reconfiguration/Recovery
• Fault Tolerance in Distributed System
• Software Fault Tolerance
• Testing Digital Circuits

 78

## Slide 78: HW06: Self Checking Circuits
• Design a Self-Checking 2:4 Demultiplexer with Enable

 79


---

# FTC07_Fault_Masking

> Source: `2110473_2026S1_FTC07_Fault_Masking-9294-17911614782797.pdf` — 71 slides. `visual: true` slides have a rendered image in `images/`.

## Slide 1: Home Exercise: Self Checking Circuits  *(visual)*
• Design a Self-Checking 2:4 Demultiplexer with Enable

 ҧ𝐴 𝐴
 ത𝐵 𝐵
 𝐴 ҧ𝐴

 𝐵 ത𝐵

 𝐸𝑁 𝐸𝑁

 A EN AB'
 B A'B' A'B

 AB
![FTC07_Fault_Masking slide 1](images/FTC07_Fault_Masking_s001.png)

## Slide 2: Fault Masking
2110473 Fault Tolerant Computing

Prof.Behrooz Parhami, Graduate course materials, University of California, Santa Barbara
Daniel J.Sorin, M&C Publishers, Fault Tolerant Computer Architecture, Duke University, 2009
and others

## Slide 3: Schedule
• Mon 15 Sep, Self Checking✓
• Mon 22 Sep, No Class (Midterm)
• Mon 29 Sep, Fault Masking✓
• Mon 06 Oct, Midterm (Fault Tolerant Computing)
 - 13.00-16.00++/ #Eng4 no.18-15 (ON-SITE)
 - Open any Books including notebooks!!
• Mon 13 Oct, No Class (Comp.Holiday)
• Mon 20 Oct, Testing Digital Circuits (Online)

## Slide 4: Contents
• Handling Faults
• Interwoven Redundant Logic
• Combinatorial Modeling
• TMR & its application
• Replication & Voting
• Alternating Logic
• Fail-safe Systems

## Slide 5: Handling Faults  *(visual)*
Fault

 Avoid Tolerate

 Quality Assurance Testing Dynamic Redundancy Static Redundancy

Prevent Remove Expose Mask

 Detect Miss Miss Detect
 Test Monitor

 Repair Discard Abort

 Yes No No Yes
 Full? Full?

 Perfect Fixed Injured Screened Faulty Faulty-safe Degraded Restored Unaffected
 5
 C o m p o n e n t o r S y s t e m S t a t e
![FTC07_Fault_Masking slide 5](images/FTC07_Fault_Masking_s005.png)

## Slide 6: Design Techniques  *(visual)*
Specification
 mistakes
 Software
 Faults

Implementation
 mistakes

 System
 Errors
 failures
 External
 disturbances
 Hardware
 Faults

 Component
 defects

 Fault Avoidance Fault Masking Fault Tolerance
![FTC07_Fault_Masking slide 6](images/FTC07_Fault_Masking_s006.png)

## Slide 7: Some Options for Fault Tolerance  *(visual)*
Detector
1. Detect and replace 1 D
 Dynamic redundancy (cold/hot standby)
 Detection via
 -- coding, watchdog timer, self-checking 2
 -- duplication (pair-and-spares) Spare

2. Mask 1
 Voter
 Static redundancy
 2 V May revert to simplex instead of duplex
 Design challenges include 3 -- synchronization for voting
 -- voting on imprecise results
 1
3. Mask, diagnose, and reconfigure
 Hybrid redundancy 2
 Fault masked at output, but diagnosed S V
 -- e.g., via comparison with voter output 3
 Faulty circuit is replaced by spare
 Switch-voter 4 Becomes static upon spare exhaustion Spare
![FTC07_Fault_Masking slide 7](images/FTC07_Fault_Masking_s007.png)

## Slide 8: Comparing Fault Tolerance Schemes  *(visual)*
Advantages Drawbacks
 Detector
 1 DLess power Coverage factor
 (cold standby)
Long life Tolerance latency
 2 (just add spares) Spare

 1
 VoterImmediate masking Power/area penalty
 2 V
High safety Voter critical
 3

Immediate masking Power/area penalty 1

 2Long life and Switch-voter critical
 S V high safety 3

 Switch-voter 4
 Spare
![FTC07_Fault_Masking slide 8](images/FTC07_Fault_Masking_s008.png)

## Slide 9: Contents
• Handling Faults
• Interwoven Redundant Logic
• Combinatorial Modeling
• TMR & its application
• Replication & Voting
• Alternating Logic
• Fail-safe Systems

## Slide 10: Inherent Fault Masking in Logic Circuits  *(visual)*
1a e 0 →1 fault in b is critical
b 0 0 g
 0 c 0 z 0 0 →1 fault in c or d is 0
d f h 1 not critical (it is masked) 0

 1 →0 fault in a or h is
 not critical (it is masked)

 Even nonredundant circuits have some masking capability

 Is there a way to exploit the inherent masking capabilities
 of logic gates to achieve fault tolerance?
![FTC07_Fault_Masking slide 10](images/FTC07_Fault_Masking_s010.png)

## Slide 11: AND-OR Logic Mask  *(visual)*
x4
 1 y4
 1
 x3
 1 y3
 1
 x2
 1 y2
 1

 x1
 0 y1
 1

• Single error can be masked
• NAND-NAND Logic
![FTC07_Fault_Masking slide 11](images/FTC07_Fault_Masking_s011.png)

## Slide 12: Interwoven Redundant Logic  *(visual)*
a e
 Let x1, x2, x3, and x4 beb g
 4 copies of the signal xc z
d f h
 1 →0 change is critical for AND,
 a1 e1 subcritical for OR a2
 b1
 b2
 0 →1 change is critical for OR, a1 e2 a2 b1 subcritical for AND
 b2
 a3 e3 Alternating layers of ANDs and ORs a4
 b3
 b4 can mask each other's critical faults
 a3 e1 e4 a4 e4
 b3 f1 To mask h critical faults:
 b4 f4
 Number of gates multiplied by (h + 1)2
 f1
 Gate inputs multiplied by h + 1
 f2
 f3 For h = 1, the scheme is known as
 f4 Quadded logic
![FTC07_Fault_Masking slide 12](images/FTC07_Fault_Masking_s012.png)

## Slide 13: Interwoven Logic for Half Adder  *(visual)*
Half-adder implemented in quadded logic

 a
 s
 b

 c

 a
 s
 b

 c

 IEEE D&T
 July-Aug. 2005
 pp. 328-339

 From: http://ieeexplore.ieee.org/iel5/54/32070/01492293.pdf
![FTC07_Fault_Masking slide 13](images/FTC07_Fault_Masking_s013.png)

## Slide 14: Contents
• Handling Faults
• Interwoven Redundant Logic
• Combinatorial Modeling
• TMR & its application
• Replication & Voting
• Alternating Logic
• Fail-safe Systems

## Slide 15: Combinatorial Modeling
• System is divided into non-overlapping modules
• Each module is assigned either a probability of
 working, Pi, or a probability as function of time, Ri(t)
• The goal is to derive the probability, Psys, or function
 Rsys(t) of correct system operation
• Assumptions:
 - Module failures are independent
 - Once a module has failed, always be assumed to yield
 incorrect results
 - System is considered failed if don't satisfy minimal set of
 functioning modules

## Slide 16: Reliability of series systems
• Reliability Ri = Prob that component i works
• Reliability Rs = Prob that system s works
Assume that components fail independently
 Component i fails with probability pi
Ri = Prob that comp i works = 1 - pi
Rs = Prob that system works= R1R2R3…Rn = Ri

## Slide 17: Reliability of parallel systems  *(visual)*
• Assume that
 components fail
 independently
 • Probability that system
 works =
 Rp = 1 - Prob of all
 components failing
 = 1 - P1P2P3 … Pn
 = 1 - n(1 - Ri) 0
![FTC07_Fault_Masking slide 17](images/FTC07_Fault_Masking_s017.png)

## Slide 18: Series‐Parallel Effects  *(visual)*
18
![FTC07_Fault_Masking slide 18](images/FTC07_Fault_Masking_s018.png)

## Slide 19: ex. Calculate the reliability of  *(visual)*
the following system
![FTC07_Fault_Masking slide 19](images/FTC07_Fault_Masking_s019.png)

## Slide 20: Non-Series Parallel System  *(visual)*
• Neither a series nor parallel system
• How to evaluate the Reliability?

 E

 A B C D

 F
![FTC07_Fault_Masking slide 20](images/FTC07_Fault_Masking_s020.png)

## Slide 21: Non-Series Parallel System - 1  *(visual)*
• Pick a module 'm' in the system

 P(sys works) = P(sys works | m works) P(m works)
 + P(sys works | m fails) P(m fails)
 Rsys = P(sys works | m)Rm + P(sys works | m')(1 - Rm)

 E

 A B C D

 F
![FTC07_Fault_Masking slide 21](images/FTC07_Fault_Masking_s021.png)

## Slide 22: Non-Series Parallel System - 2  *(visual)*
• Pick 'm' to be module E. Consider 'E fails';
 P(sys works | E') = [1 - (1 - RARB)(1 - RF)]RCRD
 'module E fails' = 'path E opened'

 A B C D

 F
![FTC07_Fault_Masking slide 22](images/FTC07_Fault_Masking_s022.png)

## Slide 23: Non-Series Parallel System - 3  *(visual)*
• Next, consider 'E works' = 'path E shorted'
• Still unsolved, do again wt a different module

 A B C D

 F
![FTC07_Fault_Masking slide 23](images/FTC07_Fault_Masking_s023.png)

## Slide 24: Non-Series Parallel System - 4  *(visual)*
• Next, consider 'B fails' = 'path B opened'
 P(sys works|E and B') = [1-(1-RA)(1-RFRC)]RD

 A C D

 F
![FTC07_Fault_Masking slide 24](images/FTC07_Fault_Masking_s024.png)

## Slide 25: Non-Series Parallel System - 5  *(visual)*
• Next, when B works, still the same as before
 P(sys works|E and B) = [1-(1-RA)(1-RFRC)]RD

 'module B works' = 'path B shorted'

 A C D

 F
![FTC07_Fault_Masking slide 25](images/FTC07_Fault_Masking_s025.png)

## Slide 26: Putting it all together ‐ 1
P(sys works|E') = [1 - (1 - RARB)(1 - RF)]RCRD

P(sys works|E and B') = [1-(1-RA)(1-RFRC)]RD
P(sys works|E and B) = [1-(1-RA)(1-RFRC)]RD

P(sys works|E) = [1 - (1 - RA)(1 - RFRC)]RD[RB + RB']
 = [1 - (1 - RA)(1 - RFRC)]RD
P(sys works) =
 P(sys works|E)RE + P(sys works|E')(1- RE)

## Slide 27: Putting it all together ‐ 2
Rsys = P(sys works) =
 [1 - (1 - RARB)(1 - RF)]RCRD(1 - RE)
 + [1 - (1 - RA)(1 - RFRC)]RD RE
 = [RERD+RCRD-RERCRD][RA+RFRC-RARFRC]
Let RA = RB = RC = RD = RE = RF = R;
Then,
 Rsys = R6 - 3R5 + R4 +2R3

## Slide 28: Some tips for non-series‐parallel
• Simpler if picked module A

• Choosing the initial module is crucial
• Heuristics:
 - Pick modules that are on as many paths as
 possible
 - Think about whether a single module prevents the
 system from becoming a serial/parallel system

## Slide 29: Non-Series Parallel System (again)  *(visual)*
E

 A B C D

 F

 Choose A as the keystone component

 Rsys = P(sys works|A)RA + P(sys works|A')(1-RA)

 R:Reliabilty; P:Possibility
![FTC07_Fault_Masking slide 29](images/FTC07_Fault_Masking_s029.png)

## Slide 30: Non-Series Parallel System (again-1)  *(visual)*
E

 B C D

 F

 If A works: →serial/parallel system

 P(sys works|A) = (1 - (1 - RE)(1 - (1 - (1 - RB)(1 - RF)) RC)) RD
![FTC07_Fault_Masking slide 30](images/FTC07_Fault_Masking_s030.png)

## Slide 31: Non-Series Parallel System (again-2)  *(visual)*
E

 B C D

 F

 If A fails: →serial/parallel system

 P(sys works|A') = RF RC RD
![FTC07_Fault_Masking slide 31](images/FTC07_Fault_Masking_s031.png)

## Slide 32: Put it all again
Rsys = P(sys works| A) RA + P(sys works | A') (1-RA)
 = (1 - (1 - RE)(1 - (1 - (1 - RB)(1 - RF)) RC)) RD RA
 + RC RD RF (1 - RA)
 = RA RB RC RD + RA RB RC RF - RA RB RC RD RF + RA RD RE
 - RA RB RC RD RE - RA RC RD RE RF + RA RB RC RD RE RF
 + RC RD RF - RA RC RD RF

 Let RA = RB = RC = RD = RE = RF = R, then
Rsys = R6 - 3R5 + R4 +2R3

## Slide 33: In-class Exercise: Non SP system  *(visual)*
33
![FTC07_Fault_Masking slide 33](images/FTC07_Fault_Masking_s033.png)

## Slide 34: Inclass Exercise: Non SP system  *(visual)*
34
![FTC07_Fault_Masking slide 34](images/FTC07_Fault_Masking_s034.png)

## Slide 35: Contents
• Handling Faults
• Interwoven Redundant Logic
• Combinatorial Modeling
• TMR & its application
• Replication & Voting
• Alternating Logic
• Fail-safe Systems

## Slide 36: TMR with Perfect Voter  *(visual)*
?
R = 3Rm2 - 2Rm3 > Rm 1
 Voter
Condition on the module reliability: 2 V
R = Rm [1 + (1 - Rm)(2Rm - 1)] 3
(1 - Rm)(2Rm - 1) > 0 Rm > 1/2
 R R
 1.0 1.0
 TMR better TMR

 0.5 0.5
 Simplex better Simplex

 0.0 Rm 0.0 t
 0.0 0.5 1.0 0 ln 2
 MTTF:TMR 5/(6)RIFTMR/Simplex = (1 - Rm)/(1 - R)
 = 1/[1 - Rm(2Rm - 1)] Simplex 1/
![FTC07_Fault_Masking slide 36](images/FTC07_Fault_Masking_s036.png)

## Slide 37: TMR with Imperfect Voter  *(visual)*
?
R = Rv(3Rm2 - 2Rm3) > Rm 1
 Voter
Condition on the voter reliability 2 V
Rv > 1/ [3Rm - 2Rm2] 3
dRvmin/dRm = (-3+4Rm)/(3Rm-2Rm2)2
 Rv
Condition on the module reliability
 0.95
3 - 9 - 8/Rv 3 + 9 - 8/Rv TMR better < Rm < 4 4
 0.885
Example: Rv = 0.95 requires that Simplex better
0.56 < < 0.94 Rm Rm 0.5 0.75 1.0
 0.56 0.94

 Slide 37
![FTC07_Fault_Masking slide 37](images/FTC07_Fault_Masking_s037.png)

## Slide 38: TMR with Compensating Faults  *(visual)*
Rm = 1 - p0 - p1 (0- and 1-fault probabilities) 1
 Voter
R = (3Rm2 - 2Rm3) + 6p0p1Rm 2 V

 3
Example: Rm = 0.998, p0 = p1 = 0.001
R = 0.999,984 + 0.000,006 = 0.999,990
 Basic TMR Compensation
RIFTMR/Simplex = 0.002 / 0.000,016 = 125
RIFCompen/TMR = 0.000,016 / 0.000,010 = 1.6
![FTC07_Fault_Masking slide 38](images/FTC07_Fault_Masking_s038.png)

## Slide 39: Contents
• Handling Faults
• Interwoven Redundant Logic
• Combinatorial Modeling
• TMR & its application
• Replication & Voting
• Alternating Logic
• Fail-safe Systems

## Slide 40: Implementing a Bit-Voter  *(visual)*
TMR bit-voting: y = x1x2 x2x3 x3x1 1 x1 (carry output of a single-bit full-adder) Bit-voter
 x2What about 5MR, 7MR? 2 V y
Gate-level design quickly explodes in size 3 x3

Other designs are also possible
 Arithmetic: add the bits, compare to threshold
 Mux-based
 Selection-based (majority of bit values is their median)

3-out-of-5 voter built of 2-input gates Two mux-based designs for a 3-out-of-5 bit-voter

 Slide 40
![FTC07_Fault_Masking slide 40](images/FTC07_Fault_Masking_s040.png)

## Slide 41: Complexity of Different Bit-Voter Designs  *(visual)*
Cost of majority bit-voters as a function of the number n of inputs
![FTC07_Fault_Masking slide 41](images/FTC07_Fault_Masking_s041.png)

## Slide 42: Voting at the Word Level
Using bit-by-bit voting may be dangerous x1 = 0 0
 x2 = 1 0
One might think that in this example, any of the x3 = 1 1
 y = 1 0module outputs could be correct, so that
producing 1 0 at the output isn't all that wrong
 x1 = 0 0 0
However, with bit-by-bit voting, the output may x2 = 1 0 1
be different from all inputs x3 = 1 1 0
 y = 1 0 0

Design of bit- and word-voting networks discussed in:
Parhami, B., "Voting Networks," IEEE TR, Aug. 1991

## Slide 43: Bit-Voting and Word-Voting (1)  *(visual)*
Scenario1: every module has an error bit at the output
 Expected output is (00000)

 maintaining data integrity 43
![FTC07_Fault_Masking slide 43](images/FTC07_Fault_Masking_s043.png)

## Slide 44: Bit-Voting and Word-Voting (2)  *(visual)*
Scenario2: some modules have multiple errors
 Expected output is (00000)

 maintaining data integrity 44
![FTC07_Fault_Masking slide 44](images/FTC07_Fault_Masking_s044.png)

## Slide 45: Some Simple Voter Designs  *(visual)*
DisagreeIf in the case of 3-way disagreement x1 Compare 1
any of the inputs can be chosen, x2 2 0then a simple design is possible y
 x3 3 1This design can be readily generalized
to a larger number of inputs

One can perform pseudo voting that yields the median of 3 analog
signals (Dennis, N.G., Microelectronics and Reliability, Aug. 1974)

Median and mean voting are also possible with digital signals

 Slide 45
![FTC07_Fault_Masking slide 45](images/FTC07_Fault_Masking_s045.png)

## Slide 46: -Modular Redundancy (NMR)  *(visual)*
N-Modular Redundancy (NMR)

Triple-modular redundancy (TMR) can be generalized to N units

N-modular redundancy (NMR) uses N modules along with a voter,
with N usually being odd
 1
Example: 5MR
 12Operates correctly as long as Voting unit
3 of the 5 modules are healthy 23 V
Voter complexity rises rapidly 34
with increasing N
 5

Even values of N are also feasible

Example: 4MR, with 3-out-of-4 voting
Voter masks single faults; can be designed to detect double faults
![FTC07_Fault_Masking slide 46](images/FTC07_Fault_Masking_s046.png)

## Slide 47: Switch for Standby Redundancy  *(visual)*
Standby redundancy requires an Detector
n-to-1 switch to select the output 1 D
of the currently active module

 2The detectors use various info Spare
to deduce fault conditions
-- Error coding 1 D
-- Reasonableness checks
-- Watchdog timer n-to-1 2 D switch
 Spares
Once a fault has been detected,
 3 Dthe switch reconfigures the system
by flagging the faulty unit and
activating next spare in sequence

If we use an n-to-2 switch and compare the two selected outputs,
the configuration is known as "pair-and-spares"
![FTC07_Fault_Masking slide 47](images/FTC07_Fault_Masking_s047.png)

## Slide 48: Switch for Hybrid Redundancy  *(visual)*
Hybrid redundancy with n active 1
and s spare modules requires an
 2(n + s)-to-n switch to select the S V
outputs of the active modules 3

 Switch-voter 4Self-purging redundancy is a variant Spare
of hybrid redundancy in which all
modules are active at the outset,
but they are purged as they
disagree with the majority output

Voter in self-purging redundancy ...
is a threshold voter that considers
the inputs with weights of 1 (active)
or 0 (purged)
![FTC07_Fault_Masking slide 48](images/FTC07_Fault_Masking_s048.png)

## Slide 49: Variations and Design Issues  *(visual)*
NMR/simplex: Voting unit is replaced with
 1
a unit that can also detects disagreements Voting unit
 2 V
When a faulty unit is detected, that unit and 3
one other unit are removed from service

This makes all votes unambiguous and also improves systems lifetime

Self-purging redundancy: Modules
purged when they disagree with the S R
 Q
output and the threshold of the voting
unit is adjusted accordingly T Module
(purged modules produce 0 outputs) output
![FTC07_Fault_Masking slide 49](images/FTC07_Fault_Masking_s049.png)

## Slide 50: Variations and Complications  *(visual)*
Static redundancy makes fault testing more challenging

 For static redundancy to be effective, we must ensure that initially all
 redundant components are fault-free

 1 Voting unit Voting unit

 0 2 V

 3 1

 2

 3

 Controllable, Mode
 but not
 observable

Oct. 2015 Part III - Faults: Logical Deviations Slide 50
![FTC07_Fault_Masking slide 50](images/FTC07_Fault_Masking_s050.png)

## Slide 51: Time Redundancy
Retry upon a detected fault: particularly useful for transient faults

 Recomputation not useful with permanent faults

 Can make recomputation work by slightly changing the operands,
 but this is not always applicable

 Compute a (2b) instead of (2a) b

 Compute b + a or -(-a - b) instead of a + b

Oct. 2015 Part III - Faults: Logical Deviations Slide 51

## Slide 52: Applications of  *(visual)*
nMR and Hybrid Redundancy

The Space Shuttle:

Uses 5-way redundancy in hardware
 Originally, 3 operational units + 2 spares
 (one warm, one cold)
 More recently, 4 operational + 1 spare

Also, uses 2 independently developed
 software systems (Design diversity)

 Japanese Shinkansen "Bullet" Train

 Triple-duplex system (6-fold redundancy)
![FTC07_Fault_Masking slide 52](images/FTC07_Fault_Masking_s052.png)

## Slide 53: Check yourself  *(visual)*
Q. List the conditions under which it will fail?
![FTC07_Fault_Masking slide 53](images/FTC07_Fault_Masking_s053.png)

## Slide 54: Hardware Redundancy Recap  *(visual)*
Data path methods: Control unit methods:
Replication in space (costly) Coding of control signals
 Duplicate and compare Control-flow watchdog
 Triplicate and vote Self-checking design
 Pair-and-spare
 NMR/hybrid
Replication in time (slow?) Glue logic methods:
 Recompute and compare Self-checking design
 Recompute and vote
 Alternating logic
 Recompute after shift
 Recompute after swap Control unit
 Replicate operand segments
Mixed space-time replication Control Condition
 Glue logicMonitoring (imperfect coverage) signals signals
 Watchdog timer
 Activity monitor … … …
Low-redundancy coding
 Inputs Outputs … Parity prediction ... … ... … Residue checking
 Data path Self-checking design
![FTC07_Fault_Masking slide 54](images/FTC07_Fault_Masking_s054.png)

## Slide 55: Replication in Space  *(visual)*
Switch
The following schemes have 1
already been discussed in
 Errorconnection with fault masking 2 C S
 Comparators
 1
 1
 2 C Error
 Error 2 C
 Pair-and-spare
 Comparator
 Duplicate and compare
 1

 2 1
 Voting unit S V
 3 2 V

 Switch-voting unit 4 3 Spare
 Triplicate and vote NMR/Hybrid
![FTC07_Fault_Masking slide 55](images/FTC07_Fault_Masking_s055.png)

## Slide 56: Replication in Time  *(visual)*
Can be slow, but in many control applications, extra time is available

Interleaving of the primary and
duplicate computations saves time +

 + Duplicate t0 + + Duplicate computation
 computation

  +  + +t0 + 1

 Schedule
 + with 1 addert0 + 2 

 Computation flowgraph, 
 and schedule with 2 adders
![FTC07_Fault_Masking slide 56](images/FTC07_Fault_Masking_s056.png)

## Slide 57: Recompute and Compare/Vote  *(visual)*
Repeat computation and store the results for comparison or voting

 Comparison or voting need not be done
 right away; primary result may be used
 in further computations, with the result
 + + Duplicate subsequently validated, if appropriate computation
 On a simultaneous
  + + Triplicate multithreading
 computation architecture, multiple
 instruction streams
  + + may be interspersed

 Some Cray machines
 take advantage of 
 Use as operand in extensive hardware
 further computations,
 resources to execute while awaiting
confirmation of validity instructions twice
![FTC07_Fault_Masking slide 57](images/FTC07_Fault_Masking_s057.png)

## Slide 58: Mixed Space/Time Replication  *(visual)*
Instead of duplicating the computation with no hardware change (slow)
or duplicating the entire hardware (costly), we can add some hardware
 to make the interleaved recomputations more efficient

 Recomputation with same Consider the effect
 + hardware resources (T = 5, of including a
 excluding compare time) second adder

 + Duplicate Recomputation
 computation with the inclusion
 of an extra adder
 (T = 3, excluding
  + + + compare time)

 Original +  + + computation
 (T = 3)

  
![FTC07_Fault_Masking slide 58](images/FTC07_Fault_Masking_s058.png)

## Slide 59: Error Detection by  *(visual)*
Duplicated Instructions (EDDI)
• The redundant code is compared before Store
![FTC07_Fault_Masking slide 59](images/FTC07_Fault_Masking_s059.png)

## Slide 60: Contents
• Handling Faults
• Interwoven Redundant Logic
• Combinatorial Modeling
• TMR & its application
• Replication & Voting
• Alternating Logic
• Fail-safe Systems

## Slide 61: Alternating Logic: Basic Ideas  *(visual)*
Transmission of data over unreliable wires or buses
 Send data; store at receiving end
 Send bitwise complement of data
 Compare the two versions
 Detects wires s-a-0 or s-a-1, as well as many transients

The dual of a Boolean function f(x1, x2, . . . , xn) is another function
fd(x1, x2, . . . , xn) such that fd(x1, x2, . . . , xn) = f(x1, x2, . . . , xn)
Fact: Obtain the dual of f by exchanging AND and OR operators in its
logical expression. For example, the dual of f = ab c is fd = (a b)c

 Advantages of this
 Inputs f Output approach compared
 Error with duplication include
 Compl. a smaller probability fd inputs of common errors
![FTC07_Fault_Masking slide 61](images/FTC07_Fault_Masking_s061.png)

## Slide 62: Alternating Logic: Self-Dual Functions  *(visual)*
A function f is self-dual if f(x1, x2, . . . , xn) = fd(x1, x2, . . . , xn)

 Use same circuit twiceFor example, both the
sum a b c and Inputs f Output
carry ab bc ca Error
outputs of a full-adder Compl. fd inputsare self-dual functions

With a self-dual function f, the functions f and fd in the diagram above
can be computed by using the same circuit twice (time redundancy)

Many functions of practical interest are self-dual

Examples (proofs left as exercise)
A k-bit binary adder, with 2k + 1 inputs and k + 1 outputs, is self-dual
So are 1's-complement and 2's-complement versions of such an adder
![FTC07_Fault_Masking slide 62](images/FTC07_Fault_Masking_s062.png)

## Slide 63: Recomputing with Transformed Operands  *(visual)*
Alternating logic is a special case of the following general scheme, with
its encoding and decoding functions being bitwise complementation

 Inputs f Output

 Encode Decode Error
 Inputs e g d
 XNOR if lower path finds
 complement of the result
Recompute after shift
When f is binary addition, we can use shifts for encoding and decoding
Shifting causes the adder circuits to be exercised differently each time
Originally proposed for ALUs with bit-slice organization

Recompute after swap
When f is binary addition, we can use swaps for encoding and decoding
 Swap the two operands; e.g., compute b + a instead of a + b
 Swap upper and lower halves of the two operands (modified adder)
![FTC07_Fault_Masking slide 63](images/FTC07_Fault_Masking_s063.png)

## Slide 64: Time-Redundant, Segmented Addition  *(visual)*
Instead of using a k-bit adder twice for error detection or 3 times for
 error correction, one can segment the operands into 2 or 3 parts and
 similarly segment the adder; perform replicated addition on operand
 segments and use comparison/voting to detect/correct error

 FF Sum computed in two cycles: cin
 cout The lower half in cycle 1, and
xL Lower half the upper half in cycle 2
xH of adder

 Upper half
yL C Error of adder
yH
 Comparator

 Various other segmentation
 schemes have been suggested
 Example: 16-bit adder with
 4-way segmentation and voting
 Townsend, Abraham, and Swartzlander, 2003
![FTC07_Fault_Masking slide 64](images/FTC07_Fault_Masking_s064.png)

## Slide 65: Contents
• Handling Faults
• Interwoven Redundant Logic
• Combinatorial Modeling
• TMR & its application
• Replication & Voting
• Alternating Logic
• Fail-safe Systems

## Slide 66: Fail-Safe Systems
Fail-safe: Produces one of a predetermined set of safe outputs when
it fails as a result of "undesirable events" that it cannot tolerate

Fail-safe traffic light: Will remain stuck on red

Fail-safe gas range/furnace pilot: Cooling off of the pilot assembly due
to the flame going out will shut off the gas intake valve

A fail-safe digital system must have at least two binary output lines,
together representing the normal outputs and the safe failure condition
Reason: If we have a single output line, then even if one value (say, 0)
is inherently safe, the output stuck at the other value would be unsafe
Two-rail encoding is a possible choice: 0: 01, 1: 10, F: 00, 11, or both

Totally fail-safe: Only safe erroneous outputs are produced, provided
another failure does not occur before detection of the current one
Ultimate fail-safe: Only safe erroneous output is produced, forever

## Slide 67: Fail-Safe System Specification  *(visual)*
Amusement park train safety system Output space
Signal sB when asserted indicates that Input space Correct
 outputthe train is at beginning of its track
(can move forward, but should not be
 Input
 Safe outputsallowed to go back)
Signal sE when asserted indicates that Unsafe
the train is at end of its track (can go outputs
back, but should not move forward)

Is the specification above consistent and complete?

No, because it does not say what happens if sB = sE = 1; this would not
occur under normal conditions, but because such sensors are often
designed to fail in the safe mode, the combination is not impossible

Why is this a problem, though? (Train simply cannot be moved at all)

Completeness will prevent potential implementation or safety problems
![FTC07_Fault_Masking slide 67](images/FTC07_Fault_Masking_s067.png)

## Slide 68: Fail-Safe 2-out-of-4 Code Checker  *(visual)*
Input: 4 bits abcd, exactly 2 of which must be 1s

Output: fg = 01 or 10, if the input is valid
 00 safe erroneous output
 11 unsafe erroneous output
 Preset
 a
 Codewords b
 c f a b c d
 0 0 1 1 d S Q
 0 1 0 1
 0 1 1 0 a R Q
 1 0 0 1 b g 1 0 1 0
 c 1 1 0 0
 d

Output will become permanently 00 upon the first unsafe condition
![FTC07_Fault_Masking slide 68](images/FTC07_Fault_Masking_s068.png)

## Slide 69: Fail-Safe State Machines  *(visual)*
Use an error code to encode states
Implement the next-state logic so that the machine is forced to an error
state when something goes wrong

Possible design methodology:
Use Berger code for states, avoiding the all 0s state with all-1s check,
and vice versa
Implement next-state logic equations in sum-of-products form for the
main state bits and in product-of-sums form for the check state bits
The resulting state machine will be fail-safe under unidirectional errors

 Input Hardware overhead for
State x=0 x=1 State Encoding n-state machine consists
 A E B A 001 10 of O(log log n) additional
 B C D B 010 10 state bits and associated
 C A D C 011 01 next-state logic, and a
 D E D D 100 10 Berger code checker
 E A D E 101 01 connected to state FFs
![FTC07_Fault_Masking slide 69](images/FTC07_Fault_Masking_s069.png)

## Slide 70: Home Exercise: Non-SP  *(visual)*
• A system operated from X to Y via non serial-parallel path
• Reliabilities of Module (A, B, K) = (Ra, Rb, Rk)
• Find the system reliability
![FTC07_Fault_Masking slide 70](images/FTC07_Fault_Masking_s070.png)

## Slide 71: Midterm Exam
• On-Site
• 12 Oct 2026, 13.00-16.00
• CP: #17-01, CEDT: #18-15 Eng.Bldg.no.4
• All about Fault Tolerant Computing
• Open Books, Open Net


---

# SYLLABUS_2110473

> Source: `SYLLABUS_2110473-9294-17856842207218.pdf` — 2 slides. `visual: true` slides have a rendered image in `images/`.

## Slide 1: COURSE SYLLABUS
วิชา 2110473 Fault Tolerant Computing
จํานวนหน่วยกิต (Course Credit) " หน่วยกิต
ชื:อผู้สอน ผศ.ดร.อาทิตย์ ทองทักษ์ (Rm.no.18-04)
 Arthit.t@chula.ac.th

วัตถุประสงค์ทั:วไป เพื:อให้ผู้เรียนได้
 1. เข้าใจทฤษฎี ความรู้พืYนฐานและมีโอกาสติดตามเทคโนโลยีที`เกี`ยวข้องกับ Fault Tolerant Computing
 2. เข้าใจถึงขัYนตอนวิธีการในการวิเคราะห์และการออกแบบระบบที`ดําเนินการแบบ Fault Tolerant
 Computing
 3. มีประสบการณ์ในการใช้เครื`องมือการออกแบบระบบที`ดําเนินการแบบ Fault Tolerant Computing

เนืPอหารายวิชา (อาจมีการเปลี:ยนแปลงได้ตามความเหมาะสม)
 1. Dependable Computing: Terminology
 2. Fault Tolerant Computing: Basic Concept
 3. Redundancy Technique: Hardware, Software, Information, Time
 4. Error Detection & Error Correction
 5. Modeling & Evaluation: Fault Modeling & Reliability
 6. Testing Digital Circuits
 7. Design for Test

การวัดผลเรียน
 1. Midterm Test 30%
 2. Final Assignment 20%
 3. Homework 50%

หนังสืออ่านประกอบ
 1. Several Sources

## Slide 2: 2.  *(visual)*
![SYLLABUS_2110473 slide 2](images/SYLLABUS_2110473_s002.png)


---

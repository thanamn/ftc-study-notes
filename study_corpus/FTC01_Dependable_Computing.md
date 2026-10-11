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

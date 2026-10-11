# FTC01 — Dependable Computing — Question Bank

Active-recall questions built from the slides. Answers cite `(Slide N)`.
Answer key is at the bottom of each section so you can self-test first.

---

## A. Concepts & Definitions

1. Give the two definitions of *dependability* (classic vs. later).
2. What does "Avoidance of Service failures that are unacceptably frequent or severe" connect a dependability failure to?
3. Name the three ways dependability is classified.
4. What are the two qualities used to judge service failures?

## B. Dependability Attributes

5. List the six **property-based** dependability attributes.
6. List the three **event-based** attributes and define each.
7. List the three **meta-information** attributes and define each.
8. Distinguish *robustness* from *stability* (commonalities and differences).
9. What are the four characteristics of a *resilient* system?
10. Define *availability* as a ratio.
11. Define *reliability* precisely (wrt time and conditions).
12. Give an example of a system that is **non-reliable but highly available**.
13. Give an example of a system that is **not reliable, not available, but safe**.
14. What is the **CIA triad** and what does each part mean?
15. Distinguish *Confidentiality → Information* from *Privacy → People*.
16. Distinguish *Data Quality* from *Data Integrity*.
17. Name three examples of **physical** integrity and three of **logical** integrity.
18. What is **RAM/RMA** and why does it matter for life-cycle cost?
19. Name the four classifications of maintenance and one line each.

## C. Dependability Means

20. List the four **dependability means** and define each.
21. In the space-mission example, give the specific technique used for each of the four means.
22. Differentiate **concurrent** vs **preemptive** error detection, with examples.
23. Differentiate the three **error recovery** methods: rollback, rollforward, compensation.
24. Differentiate the four **fault avoidance** steps: diagnosis, isolation, reconfiguration, reinitialization.
25. What is *coverage* and what are two ways it can be reduced?

## D. Dependability Threats (Impairments)

26. Define *fault*, *error*, and *failure*.
27. Give the classification of faults by **temporal** (three types) and by **origin** (three types).
28. Not all faults lead to errors, and not all errors lead to failures — explain both.
29. In interconnected systems, how can one system's failure relate to another system's fault/error?
30. Classify **failures** by Nature, Detection, Consistency, Severity.
31. Classify **errors** by Domain, Detection, Consistency, Severity.

## E. Limits & Challenges

32. What are the limits of dependability in terms of fault classes?
33. What is described as the "current bottleneck" of computing systems?
34. What are the two challenges of dependability?

---

# Answer Key

## A
1. classic '60: the probability that a system will operate when needed; review '95: an *integrative* concept — the property of a system such that its service can justifiably be trusted (Slide 6).
2. To **development process failure** (Slide 7).
3. Attributes (expected properties), Means (methods/techniques to provide the abilities), Threats/Impairments (causes or results of un-dependability) (Slide 8).
4. Failure **frequency** and **severity** (Slide 7).

## B
5. Availability, Reliability, Safety, Confidentiality, Integrity, Maintainability (Slide 10–11).
6. **Robustness** — persistence of dependability w.r.t. external faults; **Survivability** — persistence of dependability in the presence of active fault(s); **Resilience** — persistence of dependability when facing functional, environmental, or technological changes (Slide 32).
7. **Accountability** — availability & integrity of the *person* who performed an operation; **Authenticity** — integrity of message content & origin (+ possibly time of emission); **Non-repudiability** — availability & integrity of the identity of the sender/receiver (Slide 35).
8. Common: both defined for specified features of a system with specified perturbations, and both concern *persistence*. Differ: robustness addresses a more varied class of systems/perturbations/features, and extends beyond stability (Slide 33).
9. Latitude (max change before losing ability to recover), Resistance (ease/difficulty of changing the system), Precariousness (how close current state is to a threshold), Panarchy (degree a hierarchy level is influenced by other levels) — closely linked to Adaptive Capacity (Slide 34).
10. Availability = expected uptime / (expected uptime + expected downtime) (Slide 15).
11. The ability of an item to perform a required function under stated conditions up until a specified time (Slide 18).
12. A system that fails on average once per hour but restarts automatically in 10 ms → non-reliable but highly available (Slide 19).
13. A system that is turned off → not reliable, not available, but safe (Slide 25).
14. Confidentiality (rules limiting access to information), Integrity (information is trustworthy and accurate), Availability (guaranteed reliable access to information by authorized people) (Slide 26).
15. Confidentiality is about *information*; Privacy is about *people* (Slide 27).
16. Data Quality = whether data is *useful* (completeness, uniqueness, validity, timeliness, accuracy, consistency). Data Integrity = whether data is *trustworthy* (physical & logical integrity) (Slide 29).
17. Physical: redundant hardware/UPS, RAID, error-correcting codes, cryptographic hash, watchdog timer. Logical: file permission, access control, version control, referential/entity integrity, software bugs/design flaws/human errors (Slide 28).
18. Reliability + Availability + Maintainability — system design attributes affecting sustainment / total Life Cycle Cost (Slide 30).
19. Breakdown (repair after breakdown), Time-based preventive (periodic), Condition-based preventive (on specified conditions), Predictive (predict component life to maintain before breakdown) (Slide 31).

## C
20. **Fault Prevention** (prevent fault occurrence/introduction); **Fault Tolerance** (ensure service fulfills the function in the presence of faults); **Fault Removal** (reduce presence of faults); **Fault Forecasting** (estimate present number, future incidence, consequences of faults) (Slide 39).
21. Prevention: reliable coding practices / safe languages; Tolerance: detect & repair failed components during mission; Removal: remove faults at runtime or record for later removal; Forecasting: predict mission success likelihood from lessons learned (Slide 40).
22. **Concurrent**: during normal operation (watchdog timer, software assertions, process pairs). **Preemptive**: preempts the failure (spare checking, memory scrubbing, software rejuvenation) (Slide 43).
23. **Rollback** — restore state to before the fault (good for transient/intermittent); **Rollforward** — correct the fault and progress forward; **Compensation** — leverage natural redundancy to mask the error (Slide 44).
24. **Diagnosis** — identify root cause (location, type); **Isolation** — physically/logically exclude the faulty component; **Reconfiguration** — switch in non-faulty components and remap tasks; **Reinitialization** — record new state and update external entities (Slide 45).
25. Coverage = probability a technique detects/corrects a fault given a fault occurred. Reduced by: defects in the FTM's implementation ("who will check the checker?"), common-mode failures, or violated design assumptions (Slide 48).

## D
26. **Fault** — adjudged/hypothesized cause of an error; **Error** — part of the system state that may lead to a subsequent failure; **Failure** — delivered service deviates from the correct service (Slide 50).
27. Temporal: transient (occurs once at a location), intermittent (periodically recurs at a location), permanent (continuous and stable). Origin: physical faults, human-made faults (Slide 55).
28. Faults can be masked (not activated, e.g. unread locations) or corrected before they lead to errors (e.g. memory scrubbing in ECC). Errors can be benign (affect inconsequential state, or redundancy corrects them) (Slide 52).
29. One system's failure may be another system's fault/error (Slide 54).
30. Nature: halt/fail-stop vs erratic/babbling; Detection: signaled vs un-signaled/fail-silent; Consistency: consistent vs inconsistent; Severity: minor vs catastrophic (Slide 56).
31. Domain: timing vs content; Detection: detected vs latent; Consistency: consistent vs inconsistent; Severity: minor vs catastrophic (Slide 57).

## E
32. Physical faults, design/development faults, interaction faults (Slide 63).
33. Software reliability (Slide 63).
34. (1) Reducing the cost of computer failures; (2) extending fault tolerance from products to their production processes (Slide 68).

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

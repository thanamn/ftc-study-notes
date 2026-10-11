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

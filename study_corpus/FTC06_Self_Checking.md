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

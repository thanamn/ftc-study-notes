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

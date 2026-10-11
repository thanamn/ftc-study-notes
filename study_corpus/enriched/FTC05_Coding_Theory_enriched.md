# FTC05_Coding_Theory — Enriched (slide text + vision of visual slides)

> Text = exact extraction from the born-digital PDF. For `visual` slides, a faithful description of the figure/table/formula is added under **รายละเอียดจากภาพ**. Vision descriptions are model-produced and marked as such.

## Slide 1: Home Exercise: Checkpointing  *(visual)*
▪ Find the consistent cuts in the figure below (passing by ▓)

▪ The recovery line that you found is consistent, strongly consistent or
 inconsistent?

**รายละเอียดจากภาพ (vision):**

**Title:** Home Exercise: Checkpointing

**Bullet text:**
- Find the consistent cuts in the figure below (passing by <ไอคอนลายทแยงสีฟ้า เต็มกรอบสี่เหลี่ยม>) 
- The recovery line that you found is *consistent*, *strongly consistent* or *inconsistent*?

**Diagram:** แผนภาพเวลา (timeline) แบบ distributed system มีแกนนอน 4 เส้น ระบุปลายทางขวาเป็น **P0, P1, P2, P3** (บนลงล่าง) บนแต่ละเส้นมีกล่องสี่เหลี่ยมสีน้ำเงินเข้ม (checkpoint) หลายกล่อง และมีลูกศรดำเชื่อมระหว่าง process (message) ทิศทางทแยง

- บนเส้น P1 มีเครื่องหมาย **X สีแดง** (ตำแหน่งความล้มเหลว) อยู่ทางขวา
- มีเส้นโค้งประสีแดง (red curve) พาดผ่านจากบริเวณกลางไปยังขวา และเส้นโค้งสีน้ำเงิน (blue curve) อีกเส้นหนึ่ง พาดผ่านจากบนลงล่าง สื่อถึง recovery line / consistent cut ที่ต้องตรวจสอบ
- เส้นสีน้ำเงินเข้มแนวนอนคือ life line ของแต่ละ process; กล่องสีน้ำเงินคือ state/checkpoint ณ จุดต่าง ๆ

---

---

## Slide 2: Coding Theory
(Information Redundancy)

 2110473 Fault Tolerant Computing

Code Design for Dependable Systems, Eiji Fujiwara, JOHN WILEY & SONS, ISBN-13 978-0-471-75618-7, 2006
Notes on Coding Theory, J.I.Hall, Michigan State University, 2010
and Several Sources

---

## Slide 3: Contents
• Introduction
• Definition of Code
• Hamming Distance
• Linear/Cyclic Codes & Implementation
• Error Controls for Digital Systems
• Error Correcting Code
• Error Detecting Code: Checksum Code,
 Residue Code, Berger Code, Unordered Code

---

## Slide 4: Introduction
❑Coding Theory
 ▪The study of the properties of codes and their
 fitness for a specific application
 - Data Compression
 - Error Correction/ Error Control
 - Cryptography
 - Network Coding

---

## Slide 5: Various Stages of Data Processing  *(visual)*
5

**รายละเอียดจากภาพ (vision):**

**Title:** Various Stages of Data Processing

**Diagram (block diagram 2 คอลัมน์):**

ฝั่งซ้าย (ผู้ส่ง):
```
Digital Source
      ↓
Source Encoder
      ↓
Encryption
      ↓
Channel Encode
      ↓
Modulator
```
ฝั่งขวา (ผู้รับ):
```
Digital Link
      ↓
Source Decoder
      ↓
Decryption
      ↓
Channel Decode
      ↓
Demodulator
```

- ตรงกลางระหว่างสองคอลัมน์ มีป้ายกำกับทฤษฎีที่เกี่ยวข้อง:
  - **Information Theory** (ระหว่าง Source Encoder ↔ Source Decoder)
  - **Cryptography** (ระหว่าง Encryption ↔ Decryption)
  - **Coding Theory** (ระหว่าง Channel Encode ↔ Channel Decode)
- ตรงกลางล่าง: **Channel** มีลูกศรชี้จากซ้ายไปขวา (จาก Modulator ไป Demodulator)
- ใต้ Channel มีสัญลักษณ์สายฟ้า (lightning) พร้อมป้าย **Noise**

---

---

## Slide 6: Reliable Communication  *(visual)*
• In practice, most media are not perfect, Noisy channels:
 - Fiber-optic line, Satellite link, Hard disk, …
• Can we recover the original message (without errors)
 from a noisy code string?
• We focus two things:
 - Length of the code string
 - Probability of error

**รายละเอียดจากภาพ (vision):**

**Title:** Reliable Communication

**Diagram (block diagram):**
- **source string** (ลูกศรสีน้ำเงินลง) → กล่อง **encoder** (สีเหลือง) → กล่อง **noisy channel** (สีเหลือง) → กล่อง **decoder** (สีเหลือง) → ลูกศรสีน้ำเงินขึ้น → **decoded string**
- ลูกศรสีน้ำเงินเชื่อมระหว่างกล่องทั้งสาม

**Bullet text:**
- In practice, most media are not perfect, *Noisy channels*:
  – *Fiber-optic line, Satellite link, Hard disk, ...*
- Can we recover the original message (without errors) from a noisy code string?
- We focus two things:
  – *Length of the code string*
  – *Probability of error*

---

---

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

---

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

---

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

**รายละเอียดจากภาพ (vision):**

**Title:** Basic Concept

**Intro text:** *Error-correcting codes* are used to correct messages when they are transmitted through noisy channels

**Diagram 1 — Error correcting framework:**
- กล่อง **message source** → (ป้าย **W** บนลูกศร) → กล่อง **Encoding** → ป้าย **code word** → ผ่าน **channel** (มี **noise** ระบุ C(W) noise) → ได้ **code word W'** → กล่อง **Decoding** → (ป้าย **W**) → กล่อง **user**
- ป้ายแดงใต้ไดอะแกรม: **Error correcting framework**

**Diagram 2 — Example:**
- กล่อง **message YES or NO** → (ป้าย **YES**) → กล่อง **Encoding** (ภายในระบุ **YES → 00000**, **NO → 11111**) → ส่งผ่านสัญญาณรบกวน (สัญลักษณ์คลื่น/สี่เหลี่ยม) → **00000** → **01001** → กล่อง **Decoding** (ภายในระบุ **01001** แล้ว **00000**) → (ป้าย **YES**) → กล่อง **user**

**Definitions / text:**
- A *code* **C** over an alphabet **Σ** is a subset of **Σ\*** (**C ⊆ Σ\***)
- A *q -nary code* is a code over an alphabet of **q** -symbols
- A *binary code* is a code over the alphabet **{0,1}**

**Examples of codes:**
- C₁ = {00, 01, 10, 11}
- C₂ = {000, 010, 101, 100}
- C₃ = {00000, 01101, 10111, 11011}

---

---

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

---

## Slide 11: Claude Elwood Shannon  *(visual)*
"The father of Information Theory"
 American mathematician, electrical
 engineer, and cryptographer
 (Apr.30, 1916 - Feb.24, 2001)

**รายละเอียดจากภาพ (vision):**

**Title:** Claude Elwood Shannon

**Image:** ภาพถ่ายขาวดำของ Claude Elwood Shannon นั่งอยู่หน้ากากเครื่องคอมพิวเตอร์/แผงสวิตช์ (รูปอยู่ครึ่งซ้ายของสไลด์)

**Text (ด้านขวา):**
- **"The father of Information Theory"**
- *American mathematician, electrical engineer, and cryptographer*
- *(Apr.30, 1916 – Feb.24, 2001)*

---

---

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

---

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

---

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

---

## Slide 15: Binary symmetric channel (BSC) capacity
• Error rate p:
 Pr[𝑦= 1|𝑥= 0] = Pr[𝑦= 0|𝑥= 1] = 𝑝
 where x is the transmitted and y the received bit
• Channel capacity C(p):

 1 1
𝐶𝑝= 1 −𝐻𝑝= 1 −[𝑝log2 𝑝+ (1 −𝑝) log2 1−𝑝]
 (H: binary entropy function)
• For instance, 𝐶(0.1) ≈0.53, Ratio about 1:2

---

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

---

## Slide 17: Example
The encoding

 0→000 1 →111

 1
The probability of the bit error 𝑝 and the majority 2,
voting decoding

 000, 001, 010, 100 →000, 111, 110, 101, 011 →111
The probability of an erroneous message is
 3𝑝2 1 −𝑝+ 𝑝3 = 3𝑝2 −2𝑝3 < 𝑝

---

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

**รายละเอียดจากภาพ (vision):**

**Title:** Coding of a path avoiding an enemy territory

**Story text:**
- **Story:** Alice and Bob share an identical map gridded as shown. Only Alice knows the route through which Bob can reach her avoiding the enemy territory. Alice wants to send Bob the following information about the safe route he should take

**Code string (ข้อความสีดำตัวพิมพ์ใหญ่):**
`NNWNNWWS SWWNNNNWWN`

**Diagram (แผนที่ตาราง grid):**
- ด้านบนระบุชื่อ **Alice**, ด้านล่างขวาระบุ **Bob**
- มีป้าย **HQ** อยู่มุมบนซ้าย (จุดเริ่มต้น)
- ด้านขวาระบุ **N** พร้อมลูกศรทิศเหนือ (เข็มทิศ: ลูกศรขึ้น = N, ลูกศรขวา)
- มีพื้นที่แรเงา (เส้นทแยง, hatched) แทน enemy territory หลายบริเวณ
- มีเส้นทาง (route) เป็นเส้นหัก/มุมฉาก พร้อมลูกศรทิศทาง แสดงเส้นทางจาก HQ ไปยังจุด **x** ของ Bob โดยเลี่ยงพื้นที่แรเงา
- จุดสิ้นสุดคือเครื่องหมาย **x** ใกล้ป้าย **Bob** ที่มุมล่างขวา

---

---

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

---

## Slide 20: Definition of Code
• A code 𝐶over an alphabet Σ is a subset of
 Σ∗(C ⊆Σ∗)
• A q-nary code is a code over alphabet of q symbols
• A binary code is a code over the alphabet {0,1}

---

## Slide 21: Richard Wesley Hamming  *(visual)*
"Hamming Distance"
American mathematician
"The purpose of computing is insight,
not numbers"
(Feb.11, 1915 - Jan.7, 1998)

**รายละเอียดจากภาพ (vision):**

**Title:** Richard Wesley Hamming

**Text (ด้านซ้าย):**
- **"Hamming Distance"**
- *American mathematician*
- **"The purpose of computing is insight, not numbers"**
- *(Feb.11, 1915 – Jan.7, 1998)*

**Image:** ภาพขาวดำของ Richard Wesley Hamming กำลังยืนบรรยายหน้า whiteboard (มีสมการคณิตศาสตร์เขียนอยู่บนกระดาน) โดยมี silhouettes ของผู้ฟังอยู่ด้านหน้า (รูปอยู่ครึ่งขวา)

---

---

## Slide 22: Hamming Weight
• Hamming Weight w(𝑐):
 - the number of nonzero components in the
 codeword

 ex.
 w(00000) = 0
 w(11111) = 5
 w(1022001) = 4
 w(1011001) = 4

---

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

**รายละเอียดจากภาพ (vision):**

**Title:** Hamming Distance

**Bullet text:**
- **Hamming Distance h(x, y):**
  – The number of positions where words x and y differs
  ex:  h(10101; 01100) = 3,  h(fourth; eighth) = 4
- **Properties:**
  – h(x,y) = 0 ⇔ x = y
  – h(x,y) = h(y,x)
  – h(x,z) ≤ h(x,y) + h(y,z) ⇒ *triangle inequality*
- **Minimal distance:**
  h(C) = min{h(x,y)|x, y ∈ C, x ≠ y}

**สูตรปิดท้าย (ตัวหนา/แดง):**
- Code C can **detect** up to s errors if **h(C) ≥ s + 1**
- Code C can **correct** up to t errors if **h(C) ≥ 2t + 1**

---

---

## Slide 24: Hamming VS Shannon  *(visual)*
Hamming Shannon
Focus on codewords itself Directly deal wt encoding and
 decoding functions
 Look at explicit codes Not explicit at all

 Fundamental trade off: Fundamental trade off:
 rate vs distance rate vs error
 (easy to handle)

 Worst case errors Stochastic errors

**รายละเอียดจากภาพ (vision):**

**Title:** Hamming VS Shannon

**Table:**

| Hamming | Shannon |
|---|---|
| Focus on codewords itself | Directly deal wt encoding and decoding functions |
| Look at explicit codes | Not explicit at all |
| Fundamental trade off: rate vs distance (easy to handle) | Fundamental trade off: rate vs error |
| Worst case errors | Stochastic errors |

---

---

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

---

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

---

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

---

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

---

## Slide 29: Design of one code from another code
•If d is odd, then (n,d) = (n +1,d +1) A2 A2
•If d is even, then (n,d) = (n -1,d -1) A2 A2

 = 4ex. A2(5,3) = 4 A2(6,4)
 (5,4,3)-code (6,4,4)-code

---

## Slide 30: Equivalence
• Two q-nary codes are equivalent if one can be
 obtained from the other by a combination of
 following operations:
1. permutation of the positions of the code
2. permutation of symbols at the fixed positions

---

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

---

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

---

## Slide 33: Check yourself 1
• Use nearest neighbor decoding to determine
 which code word was sent from the code C =
 {0000, 1110, 1011} if 0110 is received?

 d(0110,0000)=?
 d(0110,1110)=?
 d(0110,1011)=?

---

## Slide 34: Check yourself 2
• Suppose that when a bit is sent over a binary
 symmetric channel the probability it is
 received incorrectly is 0.01. What is the
 probability that the bit string 100010 is
 received when the bit string 000000 is sent?

 Maximum likelihood decoding:
 Prob (4 correct & 2 incorrect) =
• (0.99)4(0.01)2 = 0.000096059601

---

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

---

## Slide 36: Check yourself 4
• Let C = {00000000, 11111000, 01010111,
 10101111},
How many errors can C detect and how many
can it correct?

 Minimum distance C {00000000, …, 10101111} = ?
 Detect upto = (minimum distance - 1) = ?
 Correct upto = | (minimum distance - 1) / 2 | = ?

---

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

---

## Slide 38: Cyclic codes
• Definition: Any cyclic shift of a codeword produces another codeword
• A k-bit data word corresponds to a polynomial of degree k-1
 Data = 1101001: d(x) = 1 + x + x3 + x6 (modulo-2 sum)
 (n, k) cyclic code has a generator polynomial of degree r = n-k

 g(x) = 1 + x + x3
 To encode data (1101001), multiply its associated polynomial by g(x)

• Detect all burst errors of width less than n-k

---

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

---

## Slide 40: Factorization of X  *(visual)*
n-1 (Xn+1)

**รายละเอียดจากภาพ (vision):**

**Title:** Factorization of Xⁿ-1 (Xⁿ+1)

**Table:** คอลัมน์ **n** และ **xⁿ + 1 =**

| n | xⁿ + 1 = |
|---|---|
| 1 | (x + 1) |
| 2 | (x + 1)² |
| 3 | (x + 1)(x² + x + 1) |
| 4 | (x + 1)⁴ |
| 5 | (x + 1)(x⁴ + x³ + x² + x + 1) |
| 6 | (x + 1)²(x² + x + 1)² |
| 7 | (x + 1)(x³ + x + 1)(x³ + x² + 1) |
| 8 | (x + 1)⁸ |
| 9 | (x + 1)(x² + x + 1)(x⁶ + x³ + 1) |
| 10 | (x + 1)²(x⁴ + x³ + x² + x + 1)² |
| 11 | (x + 1)(x¹⁰ + x⁹ + x⁸ + x⁷ + x⁶ + x⁵ + x⁴ + x³ + x² + x + 1) |
| 12 | (x + 1)⁴(x² + x + 1)⁴ |
| 13 | (x + 1)(x¹² + x¹¹ + x¹⁰ + x⁹ + x⁸ + x⁷ + x⁶ + x⁵ + x⁴ + x³ + x² + x + 1) |
| 14 | (x + 1)²(x³ + x + 1)²(x³ + x² + 1)² |
| 15 | (x + 1)(x² + x + 1)(x⁴ + x + 1)(x⁴ + x³ + 1)(x⁴ + x³ + x² + x + 1) |
| 16 | (x + 1)¹⁶ |
| 17 | (x + 1)(x⁸ + x⁵ + x⁴ + x³ + 1)(x⁸ + x⁷ + x⁶ + x⁴ + x² + x + 1) |
| 18 | (x + 1)²(x² + x + 1)²(x⁶ + x³ + 1)² |
| 19 | (x + 1)(x¹⁸ + x¹⁷ + x¹⁶ + ⋯ + x + 1) |
| 20 | (x + 1)⁴(x⁴ + x³ + x² + x + 1)⁴ |
| 21 | (x + 1)(x² + x + 1)(x³ + x + 1)(x³ + x² + 1)(x⁶ + x⁴ + x² + x + 1)(x⁶ + x⁵ + x⁴ + x² + 1) |
| 22 | (x + 1)²(x¹⁰ + x⁹ + x⁸ + x⁷ + x⁶ + x⁵ + x⁴ + x³ + x² + x + 1)² |
| 23 | (x + 1)(x¹¹ + x⁹ + x⁷ + x⁶ + x⁵ + x + 1)(x¹¹ + x¹⁰ + x⁶ + x⁵ + x⁴ + x² + 1) |
| 24 | (x + 1)⁸(x² + x + 1)⁸ |
| 25 | (x + 1)(x⁴ + x³ + x² + x + 1)(x²⁰ + x¹⁵ + x¹⁰ + x⁵ + 1) |
| 26 | (x + 1)²(x¹² + x¹¹ + x¹⁰ + x⁹ + x⁸ + x⁷ + x⁶ + x⁵ + x⁴ + x³ + x² + x + 1)² |
| 27 | (x + 1)(x² + x + 1)(x⁶ + x³ + 1)(x¹⁸ + x⁹ + 1) |
| 28 | (x + 1)⁴(x³ + x + 1)⁴(x³ + x² + 1)⁴ |
| 29 | (x + 1)(x²⁸ + x²⁷ + ⋯ + x + 1) |
| 30 | (x + 1)²(x² + x + 1)²(x⁴ + x + 1)²(x⁴ + x³ + 1)²(x⁴ + x³ + x² + x + 1)² |
| 31 | (x + 1)(x⁵ + x² + 1)(x⁵ + x³ + 1)(x⁵ + x³ + x² + x + 1)(x⁵ + x⁴ + x² + x + 1)(x⁵ + x⁴ + x³ + x + 1)(x⁵ + x⁴ + x³ + x² + 1) |

---

---

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

**รายละเอียดจากภาพ (vision):**

**Title:** Modulo-2 Multiplication

**Bullet text:**
- The **5th** bit of the product is the *modulo-2* sum of the corresponding bits of the multiplicand shifted **0** times, **3** times, and **4** times
- If multiplicand is *fed in serially* – we add the shifted multiplicand
- Shifting done by *delay elements*
- This cyclic code is *not separable* - data and check bits within **110000100011101** are not separable

**Example computation (การคูณแบบ long multiplication):**

```
        10001100101
    ×        11001
    ---------------
        10001100101
       00000000000
      00000000000
     10001100101
    10001100101
    ---------------
    110000100011101
```

(แถวของ partial product มีเส้นกรอบสี่เหลี่ยมแนวตั้ง เน้นคอลัมน์บิตที่ 5 ของผลคูณ)

**Circuit diagram:** วงจร shift register / LFSR ประกอบด้วย
- delay elements **D** หลายตัวต่อกัน (4 ตัวในแนวกลาง)
- สัญญาณป้อนเข้าด้านซ้ายมีป้าย **o₄**, แล้วตามด้วย **o₁** ระหว่าง D, **o₂**, **o₁**
- มี XOR gate (วงกลมเครื่องหมาย +) ระหว่าง delay element ตัวแรกและตัวที่สอง (มี **i** กำกับอยู่ด้านใน)
- ทางขวาสุด: สัญญาณรวมผ่าน XOR-like gate ไปยังป้าย **Encoded Output**
- ด้านล่างมีเส้นสัญญาณย้อนกลับจากซ้ายไปขวา ไปยังป้าย **Data**

---

---

## Slide 42: Operation of Encoding Code  *(visual)*
• i3 is the input to the O3
 delay element

 110000100011101

 10001100101

**รายละเอียดจากภาพ (vision):**

**Title:** Operation of Encoding Code

**Table (columns: shift clock | input data | O₄ | i₃ | O₃,O₂,O₁ | encoded output):**

| shift clock | input data | O₄ | i₃ | O₃,O₂,O₁ | encoded output |
|---|---|---|---|---|---|
| 1 | 1 | 0 | 1 | 000 | 1 |
| 2 | 0 | 1 | 1 | 100 | 0 |
| 3 | 1 | 0 | 1 | 110 | 1 |
| 4 | 0 | 1 | 1 | 111 | 1 |
| 5 | 0 | 0 | 0 | 111 | 1 |
| 6 | 1 | 0 | 1 | 011 | 0 |
| 7 | 1 | 1 | 0 | 101 | 0 |
| 8 | 0 | 1 | 1 | 010 | 0 |
| 9 | 0 | 0 | 0 | 101 | 1 |
| 10 | 0 | 0 | 0 | 010 | 0 |
| 11 | 1 | 0 | 1 | 001 | 0 |
| 12 | 0 | 1 | 1 | 100 | 0 |
| 13 | 0 | 0 | 0 | 110 | 0 |
| 14 | 0 | 0 | 0 | 011 | 1 |
| 15 | 0 | 0 | 0 | 001 | 1 |

**Bullet text:**
- **i3** is the input to the **O3** delay element

**Circuit diagram:** เหมือน Slide 41 (shift register/LFSR)
- delay elements **D** ต่อกัน โดยมีป้าย **o₄**, **o₁**, **o₂**, **o₁** กำกับ
- มี XOR gate (วงกลม +) ระหว่าง D ตัวแรกกับตัวที่สอง (ป้าย **i** ด้านใน)
- ขวาสุด: ป้าย **Encoded Output**
- ด้านล่าง: **Data**
- หมายเลขสีน้ำเงินเหนือวงจร: **110000100011101**
- หมายเลขสีน้ำเงินใต้วงจร (ตรงป้าย Data): **10001100101**

---

---

## Slide 43: Decoding Through Division by  *(visual)*
Generator Polynomial

 error!!

• Division by 11001
• Subtraction modulo-2 - identical to addition
• Zero remainder indicates no error detected
• If a single error occurs - 110000100111101 - non-zero remainder

**รายละเอียดจากภาพ (vision):**

**Title:** Decoding Through Division by Generator Polynomial

**การหารยาวแบบ modulo-2 (long division) สองกรณี:**

กรณีซ้าย (ไม่มี่ error):
```
110000100011101 : 11001 = 10001100101
11001
-----
 10100
 11001
 -----
  11010
  11001
  -----
   11111
   11001
   -----
    11001
    11001
    -----
     00000
```
ผลลัพธ์ = **10001100101**, เศษ = **00000** (วงรีสีน้ำเงินล้อมรอบ)

กรณีขวา (มี error — บิตที่วงกลมสีแดงในเลขตั้งต้นคือ '1' ที่ตำแหน่งหนึ่ง):
```
110000100111101 : 11001 = 10001100110
11001
-----
 10100
 11001
 -----
  11011
  11001
  -----
   10111
   11001
   -----
    11100
    11001
    -----
     01011
```
- คำว่า **error!!** ตัวเอียงสีแดง (อยู่ข้างบิตที่วงกลมสีแดงในตัวตั้ง)
- เศษ = **01011** (วงรีสีแดงล้อมรอบ)

**Bullet text:**
- Division by **11001**
- Subtraction *modulo-2* - identical to addition
- *Zero remainder* indicates no error detected
- If a single error occurs – **110000100111101** (บิตที่ผิดเน้นสีแดง ตัว '1' ตรงกลาง) - *non-zero remainder*

---

---

## Slide 44: Three Bit Errors  *(visual)*
• 110000111010101 instead of 1100000100011101 - zero remainder
 - errors not detected (erroneously)
• If errors are adjacent - 110000011011101 - non-zero remainder
 indicates an error 44

**รายละเอียดจากภาพ (vision):**

**Title:** Three Bit Errors

**การหารยาวแบบ modulo-2 สองกรณี (เกิด error หลายบิต):**

กรณีซ้าย (ตัวตั้ง = `110000111010101`, มีวงกลมสีแดงล้อม 2 บิตที่ตำแหน่ง 9 และ 10):
```
110000111010101 : 11001 = 10001101101
11001
-----
 10111
 11001
 -----
  11100
  11001
  -----
   10110
   11001
   -----
    11111
    11001
    -----
     11001
     11001
     -----
      00000
```
เศษ = **00000** (วงรีสีแดงล้อม) — แสดงว่า error ไม่ถูกตรวจจับ

กรณีขวา (ตัวตั้ง = `110000111011101`, มีวงกลมสีแดงล้อมบิตหนึ่ง):
```
110000111011101 : 11001 = 10001110011
11001
-----
 10011
 11001
 -----
  10100
  11001
  -----
   11011
   11001
   -----
    10110
    11001
    -----
     11111
     11001
     -----
      00110
```
เศษ = **00110** (วงรีสีแดงล้อม)

**Bullet text:**
- **110000111010101** instead of **110000100011101** - errors not detected (erroneously)
  (มีลูกศรชี้ไปยังเศษ 00000 ทางซ้าย และลูกศรชี้ไปที่คำว่า "zero remainder")
- If errors are adjacent - **110000011011101** (บิตที่ผิดเน้นสีแดง) - *non-zero remainder* indicates an error
  (ลูกศรชี้จากข้อความนี้ไปยังเศษ 00110 ทางขวา)

---

---

## Slide 45: Cyclic code implementation
• Multiply K bit data by (n-k+1) bit multiplier ((n-k) degree
 polynomial), the result is n bit encoded data: (n,k) cyclic code
• Shift register circuit for multiplying by generator polynomial,
 g(x) = g0+g1x+· · ·+grxr
• An encoder for an (n, k) cyclic code with generator polynomial
 g(x), with r = n-k

---

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

---

## Slide 47: Generator Polynomial
• (n,k) cyclic code:

• If n = 5: x5 + 1 = (x + 1)(x4 + x3 + x2 + x + 1)
 example 1: k = 4, g(x) = (x + 1)

• If n = 7: x7 + 1 = (x + 1)(x3 + x + 1)(x3 + x2 + 1)
 example 2: k = 4, g(x) = (x3 + x + 1)

---

## Slide 48: Cyclic code
encoding example 1

• k = (0111), g(x) = (1 + x)

 x 1 1 1 0 →
 + 1 0 0 1 0 →= (01001)

 1 1 1 0 → D
 1 1 1 0 x →

---

## Slide 49: Cyclic code
decoding example 1

• k(x) = e(x)/g(x) - Remainder (zero if no error)
• E = (01001), g(x) = (1 + x) k(x) = e(x) + k(x)*x

 0 1 0 0 1
 + 0 1 0 0 1

 0 1 1 1 0 D

 x 0 1 1 1

---

## Slide 50: Cyclic code
decoding example 1

• K(X) = E(X)/G(X) - Remainder (non-zero if error)
• E = (01101), g(x) = (1 + x) K(X) = E(X) + K(X)*X

 0 1 1 0 1
 + 0 1 1 0 1

 0 1 0 0 1 D
 x 0 1 0 0

---

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

**รายละเอียดจากภาพ (vision):**

**Title:** Cyclic code **encoding** example 2

**Formula line:** K = (0111), g(x) = (1 + x + x³)

**Side computation (มุมซ้ายบน, กรอบสี่เหลี่ยม — การหารยาว):**
```
0111
1101
----
0111
0111
----
0111
0111
----
0100011
```

**Circuit diagram (ด้านขวาบน):**
- สัญญาณป้อนเข้าจากซ้าย: **1 1 1 0 →** เข้าที่ป้าย **K**
- XOR gate แรก (วงกลม **+**) เอาต์พุตมีป้าย **A1** → ไปยัง XOR gate ที่สอง (วงกลม **+**) → เอาต์พุตป้าย **A3**, และป้าย **E**
- ล่างลงมา: delay elements **D1 → D2 → D3** เรียงต่อกัน มีลูกศรจาก D3 กลับขึ้นไปยัง XOR แรกและจาก D2 ขึ้นไปยัง XOR ที่สอง (เส้น blue)
- ด้านขวา: **E** → **1 1 0 0 0 1 0 →**
- ข้อความตัวแดง: **E = (0100011)**

**Table (columns: K | D1 | A1 | D2 | D3 | A3 (E)):**

| K | D1 | A1 | D2 | D3 | A3 (E) |
|---|---|---|---|---|---|
| 0 | x | 0 | x | x | 0 |
| 1 | 0 | 1 | x | x | 1 |
| 1 | 1 | 0 | 0 | x | 0 |
| 1 | 1 | 0 | 1 | 0 | 0 |
| 0 | 1 | 1 | 1 | 1 | 0 |
| 0 | 0 | 0 | 1 | 1 | 1 |
| 0 | 0 | 0 | 0 | 1 | 1 |

(คอลัมน์ **A3 (E)** อยู่ในกรอบสี่เหลี่ยมสีแดง)

---

---

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

**รายละเอียดจากภาพ (vision):**

**Title:** Cyclic code **decoding** example 2

**Formula line:** E = (0100011), g(x) = (1 + x + x³) ⇒ K(X) = E(X) + K(X)(X + X³)

**Side computation (มุมซ้ายบน, กรอบสี่เหลี่ยม):**
```
0100011
 1101   :01
-----
 10111
 1101   :1
 -----
  1101
  1101  :1
  -----
   000
```

**Circuit diagram:**
- ด้านขวา: **E ← 0 1 0 0 0 1 1** (ลูกศรชี้ซ้ายเข้าใกล้ XOR ตัวขวา ป้าย **A1**)
- XOR gate (วงกลม **+**) → XOR gate ที่สอง (ป้าย **A3**) → ออกทางซ้ายเป็น **K ← 0 1 1 1**
- delay elements เรียงย้อนทาง: **D1 ← D2 ← D3** (ลูกศรชี้ไปทางซ้าย)
- มีเส้นสัญญาณจากด้านล่างของ D3 กลับไปยังปลายทาง K (ด้านซ้ายสุด)

**Table (columns: E | D1 | D2 | D3 | A1 | A3 (K)):**

| E | D1 | D2 | D3 | A1 | A3 (K) |
|---|---|---|---|---|---|
| 0 | x | x | x | 0 | 0 |
| 1 | 0 | x | x | 1 | 1 |
| 0 | 1 | 0 | x | 1 | 1 |
| 0 | 1 | 1 | 0 | 1 | 1 |
| 0 | 1 | 1 | 1 | 1 | 0 |
| 1 | 0 | 1 | 1 | 1 | 0 |
| 1 | 0 | 0 | 1 | 1 | 0 |

(คอลัมน์ **A3 (K)** อยู่ในกรอบสี่เหลี่ยมสีแดง)

---

---

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

**รายละเอียดจากภาพ (vision):**

**Title:** Cyclic code **decoding** example 2

**Formula line:** E = (010**1**011), g(x) = (1 + x + x³) ⇒ K(X) = E(X) + K(X)(X + X³)
(ตัวเลข '1' ที่ 4 เน้นสีแดง)

**Side computation (มุมซ้ายบน, กรอบสี่เหลี่ยม):**
```
0101011
 1101   :01
-----
 11111
 1101   :1
 -----
  0101
  0000  :0
  -----
   101
```
(บรรทัด 101 เน้นสีแดง และบรรทัด 0000:0)

**Circuit diagram:** เหมือน Slide 52
- ด้านขวา: **E ← 0 1 0 1 0 1 1** (บิต '1' ตัวที่ 4 เน้นสีแดง ป้าย **A1**)
- XOR gates สองตัว → ออกทางซ้ายเป็น **K ← 0 1 1 0** (บิต '0' ตัวสุดท้ายเน้นสีแดง ป้าย **A3**)
- delay elements **D1 ← D2 ← D3**

**Table (columns: E | D1 | D2 | D3 | A1 | A3 (K)):**

| E | D1 | D2 | D3 | A1 | A3 (K) |
|---|---|---|---|---|---|
| 0 | x | x | x | 0 | 0 |
| 1 | 0 | x | x | 1 | 1 |
| 0 | 1 | 0 | x | 1 | 1 |
| 1 | 1 | 1 | 0 | 0 | 0 |
| 0 | 0 | 1 | 1 | 0 | 1 |
| 1 | 1 | 0 | 1 | 0 | 1 |
| 1 | 1 | 0 | 0 | 0 | 0 |

(แถว E=1 (แถวที่ 4, D1=1) เน้นสีแดงเฉพาะค่า; คอลัมน์ **A3 (K)** อยู่ในกรอบสี่เหลี่ยมสีแดง)

---

---

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

---

## Slide 55: Error Detection  *(visual)*
55

**รายละเอียดจากภาพ (vision):**

**Title:** Error Detection

**Diagram (Venn-style สองวง):**
- วงรีด้านซ้ายสีฟ้า: **Data space** ภายในมี **Data words** (จุดสีน้ำเงินหลายจุด บางจุดเป็นสี่เหลี่ยมสีน้ำเงินเข้ม = data word)
- วงรีด้านขวาสีเหลือง: **Code space** ภายในมี **Codewords** (จุดสีเขียวเข้ม) และ **Errors** (จุดสีแดง อยู่บริเวณล่างขวา)
- ป้าย **Error space** อยู่มุมล่างขวาของวงสีเหลือง (บริเวณที่มีจุดแดง = **Noncodewords**)
- ลูกศรเชื่อม **Encoding** จากวง data ไปยังวง code (ชี้ไปที่ codeword)
- ลูกศรเชื่อม **Decoding** จากวง code กลับไปยังวง data
- เส้นประ (dashed) จาก codeword ไปยังจุดแดงแต่ละจุด (แสดงการเกิด error → noncodewords)

---

---

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

---

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

---

## Slide 58: Further Readings
(Out-of-scope)

• Other Properties of Codes
• ISBN Code
• Data Compression
 - ZIP Code, Reed-Solomon Code
• Cryptography
• Information Theory

---

## Slide 59: HW05: Cyclic code
• Generate (7,4) Cyclic code from the data
 (0101, 1001, 0010, 1110, 0000), and its
 hardware implementation.

---

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

---

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

**รายละเอียดจากภาพ (vision):**

**Title:** Home Exercise: Cyclic code 2/4 (Encoding)

**Formula line:** m = (0101), g(x) = (1 + x² + x³)

**Side computation (มุมซ้ายบน, กรอบสี่เหลี่ยม):**
```
0101
1011
----
0101
0101
----
0101
0101
----
0100111
```

**Circuit diagram:**
- สัญญาณป้อนเข้าจากซ้าย: **1 0 1 0 →** เข้าป้าย **K**
- XOR gate แรก (วงกลม **+**) เอาต์พุตป้าย **A2** → XOR gate ที่สอง → เอาต์พุตป้าย **A3**, **E**
- ป้าย **A0** อยู่บนเส้นที่มาจาก K ขึ้นไปยัง XOR แรก
- delay elements **D1 → D2 → D3** เรียงต่อ; จาก D3 ขึ้นไปยัง XOR แรก, จาก D2 ขึ้นไปยัง XOR ที่สอง (เส้น blue)
- ด้านขวา: **E → 1 1 1 0 0 1 0 →**
- ข้อความตัวแดง: **E = (0100111)**

**Table (columns: K (A0) | D1 | D2 | A2 | D3 | A3 (E)):**

| K (A0) | D1 | D2 | A2 | D3 | A3 (E) |
|---|---|---|---|---|---|
| 0 | x | x | 0 | x | 0 |
| 1 | 0 | x | 1 | x | 1 |
| 0 | 1 | 0 | 0 | x | 0 |
| 1 | 0 | 1 | 0 | 0 | 0 |
| 0 | 1 | 0 | 0 | 1 | 1 |
| 0 | 0 | 1 | 1 | 0 | 1 |
| 0 | 0 | 0 | 0 | 1 | 1 |

(คอลัมน์ **A3 (E)** อยู่ในกรอบสี่เหลี่ยมสีแดง)

---

---

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

---

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

**รายละเอียดจากภาพ (vision):**

**Title:** Cyclic code **decoding** example 3/4

**Formula line:** E = (0100011), g(x) = (1 + x² + x³) ⇒ K(X) = E(X) + K(X)(X² + X³)

**Side computation (มุมซ้ายบน, กรอบสี่เหลี่ยม):**
```
0100011
 1101   :01
-----
 10111
 1101   :1
 -----
  1101
  1101  :1
  -----
   000
```

**Circuit diagram:**
- ด้านขวา: **E ← 0 1 0 0 0 1 1** (เข้าป้าย **A1**)
- XOR gate แรก → XOR gate ที่สอง (ป้าย **A3**) → ออกทางซ้ายเป็น **K ← 0 1 1 1**
- delay elements เรียงย้อนทาง: **D1 ← D2 ← D3**
- มีเส้นสัญญาณย้อนกลับจาก D3 ไปยัง K

**Table (columns: E | D1 | D2 | D3 | A1 | A3 (K)):**

| E | D1 | D2 | D3 | A1 | A3 (K) |
|---|---|---|---|---|---|
| 0 | x | x | x | 0 | 0 |
| 1 | 0 | x | x | 1 | 1 |
| 0 | 1 | 0 | x | 1 | 1 |
| 0 | 1 | 1 | 0 | 1 | 1 |
| 0 | 1 | 1 | 1 | 1 | 0 |
| 1 | 0 | 1 | 1 | 1 | 0 |
| 1 | 0 | 0 | 1 | 1 | 0 |

(คอลัมน์ **A3 (K)** อยู่ในกรอบสี่เหลี่ยมสีแดง)

---

---

## Slide 64: Error Controls for Digital Systems  *(visual)*
Data
 Transmission
 Corrected
 Digital Systems Corrector Output

 Data
Operation

 Error
 Checker Signal

**รายละเอียดจากภาพ (vision):**

**Title:** Error Controls for Digital Systems

**Diagram (block diagram):**
- กล่อง **Digital Systems** ด้านซ้ายบน
- ลูกศรหนาสีน้ำเงินจาก Digital Systems ไปทางขวา (ป้าย **Data Transmission**) → กล่อง **Corrector**
- จาก Corrector มีลูกศรหนาไปทางขวา → ป้าย **Corrected Output**
- จาก Digital Systems มีลูกศรลง (ป้าย **Data Operation**) → กล่อง **Checker** (ด้านล่าง)
- จากกลาง (บนเส้น Data Transmission) มีลูกศรลงเข้าสู่ Checker
- จาก Checker มีลูกศรขึ้นเข้าสู่ Corrector
- จาก Checker มีเส้นบางสีน้ำเงินไปทางขวา → ป้าย **Error Signal**

---

---

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

---

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

---

## Slide 67: Error Correcting Code Function  *(visual)*
67

**รายละเอียดจากภาพ (vision):**

**Title:** Error Correcting Code Function

**Diagram (block diagram / signal flow):**
- ด้านซ้ายล่าง: **Data In** → (ป้าย **M** บนเส้น) → กล่อง **Memory**
- ก่อนถึง Memory มีการแยกสัญญาณลงไปยังกล่อง **f** (เล็ก) ด้านล่าง; จาก f ออกเป็น (ป้าย **K**) เข้า Memory
- จาก Memory ออกสองทาง: ทางบน (ป้าย **M**) → กล่อง **f** → (ป้าย **K**) → กล่อง **Compare**
- ทางล่างจาก Memory (ป้าย **K**) → ตรงเข้าสู่ **Compare**
- ออกจาก Memory ทางบน (ก่อนเข้า f) ยังแยกขึ้นไปยังกล่อง **Corrector** (อยู่กลางบน)
- จาก Corrector สัญญาณไปทางซ้ายเป็น **Data Out** (มีป้าย **M** บนเส้น)
- จาก Compare มีเส้นสัญญาณย้อนขึ้นไปยัง Corrector และไปทางซ้ายบนเป็น **Error Signal**
- (จาก Memory ทาง M ยังมีเส้นแยกขึ้นไปทางซ้ายบนเข้าสู่เส้น Data Out)

---

---

## Slide 68: Overlapped Parity Code  *(visual)*
• Single Error Correcting (SEC)/ 8-Data bits wt 4-Check bits

**รายละเอียดจากภาพ (vision):**

**Title:** Overlapped Parity Code

**Bullet text:**
- Single Error Correcting (SEC)/ 8-Data bits wt 4-Check bits

**Table / bit layout:**
- แถวหัว บน: **12  11  10  9  8  7  6  5  4  3  2  1** พร้อมป้าย **Bit Position** ทางขวา
- 4 แถวข้อมูล:

| row | 12 | 11 | 10 | 9 | 8 | 7 | 6 | 5 | 4 | 3 | 2 | 1 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | 0 | 1 | 0 | 1 | 0 | 1 | 0 | 1 | 0 | 1 | 0 | 1 |
| 2 | 0 | 1 | 1 | 0 | 0 | 1 | 1 | 0 | 0 | 1 | 1 | 0 |
| 3 | 1 | 0 | 0 | 0 | 0 | 1 | 1 | 1 | 1 | 0 | 0 | 0 |
| 4 | 1 | 1 | 1 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |

- แถวป้ายกำกับ (ใต้ข้อมูล): **C4** (ในคอลัมน์ 8), **C3** (คอลัมน์ 4), **C2** (คอลัมน์ 2), **C1** (คอลัมน์ 1) — พร้อมป้าย **Check Bit** ทางขวา
- แถวป้ายกำกับล่าง: **D8 D7 D6 D5** (คอลัมน์ 12,11,10,9), **D4 D3 D2** (คอลัมน์ 7,6,5), **D1** (คอลัมน์ 3) — พร้อมป้าย **Data Bit** ทางขวา

**Formula & definition (ด้านล่าง):**
- **2ᵏ − 1 ≥ m + k**
- **m = data bits**
- **k = parity bits**

---

---

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

---

## Slide 70: Compute Check  *(visual)*
70

**รายละเอียดจากภาพ (vision):**

**Title:** Compute Check

**Table / bit layout:** เหมือน Slide 68 (หัวตารางและข้อมูลชุดเดียวกัน)

- แถวหัว: **12  11  10  9  8  7  6  5  4  3  2  1** — ป้าย **Bit Position**

| row | 12 | 11 | 10 | 9 | 8 | 7 | 6 | 5 | 4 | 3 | 2 | 1 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | 0 | 1 | 0 | 1 | 0 | 1 | 0 | 1 | 0 | 1 | 0 | 1 |
| 2 | 0 | 1 | 1 | 0 | 0 | 1 | 1 | 0 | 0 | 1 | 1 | 0 |
| 3 | 1 | 0 | 0 | 0 | 0 | 1 | 1 | 1 | 1 | 0 | 0 | 0 |
| 4 | 1 | 1 | 1 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |

- ป้าย **Check Bit**: **C4** (คอลัมน์ 8), **C3** (คอลัมน์ 4), **C2** (คอลัมน์ 2), **C1** (คอลัมน์ 1)
- ป้าย **Data Bit**: **D8 D7 D6 D5** (12,11,10,9), **D4 D3 D2** (7,6,5), **D1** (3)

**Formulas (สมการคำนวณ check bits):**
- **C1 = D1 ⊕ D2 ⊕ D4 ⊕ D5 ⊕ D7**
- **C2 = D1 ⊕ D3 ⊕ D4 ⊕ D6 ⊕ D7**
- **C3 = D2 ⊕ D3 ⊕ D4 ⊕ D8**
- **C4 = D5 ⊕ D6 ⊕ D7 ⊕ D8**

(⊕ = เครื่องหมาย XOR วงกลมบวก)

---

---

## Slide 71: Example of Overlapped Parity
• Data sent is 1110 0001 and transmitted check bits
 are 1110
• Assume received data is: 01100001
• Received check bits are: 1110
• Recomputed check bits are: 0010
• Syndrome 11000010 = 1100

---

## Slide 72: Applying Syndrome  *(visual)*
Syndrome 1100 detects D8 as faulty

**รายละเอียดจากภาพ (vision):**

**Title:** Applying Syndrome

**Table / bit layout:** เหมือน Slide 68/70 โดยคอลัมน์ **12** ถูกกรอบสี่เหลี่ยมสีแดงล้อมรอบทั้ง 4 แถว

- แถวหัว: **12  11  10  9  8  7  6  5  4  3  2  1** — ป้าย **Bit Position**

| row | 12 | 11 | 10 | 9 | 8 | 7 | 6 | 5 | 4 | 3 | 2 | 1 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | 0 | 1 | 0 | 1 | 0 | 1 | 0 | 1 | 0 | 1 | 0 | 1 |
| 2 | 0 | 1 | 1 | 0 | 0 | 1 | 1 | 0 | 0 | 1 | 1 | 0 |
| 3 | 1 | 0 | 0 | 0 | 0 | 1 | 1 | 1 | 1 | 0 | 0 | 0 |
| 4 | 1 | 1 | 1 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |

- ป้าย **Check Bit**: **C4** (คอลัมน์ 8), **C3** (คอลัมน์ 4), **C2** (คอลัมน์ 2), **C1** (คอลัมน์ 1)
- ป้าย **Data Bit**: **D8 D7 D6 D5** (12,11,10,9), **D4 D3 D2** (7,6,5), **D1** (3)

**ข้อความสรุป (ด้านล่าง, ตัวหนา):**
- **Syndrome 1100 detects D8 as faulty** (หมายเลข **1100** เน้นสีแดง)
- หมายเหตุ: ค่าสี่บิตในคอลัมน์ 12 (แถวบนลงล่าง) = 0, 0, 1, 1 ⇒ อ่านจากบนลงล่างเป็น **1100** (D8, D7, D6, D5)

---

---

## Slide 73: Check yourself 5
• ECC using Venn Diagram

 A B A B

 1 1

 1 1
 1 0 1X 0 0

 C C

---

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

---

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

---

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

---

## Slide 77: Checksum Code Example
• 16 bits block is to be sent using 8 bits checksum
• 10101001 00111001
 Addition 10101001
 00111001
 Sum 11100010
 Checksum 00011101 (complement)
• The pattern sent is 10101001 00111001 00011101

• How about 10101001 00111001 11001100 00011001?

---

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

---

## Slide 79: Arithmetic weight errors  *(visual)*
errornous carry of 1

• Arithmetic weight errors: Minimum number of signed powers of 2 that
 must be added to the correct value to turn it into the erroneous result
 (contrast with Hamming weight of an error)

**รายละเอียดจากภาพ (vision):**

**Title:** Arithmetic weight errors

**Computation (ด้านบน):**
- **Unsigned addition**

```
  0010 0111 0010 0001
+ 0101 1000 1101 0011
----------------------
  0111 1111 1111 0100   ← Correct sum
  1000 0000 0000 0100   ← Erroneous sum
```

- กล่องคำอธิบายสีเขียว (ด้านขวา): **How a single carry error can lead to an arbitrary number of bit-errors (inversions)**
- กล่องสีน้ำเงินระบุ (ตัวแดง): **errornous carry of 1** (มีเส้นชี้ไปยังตำแหน่งบิตใน erroneous sum)

**Definition text (ตัวหนา/เอียง):**
- ***Arithmetic weight errors:*** Minimum number of signed powers of 2 that must be added to the correct value to turn it into the erroneous result (contrast with Hamming weight of an error)

**Example 1 (ด้านล่างซ้าย):**
```
Example 1
__________
0111 1111 1111 0100
1000 0000 0000 0100    (มีเส้นแบ่งแนวตั้ง | ระหว่างบิตก่อนหลักสุดท้าย)
16 = 2⁴
0000 0000 0001 0000
1
Single, positive
```

**Example 2 (ด้านล่างขวา):**
```
Example 2
__________
1101 1111 1111 0100
0110 0000 0000 0100
−32752 = −2¹⁵ + 2⁴
‾1000 0000 0001 0000
2
Double, negative
```

---

---

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

---

## Slide 81: Residue Code  *(visual)*
• If 𝑀𝑚𝑜𝑑𝐴= 0, then
 𝑋∗𝑌𝑚𝑜𝑑𝑀𝑚𝑜𝑑𝐴= 𝑋𝑚𝑜𝑑𝐴∗𝑌𝑚𝑜𝑑𝐴 𝑚𝑜𝑑𝐴
• Preserve code after operation

 X
 Result 𝑋∗𝑌𝑚𝑜𝑑𝑀 Y

 𝑀𝑜𝑑𝐺𝑒𝑛𝑒𝑟𝑎𝑡𝑜𝑟

 XmodA Detection
 𝑋∗𝑌𝑚𝑜𝑑𝐴 𝐶𝑜𝑚𝑝𝑎𝑟𝑎𝑡𝑜𝑟 Signal YmodA

**รายละเอียดจากภาพ (vision):**

**Title:** Residue Code

**Bullet text:**
- If *M*mod*A* = 0, then
  |(X * Y)modM|modA = ((XmodA) * (YmodA))modA
- *Preserve code* after operation

**Diagram (block diagram):**
- ด้านซ้าย: อินพุต **X** และ **Y** เข้ากล่อง **(X * Y)modM**
- เอาต์พุตจากกล่องนี้ไปทางขวาเป็น **Result** (เส้นตรง)
- จากเส้น Result มีการแยกสัญญาณลงเข้าสู่กล่อง **Mod Generator**
- จาก Mod Generator ลงเข้าสู่กล่อง **Comparator**
- ด้านซ้ายล่าง: อินพุต **XmodA** และ **YmodA** เข้ากล่อง **(X * Y)modA** → เอาต์พุตเข้าสู่กล่อง **Comparator**
- จาก Comparator มีลูกศรไปทางขวาเป็น **Detection Signal**

---

---

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

---

## Slide 83: Low-Cost Residue Code
• Complex Hardware of 𝑋𝑚𝑜𝑑𝐴
• If 𝐴= 2𝑏−1, then
 𝑛−1
 𝑋𝑚𝑜𝑑2𝑏−1 = ෍ 𝑋𝑖𝑚𝑜𝑑(2𝑏−1)
 𝑖=0
• Use b bit End-around carry Adder
ex. 𝑏= 3, 𝐴= 7,and 𝑋= 110100011

 𝑋𝑚𝑜𝑑7 = 419 𝑚𝑜𝑑7 = 110 + 100 + 011 = 110 = 6

---

## Slide 84: Arithmetic on Residue-coded operands  *(visual)*
• Add/subtract: Data and check parts are handled separately
 (x, C(x)) ± (y, C(y)) = (x±y, (C(x) ±C(y)) mod A)
• Multiply:
 (a, C(a)) × (x, C(x)) = (a×x, (C(a)×C(x)) mod A)
• Divide/square-root: difficult

**รายละเอียดจากภาพ (vision):**

**Title:** Arithmetic on Residue-coded operands

**Bullet text:**
- *Add/subtract:* Data and check parts are handled separately
  (x, C(x)) ± (y, C(y)) = (x±y, (C(x) ± C(y)) mod A)
- *Multiply:*
  (a, C(a)) × (x, C(x)) = (a×x, (C(a)×C(x)) mod A)
- *Divide/square-root:* difficult

**Diagram (block diagram):**
- อินพุต **x** และ **C(x)** (ด้านซ้ายบน) เข้ากล่อง **Main Arithmetic Processor**
- อินพุต **y** และ **C(y)** (ด้านซ้ายล่าง) ก็เข้าสู่ Main Arithmetic Processor เช่นกัน (และแยกเข้าสู่ Check Processor ด้านล่าง)
- เอาต์พุตจาก Main Arithmetic Processor ไปทางขวาเป็น **z** และ **C(z)**
- มีการแยกสัญญาณ (จากเส้น z) ลงเข้าสู่กล่อง **mod A**
- อินพุต y, C(y) เข้ากล่อง **Check Processor** (ด้านล่าง)
- เอาต์พุตของ Check Processor และของ mod A เข้าสู่ **Compare** (วงรี)
- จาก Compare มีลูกศรลงเป็น **Error Indicator**
- กล่องคำอธิบายสีเขียว (ด้านขวาล่าง): **Arithmetic processor with residue checking**

---

---

## Slide 85: Unordered Code
• A Code in which no codeword is covered by any
 other codeword
• Unidirectional error cannot transform one codeword
 to another codeword

• 𝑋(𝑥1, 𝑥2, … , 𝑥𝑘) covers 𝑌(𝑦1, 𝑦2, … , 𝑦𝑘) is 𝑋𝑌
• 𝑋= 101010 and 𝑌= 101000 then 𝑋𝑌
• If 𝑋𝑌, then ℎ(𝑌, 𝑋) = 0
• If 𝑋≱𝑌and 𝑌≱𝑋, then 𝑋and 𝑌are Unordered

---

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

---

## Slide 87: Berger Code
• Separable Code which corresponding to the number
 of 1s in Data bits, and appending the bit-by-bit
 complement binary Check bits
• Can detect all unidirectional errors
• 𝑘Data bits wt 𝑐check bits of 𝑛bits Berger code:
 𝑐= 𝑙𝑜𝑔2(𝑘+ 1) and 𝑛= 𝑘+ 𝑐

ex. 𝑘= 0101000 = 2 1𝑠, 𝑐= 010 = 101

 𝑋= 0101000101

---

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

---

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

**รายละเอียดจากภาพ (vision):**

**Title:** Dual Rail Code

**Bullet text:**
- **1-of-2 Code**
  {0,1} ⇒ {01,10}
- **Easy Implementation** (Encoder/Decoder)
- *Preserve code* after operation
- *Non-Inverter Circuit*

**Circuit/Logic diagrams (ทางขวา เป็นคู่บิต x, x' → z, z'):**

แถวที่ 1 — Buffer/Wire:
- `x —— z`  คู่กับ  `x —— z` / `x' —— z'`
- แสดงได้ว่า: `x ——— z` และ `x' ——— z'` (เส้นตรง ไม่กลับค่า)

แถวที่ 2 — Inverter:
- สัญลักษณ์ NOT gate (triangle + วงกลม): `x →(NOT)→ z`
- คู่ dual: `x —— z`, `x' —— z'` แบบไขว้ (เส้นตัดกัน – crossover)

แถวที่ 3 — AND gate:
- `x, y →(AND)→ z` (สัญลักษณ์ D-shape)
- ลูกศรหนา (⇒) ไปยังฝั่ง dual:
  - AND gate: `x, y → z`
  - gate รูปโค้ง (dual): `x', y' → z'`

แถวที่ 4 — OR gate:
- `x, y →(OR)→ z`
- ฝั่ง dual:
  - `x, y', y → z` (gate อีกชนิด)
  - AND gate: `x', y' → z'`

(แต่ละ gate ทางซ้ายเป็นแบบ single-rail, ทางขวาเป็นคู่ dual-rail โดยใช้ทั้ง x/x' และ y/y' และสะท้อนเป็น z/z')

---

---

## Slide 90: Dual Rail Code example  *(visual)*
𝐹= ത𝑎𝑏+ 𝑏ҧ𝑐+ 𝑎𝑐

ത𝐹= 𝑎+ ത𝑏 ത𝑏+ 𝑐 ത𝑎+ ҧ𝑐

**รายละเอียดจากภาพ (vision):**

**Title:** Dual Rail Code example

**Formulas:**
- **F = āb + bč + ac**
- **F̄ = (a + b̄)(b̄ + c)(ā + č)**

**Circuit diagrams:**
- วงบน (สำหรับ F): อินพุต **ā, b** → AND gate, **č** (แยกไปที่ AND ตัวที่สองด้วย), **a, c** → AND gates หลายตัว แล้วรวมกันด้วย OR gate → เอาต์พุต **F**
  - อินพุตที่แสดง: ā, b, č, a, c
- วงล่าง (สำหรับ F̄): อินพุต **a, b̄** → OR gate, **c, ā, č** → OR gates หลายตัว แล้วรวมกันด้วย AND gate → เอาต์พุต **F̄**
  - อินพุตที่แสดง: a, b̄, c, ā, č

(ทั้งสองวงวาดด้วยเส้นสีฟ้า/น้ำเงิน, gate รูปทรง D และโค้ง)

---

---

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

**รายละเอียดจากภาพ (vision):**

**Title:** Applications: Error detection in UPC-A

**Bullet text:**
- **Checksum codes:** Given a data vector x₁, x₂, . . . , xₙ, encode the data by attaching the checksum xₙ₊₁ to the end
  (Σ_{j=1 to n+1} wⱼxⱼ = 0 mod A)
  (Weight vector wⱼ elements are predetermined constants)
- **Capabilities:** All single-digit errors; Most transposition errors
- **Example:** For the UPC-A checksum scheme,
- w = 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1; A= 10
- **Checking:** Verify that weighted mod-10 sum of all 12 digits is 0
- **12-digit UPC-A universal product code:**
  Sum odd indexed digits: **0+6+0+2+1+5 = 14**
  Multiply by 3: **14×3 = 42**
  Add even-indexed digits: **42+3+0+0+9+4 = 58**
  Compute check digit: **60 −58 = 2**

**Images (ด้านขวา):**
- รูปบาร์โค้ด UPC-A พร้อมเลข **0 36000 29145 2** (ด้านล่างมีหมายเลขตำแหน่ง 1 2 3 4 5 6 7 8 9 10 11) โดยหลักสุดท้าย **2** ถูกวงกลมสีแดงล้อม
- มีเส้น/กรอบสีเขียวครอบบางแท่งของบาร์โค้ด
- มุมขวาบน: ไอคอนแสดงเลข **4 ▶ 1011100 ▶** พร้อมภาพแท่งบาร์โค้ดย่อ (แสดงการเข้ารหัส 7 บิตต่อหนึ่งหลัก)
- ข้อความ: **Bar code uses 7 bits per digit, with different encodings on the right and left halves and different parities at various positions**

---

---

## Slide 92: Applications: JPEG Huffman Coding  *(visual)*
• Huffman codes are widely used and very effective technique
 for compression data; saving of 20% to 90%
• JPEG compression standard

 Original image Reconstructed image Reconstructed image
 under Huffman code table error wt error detection/correction

**รายละเอียดจากภาพ (vision):**

**Title:** Applications: JPEG Huffman Coding

**Bullet text:**
- *Huffman codes* are widely used and very effective technique for compression data; saving of **20% to 90%**
- JPEG compression standard

**Images (ด้านล่าง 3 ภาพ เรียงซ้าย-ขวา — ภาพนกกระยางขาว (egret) บนพื้นฟ้า):**
- ภาพที่ 1: **Original image** (ภาพต้นฉบับ คมชัด)
- ภาพที่ 2: **Reconstructed image under Huffman code table error** (ภาพมีสัญญาณรบกวน/แตกเป็นบล็อก)
- ภาพที่ 3: **Reconstructed image wt error detection/correction** (ภาพถูกแก้ไข กลับมาคมชัด)

---

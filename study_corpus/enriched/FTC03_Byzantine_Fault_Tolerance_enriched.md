# FTC03_Byzantine_Fault_Tolerance — Enriched (slide text + vision of visual slides)

> Text = exact extraction from the born-digital PDF. For `visual` slides, a faithful description of the figure/table/formula is added under **รายละเอียดจากภาพ**. Vision descriptions are model-produced and marked as such.

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

**รายละเอียดจากภาพ (vision):**

**Title:** Home Exercise: Reliability

**รูปภาพ/แผนภาพ:**

**PP scheme** (มุมซ้ายบน)
- กล่องสี่เหลี่ยมเรียงกันเป็นตาราง: คอลัมน์ซ้ายคือ A1, A2, A3 ; คอลัมน์กลางมี B1, B2, B3 ; คอลัมน์ขวาคือ C1, C2, C3
- การเชื่อมต่อ (เส้น):
  - A1 ต่อกับ B1 (B1 ต่อกับ C1)
  - A2 ต่อกับ B2
  - A3 ต่อกับ B3 (เส้นเชื่อม A3–B3 ถูกวงไว้ด้วยวงรีสีน้ำเงิน)
- วงรีสีแดง (mark) ครอบกลุ่ม: {A1, A2} , {C2, C3}
- วงรีสีน้ำเงิน (mark) ครอบกลุ่ม: {B1, C1} , {A3, B3}
- มีเส้นแนวนอนลากผ่านกลางไปทางขวา (เส้นทางความเชื่อมโยงระหว่างชั้น)

**Bridge** (มุมซ้ายล่าง)
- ป้ายกำกับสีแดง: R1, R2 (บน), R3, R4 (ล่าง)
- บล็อกกลาง: R1 = A1∪A2 ; R2 = B1∩C1
- บล็อกกลาง (ระดับกลาง): B2
- บล็อกล่าง: R3 = A3∩B3 ; R4 = C2∪C3
- โครงข่ายเชื่อมกันเป็นลูป (Bridge network)

**ตาราง (ด้านขวา):** คอลัมน์หัวตาราง R1, R2, **B2** (ไฮไลต์สีเหลือง), R3, R4, **Sys** (สีส้ม), **Probability** (ตัวหนาสีแดง)

| R1 | R2 | B2 | R3 | R4 | Sys | Probability |
|----|----|----|----|----|-----|-------------|
| 1 | 1 | 1 | 1 | 1 | 1 | R1R2 |
| 1 | 1 | 1 | 1 | 0 | 1 | R1R2 |
| - | - | - | - | - | - | |
| 1 | 1 | 0 | 0 | 0 | 1 | R1R2 |
| 1 | 0 | 1 | 1 | 1 | 1 | R1R2'B2R3R4 |
| 1 | 0 | 1 | 1 | 0 | 0 | 0 |
| 1 | 0 | 1 | 0 | 1 | 1 | R1R2'B2R3'R4 |
| 1 | 0 | 1 | 0 | 0 | 0 | 0 |
| - | - | - | - | - | - | |
| 0 | 0 | 0 | 0 | 0 | 0 | 0 |

**สูตร (มุมล่างกลาง):**
- R1 = (1-(1-R_A)^2)
- R2 = R_B·R_C
- R3 = R_A·R_B
- R4 = (1-(1-R_C)^2)

**กล่องกรอบสีแดง (มุมล่างขวา):**
- R_bridge = R1R2 + R1R2'B2R4 + R1'R2B2R3 + R1'R2B2'R3R4 + R1'R2'R3R4

(เลขมุมล่างขวา: 1)

---

---

## Slide 2: Byzantine Fault Tolerance
(Fault Tolerance in Distributed Systems)

 2110473 Fault Tolerant Computing

 Several sources

---

## Slide 3: Contents
• Process Groups
• Fault Tolerance in Process Groups
• Byzantine Generals Problem
• Oral Message Algorithm
• Blockchain
• Reliable Client-Server Communication

---

## Slide 4: Process Groups  *(visual)*
➢All members of a group receive a message sent to the group
 ➢If one process fails, others can take over
 ➢Can be dynamic; processes can have multiple memberships

(a) Communication in a flat group: No Single Point-of-Failure, Complicated Decision Making
(b) Communication in a hierarchical group: Single Point-of-Failure, Quick Decision Making

**รายละเอียดจากภาพ (vision):**

**Title:** Process Groups

- ➢ All members of a group receive a message sent to the group
- ➢ If one process fails, others can take over
- ➢ Can be dynamic; processes can have multiple memberships

**แผนภาพ (a) – Flat group:**
- วงกลมเส้นประล้อมรอบ (แทน group) มี label "Flat group" ชี้ด้วยลูกศร
- ภายในมี node วงกลม 5 จุด เชื่อมกันแบบ fully-connected (ทุกคู่เชื่อมกันเป็นโครงข่ายหนาแน่น)
- กำกับด้านล่าง "(a)"

**แผนภาพ (b) – Hierarchical group:**
- วงกลมเส้นประล้อมรอบ มี label "Hierarchical group" ชี้เข้าด้วยลูกศร
- มี node ตรงกลางด้านบน 1 จุด มี label "Coordinator" ชี้เข้าด้วยลูกศร
- Node ล่าง 5 จุด กระจายอยู่ด้านล่าง มี label "Worker" ชี้เข้าด้วยลูกศรไปที่ worker ด้านขวา
- เชื่อมจาก Coordinator ลงมาที่ Worker ทุกตัว (star/hierarchy)
- กำกับด้านล่าง "(b)"

**คำบรรยายใต้ภาพ:**
- (a) Communication in a **flat group**: *No Single Point-of-Failure, Complicated Decision Making* (ข้อความสีน้ำเงิน)
- (b) Communication in a **hierarchical group**: *Single Point-of-Failure, Quick Decision Making* (ข้อความสีแดง)

(เลขมุมล่างขวา: 4)

---

---

## Slide 5: Process Group Architecture  *(visual)*
Central Authority Consensus Protocol
 (Agreement)

**รายละเอียดจากภาพ (vision):**

**Title:** Process Group Architecture

**แผนภาพ 3 แบบ:**
- **CENTRALIZED (A):** โครงข่ายที่มี node ศูนย์กลางหนาแน่นอยู่ตรงกลาง มีเส้นกระจายจาก node กลางไปยัง node รอบนอกจำนวนมาก (star-like) มี label ชี้ว่า "Link" (ชี้ไปที่เส้น) และ "Station" (ชี้ไปที่จุด node)
- **DECENTRALIZED (B):** โครงข่ายที่มีหลายศูนย์ (หลาย hub) แต่ละ hub มีเส้นกระจายออกไป แล้วเชื่อมถึงกันไม่สมบูรณ์
- **DISTRIBUTED (C):** โครงข่ายตาข่าย (mesh) node จำนวนมากเชื่อมต่อกันเป็นตารางสม่ำเสมอ ไม่มีศูนย์กลาง

**แถบล่าง:**
- ข้อความซ้าย: "Central Authority"
- ลูกศรสีน้ำเงินขนาดใหญ่ชี้ไปทางขวา
- ข้อความขวา (สีแดง): "Consensus Protocol (Agreement)"

(เลขมุมล่างขวา: 5)

---

---

## Slide 6: Centralized & Distributed Ledger  *(visual)*
6

**รายละเอียดจากภาพ (vision):**

**Title:** Centralized & Distributed Ledger

**แผนภาพซ้าย – Centralised Ledger:**
- มีรูปตึก/ธนาคาร (bank) 4 หลัง อยู่รอบมุม (ซ้ายบน, ขวาบน, ซ้ายล่าง, ขวาล่าง)
- ตรงกลางมีกล่องข้อความ "Clearing House" (ตัวอักษรขาวบนพื้นน้ำเงินเข้ม รูปทรงบ้าน/หลังคา)
- ลูกศรสีเหลืองหนา: 4 เส้นจาก bank ทั้ง 4 ชี้เข้าหา "Clearing House" (ในทิศเข้าหาศูนย์กลาง) และมีลูกศรจาก Clearing House ชี้ลงไปที่เอกสาร (ledger) ข้างล่าง
- ด้านล่างมีไอคอนเอกสาร/ledger 1 อัน กำกับ "Centralised Ledger"

**แผนภาพขวา – Distributed Ledger:**
- มีรูปตึก/ธนาคาร 4 หลัง อยู่สี่มุม
- แต่ละมุมมีไอคอนเอกสาร/ledger อยู่ข้าง ๆ และมีลูกศรสีเหลืองเชื่อมกันเป็นโครงข่ายระหว่างมุมทั้ง 4 (เชื่อมทุกคู่แบบ peer-to-peer) รวมทั้งเชื่อมไปยัง ledger ของแต่ละโหนด
- มีเส้นทแยงเชื่อมระหว่างมุม 2 เส้น (กากบาทตรงกลาง) และเส้นแนวนอนด้านบน/ล่างเชื่อมมุมซ้าย-ขวา
- กำกับด้านล่างขวา "Distributed Ledger"

(เลขมุมล่างขวา: 6)

---

---

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

---

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

---

## Slide 9: Byzantine Generals Problem  *(visual)*
9

**รายละเอียดจากภาพ (vision):**

**Title:** Byzantine Generals Problem

**แผนภาพ:**
- วงกลม 5 วง แต่ละวงมีข้อความ:
  - "General 1 and Army" (บนซ้าย)
  - "General 2 and Army" (บนขวา)
  - "General 4 and Army" (ซ้ายล่าง)
  - "Enemy Camp" (กลาง ระหว่าง General 1/General 2 กับ General 4)
  - "General 3 and Army (traitor)" (ขวาล่าง) โดยคำว่า "traitor" อยู่ในวงเล็บและเป็นตัวหนา
- ลูกศร: จาก General 3 ชี้ขึ้นไปยัง General 2 มี label กำกับว่า "Attack" (มี Double quote " คร่อมข้อความ) — ทิศทางชี้ขึ้น (จาก General 3 ไป General 2)
- ลูกศร: จาก General 3 ชี้ไปทางซ้ายไปยัง General 4 มี label กำกับว่า "Don't attack" (มี Double quote คร่อมข้อความ) — ทิศทางชี้ไปทางซ้าย

**ข้อความด้านขวา:**
- Goal: Reach a common decision to attack at dawn or not
- Problems:
  1) Messengers could be caught so messages might not get delivered
  2) Generals might be traitors and send messages to create confusion

(เลขมุมล่างขวา: 9)

---

---

## Slide 10: Agreement: Byzantine Generals Problem (1)  *(visual)*
How does a process group deal with a faulty member?

❑The "Byzantine Generals Problem" for 3 loyal generals and 1 traitor.
a) The generals announce their troop strengths to the other members of the group by
 sending a message.
b) The vectors that each general assembles based on (a), each general knows their own
 strength. They then send their vectors to all the other generals.
c) The vectors that each general receives in step 3. It is clear to all that General 3 is the
 traitor. In each 'column', the majority value is assumed to be correct.

**รายละเอียดจากภาพ (vision):**

**Title:** Agreement: Byzantine Generals Problem (1)

**ข้อความใต้ชื่อเรื่อง:** How does a process group deal with a faulty member?

**แผนภาพ (a):** โครงข่าย node 4 จุด (วงกลม) หมายเลข 1, 2, 3, 4
- Node "3" ถูกแรเงาสีเทา (shaded) มี label "Faulty process" ชี้เข้าด้วยลูกศรจากด้านซ้าย
- ลูกศรและตัวเลขบนเส้นเชื่อม (ทิศทางต่าง ๆ ระหว่าง node):
  - ระหว่าง 1 และ 2: ตัวเลข 2 และ 1
  - ระหว่าง 1 และ 3: ตัวเลข 1 และ x
  - ระหว่าง 2 และ 3: ตัวเลข 2 และ 4
  - ระหว่าง 1 และ 4: ตัวเลข 2 (บริเวณกลาง) และ y
  - ระหว่าง 2 และ 4: ตัวเลข 2 และ 4
  - ระหว่าง 3 และ 4: ตัวเลข 4 และ z
- กำกับด้านล่าง "(a)"

**รายการ (b):** (กำกับ "(b)" ด้านล่าง)
- 1 Got(1, 2, x, 4)
- 2 Got(1, 2, y, 4)
- 3 Got(1, 2, 3, 4)
- 4 Got(1, 2, z, 4)

**ตาราง (c):** (กำกับ "(c)" ด้านล่าง)

| 1 Got | 2 Got | 4 Got |
|-------|-------|-------|
| (1, 2, y, 4) | (1, 2, x, 4) | (1, 2, x, 4) |
| (a, b, c, d) | (e, f, g, h) | (1, 2, y, 4) |
| (1, 2, z, 4) | (1, 2, z, 4) | (i, j, k, l) |

**คำอธิบายด้านล่าง:**
- ❑ The "**Byzantine Generals Problem**" for 3 loyal generals and 1 traitor. (ชื่อปัญหาเป็นตัวหนาสีแดง)
- a) The generals announce their troop strengths to the other members of the group by sending a message.
- b) The vectors that each general assembles based on (a), each general knows their own strength. They then send their vectors to all the other generals.
- c) The vectors that each general receives in step 3. It is clear to all that General 3 is the traitor. In each 'column', the majority value is assumed to be correct.

(เลขมุมล่างขวา: 10)

---

---

## Slide 11: Agreement: Byzantine Generals Problem (2)  *(visual)*
Warning: the algorithm does not always work! ⇒Two-Army Problem

• The same algorithm as in previous slide, except now with 2 loyal generals
 and 1 traitor. Note: It is no longer possible to determine the majority value
 in each column, and the algorithm has failed to produce agreement.
• It has been shown that for the algorithm to work properly, more than two-
 thirds of the processes have to be working correctly. That is: if there are M
 faulty processes, we need 2M + 1 functioning processes to reach agreement.

**รายละเอียดจากภาพ (vision):**

**Title:** Agreement: Byzantine Generals Problem (2)

**ข้อความ Warning (ตัวหนาสีแดง "Warning"):** Warning: the algorithm does not always work! ⇒ Two-Army Problem

**แผนภาพ (a):** โครงข่าย node 3 จุด หมายเลข 1, 2, 3
- Node "3" ถูกแรเงาสีเทา มี label "Faulty process" ชี้เข้าด้วยลูกศรจากด้านซ้าย
- ลูกศรและตัวเลขบนเส้นเชื่อม:
  - ระหว่าง 1 และ 3: ตัวเลข 1 และ x
  - ระหว่าง 1 และ 2: ตัวเลข 2 และ 1
  - ระหว่าง 2 และ 3: ตัวเลข 2 และ y (มีเส้นโค้งจาก 3 ไป 2)
- กำกับด้านล่าง "(a)"

**รายการ (b):** (กำกับ "(b)" ด้านล่าง)
- 1 Got(1, 2, x)
- 2 Got(1, 2, y)
- 3 Got(1, 2, 3)

**ตาราง (c):** (กำกับ "(c)" ด้านล่าง)

| 1 Got | 2 Got |
|-------|-------|
| (1, 2, y) | (1, 2, x) |
| (a, b, c) | (d, e, f) |

**คำอธิบายด้านล่าง:**
- • The same algorithm as in previous slide, except now with 2 loyal generals and 1 traitor. Note: It is no longer possible to determine the majority value in each column, and the algorithm has failed to produce agreement.
- • It has been shown that for the algorithm to work properly, *more* than two-thirds of the processes have to be working correctly. That is: if there are **M** faulty processes, we need **2M + 1** functioning processes to reach agreement. (ตัว "M" และ "2M + 1" เป็นสีแดง)

(เลขมุมล่างขวา: 11)

---

---

## Slide 12: Oral Messages
Byzantine Agreement (n nodes, m faults)
 - can be reached using Oral Messages,
 if n >= 3m+1

Assumptions:
• Every message is delivered correctly
• Receiver knows who sent message
• Absence of message can be detected

---

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

---

## Slide 14: Example: Bad Lieutenant  *(visual)*
Scenario: m=1, n=4, traitors=L3

**รายละเอียดจากภาพ (vision):**

**Title:** Example: Bad Lieutenant

**ข้อความใต้ชื่อเรื่อง:** Scenario: m=1, n=4, traitors=L3

**แผนภาพ OM(1):**
- Node บนสุดคือ "C" (สีน้ำเงิน) มีลูกศรยิงลงไปยัง node L1, L2, L3
- ลูกศรจาก C ไป L1, L2, L3 มี label "A" ทุกเส้น
- Node ล่าง: "L1" (น้ำเงิน), "L2" (น้ำเงิน), "L3" (สีแดง = faulty)
- ป้ายกำกับซ้าย: OM(1):

**แผนภาพ OM(0):???**
- Node "C" (น้ำเงิน) อยู่ด้านบน
- Node ล่าง: "L1" (น้ำเงิน), "L2" (น้ำเงิน), "L3" (แดง) เชื่อมกันแบบทุกคู่
- เส้นเชื่อมสีดำ: ระหว่าง L1–L2 มี label "A"; ระหว่าง L2–L3 ; ระหว่าง L1–L3
- เส้นเชื่อมสีแดง: จาก L3 ไป L2 มี label "R"; จาก L3 ไป L1 (เส้นโค้งด้านล่าง) มี label "R"; และมี label "A" ตรงเส้นล่าง
- ป้ายกำกับซ้าย: OM(0):???

**ข้อความล่าง:**
- Decision??   L1 = m (A, A, R); L2 = m (A, A, R); Both attack!
- ป้ายกำกับซ้าย: "Decision??"
- ข้อความทั้งหมดเป็นสีฟ้า/น้ำเงิน

(เลขมุมล่างขวา: 14)

---

---

## Slide 15: Example: Bad Commander  *(visual)*
Scenario: m=1, n=4, traitors=C

**รายละเอียดจากภาพ (vision):**

**Title:** Example: Bad Commander

**ข้อความใต้ชื่อเรื่อง:** Scenario: m=1, n=4, traitors=C

**แผนภาพ OM(1):**
- Node บนสุดคือ "C" (สีแดง = faulty)
- ลูกศรจาก C ไป L1, L2, L3: ไป L1 label "A", ไป L2 label "R", ไป L3 label "A"
- Node ล่าง: "L1" (น้ำเงิน), "L2" (น้ำเงิน), "L3" (น้ำเงิน)
- ป้ายกำกับซ้าย: OM(1):

**แผนภาพ OM(0):???**
- Node "C" (น้ำเงิน) อยู่ด้านบน
- Node ล่าง: "L1", "L2", "L3" (ทั้งหมดสีน้ำเงิน) เชื่อมกันทุกคู่
- เส้นเชื่อมมี label "A" และ "R" สลับกัน (บน: A ; ระหว่าง L2–L3: R ; ระหว่าง L2–L1: A ; ล่าง/โค้ง: R และ A)
- ป้ายกำกับซ้าย: OM(0):???

**ข้อความล่าง:**
- Decision??  L1=m(A, R, A); L2=m(A, R, A); L3=m(A,R,A); Attack!
- ป้ายกำกับซ้าย: "Decision??"
- ข้อความเป็นสีน้ำเงิน

(เลขมุมล่างขวา: 15)

---

---

## Slide 16: Bigger BFT (Bad Lieutenants )  *(visual)*
Scenario: m=2, n=7, traitors=L5,L6

Decision??

 https://github.com/AnantJoshiCZ/Byzantine
 https://github.com/AnantJoshiCZ/Byzantine

**รายละเอียดจากภาพ (vision):**

**Title:** Bigger BFT (Bad Lieutenants )

**ข้อความใต้ชื่อเรื่อง:** Scenario: m=2, n=7, traitors=L5,L6

**แผนภาพชั้นบน:**
- Node "C" (น้ำเงิน) อยู่ด้านบน ตรงกลาง
- ลูกศรจาก C ยิงลงไปยัง L1, L2, L3, L4, L5, L6 ทุกเส้นมี label "A" (มี label A หลายตัวตามแต่ละเส้น)
- Node L1 (น้ำเงิน), L2 (น้ำเงิน), L3 (น้ำเงิน), L4 (น้ำเงิน), L5 (แดง = faulty), L6 (แดง = faulty)

**แผนภาพชั้นล่าง:** หัวข้อ "Messages?"
- Node: L1 (น้ำเงิน), L2 (น้ำเงิน), L3 (น้ำเงิน), L4 (น้ำเงิน), L5 (แดง), L6 (แดง)
- ใต้แต่ละ node มีลูกศรชี้ลง พร้อม label:
  - L1 → "A", L2 → "A", L3 → "A", L4 → "A", L5 → "R" (แดง), L6 → "R" (แดง)

**ข้อความล่าง:**
- Decision?? (ตัวหนาสีแดง)
- ลิงก์: https://github.com/AnantloshiCZ/Byzantine (ขีดเส้นใต้ สีน้ำเงิน)

(เลขมุมล่างขวา: 16)

---

---

## Slide 17: Bigger BFT (Bad Commander+ )  *(visual)*
17

**รายละเอียดจากภาพ (vision):**

**Title:** Bigger BFT (Bad Commander+ )

**ข้อความใต้ชื่อเรื่อง:**
- • Scenario: m=2, n=7, traitors=C, L6

**แผนภาพชั้นบน:**
- Node "C" (สีแดง = faulty) อยู่ด้านบน
- ลูกศรจาก C ไปยัง L1, L2, L3, L4, L5, L6 โดยมี label: ไป L1 → "A" ; ไป L2 → "R" ; ไป L3 → "A" ; ไป L4 → "R" ; ไป L5 → "A" ; ไป L6 → "X" (เครื่องหมายกากบาท/ไม่ส่ง)
- Node L1–L5 สีน้ำเงิน ; L6 สีแดง (faulty)

**แผนภาพชั้นล่าง:** หัวข้อ "Messages?"
- Node: L1, L2, L3, L4, L5 (น้ำเงิน), L6 (แดง)
- ใต้แต่ละ node มีลูกศรชี้ลง พร้อม label:
  - L1 → "A", L2 → "R", L3 → "A", L4 → "R", L5 → "A"
  - L6 → "A,R,A,R,A" (ไฮไลต์ด้วยกรอบสีส้ม/ข้อความแดง)

**ข้อความล่างซ้าย:**
- Decision???

(เลขมุมล่างขวา: 17)

---

---

## Slide 18: Decision with Bad Commander+  *(visual)*
18

**รายละเอียดจากภาพ (vision):**

**Title:** Decision with Bad Commander+

**เนื้อหา (bullet list):**
- • L1: m(A,R,A,R,A,A) ==> Attack
- • L2: m(R,R,A,R,A,R) ==> Retreat
- • L3: m(A,R,A,R,A,A) ==> Attack
- • L4: m(R,R,A,R,A,R) ==> Retreat
- • L5: m(A,R,A,R,A,A) ==> Attack
- • Problem: All loyal lieutenants do NOT choose same action
  - – SO: need more communication – commander + cheater can tip majority

(เลขมุมล่างขวา: 18)

---

---

## Slide 19: Next Step of Algorithm  *(visual)*
19

**รายละเอียดจากภาพ (vision):**

**Title:** Next Step of Algorithm

**เนื้อหา:**
- • **Key: Verify that lieutenants tell each other the same thing** (ตัวหนา)
  - – Requires # rounds = m+1 (0 + m)
  - – OM(0): Msg from Lieut i of form: " L0 said v0, L1 said v1, etc…"
    - • At each level, get agreement on what the sender sends out, so cannot have some A some R
- • What messages does L1 receive in this example?
  - – OM(2): A (commander sends)
  - – OM(1):   2R, 3A, 4R, 5A, 6A (recv what cmdr sent from others)
  - – OM(0):   2{ 3A, 4R, 5A, 6R}  (2 sends all msgs heard in round 1)
  - –   3{2R,   4R, 5A, 6A}
  - –   4{2R, 3A,   5A, 6R}
  - –   5{2R, 3A, 4R,   6A}
  - –   6{ total confusion }
- • All see same messages in OM(0) from L1,2,3,4, and 5
  - – Uses majority for each other node – look down columns of matric in OM(0)
- • m(1A,2R,3A,4R,5A,–) ==> All attack
- • NOTE: # of messages: (n-1)(n-2)(n-3)…(n-m-1) messages for m traitors

(หมายเหตุ: บรรทัด OM(0) และบรรทัดต่อ ๆ มาเป็นข้อความ monospace ในสไลด์; คำว่า "matric" ปรากฏตามต้นฉบับ)
(เลขมุมล่างขวา: 19)

---

---

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

**รายละเอียดจากภาพ (vision):**

**Title:** Check Yourself

**โจทย์ (มีไฮไลต์สี):**
Imagine there are **1 loyal commander** (สีน้ำเงิน), **1 traitor** (สีแดง) lieutenant, and **4 loyal** (สีน้ำเงิน) lieutenants. Please provide a concrete example where **Oral Message algorithm** (สีเขียว) is used among these soldiers, yet the loyal lieutenants all **are able to follow** (สีแดง) the commander's command.
You need to briefly describe the process of **Oral Message algorithm** (สีเขียว) in your example.

**แผนภาพ:**
- Node กลาง (ellipse สีน้ำเงินเข้ม): "COMMANDER"
- Node ซ้าย (ellipse สีแดงอ่อน = faulty): "LIEUTENANT"
- Node ขวา (ellipse สีฟ้า = normal): "LIEUTENANT"
- ลูกศรจาก COMMANDER: ไปทางซ้ายไปยัง LIEUTENANT (สีแดง) label "A" ; ไปทางขวาไปยัง LIEUTENANT label "A"
- ลูกศรลงล่าง 3 เส้นจาก COMMANDER ไปยัง LIEUTENANT อีก 3 ตัว แต่ละเส้น label "A"
- ล่างซ้าย "LIEUTENANT", ล่างกลาง "LIEUTENANT", ล่างขวา "LIEUTENANT"

**คำบรรยายใต้ภาพ (ตัวเอียง):**
- - The red ellipse represents the faulty nodes, while the blue one for the normal nodes
- - The commander sends the "Attack" order to all lieutenants to which it connects.
- - When each lieutenant act as a commander, a loyal lieutenant sends the original order, "Attack", while the traitor sends "Retreat".

(เลขมุมล่างขวา: 20)

---

---

## Slide 21: Check Yourself - Solution (1/3)  *(visual)*
A A LIEUTENANT COMMANDER LIEUTENANT

 A A A

 LIEUTENANT LIEUTENANT LIEUTENANT

 A AOM(1) L C L
 A A A
 L L L

**รายละเอียดจากภาพ (vision):**

**Title:** Check Yourself – Solution (1/3)

**แผนภาพบน (เหมือน slide 20):**
- Node กลาง "COMMANDER" (สีน้ำเงินเข้ม); ซ้าย "LIEUTENANT" (ellipse สีแดง = faulty); ขวา "LIEUTENANT" (ฟ้า)
- ลูกศรจาก COMMANDER ไปยัง lieutenant: ซ้าย label "A", ขวา label "A"
- ลูกศรลงล่าง 3 เส้น label "A" ไปยัง LIEUTENANT 3 ตัวด้านล่าง (ซ้าย/กลาง/ขวา)

**แผนภาพล่าง:** ป้ายกำกับซ้าย "OM(1)"
- Node กลาง "C" (วงกลมสีน้ำเงินเข้ม)
- Node ซ้าย "L" (วงกลมสีแดงอ่อน = faulty) เชื่อมกับ C ด้วยลูกศร label "A" (ชี้ไปทางซ้าย)
- Node ขวา "L" (น้ำเงิน) เชื่อมกับ C ด้วยลูกศร label "A" (ชี้ไปทางขวา)
- Node ล่าง 3 ตัว "L" (น้ำเงิน) มีลูกศรจาก C ลงไป แต่ละเส้น label "A"
- ล่างซ้าย "L", ล่างกลาง "L", ล่างขวา "L"

(เลขมุมล่างขวา: 21)

---

---

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

**รายละเอียดจากภาพ (vision):**

**Title:** Check Yourself – Solution (2/3)

**แผนภาพ OM(1) (ด้านบน):**
- ป้ายกำกับซ้าย "OM(1)" และมีตัวอักษรสีแดง "L5" กำกับไว้ข้าง node ซ้าย (node ซ้ายสุดคือ faulty)
- Node กลาง "C" (น้ำเงินเข้ม)
- Node ซ้าย "L" (แดงอ่อน = faulty) — ลูกศรจาก C ชี้ไปทางซ้าย label "A"
- Node ขวา "L" (น้ำเงิน) — ลูกศรจาก C ชี้ไปทางขวา label "A"
- Node ล่าง 3 ตัว "L" — ลูกศรจาก C ลงไป label "A" ทุกเส้น

**แผนภาพ OM(0) (ด้านล่าง):** ป้ายกำกับซ้าย "OM(0)"
- กลุ่ม A (บนซ้าย): Node "C" (สีแดงอ่อน) เชื่อมออก: ไป "L" ขวา label "R" ; ลงไป "L" label "R" ; ไป "L" อีกตัว label "R" (ลูกศรออกจาก C หลายเส้น)
- กลุ่ม B (บนกลาง): Node "L" (แดงอ่อน) อยู่บน, ด้านล่างมี "C" (น้ำเงิน) และ "L" ; ลูกศรจาก C ขึ้นไป "L" label "A" ; จาก "L" (บนกลาง) ไป "L" ขวา label "A" ; จาก C ไป L label "A" ; จาก L ไป L label "A"
- กลุ่ม C (บนขวา): Node "L" (แดงอ่อน) อยู่บน ; Node "C" อยู่กลางขวา ; ลูกศรจาก C ไป "L" ซ้ายบน label "A", ไป "L" ขวา label "A", ไป "L" ซ้าย label "A"
- กลุ่ม D (ล่างซ้าย): Node "L" (แดงอ่อน) อยู่บน ; Node "C" อยู่ล่างขวา ; ลูกศรจาก C ไป "L" label "A", ไป "L" อีกตัว label "A"
- กลุ่ม E (ล่างกลาง): Node "L" (น้ำเงิน) อยู่บน ; Node "C" อยู่ล่าง ; ลูกศรจาก C ขึ้นไป "L" label "A"
- กลุ่ม F (ล่างขวา): Node "C" (น้ำเงิน) อยู่ขวา ; Node "L" (แดงอ่อน) อยู่บน ; Node อื่น ๆ "L" ; ลูกศรจาก C ไป "L" ซ้ายบน label "A", ลงไป "L" label "A", ไป "L" ล่าง label "A"

(เลขมุมล่างขวา: 22)

---

---

## Slide 23: Check Yourself - Solution (3/3)  *(visual)*
Lieute Value Frm Frm Frm Frm Frm Majority
 nant frm C L1 L2 L3 L4 L5 Vote
 L1 A - A A A R A
 L2 A A - A A R A
 L3 A A A - A R A
 L4 A A A A - R A
 L5 x x x x x - x

**รายละเอียดจากภาพ (vision):**

**Title:** Check Yourself – Solution (3/3)

**ตาราง:**

| Lieute nant | Value frm C | Frm L1 | Frm L2 | Frm L3 | Frm L4 | Frm L5 | Majority Vote |
|-------------|-------------|--------|--------|--------|--------|--------|---------------|
| L1 | A | - | A | A | A | R | A |
| L2 | A | A | - | A | A | R | A |
| L3 | A | A | A | - | A | R | A |
| L4 | A | A | A | A | - | R | A |
| L5 | x | x | x | x | x | - | x |

(หัวตาราง "Lieute nant" ถูกตัดคำในสไลด์ ; แถว L5 ทุกช่องเป็น "x" ยกเว้นคอลัมน์ Frm L5 = "-" และ Majority Vote = "x")
(เลขมุมล่างขวา: 23)

---

---

## Slide 24: Number of Messages
Number of Messages
 = (n-1)*(n-2)*…*(n-m-1)
 = O(nm)

 Exponential in number of Traitors!!

• Practical Byzantine Fault Tolerance
• Signed Message Solution

---

## Slide 25: Practical BFT  *(visual)*
- Client waits for m+1 replies from different replicas with
 same answer
- If primary is faulty, select new primary
- Many optimizations to reduce overhead

**รายละเอียดจากภาพ (vision):**

**Title:** Practical BFT

**แผนภาพ (time-sequence / message flow):**
- เส้นเวลาแนวนอน 5 เส้น มีป้ายกำกับด้านซ้าย: "C", "0", "1", "2", "3"
- เส้นประแนวตั้งแบ่งเฟส (phase) ตามหัวข้อด้านบน: "request", "pre-prepare", "prepare", "commit", "reply"
- มีเครื่องหมาย "X" อยู่ที่เส้นเวลาของ "3" ในช่วง request (แทนโหนดที่ fault/l่ม)
- ลูกศรระหว่างเส้นเวลาแสดงการส่งข้อความ:
  - request: C → 0
  - pre-prepare: 0 → 1, 0 → 2, 0 → 3
  - prepare: แลกเปลี่ยนกันระหว่าง 0,1,2,3 (ลูกศรหลายเส้นตัดกันระหว่างแถว 1,2,3 และ 0)
  - commit: แลกเปลี่ยนกันระหว่าง 0,1,2,3 อีกชุด (ลูกศรตัดกันหนาแน่น)
  - reply: จาก 0,1,2 ชี้กลับไปที่ C (มีลูกศรจาก 0,1,2 ขึ้นไปยัง C)

**ข้อความล่าง (bullet):**
- - Client waits for m+1 replies from different replicas with same answer
- - If primary is faulty, select new primary
- - Many optimizations to reduce overhead

(เลขมุมล่างขวา: 25)

---

---

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

---

## Slide 27: Proof of Work in Bitcoin  *(visual)*
27

**รายละเอียดจากภาพ (vision):**

**Title:** Proof of Work in Bitcoin

**รูป/แผนภาพ (illustration):**
- หัวข้อในภาพ: **Why You Can't Cheat at Bitcoin** (ตัวหนา)
- มีภาพเครน (crane) สีขาวดำกำลังยกบล็อกสีเหลืองอยู่บนยอดกำแพงบล็อก (บล็อกสีเทาต่อกันเป็นกำแพงสูง)
- กำแพงบล็อกสีเทามีช่องหนึ่งเป็นสีแดง/ส้ม (บล็อกที่ถูกแก้ไข)
- ด้านล่างซ้ายมีตัวการ์ตูน (คน) กำลังนั่งหน้า computer/จอภาพขนาดเล็ก แสดง blockchain (มีช่องสีแดงและสีเหลือง)
- ด้านขวาล่างมีหน้าจอแสดงตัวการ์ตูน (เหมือน mining/worker)

**ข้อความในภาพ (annotations):**
- **1.** Say everybody is working on **block 91**. (เลข 1 ชี้ไปที่บล็อกสีเหลืองบนยอด)
- **2.** But one miner wants to alter a transaction in **block 74**. (ชี้ไปที่บล็อกสีแดง/ส้ม)
- **3.** He'd have to make his changes and redo all the computations for blocks 74–90 and do block 91. That's **18 blocks of expensive computing**.
- **4.** What's worse, he'd have to do it all **before** everybody else in the Bitcoin network finished **just the one block (number 91)** that they're working on.

(เลขมุมล่างขวา: 27)

---

---

## Slide 28: BlockChain: Proof of Work  *(visual)*
28

**รายละเอียดจากภาพ (vision):**

**Title:** BlockChain: Proof of Work

**ส่วน (a) – แผนภาพ Byzantine Generals / Enemy City:**
- กลางภาพ: บ้าน/ปราสาทสีเขียว กำกับ "Enemy City"
- ข้อความเหนือ Enemy City: "When to Attack ?" (สีแดง)
- รอบ ๆ มีกลุ่ม Generals และ Messengers:
  - ซ้ายบน: "Messengers M₁" (ไอคอนคนสีน้ำเงิน 4 คน) และ "General G₁" (ไอคอนเจดีย์สีส้มแดง) ; ลูกศรไป Enemy City label "Attack"
  - ซ้ายกลาง: "Messengers M₂" และ "General G₂" ; ลูกศร "Attack"
  - ซ้ายล่าง: "Messengers M₁" (sic) และ "General G₃" ; ลูกศร "Attack"
  - ขวาบน: "General G₆" และ "Messengers M₆" ; ลูกศร "Attack"
  - ขวากลาง: "General G₃" และ "Messengers M₅" ; ลูกศร "Attack"
  - ขวาล่าง: "General G₆" (sic) และ "Messengers M₆" ; ลูกศร "Attack"
- กำกับ "(a)" มุมซ้ายบน

**ส่วน (b) – ลำดับเวลา When to Attack ?:**
- หัวคอลัมน์: "When to Attack ?" (แดง), "Start Working", "Work Complete", "Add to Blockchain"
- แถว General G₁: คิดเวลาแล้วได้ "3pm" → Start Working (General G₁ + ภูเขา) → Work Complete (General G₁ + ภูเขา) → Add to Blockchain: "Lost and Agree" (แดง)
- แถว General G₂: ได้ "5pm" → Start Working → Work Complete → "Lost and Agree" (แดง)
- แถว General G₃: ได้ "1pm" → Start Working → Work Complete (มีบล็อกสีเหลือง label "B" และมีเส้นเคลื่อนไหว) → "Win and Broadcast" (แดง) พร้อม Broadcast ไป "Messengers M₃"
- แถวล่างสุด (Time): แสดง blockchain (บล็อก) ตามเวลา "Time T₀", "Time T₁", "Time T₂", "Time T₃"
  - Time T₀: "…" → Block(…) → Block(…)
  - Time T₁: "…" → Block(…) → Block(…)
  - Time T₂: "…" → Block(…) → Block(…)
  - Time T₃: "…" → Block(…) → Block(…) → Block("1pm")
- กำกับ "(b)" มุมซ้าย

(เลขมุมล่างขวา: 28)

---

---

## Slide 29: BlockChain: Proof of Work  *(visual)*
29

**รายละเอียดจากภาพ (vision):**

**Title:** BlockChain: Proof of Work

**ส่วน (c) – แผนภาพ:**
- ด้านซ้าย: กล่องข้อความ "Previous Blocks on Blockchain" มีลูกศร → เข้าสู่บล็อก "Block B₀" (มี "…" อยู่ข้างใน)
- ลูกศรจาก Previous Blocks → Block B₀ → Block B₁ → Block B₂ → Block B₃ → "…" (เส้นทาง blockchain หลัก)
  - Block B₁ ภายในมี "1pm"
  - Block B₂ ภายในมี "1pm"
  - Block B₃ ภายในมี "1pm"
- ด้านบนขวา: Node "General G₁" → ลูกศรลง "PoW" → "Messengers M₁" → ลูกศรลง "Broadcast" → เข้าสู่ blockchain
- ด้านบนกลาง-ขวา: Node "General G₃" → ลูกศรลง → "Messengers M₂" → "Broadcast to Blockchain" → เข้าสู่ Block B₁
  - ข้อความด้านซ้ายบน: "When-to-Attack is 1pm, PoW is Completed"
- ด้านล่างซ้าย: Node "General G₄" (เจดีย์สีส้มแดง) → ลูกศรขึ้น "When-to-Attack is 7pm, PoW is Completed" (แดง/น้ำเงิน) → "Messengers M₄" → "Broadcast to Blockchain" → เข้าสู่กล่อง "Block B₁'" (ภายในมี "7pm") ซึ่งแยกออกจาก Block B₁ (เป็น fork)
- ด้านขวาล่าง: "Messengers M₆" → "Broadcast" ขึ้น ; Node "General G₄" → "PoW" ขึ้น → เข้าสู่ blockchain
- กำกับ "(c)" มุมซ้ายบน

(ข้อความ/ป้ายกำกับ: "Previous Blocks on Blockchain", "Block B₀", "Block B₁", "Block B₂", "Block B₃", "Block B₁'", "1pm", "7pm", "General G₁", "General G₃", "General G₄", "Messengers M₁", "Messengers M₂", "Messengers M₄", "Messengers M₆", "PoW", "Broadcast", "Broadcast to Blockchain", "When-to-Attack is 1pm, PoW is Completed", "When-to-Attack is 7pm, PoW is Completed")
(เลขมุมล่างขวา: 29)

---

---

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

---

## Slide 31: Lost Request Messages when Server Crashes  *(visual)*
A server in client-server communication
a) Normal case
b) Crash after execution
c) Crash before execution

**รายละเอียดจากภาพ (vision):**

**Title:** Lost Request Messages when Server Crashes

**แผนภาพ 3 แบบ (client-server):**

**(a)** Server (กล่องสี่เหลี่ยม) ภายในมีบรรทัด "Receive", "Execute", "Reply"
- ลูกศร "REQ" ชี้เข้าจากซ้ายไปที่ Server (ทึบ)
- ลูกศร "REP" ชี้กลับออกทางซ้าย (ทึบ)
- กำกับด้านล่าง "(a)"

**(b)** Server ภายในมี "Receive", "Execute", และกล่อง "Crash"
- ลูกศร "REQ" ชี้เข้าจากซ้าย (ทึบ)
- ลูกศร "No REP" ชี้กลับออกทางซ้าย (เส้นประ)
- กำกับด้านล่าง "(b)"

**(c)** Server ภายในมี "Receive" และกล่อง "Crash"
- ลูกศร "REQ" ชี้เข้าจากซ้าย (ทึบ)
- ลูกศร "No REP" ชี้กลับออกทางซ้าย (เส้นประ)
- กำกับด้านล่าง "(c)"

**ข้อความด้านล่าง:**
- A server in client-server communication
- a) Normal case
- b) Crash after execution
- c) Crash before execution
(ตัวอักษร a), b), c) เป็นสีม่วง/แดง)

(เลขมุมล่างขวา: 31)

---

---

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

---

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

---

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

---

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

---

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

**รายละเอียดจากภาพ (vision):**

**Title:** HW03: BFT

**โจทย์ (มีไฮไลต์สี):**
Imagine there are **1 loyal commander** (น้ำเงิน), **2 traitor** (แดง) lieutenants, and **5 loyal** (น้ำเงิน) lieutenants. Please provide a concrete example where **Oral Message algorithm** (เขียว) is used among these soldiers, yet the loyal lieutenants all **are able to follow** (แดง) the commander's command.
You need to briefly describe the process of **Oral Message algorithm** (เขียว) in your example.

**แผนภาพ:**
- Node กลาง (ellipse น้ำเงินเข้ม): "COMMANDER"
- Node รอบ ๆ (ellipse):
  - ซ้ายบน (ellipse สีแดงอ่อน = faulty): "LIEUTENANT"
  - ซ้ายกลาง (ellipse สีแดงอ่อน = faulty): "LIEUTENANT"
  - ขวาบน (ellipse ฟ้า = normal): "LIEUTENANT"
  - ขวากลาง (ellipse ฟ้า): "LIEUTENANT"
  - ล่างซ้าย (ellipse ฟ้า): "LIEUTENANT"
  - ล่างกลาง (ellipse ฟ้า): "LIEUTENANT"
  - ล่างขวา (ellipse ฟ้า): "LIEUTENANT"
- ลูกศรจาก COMMANDER ไปยัง lieutenant ทุกตัว มี label "A" ทุกเส้น (ลูกศรไปซ้ายบน, ซ้ายกลาง, ขวาบน, ขวากลาง, ลงล่าง 3 เส้น)
- รวม lieutenant ทั้งหมด 7 ตัว (faulty 2 ตัวคือซ้ายบนและซ้ายกลาง)

**คำบรรยายใต้ภาพ (ตัวเอียง):**
- - The red ellipse represents the faulty nodes, while the blue one for the normal nodes
- - The commander sends the "Attack" order to all lieutenants to which it connects.
- - When each lieutenant act as a commander, a loyal lieutenant sends the original order, "Attack", while the traitor sends "Retreat".

(เลขมุมล่างขวา: 36)

---

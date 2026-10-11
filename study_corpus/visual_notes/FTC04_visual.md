# FTC04 – Rollback Recovery : Visual Notes

> บันทึกภาพสไลด์ (visual notes) สำหรับคลังศึกษาวิชา Fault Tolerant Computing
> รายการสไลด์: 1, 2, 5, 8, 16, 18, 19, 20, 21, 24, 25, 26, 27, 28, 29, 31, 32, 33, 34, 35, 37, 39, 41, 42, 43, 49, 51
> ข้อความบนสไลด์ (ภาษาอังกฤษ) ป้ายกำกับ ตาราง สูตร และชื่อตัวแปร คงไว้ตามต้นฉบับทุกประการ

---

## Slide 1

**ชื่อเรื่อง (title):** Home Exercise: BFT (1/2)

**ข้อความบรรยายเหนือแผนภาพ:**
- OM(2): Commander sends A (Attack) to all 7 lieutenants (incl. traitors)

**แผนภาพส่วนบน** (Commander ส่งข้อความถึง lieutenant ทั้งหมด 7 คน รวม traitor 2 คน):
- ป้าย/โหนดฝั่งซ้าย (สีชมพูแดง 2 โหนด): **TRAITOR1**, **TRAITOR2**
- โหนดกลาง (สีฟ้า): **COMMANDER**
- โหนดฝั่งขวา (สีฟ้า): **LIEUTENANT3**, **LIEUTENANT4**, **LIEUTENANT5**
- โหนดด้านล่าง (สีฟ้า): **LIEUTENANT1**, **LIEUTENANT2**
- ลูกศรทุกเส้นจาก COMMANDER มีป้ายกำกับ **A** (แทนข้อความ Attack) ชี้ไปยัง lieutenant และ traitor ทุกคน (ลูกศรบางเส้นชี้ไปทางซ้าย, บางเส้นชี้ลง, บางเส้นชี้ไปทางขวา)

**ข้อความบรรยายใต้แผนภาพ:**
- OM(1): Every lieutenant (incl. traitor) acts as commander

**แผนภาพส่วนล่าง** (OM(1) – แสดง lieutenant แต่ละคนทำหน้าที่เป็น commander เอง มี 2 แผนภาพย่อย):
- แผนภาพย่อยซ้าย: โหนด **C** (สีชมพู, สื่อ commander) ส่งข้อความป้าย **R** ไปยังโหนด **L** หลายโหนด และไปยังโหนด **T** (สีส้มอ่อน, สื่อ traitor) มีป้าย **R** กำกับลูกศรทั้งหมด (ลูกศรหนึ่งเส้นโค้งลงไปยัง L ด้านล่างซ้าย)
- แผนภาพย่อยขวา: โหนด **C** (สีฟ้า) ส่งข้อความป้าย **A** ไปยังโหนด **T** 2 โหนด (สีส้มอ่อน) และโหนด **L** หลายโหนด ป้าย **A** กำกับลูกศรทุกเส้น

- เลขหน้า (มุมขวาล่าง): 1

---

## Slide 2

**ชื่อเรื่อง (title):** Home Exercise: BFT (2/2)

**ข้อความบรรยายเหนือแผนภาพ:**
- OM(0): Every lieutenant (incl. traitor) relays the message

**แผนภาพส่วนบน** (2 แผนภาพย่อย แสดงการ relay ข้อความ เหมือนสไลด์ 1):
- แผนภาพย่อยซ้าย: โหนด **C** (สีชมพู) ส่งป้าย **R** ไปยังโหนด **L** หลายโหนดและโหนด **T** (สีส้มอ่อน)
- แผนภาพย่อยขวา: โหนด **C** (สีฟ้า) ส่งป้าย **A** ไปยังโหนด **T** 2 โหนด และโหนด **L** หลายโหนด

**ตาราง** (ตารางค่าที่ lieutenant แต่ละคนได้รับ แล้วทำ Majority Vote):

| Lieutenant | Value frm C | Frm L1 | Frm L2 | Frm L3 | Frm L4 | Frm L5 | Frm T1 | Frm T2 | Majority Vote |
|---|---|---|---|---|---|---|---|---|---|
| L1 | A | - | A | A | A | A | R | R | A |
| L2 | A | A | - | A | A | A | R | R | A |
| L3 | A | A | A | - | A | A | R | R | A |
| L4 | A | A | A | A | - | A | R | R | A |
| L5 | A | A | A | A | A | - | R | R | A |
| T1 | X | X | X | X | X | X | - | X | X |
| T2 | X | X | X | X | X | X | X | - | X |

หมายเหตุ: หัวคอลัมน์แรกเขียนว่า "Lieute nant" และคอลัมน์ที่สอง "Value frm C" (ตัวอักษรตัดบรรทัดตามที่ปรากฏบนสไลด์) แถว L1–L5 และ T1/T2; ช่องทแยงเป็น "-" และแถว traitor เป็น "X" ทั้งหมด

- เลขหน้า (มุมขวาล่าง): 2

---

## Slide 5

**ชื่อเรื่อง (title):** Fault Tolerance & Recovery

**แผนภาพ** (ลูกศรและกล่อง/วงรี):
- กล่องสี่เหลี่ยมด้านบนสุด: **fault**
- ลูกศรจาก fault ชี้ลง พร้อมข้อความกำกับ: **causes**
- วงรีขนาดใหญ่: **erroneous state** ภายในมีวงรีเล็กซ้อนอยู่: **error**
- จาก erroneous state มีลูกศรชี้ลง กำกับ: **leads to**
- กล่องสี่เหลี่ยมด้านล่างซ้าย: **failure**
- จาก erroneous state มีลูกศรชี้ไปทางขวา กำกับคำสีแดง: **Recovery** แล้วชี้ลง
- วงรีด้านขวา: **valid state**

**Bullet (ข้อความ):**
- An error is a manifestation of a fault that can lead to a failure.
- Failures:
  - Process failure: Deadlocks, protection violation, erroneous user input.
  - System failure: Full/partial amnesia.
  - Secondary storage failure: data inaccessible.
  - Communication failure: network inaccessible.

- เลขหน้า (มุมขวาล่าง): 5

---

## Slide 8

**ชื่อเรื่อง (title):** System Design Space

**แผนภาพ** (รูปสามเหลี่ยม – trade-off สามมุม):
- ยอดบนสุด (ตัวหนา สีแดงขอบดำ): **High Availability**
- มุมล่างซ้าย (ตัวหนา สีเหลืองขอบดำ): **Low Cost**
- มุมล่างขวา (ตัวหนา สีน้ำเงิน): **High Performance**
- ข้อความด้านซ้าย (สีแดง): **Backward Error Recovery** / **(Tandem NonStop)**
- ข้อความด้านขวา (สีแดง): **Forward Error Recovery** / **(IBM mainframes)**
- ข้อความด้านล่างกลาง (สีเขียว): **Servers and PCs**

- เลขหน้า (มุมขวาล่าง): 8

---

## Slide 16

**ชื่อเรื่อง (title):** System Model

**แผนภาพ space-time (time-space diagram):**
- เส้นประแนวนอนคั่น พร้อมป้ายบรรทัดบน: **Outside world** และบรรทัดล่าง: **Message-passing system**
- เส้นเวลา (timeline) 3 เส้น มีป้ายชื่อ: **P0**, **P1**, **P2** (เรียงบนลงล่าง) แต่ละเส้นมีลูกศรชี้ไปทางขวา
- ลูกศรทแยงจาก outside world ชี้ลงมาที่ **P0** กำกับ: **Input message**
- ลูกศรทแยงจาก **P0** ขึ้นไปยัง outside world กำกับ: **Output message**
- ลูกศรจาก **P0** ชี้ลงไปยัง **P1** กำกับ: **m1**
- ลูกศรจาก **P1** ชี้ลงไปยัง **P2** กำกับ: **m2**

**ข้อความด้านล่าง (Basic approaches):**
- Basic approaches
  - Checkpointing : copying/restoring the state of a process
  - Logging : recording/replaying messages

- เลขหน้า (มุมขวาล่าง): 16

---

## Slide 18

**ชื่อเรื่อง (title):** Rollback Recovery Principles

**หัวข้อย่อย (สีแดง):** 1. Checkpointing
- ข้อความกำกับจุด: **checkpoint (stored local state)** (มีลูกศรชี้ไปยังจุด checkpoint รูปสี่เหลี่ยมสีม่วงบนเส้นเวลา)
- ป้ายด้านซ้าย (สีน้ำเงิน ตัวเอียง): **Inside the cut**
- ป้ายด้านขวา (สีน้ำเงิน ตัวเอียง): **Outside the cut**
- ป้ายด้านขวาล่าง: **Recovery line (cut)**

**แผนภาพ space-time:**
- เส้นเวลา 4 เส้น มีป้าย: **P0**, **P1**, **P2**, **P3** (บนลงล่าง) ลูกศรชี้ขวาทุกเส้น
- มีจุด checkpoint สีม่วง (สี่เหลี่ยมมุมมน) หนึ่งจุดบนแต่ละเส้นเวลา (P0, P1, P2, P3) เรียงเหลื่อมกันลงมา
- เส้นประสีน้ำเงินลากทแยงผ่านจุด checkpoint ทั้งสี่ (คือ recovery line / cut)
- ลูกศรสีดำทแยง (message arrows) ระหว่างเส้นเวลา: P0→P1, P0→P2, P2→P3 (ชี้ลงขวา) และมีลูกศรจาก P1 ขึ้นไป P0

**ข้อความด้านล่าง:**
- Restart all, or almost all, processes from a consistent cut and let a new execution run

- เลขหน้า (มุมขวาล่าง): 18

---

## Slide 19

**ชื่อเรื่อง (title):** Rollback Recovery Principles

**หัวข้อย่อย (สีแดง):** 2. Message Logging
- ข้อความกำกับจุด: **checkpoint (stored local state)** (ลูกศรชี้ไปยังจุด checkpoint รูปสี่เหลี่ยมสีม่วงบน P0)

**แผนภาพ space-time:**
- เส้นเวลา 4 เส้น มีป้าย: **P0**, **P1**, **P2**, **P3** (บนลงล่าง)
- จุด checkpoint สีม่วงบน P0, P1, P2, P3 (มีลูกศรเล็กสีดำชี้ลงภายในกล่อง checkpoint)
- เส้นประสีน้ำเงินลากทแยงผ่านจุด checkpoint
- เส้นสีแดงโค้ง (แสดงการใช้ message logging replay) ลากจากเครื่องหมาย **failure** (รูปกากบาทสีแดง ✖) บนเส้น **P1** ฝั่งขวา กลับไปยังจุดฝั่งซ้าย (ช่วงก่อน failure)
- ลูกศรสีดำทแยงหลายเส้นระหว่างเส้นเวลา (P0→P1, P0→P2, P1→P2, P2→P3, P2 บน ฯลฯ)
- เครื่องหมาย failure: กากบาทสีแดงบน **P1**

**ข้อความด้านล่าง:**
- Only one (or a few) process recover and use message information to replay the previous execution until reaching the failure point

- เลขหน้า (มุมขวาล่าง): 19

---

## Slide 20

**ชื่อเรื่อง (title):** Rollback Recovery Principles

**กล่องข้อความสีน้ำเงิน (กรอบแดง ด้านขวาบน):**
- A recoverable state contains enough information to replay an execution up to a coherent cut of the original execution (up to the failure point)

**กล่องข้อความสีน้ำเงิน (กรอบแดง ด้านขวาล่าง):**
- It is sufficient to reconstruct a state that *could* have occurred in a failure-free execution

**ข้อความกำกับ:** **checkpoint (stored local state)** (ลูกศรชี้ไปยังจุด checkpoint สีม่วงบน P0)
- ป้ายด้านล่างซ้าย: **strongly consistent cut**

**แผนภาพ space-time:**
- เส้นเวลา 4 เส้น มีป้าย: **P0**, **P1**, **P2**, **P3**
- จุด checkpoint สีม่วงบน P0, P1, P2, P3
- เส้นประสีน้ำเงินทแยงผ่านจุด checkpoint (คือ strongly consistent cut)
- เครื่องหมาย failure: กากบาทสีแดงบน **P1**
- ลูกศรสีดำทแยงหลายเส้นระหว่างเส้นเวลา (P0→P1, P0→P2, P1→P2, P2→P3, P2→P1(bน) ฯลฯ)

- เลขหน้า (มุมขวาล่าง): 20

---

## Slide 21

**ชื่อเรื่อง (title):** Implementation of Rollback Recovery

**แผนภาพซ้าย** (Layered stack – Rollback recovery อยู่บน reliable protocol):
- **User applications**
- **Rollback-recovery protocol** (กรอบมีลายทแยง cross-hatch)
- **Reliable communication protocol**
- **Unreliable communica-tion channel**

ข้อความใต้แผนภาพซ้าย:
- On top of a **reliable** communication protocol

**แผนภาพขวา** (Layered stack – Rollback recovery อยู่บน unreliable channel โดยตรง):
- **User applications**
- **Reliable communication protocol**
- **Rollback-recovery protocol** (กรอบมีลายทแยง cross-hatch)
- **Unreliable communica-tion channel**

ข้อความใต้แผนภาพขวา:
- Directly on top of **unreliable** communication channels

หมายเหตุ: คำ "reliable" แสดงสีแดงในภาพซ้าย และ "unreliable" แสดงสีแดงในภาพขวา

- เลขหน้า (มุมขวาล่าง): 21

---

## Slide 24

**ชื่อเรื่อง (title):** In-transit message

**ข้อความบรรยาย (ตัวเอียง):**
- *messages that have been sent but not yet received*

**Bullet (ข้อความ):**
- If message delivery is not guaranteed, they are not a problem!
- But if the communication protocol is reliable, they must be taken into account

**แผนภาพ space-time:**
- ป้ายด้านบน (สีน้ำเงิน): **in transit messages**
- เส้นเวลา 4 เส้น มีป้าย: **P0**, **P1**, **P2**, **P3** (บนลงล่าง)
- ลูกศรสีดำทแยงจาก **P1** ลงไปยัง **P2** และจาก **P3** ขึ้นไปยัง **P2**
- เส้นประสีน้ำเงินทแยงผ่านระหว่างเส้นเวลา (แสดง cut)
- เส้นบาง (สีเทา/ดำ) แสดงระยะของ in-transit messages (ลูกศรสีเทาชี้ลงจากใน P1 ไปยัง P2 เป็นต้น)

- เลขหน้า (มุมขวาล่าง): 24

---

## Slide 25

**ชื่อเรื่อง (title):** Lost message

**Bullet (ข้อความ):**
- Due to the failure in process, the message count not reach the process and so it is lost on the way
- Different from In-transit message

**แผนภาพ space-time:**
- ป้ายบนเส้น **P1**: จุด checkpoint **C1**, **C2** (สี่เหลี่ยมสีน้ำเงิน)
- มีเส้นโค้งสีน้ำเงิน กำกับคำ **Rollback** (ชี้จากฝั่งขวากลับไปยังจุด C2)
- เครื่องหมาย failure: กากบาทสีแดง ✖ บน **P1** (ด้านขวาของ C2) กำกับคำสีแดง **failure**
- บนเส้น **P2**: ลูกศรข้อความจาก P2 ขึ้นไปยัง P1 กำกับ **m1** (ชี้ไปยังจุด failure บน P1)
- มีเส้นเวลาที่ 3 (เส้นล่างสุด ไม่มีป้ายชื่อ)

**ข้อความด้านล่าง:**
- Due to the failure in **P1**, **m1** could not reach **P1** and lost on the way
- **P1** rollback to **C2** to recover its old status to continue the task

- เลขหน้า (มุมขวาล่าง): 25

---

## Slide 26

**ชื่อเรื่อง (title):** Delayed message

**Bullet (ข้อความ):**
- The lost messages may reach the destination process after recovered, ie. messages arrived after rollback

**แผนภาพ space-time:**
- เส้นเวลา 2 เส้น มีป้าย: **P0**, **P1** (บนลงล่าง)
- บน **P0**: จุด checkpoint **C0** (สี่เหลี่ยมสีน้ำเงิน) และมีเส้นโค้งสีน้ำเงิน กำกับคำ **Rollback** ชี้กลับไปยัง C0; ต่อจาก C0 มีจุดกลม (node) สีน้ำเงินบน P0
- บน **P1**: จุด checkpoint **C1** (สี่เหลี่ยมสีน้ำเงิน) มีเส้นโค้งสีน้ำเงิน กำกับคำ **Rollback** ชี้กลับไปยัง C1
- ลูกศรจากด้านล่างซ้ายชี้ขึ้นไปยังจุดกลมบน P0 กำกับ **m1**
- ลูกศรจากจุดกลมบน P0 ชี้ลงไปยัง **P1** กำกับ **m5**
- ข้อความสีน้ำเงิน ตัวเอียง ด้านขวาบน: *m1 reached P1 after recovered from failure*
- ข้อความสีน้ำเงิน ตัวเอียง ด้านขวา: *m5 also delayed message*

- เลขหน้า (มุมขวาล่าง): 26

---

## Slide 27

**ชื่อเรื่อง (title):** Orphan messages

**ข้อความบรรยาย (ตัวเอียง):**
- *messages with 'receive' recorded but message 'send' not recorded*

**Bullet (ข้อความ):**
- If P2 fails and restarts from the cut, the message will be re-emitted and received twice by P1
  - Either avoid using inconsistent cuts (in general for checkpointing)
  - Or avoid re-emitting the message (in general for message logging) and replay the same execution

**แผนภาพ space-time (ด้านขวา):**
- ป้ายด้านบน (สีน้ำเงิน): **not consistent cut**
- เส้นเวลา 4 เส้น มีป้าย: **P0**, **P1**, **P2**, **P3**
- เส้นประสีน้ำเงินทแยงผ่านระหว่างเส้นเวลา (แสดง cut ที่ไม่สอดคล้อง)
- ลูกศรสีดำทแยง: P0→P1 (ลงขวา), P3→P2 (ขึ้นขวา), P1→P2 (ชี้ขึ้นไปทางซ้าย เป็น orphan message)
- ป้ายด้านล่าง (สีน้ำเงิน): **orphan message** (มีเส้นชี้จากป้ายไปยังลูกศร orphan)

- เลขหน้า (มุมขวาล่าง): 27

---

## Slide 28

**ชื่อเรื่อง (title):** Duplicate message

**Bullet (ข้อความ):**
- The message which already received has been re-sent after recovery

**แผนภาพ space-time:**
- เส้นเวลา 2 เส้น มีป้าย: **P0**, **P1**
- บน **P0**: จุด checkpoint **C1** (สี่เหลี่ยมสีน้ำเงิน) มีเส้นโค้งสีน้ำเงิน กำกับคำ **Rollback** ชี้กลับไปยัง C1
- เครื่องหมาย failure: กากบาทสีแดง ✖ บน **P0** ด้านขวา กำกับคำสีแดง **failure**
- ลูกศรข้อความจาก **P0** (หลัง C1) ชี้ลงไปยัง **P1** กำกับ **m1**

- เลขหน้า (มุมขวาล่าง): 28

---

## Slide 29

**ชื่อเรื่อง (title):** Messages – example

**Bullet (ข้อความด้านซ้าย):**
- In-transit
  - *m1, m2*
- Lost
  - *m1*
- Delayed
  - *m1, m5*
- Orphan
  - *none*
- Duplicated
  - *m4, m5*

**แผนภาพ space-time (ด้านขวา, มี 4 process: P1, P2, P3, P4 เรียงบนลงล่าง):**
- เส้นเวลาแต่ละเส้นมีป้ายตัวเลขเวลา (tick) กำกับ:
  - **P1**: 0, 2, 4, 6, 8 (มีป้าย **Failure** และเครื่องหมายกากบาทใกล้จุดเวลา 8)
  - **P2**: 0, 3, 6, 9
  - **P3**: 0, 4, 8
  - **P4**: 0, 1, 2, 3, 4, 5, 6, 7, 8
- ลูกศรข้อความ (message arrows) ระหว่างเส้นเวลา พร้อมป้าย:
  - **m2** (ลูกศรจาก P2 ขึ้นไป P1), **m5** (ลูกศรจาก P2 ลงไป P3), **m1** (ลูกศรจาก P3 ขึ้น/ลงระหว่าง P2 กับ P3), **m3** (ลูกศรระหว่าง P2/P3), **m4** (ลูกศรจาก P2/P3 ลงไป P4)
  (การวางแนวลูกศร: m1 ทแยงขึ้นและลง, m2 ชี้ขึ้นไป P1, m4 ชี้ลงไป P4, m5 ชี้ลงจาก P2, m3 ทแยง)
- เส้นประโค้ง (Recovery line) ลากผ่านระหว่างกระบวนการ พร้อมป้ายด้านล่าง: **Recovery line**

- เลขหน้า (มุมขวาล่าง): 29

---

## Slide 31

**ชื่อเรื่อง (title):** Consistent/Inconsistent State

**แผนภาพ space-time:** (มี 4 เส้นเวลา: **P0**, **P1**, **P2**, **P3** เรียงบนลงล่าง; ลูกศรข้อความสีดำหลายเส้นระหว่างเส้นเวลา; และเส้นประสีน้ำเงิน 3 เส้นแสดง cut ที่ต่างกัน)

**ป้ายกำกับ (labels):**
- ป้ายด้านซ้ายบน (สีแดง): **Inconsistent state**
- ป้ายด้านซ้ายล่าง (สีน้ำเงิน): **Orphan message** (ลูกศรชี้ขึ้นไปยัง cut ด้านซ้าย)
- ป้ายกลางล่าง (สีแดง): **Strongly consistent state** (ชี้ไปยังเส้นประกลาง)
- ป้ายด้านขวาบน (สีน้ำเงิน): **In-transit messages** (มีเส้นชี้ 2 เส้นไปยังจุดบน cut ขวา)
- ป้ายด้านขวาล่าง (สีแดง): **Consistent State** (ชี้ไปยังเส้นประขวา)

**รายละเอียด cut ทั้ง 3:**
- เส้นประซ้าย: เป็น inconsistent state และมี orphan message
- เส้นประกลาง: เป็น strongly consistent state
- เส้นประขวา: เป็น Consistent State แต่มี in-transit messages

- เลขหน้า (มุมขวาล่าง): 31

---

## Slide 32

**ชื่อเรื่อง (title):** Domino Effect

**ข้อความบรรยาย:**
- Cascaded rollback which causes the system to roll back to too far in the computation (even to the beginning), in spite of all the checkpoints

**แผนภาพ space-time:** (3 เส้นเวลา: **X**, **Y**, **Z** เรียงบนลงล่าง; เครื่องหมาย `[` แทน checkpoint)
- บน **X**: checkpoint ป้าย **x1**, **x2**, **x3**
- บน **Y**: checkpoint ป้าย **y1**, **y2**; มีลูกศรข้อความ **m** ชี้ลงไป Z; เครื่องหมาย failure: กากบาทสีแดง ✖ บน Y ด้านขวา กำกับคำสีแดง **failure**
- บน **Z**: checkpoint ป้าย **z1**, **z2**; ด้านขวาล่างมีป้าย `[` กำกับ **recovery point**
- ลูกศรข้อความระหว่างเส้นเวลา: Y→X (ขึ้นไป), Z→Y, Y→Z, Z→X หลายเส้น (ทแยงขึ้น/ลง)

**ข้อความด้านล่าง:**
- Suppose Y rolls back to y2
  - m is **orphan message**
  - Process X must rollback to x2
- Suppose Z rolls back to z2
  - Y rolls back to **y1**
  - Force X, Z to roll back to **x1, z1**

- เลขหน้า (มุมขวาล่าง): 32

---

## Slide 33

**ชื่อเรื่อง (title):** Livelocks

**แผนภาพ space-time** (มี 2 แผนภาพย่อย ซ้อนกัน แสดงเหตุการณ์ X, Y):
- แผนภาพย่อยที่ 1:
  - บน **X**: checkpoint **x1**
  - บน **Y**: checkpoint **y1**
  - ลูกศรข้อความ: X→Y กำกับ **n1**; Y→X กำกับ **m1**
  - เครื่องหมาย failure: กากบาทสีแดง ✖ บน **Y** ด้านขวา กำกับคำสีแดง **failure**
- แผนภาพย่อยที่ 2:
  - บน **X**: checkpoint **x1**
  - บน **Y**: checkpoint **y1**
  - ลูกศรข้อความ: **n1**, **n2** (จาก X ไป Y), **m2** (จาก Y ไป X)
  - เครื่องหมาย failure: กากบาทสีแดง ✖ กำกับคำสีแดง **2nd Rollback**

**Bullet (ข้อความ):**
- **Y crashes** before receiving n1. Y **rolls back to Y1** -> X to **x1**.
- Y recovers, receives n1 and sends m2.
- X recovers, sends n2 but has no record of sending n1
- Hence, Y is forced to rollback second time. X also rolls back as it has received m2 but Y has no record of m2.
- Above sequence can **repeat indefinitely**, causing a **livelock**.

- เลขหน้า (มุมขวาล่าง): 33

---

## Slide 34

**ชื่อเรื่อง (title):** Consistent Checkpoints

**Bullet (ข้อความ):**
- Overcoming domino effect and livelocks: checkpoints should not have messages in transit.
- Consistent checkpoints: no message exchange between any pair of processes in the set as well as outside the set during the interval spanned by checkpoints.
- {x1,y1,z1} is a **strongly consistent checkpoint**.

**แผนภาพ space-time:** (3 เส้นเวลา: **X**, **Y**, **Z**; จุด checkpoint แสดงเป็นสี่เหลี่ยมสีน้ำเงิน)
- บน **X**: checkpoint **x1**, **x2**, **x3**
- บน **Y**: checkpoint **y1**, **y2**
- บน **Z**: checkpoint **z1**, **z2**
- ลูกศรข้อความระหว่างเส้นเวลา: Y→X (ขึ้นไป), X→Z, Z→X, Z→Y (ขึ้นไป), Y→Z, และลูกศร **m** จาก Y ไปยัง X (ขึ้นไปทางขวา)

- เลขหน้า (มุมขวาล่าง): 34

---

## Slide 35

**ชื่อเรื่อง (title):** Recovery Techniques

**แผนภาพต้นไม้ (tree diagram):**

- **Rollback-Recovery** (โหนดราก)
  - สาขาซ้าย: **checkpointing**
    - **uncoordinated**
    - **coordinated**
      - **blocking**
      - **non-blocking**
    - **communication-induced**
      - **model-based**
      - **index-based**
  - สาขาขวา: **logging**
    - **pessimistic**
    - **optimistic**
    - **causal**

- เลขหน้า (มุมขวาล่าง): 35

---

## Slide 37

**ชื่อเรื่อง (title):** Coordinated/Blocking Protocols

**แผนภาพต้นไม้ย่อย (ด้านซ้าย):**
- **Rollback-Recovery** → **checkpointing** → **coordinated** → **blocking**

**แผนภาพ space-time (ด้านขวา):** (3 เส้นเวลา: **X**, **Y**, **Z**; checkpoint แสดงเป็น `[` พร้อมป้าย下标)
- บน **X**: checkpoint **x₁**, **x₂**
- บน **Y**: checkpoint **y₁**, **y₂**
- บน **Z**: checkpoint **z₁**, **z₂**
- ลูกศรข้อความระหว่างเส้นเวลา: X→Y (ลงขวา), X→Z (ลงขวา), X→Z (ขึ้น?) , Y→Z, Z→X (ขึ้นไป), Y→X (ขึ้นไป), Z→Y (ขึ้นไป), Z→Z?, และลูกศร **m** จาก Z ไปยัง X (ขึ้นไปทางขวา)
- เส้นประแนวตั้งลากผ่าน x₁, y₁, z₁ และมีวงเล็บ (brace) สีแดงด้านล่างเชื่อมช่วงระหว่าง x₁ ถึง z₁

**ข้อความด้านล่าง (สีแดง):**
- no messages can be in transit during checkpointing
- {x1, y1, z1} forms "recovery line"

- เลขหน้า (มุมขวาล่าง): 37

---

## Slide 39

**ชื่อเรื่อง (title):** Coordinated checkpointing

**Bullet (ข้อความ):**
- There is an initiator process for the checkpointing
  - Only one (or 2) checkpoint per process (always consistent)
  - large latency: processed blocked until checkpoint is finished

**แผนภาพ space-time (ด้านซ้าย):** (4 เส้นเวลา: **P0: initiator**, **P1**, **P2**, **P3**)
- ลูกศรเส้นประ (dotted) จาก P0 กระจายลงไปยัง P1, P2, P3 กำกับคำ: **checkpoint requests**
- เส้น P0 มีป้ายกำกับด้านขวา: **P0: initiator**

**แผนภาพ space-time (ด้านขวา):**
- ป้ายด้านบน: **Initiator**
- เส้นเวลา 2 เส้น มีป้าย: **P₀** (บน), **P₁** (ล่าง)
- จุด checkpoint: **c₀,ₓ** บน P₀ และ **c₁,ₓ** บน P₁ (แสดงเป็นสี่เหลี่ยมดำทึบ)
- ลูกศรเส้นประจาก Initiator ลงไปยัง c₀,ₓ และไปยัง c₁,ₓ กำกับคำ (ตัวเอียง): *checkpoint request*
- ลูกศรข้อความจาก P₀ ลงไปยัง P₁ กำกับ **m**
- วงรีสีแดง (วงกลมแดง) ล้อมบริเวณระหว่าง c₀,ₓ ฝั่งขวา กับลูกศร m และ c₁,ₓ

**ข้อความด้านล่าง (ใต้แผนภาพขวา):**
- inconsistency if communications are not blocked until the end of the checkpointing phase

- เลขหน้า (มุมขวาล่าง): 39

---

## Slide 41

**ชื่อเรื่อง (title):** Coordinated Checkpointing (3) / **Overall execution graph**

**แผนภาพ space-time:** (4 เส้นเวลา: **P0: initiator**, **P1**, **P2**, **P3** เรียงบนลงล่าง)
- ลูกศรเส้นประ (dotted) กระจายจาก P0 ลงไปยัง P1, P2, P3 กำกับคำ: **checkpoint requests**
- ลูกศรเส้นประจำนวนมาก (acknowledgment) ชี้กลับขึ้นไปรวมที่ P0 กำกับคำ: **acknowledgments**
- ป้ายด้านขวาบน: **Commit** (มีเส้นประโค้งสีน้ำเงินทแยงผ่านปลายขวาของเส้นเวลา P0..P3)
- เส้นประสีน้ำเงิน (แนวตั้ง/ทแยงเล็กน้อย) แสดง cut หลัง Commit
- ป้ายชื่อ process: **P0: initiator** (ด้านขวาบน), **P1**, **P2**, **P3**

- เลขหน้า (มุมขวาล่าง): 41

---

## Slide 42

**ชื่อเรื่อง (title):** Checkpoint inconsistency

**แผนภาพ space-time (ด้านซ้าย, ป้าย (a)):** (2 เส้นเวลา: **P₀** (บน), **P₁** (ล่าง))
- ป้ายด้านบน: **Initiator**
- จุด checkpoint: **c₀,ₓ** บน P₀, **c₁,ₓ** บน P₁
- ลูกศรเส้นประจาก Initiator ลงไปยัง c₀,ₓ และไปยัง c₁,ₓ กำกับคำ: **Checkpoint request**
- ลูกศรข้อความจาก P₀ ลงไปยัง P₁ กำกับ **m**
- ป้ายกำกับใต้แผนภาพ: **(a)**

**Bullet (ข้อความด้านขวา):**
- message **m** is sent by *P₀* after receiving a checkpoint request from the checkpoint coordinator
- Assume **m reaches *P₁* before** the checkpoint request
- This situation results in an **inconsistent checkpoint** since checkpoint *C₁,ₓ* shows the receipt of message m from *P₀*, while checkpoint *C₀,ₓ* does not show m being sent from *P₀*

- เลขหน้า (มุมขวาล่าง): 42

---

## Slide 43

**ชื่อเรื่อง (title):** Checkpoint inconsistency: a solution with FIFO channels

**Bullet (ข้อความด้านซ้าย):**
- If channels are FIFO, this problem can be avoided by preceding the first post-checkpoint message on each channel by a checkpoint request, forcing each process to take a **checkpoint before receiving** the first post-checkpoint message

**แผนภาพ space-time (ด้านขวา, ป้าย (b)):** (2 เส้นเวลา: **P₀** (บน), **P₁** (ล่าง))
- ป้ายด้านบน: **Initiator**
- จุด checkpoint: **c₀,ₓ** บน P₀, **c₁,ₓ** บน P₁
- ลูกศรเส้นประจาก Initiator ลงไปยัง c₀,ₓ และไปยัง c₁,ₓ กำกับคำ: **Checkpoint request**
- ลูกศรข้อความจาก P₀ ลงไปยัง P₁ กำกับ **m**
- ป้ายกำกับใต้แผนภาพ: **(b)**

- เลขหน้า (มุมขวาล่าง): 43

---

## Slide 49

**ชื่อเรื่อง (title):** Pessimistic message logging

**Bullet (ข้อความ):**
- orphan processes are never created but requires a lot of synchronizations with the stable storage
- Logs the determinant of ND events before executing them

**สูตร / เงื่อนไข (synchronous logging (stronger condition)):**
- ข้อความตัวเอียง: *synchronous logging (stronger condition)*
- สูตร: ∀e : ¬Stable(e) ⇒ |Depend(e)| = 0

**กล่องข้อความสีน้ำเงิน (กรอบแดง ด้านขวา):**
- Only 1 process restarts

**แผนภาพ space-time:** (4 เส้นเวลา: **P0**, **P1**, **P2**, **P3** เรียงบนลงล่าง)
- จุด checkpoint สีม่วง (สี่เหลี่ยมมุมมน มีลูกศรดำชี้ลงภายใน) บน P0, P1, P2, P3
- เส้นสีแดงโค้ง (แสดง replay) จากเครื่องหมาย failure กลับไปทางซ้าย
- เครื่องหมาย failure: กากบาทสีแดง ✖ บน **P1** ด้านขวา
- ลูกศรข้อความสีดำทแยงหลายเส้นระหว่างเส้นเวลา (P0→P1, P1→P2, P2→P3, P2→P1(bน), P2→P0(bน) ฯลฯ)
- มีวงกลมสีน้ำเงิน (2 วง) ล้อมลูกศรข้อความ, วงกลมสีแดง (2 วง) ล้อมจุดบนเส้น P1

**ข้อความด้านล่าง:**
- ด้านซ้าย: message resent during recovery (might have to be cancelled) (มีเส้นชี้ไปยังวงกลมสีน้ำเงิน)
- ด้านขวา: logged message reception (มีเส้นชี้ไปยังวงกลมสีแดง)

- เลขหน้า (มุมขวาล่าง): 49

---

## Slide 51

**ชื่อเรื่อง (title):** HW04: Checkpointing

**Bullet (ข้อความ):**
- Find the consistent cuts in the figure below (passing by ▦) *(สัญลักษณ์ท้ายประโยคเป็นรูปสี่เหลี่ยมมีลายจุด grid สีฟ้า)*
- The recovery line that you found is **consistent**, **strongly consistent** or inconsistent?

**แผนภาพ space-time:** (4 เส้นเวลา: **P0**, **P1**, **P2**, **P3** เรียงบนลงล่าง; จุด checkpoint เป็นสี่เหลี่ยมสีน้ำเงินทึบ)
- บน **P0**: มี checkpoint 4 จุด
- บน **P1**: มี checkpoint 3 จุด (และมีเครื่องหมาย failure กากบาทสีแดง ✖ อยู่ด้านขวาสุด)
- บน **P2**: มี checkpoint 4 จุด
- บน **P3**: มี checkpoint 4 จุด
- ลูกศรข้อความสีดำหลายเส้นระหว่างเส้นเวลา (ทแยงขึ้น/ลง) เชื่อมระหว่าง checkpoint ต่างๆ
- เครื่องหมาย failure: กากบาทสีแดง ✖ บนเส้น **P1** ด้านขวา

- เลขหน้า (มุมขวาล่าง): 51

---

*(สิ้นสุด visual notes)*

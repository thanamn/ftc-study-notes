# FTC04_Rollback_Recovery — Enriched (slide text + vision of visual slides)

> Text = exact extraction from the born-digital PDF. For `visual` slides, a faithful description of the figure/table/formula is added under **รายละเอียดจากภาพ**. Vision descriptions are model-produced and marked as such.

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

**รายละเอียดจากภาพ (vision):**

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

---

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

**รายละเอียดจากภาพ (vision):**

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

---

## Slide 3: Rollback Recovery
(Fault Tolerance in Distributed Systems)

 2110473 Fault Tolerant Computing

---

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

---

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

**รายละเอียดจากภาพ (vision):**

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

---

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

---

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

---

## Slide 8: System Design Space  *(visual)*
8

**รายละเอียดจากภาพ (vision):**

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

---

## Slide 9: Forward Recovery
• Repair and go ahead
• Goal: To restore system from erroneous state
 to error-free state
• If nature of error is completely known
 - Remove error from state
 - Proceed with execution from error-free state
• Rarely possible to do

---

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

---

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

---

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

---

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

---

## Slide 14: Checkpointing
• Checkpoint recover is the saving and
 restoration of the system state.
• By saving the current state of the system
 periodically, it provides the information
 needed for the restoration of the lost state,
 when the system fails

---

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

---

## Slide 16: System Model  *(visual)*
Basic approaches
 - Checkpointing : copying/restoring the state of a process
 - Logging : recording/replaying messages

**รายละเอียดจากภาพ (vision):**

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

---

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

---

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

**รายละเอียดจากภาพ (vision):**

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

---

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

**รายละเอียดจากภาพ (vision):**

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

---

## Slide 20: Rollback Recovery Principles  *(visual)*
20

**รายละเอียดจากภาพ (vision):**

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

---

## Slide 21: Implementation of Rollback Recovery  *(visual)*
On top of a reliable Directly on top of unreliable
 communication protocol communication channels

**รายละเอียดจากภาพ (vision):**

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

---

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

---

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

---

## Slide 24: In-transit message  *(visual)*
messages that have been sent but not yet received
• If message delivery is not guaranteed, they are not a problem!
• But if the communication protocol is reliable, they must be
 taken into account

**รายละเอียดจากภาพ (vision):**

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

---

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

**รายละเอียดจากภาพ (vision):**

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

---

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

**รายละเอียดจากภาพ (vision):**

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

---

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

**รายละเอียดจากภาพ (vision):**

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

---

## Slide 28: Duplicate message  *(visual)*
• The message which already received has been re-sent after
 recovery

 Rollback

 C1 failure
 P0
 m1

 P1

**รายละเอียดจากภาพ (vision):**

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

---

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

**รายละเอียดจากภาพ (vision):**

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

---

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

---

## Slide 31: Consistent/Inconsistent State  *(visual)*
In-transit messages Inconsistent state

 P0

 P1

 P2

 P3

 Consistent State
Orphan message Strongly
 consistent state

**รายละเอียดจากภาพ (vision):**

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

---

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

**รายละเอียดจากภาพ (vision):**

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

---

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

**รายละเอียดจากภาพ (vision):**

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

---

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

**รายละเอียดจากภาพ (vision):**

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

---

## Slide 35: Recovery Techniques  *(visual)*
Rollback-Recovery

 checkpointing logging

uncoordinated coordinated communication pessimistic optimistic causal
 -induced

 blocking non-blocking model-based index-based

**รายละเอียดจากภาพ (vision):**

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

---

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

---

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

**รายละเอียดจากภาพ (vision):**

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

---

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

---

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

**รายละเอียดจากภาพ (vision):**

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

---

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

---

## Slide 41: Coordinated Checkpointing (3)  *(visual)*
Overall execution graph

**รายละเอียดจากภาพ (vision):**

**ชื่อเรื่อง (title):** Coordinated Checkpointing (3) / **Overall execution graph**

**แผนภาพ space-time:** (4 เส้นเวลา: **P0: initiator**, **P1**, **P2**, **P3** เรียงบนลงล่าง)
- ลูกศรเส้นประ (dotted) กระจายจาก P0 ลงไปยัง P1, P2, P3 กำกับคำ: **checkpoint requests**
- ลูกศรเส้นประจำนวนมาก (acknowledgment) ชี้กลับขึ้นไปรวมที่ P0 กำกับคำ: **acknowledgments**
- ป้ายด้านขวาบน: **Commit** (มีเส้นประโค้งสีน้ำเงินทแยงผ่านปลายขวาของเส้นเวลา P0..P3)
- เส้นประสีน้ำเงิน (แนวตั้ง/ทแยงเล็กน้อย) แสดง cut หลัง Commit
- ป้ายชื่อ process: **P0: initiator** (ด้านขวาบน), **P1**, **P2**, **P3**

- เลขหน้า (มุมขวาล่าง): 41

---

---

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

**รายละเอียดจากภาพ (vision):**

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

---

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

**รายละเอียดจากภาพ (vision):**

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

---

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

---

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

---

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

---

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

---

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

---

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

**รายละเอียดจากภาพ (vision):**

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

---

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

---

## Slide 51: HW04: Checkpointing  *(visual)*
▪ Find the consistent cuts in the figure below (passing by ▓)

▪ The recovery line that you found is consistent, strongly consistent or
 inconsistent?

**รายละเอียดจากภาพ (vision):**

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

---

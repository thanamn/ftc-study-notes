# FTC02_Fault_Tolerant_Systems — Enriched (slide text + vision of visual slides)

> Text = exact extraction from the born-digital PDF. For `visual` slides, a faithful description of the figure/table/formula is added under **รายละเอียดจากภาพ**. Vision descriptions are model-produced and marked as such.

## Slide 1: Fault Tolerant Systems - Overview
(Fault Tolerance in Distributed Systems)

 2110473 Fault Tolerant Computing

---

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

---

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

---

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

---

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

**รายละเอียดจากภาพ (vision):**

**หัวข้อ (title):** Attributes, Consequences and Strategies

สไลด์แสดงแผนภาพ 3 กล่องสี (attribute / consequence / strategy) แต่ละกล่องมี bullet list และมี "bubble" (กรอบคำพูด) สีต่าง ๆ ชี้เข้ามาพร้อมคำถาม

**กล่องสีชมพู (ด้านซ้าย) — Attributes**
- Availability
- Reliability
- Safety
- Confidentiality
- Integrity
- Maintainability

**bubble สีม่วงอ่อน (ชี้ไปที่ Attributes):** "What is a Dependable system?"

**กล่องสีฟ้า (กลาง) — Consequences**
- Fault
- Error
- Failure

**bubble สีฟ้าอ่อน (ชี้ไปที่ Consequences):** "How to distinguish faults?"

**กล่องสีส้ม (ล่างขวา) — Strategies**
- Fault prevention
- Fault tolerance
- Fault recovery
- Fault forecasting

**bubble สีเหลือง (ชี้ไปที่ Strategies):** "How to handle faults?"

- เลขหน้า: 5

---

---

## Slide 6: Terminology of Fault Tolerance
Fault causes Error results in Failure

• Fault - is a defect within the system

• Error - is observed by a deviation from the expected
 behavior of the system

• Failure occurs when the system can no longer
 perform as required (does not meet spec)

• Fault Tolerance - is ability of system to provide a
 service, even in the presence of errors

---

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

---

## Slide 8: Types of Fault  *(visual)*
(wrt attributes)
(Failure Mode of Distributed Systems)

**รายละเอียดจากภาพ (vision):**

**หัวข้อ (title):** Types of Fault (wrt attributes)
**หัวข้อรอง (subtitle):** (Failure Mode of Distributed Systems)

ตาราง 2 คอลัมน์ (หัวตารางพื้นสีเขียวอ่อน เนื้อหาพื้นสีฟ้าอ่อน):

| Type of failure | Description |
|---|---|
| Crash failure | A server halts, but is working correctly until it halts |
| &nbsp;&nbsp;Amnesia crash | Lost all history, must be reboot |
| &nbsp;&nbsp;Pause crash | Still remember state before crash, can be recovered |
| &nbsp;&nbsp;Halting crash | Hardware failure, must be replaced or re-installed |
| Omission failure | A server fails to respond to incoming requests |
| &nbsp;&nbsp;Receive omission | A server fails to receive incoming messages |
| &nbsp;&nbsp;Send omission | A server fails to send messages |
| Timing failure | A server's response lies outside the specified time interval |
| Response failure | The server's response is incorrect |
| &nbsp;&nbsp;Value failure | The value of the response is wrong |
| &nbsp;&nbsp;State transition failure | The server deviates from the correct flow of control |
| Arbitrary failure | A server may produce arbitrary responses at arbitrary times |

- เลขหน้า: 8

---

---

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

**รายละเอียดจากภาพ (vision):**

**หัวข้อ (title):** Failure Rate

**เนื้อหา:**
- λ(t) = Component failure rate
  - Measured in FITS (failures per 10⁹ hours)
- e.g. NASA Flight = 1 FIT, Computers = 10⁵-10⁶ FITs, Human Life (85yrs) = 1,343 FITs
  - (สีข้อความ: "NASA Flight = 1 FIT" สีเขียว, "Computers = 10⁵-10⁶ FITs" สีฟ้า, "Human Life (85yrs) = 1,343 FITs" สีแดง)

**กราฟ (เส้นโค้งอ่างอาบน้ำ / bathtub curve):**
- แกน Y: Failure rate (มีลูกศรชี้ขึ้น)
- แกน X: Time (มีลูกศรชี้ขวา)
- แบ่งเป็น 3 ช่วงด้วยเส้นประแนวตั้ง: **Infant mortality** (ซ้าย), **Working life** (กลาง), **Wearout** (ขวา)
- เส้นทึบ **Overall curve** เป็นรูปอ่างอาบน้ำ (ลงต่ำช่วงกลางแล้วขึ้นช่วงท้าย) มีลูกศรชี้ลงมาที่เส้น (slope) อยู่กลางกราฟ
- ป้าย **Random failures** อยู่ใต้ Overall curve มีลูกศรชี้ลง
- เส้นประ **Early failures** (ด้านซ้าย) ลดลง และมีลูกศรชี้ไปทางขวา
- เส้นประ **Wearout failures** (ด้านขวา) เพิ่มขึ้น และมีลูกศรชี้ไปทางซ้าย
- เลขหน้า: 9

---

---

## Slide 10: Bathtub curve for software reliability  *(visual)*
10

**รายละเอียดจากภาพ (vision):**

**หัวข้อ (title):** Bathtub curve for software reliability

**กราฟ:**
- แกน Y: Failure Rate (ข้อความหมุนแนวตั้ง) มีป้าย **λ** กำกับที่ระดับคงที่ (เส้นประแนวนอนลากจาก λ ไปทางขวา)
- แกน X: Time
- แบ่งเป็น 3 ช่วงด้วยเส้นประแนวตั้ง: **Test/Debug** (ซ้าย), **Useful Life** (กลาง), **Obsolescence** (ขวา)
- เส้นโค้งเริ่มสูงช่วง Test/Debug แล้วลดลง มีจุดกระโดดขึ้น (spike) หลายครั้ง แต่ละครั้งมีป้าย **Upgrade** เขียนแนวตั้งกำกับลูกศร (มีทั้งหมด 3 จุด Upgrade)
- หลัง Upgrade ครั้งที่ 3 เส้นโค้งลดลงแล้วคงที่ระดับหนึ่งตลอดช่วง Obsolescence
- เลขหน้า: 10

---

---

## Slide 11: Reliability Modeling  *(visual)*
11

**รายละเอียดจากภาพ (vision):**

**หัวข้อ (title):** Reliability Modeling

สไลด์มี 4 แผนภาพ จัดเป็น 2 แถว 2 คอลัมน์

**บนซ้าย — Physical schema (ระบบสูบน้ำ):**
- ลูกศรสีฟ้าเข้าจากซ้าย ป้าย **Concentrate and squeezing**
- วงกลมมีรูปสามเหลี่ยมภายใน (สัญลักษณ์ pump) ป้ายด้านบน **pump**
- ลูกศรสีฟ้าชี้ไปขวาเข้าสู่กล่องสี่เหลี่ยมแบ่งเป็นช่อง ๆ (filter) ป้ายด้านบน **filter**
- ลูกศรออกทางขวา ป้าย **Squeezing**
- ลูกศรออกลงด้านล่าง ป้าย **Concentrate**

**บนขวา — Reliability schema:**
- เส้นต่อจากซ้ายเข้า → กล่องสีส้ม **Pump** → เส้น → กล่องสีส้ม **Filter** → เส้นออกขวา (อนุกรม / series)

**ล่างซ้าย — Physical schema (เครื่องกำเนิดไฟฟ้า):**
- เส้นสีฟ้าแนวนอน 2 เส้น (บัส) ด้านบน ป้าย **Generator A** และ **Generator B**
- กล่องสี่เหลี่ยมแบ่งช่อง (เครื่องกำเนิด) 2 กล่องด้านล่าง มีลูกศรสีฟ้าชี้ขึ้นจากแต่ละกล่องไปยังบัส

**ล่างขวา — Reliability schema:**
- กล่องสีส้ม **Generator A** และ **Generator B** ต่อแบบขนาน (parallel) — มีเส้นแยกจากซ้ายเข้า 2 กล่อง แล้วรวมกลับทางขวา

- เลขหน้า: 11

---

---

## Slide 12: Reliability Block Diagram  *(visual)*
• Series system works if all component work
• Parallel system works if @least one work

**รายละเอียดจากภาพ (vision):**

**หัวข้อ (title):** Reliability Block Diagram

**เนื้อหา:**
- Series system works if all component work
- Parallel system works if @least one work

**แผนภาพ:**
- ซ้าย: ระบบอนุกรม — กล่องสีส้มหมายเลข 1 → 2 → 3 → 4 ต่อเรียงกันเป็นแนวราบ (เส้นจากซ้ายเข้าและออกขวา)
- ขวา: ระบบขนาน — กล่องสีส้มหมายเลข 1, 2, 3, 4 วางเรียงแนวตั้ง โดยมีเส้น bus ทำ paralle จุดออก/เข้า 1→2→3→4 (ทุกกล่องอยู่ระหว่างบัสซ้ายและบัสขวาเดียวกัน)
- เลขหน้า: 12

---

---

## Slide 13: Series-Parallel System  *(visual)*
13

**รายละเอียดจากภาพ (vision):**

**หัวข้อ (title):** Series-Parallel System

**แผนภาพ Reliability Block Diagram ประกอบ 9 กล่อง:**
- บล็อกที่ 1: กล่อง 1 และ 2 ต่อขนาน (parallel)
- ต่ออนุกรมไปยังบล็อกที่ 2: กล่อง 3, 4, 5 ต่อขนานกัน
- ต่ออนุกรมไปยังบล็อกที่ 3: กล่อง 6, 7, 8, 9 ต่อขนานกัน
- ทางเข้าเส้นเดียวจากซ้าย ผ่านทั้ง 3 บล็อกตามลำดับ แล้วออกทางขวา
- เลขหน้า: 13

---

---

## Slide 14: Minimal Path Set  *(visual)*
• A subset of the system components such that
 the operation of all the components in the
 subset implies the operation of the system.

**รายละเอียดจากภาพ (vision):**

**หัวข้อ (title):** Minimal Path Set

**เนื้อหา:**
- A subset of the system components such that the operation of all the components in the subset implies the operation of the system.

**แผนภาพซ้าย — วงจรระบบ (bridge):** กล่อง 1 (บนซ้าย), 2 (บนขวา), 3 (กลาง), 4 (ล่างซ้าย), 5 (ล่างขวา) เชื่อมกันเป็นโครงข่าย bridge มีเส้นประสีฟ้า (dashed) แสดงเส้นทางต่าง ๆ ทับบนแผนภาพ (มี 3 เส้นทาง ระบุ [labels ที่เส้นประคาดว่าเป็น 1-2-3-4-5; ไม่มีตัวอักษรกำกับชัดเจน])

**แผนภาพขวา — MPS ที่แปลงเป็นอนุกรม-ขนาน:** 4 แถวขนานกัน:
- แถว 1: กล่อง 1 → 2
- แถว 2: กล่อง 1 → 3 → 5
- แถว 3: กล่อง 4 → 3 → 2
- แถว 4: กล่อง 4 → 5
(ทุกแถวเริ่มจากบัสซ้ายเดียวกันและจบที่บัสขวาเดียวกัน)

- เลขหน้า: 14

---

---

## Slide 15: Minimal Cut Set  *(visual)*
• A subset of the system components, such that
 the failure of all components in the subset
 does not imply the operation of the system

**รายละเอียดจากภาพ (vision):**

**หัวข้อ (title):** Minimal Cut Set

**เนื้อหา:**
- A subset of the system components, such that the failure of all components in the subset does not imply the operation of the system

**แผนภาพซ้าย — วงจรระบบ (bridge):** กล่อง 1 (บนซ้าย), 2 (บนขวา), 3 (กลาง), 4 (ล่างซ้าย), 5 (ล่างขวา) เชื่อมกันเป็นโครงข่าย มีเส้นประสีฟ้าแสดง minimal cut sets ทับบนแผนภาพ (เส้น 1-4, 2-5, 1-3-5, 4-3-2)

**แผนภาพขวา — MCS ที่แปลงเป็นอนุกรม-ขนาน:** 4 กลุ่มต่ออนุกรมกัน แต่ละกลุ่มมีกล่องต่อขนาน:
- กลุ่ม 1: 1 ขนานกับ 4
- กลุ่ม 2: 1, 3, 5 ขนานกัน
- กลุ่ม 3: 4, 3, 2 ขนานกัน
- กลุ่ม 4: 2 ขนานกับ 5
- เลขหน้า: 15

---

---

## Slide 16: System Failure Rate
❑System constructed from components
❑No Fault Tolerance
 - Any component fails, whole system fails

 k
  =  sys c , i 
 i =1

---

## Slide 17: Reliability
❑If component working at time 0
 - R(t) = Probability still working at time t
❑Exponential Failure Law
 - If failure rate assumed constant
 • Good approximation if past infant mortality period

 −t R (t ) = e

---

## Slide 18: Reliability for Series System
❑Series System
 - All components need to work for system to work

 A B C

 R = R R R sys A B C

---

## Slide 19: How to make more Reliable
Reliability of n-Component system, each having
failure rate :

 𝑅𝑡= 𝑒−𝑛𝜆𝑡

• Reduce Failure Rate 
• Reduce Number of Components n
• Reduce Time t
Alternative:
• Introduce Redundancy

---

## Slide 20: System Reliability with Redundancy  *(visual)*
❑System reliability with component B in Parallel
 - Can tolerate one component B failing

 B
 A C
 B

 R = R 1 − 1( − R ) 2 R = R ( 2 R − R 2 ) R sys A  B  C A B B C

**รายละเอียดจากภาพ (vision):**

**หัวข้อ (title):** System Reliability with Redundancy

**เนื้อหา:**
- System reliability with component *B* in Parallel
  - Can tolerate one component *B* failing

**แผนภาพ RBD:** กล่อง **A** → (กล่อง **B** สองกล่องต่อขนานกัน) → กล่อง **C**

**สูตร (แสดงท้ายสไลด์):**
- R_sys = R_A [1 − (1 − R_B)²] R_C = R_A (2 R_B − R_B²) R_C
- เลขหน้า: 20

---

---

## Slide 21: System Reliability
• Series System
 𝑁
 𝑅𝑜𝑣𝑒𝑟𝑎𝑙𝑙= ෑ 𝑅𝑖
 𝑖=1
• Parallel System
 𝑁
 𝑅𝑜𝑣𝑒𝑟𝑎𝑙𝑙= 1 −ෑ 1 −𝑅𝑖
 𝑖=1

---

## Slide 22: Some Simple Probability Distributions  *(visual)*
• Cumulative distribution function: CDF 𝑓𝑡= 𝑝𝑟𝑜𝑏𝑡≤𝑥≤𝑡+𝑑𝑡 = 𝑑𝐹(𝑡)/𝑑𝑡 𝑑𝑡
• Probability density function: pdf 𝐹𝑡= 𝑝𝑟𝑜𝑏𝑥≤𝑓= ׬ 𝑡𝑓𝑥𝑑𝑥 0

**รายละเอียดจากภาพ (vision):**

**หัวข้อ (title):** Some Simple Probability Distributions

**เนื้อหาและสูตร:**
- Cumulative distribution function: CDF
  - f(t) = prob[t ≤ x ≤ t + dt] / dt = dF(t)/dt
- Probability density function: pdf
  - F(t) = prob[x ≤ f] = ∫₀ᵗ f(x) dx

**กราฟ 2 แถว 4 คอลัมน์:**
- แถวบน แกน Y กำกับ **F(x)** มีจุด **1** อยู่บนแกน, กราฟติดป้าย **CDF** ทั้ง 4 รูป:
  1. Uniform: เส้นตรงเพิ่มขึ้นเป็นขั้นบันได (linear rising) แล้วคงที่
  2. Exponential: เส้นโค้งเพิ่มขึ้นแบบอิ่มตัว (concave)
  3. Normal: เส้นรูปตัว S (sigmoid)
  4. Binomial: เส้นขั้นบันได (staircase) ขึ้นทีละขั้น
- แถวล่าง แกน Y กำกับ **f(x)**, กราฟติดป้าย **pdf** ทั้ง 4 รูป:
  1. Uniform: สี่เหลี่ยมผืนผ้า (แบนราบ) พื้นที่แรเงา
  2. Exponential: เส้นโค้งลดลงแบบทวีคูณ พื้นที่แรเงาใต้เส้น
  3. Normal: เส้นโค้งกระดิ่ง (bell curve) พื้นที่แรเงา
  4. Binomial: แท่งกราฟหลายแท่งสูงต่ำ (discrete bars)
- ป้ายชื่อใต้กราฟ (เรียงซ้ายไปขวา): **Uniform, Exponential, Normal, Binomial**
- เลขหน้า: 22

---

---

## Slide 23: Reliability and MTTF  *(visual)*
23

**รายละเอียดจากภาพ (vision):**

**หัวข้อ (title):** Reliability and MTTF

**คอลัมน์ซ้าย — Reliability: R(t)**
- Probability that system remains in the "Good" state through the interval [0, t]
- R(t + dt) = R(t) [1 − z(t) dt]
  - ป้ายกำกับใต้เทอม: **Hazard function**
- R(t) = 1 − F(t) — ป้ายกำกับทางขวา: **CDF of the system lifetime, or its unreliability**
- Constant hazard function z(t) = λ ⇒ R(t) = e^(−λ·t)
  - (system failure rate is independent of its age)
- กล่องสีเหลืองไฮไลต์ข้อความสีแดง: **Exponential reliability law**

**คอลัมน์ขวา — Two-state nonrepairable system:**
- รูป state diagram: วงกลม **Up** —(ลูกศรมีป้าย **Failure**)→ วงกลม **Down**
- ป้าย **Start state** อยู่ทางซ้ายของวงกลม Up

**ส่วนล่าง — Mean time to failure: MTTF** (สีน้ำเงิน/แดง)
- MTTF = ∫₀^{+∞} t f(t) dt = ∫₀^{+∞} R(t) dt
  - ป้ายใต้เทอมแรก: **Expected value of lifetime**
  - ป้ายใต้เทอมที่สอง: **Area under the reliability curve (easily provable)**
- เลขหน้า: 23

---

---

## Slide 24: Mean-Time-to-Failure (MTTF)
❑Average time before system fails
 - Equal to area under reliability curve

 
 MTTF = R (t )dt 
 0

❑For Exponential Failure Law

 
 t 1 MTTF = e −dt =   0

---

## Slide 25: Comparing Reliabilities  *(visual)*
25

**รายละเอียดจากภาพ (vision):**

**หัวข้อ (title):** Comparing Reliabilities

**คอลัมน์ซ้าย (นิยาม/สูตร สีน้ำเงินคือหัวข้อ):**
- Reliability difference: R₂ − R₁
- Reliability gain: R₂ / R₁
- Reliability improvement factor
  - RIF_{2/1} = [1−R₁(t_M)]/[1−R₂(t_M)]
  - Example: [1 − 0.9] / [1 − 0.99] = 10
- Reliability improv. index
  - RII = log R₁(t_M) / log R₂(t_M)
- Mission time extension
  - MTE_{2/1}(r_G) = T₂(r_G) − T₁(r_G)
- Mission time improv. factor:
  - MTIF_{2/1}(r_G) = T₂(r_G) / T₁(r_G)

**คอลัมน์ขวา — กราฟ Reliability functions for Systems 1/2:**
- แกน Y: System Reliability (R) ตั้งแต่ **0.0** ถึง **1.0**; มีป้าย R₂(t_M), R₁(t_M) และ **r_G** (มีเส้นแนวนอนสีเขียวที่ระดับ r_G)
- แกน X: Time (t); มีป้ายจุด **T₁(r_G)**, **t_M**, **T₂(r_G)**, **MTTF₂**, **MTTF₁**
- เส้นโค้ง R₂(t) อยู่เหนือเส้นโค้ง R₁(t) (R₂ ลดช้ากว่า)
- มีแถบแนวนอนสีเขียวที่ระดับ r_G และแถบแนวตั้งสีแดงที่ตำแหน่ง **t_M**
- เลขหน้า: 25

---

---

## Slide 26: Repair Rate and MTTR
❑= rate at which system repaired
 - constant for the exponential case
 - analogous to failure rate 
❑Maintainability often modeled as
 − t M (t ) =1 − e

❑Mean-Time-to-Repair (MTTR) = 1/

---

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

**รายละเอียดจากภาพ (vision):**

**หัวข้อ (title):** Availability

**เนื้อหา:**
- System Availability
  - Fraction of time system is operational
- สูตร: system availability = MTTF / (MTTF + MTTR)

**กราฟ (state over time):**
- แกน Y: **S** มีสเกล **1** และ **0**
- แกน X: **t** มีจุดกำกับ **t₀**, **t₁**, **t₂**, **t₃**, **t₄**
- เส้นระดับ 0 (ล่าง) เป็นแนวราบ; มีช่วงที่ระบบทำงาน (S = 1) เป็นรูปสี่เหลี่ยมผืนผ้า (หรือทรงสี่เหลี่ยมคางหมู) ยกขึ้น 2 ช่วง
  - ช่วงที่ 1 ระหว่าง t₁ ถึง t₂
  - ช่วงที่ 2 ระหว่าง t₃ ถึง t₄
- กล่องข้อความพื้นเขียวอ่อน: **Normal system operation** พร้อมลูกศรชี้ลง 2 เส้นมาที่ช่วงการทำงาน
- กล่องข้อความพื้นชมพู: **failures** พร้อมลูกศรชี้จากกล่องไปยังช่วงที่ระบบล่ม (ระหว่าง t₂ ถึง t₃ และหลัง t₄)
- เลขหน้า: 27

---

---

## Slide 28: Availability (cont.)
❑Telephone Systems
 - Required to have system availability of 0.9999
 ("four nines")
❑High-Reliability Systems
 - May require 7 or more nines
❑Fault-Tolerant Design
 - Needed to achieve such high availability from less
 reliable components

---

## Slide 29: Availability in Series  *(visual)*
• A = Ax Ay

**รายละเอียดจากภาพ (vision):**

**หัวข้อ (title):** Availability in Series

**เนื้อหา:**
- สูตร: A = A_x A_y
- แผนภาพ: เส้นจากซ้ายเข้า → กล่อง **Part X** → กล่อง **Part Y** → ออกขวา (อนุกรม)

**ตาราง:**

| Component | Availability | Downtime |
|---|---|---|
| X | 99% (2-nines) | 3.65 days/year |
| Y | 99.99% (4-nines) | 52 minutes/year |
| X and Y Combined | 98.99% | 3.69 days/year |

- เลขหน้า: 29

---

---

## Slide 30: Availability in Parallel  *(visual)*
• A = )2 1-(1-Ax

**รายละเอียดจากภาพ (vision):**

**หัวข้อ (title):** Availability in Parallel

**เนื้อหา:**
- สูตร: A = 1-(1-A_x)²
- แผนภาพ: เส้นจากซ้ายเข้า แล้วแยกเป็น 2 ทาง ผ่านกล่อง **Part X** สองกล่องต่อขนานกัน แล้วรวมกลับออกขวา

**ตาราง:**

| Component | Availability | Downtime |
|---|---|---|
| X | 99% (2-nines) | 3.65 days/year |
| Two X components operating in parallel | 99.99% (4-nines) | 52 minutes/year |
| Three X components operating in parallel | 99.9999% (6-nines) | 31 seconds /year ! |

- เลขหน้า: 30

---

---

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

---

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

---

## Slide 33: Multiple Nodes Single Spare  *(visual)*
• The number of Failure modes, f, is

• The probability of failure of the system, F, is
 the probability that any two nodes will fail

• System Availability, A, is

Note:
For Five-node system (node availability is 0.99),
The number of failure modes is ??
The availability of this five-node system is ??

**รายละเอียดจากภาพ (vision):**

**หัวข้อ (title):** Multiple Nodes Single Spare

**เนื้อหาและสูตร:**
- The number of Failure modes, *f*, is
  - f = n(n − 1) / 2
- The probability of failure of the system, *F*, is the probability that any two nodes will fail
  - F = (n(n − 1) / 2) (1 − a)²
- System Availability, *A*, is
  - A = 1 − F = 1 − (n(n − 1) / 2) (1 − a)²

**แผนภาพ (ขวา):** โหนดสีเหลือง 5 โหนดเชื่อมกับ cloud สีเทากลางที่เขียนกำกับ **Network**
- กล่อง **Node 1** (ซ้าย), **Node 2** (บน), **Node 3** (ขวาบน — มีกากบาทสีแดงทับ = fail), **Node 4** (ขวา), **Node 5** (ล่าง)

**Note:** (ตัวเอียง)
- For Five-node system (node availability is 0.99),
- The number of failure modes is ??
- The availability of this five-node system is ??
- เลขหน้า: 33

---

---

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

**รายละเอียดจากภาพ (vision):**

**หัวข้อ (title):** Multiple Nodes Single Spare

สไลด์นี้เป็นสไลด์เดียวกับ Slide 33 แต่มีกล่องข้อความคำตอบซ้อนทับบนเนื้อหาเดิม

**เนื้อหาเดิม (ยังเห็นได้):**
- The number of Failure modes, *f*, is
- The probability of failure of the system, *F*, is / the ...
- System Availability, *A*, is
  - A = 1 − F = 1 − (n(n − 1) / 2) (1 − a)²

**กล่องข้อความคำตอบ (ทับด้านบน):**
- the number of failure modes is **ten** (คำว่า ten สีแดง)
- the availability of a five-node system is [1 - 10(.01)2], or .999. This is three 9s of availability

**แผนภาพ (ขวา):** เหมือน Slide 33 — โหนดสีเหลือง 5 โหนด (Node 1–5) เชื่อมกับ **Network** โดย **Node 3** มีกากบาทสีแดง (fail)

**Note:** ข้อความเหมือน Slide 33 (For Five-node system (node availability is 0.99), ... ??)

- เลขหน้า: 34

---

---

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

**รายละเอียดจากภาพ (vision):**

**หัวข้อ (title):** Multiple Nodes Multiple Spares

**เนื้อหาและสูตร:**
- The number of failure modes, *f*, is the number of ways that s+1 nodes out of n nodes can fail
  - f = n! / ( (s + 1)! (n − s − 1)! )
- The probability of failure is
  - F = f (1 − a)^{s+1}
- The system availability is
  - A = 1 − f (1 − a)^{s+1}

**แผนภาพ (ขวา):** โหนดสีเหลือง 6 โหนดเชื่อมกับ cloud **Network**
- **Node 1** (ซ้าย), **Node 2** (บนซ้าย), **Node 3** (บนขวา — มีกากบาทสีแดง = fail), **Node 4** (ขวา), **Node 5** (ล่างขวา — มีกากบาทสีแดง = fail), **Node 6** (ล่างซ้าย)

**Note:** (ตัวเอียง ข้อความคำตอบสีแดง)
- For Six-node system wt Two-spare (node availability is 0.99),
- The number of failure modes is ?? => 20
- The availability of this six-node system is ?? =>1-20*(1-0.99)^3 = 0.99998
- เลขหน้า: 35

---

---

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

**รายละเอียดจากภาพ (vision):**

**หัวข้อ (title):** Relationship Between Availability and Reliability

**ตาราง (หัวตารางพื้นน้ำเงิน ตัวอักษรขาว):**

| Reliability | Maintainability | Availability |
|---|---|---|
| Constant | Decrease | ? |
| Constant | Increase | ? |
| Increase | Constant | ? |
| Decrease | Constant | ? |

**Notes:** (ตัวเอียง)
- Reliability represents the probability of components, parts and systems to perform their required functions for a desired period of time without failure in specified environments with a desired confidence.
- Availability represents the probability that the system is capable of conducting its required function when it is called upon given that it is not failed or undergoing a repair action.
- An increase in maintainability implies a decrease in the time it takes to perform maintenance actions.
- Therefore, not only is availability a function of reliability, but it is also a function of maintainability.
- เลขหน้า: 36

---

---

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

---

## Slide 38: Check Yourself 1  *(visual)*
• Calculate the Reliability of TMR system (Triple
 Modular Redundant system)
 - Reliability of U1 = U2 = U3 = RU, Voter = RV

**รายละเอียดจากภาพ (vision):**

**หัวข้อ (title):** Check Yourself 1

**เนื้อหา:**
- Calculate the Reliability of TMR system (Triple Modular Redundant system)
  - Reliability of U1 = U2 = U3 = RU, Voter = RV

**แผนภาพ (TMR circuit):**
- ป้าย **Input** ทางซ้าย มีเส้นแยกเป็น 3 สาขา (ลูกศรชี้ขวา) เข้าหน่วย **U₁**, **U₂**, **U₃** (กล่องสี่เหลี่ยม)
- ทั้งสามส่งสัญญาณเข้าสู่วงกลม **Voter** (ลูกศร 3 เส้นพุ่งเข้าหา Voter)
- Voter ส่งออกทางขวาเป็นลูกศรไปยังป้าย **Output**
- เลขหน้า: 38

---

---

## Slide 39: Check Yourself 1 - Solution  *(visual)*
• Calculate the Reliability of TMR system (Triple
 Modular Redundant system)
 - Reliability of U1 = U2 = U3 = RU, Voter = RV

 𝑅𝑈3 + 3𝑅𝑈2 1 −𝑅𝑈 𝑅𝑉= (3𝑅𝑈2−2𝑅𝑈3)𝑅𝑉𝑅𝑡𝑚𝑟=

**รายละเอียดจากภาพ (vision):**

**หัวข้อ (title):** Check Yourself 1 - Solution

เนื้อหาและแผนภาพเหมือน Slide 38 (TMR: Input → U₁, U₂, U₃ → Voter → Output; Reliability of U1 = U2 = U3 = RU, Voter = RV)

**กล่องสูตร (พื้นสีชมพูอ่อน ขอบสีส้ม):**
- R_tmr = ( RU³ + 3RU²(1 − RU) ) RV = ( 3RU² − 2RU³ ) RV

- เลขหน้า: 39

---

---

## Slide 40: Check Yourself 2  *(visual)*
• Parallel-to-series interconnection scheme and Series-to-
 parallel interconnection scheme
• Find the both reliabilities, 𝑅𝑃𝑆and 𝑅𝑆𝑃
• If each subsystem reliability is 𝑅, find 𝑅𝑃𝑆and 𝑅𝑆𝑃and
 which one is more reliable?

 A B A B

 A B A B

 PS scheme SP scheme 40

**รายละเอียดจากภาพ (vision):**

**หัวข้อ (title):** Check Yourself 2

**เนื้อหา:**
- Parallel-to-series interconnection scheme and Series-to-parallel interconnection scheme
- Find the both reliabilities, R_{PS} and R_{SP}
- If each subsystem reliability is R, find R_{PS} and R_{SP} and which one is more reliable?

**แผนภาพซ้าย — PS scheme:** กล่อง **A** สองกล่องต่อขนานกัน ต่ออนุกรมกับกล่อง **B** สองกล่องที่ต่อขนานกัน (บล็อก A ขนาน → บล็อก B ขนาน)

**แผนภาพขวา — SP scheme:** กล่อง **A** ต่ออนุกรมกับกล่อง **B** (คู่บน) ขนานกับอีกเส้นที่กล่อง **A** ต่ออนุกรมกับกล่อง **B** (คู่ล่าง) — โครงสร้างตาราง 2×2

- เลขหน้า: 40

---

---

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

**รายละเอียดจากภาพ (vision):**

**หัวข้อ (title):** Check Yourself 2 - Solution

เนื้อหาตอนบนและแผนภาพเหมือน Slide 40 (PS scheme และ SP scheme)

**กล่องสูตร (พื้นสีส้มอ่อน ขอบสีแดง):**
- RPS = [ 1 − ( 1 − RA )^2 ] [ 1 − ( 1 − RB )^2 ]  = R^4 − 4 R^3 + 4 R^2
- RSP = [ 1 − ( 1 − RA RB ) ( 1 − RA RB ) ]  = 2 R^2 − R^4
- (บรรทัดล่างสุด สีแดง) RPS > RSP

- เลขหน้า: 41

---

---

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

---

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

---

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

---

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

---

## Slide 46: RAID  *(visual)*
(Redundant Array of Independent Disks)

 RAID has been classified into several levels: 0, 1, 2, 3, 4, 5, 6, 10, 50,
 each level provides a different degree of fault tolerance

**รายละเอียดจากภาพ (vision):**

**หัวข้อ (title):** RAID
**หัวข้อรอง (subtitle):** (Redundant Array of Independent Disks)

**แผนภาพ RAID LEVEL 1 : Mirroring & Duplexing** (ตัวเอียง ด้านบนซ้าย):
- มีดิสก์ (ทรงกระบอก) เรียงกัน 8 ลูก แต่ละลูกมีตัวอักษร A, B, C, D (เรียงลงล่าง)
  - ดิสก์ 1: A B C D
  - ดิสก์ 2: A B C D (มีเครื่องหมาย "=" ระหว่างดิสก์ 1 กับ 2) ป้าย **Mirroring** ใต้ดิสก์นี้
  - ดิสก์ 3: E F G H
  - ดิสก์ 4: E F G H ("=" ระหว่าง 3 กับ 4) ป้าย **Mirroring**
  - ดิสก์ 5: I J K L
  - ดิสก์ 6: I J K L ("=") ป้าย **Mirroring**
  - ดิสก์ 7: M N O P
  - ดิสก์ 8: M N O P ("=") ป้าย **Mirroring**
- ทุกดิสก์เชื่อมต่อกับบัสแนวนอนด้านบน

**แผนภาพ RAID LEVEL 2 : Hamming Code ECC** (ด้านล่าง):
- กลุ่มดิสก์ข้อมูล 4 ลูก:
  - ดิสก์ A0 B0 C0 D0
  - ดิสก์ A1 B1 C1 D1
  - ดิสก์ A2 B2 C2 D2
  - ดิสก์ A3 B3 C3 D3
  - ป้ายกำกับด้านล่าง: "A0 to A3 = Word A", "C0 to C3 = Word C", "B0 to B3 = Word B", "D0 to D3 = Word D"
- กลุ่มดิสก์ ECC 3 ลูก (ด้านขวา) แต่ละช่องเป็น ECC ของ word:
  - ดิสก์ 1: ECC / Ax, ECC / Bx, ECC / Cx, ECC / Dx
  - ดิสก์ 2: ECC / Ay, ECC / By, ECC / Cy, ECC / Dy
  - ดิสก์ 3: ECC / Az, ECC / Bz, ECC / Cz, ECC / Dz
  - ป้ายกำกับด้านล่าง: "ECC/Ax to Az = Word A ECC", "ECC/Cx to Cz = Word C ECC", "ECC/Bx to Bz = Word B ECC", "ECC/Dx to Dz = Word D ECC"
- มีเส้นเชื่อม (cross) แสดงการกระจาย ECC

**กล่องข้อความ (พื้นฟ้าอ่อน ด้านล่าง):**
**RAID** has been classified into several levels: 0, 1, 2, 3, 4, 5, 6, 10, 50, each level provides a different degree of fault tolerance

- เลขหน้า: 46

---

---

## Slide 47: Failure Masking by TMR  *(visual)*
(a) Original circuit
 (b) Triple modular redundancy (TMR)

**รายละเอียดจากภาพ (vision):**

**หัวข้อ (title):** Failure Masking by TMR

**แผนภาพ (a) — Original circuit:**
- สามวงกลมเรียงแนวนอน: **A** → **B** → **C** (เส้นเชื่อมตรง, มีป้าย **(a)** ด้านล่าง)

**แผนภาพ (b) — TMR circuit:**
- สามคอลัมน์ แต่ละคอลัมน์มี 3 หน่วย:
  - คอลัมน์ A: วงกลม **A1**, **A2**, **A3**
  - คอลัมน์ Voter 1: สามเหลี่ยม **V1** (มีป้าย **Voter** พร้อมลูกศรชี้ไปที่ V1), **V2**, **V3** (สามเหลี่ยมชี้ขวา)
  - คอลัมน์ B: วงกลม **B1**, **B2**, **B3**
  - คอลัมน์ Voter 2: สามเหลี่ยม **V4**, **V5**, **V6**
  - คอลัมน์ C: วงกลม **C1**, **C2**, **C3**
  - คอลัมน์ Voter 3: สามเหลี่ยม **V7**, **V8**, **V9**
- ทุก A1,A2,A3 เชื่อม (cross) เข้าทุก V1,V2,V3; ทุก V เชื่อมเข้าทุก B; B เชื่อม cross เข้า V4,V5,V6; เป็นต้น (การเชื่อมโยงแบบ fully-crossed)
- ป้าย **(b)** อยู่ด้านล่าง

**กล่องข้อความ (พื้นฟ้าอ่อน):**
- (a) Original circuit
- (b) Triple modular redundancy (TMR)
- เลขหน้า: 47

---

---

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

---

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

---

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

---

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

**รายละเอียดจากภาพ (vision):**

**หัวข้อ (title):** HW02: System Reliability

**เนื้อหา:**
- Find Minimal Path Set (MPS) and Minimal Cut Set (MCS) of each scheme (PP and AP)
- Find the both reliabilities, R_{PP} and R_{AP}
- If each subsystem reliability is R, find R_{PP} and R_{AP} and which one is more reliable?

**แผนภาพซ้าย — PP scheme:** กล่อง 3×3 (แถวละ A, B, C) โดยมีความเชื่อมโยงพิเศษ: Col A ทุกแถวต่อถึงกันในแนวตั้ง, Col B ทุกแถวต่อถึงกันบางส่วน, Col C ทุกแถวต่อถึงกัน — ดูเป็นโครงข่ายมีความเชื่อมต่อ 3 แถว × 3 คอลัมน์

**แผนภาพขวา — AP scheme:** กล่อง 3×3 (แถวละ A, B, C) โดยแต่ละคอลัมน์ (A, B, C) ต่ออนุกรมกันในแนวตั้ง (ทุก A อยู่บนบัสเดียวกัน ทุก B บนบัสเดียวกัน ทุก C บนบัสเดียวกัน) และแต่ละแถวต่ออนุกรมกัน — โครงสร้าง mesh/grid

**ป้ายกำกับด้านล่าง:** **PP scheme** (ซ้าย), **AP scheme** (ขวา)

- เลขหน้า: 51

---

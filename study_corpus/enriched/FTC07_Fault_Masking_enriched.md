# FTC07_Fault_Masking — Enriched (slide text + vision of visual slides)

> Text = exact extraction from the born-digital PDF. For `visual` slides, a faithful description of the figure/table/formula is added under **รายละเอียดจากภาพ**. Vision descriptions are model-produced and marked as such.

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

**รายละเอียดจากภาพ (vision):**

**หัวข้อ:** Home Exercise: Self Checking Circuits

- **Design a Self-Checking 2:4 Demultiplexer with Enable**

ไดอะแกรมบนสไลด์:

1. **วงจรเกต 2:4 Demultiplexer with Enable (มุมซ้ายบน)** — อินพุตจากซ้าย: `A`, `B`, `EN`
   - `A` ผ่านอินเวอร์เตอร์ (บับเบิล) แล้วแตกเป็น `A'`
   - `B` ผ่านอินเวอร์เตอร์แล้วแตกเป็น `B'`
   - เกต AND 4 ตัวทางขวา ให้เอาต์พุตกำกับ: `A'B'`, `AB'`, `A'B`, `AB`
   - โครงสร้าง: เส้น A และ A' ป้อนเข้า AND ทุกตัว; เส้น B/B' ป้อนด้วย; `EN` ป้อนเข้าทุก AND

2. **AND-array (กลาง ด้านบน)** — อินพุตด้านซ้ายจากบนลงล่าง: `\bar{A}`, `\bar{B}`, `A`, `B`, `EN` ป้อนเข้าชุดเกต AND (รูป D-shape, บับเบิลไม่มี) จำนวน 5 ตัว เรียงลงมา เอาต์พุตออกทางขวาเป็นเส้นขนานกัน

3. **OR-array (ขวา ด้านบน)** — อินพุตด้านซ้าย: `A`, `B`, `\bar{A}`, `\bar{B}`, `\overline{EN}` ป้อนเข้าชุดเกต OR (รูป D-shape มีบับเบิลด้านขวา) จำนวน 5 ตัว

4. **ไดอะแกรม AND-array + OR-array ประกอบกัน (กลาง ด้านล่าง)** — โครงสร้าง AND แล้วตามด้วย OR รวมกันในกรอบเส้นประ

5. **ไดอะแกรมบล็อกการตรวจสอบ (ขวา ด้านล่าง)** — บล็อกกำกับ:
   - บล็อกซ้าย: `A` / `B`
   - บล็อกกลาง: `EN` / `A'B'`
   - บล็อกขวา: `AB'` / `A'B`
   - ทั้งสามบล็อกส่งลงไปยังบล็อกสี่เหลี่ยมคู่ (ซ้าย-ขวา), บล็อกขวาส่งสัญญาณออกทางขวาเป็นป้าย `AB`
   - บล็อกคู่ส่งรวมลงยังบล็อกสี่เหลี่ยมด้านล่าง แล้วมีลูกศรชี้ลง (เอาต์พุต)

---

---

## Slide 2: Fault Masking
2110473 Fault Tolerant Computing

Prof.Behrooz Parhami, Graduate course materials, University of California, Santa Barbara
Daniel J.Sorin, M&C Publishers, Fault Tolerant Computer Architecture, Duke University, 2009
and others

---

## Slide 3: Schedule
• Mon 15 Sep, Self Checking✓
• Mon 22 Sep, No Class (Midterm)
• Mon 29 Sep, Fault Masking✓
• Mon 06 Oct, Midterm (Fault Tolerant Computing)
 - 13.00-16.00++/ #Eng4 no.18-15 (ON-SITE)
 - Open any Books including notebooks!!
• Mon 13 Oct, No Class (Comp.Holiday)
• Mon 20 Oct, Testing Digital Circuits (Online)

---

## Slide 4: Contents
• Handling Faults
• Interwoven Redundant Logic
• Combinatorial Modeling
• TMR & its application
• Replication & Voting
• Alternating Logic
• Fail-safe Systems

---

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

**รายละเอียดจากภาพ (vision):**

**หัวข้อ:** Handling Faults

**แผนภาพต้นไม้ (tree diagram) การจัดการ Fault:**

- บนสุด: บล็อก **Fault**
- แตกสองทาง:
  - **Avoid**
    - สาขาซ้าย ป้ายกำกับ **Quality Assurance** → บล็อก **Prevent** → ลูกศรลงไปยัง **Perfect**
    - สาขาขวา ป้ายกำกับ **Testing** → บล็อก **Remove** → ไปยังสี่เหลี่ยมข้าวหลามตัด (diamond) **Test**
      - จาก **Test**: ด้านซ้าย ป้าย **Detect** → บล็อก **Repair** → diamond **Full?**
        - **Full?** → ด้านซ้าย ป้าย **Yes** → **Fixed**
        - **Full?** → ด้านขวา ป้าย **No** → **Injured**
      - จาก **Test**: ด้านขวา ป้าย **Miss** → บล็อก **Discard** → **Screened**
  - **Tolerate**
    - สาขาซ้าย ป้ายกำกับ **Dynamic Redundancy** → บล็อก **Expose** → ไปยัง diamond **Monitor**
      - จาก **Monitor**: ด้านซ้าย ป้าย **Miss** → บล็อก **Abort** → **Faulty-safe**
      - จาก **Monitor**: ด้านขวา ป้าย **Detect** → บล็อก (ว่าง ไม่มีข้อความ) → diamond **Full?**
        - **Full?** → ด้านซ้าย ป้าย **No** → **Degraded**
        - **Full?** → ด้านขวา ป้าย **Yes** → **Restored**
    - สาขาขวา ป้ายกำกับ **Static Redundancy** → บล็อก **Mask** (ไฮไลต์สีฟ้า) → ลูกศรตรงลงไปยัง **Unaffected**

แถวล่างสุด (ป้ายกำกับรวม): **Component or System State**

รายการ state ใต้แผนภาพ (ซ้าย→ขวา): `Perfect`, `Fixed`, `Injured`, `Screened`, `Faulty`, `Faulty-safe`, `Degraded`, `Restored`, `Unaffected`

---

---

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

**รายละเอียดจากภาพ (vision):**

**หัวข้อ:** Design Techniques

**ไดอะแกรมลูกศร (flow) จาก fault sources → effects:**

คอลัมน์ซ้าย (รูปวงรี, fault sources):
- **Specification mistakes**
- **Implementation mistakes**
- **External disturbances**
- **Component defects**

คอลัมน์กลางซ้าย:
- **Software Faults**
- **Hardware Faults**

คอลัมน์กลางขวา:
- **Errors**

คอลัมน์ขวา:
- **System failures**

เส้นเชื่อม (ลูกศร):
- `Specification mistakes` → `Software Faults`
- `Specification mistakes` → `Hardware Faults`
- `Implementation mistakes` → `Software Faults`
- `Implementation mistakes` → `Hardware Faults`
- `External disturbances` → `Hardware Faults`
- `Component defects` → `Hardware Faults`
- `Software Faults` → `Errors`
- `Hardware Faults` → `Errors`
- `Errors` → `System failures`

เส้นประสีแดงตั้ง 3 เส้น พร้อมลูกศรสีแดงชี้ไปทางซ้าย (แสดงขอบเขตการป้องกัน) ป้ายกำกับด้านล่างของแต่ละเส้น:
- **Fault Avoidance** (เส้นประที่ 1 ระหว่าง fault sources กับ Software/Hardware Faults)
- **Fault Masking** (เส้นประที่ 2 ระหว่าง Software/Hardware Faults กับ Errors)
- **Fault Tolerance** (เส้นประที่ 3 ระหว่าง Errors กับ System failures)

---

---

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

**รายละเอียดจากภาพ (vision):**

**หัวข้อ:** Some Options for Fault Tolerance

**1. Detect and replace**
- **Dynamic redundancy** (cold/hot standby)
- Detection via
  - `-- coding, watchdog timer, self-checking`
  - `-- duplication (pair-and-spares)`

ไดอะแกรม (ขวาบน): บล็อก `1` ต่อกับวงกลม `D` ป้าย **Detector**; ด้านล่าง блок `2` ป้าย **Spare**; สวิตช์เลื่อนเลือกเส้นทาง (มีจุดต่อ switch) ลูกศรเข้า-ออก

**2. Mask**
- **Static redundancy**
- May revert to simplex instead of duplex
- Design challenges include
  - `-- synchronization for voting`
  - `-- voting on imprecise results`

ไดอะแกรม (ขวากลาง): บล็อก `1`, `2`, `3` ป้อนเข้าวงกลม `V` ป้าย **Voter** เอาต์พุตออกทางขวา

**3. Mask, diagnose, and reconfigure**
- **Hybrid redundancy**
- Fault masked at output, but diagnosed
  - `-- e.g., via comparison with voter output`
- Faulty circuit is replaced by spare
- Becomes static upon spare exhaustion

ไดอะแกรม (ขวาล่าง): บล็อก `1`, `2`, `3` และบล็อก `4` ป้าย **Spare** ด้านล่าง ป้อนเข้าบล็อกตั้ง `S` ป้าย **Switch-voter** ต่อกับวงกลม `V`; มีเส้นประจาก `V` กลับไปยัง `S`

---

---

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

**รายละเอียดจากภาพ (vision):**

**หัวข้อ:** Comparing Fault Tolerance Schemes

ตาราง (สองคอลัมน์):

| Advantages | Drawbacks |
|---|---|
| Less power (cold standby) | Coverage factor |
| Long life (just add spares) | Tolerance latency |
| Immediate masking | Power/area penalty |
| High safety | Voter critical |
| Immediate masking | Power/area penalty |
| Long life and high safety | Switch-voter critical |

ไดอะแกรมด้านขวา (แบบเดียวกับ Slide 7):
- **บน:** บล็อก `1` → วงกลม `D` ป้าย **Detector**; บล็อก `2` ป้าย **Spare** (สวิตช์เลื่อน)
- **กลาง:** บล็อก `1`, `2`, `3` → วงกลม `V` ป้าย **Voter**
- **ล่าง:** บล็อก `1`, `2`, `3` + บล็อก `4` ป้าย **Spare** → บล็อกตั้ง `S` ป้าย **Switch-voter** → วงกลม `V`; เส้นประจาก `V` กลับไป `S` (ป้าย **Switch-voter**)

---

---

## Slide 9: Contents
• Handling Faults
• Interwoven Redundant Logic
• Combinatorial Modeling
• TMR & its application
• Replication & Voting
• Alternating Logic
• Fail-safe Systems

---

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

**รายละเอียดจากภาพ (vision):**

**หัวข้อ:** Inherent Fault Masking in Logic Circuits

**วงจรลอจิก (ซ้าย):**
- อินพุต `a` (ค่า `1`), `b` (ค่า `0`) เข้าเกต AND → เอาต์พุต `e` (ค่า `0`)
- อินพุต `c` (ค่า `0`), `d` (ค่า `0`) เข้าเกต AND → เอาต์พุต `f` (ค่า `0`)
- `e` และ `f` เข้าเกต OR → เอาต์พุต `g` (ค่า `0`)
- `g` และ `h` (ค่า `1`) เข้าเกต AND → เอาต์พุต `z` (ค่า `0`)

**คำอธิบาย (ขวา):**
- `0 → 1 fault in b is critical` (สีแดง)
- `0 → 1 fault in c or d is not critical (it is masked)` (แดง + ฟ้า)
- `1 → 0 fault in a or h is not critical (it is masked)` (แดง + ฟ้า)

**ข้อความท้ายสไลด์:**
- Even nonredundant circuits have some masking capability
- Is there a way to exploit the inherent masking capabilities of logic gates to achieve fault tolerance?

---

---

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

**รายละเอียดจากภาพ (vision):**

**หัวข้อ:** AND-OR Logic Mask

**วงจร AND-OR (crosspoint array):**
- อินพุตด้านซ้าย (บนลงล่าง): `x4` (ค่า `1`), `x3` (ค่า `1`), `x2` (ค่า `1`), `x1` (ค่า `0`)
- เกต AND 4 ตัวอยู่แถวกลาง
- เกต OR 4 ตัวอยู่แถวขวา
- เอาต์พุตด้านขวา (บนลงล่าง): `y4` (`1`), `y3` (`1`), `y2` (`1`), `y1` (`1`)
- โครงสร้าง: `x4` และ `x3` เป็นอินพุตของ AND ตัวบน (ให้ `y4`); `x3`, `x2` เป็นอินพุตของ AND ถัดไป (ให้ `y3`); `x2`, `x1` ให้ `y2`; และมี AND ที่รับอินพุตต่อเนื่องให้ `y1`; เอาต์พุต AND ป้อนเข้า OR แต่ละตัวตามแนวทแยง

**หัวข้อย่อย:**
- Single error can be masked
- NAND-NAND Logic

---

---

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

**รายละเอียดจากภาพ (vision):**

**หัวข้อ:** Interwoven Redundant Logic

**วงจรตัวอย่างด้านซ้ายบน:**
- `a`, `b` เข้าเกต AND (ไฮไลต์เหลือง) → `e`
- `c`, `d` เข้าเกต AND → `f`
- `e`, `f` เข้าเกต OR → `g`
- `g`, `h` เข้าเกต AND → เอาต์พุต `z`

**ไดอะแกรม Interwoven (ซ้ายล่าง):** เกต AND (ไฮไลต์เหลือง) 4 ตัว:
- ตัวที่ 1: อินพุต `a1`, `a2`, `b1`, `b2` → เอาต์พุต `e1`
- ตัวที่ 2: อินพุต `a1`, `a2`, `b1`, `b2` → เอาต์พุต `e2`
- ตัวที่ 3: อินพุต `a3`, `a4`, `b3`, `b4` → เอาต์พุต `e3`
- ตัวที่ 4: อินพุต `a3`, `a4`, `b3`, `b4` → เอาต์พุต `e4`
- เอาต์พุต `e1`..`e4` ป้อนเข้าเกต OR (แถวกลาง), และมีเกต OR อีกด้านรับ `e1`, `e4`, `f1`, `f4`
- สัญญาณ `f1`, `f2`, `f3`, `f4` ป้อนเข้าเกต OR อีกชุด
- เกต OR แสดงเป็นสัญลักษณ์รูปใบพาย (OR) 3 ตัวเรียงลงมา

**คำอธิบาย (ขวา):**
- Let x1, x2, x3, and x4 be 4 copies of the signal x
- `1 → 0 change is critical for AND, subcritical for OR`
- `0 → 1 change is critical for OR, subcritical for AND`
- Alternating layers of ANDs and ORs can mask each other's critical faults
- To mask `h` critical faults:
  - Number of gates multiplied by `(h + 1)^2`
  - Gate inputs multiplied by `h + 1`
- For `h = 1`, the scheme is known as **Quadded logic**

---

---

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

**รายละเอียดจากภาพ (vision):**

**หัวข้อ:** Interwoven Logic for Half Adder

**ไดอะแกรมใหญ่ด้านซ้าย — Half-adder implemented in quadded logic**

แบ่งเป็น Stages:
- **Stage A**: อินพุต `a1`, `a2`, `a3`, `a4` ป้อนเข้าเกต (NAND, มีบับเบิล) ให้สัญญาณ `A1`, `A2`, `A3`, `A4`
- อินพุต `b1`, `b2`, `b3`, `b4` (Stage B): ป้อนเข้าเกต ให้ `B1`, `B2`, `B3`, `B4`
- **Stage D**: เกตที่ให้สัญญาณ `D1`, `D2`, `D3`, `D4`
- **Stage E**: เกตที่ให้สัญญาณ `E1`, `E2`, `E3`, `E4` และเอาต์พุต `cs1`, `cs2`, `cs3`, `cs4`
- **Stage C**: เกตที่ให้สัญญาณ `C1`, `C2`, `C3`, `C4` และเอาต์พุต `cc1`, `cc2`, `cc3`, `cc4`

**บล็อก Half-adder ปกติ (ขวาบน):**
- อินพุต `a`, `b`
- บน: `a` XOR `b` → เกต AND → เอาต์พุต `S`; และเกต AND อีกตัว → เอาต์พุต `C`
- ล่าง (เวอร์ชัน complemented/NAND): `a`, `b` เข้าเกต NAND → เอาต์พุต `S̄`; และเกตอีกตัว → เอาต์พุต `C̄`

**ข้อความอ้างอิง (ขวาล่าง):**
- *IEEE D&T*
- July-Aug. 2005
- pp. 328-339

**ที่มา:** `From: http://ieeexplore.ieee.org/iel5/54/32070/01492293.pdf`

---

---

## Slide 14: Contents
• Handling Faults
• Interwoven Redundant Logic
• Combinatorial Modeling
• TMR & its application
• Replication & Voting
• Alternating Logic
• Fail-safe Systems

---

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

---

## Slide 16: Reliability of series systems
• Reliability Ri = Prob that component i works
• Reliability Rs = Prob that system s works
Assume that components fail independently
 Component i fails with probability pi
Ri = Prob that comp i works = 1 - pi
Rs = Prob that system works= R1R2R3…Rn = Ri

---

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

**รายละเอียดจากภาพ (vision):**

**หัวข้อ:** Reliability of parallel systems

**ไดอะแกรม (ซ้าย):** บล็อกขนาน 3 บล็อก (แผนภาพบล็อกกำลังสอง):
- บล็อก `1` (บน)
- บล็อก `2` (กลาง)
- บล็อก `N` (ล่าง)
- อินพุตแยกเข้าทุกบล็อก; เอาต์พุตรวมกันทางขวา

**bullet (ขวา):**
- Assume that components fail independently
- Probability that system works =
  - `Rp = 1 − Prob of all components failing`
  - `= 1 − P1P2P3 ... Pn`
  - `= 1 - ∏_0^n (1 − Ri)`

---

---

## Slide 18: Series‐Parallel Effects  *(visual)*
18

**รายละเอียดจากภาพ (vision):**

**หัวข้อ:** Series-Parallel Effects

**คอลัมน์ซ้าย — Series system Reliability**
- กราฟชื่อ **Series System**
- แกน Y: `Reliability` (สเกล 0, 0.2, 0.4, 0.6, 0.8, 1, 1.2)
- แกน X: `Number of components` (1, 2, 3, 4, 5)
- Legend: `Ri = 0.99` (แดง), `Ri = 0.98` (เขียว), `Ri = 0.97` (ม่วง), `Ri = 0.96` (ฟ้า), `Ri = 0.95` (ส้ม)
- เส้นทุกเส้นลาดลงเล็กน้อยจากค่า ~1.0 เมื่อ N เพิ่มขึ้น
- คำอธิบาย: Reliability decreases with N steadily

**คอลัมน์ขวา — Parallel system Reliability**
- กราฟชื่อ **Parallel system**
- แกน Y: `Reliability R` (สเกล 0.996 ถึง 1.0005)
- แกน X: `Number of components (n)` (2, 3, 4, 5)
- Legend: `Ri = 0.99` (เขียว), `Ri = 0.98` (ม่วง), `Ri = 0.97` (ฟ้า), `Ri = 0.96` (น้ำเงิน), `Ri = 0.95` (ส้ม)
- เส้นส่วนใหญ่ลู่เข้าหา 1 อย่างรวดเร็ว; เส้น `Ri = 0.95` เริ่มต่ำ (~0.9975) แล้วเพิ่มขึ้นชัน
- คำอธิบาย: Reliability increases sharply with N

---

---

## Slide 19: ex. Calculate the reliability of  *(visual)*
the following system

**รายละเอียดจากภาพ (vision):**

**หัวข้อ:** ex. Calculate the reliability of the following system

**Reliability block diagram (ระบบผสม non-series-parallel):**
- อินพุตซ้าย → บล็อก `R1` (series) → บล็อก `R2` (series)
- หลัง `R2` แยกเป็น 3 สาขา (parallel):
  - สาขาบน: บล็อก `R3`
  - สาขากลาง: บล็อก `R3`
  - สาขาล่าง: บล็อก `R3`
- จากกลุ่ม `R3` (3 ตัว) รวมกันแล้วแยกเป็น 2 สาขา (parallel):
  - สาขาบน: บล็อก `R4`
  - สาขาล่าง: บล็อก `R4`
- จากกลุ่มนี้ไปยังบล็อก `R5` (series) → เอาต์พุต

(แผนภาพเป็นสะพาน/โครงข่าย: R1-R2 อนุกรม, กลุ่ม R3 ขนานสามทาง, กลุ่ม R4 ขนานสองทาง, R5 อนุกรม)

---

---

## Slide 20: Non-Series Parallel System  *(visual)*
• Neither a series nor parallel system
• How to evaluate the Reliability?

 E

 A B C D

 F

**รายละเอียดจากภาพ (vision):**

**หัวข้อ:** Non-Series Parallel System

- Neither a series nor parallel system
- How to evaluate the **Reliability**? (คำว่า Reliability เป็นสีแดง)

**Reliability block diagram:**
- อินพุต → บล็อก `A` (มีกรอบไฮไลต์สีฟ้า) → แยกเป็น 3 ทาง:
  - ทางบน: บล็อก `E` → รวมเข้าโหนดก่อน `D`
  - ทางกลาง: บล็อก `B` → บล็อก `C` → รวมเข้าโหนดก่อน `D`
  - ทางล่าง (จากก่อน `A`): บล็อก `F` → เข้ารวมที่โหนดระหว่าง `B` กับ `C` (ก่อน `C`)
- หลังรวม → บล็อก `D` → เอาต์พุต

โครงสร้าง: อินพุตผ่าน `A`; หลัง `A` แยกไป `E` และ `B`; `F` ขนานกับ `A`+`B` (ป้อนเข้าก่อน `C`); `E` ขนานกับ `B`+`C` (ป้อนเข้าก่อน `D`); สุดท้าย `D` อนุกรม

---

---

## Slide 21: Non-Series Parallel System - 1  *(visual)*
• Pick a module 'm' in the system

 P(sys works) = P(sys works | m works) P(m works)
 + P(sys works | m fails) P(m fails)
 Rsys = P(sys works | m)Rm + P(sys works | m')(1 - Rm)

 E

 A B C D

 F

**รายละเอียดจากภาพ (vision):**

**หัวข้อ:** Non-Series Parallel System - 1

- Pick a module 'm' in the system

**สูตร:**
- `P(sys works) = P(sys works | m works) P(m works) + P(sys works | m fails) P(m fails)`
- `Rsys = P(sys works | m)Rm + P(sys works | m')(1 − Rm)`

**Reliability block diagram** (เหมือน Slide 20):
- อินพุต → `A` (ไฮไลต์) → แยกเป็น `E` (บน) และ `B` (กลาง); `F` (ล่าง) รับจากก่อน `A` แล้วรวมก่อน `C`; `B` → `C` → รวมกับ `E` ก่อน `D` → `D` → เอาต์พุต

---

---

## Slide 22: Non-Series Parallel System - 2  *(visual)*
• Pick 'm' to be module E. Consider 'E fails';
 P(sys works | E') = [1 - (1 - RARB)(1 - RF)]RCRD
 'module E fails' = 'path E opened'

 A B C D

 F

**รายละเอียดจากภาพ (vision):**

**หัวข้อ:** Non-Series Parallel System - 2

- Pick 'm' to be module E. Consider 'E fails';
- `P(sys works | E') = [1 − (1 − R_A R_B)(1 − R_F)]R_C R_D`

**ข้อความสีแดง:** 'module E fails' = 'path E opened' พร้อมลูกศรสีแดงชี้ลง

**Reliability block diagram:** แสดง `E` ถูกเปิดออก (เส้นทางบนขาด) เหลือ `A` → `B` → `C` → `D` และ `F` ชนาน `B`; โหนดรวมก่อน `D` จาก `C` และจาก (ไม่มี E)

---

---

## Slide 23: Non-Series Parallel System - 3  *(visual)*
• Next, consider 'E works' = 'path E shorted'
• Still unsolved, do again wt a different module

 A B C D

 F

**รายละเอียดจากภาพ (vision):**

**หัวข้อ:** Non-Series Parallel System - 3

- Next, consider 'E works' = 'path E shorted' (สีแดง)
- Still unsolved, do again wt a different module

**Reliability block diagram:** แสดง `E` ถูก short (เส้นทางบนเชื่อมตรง) โดยที่ `E` ไม่ปรากฏเป็นบล็อกแล้ว (มีลูกศรสีแดงชี้ลงตรงกลางบน); โครงสร้าง `A` (ไฮไลต์ฟ้า), `B`, `C`, `D`, `F` ยังคงอยู่ โดยทางบนลัดจาก `B` ไปยังโหนดก่อน `D`

---

---

## Slide 24: Non-Series Parallel System - 4  *(visual)*
• Next, consider 'B fails' = 'path B opened'
 P(sys works|E and B') = [1-(1-RA)(1-RFRC)]RD

 A C D

 F

**รายละเอียดจากภาพ (vision):**

**หัวข้อ:** Non-Series Parallel System - 4

- Next, consider 'B fails' = 'path B opened' (สีแดง)
- `P(sys works | E and B') = [1−(1−R_A)(1−R_F R_C)]R_D`

**Reliability block diagram:** บล็อก `B` ถูกเปิดออก (มีลูกศรสีแดงชี้ลงตรงตำแหน่ง B); โครงสร้าง: `A` (ไฮไลต์) → และ `F`; ทางบนลัดไปโหนดก่อน `D`; `C` → รวมก่อน `D`; `D` → เอาต์พุต

---

---

## Slide 25: Non-Series Parallel System - 5  *(visual)*
• Next, when B works, still the same as before
 P(sys works|E and B) = [1-(1-RA)(1-RFRC)]RD

 'module B works' = 'path B shorted'

 A C D

 F

**รายละเอียดจากภาพ (vision):**

**หัวข้อ:** Non-Series Parallel System - 5

- Next, when **B works** (สีแดง), still the same as before
- `P(sys works | E and B) = [1−(1−R_A)(1−R_F R_C)]R_D`

**ข้อความสีแดง:** 'module B works' = 'path B shorted'

**Reliability block diagram:** แสดง `B` ถูก short (ลูกศรแดงชี้ลงตรงกลางบน); โครงสร้าง `A` (ไฮไลต์) → ทางบนลัดไปโหนดก่อน `D`; `F` → รวมก่อน `C`; `C` → รวมก่อน `D`; `D` → เอาต์พุต

---

---

## Slide 26: Putting it all together ‐ 1
P(sys works|E') = [1 - (1 - RARB)(1 - RF)]RCRD

P(sys works|E and B') = [1-(1-RA)(1-RFRC)]RD
P(sys works|E and B) = [1-(1-RA)(1-RFRC)]RD

P(sys works|E) = [1 - (1 - RA)(1 - RFRC)]RD[RB + RB']
 = [1 - (1 - RA)(1 - RFRC)]RD
P(sys works) =
 P(sys works|E)RE + P(sys works|E')(1- RE)

---

## Slide 27: Putting it all together ‐ 2
Rsys = P(sys works) =
 [1 - (1 - RARB)(1 - RF)]RCRD(1 - RE)
 + [1 - (1 - RA)(1 - RFRC)]RD RE
 = [RERD+RCRD-RERCRD][RA+RFRC-RARFRC]
Let RA = RB = RC = RD = RE = RF = R;
Then,
 Rsys = R6 - 3R5 + R4 +2R3

---

## Slide 28: Some tips for non-series‐parallel
• Simpler if picked module A

• Choosing the initial module is crucial
• Heuristics:
 - Pick modules that are on as many paths as
 possible
 - Think about whether a single module prevents the
 system from becoming a serial/parallel system

---

## Slide 29: Non-Series Parallel System (again)  *(visual)*
E

 A B C D

 F

 Choose A as the keystone component

 Rsys = P(sys works|A)RA + P(sys works|A')(1-RA)

 R:Reliabilty; P:Possibility

**รายละเอียดจากภาพ (vision):**

**หัวข้อ:** Non-Series Parallel System (again)

**Reliability block diagram** (เหมือน Slide 20 แต่ `A` มีกรอบสีแดง):
- อินพุต → `A` (กรอบแดง) → แยกเป็น `E` (บน) และ `B` (กลาง); `F` (ล่าง) รับจากก่อน `A` รวมก่อน `C`; `B` → `C` → รวมกับ `E` ก่อน `D` → `D` → เอาต์พุต

**ข้อความ:**
- Choose **A** as the keystone component

**สูตร (สีแดง):**
- `Rsys = P(sys works|A)R_A + P(sys works|A')(1-R_A)`

**หมายเหตุ (ขวาล่าง):** `R:Reliabilty; P:Possibility`

---

---

## Slide 30: Non-Series Parallel System (again-1)  *(visual)*
E

 B C D

 F

 If A works: →serial/parallel system

 P(sys works|A) = (1 - (1 - RE)(1 - (1 - (1 - RB)(1 - RF)) RC)) RD

**รายละเอียดจากภาพ (vision):**

**หัวข้อ:** Non-Series Parallel System (again-1)

**Reliability block diagram:** `A` ถูกนำออก (short) เนื่องจากพิจารณากรณี A works; อินพุตตรงเข้าสู่ `B` (กลาง) และ `F` (ล่าง); `B` → `C`; `F` รวมก่อน `C`; ทางบน `E` รับจากก่อน `B` และรวมก่อน `D`; `C` → รวมก่อน `D`; `D` → เอาต์พุต

**ข้อความหัวข้อย่อย:**
- If A works: → *serial/parallel system*

**สูตร (สีแดง):**
- `P(sys works|A) = (1 − (1 − R_E)(1 − (1 − (1 − R_B)(1 − R_F)) R_C)) R_D`

---

---

## Slide 31: Non-Series Parallel System (again-2)  *(visual)*
E

 B C D

 F

 If A fails: →serial/parallel system

 P(sys works|A') = RF RC RD

**รายละเอียดจากภาพ (vision):**

**หัวข้อ:** Non-Series Parallel System (again-2)

**Reliability block diagram:** แสดงกรณี A ถูก short; บล็อก `E` และ `B` ถูกตัดออก (มีเส้นทแยงสีแดงพาดผ่านทั้ง `E` และ `B`):
- อินพุตตรงเข้าสู่ `F` (ล่าง) และมีเส้นไปถึงโหนดก่อน `C`
- `F` → รวมก่อน `C`; `C` → `D` → เอาต์พุต
- `E` และ `B` ถูกขีดฆ่า (fail)

**ข้อความหัวข้อย่อย:**
- If A fails: → *serial/parallel system*

**สูตร (สีแดง):**
- `P(sys works|A') = R_F R_C R_D`

---

---

## Slide 32: Put it all again
Rsys = P(sys works| A) RA + P(sys works | A') (1-RA)
 = (1 - (1 - RE)(1 - (1 - (1 - RB)(1 - RF)) RC)) RD RA
 + RC RD RF (1 - RA)
 = RA RB RC RD + RA RB RC RF - RA RB RC RD RF + RA RD RE
 - RA RB RC RD RE - RA RC RD RE RF + RA RB RC RD RE RF
 + RC RD RF - RA RC RD RF

 Let RA = RB = RC = RD = RE = RF = R, then
Rsys = R6 - 3R5 + R4 +2R3

---

## Slide 33: In-class Exercise: Non SP system  *(visual)*
33

**รายละเอียดจากภาพ (vision):**

**หัวข้อ:** In-class Exercise: Non SP system

**สองไดอะแกรม (bridging / diamond network):**

**System P (ซ้าย):** อินพุต `X` แยกเป็น 2 สาขา:
- สาขาบน: บล็อก `A` → บล็อก `C`
- สาขาล่าง: บล็อก `B` → บล็อก `D`
- สองสาขารวมกันที่เอาต์พุต `Y`
- เส้นทาง: X→A→C→Y (บน) และ X→B→D→Y (ล่าง) — รูปสี่เหลี่ยมขนมเปียกปูน

**System Q (ขวา):** อินพุต `X` แยกเป็น 2 สาขา:
- สาขาบน: บล็อก `A` → บล็อก `C`
- สาขาล่าง: บล็อก `B` → บล็อก `D`
- ตรงกลางมีบล็อก `K` เชื่อมข้ามจากโหนดบน (ระหว่าง A-C กับ... จุดเชื่อมบน) มาที่โหนดล่าง/กลาง (bridge)
- เอาต์พุต `Y` รวมจาก 2 สาขา
- โครงสร้าง: A, C สาขาบน; B, D สาขาล่าง; `K` เป็นสะพานเชื่อมกลาง

---

---

## Slide 34: Inclass Exercise: Non SP system  *(visual)*
34

**รายละเอียดจากภาพ (vision):**

**หัวข้อ:** Inclass Exercise: Non SP system

**ไดอะแกรมย่อ (บน):** System P และ System Q (แบบเดียวกัน Slide 33)

**Ans**

**System P:**
- `Rp = 1-(1-RaRc)(1-RbRd) = 1-(1-R²)² = 2R²-R⁴` (ผลลัพธ์ `2R²-R⁴` สีแดง)

**System Q:**
- `Rp = P(Sys works|K)Rk + P(Sys works|K')(1-Rk)`
- `P(Sys works|K) = [1-(1-Ra)(1-Rb)][1-(1-Rc)(1-Rd)]`
- `= R⁴-4R³+4R²`
- `P(Sys works|K') = 1-(1-RaRc)(1-RbRd) = Rp` (ตัว Rp สีน้ำเงิน)
- `Then, Rq = (R⁴-4R³+4R²)Rk + Rp(1-Rk)`
- `= 2R⁵-5R⁴+2R³+2R²` (ผลลัพธ์สีแดง)

**เปรียบเทียบ:**
- `If Rk is perfect (Rk=1): Rq = [(R⁴-4R³+4R²)Rk + Rp(1-Rk)]|Rk=1] = R⁴-4R³+4R²`
- `Hence: Rq − Rp = (R⁴-4R³+4R²) − (2R²-R⁴) = 2R²(R-1)² >= 0`

**ข้อความสรุปสีแดง:** System Q is better reliable than System P

**ไดอะแกรมย่อย (ขวา):**
- **System Q | K works** — แสดง A, B, C, D เชื่อมกัน (โครงข่ายไม่มี K / K short)
- **System Q | K fails** — แสดง A, B, C, D พร้อมบล็อก `K` ตรงกลาง (bridged)

---

---

## Slide 35: Contents
• Handling Faults
• Interwoven Redundant Logic
• Combinatorial Modeling
• TMR & its application
• Replication & Voting
• Alternating Logic
• Fail-safe Systems

---

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

**รายละเอียดจากภาพ (vision):**

**หัวข้อ:** TMR with Perfect Voter

**สูตร (บนซ้าย):**
- `R = 3R_m² − 2R_m³ ≥ R_m` (มีเครื่องหมาย "≥?" กำกับด้านบน)

**ข้อความ:**
- Condition on the module reliability:
- `R = R_m [1 + (1 − R_m)(2R_m − 1)]`
- `(1 − R_m)(2R_m − 1) > 0 ⟹ R_m > 1/2`

**ไดอะแกรม (ขวาบน):** บล็อก `1`, `2`, `3` ป้อนเข้าวงกลม `V` ป้าย **Voter** → เอาต์พุต

**กราฟซ้าย (R เทียบ R_m):**
- แกน Y: `R` (0.0, 0.5, 1.0)
- แกน X: `R_m` (0.0, 0.5, 1.0)
- เส้นโค้งหนา + เส้นทแยงประ `R = R_m`
- ป้าย **TMR better** (แดง) เหนือเส้นทแยง; ป้าย **Simplex better** (น้ำเงิน) ใต้เส้นทแยง
- จุดตัดที่ `R_m = 0.5`

**กราฟขวา (R เทียบ λt):**
- แกน Y: `R` (0.0, 0.5, 1.0)
- แกน X: `λt` (0, ln 2, ...)
- เส้นทึบสีแดง = `TMR`; เส้นประสีน้ำเงิน = `Simplex`
- เส้น `TMR` อยู่เหนือ `Simplex` เมื่อ λt น้อย และตกต่ำกว่าเมื่อ λt มาก (ตัดกันที่เครื่องหมาย `ln 2`)

**สูตรล่างซ้าย:**
- `RIF_TMR/Simplex = (1 − R_m)/(1 − R)`
- `= 1/[1 − R_m(2R_m − 1)]`

**สูตรล่างขวา:**
- `MTTF: TMR 5/(6λ)`
- `Simplex 1/λ`

---

---

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

**รายละเอียดจากภาพ (vision):**

**หัวข้อ:** TMR with Imperfect Voter

**สูตร:**
- `R = R_v(3R_m² − 2R_m³) ≥? R_m`

**Condition on the voter reliability:**
- `R_v > 1 / [3R_m − 2R_m²]`

**อนุพันธ์:**
- `dR_v^min/ dR_m = (−3 + 4R_m)/(3R_m − 2R_m²)²`

**Condition on the module reliability:**
- `(3 − √(9 − 8/R_v))/4 < R_m < (3 + √(9 − 8/R_v))/4`

**Example:**
- `R_v = 0.95` requires that
- `0.56 < R_m < 0.94`

**ไดอะแกรม (ขวาบน):** บล็อก `1`, `2`, `3` ป้อนเข้าวงกลม `V` ป้าย **Voter** → เอาต์พุต

**กราฟ (ขวาล่าง): R_v เทียบ R_m:**
- แกน Y: `R_v` (มีค่ากำกับ 0.95, 0.885, 0.5)
- แกน X: `R_m` (ค่ากำกับ 0.5, 0.56, 0.75, 0.94, 1.0)
- เส้นโค้งเป็นรูปตัว U (พาราโบลาเปิดขึ้น)
- ป้าย **TMR better** (แดง) อยู่ด้านในโค้ง; ป้าย **Simplex better** (น้ำเงิน) อยู่ด้านล่าง
- เส้นประแนวนอนที่ `R_v = 0.95` และ `R_v = 0.885` (ค่าต่ำสุด); เส้นประแนวตั้งที่ `R_m = 0.56` และ `R_m = 0.94`
- เลขหน้า: `Slide 37`

---

---

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

**รายละเอียดจากภาพ (vision):**

**หัวข้อ:** TMR with Compensating Faults

**สูตร:**
- `R_m = 1 − p_0 − p_1  (0- and 1-fault probabilities)`
- `R = (3R_m² − 2R_m³) + 6p_0p_1R_m`

**Example:**
- `R_m = 0.998, p_0 = p_1 = 0.001`
- `R = 0.999,984 + 0.000,006 = 0.999,990`
  - ใต้พจน์ `0.999,984` มีป้าย **Basic TMR**
  - ใต้พจน์ `0.000,006` มีป้าย **Compensation**

**RIF:**
- `RIF_TMR/Simplex = 0.002 / 0.000,016 = 125`
- `RIF_Compen/TMR = 0.000,016 / 0.000,010 = 1.6`

**ไดอะแกรม (ขวาบน):** บล็อก `1`, `2`, `3` ป้อนเข้าวงกลม `V` ป้าย **Voter** → เอาต์พุต

---

## Slide 39: Contents
• Handling Faults
• Interwoven Redundant Logic
• Combinatorial Modeling
• TMR & its application
• Replication & Voting
• Alternating Logic
• Fail-safe Systems

---

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

**รายละเอียดจากภาพ (vision):**

**หัวข้อ:** Implementing a Bit-Voter

ข้อความบนสไลด์ (verbatim):
- TMR bit-voting: `y = x₁x₂ ∨ x₂x₃ ∨ x₃x₁`
  - `(carry output of a single-bit full-adder)`
- What about 5MR, 7MR?
- Gate-level design quickly explodes in size
- Other designs are also possible
  - Arithmetic: add the bits, compare to threshold
  - Mux-based
  - Selection-based (majority of bit values is their median)

**แผนภาพ Bit-voter (มุมขวาบน):** มีโมดูล 3 กล่องเรียงกันหมายเลข `1`, `2`, `3`
อินพุตเดียวกันป้อนเข้าทั้งสามกล่อง (เส้นจากด้านซ้ายแยกไปเข้าแต่ละกล่อง)
เอาต์พุตของกล่องตามลำดับคือ `x₁`, `x₂`, `x₃` ป้อนเข้าสู่วงกลมสีเหลืองมีตัวอักษร `V`
(ป้ายกำกับ `Bit-voter`) เอาต์พุตออกทางขวาเป็น `y`

**แผนภาพวงจร (แถวล่าง) 3 รูป:**

1. `3-out-of-5 voter built of 2-input gates` — วงจรเกตเลเวล ใช้ AND/OR แบบ 2-input จำนวนมาก
   เชื่อมกันเป็นโครงข่ายซับซ้อน มีอินพุตกำกับเลข `1`–`5` และเอาต์พุต `y` ทางขวา (รายละเอียดเกตยิบย่อย [illegible] แต่โครงสร้างเป็น 2-input gates เรียงต่อกัน)
2. `Two mux-based designs for a 3-out-of-5 bit-voter` (ภาพซ้าย) — อินพุต `x₁ x₂ x₃ x₄ x₅`
   ป้อนเข้าอินพุต AND และ OR, มีสัญญาณกลาง `h`, มี MUX (สามเหลี่ยมมี `0`,`1`,`:` ข้างใน) และมี `0`,`1` กำกับ selector, เอาต์พุต `y`
   (ป้าย `0`,`1`/`:` ปรากฏที่มัลติเพล็กเซอร์)
3. (ภาพขวา) อินพุต `x₁ x₂ x₃ x₄ x₅` ป้อนเข้า AND และมีสัญญาณกลาง `h₁`, `h₂`
   แล้วเข้า `Mux` ขนาดใหญ่ที่ระบุเลข selector `0`,`1`,`2`,`3`,`4`,`5`,`6`,`7`
   โดยมีค่าคงที่ `0` และ `1` ป้อนเข้าด้วย เอาต์พุต `y`

มุมขวาล่าง: `Slide 40`

---

---

## Slide 41: Complexity of Different Bit-Voter Designs  *(visual)*
Cost of majority bit-voters as a function of the number n of inputs

**รายละเอียดจากภาพ (vision):**

**หัวข้อ:** Complexity of Different Bit-Voter Designs

**กราฟเส้น (Line graph):**
- แกน Y: `Number of Gates` (สเกล 0, 40, 80, 120; มีเส้นกริดที่ 40 และ 80)
- แกน X: `n` (สเกล 0, 4, 8, 12, 16; มีเส้นกริดแนวตั้งที่ 4, 8, 12)
- เส้นโค้ง 4 เส้น มีป้ายกำกับ: `Gate-Level`, `Multiplexer`, `Selection`, `Arithmetic`
  - `Gate-Level` เพิ่มขึ้นชันมาก และตัดเพดาน 120 ราว n≈6
  - `Arithmetic` เตี้ยที่สุด เพิ่มขึ้นช้า ๆ
  - `Multiplexer` เพิ่มชันช่วงท้าย
  - `Selection` เพิ่มแบบค่อนข้างเป็นเส้นตรง

คำบรรยายใต้กราฟ: `Cost of majority bit-voters as a function of the number n of inputs`

มุมขวาล่าง: `41`

---

---

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

---

## Slide 43: Bit-Voting and Word-Voting (1)  *(visual)*
Scenario1: every module has an error bit at the output
 Expected output is (00000)

 maintaining data integrity 43

**รายละเอียดจากภาพ (vision):**

**หัวข้อ:** Bit-Voting and Word-Voting (1)

ข้อความ:
- Scenario1: every module has an error bit at the output
- Expected output is *(00000)* (ตัวเอียง สีแดง)

**ตาราง:**

| Module Number | Bit 4 | Bit 3 | Bit 2 | Bit 1 | Bit 0 | Value (decimal) |
|---|---|---|---|---|---|---|
| #1 | 0 | 1 | 0 | 0 | 0 | 8 |
| #2 | 0 | 1 | 0 | 0 | 0 | 8 |
| #3 | 0 | 0 | 1 | 0 | 0 | 4 |
| #4 | 0 | 0 | 0 | 1 | 0 | 2 |
| #5 | 0 | 0 | 0 | 0 | 1 | 1 |
| **Bit-Voter Result** | 0 | 0 | 0 | 0 | 0 | 0 |
| **Word-Voter Result** | 0 | 1 | 0 | 0 | 0 | 8 |

(หัวตารางมี `Module Number`, `Word (5 bits)` ครอบ `Bit 4`…`Bit 0`, และ `Value (decimal)`)

**การเน้นในภาพ:** กลุ่มโมดูล #1–#5 อยู่ในกรอบสี่เหลี่ยมดำ (ล้อมรอบแถวข้อมูล 5 แถว)
แถว `Bit-Voter Result` วงด้วยวงรีสีแดง และมีลูกศรสีแดงชี้ขึ้นไปที่แถว `Word-Voter Result` พร้อมข้อความ `maintaining data integrity`

มุมขวาล่าง: `43`

---

---

## Slide 44: Bit-Voting and Word-Voting (2)  *(visual)*
Scenario2: some modules have multiple errors
 Expected output is (00000)

 maintaining data integrity 44

**รายละเอียดจากภาพ (vision):**

**หัวข้อ:** Bit-Voting and Word-Voting (2)

ข้อความ:
- Scenario2: some modules have multiple errors
- Expected output is *(00000)* (ตัวเอียง สีแดง)

**ตาราง:**

| Module Number | Bit 4 | Bit 3 | Bit 2 | Bit 1 | Bit 0 | Value (decimal) |
|---|---|---|---|---|---|---|
| #1 | 0 | 0 | 0 | 0 | 0 | 0 |
| #2 | 1 | 0 | 1 | 1 | 1 | 23 |
| #3 | 0 | 0 | 0 | 0 | 0 | 0 |
| #4 | 1 | 1 | 0 | 0 | 1 | 25 |
| #5 | 1 | 1 | 1 | 0 | 1 | 27 |
| **Bit-Voter Result** | 1 | 0 | 0 | 0 | 1 | 17 |
| **Word-Voter Result** | 0 | 0 | 0 | 0 | 0 | 0 |

(หัวตาราง: `Module Number`, `Word (5 bits)` ครอบ `Bit 4`…`Bit 0`, `Value (decimal)`)

**การเน้นในภาพ:** โมดูล #1–#5 อยู่ในกรอบดำ แถว `Word-Voter Result` วงด้วยวงรีสีแดง
มีลูกศรสีแดงชี้ขึ้นที่แถว `Word-Voter Result` พร้อมข้อความ `maintaining data integrity`

มุมขวาล่าง: `44`

---

---

## Slide 45: Some Simple Voter Designs  *(visual)*
DisagreeIf in the case of 3-way disagreement x1 Compare 1
any of the inputs can be chosen, x2 2 0then a simple design is possible y
 x3 3 1This design can be readily generalized
to a larger number of inputs

One can perform pseudo voting that yields the median of 3 analog
signals (Dennis, N.G., Microelectronics and Reliability, Aug. 1974)

Median and mean voting are also possible with digital signals

 Slide 45

**รายละเอียดจากภาพ (vision):**

**หัวข้อ:** Some Simple Voter Designs

ข้อความ:
- If in the case of 3-way disagreement any of the inputs can be chosen, then a simple design is possible
- This design can be readily generalized to a larger number of inputs
- One can perform pseudo voting that yields the median of 3 analog signals (Dennis, N.G., *Microelectronics and Reliability*, Aug. 1974)
- Median and mean voting are also possible with digital signals

**แผนภาพวงจร (ขวาบน):** โมดูล 3 กล่องหมายเลข `1`, `2`, `3`
เอาต์พุตเป็น `x₁`, `x₂`, `x₃` โดย `x₁` และ `x₂` ป้อนเข้าสู่วงรีสีเหลือง `Compare`
(มีลูกศรจาก Compare ขึ้น/ลงสร้างสัญญาณ `Disagree` ซึ่งเป็นเส้นประ) สัญญาณ `Disagree` และ `x₃`
ป้อนเข้าสู่วงกลม/MUX (สามเหลี่ยมมี `0` ด้านบน, `1` ด้านล่าง) เอาต์พุตออกทางขวา `y`
(input ที่ 3 คือ x₃ เข้า selector — มีเส้นประจาก Disagree ลงมาที่ selector)

มุมขวาล่าง: `Slide 45`

---

---

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

**รายละเอียดจากภาพ (vision):**

**หัวข้อ:** *N*-Modular Redundancy (NMR)

ข้อความ:
- Triple-modular redundancy (TMR) can be generalized to *N* units
- *N*-modular redundancy (NMR) uses *N* modules along with a voter, with *N* usually being odd
- Example: 5MR
  - Operates correctly as long as 3 of the 5 modules are healthy
- Voter complexity rises rapidly with increasing *N*
- Even values of *N* are also feasible
- Example: 4MR, with 3-out-of-4 voting
  - Voter masks single faults; can be designed to detect double faults

**แผนภาพ (ขวา):** โมดูล 5 กล่องหมายเลข `1`,`2`,`3`,`4`,`5` อินพุตเดียวกันแยกเข้าแต่ละกล่อง
เอาต์พุตทั้ง 5 รวมเข้าสู่วงกลมสีเหลือง `V` (ป้าย `Voting unit`) เอาต์พุตออกทางขวาเป็นลูกศร

มุมขวาล่าง: `46`

---

---

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

**รายละเอียดจากภาพ (vision):**

**หัวข้อ:** Switch for Standby Redundancy

ข้อความ:
- Standby redundancy requires an *n*-to-1 switch to select the output of the currently active module
- The detectors use various info to deduce fault conditions
  - `--` Error coding
  - `--` Reasonableness checks
  - `--` Watchdog timer
- Once a fault has been detected, the switch reconfigures the system by flagging the faulty unit and activating next spare in sequence
- If we use an *n*-to-2 switch and compare the two selected outputs, the configuration is known as "pair-and-spares"

**แผนภาพบน (ขวาบน):** สวิตช์สองทาง (double-pole) ด้านซ้ายและขวา
โมดูล 1 (กล่องสีส้ม) ต่อผ่านวงกลม `D` (ป้าย `Detector`) ไปยังสวิตช์ขวา
ด้านล่างมีกล่อง `2` (ป้าย `Spare`) ซึ่งเป็นเส้นทางสำรอง (เส้นทึบต่อจากสวิตช์ซ้ายมาที่กล่อง 2 แล้วไปยังสวิตช์ขวา)
เส้นประแสดงเส้นทางสำรอง/การตรวจจับ

**แผนภาพล่าง (ขวาล่าง):** โมดูล `1`,`2`,`3` แต่ละตัวมีวงกลม `D` ต่อท้าย
ด้านซ้ายเขียน `Spares` กำกับกลุ่มโมดูล 2 และ 3
เอาต์พุตของทุกโมดูลเข้าสู่บล็อกสีเขียว `n-to-1 switch` แล้วออกทางขวาเป็นลูกศร
(เส้นประจาก D ต่าง ๆ เข้าสู่ switch)

มุมขวาล่าง: `47`

---

---

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

**รายละเอียดจากภาพ (vision):**

**หัวข้อ:** Switch for Hybrid Redundancy

ข้อความ:
- Hybrid redundancy with *n* active and *s* spare modules requires an (*n* + *s*)-to-*n* switch to select the outputs of the active modules
- Self-purging redundancy is a variant of hybrid redundancy in which all modules are active at the outset, but they are purged as they disagree with the majority output
- Voter in self-purging redundancy is a threshold voter that considers the inputs with weights of 1 (active) or 0 (purged)

**แผนภาพบน (ขวาบน):** โมดูล `1`,`2`,`3` (กล่องส้ม) และกล่อง `4` (ป้าย `Spare` ด้านล่าง)
เอาต์พุตเข้าแถบสีเหลืองแนวตั้งมีตัวอักษร `S` (switch) แล้วเข้าสู่วงกลมสีเหลือง `V`
เอาต์พุตออกทางขวา ป้าย `Switch-voter` อยู่ด้านล่าง มีเส้นประแสดง feedback จากเอาต์พุตกลับไปที่ switch (ด้านบนขวา)

**แผนภาพล่าง (ขวาล่าง):** แผนภาพบล็อกทั่วไป มีกล่องอินพุตหลายกล่อง (ด้านซ้าย) ต่อเข้าบล็อกใหญ่ตรงกลาง
บล็อกบนด้านบนเชื่อมกับบล็อกกลาง (มี `...` กำกับ) และมีลูกศรป้อนกลับ (feedback) จากเอาต์พุตกลับเข้าบล็อกบน
เอาต์พุตของบล็อกกลางเข้าสู่วงกลม (voter) ทางขวาแล้วออกเป็นลูกศร (มีจุดไข่ปลา `...` กำกับที่เส้นเชื่อมสายโหวต)

มุมขวาล่าง: `48`

---

---

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

**รายละเอียดจากภาพ (vision):**

**หัวข้อ:** Variations and Design Issues

ข้อความ:
- **NMR/simplex:** Voting unit is replaced with a unit that can also detects disagreements
- When a faulty unit is detected, that unit and one other unit are removed from service
- This makes all votes unambiguous and also improves systems lifetime
- **Self-purging redundancy:** Modules purged when they disagree with the output and the threshold of the voting unit is adjusted accordingly (purged modules produce 0 outputs)

**แผนภาพบน (ขวาบน):** โมดูล `1`,`2`,`3` อินพุตเดียวกัน เอาต์พุตรวมที่วงกลมสีเหลือง `V`
(ป้าย `Voting unit`) เอาต์พุตออกทางขวา

**แผนภาพล่าง (ขวาล่าง):** วงจรลอจิก มีเกต XNOR/XOR (เกตโค้ง), บล็อก `S R / Q` (latch/flip-flop: มี `S` บน, `R`, และ `Q` พร้อม `Q` กลับด้าน)
มีเกต AND (ป้อน `Module output` และสัญญาณจาก Q) และวงกลมสีเหลือง `T` (threshold voter)
มีเส้นหลายเส้นรวมเข้า `T` จากด้านซ้ายล่าง/ล่าง และมี feedback จากเอาต์พุตหลัง `T`

มุมขวาล่าง: `49`

---

---

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

**รายละเอียดจากภาพ (vision):**

**หัวข้อ:** Variations and Complications

ข้อความ:
- Static redundancy makes fault testing more challenging
- For static redundancy to be effective, we must ensure that initially all redundant components are fault-free

**แผนภาพ (กลาง/ขวา):** โมดูล `1`,`2`,`3` อินพุตเดียวกัน
- เอาต์พุตโมดูล 1 → เข้า selector ด้านบน (เลข `0`)
- เอาต์พุตทั้งหมดป้อนเข้าวงกลมสีเหลือง `V` (ป้าย `Voting unit`)
- เอาต์พุตโมดูล 2, 3 และเอาต์พุต V เข้าสู่ MUX (สี่เหลี่ยมคางหมูด้านขวา) ที่มีอินพุตหมายเลข `0`,`1`,`2`,`3` และมี `Mode` (เส้นประ) กำกับที่ด้านล่าง selector
- เอาต์พุต MUX ออกทางขวา
- มีลูกศรสีน้ำเงิน (ลูกศรหนา) ชี้ขึ้นที่ขอบ select line ระหว่างโมดูลกับ MUX พร้อมข้อความ:
  - `Controllable, but not observable`

แถบล่าง: `Oct. 2015` | `Part III – Faults: Logical Deviations` | `Slide 50`

---

---

## Slide 51: Time Redundancy
Retry upon a detected fault: particularly useful for transient faults

 Recomputation not useful with permanent faults

 Can make recomputation work by slightly changing the operands,
 but this is not always applicable

 Compute a (2b) instead of (2a) b

 Compute b + a or -(-a - b) instead of a + b

Oct. 2015 Part III - Faults: Logical Deviations Slide 51

---

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

**รายละเอียดจากภาพ (vision):**

**หัวข้อ:** Applications of *n*MR and Hybrid Redundancy

ข้อความ:
- The Space Shuttle:
  - Uses 5-way redundancy in hardware
    - Originally, 3 operational units + 2 spares (one warm, one cold)
    - More recently, 4 operational + 1 spare
  - Also, uses 2 independently developed software systems (Design diversity)
- Japanese Shinkansen "Bullet" Train
  - Triple-duplex system (6-fold redundancy)

**รูปภาพ:** ภาพ Space Shuttle กำลังปล่อยตัว (จรวด/กระสวยอวกาศ) มุมขวาบน
ภาพรถไฟ Shinkansen (Bullet Train) มุมซ้ายล่าง (มีข้อความบนตัวรถ `JR 500`)

มุมขวาล่าง: `52`

---

---

## Slide 53: Check yourself  *(visual)*
Q. List the conditions under which it will fail?

**รายละเอียดจากภาพ (vision):**

**หัวข้อ:** Check yourself

ข้อความ: `Q. List the conditions under which it will fail?` (ตัวเอียง)

**แผนภาพ:** โมดูลเรียงเป็น 3 แถว แต่ละแถวมี:
- กล่อง `Processor` (ด้านซ้าย, มีเส้นคู่กรอบ)
- วงกลม `V` (กลาง)
- กล่อง `Memory` (ด้านขวา, มีเส้นคู่กรอบ)
แต่ละ Processor เชื่อม (แบบ full mesh / ไขว้กันทุกเส้น) เข้ากับ V ทั้งสามและแต่ละ V เชื่อมกับ Memory ทั้งสาม (เส้นเชื่อมกันแบบ cross-connection จำนวนมาก)

มุมขวาล่าง: `53`

---

---

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

**รายละเอียดจากภาพ (vision):**

**หัวข้อ:** Hardware Redundancy Recap

**คอลัมน์ซ้าย — `Data path methods:` (สีน้ำเงิน):**
- Replication in space (costly)
  - Duplicate and compare
  - Triplicate and vote
  - Pair-and-spare
  - NMR/hybrid
- Replication in time (slow?)
  - Recompute and compare
  - Recompute and vote
  - Alternating logic
  - Recompute after shift
  - Recompute after swap
  - Replicate operand segments
- Mixed space-time replication
- Monitoring (imperfect coverage)
  - Watchdog timer
  - Activity monitor
- Low-redundancy coding
  - Parity prediction
  - Residue checking
  - Self-checking design

**คอลัมน์ขวาบน — `Control unit methods:` (สีม่วง):**
- Coding of control signals
- Control-flow watchdog
- Self-checking design

**คอลัมน์ขวากลาง — `Glue logic methods:` (สีเขียว):**
- Self-checking design

**แผนภาพ (ขวาล่าง):** วงรีสีชมพู `Control unit` ด้านบน
- ลูกศรลง `Control signals` จาก Control unit ไปยัง Data path
- กลุ่มรูปดาวสีเขียว `Glue logic` อยู่ระหว่าง Control unit กับ Data path
- ลูกศรขึ้น `Condition signals` จาก Data path กลับไป Control unit
- บล็อกสี่เหลี่ยม `Data path` ด้านล่าง มี `Inputs` (ลูกศรเข้าซ้าย) และ `Outputs` (ลูกศรออกขวา) ภายในมีช่องสี่เหลี่ยมเล็ก (สีส้ม) และจุดไข่ปลา `...` แทน register/block ต่าง ๆ

มุมขวาล่าง: `54`

---

---

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

**รายละเอียดจากภาพ (vision):**

**หัวข้อ:** Replication in Space

ข้อความ:
- The following schemes have already been discussed in connection with fault masking

**แผนภาพ 4 รูป:**

1. `Duplicate and compare` (ซ้ายบน): โมดูล `1` และ `2` อินพุตเดียวกัน
   เอาต์พุตโมดูล 1 ตรงออกไปทางขวา (เอาต์พุต system)
   โมดูล 2 → วงกลม `C` (ป้าย `Comparator`) ซึ่งเทียบกับเอาต์พุตโมดูล 1 (เส้นเชื่อมลงมา)
   เอาต์พุต `Error` (เส้นประ) ออกจาก C ทางขวา

2. `Triplicate and vote` (ซ้ายล่าง): โมดูล `1`,`2`,`3` อินพุตเดียวกัน
   เอาต์พุตรวมที่วงกลม `V` (ป้าย `Voting unit`) เอาต์พุตออกขวา

3. `Pair-and-spare` (ขวาบน): มี 2 คู่ ได้แก่ (`1`,`2`) และ (`1'`,`2'`)
   คู่บน: `1` ตรงออกไป, `2` → วงกลม `C` (ป้าย `Comparators` ด้านล่าง)
   คู่ล่าง: `1'` ตรงออกไป, `2'` → วงกลม `C` อีกตัว
   เอาต์พุต `Error` (เส้นประ) จาก C ทั้งสองเข้าสู่บล็อกสี่เหลี่ยม `S` (ป้าย `Switch` ด้านบน) แล้วออกทางขวา

4. `NMR/Hybrid` (ขวาล่าง): โมดูล `1`,`2`,`3` (กล่องส้ม) และกล่อง `4` (ป้าย `Spare`)
   เอาต์พุตทั้งหมดเข้าแถบแนวตั้ง `S` (switch) แล้วเข้าสู่วงกลม `V`
   เอาต์พุตออกขวา ป้าย `Switch-voting unit` (มีเส้นประ feedback จากหลัง V กลับไปที่ S ด้านบน)

มุมขวาล่าง: `55`

---

---

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

**รายละเอียดจากภาพ (vision):**

**หัวข้อ:** Replication in Time

ข้อความ:
- Can be slow, but in many control applications, extra time is available
- Interleaving of the primary and duplicate computations saves time

**แผนภาพ (flowgraph):**

รูปซ้าย:
- `Computation flowgraph, and schedule with 2 adders`
- ที่เวลา `t₀`: มีสองโหนด `+` (adder) รับอินพุต
- ที่เวลา `t₀ + 1`: โหนด `×` (multiplier) รับผลจาก adder ทั้งสอง
- ที่เวลา `t₀ + 2`: ไม่มีโหนด (เอาต์พุตออกด้านล่างเป็นลูกศรยาว)
- ข้าง ๆ (ขวาของ flowgraph) แสดงตารางเวลาแบบ interleaving: โหนด `+` สองตัวกับ `×` ถูกใส่ในกรอบสีเหลือง ป้าย `Duplicate computation` โดยผู้คำนวณซ้ำวางตัวสลับเวลา (เลื่อนลงหนึ่งบรรทัด)

รูปกลาง (บน):
- แสดงการจัดตารางด้วย adder ตัวเดียว: บนสุดโหนด `+` หนึ่งตัว (รับอินพุต 2 เส้น)
- แถวล่าง (หลังเส้นประ) มีโหนด `×` และโหนด `+` (รับอินพุต 2 เส้น)
- ป้ายใต้รูป: `Schedule with 1 adder`

รูปขวา:
- โหนด `+` (บน) → `×` (ล่าง) และโหนด `+` (กลาง/ขวา) → `×` เดียวกัน
- ส่วนที่เป็น `Duplicate computation` อยู่ในกรอบสีเหลือง (คอลัมน์ขวา) แสดงการคำนวณซ้ำด้วย adder ตัวที่สอง
- เส้นประแบ่งช่วงเวลาเป็น 3 ช่วง

มุมขวาล่าง: `56`

---

---

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

**รายละเอียดจากภาพ (vision):**

**หัวข้อ:** Recompute and Compare/Vote

ข้อความ:
- Repeat computation and store the results for comparison or voting
- Comparison or voting need not be done right away; primary result may be used in further computations, with the result subsequently validated, if appropriate
- On a simultaneous multithreading architecture, multiple instruction streams may be interspersed
- Some Cray machines take advantage of extensive hardware resources to execute instructions twice

**แผนภาพ flowgraph 3 ส่วน:**
- ซ้าย: โหนด `+`,`+` → `×` แล้วมีแท่งสี่เหลี่ยมสีส้ม (register/result) ต่อท้าย
  ป้ายด้านล่าง: `Use as operand in further computations, while awaiting confirmation of validity` (มีเส้นประแสดงการรอตรวจสอบ)
- กลาง (กรอบเหลืองป้าย `Duplicate computation`): โหนด `+`,`+` → `×` → แท่งสีส้ม (คำนวณซ้ำ)
- ขวา (กรอบเหลืองป้าย `Triplicate computation`): โหนด `+`,`+` → `×` → แท่งสีส้ม (คำนวณสามครั้ง)

มุมขวาล่าง: `57`

---

---

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

**รายละเอียดจากภาพ (vision):**

**หัวข้อ:** Mixed Space/Time Replication

ข้อความ:
- Instead of duplicating the computation with no hardware change (slow) or duplicating the entire hardware (costly), we can add some hardware to make the interleaved recomputations more efficient

**แผนภาพ flowgraph:**
- ซ้าย: flowgraph เดิม `Original computation (T = 3)` — โหนด `+` → `×`
- กลาง: กรอบสีเหลืองป้าย `Duplicate computation`
  ป้ายบน: `Recomputation with same hardware resources (T = 5, excluding compare time)`
  ภายในมี `+` (บน) → `×` (กลาง) และ `+` (ขวา) → `×` เดียวกัน (ใช้ adder ซ้ำ)
- ขวา: flowgraph ด้านซ้ายเหมือนเดิม (โหนด `+`,`+`) → `×`
  ส่วน recomputation อยู่ในกรอบเหลืองด้านขวา
  ป้ายขวาบน: `Recomputation with the inclusion of an extra adder (T = 3, excluding compare time)`
  ป้ายซ้ายบน: `Consider the effect of including a second adder`

มุมขวาล่าง: `58`

---

---

## Slide 59: Error Detection by  *(visual)*
Duplicated Instructions (EDDI)
• The redundant code is compared before Store

**รายละเอียดจากภาพ (vision):**

**หัวข้อ:** Error Detection by Duplicated Instructions (EDDI)

ข้อความ:
- The redundant code is compared before Store

**โค้ด 2 คอลัมน์:**

`Original Code`
```
add r1, r2, r3     // r1 = r2 + r3
xor r4, r1, r5     // r4 = r1 XOR r5
store r4, 0($r6)   // Mem[$r6] = r4
```

`Code with EDDI-like Redundancy`
```
add r1, r2, r3      // r1 = r2 + r3
add r11, r12, r13   // r11 = r12 + r13
xor r4, r1, r5      // r4 = r1 XOR r5
xor r14, r11, r15   // r14 = r11 XOR r15
bne r4, r14, error  // if r4 !=r14, goto error
store r4, 0($r6)    // Mem[$r6] = r4
```

มุมขวาล่าง: `59`

---

---

## Slide 60: Contents
• Handling Faults
• Interwoven Redundant Logic
• Combinatorial Modeling
• TMR & its application
• Replication & Voting
• Alternating Logic
• Fail-safe Systems

---

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

**รายละเอียดจากภาพ (vision):**

**หัวข้อ:** Alternating Logic: Basic Ideas

ข้อความ:
- Transmission of data over unreliable wires or buses
  - Send data; store at receiving end
  - Send bitwise complement of data
  - Compare the two versions
  - Detects wires s-a-0 or s-a-1, as well as many transients
- The *dual* of a Boolean function f(x₁, x₂, . . . , xₙ) is another function f_d(x₁, x₂, . . . , xₙ) such that f_d(x₁′, x₂′, . . . , xₙ′) = f′(x₁, x₂, . . . , xₙ)
- Fact: Obtain the dual of f by exchanging AND and OR operators in its logical expression. For example, the dual of f = ab ∨ c is f_d = (a ∨ b)c

**แผนภาพวงจร (ล่างซ้าย):**
- บล็อก `f` รับ `Inputs` (หลายเส้น) → เอาต์พุต `Output`
- บล็อก `f_d` รับ `Compl. inputs` (อินพุตกลับด้าน, หลายเส้น)
- เอาต์พุตของ `f` และ `f_d` เข้าเกต XOR/XNOR (เกตโค้ง มีจุดที่เอาต์พุต) → เอาต์พุต `Error`

ข้อความ (ขวาล่าง): `Advantages of this approach compared with duplication include a smaller probability of common errors`

มุมขวาล่าง: `61`

---

---

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

**รายละเอียดจากภาพ (vision):**

**หัวข้อ:** Alternating Logic: Self-Dual Functions

ข้อความ:
- A function f is self-dual if f(x₁, x₂, . . . , xₙ) = f_d(x₁, x₂, . . . , xₙ)
- For example, both the sum a ⊕ b ⊕ c and carry ab ∨ bc ∨ ca outputs of a full-adder are self-dual functions
- With a self-dual function f, the functions f and f_d in the diagram above can be computed by using the same circuit twice (time redundancy)
- Many functions of practical interest are self-dual
- **Examples** (proofs left as exercise)
  - A *k*-bit binary adder, with 2*k* + 1 inputs and *k* + 1 outputs, is self-dual
  - So are 1's-complement and 2's-complement versions of such an adder

**แผนภาพวงจร (ขวา):**
- บล็อก `f` รับ `Inputs` → เอาต์พุต `Output`
- บล็อก `f_d` รับ `Compl. inputs`
- เอาต์พุตทั้งสองเข้าเกต XOR/XNOR → `Error`
- มีข้อความสีแดง `Use same circuit twice` และเส้นประสีแดงเชื่อมระหว่างบล็อก `f` กับบล็อก `f_d` (แสดงว่าใช้ circuit เดียวกันสองครั้ง)

มุมขวาล่าง: `62`

---

---

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

**รายละเอียดจากภาพ (vision):**

**หัวข้อ:** Recomputation with Transformed Operands

ข้อความ:
- Alternating logic is a special case of the following general scheme, with its encoding and decoding functions being bitwise complementation

**แผนภาพวงจร:**
- แถวบน: `Inputs` → บล็อก `f` → `Output`
- แถวล่าง: `Inputs` → บล็อก `e` (ป้าย `Encode`) → บล็อก `g` → บล็อก `d` (ป้าย `Decode`)
- เอาต์พุตของ `f` และ `d` เข้าเกต XOR/XNOR → `Error`
- ข้อความสีแดง: `XNOR if lower path finds complement of the result`

**Recompute after shift**
- When f is binary addition, we can use shifts for encoding and decoding
- Shifting causes the adder circuits to be exercised differently each time
- Originally proposed for ALUs with bit-slice organization

**Recompute after swap**
- When f is binary addition, we can use swaps for encoding and decoding
  - Swap the two operands; e.g., compute b + a instead of a + b
  - Swap upper and lower halves of the two operands (modified adder)

มุมขวาล่าง: `63`

---

---

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

**รายละเอียดจากภาพ (vision):**

**หัวข้อ:** Time-Redundant, Segmented Addition

ข้อความ:
- Instead of using a *k*-bit adder twice for error detection or 3 times for error correction, one can segment the operands into 2 or 3 parts and similarly segment the adder; perform replicated addition on operand segments and use comparison/voting to detect/correct error

**แผนภาพวงจร (ซ้าย):**
- อินพุต `x_L`, `x_H` เข้า MUX (สี่เหลี่ยมคางหมู) ตัวบน
- อินพุต `y_L`, `y_H` เข้า MUX ตัวล่าง
- มี FF (flip-flop) ที่สัญญาณ `c_in` (ด้านบน) และ `c_out` (ด้านขวา) — เส้นประแสดง carry feedback จาก `c_out` ผ่าน FF กลับเป็น `c_in`
- MUX บน → บล็อก `Lower half of adder`
- MUX ล่าง → บล็อก `Upper half of adder`
- เอาต์พุต `Lower half of adder` ไปเป็นเอาต์พุต (ลูกศรขวา) และป้อนเข้า comparator `C` (ป้าย `Comparator`)
- เอาต์พุต `Upper half of adder` ป้อนเข้า `C` เช่นกัน
- เอาต์พุต `C` → `Error` (เส้นประ)

ข้อความ (ซ้ายล่าง):
- Various other segmentation schemes have been suggested
- **Example:** 16-bit adder with 4-way segmentation and voting

ข้อความ (ขวาบน): `Sum computed in two cycles: The lower half in cycle 1, and the upper half in cycle 2`

**แผนภาพบล็อก (ขวาล่าง, พื้นน้ำเงิน):** วงจร adder แบบแบ่งส่วน ประกอบด้วย
- `4 bit 4:1 mux` สองตัว (มีอินพุต `16` กำกับด้านบน) และ `2:1 mux`
- `4 bit adder` สามตัว (มี `ci` และ `co` กำกับ)
- `4 bit voter` (ด้านล่าง, มี `4` กำกับ)
- `1 bit reg` และ `1 bit voter` (ด้านขวา)
เชื่อมกันด้วยเส้นทางบัสขนาน
เครดิตใต้ภาพ: `Townsend, Abraham, and Swartzlander, 2003`

มุมขวาล่าง (ของสไลด์): `64`

---

---

## Slide 65: Contents
• Handling Faults
• Interwoven Redundant Logic
• Combinatorial Modeling
• TMR & its application
• Replication & Voting
• Alternating Logic
• Fail-safe Systems

---

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

---

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

**รายละเอียดจากภาพ (vision):**

**หัวข้อ:** Fail-Safe System Specification

ข้อความ:
- Amusement park train safety system
- Signal s_B when asserted indicates that the train is at beginning of its track (can move forward, but should not be allowed to go back)
- Signal s_E when asserted indicates that the train is at end of its track (can go back, but should not move forward)
- Is the specification above consistent and complete?
- No, because it does not say what happens if s_B = s_E = 1; this would not occur under normal conditions, but because such sensors are often designed to fail in the safe mode, the combination is not impossible
- Why is this a problem, though? (Train simply cannot be moved at all)
- Completeness will prevent potential implementation or safety problems

**แผนภาพ (ขวา):** วงรีสองวง
- วงรีซ้าย (ขอบเขตโปร่ง) ป้าย `Input space` มีจุด `Input`
- วงรีขวา (สีเหลือง) ป้าย `Output space` ภายในแบ่งเป็นโซน มีป้าย `Correct output`, `Safe outputs`, `Unsafe outputs` (มีป้ายลูกศรทึบและเส้นประ)
- จากจุด `Input` มีลูกศรออกตามทิศทางต่าง ๆ (ลูกศรทึบไปยัง Correct output; ลูกศรประที่มีเครื่องหมาย `×`(กากบาทแดง) ไปยังโซนอื่นแทนการผิดพลาด)

มุมขวาล่าง: `67`

---

---

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

**รายละเอียดจากภาพ (vision):**

**หัวข้อ:** Fail-Safe 2-out-of-4 Code Checker

ข้อความ:
- Input: 4 bits *abcd*, exactly 2 of which must be 1s
- Output: *fg* = 01 or 10, if the input is valid
  - 00 safe erroneous output
  - 11 unsafe erroneous output

**Codewords (ตารางพื้นฟ้า, ซ้าย):**

| a | b | c | d |
|---|---|---|---|
| 0 | 0 | 1 | 1 |
| 0 | 1 | 0 | 1 |
| 0 | 1 | 1 | 0 |
| 1 | 0 | 0 | 1 |
| 1 | 0 | 1 | 0 |
| 1 | 1 | 0 | 0 |

(หัวตาราง: `Codewords` และ `a b c d`)

**แผนภาพวงจร (ขวา):**
- อินพุต `a`,`b` เข้าเกต XOR (เกตโค้ง) ตัวหนึ่ง; `c`,`d` เข้าเกต XOR อีกตัวหนึ่ง
- เอาต์พุตของสอง XOR เข้าเกต AND → เส้นสัญญาณหนึ่ง
- อินพุต `a`,`b` เข้าเกต AND ตัวหนึ่ง; `c`,`d` เข้าเกต AND อีกตัวหนึ่ง
- เอาต์พุตของสอง AND เข้าเกต XOR → เส้นสัญญาณที่สอง
- มีสัญญาณ `Preset` ป้อนเข้าที่บล็อก `S R / Q` (latch: `S`, `R`, เอาต์พุต `Q` และ `Q̄`)
- เอาต์พุตของ AND (ตัวบนสำหรับ XOR-คู่แรก) เข้าสู่ขาอินพุตของ AND ตัวบนขวา และเข้า S (พร้อมกับ Preset)
- เอาต์พุต `Q` ป้อนกลับเข้าเกต AND ตัวบนและล่าง (ด้านขวา)
- เกต AND ขวาบน → เอาต์พุต `f`; เกต AND ขวาล่าง → เอาต์พุต `g`

คำบรรยายใต้ภาพ: `Output will become permanently 00 upon the first unsafe condition`

มุมขวาล่าง: `68`

---

---

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

**รายละเอียดจากภาพ (vision):**

**หัวข้อ:** Fail-Safe State Machines

ข้อความ:
- Use an error code to encode states
- Implement the next-state logic so that the machine is forced to an error state when something goes wrong
- Possible design methodology:
  - Use Berger code for states, avoiding the all 0s state with all-1s check, and vice versa
  - Implement next-state logic equations in sum-of-products form for the main state bits and in product-of-sums form for the check state bits
  - The resulting state machine will be fail-safe under unidirectional errors

**ตารางซ้าย (พื้นเขียว) — Input / State transition:**

| State | x=0 | x=1 |
|---|---|---|
| A | E | B |
| B | C | D |
| C | A | D |
| D | E | D |
| E | A | D |

(หัวคอลัมน์: `State`, `Input` ครอบ `x=0`, `x=1`)

**ตารางกลาง — Encoding:**

| State | Encoding |
|---|---|
| A | 001 10 |
| B | 010 10 |
| C | 011 01 |
| D | 100 10 |
| E | 101 01 |

**กล่องข้อความ (ขวา):**
- Hardware overhead for *n*-state machine consists of O(log log *n*) additional state bits and associated next-state logic, and a Berger code checker connected to state FFs

มุมขวาล่าง: `69`

---

---

## Slide 70: Home Exercise: Non-SP  *(visual)*
• A system operated from X to Y via non serial-parallel path
• Reliabilities of Module (A, B, K) = (Ra, Rb, Rk)
• Find the system reliability

**รายละเอียดจากภาพ (vision):**

**หัวข้อ:** Home Exercise: Non-SP

ข้อความ:
- A system operated from X to Y via non serial-parallel path
- Reliabilities of Module (A, B, K) = **(Ra, Rb, Rk)** (สีน้ำเงิน)
- Find the **system reliability** (สีแดง)

**แผนภาพ:** ระบบ 3 ชั้นขนานกันจาก X ไป Y
- อินพุต `X` แยกเป็น 3 เส้นทาง
- แต่ละเส้นทางมีโมดูล `A` (ด้านซ้าย), `B` (ด้านขวา)
- ระหว่างโมดูล A และ B ตามแนวนอน มีโมดูล `K` เชื่อมแบบข้ามแนว (แนวนอน) ระหว่างเส้นทาง:
  - `K` หนึ่งตัววางระหว่างแถวบนและแถวกลาง (ป้อนขึ้น/ลงเชื่อมกับเส้นทางแถวบนและกลาง)
  - `K` อีกหนึ่งตัววางระหว่างแถวกลางและแถวล่าง
- เอาต์พุตของทุกเส้นทางรวมกันเป็น `Y` ทางขวา
(โครงสร้างไม่ใช่ serial-parallel ธรรมดา มี cross-link ผ่าน K)

มุมขวาล่าง: `70`

---

## Slide 71: Midterm Exam
• On-Site
• 12 Oct 2026, 13.00-16.00
• CP: #17-01, CEDT: #18-15 Eng.Bldg.no.4
• All about Fault Tolerant Computing
• Open Books, Open Net

---

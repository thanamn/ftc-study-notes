# FTC07 Fault Masking — Visual Notes (A)

หมายเหตุ: บันทึกจากภาพสไลด์เท่านั้น ข้อความ/ป้าย/สูตร/ตัวแปร/ศัพท์เทคนิคคงไว้ตามต้นฉบับทุกประการ

---

## Slide 1

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

## Slide 5

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

## Slide 6

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

## Slide 7

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

## Slide 8

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

## Slide 10

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

## Slide 11

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

## Slide 12

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

## Slide 13

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

## Slide 17

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

## Slide 18

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

## Slide 19

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

## Slide 20

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

## Slide 21

**หัวข้อ:** Non-Series Parallel System - 1

- Pick a module 'm' in the system

**สูตร:**
- `P(sys works) = P(sys works | m works) P(m works) + P(sys works | m fails) P(m fails)`
- `Rsys = P(sys works | m)Rm + P(sys works | m')(1 − Rm)`

**Reliability block diagram** (เหมือน Slide 20):
- อินพุต → `A` (ไฮไลต์) → แยกเป็น `E` (บน) และ `B` (กลาง); `F` (ล่าง) รับจากก่อน `A` แล้วรวมก่อน `C`; `B` → `C` → รวมกับ `E` ก่อน `D` → `D` → เอาต์พุต

---

## Slide 22

**หัวข้อ:** Non-Series Parallel System - 2

- Pick 'm' to be module E. Consider 'E fails';
- `P(sys works | E') = [1 − (1 − R_A R_B)(1 − R_F)]R_C R_D`

**ข้อความสีแดง:** 'module E fails' = 'path E opened' พร้อมลูกศรสีแดงชี้ลง

**Reliability block diagram:** แสดง `E` ถูกเปิดออก (เส้นทางบนขาด) เหลือ `A` → `B` → `C` → `D` และ `F` ชนาน `B`; โหนดรวมก่อน `D` จาก `C` และจาก (ไม่มี E)

---

## Slide 23

**หัวข้อ:** Non-Series Parallel System - 3

- Next, consider 'E works' = 'path E shorted' (สีแดง)
- Still unsolved, do again wt a different module

**Reliability block diagram:** แสดง `E` ถูก short (เส้นทางบนเชื่อมตรง) โดยที่ `E` ไม่ปรากฏเป็นบล็อกแล้ว (มีลูกศรสีแดงชี้ลงตรงกลางบน); โครงสร้าง `A` (ไฮไลต์ฟ้า), `B`, `C`, `D`, `F` ยังคงอยู่ โดยทางบนลัดจาก `B` ไปยังโหนดก่อน `D`

---

## Slide 24

**หัวข้อ:** Non-Series Parallel System - 4

- Next, consider 'B fails' = 'path B opened' (สีแดง)
- `P(sys works | E and B') = [1−(1−R_A)(1−R_F R_C)]R_D`

**Reliability block diagram:** บล็อก `B` ถูกเปิดออก (มีลูกศรสีแดงชี้ลงตรงตำแหน่ง B); โครงสร้าง: `A` (ไฮไลต์) → และ `F`; ทางบนลัดไปโหนดก่อน `D`; `C` → รวมก่อน `D`; `D` → เอาต์พุต

---

## Slide 25

**หัวข้อ:** Non-Series Parallel System - 5

- Next, when **B works** (สีแดง), still the same as before
- `P(sys works | E and B) = [1−(1−R_A)(1−R_F R_C)]R_D`

**ข้อความสีแดง:** 'module B works' = 'path B shorted'

**Reliability block diagram:** แสดง `B` ถูก short (ลูกศรแดงชี้ลงตรงกลางบน); โครงสร้าง `A` (ไฮไลต์) → ทางบนลัดไปโหนดก่อน `D`; `F` → รวมก่อน `C`; `C` → รวมก่อน `D`; `D` → เอาต์พุต

---

## Slide 29

**หัวข้อ:** Non-Series Parallel System (again)

**Reliability block diagram** (เหมือน Slide 20 แต่ `A` มีกรอบสีแดง):
- อินพุต → `A` (กรอบแดง) → แยกเป็น `E` (บน) และ `B` (กลาง); `F` (ล่าง) รับจากก่อน `A` รวมก่อน `C`; `B` → `C` → รวมกับ `E` ก่อน `D` → `D` → เอาต์พุต

**ข้อความ:**
- Choose **A** as the keystone component

**สูตร (สีแดง):**
- `Rsys = P(sys works|A)R_A + P(sys works|A')(1-R_A)`

**หมายเหตุ (ขวาล่าง):** `R:Reliabilty; P:Possibility`

---

## Slide 30

**หัวข้อ:** Non-Series Parallel System (again-1)

**Reliability block diagram:** `A` ถูกนำออก (short) เนื่องจากพิจารณากรณี A works; อินพุตตรงเข้าสู่ `B` (กลาง) และ `F` (ล่าง); `B` → `C`; `F` รวมก่อน `C`; ทางบน `E` รับจากก่อน `B` และรวมก่อน `D`; `C` → รวมก่อน `D`; `D` → เอาต์พุต

**ข้อความหัวข้อย่อย:**
- If A works: → *serial/parallel system*

**สูตร (สีแดง):**
- `P(sys works|A) = (1 − (1 − R_E)(1 − (1 − (1 − R_B)(1 − R_F)) R_C)) R_D`

---

## Slide 31

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

## Slide 33

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

## Slide 34

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

## Slide 36

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

## Slide 37

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

## Slide 38

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

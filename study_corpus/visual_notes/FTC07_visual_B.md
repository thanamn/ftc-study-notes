# FTC07 Fault Masking — Visual Notes (Part B)

บันทึกภาพสไลด์วิชา Fault Tolerant Computing หมวด Fault Masking (ชุด B)
อ่านจากไฟล์ภาพจริงใน `study_corpus/images/` ทุกข้อความภาษาอังกฤษในสไลด์คงไว้ตามต้นฉบับ

---

## Slide 40

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

## Slide 41

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

## Slide 43

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

## Slide 44

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

## Slide 45

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

## Slide 46

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

## Slide 47

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

## Slide 48

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

## Slide 49

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

## Slide 50

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

## Slide 52

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

## Slide 53

**หัวข้อ:** Check yourself

ข้อความ: `Q. List the conditions under which it will fail?` (ตัวเอียง)

**แผนภาพ:** โมดูลเรียงเป็น 3 แถว แต่ละแถวมี:
- กล่อง `Processor` (ด้านซ้าย, มีเส้นคู่กรอบ)
- วงกลม `V` (กลาง)
- กล่อง `Memory` (ด้านขวา, มีเส้นคู่กรอบ)
แต่ละ Processor เชื่อม (แบบ full mesh / ไขว้กันทุกเส้น) เข้ากับ V ทั้งสามและแต่ละ V เชื่อมกับ Memory ทั้งสาม (เส้นเชื่อมกันแบบ cross-connection จำนวนมาก)

มุมขวาล่าง: `53`

---

## Slide 54

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

## Slide 55

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

## Slide 56

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

## Slide 57

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

## Slide 58

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

## Slide 59

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

## Slide 61

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

## Slide 62

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

## Slide 63

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

## Slide 64

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

## Slide 67

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

## Slide 68

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

## Slide 69

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

## Slide 70

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

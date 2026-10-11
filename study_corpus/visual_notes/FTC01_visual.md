# FTC01 — Dependable Computing : Visual Notes (จากภาพสไลด์)

เอกสารนี้บรรยายเนื้อหาที่ปรากฏจริงบนภาพสไลด์แต่ละใบ (ภาพถ่ายสไลด์บรรยาย) โดยคงข้อความภาษาอังกฤษ/ตัวเลข/สูตร/ป้ายกำกับ ทุกอย่างไว้ตามที่ปรากฏบนสไลด์

## Slide 1
หัวข้อบนสุด (กึ่งกลาง): **COURSE SYLLABUS**

รายการด้านล่าง (คอลัมน์ซ้ายเป็นป้ายภาษาไทย, คอลัมน์ขวาเป็นค่า):

| ป้าย (ไทย) | ค่า |
|---|---|
| วิชา | **2110473 Fault Tolerant Computing** |
| จำนวนหน่วยกิต (Course Credit) | 3 หน่วยกิต |
| ชื่อผู้สอน | ผศ.ดร.อาทิตย์ ทองทักษ์ (Rm.no. 18—04) |
| (อีเมล) | Arithit.th@chula.ac.th |

**วัตถุประสงค์ทั่วไป เพื่อให้ผู้เรียนได้**
1. เข้าใจทฤษฎี ความรู้พื้นฐานและมีโอกาสติดตามเทคโนโลยีที่เกี่ยวข้องกับ Fault Tolerant Computing
2. เข้าใจถึงขั้นตอนวิธีการในการวิเคราะห์และการออกแบบระบบที่ดีำเนินการแบบ Fault Tolerant Computing
3. มีประสบการณ์ในการใช้เครื่องมือการออกแบบระบบที่ดีำเนินการแบบ Fault Tolerant Computing

**เนื้อหารายวิชา (อาจมีการเปลี่ยนแปลงได้ตามความเหมาะสม)**
1. Dependable Computing: Terminology
2. Fault Tolerant Computing: Basic Concept
3. Redundancy Technique: Hardware, Software, Information, Time
4. Error Detection & Error Correction
5. Modeling & Evaluation: Fault Modeling & Reliability
6. Testing Digital Circuits
7. Design for Test

**การวัดผลเรียน**
1. Midterm Test 30%
2. Final Assignment 20%
3. Homework 50%

**หนังสืออ่านประกอบ**
1. Several Sources

(มุมขวาล่าง: เลขหน้า 1)

## Slide 3
หัวข้อ: **Weekly Plan (tentative)**

ตาราง (หัวตารางพื้นสีส้ม):

| Date 1 | Week | Chapter | Class | Assignment |
|---|---|---|---|---|
| 2026-08-03 | 1 | Administrative issues | Eng3-421 | |
| 2026-08-10 | 2 | FTC01 Dependable Computing | TBA | 1 |
| 2026-08-17 | 3 | FTC02 Fault Tolerant Systems | TBA | 2 |
| 2026-08-24 | 4 | FTC02plus Checkpointing and Recovery | TBA | 3 |
| 2026-08-31 | 5 | FTC03 Coding Theory | TBA | 4 |
| 2026-09-07 | 6 | FTC04 Self Checking | TBA | 5 |
| 2026-09-14 | 7 | FTC05 Fault Masking and Recovery | TBA | 6 |
| 2026-09-21 | 8 | **Midterm week** | | |
| 2026-09-28 | 9 | Review | ZOOM | |
| 2026-10-05 | 10 | Review | ZOOM | |
| 2026-10-12 | 11 | **MIDTERM TEST** (ตัวสีแดง) | TBA | |
| 2026-10-19 | 12 | TDC01 Overview of Testing Digital Circuits | ZOOM | 7 |
| 2026-10-26 | 13 | TDC02 Delay Fault Testing | ZOOM | 8 |
| 2026-11-02 | 14 | TDC03 Digital Circuit Testing Issues | ZOOM | 9 |
| 2026-11-09 | 15 | TDC04 Asynchronous Circuit Testing | ZOOM | 10 |
| 2026-11-16 | 16 | Review | ZOOM | **FINAL ASSIGNMENT** |
| 2026-11-23 | | **Final week** | | (as of Aug.03, 2025) |

หมายเหตุ: แถวสลับสีพื้นตามแถว, แถว Midterm week / Final week มีพื้นสีส้มอ่อน; ตัวอักษร "MIDTERM TEST" และ "FINAL ASSIGNMENT" เป็นสีแดง; "(as of Aug.03, 2025)" เป็นตัวเอียงสีแดง
(มุมขวาล่าง: เลขหน้า 3)

## Slide 9
หัวข้อ (สองบรรทัด): **Dependability:** / **Attributes, Means and Impairments**

แผนภาพแบบต้นไม้ (tree) โดยมี "Dependability" อยู่ซ้ายสุด แล้วแตกแขนงไปทางขวา 3 กิ่งหลัก (เส้นสีน้ำเงิน/เทา):
- **ATTRIBUTES** → แตกเป็นรายการ (สีเขียว): **AVAILABILITY**, **RELIABILITY**, **SAFETY**, **CONFIDENTIALITY**, **INTEGRITY**, **MAINTAINABILITY**
- **MEANS** → แตกเป็นรายการ (สีเขียว): **FAULT PREVENTION**, **FAULT TOLERANCE**, **FAULT REMOVAL**, **FAULT FORECASTING**
- **IMPAIRMENTS** → แตกเป็นรายการ (สีเขียว): **FAULTS**, **ERRORS**, **FAILURES**

ที่สำคัญ: บนสไลด์นี้มี **วงรีสีแดงหนา (hand-drawn highlight)** ล้อมกรอบกลุ่ม **ATTRIBUTES** และรายการย่อยทั้ง 6 ตัว (AVAILABILITY … MAINTAINABILITY)
(มุมขวาล่าง: เลขหน้า 9)

## Slide 12
หัวข้อ: **Examples of Attributes**

ตาราง (หัวตารางพื้นสีน้ำเงิน ตัวอักษรขาว):

| Type of system | Availability | Reliability | Safety | Integrity | Maintainability |
|---|---|---|---|---|---|
| Aircraft systems | X | X | X | X | X |
| Nuclear reactor | X | X | X |  | X |
| Internet News page | X | X |  | X | X |
| Smart Phone | X |  | X | X | X |
| Pace Maker | X | X | X | X |  |
| Automobile System |  | X | X | X | X |

หมายเหตุ: หัวคอลัมน์สุดท้ายตัดคำเป็นสองบรรทัด "Maintainab / ility"; ช่องที่มีเครื่องหมาย X มี X กำกับ ส่วนช่องว่างไม่มีตัวอักษร
(มุมขวาล่าง: เลขหน้า 12)

## Slide 13
หัวข้อ: **Historical Evolution** (ตัวอักษรสีม่วงเข้ม)

รายการแบบ bullet (สี่เหลี่ยมเล็ก):
- 40's: ENIAC
  - 18K vacuum tubes → failed ~ every 7 mns
  - 18K multiplies/minute → 7 mns ~ one program execution
  - **Need RELIABILITY** (ตัวอักษรสีม่วง/แดงเข้ม หนา)
- 60's: Interactive systems
  - **+ AVAILABILITY** (สีม่วงเข้ม หนา)
- 70's: F-8 Crusader, MD-11, Patriot missile defense
  - **+ SAFETY** (สีม่วงเข้ม หนา)
- 90's-today: Internet, E-commerce, Grid/Web services
  - **+ SECURITY** (สีม่วงเข้ม หนา)

(มุมขวาล่าง: เลขหน้า 13)

## Slide 14
หัวข้อ: **Dependability and Security**

แผนภาพเวนน์ (Venn diagram) วงรีสองวงเหลื่อมกัน:
- วงรีซ้าย มีป้ายด้านบนว่า **Security** (วงสีส้มอ่อน/ส้มอิฐ)
- วงรีขวา มีป้ายด้านบนว่า **Dependability** (วงสีเขียวอ่อน)
- ส่วนเหลื่อมตรงกลางเป็นสีเขียวอมน้ำตาล (ทับซ้อน)
- ลูกศรสีฟ้าสามลูกชี้ลงด้านล่าง พร้อมป้ายกำกับ:
  - จากส่วนของ Security (ซ้าย) → **Confidentiality**
  - จากส่วนเหลื่อมกลาง → **Availability, Integrity and Reliability**
  - จากส่วนของ Dependability (ขวา) → **Maintainability and Safety**

(มุมขวาล่าง: เลขหน้า 14)

## Slide 17
หัวข้อ: **Nines of Availability**

ตาราง (เส้นตารางดำ):

| # 9's | % | Downtime / year | Systems |
|---|---|---|---|
| 2 | 99% | ~5000 minutes | General web site |
| 3 | 99.9% | ~500 minutes | Amazon.com |
| 4 | 99.99% | ~50 minutes | Enterprise server |
| 5 | 99.999% | ~5 minutes | Telephone System |
| 6 | 99.9999% | ~30 seconds | Phone switches |

(มุมขวาล่าง: เลขหน้า 17)

## Slide 18
หัวข้อ: **Reliability**

ข้อความ bullet:
- The ability of an item to perform a required function under stated conditions up until specified time

สูตร (plain-text):
- m = 1 / λ   (เศษ 1 ส่วน λ)
- R(t) = e^(-λ·t) = e^(-(t/m))   (เขียนบนสไลด์เป็น R_(t) = e-λt = e-(t/m))
- m = t / log_(n) ( 1 / R_(t) )   (เขียนเป็นเศษส่วน เศษ = t, ส่วน = log_(n)(1/R_(t)))

กล่องคำอธิบาย "Where" (ด้านขวา):
- R_(t) = reliability
- e = exponential (2.178)
- λ = failure rate
- m = mtbf
- t = time

(มุมขวาล่าง: เลขหน้า 18)

## Slide 20
หัวข้อ: **Failure Metrics**

แผนภาพแกนเวลา (timeline) รูปแถบลูกศรสีฟ้าใหญ่ชี้ไปทางขวา (เริ่มจากเส้นคู่เล็ก ๆ ด้านซ้าย):
- บนแกนมีสัญลักษณ์:
  - รูปแปดเหลี่ยม/หกเหลี่ยมสีแดง (หยุด) ตัวแรก — ด้านล่างมีป้ายกล่องสีแดงว่า **System Failure**
  - จุดวงกลมสีเขียว — ด้านขวามีกล่องสีเขียวว่า **Resume Normal Operations**
  - รูปแปดเหลี่ยม/หกเหลี่ยมสีแดง ตัวที่สอง (ท้าย) — ด้านล่างมีป้ายกล่องสีแดงว่า **System Failure**
- วงเล็บ (brackets) เหนือแกน ระบุช่วงเวลา:
  - **Time to Repair** — เหนือช่วงจาก System Failure (ตัวแรก) ถึง Resume Normal Operations
  - **Time to Failure** — เหนือช่วงจาก Resume Normal Operations ถึง System Failure (ตัวที่สอง)
  - **Time Between Failures** — วงเล็บใหญ่คุมครอบตั้งแต่ System Failure ตัวแรก ถึง System Failure ตัวที่สอง

(มุมขวาล่าง: เลขหน้า 20)

## Slide 21
หัวข้อ (ด้านบน): **Design Tradeoffs** (ฟอนต์ใหญ่กลางจอ)
หัวข้อย่อย (ซ้าย): **Design Tradeoffs** (ตัวหนา มีเส้นใต้)

สูตร:
- **Availability = MTTF / (MTTF + MTTR)** (เขียนเป็นเศษส่วน: เศษ = MTTF, ส่วน = MTTF + MTTR)

กล่องด้านขวา:
- MTTF = Mean Time To Failure
- MTTR = Mean Time To Repair

รายการ bullet:
- How to make availability approach 100%?
  - MTTF → infinity (high reliability)
  - MTTR → zero (fast recovery)
- Need to define maximum repair time
- Need to define how Availability is measured

(มุมขวาล่าง: เลขหน้า 21)

## Slide 23
หัวข้อ: **Safety (cont.)**

ข้อความกลาง (ตัวหนา):
- **Absence of catastrophic consequences on the users or the environment**

รายการ bullet:
- Are commercial aircraft "safe"?
- They crash occasionally
- How many crashes are too many?
- Are cars "safe"?   They crash quite a lot

กล่องพื้นสีชมพู (กรอบดำ) ด้านล่าง:
- 40K deaths/yr; 800/week = 2 fully loaded Boeing 747/week

(มุมขวาล่าง: เลขหน้า 23)

## Slide 24
หัวข้อ: **Risk**

รายการ:
- *Risk* is defined to be expected loss per unit time:

สูตร (กลางจอ):
- **Risk = Σ pr(accident_i) x cost(accident_i)**  (เครื่องหมาย Σ ใหญ่; ตัวห้อย i ที่ accident)

รายการ:
- *Safety* is defined to be an acceptable level of risk:

สูตร:
- **Risk < pre-defined_delta**

(มุมขวาล่าง: เลขหน้า 24)

## Slide 34
หัวข้อ: **Characteristics of Resilient Systems**

ด้านซ้ายเป็นกราฟเส้น (line graph) แกน:
- แกนตั้ง: **System state**
- แกนนอน: **Environment**
- เส้นกราฟสีน้ำเงินมีรูปร่างเป็นเนิน/ลาดลง โดยมีจุดวงกลมสีแดงอยู่ตรงกลางของเส้น
- ป้ายกำกับพร้อมเส้นชี้:
  - **Resistance** (มีเส้นชี้ลงไปยังจุดบนเส้นกราฟ)
  - **Robustness** (มีเส้นวัดระยะแนวตั้ง จากยอดเนินลงมา — ระบุความสูง)
  - **Latitude** (มีเส้นวัดระยะตามแนวราบจากจุดอ้างอิงไปทางขวา)
  - **Precariousness** (มีเส้นชี้ลงจากตำแหน่งของเส้นกราฟ)

ข้อความด้านขวา (bullet สีแดงนำหน้า บางข้อตัวเอียง):
- **Latitude**: the maximum amount a system can be changed before losing its ability to recover (before crossing a threshold which, if breached, makes recovery difficult or impossible)
- **Resistance**: the ease or difficulty of changing the system; how "resistant" it is to being changed
- **Precariousness**: how close the current state of the system is to a limit or "threshold"
- *Panarchy: the degree to which a certain hierarchical level of an ecosystem is influenced by other levels* (ตัวเอียง สีเทา)

ข้อความด้านล่าง (กึ่งกลาง ตัวเอียง):
- *Closely linked to Adaptive Capacity*

(มุมขวาล่าง: เลขหน้า 34)

## Slide 36
หัวข้อ: **Dependability: / Attributes, Means and Impairments**

แผนภาพต้นไม้คล้าย Slide 9:
- **Dependability** (ซ้ายสุด) แตกแขนง 3 กิ่ง:
  - **ATTRIBUTES** → **AVAILABILITY**, **RELIABILITY**, **SAFETY**, **CONFIDENTIALITY**, **INTEGRITY**, **MAINTAINABILITY** (สีเขียว)
  - **MEANS** → **FAULT PREVENTION**, **FAULT TOLERANCE**, **FAULT REMOVAL**, **FAULT FORECASTING** (สีเขียว)
  - **IMPAIRMENTS** → **FAULTS**, **ERRORS**, **FAILURES** (สีเขียว)

ที่สำคัญ: บนสไลด์นี้มี **วงรีสีแดงหนา** ล้อมกรอบกลุ่ม **MEANS** และรายการย่อยทั้ง 4 ตัว (FAULT PREVENTION … FAULT FORECASTING)

(มุมขวาล่าง: เลขหน้า 36)

## Slide 37
หัวข้อ: **Exercise**

**Example**  Assume a disk subsystem with the following components and MTTF:
- 10 disks, each rated at 1,000,000-hour MTTF
- 1 SCSI controller, 500,000-hour MTTF
- 1 power supply, 200,000-hour MTTF
- 1 fan, 200,000-hour MTTF
- 1 SCSI cable, 1,000,000-hour MTTF

ข้อความ (ตัวเอียง):
- *Using the simplifying assumptions that the lifetimes are exponentially distributed and that failures are independent, compute the MTTF of the system as a whole.*

(มุมขวาล่าง: เลขหน้า 37)

## Slide 38
หัวข้อ: **Answer**

ด้านบนซ้ำโจทย์ Example (ย่อ):
- **Example**  Assume a disk subsystem with the following components and MTTF:
  - 10 disks, each rated at 1,000,000-hour MTTF
  - 1 SCSI controller, 500,000-hour MTTF
  - 1 power supply, 200,000-hour MTTF
  - 1 fan, 200,000-hour MTTF
  - 1 SCSI cable, 1,000,000-hour MTTF
- *Using the simplifying assumptions that the lifetimes are exponentially distributed and that failures are independent, compute the MTTF of the system as a whole.*

กรอบสีแดงหนา ด้านล่าง บรรจุคำตอบ:

**Answer**  The sum of the failure rates is

- **Failure rate_system = 10 × 1/1,000,000 + 1/500,000 + 1/200,000 + 1/200,000 + 1/1,000,000**
- **= (10 + 2 + 5 + 5 + 1) / 1,000,000 hours = 23 / 1,000,000 = 23,000 / 1,000,000,000 hours**

- or 23,000 FIT. The MTTF for the system is just the inverse of the failure rate:

- **MTTF_system = 1 / (Failure rate_system) = 1,000,000,000 hours / 23,000 = 43,500 hours**
- or just under 5 years.

(มุมขวาล่าง: เลขหน้า 38)

## Slide 41
หัวข้อ: **Fault Tolerance Techniques**

แผนภาพ: วงรีสีเขียว 3 วง เรียงซ้าย→ขวา เชื่อมด้วยลูกศรสีฟ้า:
- **Error Detection** → **Error Recovery** → **Fault Avoidance**
(ลูกศรชี้จาก Error Detection ไป Error Recovery และจาก Error Recovery ไป Fault Avoidance)

ภายใต้วงรีแต่ละวง มีสาขาย่อย (เส้นสีฟ้าเชื่อม):

ใต้ **Error Detection**:
- **Concurrent:** Detect errors during system operation
- **Pre-emptive:** Detect errors ahead of time

ใต้ **Error Recovery**:
- **Roll-back:** Restore system to a state before errors
- **Roll-forward:** Clean up the error from state or go to new state without errors

ใต้ **Fault Avoidance**:
- **Diagnosis:** Figure out the root cause of the error (fault)
- **Isolation/ Reconfiguration:** Isolate faulty component and reconfigure the system

(มุมขวาล่าง: เลขหน้า 41)

## Slide 49
หัวข้อ: **Dependability: / Attributes, Means and Impairments**

แผนภาพต้นไม้แบบเดียวกับ Slide 9/36:
- **Dependability** แตกแขนง 3 กิ่ง:
  - **ATTRIBUTES** → **AVAILABILITY**, **RELIABILITY**, **SAFETY**, **CONFIDENTIALITY**, **INTEGRITY**, **MAINTAINABILITY**
  - **MEANS** → **FAULT PREVENTION**, **FAULT TOLERANCE**, **FAULT REMOVAL**, **FAULT FORECASTING**
  - **IMPAIRMENTS** → **FAULTS**, **ERRORS**, **FAILURES**

ที่สำคัญ: บนสไลด์นี้มี **วงรีสีแดงหนา** ล้อมกรอบกลุ่ม **IMPAIRMENTS** และรายการย่อยทั้ง 3 ตัว (FAULTS, ERRORS, FAILURES)

(มุมขวาล่าง: เลขหน้า 49)

## Slide 51
หัวข้อ: **Dependability Impairments**

แผนภาพแกนเวลา (timeline) รูปแถบลูกศรสีฟ้าใหญ่ชี้ไปทางขวา:
- ด้านซ้ายมือมีรูปสายฟ้า (lightning bolt) สีส้ม/ส้มเหลือง (แทนเหตุการณ์รบกวน)
- บนแกนมีจุดสำคัญ 3 จุด (มีลูกศรสีฟ้าชี้ขึ้นจากป้ายด้านล่าง):
  - **Fault** (จุดเริ่ม ซ้ายสุด)
  - **Error** (จุดกลาง)
  - **Failure** (จุดท้าย ขวาสุด; มีรูปก้อนเมฆ/รูประเบิดสีแดงอยู่ปลายลูกศร)
- ระยะทางระหว่างจุด ระบุด้วยลูกศรสองหัว (double-headed arrow):
  - **Activation Latency** — จาก Fault ถึง Error
  - **Failure Latency** — จาก Error ถึง Failure

(มุมขวาล่าง: เลขหน้า 51)

## Slide 53
หัวข้อ: **Anatomy of an Error**

แผนภาพกราฟ 2 มิติ:
- แกนตั้ง: **Event** (มีลูกศรชี้ขึ้น)
- แกนนอน: **Time** (มีลูกศรชี้ขวา)

รายละเอียดเส้นทาง (เส้นสีน้ำเงินเข้ม):
- จุดเริ่ม: **Error Occurs !** (มีรูปดาวระเบิดสีแดง) บนเส้นระดับล่าง
- แยกเป็นสองเส้นทาง:
  1. เส้นบน – ไปยัง **Error Activated !** (มีรูปดาวระเบิดสีแดง) จากนั้นเส้นแยกขึ้นไปด้านบน:
     - ไปทางซ้าย: มีลูกศรระบุช่วง **Crash Latency** (ลูกศรสองหัว ระหว่างจุด Error Activated กับจุดบนเส้นที่ยกขึ้น)
     - เส้นบนสุดยาวไปทางขวา สิ้นสุดที่ปลายลูกศร พร้อมป้ายสีแดง **Incorrect Output !**
     - เส้นกลางยาวไปทางขวา สิ้นสุดที่ **Program Crash !** (รูปดาวระเบิดสีแดง ปลายลูกศร ป้ายสีแดง)
  2. เส้นล่าง – **Unactivated Error** ยาวไปทางขวา
- ปลายทางรวม: วงเล็บปีกกา (brace) สีเขียวรวบปลายเส้น **Benign Error** (ป้ายอยู่เหนือเส้นล่าง) และ **Unactivated Error** เข้าด้วยกัน ระบุเป็น **Success**

หมายเหตุป้ายกำกับ: "Error Occurs", "Error Activated", "Crash Latency", "Incorrect Output !", "Program Crash !", "Benign Error", "Unactivated Error", "Success"
(มุมขวาล่าง: เลขหน้า 53)

## Slide 54
หัวข้อ: **Inter-connected Systems**

ข้อความ bullet:
- One system's failure (system A) may be another one's fault/error (system B)

แผนภาพ: วงรีสีฟ้าใบใหญ่ (ภายในมีวงรีสีเขียวทึบซ้อนอยู่ด้านใน)
- ภายในวงรีสีเขียว: มีป้าย **Fault** (ตัวอักษรขาว) พร้อมลูกศรโค้งสีดำชี้ไปยังขอบเขตของวงรีเขียว ที่มีป้าย **Failure A**
- พื้นที่วงรีสีฟ้าด้านนอก (รอบวงเขียว):
  - ป้าย **Fault B** (เหนือขอบวงเขียว ด้านขวา)
  - เส้นกราฟหยึกสีดำ (zig-zag) เริ่มจากปลายลูกศร Failure A ทะลุออกมาในพื้นที่สีฟ้า แล้วพุ่งขึ้น–ลงเป็นรูปคลื่นหยึกไปทางขวา สิ้นสุดที่ปลายด้านขวาพร้อมป้าย **Failure B**

(มุมขวาล่าง: เลขหน้า 54)

## Slide 56
หัวข้อ: **Classification of Failures**

ตาราง (หัวตารางพื้นสีน้ำเงิน ตัวอักษรขาว):

| Criteria | Classification 1 | Classification 2 |
|---|---|---|
| **Nature** | Halt (fail-stop) | Erratic (Babbling) |
| **Detection** | Signaled | Un-signaled (fail silent) |
| **Consistency** | Consistent | Inconsistent |
| **Severity** | Minor | Catastrophic |

(มุมขวาล่าง: เลขหน้า 56)

## Slide 57
หัวข้อ: **Classification of Errors**

ตาราง (หัวตารางพื้นสีน้ำเงิน ตัวอักษรขาว):

| Criteria | Classification 1 | Classification 2 |
|---|---|---|
| **Domain** | Timing | Content |
| **Detection** | Detected | Latent |
| **Consistency** | Consistent | Inconsistent |
| **Severity** | Minor | Catastrophic |

(มุมขวาล่าง: เลขหน้า 57)

## Slide 58
หัวข้อ: **Dependability Threats**

แผนภาพลูกโซ่ Threat (แนวนอน จากซ้ายไปขวา, มีจุดไข่ปลา "…" สองข้าง):
- **… → Failure → Fault → Error → Failure → Fault → …**

ลูกศรเชื่อมระหว่างโหนด มีป้ายกำกับสีแดง:
- ระหว่าง Fault → Error: **Activation**
- ระหว่าง Error → Failure: **Propagation**
- ระหว่าง Failure (ตัวถัดไป) → Fault: **Causation**

เส้นเชื่อม (สีดำ) จากโหนดลงมาแสดงคำอธิบายย่อย:
- ใต้ **Failure** (ตัวแรก) → ข้อความ *Adjudged or hypothesized cause of an error* (ตัวเอียง) → ลูกศรลง → **Context dependent**
- ใต้ **Fault** → แตกเป็นสองสาขา:
  - **Internal fault** → ลูกศรลง → **Computation process**
  - **External fault** → ลูกศรลง → **Taking advantage of a *vulnerability*, i.e., an internal fault which enables the system to be harmed**
- ใต้ **Error** → **Part of system state that may cause a subsequent failure**
- ใต้ **Failure** (ตัวที่สอง) → *Deviation of the delivered service from correct service, i.e., implementing the system function* (ตัวเอียง สีน้ำเงิน) → แตกเป็นสองสาขา (ลูกศรสีแดง):
  - **System does not comply with the specification describing the system function**
  - **Specification does not adequately describe the system function**

(มุมขวาล่าง: เลขหน้า 58)

## Slide 59
ด้านบนเป็นแผนภาพลูกโซ่ (แนวนอน):
- **… Failures → Faults → Errors → Failures → Faults …**
- ลูกศรสีแดงเชื่อม พร้อมป้ายกำกับสีแดง:
  - Failures → Faults: **Causation**
  - Faults → Errors: **Activation**
  - Errors → Failures: **Propagation**
  - Failures → Faults (ตัวถัดไป): **Causation**

ด้านล่างเป็นแผนภาพต้นไม้ (เส้นสีแดง) แตกสาขา:
- **Domain** → **Content failures**, **Timing failures**
- **Consistency** → **Consistent failures**, **Inconsistent (Byzantine) failures**
- **Detectability** → **Signaled failures**, **Unsignaled failures**
- **Consequences** → **Minor failures** … (จุดสามจุดแนวตั้ง 3 จุด) … **Catastrophic failures**
- **Identification** → **Latent errors**, **Detected errors**
- **Extent** → **Single errors**, **Multiple related errors**

หมายเหตุ: โครงสร้างเชื่อมจากโหนด "Errors" ลงมา (เส้นยาวด้านซ้าย) แยกไปยังกลุ่ม Domain/Consistency/Detectability/Consequences และจากโหนด Failures ลงมาแยกไปยังกลุ่ม Identification/Extent
(มุมขวาล่าง: เลขหน้า 59)

## Slide 60
ด้านบนเป็นแผนภาพลูกโซ่ (แนวนอน):
- **… Failures → Faults → Errors → Failures → Faults …**
- ป้ายลูกศรสีแดง: **Causation** (Failures→Faults), **Activation** (Faults→Errors), **Propagation** (Errors→Failures), **Causation** (Failures→Faults)

ด้านซ้าย (ใต้ป้ายคำว่า **Origin** แนวตั้ง) แตกสาขา:
- **Phase of creation or occurrence** → **Development faults**, **Operational faults**
- **System boundaries** → **Internal faults**, **External faults**
- **Phenomenological cause** → **Natural faults**, **Human-made faults**
- **Intent** → **Malicious faults**, **Non-malicious faults**
- **Capability** → **Accidental faults**, **Deliberate faults**, **Incompetence faults**

ด้านขวา (ใต้ป้ายคำว่า **Manifestation** แนวตั้ง) แตกสาขา:
- **Style** → **Omission faults**, **Commission faults**
- **Persistence** → **Permanent faults**, **Transient faults**
- **Activation reproducibility** → **Solid faults**, **Elusive faults**
- **Dimension** → **Hardware faults**, **Software faults**, **System faults**
- **Plurality** → **Single faults**, **Multiple faults**
- **Correlation** → **Independent faults**, **Related faults**
- **Damage** → **Soft faults**, **Hard faults**
- **Status** → **Dormant faults**, **Active faults**

(มุมขวาล่าง: เลขหน้า 60)

## Slide 61
หัวข้อ (กึ่งกลางด้านบน): **Faults** / **— by origin —**  (เส้นคาดสีแดง)

แผนภาพต้นไม้ใหญ่ (เส้นสีแดง) แตกสาขา ดังนี้:

ระดับที่ 1: **Development** และ **Operational**

- **Development** → **Internal** → แตกเป็น:
  - **Human-made** → **Malicious** → **Delib.** → [กล่อง] **Malicious logic**
  - **Human-made** → **Non-malicious** → **Delib.** → และ **Delib.**/**Accid.**/**Incomp.** → [กล่อง] **Design Flaws** และ [กล่อง] **Production Defects**
  - **Natural** → **Non-malicious** → **Incomp.** → (ลู่ลงไปยัง Physical faults)
- **Operational** → **Internal** → **Natural** → **Non-malicious.** → **Accid.** → **Accidental** → [กล่อง] **Physical Deterior.**
- **Operational** → **External** → **Natural** → **Non-malicious.** → **Accidental** → [กล่อง] **Physical Interference**
- **Operational** → **External** → **Human-made** → **Non-malicious** → **Accid./Delib./Incomp.** → [กล่อง] **Input Mistakes**, [กล่อง] **Configuration and Reconfiguration Mistakes**, [กล่อง] **Overload**
- **Operational** → **External** → **Human-made** → **Malicious** → **Deliberate** → [กล่อง] **Intrusion Attempts**, [กล่อง] **Viruses Worms**

กล่องข้อความ (สี่เหลี่ยมขอบน้ำเงิน): **Malicious logic**, **Design Flaws**, **Production Defects**, **Physical Deterior.**, **Physical Interference**, **Input Mistakes**, **Configuration and Reconfiguration Mistakes**, **Overload**, **Intrusion Attempts**, **Viruses Worms**

ป้ายด้านซ้าย (สีเขียว มีเส้นคาดใต้): **Phase of creation or occurrence**, **System boundaries**, **Phenomenological cause**, **Intent**, **Capability**

ผลลัพธ์รวมด้านล่าง (ตัวหนาสีแดง หนาใหญ่) 3 กลุ่ม พร้อมลูกศรชี้ลง:
- **Development faults**
- **Physical faults**
- **Interaction faults**

(มุมขวาล่าง: เลขหน้า 61)

## Slide 62
แผนภาพต้นไม้ (เส้นดำ, กล่องสี่เหลี่ยมมีเงา lightbox):

โหนดราก (ซ้ายสุด): **Dependability and Security**
แตกเป็น 3 กิ่ง:
- **Attributes** → **Availability**, **Reliability**, **Safety**, **Confidentiality**, **Integrity**, **Maintainability**
- **Threats** → **Faults**, **Errors**, **Failures**
- **Means** → **Prevention**, **Tolerance**, **Removal**, **Forecasting**

(มุมขวาล่าง: เลขหน้า 62)

## Slide 64
หัวข้อ (สองบรรทัด): **Failure Sources & Frequencies for Computing Systems**

แผนภาพกล่องใหญ่แบ่งเป็นสองคอลัมน์:

**คอลัมน์ซ้าย — Non-fault-tolerant systems**
- (Japan, 1383 organizations [Watanabe 86]; USA, 450 companies [FIND/SVP 93])
- Mean Time To Failure: 6 to 12 weeks
- Average outage duration after failure: 1 to 4 hours
- Failure sources:
  - Hardware 50%
  - Software 25%
  - Communications-Environment 15%
  - Operations - Procedures 10%

**คอลัมน์ขวา — Fault-tolerant systems**
- (Tandem Computers [Gray 90]; Bell Northern Research [Cramp et al. 92])
- Mean Time To Failure: 21 years [Tandem]
- Failure sources:
  - Software 65%
  - Operations - Procedures 10%
  - Hardware 8%
  - Environment 7%

หมายเหตุ: เส้นแบ่งกลางกล่องเป็นเส้นดำหนา และมีเส้นคาด (divider) ระหว่างส่วนหัวข้อกับส่วนตัวเลข
(มุมขวาล่าง: เลขหน้า 64)

## Slide 65
หัวข้อ (สองบรรทัด): **User Outage in Non-Fault-Tolerant Client-Server Networks** *[Wood 94]*

แผนภาพกราฟแท่งซ้อน (stacked bar chart):
- แกนตั้ง (Y): **User outage (minutes for 1000 users)** ตั้งแต่ 0 ถึง 5 10⁶ (ป้ายสเกล: 0, 10⁶, 2 10⁶, 3 10⁶, 4 10⁶, 5 10⁶)
- แกนนอน (X): **Outage category** ประกอบด้วย: **Physical**, **Design**, **Opérations**, **Environ-ment**, **Configu-ration change**
- Legend (กล่องด้านขวาบน):
  - (พื้นเทาอ่อน) **Client**
  - (พื้นดำ) **Network**
  - (พื้นขาว) **Server**
  - (พื้นเทาเข้ม) **All**

ลักษณะแท่ง:
- **Physical** — แท่งเล็ก สูง ~10⁶ (มีส่วน Server สีขาว + All สีเทา + Network สีดำด้านบน)
- **Design** — แท่งสูงสุด สูง ~4.5×10⁶ (ส่วน Server สีขาวขนาดใหญ่ที่สุด + Client สีเทา + Network สีดำด้านบน)
- **Opérations** — แท่งกลาง สูง ~1.6×10⁶ (ส่วน Server สีขาว + Network สีดำด้านบน)
- **Environ-ment** — แท่งเล็กที่สุด สูงไม่ถึง 10⁶ (พื้นเทา)
- **Configu-ration change** — แท่งสูง ~3.8×10⁶ (ส่วน All สีเทาเข้ม + Server สีขาว + Network สีดำด้านบนเล็ก)

(มุมขวาล่าง: เลขหน้า 65)

## Slide 66
หัวข้อ (สองบรรทัด): **Primary Cause of Accident of Domestic Flights in US** *[Ruegger 90]*

ตาราง (กรอบดำ):
หัวตาราง: **Accidents per million takeoffs**
คอลัมน์ระยะเวลา: **1970-1978** และ **1979-1986**

| (Cause) | 1970-1978 | | 1979-1986 | |
|---|---|---|---|---|
| Technical defects | 1.49 | (45%) | 0.43 | (33%) |
| Weather | 0.82 | (25%) | 0.33 | (26%) |
| Human error | 1.03 | (30%) | 0.53 | (41%) |
| Total | 3.34 | | 1.29 | |

(มุมขวาล่าง: เลขหน้า 66)

## Slide 67
หัวข้อ (สองบรรทัด): **Results of Fault-Injection Experiments in Delta-4** *[Arlat et al.91]*

แผนภาพกล่อง (block diagram) อยู่ภายในกรอบสี่เหลี่ยม ประกอบด้วยกล่อง 4 กล่อง:
- **Faults** → (ลูกศร, ป้าย **94%**) → **Errors**
- **Errors** → (ลูกศร, ป้าย **85%**) → **Detected errors**
- **Detected errors** → (ลูกศร, ป้าย **99%**) → **Tolerated errors**
- **Errors** → (ลูกศรชี้ลง, ป้าย **3%**) → **Failures** (กล่องยาวด้านล่าง)
- **Detected errors** → (ลูกศรชี้ลง, ป้าย **1%**) → **Failures**
- มีเส้นโค้งจาก **Errors** ด้านบน ลากไปทางขวา พร้อมป้าย **12%** แล้วชี้ลงเข้าที่ **Tolerated errors**

(มุมขวาล่าง: เลขหน้า 67)

## Slide 69
หัวข้อ (สองบรรทัด): **Cost of Computer Failures in FRA as compared to the Revenue**

แผนภาพกราฟเส้นรวมในกล่องกรอบ (ประเทศฝรั่งเศส, ปี 1984–1993):
- แกนตั้ง (Y): **Billion FF (1993 FF)** มีค่าตั้งแต่ -6 ถึง 250 (สองสเกลรวมกันในภาพ; ค่าสเกลบน 100–250 และสเกลล่าง -6 ถึง 12)
- แกนนอน (X): ปี **1984, 1985, 1986, 1987, 1988, 1989, 1990, 1991, 1992, 1993** (มีเส้นประ grid ตามปี)

Legend (กล่องด้านล่างกราฟ):
- First 500 computer companies (construction, distribution, services) [Source: O1 Références]
  - (วงกลม ○) **Cumulative revenue, France**
  - (สี่เหลี่ยมข้าวหลามตัด ◇) **Net cumulative result**
- Computer failures [Source: APSAIRD/CLUSIF]:
  - (สี่เหลี่ยม □) **Total cost (private organizations)**
  - (กากบาท ×) **Cost allocated to accidental faults**
  - (สามเหลี่ยม △) **Cost allocated to malicious faults**

แนวโน้มเส้น (ตามที่อ่านได้):
- ○ Cumulative revenue, France — เพิ่มขึ้นจาก ~100 (1984) ไปจนถึง ~200-210 (1993) อยู่ช่วงบนของกราฟ
- □ Total cost — เพิ่มจาก ~7.5 ขึ้นไปสูงสุด ~10.5 (1991) แล้วลดลงเล็กน้อย
- × Cost allocated to accidental faults — คงที่ประมาณ 4-5 ตลอดช่วง
- △ Cost allocated to malicious faults — เริ่ม ~2.5 เพิ่มขึ้นเล็กน้อยแล้วทรงตัว
- ◇ Net cumulative result — เพิ่มจาก ~3 ขึ้นไป ~9 (1988) แล้วลดลงฮวบลงต่ำกว่า 0 (1992 ~ -5) แล้วดีดขึ้นเล็กน้อย (-3.5 ที่ 1993)

(มุมขวาล่าง: เลขหน้า 69)

## Slide 70
หัวข้อ: **FTC incidents in 2025** (ตัวอักษรใหญ่กึ่งกลาง)

ตาราง 3 คอลัมน์ หัวตาราง: **Incident (2025)** | **What Happened** | **Fault Tolerance Lesson**

| Incident (2025) | What Happened | Fault Tolerance Lesson |
|---|---|---|
| **Google Cloud Outage (June 12, 2025)** | A configuration change introduced a null-pointer crash loop in Google Service Control, causing failures across many Google Cloud services. The faulty configuration propagated globally within seconds. (The Economic Times) | Global replication without staged rollout created a **common-mode failure**. Better fault tolerance would include feature flags, canary deployments, and regional isolation. |
| **AWS DynamoDB/DNS Outage (October 20, 2025)** | A DNS-related failure in the US-East-1 region caused cascading failures across DynamoDB and many AWS services, affecting thousands of applications worldwide. (TechRadar) | Even highly redundant cloud systems can fail if a critical dependency becomes a single point of failure. Multi-region and multi-cloud architectures improve resilience. |
| **Microsoft Azure Front Door Outage (October 29, 2025)** | A configuration update prevented Azure Front Door nodes from loading correctly worldwide until Microsoft rolled back the change. (ThousandEyes) | Geographic redundancy cannot help when every region receives the same faulty configuration. Progressive rollouts and automated rollback mechanisms are essential. |
| **Slack Database Outage (February 26, 2025)** | A maintenance action overloaded database systems, causing messaging failures for several hours despite healthy network connectivity. (Network World) | Fault tolerance must cover backend databases as well as network infrastructure. Monitoring should detect application-layer failures, not just network health. |
| **Asana Consecutive Outages (February 5–6, 2025)** | Two configuration-related incidents caused service disruptions after server logs overwhelmed systems. Afterward, Asana adopted staged configuration rollouts. (ThousandEyes) | Small configuration errors can cascade. Canary deployments and gradual rollouts are effective fault-tolerance practices. |
| **Cloudflare Outage (November 18, 2025)** | A latent software bug triggered by a routine configuration change caused widespread degradation affecting numerous Internet services. (CIO) | Hidden software defects can bypass redundant infrastructure. Extensive testing and automatic rollback reduce the impact. |
| **Equinix Singapore Data Center Outage (May 31, 2025)** | Maintenance temporarily reduced redundancy, and an equipment fault caused two data halls to go offline. (Data Center Frontier) | Maintenance windows can weaken fault tolerance. Critical infrastructure should preserve sufficient redundancy during planned work. |

หมายเหตุ: ชื่อแหล่งอ้างอิงในวงเล็บ (The Economic Times, TechRadar, ThousandEyes, Network World, CIO, Data Center Frontier) เป็นข้อความขีดเส้นใต้สีน้ำเงิน (hyperlink)
(มุมขวาล่าง: เลขหน้า 70)

# FTC02 — Transcript Insights (Fault Tolerant Systems / Reliability)

> สรุปเนื้อหาที่ "อาจารย์พูดอธิบายด้วยปาก" เพิ่มเติมจากสไลด์ (intuition, การคิด/คำนวณ, ตัวอย่าง, จุดเน้น, การบ้าน) — ไม่ใช่การลอก bullet ในสไลด์
> [ไม่แน่ใจ: ...] = ช่วงเสียง garbled หรือตีความไม่ได้ชัด

---

## 1. ภาพรวม / นิยาม Fault Tolerance

- อาจารย์เริ่มด้วยการ "พูดซ้ำ" นิยาม: **Fault Tolerance = ความสามารถของระบบที่จะ continue การทำงาน (operation) ให้เป็นลักษณะ error-free แม้ว่าจะมี fault เกิดขึ้นก็ตาม** — คือเป็นระบบที่ยอมให้มี fault เกิดขึ้นได้ แต่ตัว error นั้นไม่ส่งผลกระทบต่อ operation
- เน้นว่าเป็นระบบที่ยอมให้ fault เกิดขึ้น (ไม่ได้พยายามให้ fault เป็นศูนย์) แต่ทำให้ fault ไม่มีผลต่อการทำงาน
- ใช้ในระบบที่ต้องการ **reliability สูง** เช่น ระบบการแพทย์ การบิน และระบบการเงิน
- ประเด็นที่他强调: ทุกระบบมี **ความเสี่ยง (risk)** ที่จะเกิด fault อยู่ ซึ่งเรารู้ล่วงหน้าได้บ้าง แต่ก็ **มีข้อจำกัดในการรู้ล่วงหน้า** — บางครั้งเรายอมรับว่าเราไม่สามารถทำให้ perfect ได้ แต่พยายามทำให้ **fault ที่เกิดขึ้นมีผลกระทบต่อระบบน้อยที่สุด** / ทำให้ระบบมีความยืดหยุ่นรองรับตรงนั้น
- **ไม่มีระบบไหนที่ Free From Failure ได้** — ระบบอาจมี failure ได้
- Fault tolerance ถือเป็น **Non-Functional Requirement** ที่ระบบทั่วไปควรมี
- **Fault tolerance ที่ดี = ระบบที่ user หรือ admin ต้องเข้าไป involve น้อยที่สุด** แต่ยังคงทนทานต่อ fault ได้
- ระบบปัจจุบันส่วนใหญ่ไม่ได้เป็นเครื่องเดี่ยว แต่เป็น **Distributed System** (เช่น cloud) จึงต้องดูแลให้ทนทานด้วย

## 2. มุมมอง Fault / Error / Failure และ Attribute

- มองระบบเป็น **สามมิติ / สามมุม**: fault → error → failure (triad)
- ลำดับการวิเคราะห์ที่他强调:
  1. ดูว่าใน **Attributes** มีอะไรเป็นสาเหตุที่ทำให้เกิด Fault, Error หรือ Failure
  2. เมื่อรู้ว่า attribute ใดและ **consequence** อยู่ที่ใดแล้ว
  3. จึงกำหนด **Set Strategy** ว่าจะ handle fault นั้นอย่างไร
- มีหลายวิธี (strategy) ในการ handle fault แต่ละวิธีต่างกันที่ **ระดับของผลกระทบ** ว่ากระทบต่อภายนอกหรือไม่ และ **ประเภท** ของมัน
- มุมมอง **เวลา (temporal)**: fault เกิดขึ้นในช่วงเวลาใด อย่าง **transient** (ชั่วคราว, บางครั้งบางคราว) กับ **permanent**
- ระบุว่ามุมมอง Attribute โดยเฉพาะที่มองแบบ (distributed system) จะแยก classify ประเภทและจำแนกตาม failure ได้

## 3. การจำแนก Failure ของ Distributed System

อาจารย์ยกตัวอย่าง **Failure ของ Distributed System**:
- **Crash Failure** — server มีปัญหา พัง ทำงานไม่ได้
- **Omission Failure** — รับส่งข้อมูลไม่ได้ เช่น รับ request ไม่ได้ หรือส่ง message ไม่ได้ (ฝั่ง send/receive)
- **Timing Failure** — ทำงานผิดเรื่องเวลา
- บอกว่าพวกนี้จัดอยู่ใน failure ของ distributed system

> หมายเหตุ: อาจารย์ดูลิสต์นี้ในสไลด์แล้วอธิบายด้วยปากสั้น ๆ (ควรดูสไลด์ประกอบ)

## 4. Failure Rate และหน่วย FIT

- เรื่อง **failure rate (λ)** — อาจารย์บอกว่าตอนนั้น λ ในสไลด์ไม่แสดง (ปัญหาการแสดงผลจอ)
- หน่วยที่ใช้กันคือ **FIT (Failures In Time)**
  - หลักการ: **FIT ยิ่งน้อยยิ่งดี** (อาจารย์พูดสลับ/แก้ตัวเองกลางประโยค — สรุปคือค่าน้อย = ดี)
- ตัวเลขอ้างอิงที่อาจารย์ให้:
  - **ชีวิตคนเฉลี่ย ~85 ปี ≈ 1,300 กว่าฟิต** (ในเชิงการเปรียบเทียบอัตราการล้มเหลว)
  - **คอมพิวเตอร์อยู่ในระดับ "ร้อย" FIT**
  - [ไม่แน่ใจ: ตัวเลขและทิศทางที่อาจารย์พูดสลับเล็กน้อย ช่วง [00:07:40]–[00:08:48]]

## 5. Reliability Modeling และ Reliability Block Diagram

- **Reliability model** สร้างขึ้นจากระบบจริง: เอาแต่ละ component ในระบบมาต่อกันตาม **Physical Model** ของระบบ แล้วดู reliability ของแต่ละตัว
- ตัวอย่างที่อาจารย์เล่า (ระบบจริง → model):
  - **ตัวอย่างน้ำส้มข้น**: มี **ปั๊ม (pump)** สูบน้ำ แล้วผ่าน **ฟิลเตอร์ (filter)** เพื่อกรอง/คัด จากซ้ายไปขวา มี process 2 อัน (pump, filter) ต่อกัน → เป็น **Series** reliability = ผลคูณของทั้งคู่
  - **ตัวอย่าง Conveyor**: มีเส้นทางสายพานลำเลียง และมีระบบที่ทำ process กับเส้นนั้น — มี 2 ตัวที่ **ทำงานเหมือนกัน** ใส่ไป 2 ตัวเพื่อ **ป้องกัน** (ถ้าตัวหนึ่งไม่ทำงาน อีกตัวยังทำได้) → เป็น **Parallel redundancy**
- **Reliability Block Diagram** มีวิธีต่อพื้นฐาน **แค่ 2 แบบเท่านั้น**:
  - **Series** (รูปทางซ้าย) — สัญญาณต้องผ่าน component ทั้งหมด (ตัวอย่างมี 4 ตัว) ถือว่าสำเร็จเมื่อผ่านครบ
  - **Parallel** (รูปทางขวา) — ทำงานขนานกัน **at least one** ตัวที่ทำงานได้ก็ถือว่า system working
  - ผสมกันได้ (series-parallel ผสม)

### Minimal Path Set
- **Minimal Path Set** ("นิมัล" ในเสียง) = subset ของ component ที่ทำให้ระบบ **operation จากซ้ายไปขวาได้** (path ที่สั้นสุด)
- จากตัวอย่าง (ซ้าย→ขวา) อาจารย์ไล่ได้เส้นทางประมาณ 4 เส้น เช่น ผ่าน 1→2, 1→3→5, 4→3→5(?), 4→5 — และบอกว่า path 1,3,2 ไม่นับเพราะ 1→2 ไปได้อยู่แล้ว (จึงถูกตัดออก)
- [ไม่แน่ใจ: เลข node ของแต่ละ path — ระบบฟังไม่ชัด ช่วง [00:16:45]–[00:19:44]]

### Minimal Cut Set
- **Minimal Cut Set** = เซตของ component ที่ถ้า fail แล้วจะทำให้ **ระบบ operation จากซ้ายไปขวาไม่ได้**
- ตัวอย่างเส้นที่ตัดของระบบเดิม: {1,4}, {1,3,5}, {2,4}, {2,5} [ไม่แน่ใจ: เลข node จากการฟัง]
- จาก cut set สามารถสร้าง **Equivalent block diagram** (รูปขวามือ) ได้เช่นเดียวกับ path set

## 6. การคำนวณ Reliability (จุดที่อาจารย์เน้นวิธีคิด)

- สมมติมี component **k ตัว** → reliability ของระบบขึ้นกับ **เวลา** ที่ component working (โอกาส/probability ที่จะ working ได้)
- ใช้ **Failure Rate** มาทำเป็น **Exponential Failure Law**
  - สมมติฐาน: failure rate เป็น **ค่าคงที่ (Constant Failure Rate, CFR)**
  - ถ้า failure rate **ไม่ constant** จะได้การแจกแจงอีกแบบที่ซับซ้อนกว่า (แต่โดยทั่วไปสมมติ CFR)

### Series System
- reliability ของระบบ = **ผลคูณ** ของ reliability แต่ละ component (เช่น ABC ต่อ CD: R_sys = R_A·R_B·R_C·R_D)
- **วิธีทำให้ reliability ดีขึ้น** (จากสมการ) — อาจารย์列举:
  1. **ลดค่า failure rate** ของแต่ละตัว (ทำให้โอกาส fail น้อยลง)
  2. **ลดจำนวน component** ให้น้อยลง
  3. **ลดช่วงเวลา (mission time)** ที่กำหนด — เวลาน้อยลง โอกาสได้ reliability สูงได้
  4. **ทำ redundancy** (ดูด้านล่าง)

### Redundancy (Parallel)
- อาศัยหลัก **parallel system**: มี n ตัว run ขนานกัน ถ้า **ตัวใดตัวหนึ่ง process ได้** ถือว่า operation ผ่าน → ทำให้โอกาสสำเร็จสูงขึ้น
- ตัวอย่างการคิด: เอา B สองตัวขนานกัน
  - reliability ส่วนขนาน = 1 − (1 − R_B)²
  - **เหตุผล**: ส่วนนี้จะ fail ก็ต่อเมื่อ **B ทั้งคู่ fail พร้อมกัน** → P(B fail) = 1 − R_B, สองตัว = (1 − R_B)²
  - อาจารย์เน้นที่มาของเทอมนี้ (ไม่ใช่ท่องสูตร)
- ระบบรวมถ้าเป็น series → ผลคูณ; ถ้าเป็น parallel → ตัวใดตัวหนึ่งทำงานได้ถือว่าใช้ได้

### Reliability = Probability (CDF / PDF)
- Reliability มองคล้าย ๆ เป็นค่า probability
- สองมุมมองการแจกแจง:
  - **CDF (Cumulative Distribution Function)** = พื้นที่สะสมจาก 0 ถึง x → มองเป็น probability ที่เหตุการณ์เกิดขึ้น (สะสมตรง ๆ)
  - **PDF (Probability Density Function)** = **shape** ของ distribution ว่าเป็นแบบใด (เช่น uniform) → CDF คือพื้นที่ใต้ PDF
- Reliability มีความสัมพันธ์กับ **MTTF** และอยู่ในช่วงเวลา 0 ถึง t (ช่วงที่รับประกันว่าทำงานได้)

### MTTF จาก Exponential Law
- เมื่อใช้ exponential failure law และ integrate reliability จาก 0 ถึง ∞ จะได้ **MTTF = 1/λ**
- อาจารย์เน้น: **พอรู้ failure rate (λ) ก็รู้ MTTF ได้เลย** (เป็นค่ากลับกัน) ภายใต้ CFR

## 7. เปรียบเทียบระบบสองแบบกับ Mission Time (จุดที่อาจารย์ย้ำ)

- เอา 2 ระบบ R1 กับ R2 มา compare
  - **difference** = ค่าต่าง, **ratio** = สัดส่วน, และ **improvement factor**
- การอ่านกราฟ/เปรียบเทียบ:
  - **ช่วงระยะแรก (สั้น) R2 สูงกว่า (ดีกว่า)**
  - **ในช่วงระยะยาว R1 กลับดีกว่า R2**
- **ข้อสรุปสำคัญที่他强调**: R1 หรือ R2 จะ reliable กว่ากัน **ขึ้นกับ Mission Time**
  - ถ้า **mission ยาว** → อาจเลือก **R1**
  - ถ้า **mission สั้น** → ออกแบบ/เลือก **R2** (ให้ reliability ดีในช่วง mission ที่กำหนด)
  - ดังนั้นการเลือกขึ้นกับ **ระยะเวลาของ mission** ที่เราจะทำ

## 8. Repair / Maintainability / Availability

- หลังเกิด failure แล้ว **repair** อย่างไร → เกี่ยวกับ **Maintainability** และ **MTTR (Mean Time To Repair)**
- **Repair rate (μ)** = ค่าที่เป็น reciprocal ของ MTTR (คือ 1/MTTR)
  - [ไม่แน่ใจ: อาจารย์พูดสลับเป็น "reciprocal ของ failure rate" กลางประโยค แต่ใจความคือ μ = 1/MTTR — ช่วง [00:35:42]–[00:37:09]]
- **Availability = MTTF / (MTTF + MTTR)**
  - เพราะมีช่วงที่ operate ได้เทียบกับเวลารวม (operate + repair)
- **System availability** รวมจาก component ได้คล้าย reliability: series → ผลคูณ, parallel → คิดแบบเดียวกัน

### ตัวอย่าง: Dual Node / Single Spare
- node ต่อกับ network 2 node โดยตัวหนึ่งเป็น **spare**
- กำหนด node available = 0.99 → โอกาส down = 0.01
- ระบบจะ down ก็ต่อเมื่อ **node ทั้งสอง down พร้อมกัน** = 0.01 × 0.01 = 0.0001
- ดังนั้น availability = **0.9999** (มี spare 1 ตัวทำให้โอกาส down น้อยลงมาก)

### ตัวอย่าง: Multiple Nodes / Single Spare และ Multiple Spares
- กรณี node หลายตัวในระบบ: ระบบ down เมื่อ **down 2 node** (ตามสมการที่เขียน)
  - นับ **จำนวน combination** เช่น "ดูทุก combination 2 ใน 5" = C(5,2) = 10 pattern แล้วใช้ 1 − ... คำนวณ
  - ได้ผลประมาณ **0.9999** (ตัวเลข 0.01 ยกกำลังสอง)
  - [ไม่แน่ใจ: รายละเอียดสมการ/ตัวเลข — ช่วง [00:42:24]–[00:44:18]]
- กรณี **Multiple Nodes / Multiple Spares**: ตัวอย่าง **6 nodes, 2 spares, ต้องการ 4 node ทำงาน** → นับจำนวน ways ที่ node ทำงานมากกว่าที่ต้องการ
  - [ไม่แน่ใจ: ตัวเลข "20 ways" และผลลัพธ์ท้าย — เสียงไม่ชัด ช่วง [00:45:26]–[00:46:33]]

### Availability vs (MTBF/MTTR) — จุดที่อาจารย์พูดหลายรอบ
- มีความสัมพันธ์ระหว่าง **MTBF** กับ **availability** (และความสัมพันธ์นี้ไม่ได้ขึ้นกับตัวเดียว)
- **แนวคิดที่他强调 (พูดหลายรอบ)**:
  - ระบบ/component บางตัว **อาจ down บ่อย (MTBF สั้น)** แต่ **ซ่อมเร็ว** → availability อาจยังดีอยู่ได้
  - ตรงกันข้าม ตัวที่ down นาน ๆ ครั้ง แต **ซ่อมนาน** → availability แย่ลง
- **ความแตกต่างเชิงมุมมอง**: ในมุม **reliability** การที่ระบบ down แล้วฟื้นเร็วไม่เหมือนกันกับตัวที่ down บ่อย — "ดาวน์เร็ว ≠ ฟื้นเร็ว" จึงต้องแยกดู ทั้ง reliability และ availability
  - [ไม่แน่ใจ: ประโยคสรุปช่วง [00:47:51]–[00:49:02] เสียงกลืน]

## 9. ตัวอย่าง TMR (อาจารย์ให้ลองทำในห้อง)

- ระบบ **TMR** ที่มี **U1, U2, U3 + Voter**
  - U1,U2,U3 ประมวลผล ถ้า U1 = yes, U2 = yes, U3 = no → Voter เลือก **yes** ออกไป (majority vote)
  - ถ้า U1 กับ U2 ทำงานถูกต้อง ส่วน U3 เกิด fail → ระบบยังทำงานถูกต้อง
- **คำถาม**: reliability ของ TMR = เท่าไร?
- วิธีคิดที่อาจารย์นำ: reliability ของ TMR = ผลรวมของกรณีที่ระบบยัง out ถูกต้อง
  1. ทั้งสามตัวถูกต้องทั้งหมด → **R_U³**
  2. **2 ใน 3 ถูกต้อง** → มี **3 patterns** (U1 ปกติ, U2 ปกติ, หรือ U3 ปกติ) → 3·R_U²·(1−R_U)
  - กรณี 1 ใน 3 ถูกต้อง → **ไม่มีผล/ไม่นับ** เพราะ Voter จะเลือกผลผิดออก
- ผลรวมเป็นสมการ reliability ของ TMR
- **อาจารย์บอกว่า "เฉลยไม่อยู่ในสไลด์" และจะจัดส่ง/แจกใหม่ให้** — [จุดนี้ควรจดสมการตอน他终于แจก]

## 10. ตัวอย่าง RPS vs RSP (Reliability Block Diagram)

- โจทย์: มี **RPS** (Parallel-Series?) กับ **RSP** — หา reliability ของทั้งสอง แล้ววิเคราะห์ว่าอันไหน reliable กว่ากัน
- ขั้นตอนที่อาจารย์ทำให้ดู: เอา 2 ตัวในแนวนั้นคูณกันก่อน แล้วค่อยรวม
  - ตัวอย่างแนวคิด: P-S scheme ได้พจน์ประมาณ 1 − (1−R_A·R_B)·(1−R_C·R_D) แทนค่า R เท่ากันได้ **2R² − R⁴**
  - [ไม่แน่ใจ: รายละเอียดพีชคณิตของ RPS/RSP — ช่วง [00:58:10]–[01:02:06]]
- **ผลลัพธ์: RPS > RSP** (RPS reliable มากกว่า)
- **เหตุผลที่อาจารย์ให้ (สำคัญ)**: ดูจาก **minimum path set**
  - ฝั่ง RPS มี **เส้นทาง (path) มากกว่า** ฝั่ง RSP
  - ฝั่ง RSP มีจุดที่ถ้า fail แล้วระบบ operate ไม่ได้เลย
  - ดังนั้น RPS จึงทนกว่า/ดีกว่า
- หมายเหตุ: อาจารย์บอกว่าโจทย์แบบนี้คือ **การบ้าน** (ดูหัวข้อ 12)

## 11. การออกแบบตาม Mission (Dependable Computing)

- หลังคำนวณแล้ว แนวทางออกแบบ fault tolerance ให้ **match กับ mission** จะต่างกันไปตามภารกิจ:

### Long Life System
- เช่น **Spacecraft** ที่เป็น mission หลายปี ไปยัง location ที่ **เข้าถึงยาก**
- ให้ความสำคัญกับ **อายุการใช้งานยาวนานที่สุด (long life)** เป็นหลัก — อาจยอมให้ "เสียช้าหน่อย"
- เทคนิคที่เกี่ยว: redundancy, การ monitor, coding ต่าง ๆ

### Safety-Critical
- เช่น **การบิน, ระบบการแพทย์** — ต้องทำให้ **ไม่เกิด failure** และ outputs ถูกต้อง
- ใช้หลัก **masking**, การ **voting**, และ redundancy ช่วย

### Availability-Centric (ระบบชีวิตประจำวัน)
- ต้องการ **availability เป็นหลัก** ให้เป็น **non-stop**
- อาจตามมาด้วย **security**, ทำ hardware เสริม, ทำ **recovery** เมื่อเสียแล้วกู้คืนได้

### เทคนิคหลัก 4 อย่าง (Fault Tolerance Techniques)
อาจารย์列举หลัก ๆ 4 ตัว:
1. **Fault Avoidance** — ป้องกันไม่ให้เกิด fault
2. **Fault Removal** — หา fault ให้เจอ และกำจัดก่อน service
3. **Fault Detection** — ยอมให้มี fault แต่ **detect** ได้
4. **Fault Tolerance** — ยอมให้มี fault และระบบ **ทนต่อ fault** นั้นได้

### ประเภทของ Redundancy
- **Hardware Redundancy** — ใช้หลายตัว เช่น dual, voting
- **Information Redundancy** — เพิ่มข้อมูล/สัญญาณเข้าไปใน data (มี coding theory / information theory, การใส่ code) เพื่อสร้าง redundancy
- **Temporal Redundancy** — ทำซ้ำ (Repeat Calculation) แล้ว **compare results**
  - ป้องกัน **transient fault** (fault ชั่วคราว) ได้ แต่ **ไม่ช่วยกับ permanent fault**

### Architecture
- ถ้าไม่มี fault tolerance เลย = ระบบทั่วไป (single/basic)
- เพิ่ม component ที่เหมือนกัน → **Dual System** (= 2x), มากกว่า 2 = **N-way**
- ตัวอย่าง **RAID**: level 1 = mirroring, level 2/3 = ใช้ **ECC / coding** — แต่ละ level ให้ redundancy ต่างกัน

### ตัวอย่าง Space Shuttle
- ใช้คอมพิวเตอร์ประมวลผลหลัก **5 เครื่อง** ทำเป็น **MMR Configuration** (มี 4 เครื่องทำงานแบบ MMR ก่อน) — ถ้าเสียไป 1 เครื่อง จะเปลี่ยน configuration ไปเป็น **TMR**
- task ที่ไม่ critical จะย้ายไปรันระบบอื่น
- มี **self-test** และส่วนอื่น ๆ เสริม

### Software Fault Tolerance
- software มี **bug** → ต้องการ **software fault tolerance**
- ตัวอย่างวิธี: **N-Version Programming** — **spec เดียวกัน แต่ implement ต่างกัน** (code คนละแบบ, คนละภาษาได้) แล้ว **compare** ผลว่าทำงานถูกต้องหรือไม่

## 12. การบ้าน & สิ่งที่ต้องส่ง/ทบทวน

- **การบ้านชุดที่ 1**: เป็น **โจทย์คำนวณ reliability** แบบเดียวกับตัวอย่างในห้อง (RPS/RSP, series/parallel, TMR)
  - [ไม่แน่ใจ: ประโยค "การบ้านผมก็เป็นการบ้านการคำนวณแบบนี้" — เสียง garbled ช่วง [01:02:06]–[01:03:59]]
- **การบ้านครั้งที่ 2 (เปลี่ยนชุดใหม่)** — อาจารย์แจ้งตอนท้ายคาบ:
  - โจทย์รูป **ABC** ที่ **ซับซ้อนกว่าตัวอย่างเดิมเล็กน้อย** ต่อกันแบบ series ที่ไม่เหมือนกันเท่าไร
  - มี **PP Scheme** กับ **AP Scheme** สองตัว
  - **คำถาม**: ให้ **เขียน reliability expression** ของทั้ง PP และ AP ออกมา แล้วดูว่า **ระบบ PP หรือ AP ที่ reliable มากกว่า**
  - ให้ **ส่งงาน (submit)**
- **เฉลย TMR**: อาจารย์บอกว่าเฉลยไม่อยู่ในสไลด์ **จะส่ง/แจกใหม่ให้**
- **สไลด์/lecture note**: อาจารย์จะ **convert PowerPoint เป็น PDF** แล้วอัปโหลดให้ใหม่ (บอกว่าตอนนั้นทำ PDF ในเครื่องลำบาก จะทำให้ตอนเย็น)
- วันนี้ **ไม่มีคำถาม** → กลับบ้านได้

## 13. เรื่องอื่น ๆ

- ช่วงต้นคาบมีปัญหาเรื่อง **เสียง/จอ/การแชร์หน้าจอ** ทำให้สไลด์บางช่วงไม่ขึ้น (λ และกราฟไม่แสดง) — อาจารย์พูดแก้สถานการณ์เป็นระยะ
- อาจารย์มีหายเบรก ~10 นาที กลางคาบ (ช่วงคำนวณ RPS/RSP)

---

## สรุปสิ่งที่อาจารย์ "ย้ำเป็นพิเศษ" (สำหรับทบทวน/เตรียมสอบ)
- Fault tolerance = ยอมให้มี fault แต่ operation ต้อง error-free; เป็น **Non-Functional Requirement**; ที่ดีคือ user/admin ยุ่งน้อย
- ต้องแยกให้ออก: **Fault vs Error vs Failure**, **Transient vs Permanent**, **Crash / Omission / Timing failure**
- **Series = ผลคูณ**, **Parallel = at-least-one (1 − ผลคูณของความน่าจะเป็น fail)**
- **MTTF = 1/λ** (ภายใต้ CFR) และ **Availability = MTTF/(MTTF+MTTR)**
- **R1/R2 ดีกว่ากันขึ้นกับ Mission Time** (สั้น vs ยาว)
- **Minimum Path Set / Minimum Cut Set** ใช้ตัดสินว่าระบบไหนดีกว่า (path มากกว่า = ทนกว่า)
- เทคนิค: **Avoidance / Removal / Detection / Tolerance**; Redundancy: **Hardware / Information / Temporal**
- ออกแบบตาม mission: **Long Life / Safety / Availability**
- **การบ้าน 2 ชุด** เป็นการคำนวณ reliability (RPS/RSP, TMR, PP/AP scheme) — ควรฝึกคำนวณเอง

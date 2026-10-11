# บทที่ 2 — FTC02 Fault Tolerant Systems (ฉบับย่อ)

## ภาพรวมและคำศัพท์

บทนี้เป็นด้านปริมาณของวิชา **Fault** = defect ภายในระบบ **Error** = การเบี่ยงเบนจากพฤติกรรมที่คาดหมาย **Failure** = ระบบทำตาม specification ไม่ได้ **Fault tolerance** = ให้บริการได้แม้มี error เป็น **non-functional/QoS requirement** และที่ดีคือผู้ใช้/ผู้ดูแลต้องยุ่งน้อยที่สุด ระบบกระจายทนกว่า centralized แต่ยิ่งมี host มาก fault ก็ยิ่งบ่อย

สไลด์ overview วางสามกล่องคือ Attributes (What is a dependable system?), Consequences: fault/error/failure (How to distinguish faults?), Strategies (How to handle faults?)

**Failure ของระบบกระจาย (จำตารางนี้):** Crash failure (server หยุด แต่ทำงานถูกจนกระทั่งหยุด — มี Amnesia/Pause/Halting crash), Omission failure (รับ/ส่งข้อมูลไม่ได้ — Receive/Send omission), Timing failure (ตอบนอกช่วงเวลา), Response failure (Value failure / State transition failure), Arbitrary failure (ตอบอะไรก็ได้ = Byzantine)

## Failure rate และ bathtub curve

**failure rate** λ วัดเป็น **FITS** (1 FIT = 1 failure ต่อ 10^9 ชั่วโมง): NASA ≈ 1 FIT, คอมพิวเตอร์ 10^5–10^6 FITs, ชีวิตมนุษย์ 85 ปี ≈ 1,343 FITs **bathtub curve** 3 ช่วง: infant mortality (สูงแล้วลด), working life (เกือบคงที่ random failure), wearout (สูงขึ้น) ช่วงกลางที่คงที่คือเหตุผลของ exponential law (ซอฟต์แวร์มี bathtub ต่างออกไป และมี spike ทุกครั้งที่ upgrade)

## Reliability, MTTF, availability

**Reliability** R(t) = ถ้าทำงานที่ t=0 แล้วความน่าจะเป็นที่ยังทำงานที่ t **Exponential law:** R(t) = e^(−λt) **MTTF = ∫R(t)dt = 1/λ** (τ คงที่) ทำให้ reliable ขึ้นได้โดยลด λ, ลดจำนวน component, ลดเวลา t หรือเพิ่ม redundancy

**repair rate** μ, maintainability M(t) = 1 − e^(−μt), **MTTR = 1/μ**, **Availability = MTTF/(MTTF+MTTR)** ระบบโทรศัพท์ต้อง 4 nines, high-reliability 7 nines ขึ้นไป

**Reliability กับ availability:** availability = เปอร์เซ็นต์เวลาที่ operable; reliability = นานแค่ไหนที่ทำหน้าที่ได้ ตัวอย่าง down 6 นาทีทุกชั่วโมง = availability 90% แต่ reliability < 1 ชั่วโมง สรุป: เครื่อง reliable มี availability สูง แต่เครื่องที่ available อาจ reliable หรือไม่ก็ได้ ความสัมพันธ์กับ maintainability: ซ่อมเร็วขึ้น → availability สูงขึ้น

## Series และ parallel

**Series** (ต้องทำงานครบทุกตัว): **R = ∏Rᵢ**, availability A = AₓAᵧ
**Parallel** (อย่างน้อยหนึ่งตัว): **R = 1 − ∏(1−Rᵢ)**, availability A = 1 − (1−Aₓ)²

ตัวอย่าง availability: ชิ้น X มี 2 nines รวม Y 4 nines แบบ series ได้ 98.99% (ต่ำลง) แต่สองชิ้นขนานกันได้ 4 nines, สามชิ้นขนานได้ 6 nines ⚠ series = AND ของการอยู่รอด, parallel = OR (ไม่เหมือน schematic)

## Minimal path set และ cut set

**MPS** = เซตย่อยที่ถ้าทำงานครบแล้วรับประกันว่าระบบทำงาน **MCS** = เซตย่อยที่ถ้าพังครบแล้วรับประกันว่าระบบพัง สำหรับบริดจ์ 5 กล่อง MPS = {1,2}, {1,3,5}, {4,3,2}, {4,5} และ MCS = {1,4}, {2,5}, {1,3,5}, {2,3,4} (ใช้ inclusion-exclusion หรือลดเป็น series-parallel)

## ระบบมี spare

n node, node availability a, spare s: จำนวนโหมดความล้มเหลว **f = C(n, s+1)** และ **A = 1 − f·(1−a)^(s+1)**
- Dual node single spare: f = C(2,2) = 1, a = 0.99 → A = **0.9999** (4 nines)
- Five nodes single spare: f = C(5,2) = 10 → A = **0.999** (3 nines) — เพิ่ม node โดย spare เท่าเดิม *ลด* availability
- Six nodes two spares: f = C(6,3) = 20 → A = **0.99998**

## TMR

**R_tmr = (3R_m² − 2R_m³)·R_V** โดยวงเล็บคือความน่าจะเป็นที่มีอย่างน้อย 2 ใน 3 unit ทำงาน
- **Voter สมบูรณ์แบบ:** TMR ชนะ simplex เมื่อ **R_m > 1/2**; MTTF = **5/(6λ)** (ต่ำกว่า simplex 1/λ) — TMR reliable กว่าที่ mission สั้น (เส้นตัดกันที่ λt = ln 2)
- **Voter ไม่สมบูรณ์แบบ:** R = R_V(3R_m² − 2R_m³); เงื่อนไข **R_V > 1/(3R_m − 2R_m²)** และ R_m ต้องอยู่ในช่วง; ตัวอย่าง R_V = 0.95 → **0.56 < R_m < 0.94** (ต่ำสุดของ R_V ที่ยอมรับได้ ~0.885) module ที่ reliable สูงเกินไปทำให้ TMR แย่ลง
- **Compensating faults:** R = (3R_m² − 2R_m³) + **6p0p1R_m** (module หนึ่งพังไปทาง 0 อีกอันไปทาง 1 แล้วตัวที่สามยังถือเสียงข้างมาก)

## PS กับ SP

**PS** = replicate แต่ละ stage ก่อน แล้วต่อ series: R_PS = [1−(1−R)²]² = **R⁴ − 4R³ + 4R²**
**SP** = ต่อ series ก่อน แล้ว replicate: R_SP = 1−(1−R²)² = **2R² − R⁴**
ผลคือ **R_PS > R_SP** เสมอ (0<R<1) เพราะ PS มีเส้นทางมากกว่า

## Network ที่ไม่ใช่ series-parallel

ใช้ **keystone conditioning:** **R_sys = P(works | m ทำงาน)·R_m + P(works | m พัง)·(1−R_m)** วลีช่วยจำ: **"module works = path shorted"** และ **"module fails = path opened"** เลือก m ให้เมื่อ fix แล้ว network กลายเป็น series-parallel (เลือกตัวที่อยู่บนหลาย path มากสุด)

**บริดจ์ 6 โมดูล (FTC07):** R_sys = [1−(1−R_AR_B)(1−R_F)]R_CR_D(1−R_E) + [1−(1−R_A)(1−R_FR_C)]R_D R_E; เมื่อทุกตัว = R → **R_sys = R⁶ − 3R⁵ + R⁴ + 2R³** ถ้าเลือก A เป็น keystone จะง่ายสุด

## Redundancy และสถาปัตยกรรม

**Hardware** (ทำสำเนา+เปรียบเทียบ; ตรวจ permanent+temporary; แลกพื้นที่/พลังงาน) **Information** (ใช้ EDC/ECC; ฮาร์ดแวร์น้อย) **Temporal** (ทำซ้ำ+เปรียบเทียบ; **ใช้กับ transient เท่านั้น ตรวจ permanent ไม่ได้**) สถาปัตยกรรม: simplex → dual (identical/dissimilar=diverse, control+monitor) → N-way (self-checking/voting); pair-and-spare เป็นแบบกลางที่มีประโยชน์

**Space Shuttle:** 5 เครื่อง NMR ช่วงวิกฤต สลับออกเหลือ TMR มี diverse software ทน 2 เครื่อง **Software fault:** มาจาก specification/design/coding/integration/runtime error; มัก deterministic **N-version programming:** spec เดียวกัน implement ต่างกัน เปรียบเทียบ/vote

## การบ้าน HW02

ให้ PP กับ AP (ตาราง 3×3 ของ A,B,C) หา MPS/MCS, หา reliability ทั้งคู่ และเทียบเมื่อทุก subsystem = R วิธีคือหา MPS โดยไล่ทุกเส้นทาง แล้วใช้ inclusion-exclusion หรือลดเป็น series-parallel

## ต้องจำทันที และกับดัก

**จำทันที:** R(t)=e^(−λt); MTTF=1/λ; A=MTTF/(MTTF+MTTR); series=ผลคูณ; parallel=1−ผลคูณของ failure; TMR=(3R_m²−2R_m³)R_V ชนะเมื่อ R_m>1/2; keystone; R_PS>R_SP

**กับดัก:** series/parallel ไม่เหมือน schematic; อย่าลืม voter; เพิ่ม node อาจทำร้าย; time redundancy ตรวจ permanent ไม่ได้; R1/R2 อันไหนดีกว่าขึ้นกับ mission time

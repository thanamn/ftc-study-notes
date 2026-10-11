# บทที่ 8 — ซ้อมโจทย์ แผ่นสูตร และเช็กลิสต์ (ฉบับย่อ)

## กลยุทธ์ในห้องสอบ

สอบเปิดหนังสือ/โน้ต/เน็ต 3 ชั่วโมง ไม่ต้องท่องทุกอย่าง ให้จำแนกโจทย์แล้วเปิดโน้ตหาข้อมูล ตั้งเป้าสามระดับ: **รู้แบบไม่ต้องคิด** (นิยาม/กฎที่ทำให้จำแนกโจทย์), **derive ได้** (กระบวนการทีละขั้น), **เปิดดูได้** (รายการยาว/ทฤษฎีบทรอง) ทุกโจทย์ถามตัวเองว่าเป็นเรื่อง **หาปริมาณ** (reliability, probability), **แยกประเภท** (FS/ST/TSC, consistent/inconsistent, fault class) หรือ **ออกแบบ/บรรยายขั้นตอน** (Oral Message, cyclic encoding, checker)

## โยงข้อสอบเก่ากับบท

- **Liveness/Safety** → บท 1: safety = "ไม่มีอะไรแย่" (safety attribute); liveness = "มีสิ่งดีเกิดในที่สุด" (reliability/availability)
- **Threat ของ net banking** → บท 1: hacker/human error = fault → error → failure; โยง attribute และการป้องกัน
- **MTTF < เวลารัน แก้ด้วยอะไรที่ไม่ใช่เพิ่ม reliability** → บท 1–2: redundancy, fault tolerance (checkpointing/rollback), ลด MTTR
- **Fail-Safe/Self-Checking/Recovery วางตรงไหน** → บท 1, 7: self-checking = ต้น error; fault masking = ซ่อน error; fail-safe = ตอน failure; recovery = คืน state
- **ตาราง recovery เวลาเท่ากัน/ไม่เท่ากัน** → บท 4: เท่ากัน = coordinated/synchronous; ไม่เท่ากัน = uncoordinated/asynchronous
- **กริด Hamming distance** → บท 5: detect d≥s+1, correct d≥2t+1, SEC-DED d≥4
- **โจทย์ network probability** → บท 2: series/parallel/bridge; ตั้งอสมการแล้วแก้หา R
- **Byzantine 7 node (ซื่อสัตย์ 5, กบฏ 2)** → บท 3: n ≥ 3m+1; วาด OM(2)/OM(1)/OM(0) + ตารางเสียงข้างมาก
- **(n,M,d), Berger, หารยาว** → บท 5
- **FS/ST/TSC/SFS + a stuck 0** → บท 6: เจน truth table ก่อน
- **notation code length 6 + C stuck-at-1** → บท 5, 6

## ตารางคำที่สับสน

reliability vs availability (ระยะเวลา vs เปอร์เซ็นต์เวลา); fault removal vs fault tolerance; fault avoidance vs fault masking (ออกแบบ vs รัน); error vs failure (state ภายใน vs บริการที่ส่งออก); detect vs correct (d≥s+1 vs d≥2t+1); lost vs delayed vs orphan vs duplicate message; consistent vs strongly consistent cut (orphan vs message ค้าง); FS vs ST; CD vs ES; TMR vs NMR; bit voting vs word voting; forward vs backward recovery

## แผ่นสูตร

**Reliability:** R(t) = e^(−λt); MTTF = 1/λ = ∫R(t)dt; M(t) = 1−e^(−μt); MTTR = 1/μ; **A = MTTF/(MTTF+MTTR)**
**series:** R = ∏Rᵢ, A = AₓAᵧ; **parallel:** R = 1−∏(1−Rᵢ), A = 1−(1−Aₓ)²
**spare:** A = 1 − f(1−a)^(s+1), f = C(n,s+1)
**TMR:** R = (3R_m²−2R_m³)R_V; ชนะเมื่อ R_m > 1/2; MTTF = 5/(6λ); voter R_V > 1/(3R_m−2R_m²)
**non-SP:** R_sys = P(works|m)R_m + P(works|m พัง)(1−R_m); bridge = R⁶−3R⁵+R⁴+2R³
**Byzantine:** n ≥ 3m+1; messages = O(n^m); k+1 (silent), 2k+1 (arbitrary), 3k+1 (colluding)
**Coding:** detect s: d ≥ s+1; correct t: d ≥ 2t+1; SEC-DED: d ≥ 4; (n,M,d); rate R = log_q(M)/n; cyclic (n,k) g ดีกรี n−k หาร x^n−1; Berger c = ⌈log₂(k+1)⌉, n = k+c; low-cost residue A = 2^a−1
**Hamming/parity:** C1 = D1⊕D2⊕D4⊕D5⊕D7; C2 = D1⊕D3⊕D4⊕D6⊕D7; C3 = D2⊕D3⊕D4⊕D8; C4 = D5⊕D6⊕D7⊕D8; syndrome = ตำแหน่ง error
**Logging:** ∀e : ¬Stable(e) ⇒ |Depend(e)| = 0

## การตรวจช่องโหว่

**ครอบคลุมครบ:** FTC01–FTC07 ทุกสไลด์เชิงเนื้อหา รวมหัวข้อรอง (resilience, RAM/RMA, maintenance, ตารางจำแนก, RAID, Space Shuttle, blockchain, client-server 5 สถานการณ์, ตระกูล recovery, code detection/correction, checker ทุกชนิด, fail-safe) **นอกขอบเขต:** TDC01–TDC04 และเนื้อหา out-of-scope (ISBN, compression ลึก ๆ, cryptography, information theory)

**จุดที่ไม่แน่นอน (ติดธง):** liveness/safety ไม่ได้เขียนในสไลด์ตรง ๆ; โจทย์ "เวลาเท่ากัน/ไม่เท่ากัน" กำกวม; กริด Hamming distance = 1 น่าจะเพี้ยน; "code length = 6" กำกวม; FTC01/02 ไม่มี transcript

## เช็กลิสต์ก่อนสอบ (อธิบายออกเสียงให้ได้)

1. สายพาน fault→error→failure + ตัวอย่าง net banking
2. สูตร series/parallel/TMR/bridge + ทำไม TMR ดีกว่าเมื่อ R > 1/2
3. OM(2) เจ็ด node กบฏสอง + วาดตารางเสียงข้างมาก
4. consistent/strongly consistent/inconsistent cut + ตัวอย่าง orphan
5. หารยาว cyclic (7,4) จาก 0101 → 0101100
6. คำนวณ Berger check
7. อธิบาย FS/ST/TSC/SFS + ตรวจ input หนึ่งชุด
8. แผนที่ Fault Avoidance/Masking/Tolerance + วาง self-checking/recovery/fail-safe
9. keystone decomposition + วลี path shorted / path opened
10. แยกแยะ message 5 ชนิดบนไทม์ไลน์

ถ้าจะฟังซ้ำตอนเดินทาง ให้เริ่มจาก "ต้องจำทันที" ท้ายแต่ละบท แล้วฟังเนื้อหาเต็มเฉพาะส่วนที่ไม่แม่น

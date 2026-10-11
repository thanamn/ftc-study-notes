# บทที่ 7 — FTC07 Fault Masking (ฉบับย่อ)

## ภาพรวมและแผนที่ Design Techniques

จัดการ fault สองแนวทาง: **Avoid** (หลีกเลี่ยงไม่ให้เกิด) และ **Tolerate** (ยอมให้เกิดแล้วรับมือ) แผนภาพ **Design Techniques** (รูปที่แนบข้อสอบเก่า): specification/implementation mistake, external disturbance, component defect → software/hardware fault → **Errors** → **System failures** โดยมีวงเล็บ **Fault Avoidance** (ก่อน fault) → **Fault Masking** (ระหว่าง fault-กับ-error) → **Fault Tolerance** (ระหว่าง error-กับ-failure)

**สามตัวเลือก:** (1) Detect and replace (dynamic: detectors + spare) (2) Mask (static: voter เลือกเสียงข้างมาก) (3) Mask+diagnose+reconfigure (hybrid: mask ที่ output แต่ diagnose ได้ + เปลี่ยน spare; เป็น static เมื่อ spare หมด)

## การบังความผิดพลาดโดยธรรมชาติของลอจิก

ใน AND: fault 1→0 ที่ input เป็น **critical**, 0→1 ถูก mask; ใน OR กลับกัน แม้วงจร non-redundant ก็ mask ได้บ้าง **Interwoven redundant logic:** ทำสำเนา x เป็น x1..x4 แล้วสลับชั้น AND/OR → critical fault ของชั้นหนึ่งถูกบังโดยอีกชั้น เพื่อบัง h fault: replication โตตาม (h+1); **h=1 เรียกว่า Quadded logic**

## Combinatorial modeling

สมมติ: module พังอิสระ; พังแล้วให้ผลผิดเสมอ; ระบบพังถ้าไม่เป็นตาม minimal set
**series:** R_s = ∏Rᵢ; **parallel:** R_p = 1 − ∏(1−Rᵢ)
**non-series-parallel:** keystone **R_sys = P(works | m ทำงาน)·R_m + P(works | m พัง)·(1−R_m)**
**วลีช่วยจำ:** **"module works = path shorted"**, **"module fails = path opened"** (บังคับแล้ว module หายไปจากไดอะแกรม)

**บริดจ์ 6 โมดูล (condition บน E แล้วภายใน condition บน B):** R_sys = [1−(1−R_AR_B)(1−R_F)]·R_CR_D·(1−R_E) + [1−(1−R_A)(1−R_FR_C)]·R_D·R_E; เมื่อทุกตัว = R → **R_sys = R⁶ − 3R⁵ + R⁴ + 2R³** **Insight:** เมื่อ E ถูก short แล้ว ไดอะแกรมที่ยุบไม่มี B จึงได้สูตรเดียวกันไม่ว่า B will work หรือ fail เลือก **A** เป็น keystone จะง่ายสุด (แยกเป็น series-parallel ทันที) heuristic: เลือก module บนหลาย path มากสุด, เลือกตัวที่ทำให้เป็น serial/parallel

**โจทย์ System P vs Q:** P = ขนานล้วน (A→C ขนาน B→D); Q = เหมือนกันแต่มี **K เป็นสะพาน** → non-SP เลือก K เป็น keystone สรุป **Q > P** เพราะ K พัง Q กลายเป็น P, K ทำงาน Q มีทางมากกว่า → Rq − Rp = 2R²(R−1)² ≥ 0

## TMR และ NMR

**TMR voter สมบูรณ์แบบ:** R = 3R_m² − 2R_m³; ชนะ simplex เมื่อ **R_m > 1/2**; MTTF = **5/(6λ)** (ต่ำกว่า simplex) **มุมเวลา:** เส้น R ของ TMR ตกชันกว่า simplex และ **ตัดกันที่ λt = ln 2** → mission สั้นเลือก TMR, mission ยาว simplex อาจดีกว่า
**voter ไม่สมบูรณ์แบบ:** R = R_V(3R_m² − 2R_m³); เงื่อนไข **R_V > 1/(3R_m − 2R_m²)** และ R_m ต้องอยู่ในช่วง; ตัวอย่าง R_V=0.95 → **0.56 < R_m < 0.94**; กราฟเป็นรูปตัว U, ค่าต่ำสุดของ R_V ~0.885
**compensating faults:** R = (3R_m² − 2R_m³) + **6p0p1R_m** (พังคนละทิศแล้วหักกลบกัน) ตัวอย่าง R_m=0.998, p0=p1=0.001 → R=0.999990
**NMR:** N module + voter (N มักคี่); 5MR ทำงานถ้า 3/5 ดี; 4MR vote 3-out-of-4; voter โตเร็วเมื่อ N เพิ่ม

## Voter และ word voting

**Bit-voter TMR:** y = x1x2 + x2x3 + x3x1 (= carry ของ full-adder) 5MR/7MR ระดับ gate ระเบิดเร็ว **คำเตือน:** bit voting ≠ word voting และ bit-by-bit voting อาจให้ค่าที่**ไม่ตรงกับ input ใดเลย** เช่นได้ค่าที่ไม่มีในความเป็นจริง ขณะที่ word voting ยังได้ค่าถูก → word voting รักษา data integrity ดีกว่า voter แบบง่าย: ถ้า disagreement กันหมดเลือกอันใดก็ได้ (compare + mux)

## Standby และ hybrid

**Standby:** n-to-1 switch เลือก output ของ module ที่ทำงาน; detector ใช้ error coding/reasonableness check/watchdog; เมื่อ detect ก็ flag ตัวเสียและเปิด spare ถัดไป; ใช้ n-to-2 + เปรียบเทียบ = **pair-and-spares**
**Hybrid:** n active + s spare → **(n+s)-to-n switch** **Self-purging:** ทุก module active ตั้งแต่แรก ถูก purge เมื่อ disagree; voter = threshold voter (weight 1 active / 0 purged) **Variation:** NMR/simplex ที่ voting unit ตรวจ disagreement ได้ → ถอดตัวเสีย + อีกหนึ่งตัว → vote ชัดเจน + ยืดอายุ **static redundancy ทำให้ทดสอบ fault ยากขึ้น** ต้องมั่นใจว่า component ปลอด fault ตอนเริ่ม

## Time redundancy และ applications

**Retry** เหมาะกับ transient fault; recomputation ไม่ช่วยกับ permanent fault — เลี่ยงได้โดยเปลี่ยน operand (คำนวณ a·(2b) แทน (2a)·b; b+a หรือ −(−a−b) แทน a+b) **Mixed space/time:** เพิ่ม hardware บางส่วนเพื่อ interleave การ recompute ให้เร็วขึ้น **EDDI:** เขียนโค้ดซ้ำแล้ว compare ก่อน store **Space Shuttle:** 5-way (NMR ช่วงวิกฤต + diverse software); **Shinkansen:** triple-duplex (6-fold)

## Alternating logic

ส่งข้อมูลและเก็บ → ส่ง bitwise complement → เปรียบเทียบ → ตรวจจับ stuck-at และ transient; ข้อดีเทียบ duplication คือ common error น้อยกว่า **Dual ของ f:** fd(x̄) = f̄(x) (สลับ AND/OR); **self-dual** ถ้า f = fd → คำนวณ f กับ fd ด้วยวงจรเดียวกันได้ (time redundancy) full-adder sum และ carry เป็น self-dual; k-bit adder ก็ self-dual **Recomputing with transformed operands:** encode/decode ด้วย complement, shift หรือ swap (b+a) **Segmented addition:** แบ่ง operand/adder เป็น 2–3 ส่วน ทำ replicated addition + compare/vote

## Fail-safe systems

**Fail-safe** = เมื่อพังแล้วผลิต output ในชุดที่ปลอดภัยล่วงหน้า (ไฟจราจรค้างแดง; pilot เตาแก๊สปิดวาล์วเมื่อเปลวดับ) ต้องมี **output ≥ 2 line** (ถ้า line เดียว แม้ค่าหนึ่งปลอดภัย แต่ stuck ค่าอื่นก็ไม่ปลอดภัย) two-rail เป็นทางเลือก (0=01, 1=10, F=00,11) **Totally fail-safe** = ปลอดภัยตราบที่ไม่มี failure อีกอันก่อนตรวจพบ; **Ultimate fail-safe** = ตลอดไป
**ตัวอย่างรถไฟสวนสนุก:** sB (ต้นราง, เดินหน้าได้ไม่ควรถอย), sE (ปลายราง, ถอยได้ไม่ควรเดินหน้า) → ข้อกำหนดไม่ complete เพราะไม่บอกว่า sB=sE=1 ทำอะไร
**Fail-safe 2-out-of-4 checker:** input มีหนึ่งพอดี 2; fg = 01/10 ถ้าถูกต้อง, 00 = safe, 11 = unsafe; output กลายเป็น 00 ถาวรเมื่อ unsafe ครั้งแรก **Fail-safe state machine:** encode state ด้วย Berger code เลี่ยง state 0 ทั้งหมด/check 1 ทั้งหมด; next-state เป็น SOP สำหรับ main bit, POS สำหรับ check bit

## ต้องจำทันที และกับดัก

**จำทันที:** แผนที่ Fault Avoidance/Masking/Tolerance; inherent masking + quadded (h=1); series/parallel/keystone; พหุนาม bridge R⁶−3R⁵+R⁴+2R³; TMR ชนะเมื่อ R_m>1/2; NMR; standby/hybrid/self-purging; alternating logic + self-dual; fail-safe ≥2 output

**กับดัก:** fail-safe ต้องมี output ≥2 line; static redundancy ทำให้ทดสอบยากและต้องปลอด fault ตอนเริ่ม; bit voting ≠ word voting; TMR ที่ module reliable สูงเกินไปอาจแย่กว่า simplex (voter เป็นจุดพังใหม่); แนวข้อสอบที่อาจารย์ยืนยันว่าออกคือ TMR, non-SP และ masking

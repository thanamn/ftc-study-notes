# FTC04 — Transcript Insights (Rollback Recovery & Checkpointing)

> สรุปเนื้อหาที่ **อาจารย์อธิบายด้วยคำพูด** (ไม่ใช่การทวน bullet บนสไลด์)
> เน้น: 直觉/เหตุผล/ตัวอย่าง/สิ่งที่เน้นย้ำ/แนวข้อสอบ
> หมายเหตุ: transcript เป็น ASR ภาษาไทยที่เพี้ยนพอสมควร หากกำกวมจะเขียน `[ไม่แน่ใจ: ...]` ไม่เดา

---

## 0. ภาพรวมบรรยากาศคาบนี้

- คาบนี้ **รีบ** (อาจารย์พูดเองว่า "วันนี้เร็วนิดหนึ่ง") และยัง **อธิบายไม่จบ** — ท่อนเรื่อง Blocking/Non-blocking และเทคนิค coordinated/uncoordinated อาจารย์บอกว่า "เดี๋ยวจะอธิบายเพิ่มเติมภายหลัง"
- ลำดับการสอน: ทบทวนการบ้าน BFT สัปดาห์ก่อน → เข้าเรื่อง Fault/Error/Failure และ Recovery → Rollback Recovery, Checkpoint → System Model → Cut/Recovery Line → ประเภท Message → Domino Effect/Livelock → โยนการบ้านท้ายคาบแล้วปิด
- อาจารย์ **ไม่ค่อยลงรายละเอียดสไลด์** แต่ใช้เวลาอธิบาย "ทำไม" และ "ทำไมต้องสนใจ"

---

## 1. ทบทวนโจทย์ BFT สัปดาห์ก่อน (Oral Message) — ใช้เป็นแรงจูงใจเข้าสู่ Rollback

- ตัวอย่างเป็นโจทย์ของสัปดาห์ก่อน (Byzantine) `[ไม่แน่ใจ: คำว่า "ใบสันตา" น่าจะคือ Byzantine]`
- ตั้ง: มีทั้งหมด **8 หน่วย** = Commander 1 + lieutenant ราว 6–7 ตัว, มี **traitor 2 ตัว** (คือ M = 2)
- เกณฑ์ที่อาจารย์เน้น: ต้องมีจำนวนรวม **≥ 3M+1** — แทน M=2 ได้ 7 แต่ของจริงมี 8 → จึงแก้ได้
- ขั้นตอนที่อธิบาย (ตรงกับสไลด์ 1–2): **OM(2) → OM(1) → OM(0)**
  - รอบแรก: Commander ส่งคำสั่ง (Attack) ไปยัง lieutenant ทุกคน (Commander ปกติจะไม่โกหก)
  - OM(1): lieutenant ทุกคน **รวม traitor** ทำหน้าที่เป็น commander ส่งต่อ
  - OM(0): lieutenant ทุกคน (รวม traitor) relay ข้อความต่อ
  - ได้ตารางค่า value ที่แต่ละตัวได้รับ แล้วทำ **majority vote** → ผลออกมาเป็น A ทั้งหมด
- ประเด็นที่อาจารย์โยง: ค่าที่ได้เป็นผลจาก tag/ค่าที่ส่งต่อในแต่ละ level และแท็กที่ผิด/ถูกตรวจได้ตั้งแต่ level 2 ขึ้นไป `[ไม่แน่ใจ: "ส่วน A เนี้ยมีแค่ 3"]`

**สะพานเชื่อมไปเนื้อหาใหม่ (สำคัญ):** ถ้าข้อความ/ระบบมี **error มากกว่าระบบจะรับได้ (เกินกว่าที่ majority vote จะแก้)** → ผลการ vote จะไม่ unique (เสียงข้างมากไม่ชัด) `[ไม่แน่ใจ: อาจารย์พูดว่าโอกาส > 1/2]` → เราจึงต้องมีกลไก **Checkpoint / Rollback Recovery** แทน

---

## 2. Fault → Error → Failure และความหมายของ Recovery

- ลำดับเหตุการณ์ที่อาจารย์อธิบาย: ระบบเดินไปเรื่อย ๆ แล้วเกิด fault → กลายเป็น error → ถ้าปล่อยไว้จะกลายเป็น failure
- **แทรกได้ก่อนเป็น failure**: ช่วงที่ยังเป็น error เราสามารถ **detect** ได้ → เข้าสู่กระบวนการ recovery → ได้ **valid state** กลับมา
- กล่าวเชิงแนวคิด: **error คือ event ที่นำไปสู่ failure ได้** ต้อง recover ให้ทันก่อน
- ประเภทของ failure ที่อาจารย์ไล่ (ตรงกับสไลด์): process failure (deadlock, protection violation, erroneous input), system failure (full/partial amnesia), secondary storage failure, communication/network failure

**Recovery หมายถึงอะไร (คำอธิบายของอาจารย์):**
- การกู้คืนใน digital system ที่ state อาจ **ไม่ consistent กัน** เพราะเกิด failure
- ถ้า **ไม่ได้ checkpoint ไว้** ต้องเริ่มใหม่ตั้งแต่ต้น
- ถ้า **จับ state ก่อนที่มันจะเสียได้** (capture at a point) แล้วย้อนกลับไปแค่จุดนั้น → **ลดเวลาได้** (กู้คืน/กู้ได้เร็วขึ้น)
- วิธีที่ยกตัวอย่าง: Restart, Reclaim resources, Undo/ทำ transaction ที่ค้างให้จบ — ทั้งหมดนับเป็น recovery
- **Failure Recovery** = หลัง failure เกิด แล้ว restore ระบบกลับสู่ Normal State

---

## 3. Forward Recovery vs Backward (Rollback) Recovery — และ "เลือกใช้ตามเป้าหมาย"

- **Forward recovery** = พอรู้ว่าเสียหาย เรา **เดินหน้าแก้** แทนที่จะถอยกลับไป state ที่ถูก (คือมุ่งไปข้างหน้า) — แนวคิดแบบ error filter / TMR
  - ข้อดี: **ลดเวลา processing** ได้ และให้ availability ที่ดี แต่ **ต้องลงทุนสูง (cost สูง)**
- **Backward (Rollback) recovery** = **operation-based** (do/undo/redo logs) — ย้อนกลับไป state ที่เราตั้ง/checkpoint ไว้
  - ข้อเสีย: **ต้องทำงานซ้ำ → performance penalty** จ่ายเป็น "เวลา/งานที่ทำซ้ำ"
- **เกณฑ์ตัดสินใจที่อาจารย์เน้นชัดเจน:**
  - ถ้าระบบ **ไม่แคร์ performance แต่ต้องการ validity สูง** → เน้น **Forward** (เกิด error ก็ให้ข้ามไปเลย)
  - ถ้าระบบ **ต้องการ low cost** → เน้น **Backward/Rollback**
- ตัวอย่าง forward ที่อาจารย์ยกเพิ่ม: `[ไม่แน่ใจ: "GMR"]` (น่าจะหมายถึง TMR/replication), โมดูลที่เสีย 1 ตัวแล้วทำงานต่อได้ ค่อยแก้ทีหลัง
- **Exception** = ถือเป็น forward recovery รูปแบบหนึ่ง: พอรู้ว่า system เกิดเหตุ ก็ interrupt ขึ้นมา, มี "set exception" **predefine** ไว้ล่วงหน้าว่าเจอ exception ชนิดนี้ให้เริ่มที่ไหน (เช่น divide-by-zero) — ต่างจาก backward ที่พอกดย้อนกลับไปก็เจอโจทย์เดิมซ้ำ (จึงต้อง predefine ไว้)
- **จุดที่อาจารย์ย้ำเกี่ยวกับ backward:** เรามัก **repair ไม่ได้** จึงต้องย้อนไปจุดที่กำหนด; พอย้อนแล้วเดินต่อ อาจเจอปัญหา:
  1. performance (ทำงานซ้ำ)
  2. **เราไม่รู้ว่า fault ที่เพิ่งเกิดเป็น transient หรือ permanent** → fault อาจเกิดซ้ำอีก

---

## 4. Checkpoint / Backup & Recovery คืออะไร (คำอธิบายเพิ่มจากสไลด์)

- หลักการ Backup & Recovery = restore ระบบกลับไป state ที่เราตั้งไว้ (checkpoint) แล้วประมวลผล (reprocess) ใหม่ ระบบจึงทำงานต่อได้ → **จำเป็นต้องมี checkpoint**
- นิยามเชิง intuition: checkpoint = state ของระบบที่ผ่านมา เก็บว่ามี state อะไรบ้าง; ย้อนกลับได้หลายครั้ง
- **ความซับซ้อนของ rollback recovery ขึ้นอยู่กับ message** — message บางตัวมี "ordering" ติดมาด้วย ต้องระวัง
- rollback มีแนวโน้ม **ย้อนไปย้อนมา** และอาจย้อนไปถึงต้นทางเลย → ปรากฏการณ์นี้เรียกว่า **Domino Effect**
- แบ่งเป็น 2 กลุ่ม: **state-based** (checkpointing) และ **log-based** (ตามสไลด์ 13)

---

## 5. Checkpointing Issues in Distributed Environment (ที่อาจารย์ขยาย)

- หัวใจคือ **Consistency**: ข้อความต้องรู้ว่า **ใครส่ง (sender) และใครรับ (receiver)** อย่างชัดเจน
- เหตุผล: ถ้าไม่รู้ แล้ว checkpoint แล้วย้อนกลับมา จะ **ไม่รู้ว่า message นั้นใครเป็นผู้ส่ง/ผู้รับ** → ใช้ recovery ไม่ได้
- **Trade-off ของความถี่ checkpoint** (อาจารย์เน้น):
  - ทำถี่ ๆ (ทุก 1 วินาที / 0.1 วินาที) ทำได้ แต่ **เปลือง (cost/overhead)** → ไม่ควรทำมากเกินไป
  - ทำห่างเกินไปก็ไม่ไหว → **คล้ายกับการเริ่มต้นใหม่หมด**
- ระบบนี้เป็น **distributed system** บางครั้งสื่อสารกับ **outside world** ซึ่งบางที **เราไม่รู้เลยว่าส่งไปสำเร็จหรือยัง** (จึงจัดการยาก)

---

## 6. System Model — ทำไมต้อง model

- เพื่อสร้าง checkpoint ที่ดี ต้อง **model ระบบของเรา** ว่า จัดการ/สร้าง checkpoint อย่างไร เพื่อให้อธิบายการทำงานได้ง่ายขึ้น → เรียกว่า **System Model**
- โครงที่อาจารย์อธิบาย: มีส่วน "นอกระบบ" (outside) และ "ระบบของเรา" ที่ประกอบด้วยหลาย **Process**
  - process สื่อสารกันด้วยการ send/receive message
  - message อาจเป็น message ภายใน process ด้วยกันเอง หรือ message ที่มาจาก **ภายนอก** ก็ได้
  - ตัวอย่างลำดับ: external → P0 → P1 → แล้ว P0/P1 ส่งต่อไป P2 สลับไปมา

---

## 7. Recovery Line / Cut / Consistent State

- **Checkpointing vs Logging** (basic approach 2 แบบ):
  - Checkpointing = restore กลับไปที่ state ของ process
  - Logging = **replay message**
- **Stable storage เป็น prerequisite**: state ที่จะเริ่ม recovery ต้องเก็บใน stable storage — ถ้า storage ไม่ stable recovery จะไม่ถูกต้อง/ไม่ปลอดภัย
- checkpoint ใน rollback recovery = การสร้าง checkpoint ในแต่ละ process (checkpoint process) → เมื่อเชื่อมกันจะได้เป็น **Recovery Line / Recovery Cut**
- วิธีมองภาพ: ส่วนที่อยู่ **ก่อน** recovery line = ฝั่งที่ถูก cut ไว้ (ย้อนกลับได้); ส่วน **นอก** (ฝั่งขวามือของเส้น) = ไม่ย้อน
- **Consistent state** = state ที่เราสามารถ recover กลับมาได้ และมี **ข้อมูลเพียงพอที่จะ replay** ได้ (เริ่มจากจุด checkpoint นั้น)
- **Local Recovery Line** ที่ตัดได้ถูกต้อง = **Strongly Consistent Cut** — ตัดแล้วไม่ทิ้ง message ค้างในเส้น

### วิธีคิดตอนหา cut (อาจารย์อธิบายเป็นขั้น)
- สมมติ process เดินมา แล้ว P1 เกิด error ที่จุดหนึ่ง (ในภาพคือจุดสีแดงเข้ม) → ต้องย้อนกลับไป state ที่ checkpoint ไว้
- ย้อนกลับมาแล้ว ต้องเช็คว่า **ทำให้ process ที่มี dependency กันไม่พัง** (`consistent`)
- ถ้าเลือก cut ดี: จะ **ไม่มี message ตกค้าง** ทั้งฝั่งก่อนและหลังเส้น — message แยกกันเป็นอิสระ (ต้นทาง–ปลายทาง)
- **เทคนิคอ่านภาพ:** ลูกศร (message) ที่อยู่ในฝั่ง **ก่อน** เส้น cut = ถูกตัดไว้ข้างใน; ลูกศรที่เหลือ = message ที่ **ส่งหลัง** cut

---

## 8. ประเภทของ Message (คำอธิบายของอาจารย์ — เน้น "รู้ send รู้ receive")

1. **In-transit message** — ส่งไปแล้วแต่ยังไม่ถึง ยังอยู่ระหว่างทาง
2. **Lost message** — ส่งไปแล้ว "หายไป" เพราะเกิด failure ใน process ปลายทาง จึงไปไม่ถึง → message หายระหว่างทาง (ต่างจาก in-transit)
3. **Delayed message** — message ที่ไปถึง **ช้า** หรือไปถึง **หลังจาก rollback/recover แล้ว**
4. **Orphan message** — มี record การ **receive** แต่ไม่มี record การ **send** (รู้ว่าปลายทางเป็นใคร แต่ไม่รู้ว่าต้นทางส่งมาจากไหน) → เกิดเมื่อ cut ไม่ consistent (เช่น cut ที่มี orphan message)
5. **Duplicate message** — message ที่เคยรับแล้วถูก **ส่งซ้ำอีก** หลัง recovery

### ความต่างที่อาจารย์ย้ำ
- **In-transit vs Lost:** in-transit = ตัดกับเส้น (cross); lost = เกิด failure ใน process จนส่งไปไม่ถึง อาจไม่ตัดกับเส้นก็ได้
- **In-transit vs Delay:** delay = ไปถึงหลัง recover/หลัง rollback
- **Orphan ต่างจากตัวอื่น** ตรงที่รู้ผู้รับแต่ไม่รู้ผู้ส่ง (cross กับเส้น cut ที่จุด rollback)

---

## 9. ตัวอย่างนับ Message (m1..m5) ที่อาจารย์ไล่ทีละตัว

- ตัดเส้นแล้วพบ message **ส่งแล้วยังไม่ถึง** → **in-transit** = m1, m2
- **lost** = m1 (หายไปเพราะไปถึง)
- **delayed** = m1, m5 (m5 มาช้าเช่นกัน)
- **orphan** = ไม่มี
- **duplicate** = m4, m5

(ตรงกับสไลด์ 29 — อาจารย์ไล่เหตุผลทีละตัวจากภาพ ไม่ใช่แค่อ่านคำตอบ)

---

## 10. Consistent / Strongly Consistent / Inconsistent (สรุปท้ายคาบ — สำคัญมาก)

อาจารย์สรุปนิยามตอนท้ายคาบ (น่าจะเป็น key ของการบ้าน/ข้อสอบ):

- **Inconsistent checkpoint** = มี **orphan message** → ใช้ไม่ได้ เพราะ**ไม่รู้ว่าใครเป็นเจ้าของ message** (ไม่รู้ผู้ส่ง)
- **Consistent checkpoint** = **ไม่มี orphan message** (แต่อาจมี in-transit ค้างอยู่ได้)
- **Strongly Consistent checkpoint** = **ไม่มี in-transit message** (และไม่มี orphan) → คือ cut ที่สะอาดที่สุด
- กฎอ่านภาพ: ถ้า cut แล้วมี message ที่ **cross** เส้น (โดยเฉพาะ in-transit) → ยังนับ consistent ได้; แต่ถ้าเป็น **orphan** → **inconsistent**

> Consistent state = state ที่สร้าง recovery line ได้; recovery line ต้องอยู่ใน consistent state

---

## 11. Domino Effect / Livelock และวิธีกัน

- **Domino Effect**: การ rollback ต่อกันเป็นลูกโซ่ ทำให้ย้อนไปไกลเกินจริง (อาจถึงจุดเริ่มต้น) ทั้งที่มี checkpoint อยู่
  - ตัวอย่างที่อาจารย์อธิบาย (สไลด์ 32): Y rollback ไป y2 → m กลายเป็น orphan → X ต้อง rollback ไป x2; ถ้า Z rollback ไป z2 → Y ต้องไป y1 → บังคับให้ X, Z ย้อนไป x1, z1
- **Livelock** (สไลด์ 33): Y crash ก่อนรับ n1 → rollback; recover มารับ n1 ส่ง m2; X recover ส่ง n2 แต่ไม่มี record ของ n1 → Y ถูกบังคับ rollback อีกรอบ; วนซ้ำได้ไม่รู้จบ
- **วิธีกัน (สรุปของอาจารย์):** เวลาสร้าง checkpoint **ควรสร้าง checkpoint ที่ไม่มี in-transit message** (และไม่มี orphan) — จะช่วยกันทั้ง Domino Effect และ Livelock
- อาจารย์ทวนกลไก domino อีกครั้งด้วยจุด X1/Z1/X2/Y2/X3/Y3: "การถอยกลับจริง ๆ จาก X3 → X2 …" แล้วชี้ว่าการถอยจะบังคับกันเป็นทอด (`force`) จนเป็น loop ที่ไม่สิ้นสุดเพราะมี lock

---

## 12. เทคนิคที่เหลือ (อธิบายไม่จบในคาบนี้)

- เทคนิค rollback ทั้งหมดที่พูดในคาบเป็นแนว **state-based / checkpointing**
- แบ่งเป็น **coordinated vs uncoordinated** → จะลงรายละเอียดต่อในคลิป/คาบถัดไป
- มีส่วน **locking-based** ที่อาจารย์บอกว่าอาจพูดไปแล้ว
- เรื่อง **Blocking / Non-blocking** — อาจารย์บอกว่า **ยังไม่มีตัวอย่าง** จึงเขียนสไลด์ไว้ก่อน "เดี๋ยวหา example แล้วโชว์" และจะอธิบายเพิ่มภายหลัง
- จุดที่เน้น: checkpoint เป็นกลไกหนึ่งที่ **ป้องกัน Domino Effect** ได้ และ Blocking/Non-blocking เกี่ยวกับการกันปัญหา orphan message

---

## 13. การบ้าน (HW04) และแนวข้อสอบ — สิ่งที่อาจารย์ย้ำ

- โจทย์การบ้าน (สไลด์ 51): **หาจุด/เส้นตัด consistent cuts ในรูป (ที่ลากผ่าน ▓)** แล้วตอบว่า recovery line ที่หาได้เป็น **consistent / strongly consistent / inconsistent**
- **Hint ที่อาจารย์ให้ชัด:** "เวลาลาก recovery line ต้องลาก **ผ่านทุก process**" (เส้นเดียวลากผ่านทุก process ถือเป็น recovery line หนึ่งตัว)
- ให้ **ยกตัวอย่าง/โชว์เส้นที่ consistent** ให้ดูด้วย
- เกณฑ์ตอบ (ตามหัวข้อ 10): ดูว่ามี **orphan message** ไหม → inconsistent; มีแค่ **in-transit** → consistent; **ไม่มีทั้ง orphan และ in-transit** → strongly consistent
- อาจารย์บอกว่าส่งการบ้านให้แล้ว (`[ไม่แน่ใจ: "ส่งแบบอากาศไปแล้ว" น่าจะหมายถึงส่งไฟล์/airdrop ให้แล้ว]`) แล้วปิดคาบ
- **ข้อควรระวัง**: เนื้อหาคาบนี้ถูกตัดจบเร็ว และอาจารย์ยังไม่อธิบาย coordinated/uncoordinated + pessimistic logging ละเอียด — ควรไปดูส่วนที่เหลือ

---

## ภาคผนวก: จุดที่ transcript เพี้ยน/ไม่แน่ใจ

- `[ไม่แน่ใจ: "ใบสันตา" = Byzantine]`
- `[ไม่แน่ใจ: ช่วงทบทวน BFT ท้ายรอบ — "ส่วน A เนี้ยมีแค่ 3" และค่า threshold ที่อาจารย์พูด]`
- `[ไม่แน่ใจ: "GMR" ในท่อน forward recovery — น่าจะเป็น replication/TMR]`
- `[ไม่แน่ใจ: ชื่อระดับ/ศัพท์ operation หลายจุดในท่อน [00:10:12]–[00:13:01] เสียงขาด]`
- `[ไม่แน่ใจ: ตัวอย่าง m1..m5 ในท่อน [00:37:23]–[00:38:30] เสียงเพี้ยน แต่ผลลัพธ์ตรงกับสไลด์ 29]`
- `[ไม่แน่ใจ: "Blocking ใต้ปัญหาโฟร์แฟนเมส" — น่าจะเกี่ยวกับ orphan message/blocking]`

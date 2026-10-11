# FTC03 — Transcript Insights (Byzantine Fault Tolerance / Distributed Systems)

> แยกเฉพาะ "คำอธิบายของอาจารย์" (intuition, การคิดให้ดู, ตัวอย่าง, จุดที่เน้น, hint ข้อสอบ)
> ไม่ใช่การทวนสไลด์ · ข้อความที่ garbled/ไม่ชัดเขียนกำกับ `[ไม่แน่ใจ: ...]`

---

## 0. ช่วงทบทวนตอนเปิดคลาส (ต่อจากบทก่อน — Reliability Network)
- อาจารย์เฉลย/ทบทวนโจทย์เปรียบเทียบ reliability ของ "สองสกรีม (diagram/network)" โดยไล่ตามที่เขียนไว้: รวม series-parallel เป็น S1, S2, B (แต่ละกิ่ง) แล้วรวมทั้งหมดเป็นน้ำหนักเดียว แต่ละสกรีมมีเส้นเชื่อม
- **Bridge** = ตัวกลางที่ "ไปได้ทั้ง 2 ทาง" จึงต้องคิด probability เกี่ยวกับ reliability ของ Bridge แยกออกมา
- พอคำนวณเสร็จแล้วเอาไปเทียบกัน พบว่า **สกรีมที่ 1 มี reliability สูงกว่า** (ค่าที่ได้มากกว่า) — บทเรียนคือโครงสร้างที่มี Bridge/เส้นเชื่อมช่วย ทำให้ reliability ดีขึ้น
- `[ไม่แน่ใจ: รายละเอียดตัวเลข/ชื่อกิ่ง (A, S1, S2, B) เพราะ transcript เพี้ยนหนัก]`

---

## 1. ทำไมต้องพูดเรื่อง Process Group (จาก Single Process → Distributed)
- บทนี้เป็นเรื่อง **Fault Tolerance ของระบบที่กระจายออกไป (distributed)** ต้องมีแนวคิดการป้องกันให้ทนต่อความบกพร่อง
- **Single Process:** ทำ fault tolerance ได้ง่าย — แค่ทำให้ processor ตัวนั้นมี **reliability สูงขึ้น** ให้ได้ตามเวลา Mission ที่กำหนดไว้ ก็เพิ่มศักยภาพของ process ได้ดี
- แต่ระบบปัจจุบันกระจาย resource และมี network เชื่อมต่อกัน มุมมองแบบ single process **ไม่เพียงพออีกต่อไป**
- เมื่อเป็น **Process Group (multiple process)** ความยากเปลี่ยนไป เพราะ:
  - เรารับข้อมูล/คำสั่งเข้ามาเป็น **Message**
  - Single process อาจมี **coding / check message** ได้ (ตรวจได้แบบหนึ่ง)
  - แต่ Process Group **ทำ coding ทั้งหมดไม่ได้** เพราะมี process จำนวนมาก การ coding จะ **สิ้นเปลือง** เกินไป
  - จึงต้องมีหลักการดูว่า **Message ไหนจริง Message ไหนปลอม** (message authentication/agreement)
- อาจารย์บอกว่าบทนี้ต่อยอดไปถึง: **Oral Message Algorithm**, **blockchain**, และ **client–server communication** (ระบบที่ยังใช้อยู่จริงปัจจุบัน) โดยจะ **เน้นที่ BFT** `[ไม่แน่ใจ: ท่านพูดว่า "VFT" แต่บริบทคือ BFT]`
- เนื้อหาส่วน **fault types, process groups** บอกว่าคนที่เรียน OS หรือ Disk System จะเคยเจอมาแล้ว วันนี้แค่ทบทวน

---

## 2. Process Group — 2 โครงสร้างหลัก (Hierarchical vs Flat)
- **Hierarchical (แบบมีตัวแม่):** มี "ตัวการ/ตัวแม่" แล้วให้เป็นตัวลูกไล่ลงเป็นชั้น ๆ
  - แทนที่ทุก process จะต้องสื่อสารกันเองทั้งหมด จะ **แบ่งเป็นตัวแม่คอยสั่งตัวลูก** ลดเส้นทางการสื่อสาร
  - ข้อเสีย: **ถ้าตัวแม่เสีย = เสียหมดทั้งยวง** (single point of failure) `[ไม่แน่ใจ: ท่านพูดวกไปว่าจุดนี้จะใช้เวลานานกว่า/สั้นกว่ากัน — ใจความคือ hierarchical ประหยัดเส้นทาง แต่เปราะที่ตัวแม่]`
- **Flat Group (แบบแบน):** ทุกตัว **เท่ากัน (fair)** ไม่มีใครใหญ่กว่า
  - แต่ต้อง **compare/check กันเอง** — ทุกตัวที่รับเข้ามาต้องตรวจสอบ (เช่น เปรียบเทียบ message ที่ได้รับทั้งหมด)
- สรุปเชิงเปรียบเทียบ: ถ้ามองแบบ single process แล้วเรื่อง flat มักจะ **reliability ดีกว่า** เพราะไม่ผูกกับตัวแม่ตัวเดียว

---

## 3. Centralized vs Decentralized + Consensus
- ระบบเดิมที่เป็น single process = ทุกอย่างผ่าน **center ตัวเดียว**; centralize มาที่ node แล้วกระจายด้วย link
- ลักษณะนี้คือ **Center Authority** — ส่วนกลางมีอำนาจตัดสินใจทุกอย่าง เหมือน **server ตัวเดียว** ที่กระจายไปทุกโหนด (server ตัวนี้ต้องมี reliability สูง)
- ถ้าต้องการกระจายความเสี่ยง → เปลี่ยนเป็น **Decentralized** ย่อย center ออกเป็น center เล็ก ๆ กระจายไปให้ทั่ว → **ตัวที่เสียมีผลเสียหายน้อยกว่า**
- เมื่อไม่มี center แล้ว การตัดสินใจต้องใช้ **Consensus (ข้อตกลงร่วมกัน)** โดย **เลือก majority (เสียงข้างมาก)** เป็นคำตัดสิน — อาจารย์เน้นว่า "ยกมือว่าใครมีเสียงข้างมาก"
- ตัวอย่างเชิงระบบข้อมูล:
  - **Centralized:** database/account book, **bank account**, account ของบริษัท — มักเป็น server เดียว
  - **Distributed / Flat Group:** database ที่ **แชร์กันทุกหน่วย + replicate copy across network** โดยไม่มีกลุ่ม center ดูแล จึงต้องใช้ **Consensus** ตัดสินว่า database ถูกต้องหรือไม่
  - **Blockchain / network / cryptocurrency** = **Distributed Ledger** (ใช้หลักการนี้)

---

## 4. Resilience + นิยาม Fault Tolerant (จุดสำคัญ)
- Process Group โดยทั่วไปเป็น **Flat Group** ที่มี **Identical Process** อยู่ด้วยกัน จัดระเบียบเป็น decentralized/hierarchy/flat ก็ได้
- เวลาทำงานจะ **ส่ง Message ไปที่ member ทุกคน** (message เดียวกันส่งให้ทุก member)
- คุณสมบัติที่ต้องการเรียกว่า **Resilience** — **ถ้า process หนึ่ง fail ขึ้นมา process อื่น ๆ ยังช่วยให้งานดำเนินต่อได้**
- **ต้องมี Agreement ว่า "ระดับใด" ที่เรายอมให้ Process fail ได้** (ยอมรับได้กี่ตัว) ถ้า fail เกินระดับที่รองรับ ก็อาจต้องดาวน์ทั้งระบบ
- **นิยาม K fault tolerant:** ถ้าแบ่งระบบเป็น **K components** แล้วยังทำงานได้ตาม spec ที่กำหนด → ระบบนั้นมีระดับ **K fault tolerant**

### 4.1 ความหมายของ Failure 2 แบบ (สำคัญมาก)
- **Silence / Safe failure:** message **ไม่มีการส่งไปเลย = เงียบ** → กรณีนี้รองรับด้วย **K−1** (นับ silent เป็น 1 ตัว ยังมี process ที่ทำงานได้อยู่ K ตัว ตาม spec)
- **Arbitrary (Byzantine) failure:** ส่ง message **โกหกหลอก** เช่น ตอบ **Yes** แต่ที่จริงเป็น **No** (พูดไม่ตรงกับคำสั่ง) → ต้องใช้จำนวน process มากขึ้น
  - ใช้หลักคล้าย **Error Correction**: ต้องมี **2K + 1** จึงจะ **detect ได้** และ **correct ข้อผิดพลาดกลับมาให้ถูกต้องได้** แม้มีตัวหนึ่งโกหก
- **กรณี distributed system ที่ต้องกันไม่ให้คำสั่ง "No" ปนเข้ามา:** faulty node อาจเปลี่ยนคำตอบเป็น **No แทน Yes** ทำให้ process อื่นได้รับคำสั่ง No มากขึ้น → ต้องเพิ่มจำนวน component
  - **ต้องมีมากกว่า 3K + 1 (ประมาณ 3K+1)** เพื่อป้องกันไม่ให้คำสั่ง No กลายเป็นคำตัดสินที่ผิด

---

## 5. Byzantine Generals Problem (อาจารย์ออกเสียง "Bicentile/Bicentennial")
- ตั้งชื่อให้จำง่ายแบบ "นิยายประวัติศาสตร์" เหมือนกรีกโบราณ (เทียบกับ **Starving Philosophers** / Dining Philosophers ที่เป็น classic อีกเรื่อง)
- **เรื่องเล่า:** เราจะร้อง (บุก) ฆ่าศัตรู มี **4 กองทัพ / 4 Generals** วางแผน **โจมตีแคมป์ศัตรูพร้อมกันตอนเที่ยงคืน** เป็นข้อตกลง (General 1 กำหนดแล้วต้องสื่อสารให้ General 2, 3, 4 ด้วย ว่าจะโจมตีหรือไม่)
- ถ้ามี General ตัวหนึ่งเป็น faulty → **"Traitor" (ไส้ศึก)**: แทนที่จะออกคำสั่งโจมตี กลับ **หลอก General คนอื่นว่า "Don't Attack / Retreat (ถอยทัพ)"**
- ประเด็น: General แต่ละตัว **ไม่รู้ว่าคำสั่งที่ได้รับมาจากไหน ตัวไหนถูก ตัวไหนผิด** จึงต้องมีวิธีจัดการ
- **การแก้ด้วย Oral Message:** ให้แต่ละ node/general **ส่ง message ไปให้ general อื่นทุกตัวในแต่ละ cycle** (จำนวน 1 message)
  - ตัวอย่าง 4 Generals: สมมติ **1, 2, 4 เป็นฝ่ายโจมตี (loyal)**, **3 เป็น traitor**
  - ไล่ดูว่า node 1 ได้ค่าอะไรในแต่ละรอบ แล้วเอา message ทั้งหมดมา **majority** เพื่อ decide
  - พอถึงรอบสอง message จะถูกส่งซ้ำ (forward ต่อ) ระหว่างกัน พอรวมแล้วค่า message ควร **ตรงกัน** จึง majority ได้คำตอบ
- **กรณี 3 node (ไม่ถึง 3K+1): ล้มเหลว** — แสดงตัวอย่าง 3 nodes ซึ่ง "ทำได้ทุกอย่างเหมือนเดิม" แต่ **ตัดสินไม่ได้** ว่าค่าไหนถูก (เช่น 1 vs A, 2 vs B, Y vs C) → ยืนยันว่าจำนวน node ต้องเพียงพอ
- **Oral Message Algorithm (สรุป):**
  - ให้ **n = จำนวน node** (ที่สามารถ reach agreement ได้)
  - รับประกันว่า reach agreement ได้เมื่อ **n > 3m + 1** (m = จำนวน faulty node)
  - เงื่อนไข: **ทุก message ต้องส่งได้ถูกต้อง**, **receiver รู้ว่าใครเป็นผู้ส่ง**, และ **message ที่ขาดหาย detect ได้**
- **โมเดล Commander & Lieutenant:** เปลี่ยนมุมมองผู้ส่งเป็น **Commander** และผู้รับเป็น **Lieutenant (ลูกน้อง)** — ตั้ง node หนึ่งเป็น Commander ที่เหลือเป็น lieutenant ที่รับคำสั่งมาแล้วทำ algorithm
- **Recursion OM(m):** run ไล่ลงมา **OM(m), OM(m−1), …, OM(0)**
  - ถ้า **m = 1** → run 2 รอบ
  - ถ้า **m = 2** → run OM2, OM1, OM0 = 3 รอบ
  - ที่ระดับ OM0 → commander ส่งเสร็จ ก็ตัดทิ้ง/ไม่ต้องนับต่อ แล้ว restart ให้ lieutenant ตัวถัดไปเป็น commander วนซ้ำ

### 5.1 ตัวอย่างที่เฉลยละเอียด (สำคัญ)
- **ตัวอย่าง 4 node, traitor 1 ตัวที่ L3:**
  - ตั้งค่า A = "Attack" ที่ถูกต้อง (ส่งจาก software ที่ถูก)
  - L3 (traitor) เปลี่ยนจากค่าจริง (Attack) เป็น **Retreat (R)** = คำสั่งหลอก
  - L1 รับจาก commander = A, จาก L2 = A, จาก L3 = R → ได้ชุด **A A R** → majority = **A** (L1, L2 vote A; L3 ปล่อยช่างมัน) → สรุป **Attack**
- **Bad Commander (commander เองโกหก):**
  - เริ่มจาก **Single Error**: ให้มี R ส่งไปที่ L2 ตัวเดียว (L1, L3 ยังได้ A)
  - Commander ส่งให้ L1, L2, L3 → แล้ว L1/L2/L3 ต่างส่งต่อให้กัน (L1→L2,L3; L2→L1,L3; L3→L1,L2)
  - L2 เป็นตัวที่รับ R จาก commander แต่ L2 ยังปกติ → L2 จะส่ง R ต่อออกไป
  - โชคดีที่โครงสร้าง 3K+1 ทำให้ L1 รับค่ามาผสมกัน แล้วเลือกได้ว่าเป็น **A**; L2, L3 ก็เลือก A ได้เช่นกัน
  - **สรุป:** faulty จะเป็นที่ Commander หรือ Lieutenant ก็ **ป้องกันได้ ถ้าใช้ 3K+1**
- **Second Bad Lieutenant (2 faulty):**
  - ระบบมี **7 node**, มี **2 faulty (L5, L6)** ส่วน **commander ถูกต้อง (ไม่มี fault)**
  - L5, L6 ที่ level 2 **โกหก ส่ง R เข้ามา** → ปัญหายากขึ้น
  - อาจารย์บอก "ตัวที่ทำ commander ก็สำคัญ" — กรณีนี้โหดกว่าเพราะ faulty ตัวที่ทำ commander ส่งของมาเยอะ มี fault กระทบในรอบแรกมากกว่ารอบสอง
  - **ข้อสังเกตของอาจารย์:** ถ้า faulty ตอบไม่ตรงคำสั่งกระจายไปหมด (Attach/Retreat สลับกัน 1,3,5 = attack, 2,4 = retreat ฯลฯ) จะ **ตัดสินไม่ได้ (ลงกันไม่ได้)** → ย้ำว่า **จำนวน faulty + จำนวน node ต้องสัมพันธ์กับกฎ 3K+1**
  - ท่านบอกยัง **ไม่ได้ลงรายละเอียดครบ** ของกรณีนี้ (มีอีกหนึ่งระดับ/ซ้ำอีกรอบ) `[ไม่แน่ใจ: รายละเอียดเชิงตัวเลขของ second bad lieutenant]`

---

## 6. Check Yourself / การบ้าน (สัญญาณข้อสอบ)
- **โจทย์ "check yourself" ที่ให้ทำในคลาส:** Commander **ทำงานถูกต้อง**, มีทั้งหมด **7 process/node**, commander 1 ตัวสั่ง **Attack** ไปยัง lieutenant **5 ตัว** (ในนั้น **1 ตัว (สีแดง) เป็น traitor**) ส่วนอีก 4 ตัวปกติ
  - ให้ **เขียน Oral Message Algorithm** และสรุป **Decision Making** ว่า lieutenant เหล่านี้จะ **ตกลง (agree) ว่าโจมตี** ได้อย่างไร
  - วิธีคิดที่อาจารย์แนะ: เริ่มจาก **มี 1 faulty → error message จะมี 2 level** → ทำ **OM1** (commander ส่งให้ lieutenant ทุกตัว) แล้วทำ **OM0** (เลือก lieutenant หนึ่งตัวเป็น commander แล้วส่งต่อ) ไล่เป็นรูป
  - **ให้เวลาทำ ~10 นาที**
- **การบ้านที่ 3 / โจทย์ถัดไป:** ให้ทำ Oral Message แบบเดียวกับรูปที่เฉลย (สร้าง diagram) และแสดงคำตอบ
- **โจทย์ท้ายคลาส (ตรงกับที่อาจารย์จะอัปโหลดสไลด์ใหม่):** **Royal Commander ส่งคำสั่ง Attack ไปให้ 7 Lieutenant โดยใน 7 ตัวมี 5 loyal และ 2 traitor** → ให้ **ใช้ Oral Message Algorithm แสดงให้เห็นว่า loyal lieutenant ทั้ง 5 จะได้รับสารที่ถูกต้องและ follow คำสั่งของ commander ได้** → ให้อธิบายด้วย Oral Message ให้ละเอียด
  - เกณฑ์การจัดการจะ "เป็นตามที่เขียนไว้ด้านล่าง" ของสไลด์

---

## 7. BFT แบบ Practical (ลด Overhead)
- **จำนวน message ใน Oral Message โตแบบ exponent** ตาม m — จำนวน message ขึ้นกับ **ผลต่างของ m** และ **"order N"** ยิ่งมี traitor มาก ค่า N ยิ่งเพิ่ม → **ต้องหาวิธีแก้**
- **แนวคิด Practical BFT:** เลือก commander **ตัวเดียวเป็น Primary** (กำหนด index 0 เป็น primary) แล้ว **สมมติว่า primary ไม่มี fault** (fault ไปอยู่ที่ secondary)
- ตัวอย่างที่อาจารย์ไล่ (เหมือน **3-phase**): request เข้ามาที่ primary → primary ส่ง **prepare** ไปทุกตัว → แต่ละตัวส่ง message กลับ → ครบแล้วมี **commit** → ได้ค่า output
- **Optimization:** ฝั่ง replica **reply** — ถ้ามี m fault แล้วได้ **reply มากกว่า m+1 ตัวที่ตอบเหมือนกัน (same answer)** ก็ **จัดการได้/ตอบได้เลย** ไม่ต้องรอครบ
- สรุป: ทำให้ **practical กว่า** และ **ลด overhead** ได้
- **นิยามโดยรวมของ Byzantine Fault Tolerant:** เป็น solution ของ N ต่อจำนวน fault ที่ **fix** ไว้ — พอกำหนด fault ได้ m ตัว จะใช้หลัก **consensus** จัดการเพื่อได้คำตอบที่ถูกต้อง โดยใช้ **3m+1 nodes**
  - ข้อสังเกต: ในกรณีนี้มี **middle man (ตัวกลาง)** เข้ามาเกี่ยวข้อง
  - ถ้า **เพิ่มจำนวน node เรื่อย ๆ** → **ทน fault ได้มากขึ้น (resilient ขึ้น)** แต่ **consensus ก็ใหญ่ขึ้น + ค่าใช้จ่าย computing สูงขึ้น** → ความถูกต้องสูงขึ้นแลกกับต้นทุนที่เพิ่มขึ้น

---

## 8. ตัวอย่าง Blockchain / Distributed Ledger
- เรา "สร้าง block" ไปเรื่อย ๆ แล้วพบว่ามี **block หนึ่งถูก attack** — ตัวอย่างคือ **block ที่ 74** ตอนนี้มี block ทั้งหมด **90 (91 ด้วยซ้ำ กำลังสร้างอยู่)**
- ตัวที่เข้ามาเป็น attack ต้อง "สร้าง" ใหม่: message ตั้งแต่ **block 74 ถึง 90** → **ค่าใช้จ่าย computing สูงมาก** ที่จะแปลง message ปลอมให้กลายเป็น message ถูกต้อง เพราะต้องผ่าน **consensus**
- ตัวอย่างเชิงเวลาที่อาจารย์ยก: กำหนดจะโจมตีตอน **บ่ายโมง** แล้วบอกทุกคน ส่งเป็น block; มี **traitor 1 block ที่แปลง 7 โมงเช้า** ให้เปลี่ยนเป็นบ่ายโมง… `[ไม่แน่ใจ: ตัวอย่างนี้ transcript เพี้ยนมาก — ใจความคือ block ที่ถูกแก้ให้ผิดจะถูก consensus ตรวจไม่ผ่าน]`
- อาจารย์ย้ำว่าวันนี้ **อธิบาย blockchain ส่วนนี้ได้ไม่ค่อยดี + ไม่ค่อยมีตัวอย่าง** `[ไม่แน่ใจ: เนื้อหาส่วน blockchain]`

---

## 9. Client–Server Communication & Failure Models
- กลุ่มนี้เป็นมุมมอง **server ทั่วไป** มีปัญหา **communication failure** และ **crash failure / omission failure** (server crash ไม่ตอบสนอง)
- ต้องการทำ communication แบบ **point-to-point** เช่น **TCP**
- **Model ความล้มเหลวที่ต้องเตรียมรับ (อาจารย์ไล่ทีละกรณี):**
  1. client ไม่สามารถ **locate server ได้** (server down / server เปลี่ยน)
  2. **client request หายไป**
  3. **server crash**
  4. **server reply หายไป**
  5. **client crash** หลังจากส่ง request ไปแล้ว

### 9.1 วิธีป้องกันแต่ละกรณี (คำอธิบายของอาจารย์)
- **Normal case:** request เข้ามา → server reply กลับ
- **ถ้ามี crash หลัง execute หรือก่อน execute** → จะ **ไม่มี reply** ออกมา
- **client locate server ไม่ได้** (server down/change) → ใช้ **exception handler** เข้าสู่ exception แล้ว **run ซ้ำ**
- **request to server หายไป (lost)** → ใช้ **timeout** (เหมือน exception) แล้ว **resend**; มีกลไก **multiple request** รองรับ
- **server crash** → ต้องดูว่า crash **ตอนไหน (ก่อน/หลัง execute)** แล้ว **สร้าง server ใหม่** ให้ client request เข้ามาใหม่; หรือถ้าไม่ไหวก็ใช้ **Fail-Safe** = ยอมแพ้ (ขึ้นกับว่าระบบรองรับ redundancy ระดับไหน)
- **server reply หายไป (loss)** → ให้ client **request กลับมาอีกที**
- **client crash หลังส่ง request** → เป็น **idempotent request** `[ไม่แน่ใจ: ท่านพูดคำที่ฟังคล้าย "offense request" — น่าจะหมายถึง idempotent]` ทำใหม่/ทำซ้ำ แล้วแต่โมเดล
- **สรุป:** ในแต่ละโมเดลสามารถสร้าง **Reliable Communication** ได้
- **Synchronous Communication** = ใช้ **Time Out** (ตั้งเวลา; ถ้าถึงเวลาแล้วยังไม่ครบ/ไม่มา = Time Out → rerun / recover) หลักการเดียวกับ message ที่หาย
- ถ้าต้องการให้ **message ส่งได้ถูกต้อง** → ใช้ **BFT** และ **เพิ่ม node ให้มากกว่า 3K+1** เพื่อรองรับ K fault
- ถ้ารู้ว่าไม่สำเร็จ ต้องดูว่า **ใครเป็นผู้ส่ง**, ดู **Switching Network** ว่าถูก set อย่างไร
- เรื่อง **Signature / Authenticity** → ใช้ **Cryptography** ในการเข้ารหัส เพื่อให้รู้ว่า signature เป็นของใครจริง

---

## 10. จุดที่อาจารย์เน้น / สัญญาณเกี่ยวกับข้อสอบ
- **3K+1 และ 2K+1 เป็นสูตรที่ต้องใช้บ่อย** — ใช้ตอบคำถามจำนวน node ที่ต้องมีในระบบที่มี faulty m ตัว (oral message, BFT, client-server ที่ต้องส่ง message ถูกต้อง)
- **ข้อสอบ/การบ้านจะให้ "เขียน Oral Message Algorithm + แสดง decision agreement"** โดยเฉพาะโจทย์ **Commander + 5 lieutenant, 1 traitor** และโจทย์ **Royal Commander + 7 lieutenant, 5 loyal 2 traitor**
- อาจารย์จะ **อัปโหลดสไลด์ชุดใหม่ (รวมโจทย์ check yourself)** ให้อีกที
- **นิยามที่ต้องจำ:** Resilience, K fault tolerant, safe(silent) failure vs arbitrary failure, OM(m) recursion, เงื่อนไข n > 3m+1
- ตัวอย่าง (4 node / 3 node / bad commander / second bad lieutenant) เป็น **แนวที่โจทย์จะออก** — ต้องวาดรูป communication แล้วหา majority ได้

---

## 11. คำ/ชื่อที่ transcript เพี้ยน (เพื่อความเข้าใจ)
- "Bicentile / Bicentennial Fall Tolerance" = **Byzantine Fault Tolerance**
- "Bicentile Scenario/General Problem" = **Byzantine Generals Problem**
- "Consent" = **Consensus**
- "SafeNag Failure" = **Safe / silencing (silent) failure**
- "Auromessage / Oral Message" = **Oral Message Algorithm**
- "commission failure" = `[ไม่แน่ใจ: น่าจะเป็น omission failure]`
- "VFT" = `[ไม่แน่ใจ: BFT]`

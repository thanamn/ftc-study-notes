# บทที่ 3 — FTC03 Byzantine Fault Tolerance (ฉบับย่อ)

## Process group

**Process group** = กลุ่มที่สมาชิกทุกตัวได้รับ message ที่ส่งเข้ากลุ่ม ถ้าตัวหนึ่งพังตัวอื่นรับงานแทนได้ กลุ่มเป็น dynamic ได้ **Flat group** (ทุกตัวเท่ากัน) = ไม่มี single point of failure แต่ตัดสินใจซับซ้อน **Hierarchical group** (มี coordinator) = ตัดสินใจเร็ว แต่ถ้าตัวแม่เสียก็เสียทั้งกลุ่ม

ทำไมต้องเรียน: ระบบ process เดียวทำ fault tolerance ง่าย (แค่เพิ่ม reliability) แต่ระบบกระจายมี process เยอะจน *coding ทุก message สิ้นเปลือง* จึงต้องอาศัย agreement/consensus ตรวจว่า message ไหนจริง เพื่อไม่ให้เสียงผิดกลายเป็นคำตัดสิน และลบคนกลางด้วย distributed ledger (blockchain)

## กฎจำนวน process

ระบบเป็น **k fault tolerant** ถ้าทน fault ของ k component แล้วยังทำตาม spec ได้
- **safe/silent failure** (หยุดเงียบ) → ต้อง **k+1**
- **arbitrary (Byzantine) failure** (ตอบอะไรก็ได้) → ต้อง **2k+1** (เพราะ k ตัวที่พังอาจบังเอิญให้ผลผิดตรงกัน)
- faulty **สมคบกัน** (collude) → ต้อง **3k+1** ซึ่งในนั้น **2k+1** ทำงานถูก

ทั้งหมดสมมติว่าไม่มีความผิดพลาดในการสื่อสาร

## Byzantine Generals

เรื่องเล่า: นายพลต้องตกลงบุกหรือถอย มี messenger และมีกบฏที่โกหกและส่ง message ขัดแย้งกันได้ **3 ซื่อสัตย์ + 1 กบฏ (n=4, m=1):** แต่ละคนส่งค่า แล้วส่งต่อสิ่งที่ได้ แล้วโหวตเสียงข้างมากแต่ละคอลัมน์ → ได้ผล กบฏปรากฏชัด **2 ซื่อสัตย์ + 1 กบฏ (n=3):** ล้มเหลว = **two-army problem** กฎ: ต้องมี **> 2/3** ทำงานถูก ถ้ามี M faulty ต้องมี **2M+1** ทำงาน

## Oral Message algorithm และ n ≥ 3m+1

บรรลุข้อตกลงได้ก็ต่อเมื่อ **n ≥ 3m+1** (n = จำนวน node รวม, m = กบฏ → ซื่อสัตย์ 2m+1 ตัว) **สมมติฐาน 3 ข้อ:** ทุก message ส่งถึงถูกต้อง; ผู้รับรู้ว่าใครส่ง; ตรวจการไม่มี message ได้

**OM(0):** commander ส่งค่าให้ lieutenant ทุกคน; แต่ละคนใช้ค่าที่ได้ หรือ "retreat" ถ้าไม่ได้
**OM(m) (m>0):** commander ส่งค่า → ทุกคนรัน OM(m−1) ในบทบาท commander ส่งค่าที่ได้ต่อ → แต่ละคนใช้เสียงข้างมาก (จำนวนรอบ = m+1)

**ตัวอย่างที่ต้องทำได้:**
- **Bad lieutenant (m=1, n=4, กบฏ L3):** commander ส่ง A; รอบส่งต่อ L1/L2/L4 ส่ง A, L3 ส่ง R → lieutenant ซื่อสัตย์เห็นเสียงข้างมาก A
- **Bad commander (m=1, n=4):** commander ส่ง A ให้ L1, R ให้ L2, A ให้ L3 → เสียงข้างมากออกมา A; ประเด็นคือ commander กบฏทำให้ **agree บนค่าผิด** ได้ แต่ทำให้ lieutenant ซื่อสัตย์ **ขัดแย้งกันเอง** ไม่ได้
- **m=2, n=7 (กบฏ L5,L6):** ตรงกับข้อสอบเก่า — commander ส่ง A; OM(1) ทุกคนเป็น commander; OM(0) ทุกคนส่งต่อ; ตารางสุดท้าย lieutenant ซื่อสัตย์ L1–L5 ทุกแถวได้เสียงข้างมาก A (คอลัมน์กบฏ = X)

**บทเรียนสำคัญ:** ถ้าจำนวนรอบไม่พอ (เช่นหยุดที่ OM(1)) commander ที่โกหกบวกกบฏจะพลิกเสียงข้างมาก ทำให้ lieutenant ซื่อสัตย์เลือกไม่ตรงกัน (L1 attack, L2 retreat) จึงต้องรันถึง OM(0) เพื่อ verify ว่าทุกคนบอกคนอื่นว่าอะไร จำนวนรอบ m+1 จึงจำเป็น ไม่ใช่ทางเลือก

**จำนวน message** = (n−1)(n−2)…(n−m−1) = **O(n^m)** โตแบบ exponential ในจำนวนกบฏ จึงต้องมี **practical BFT** (client รอคำตอบ m+1 จาก replica ที่ตรงกัน; ถ้า primary ผิดเลือกใหม่) และ **signed messages** (ลายเซ็นปลอมไม่ได้ → ประหยัดกว่า)

## Blockchain

เป็นคำตอบของ BFT ที่ลบคนกลางแต่ยังแลกเปลี่ยนอย่างเชื่อถือได้ (decentralised, self-governing) อาศัย **proof of work / proof of stake** ถ้าใครอยากแก้บล็อกเก่า ต้องคำนวณใหม่ทุกบล็อกตั้งแต่จุดนั้นถึงปัจจุบัน และต้องทำเสร็จก่อนเครือข่ายทำบล็อกปัจจุบันเสร็จ ซึ่งแพงมาก (นี่คือแนวคิด blockchain)

## Reliable client-server communication

TCP กลบ omission failure ด้วย ACK + retransmission แต่ทำงานแย่เมื่อเกิด crash **ห้าสถานการณ์ที่ต้องจัดการ:**
1. client หา server ไม่เจอ → exception handler
2. client request หาย → timeout แล้วส่งซ้ำ (ระวัง **idempotent operation**)
3. server crash หลังรับ request → ไม่รู้ว่าทำไปหรือยัง → สร้างใหม่+retry (at-least-once) หรือยอมแพ้ (at-most-once); ที่ต้องการจริงคือ **exactly-once** แต่การันตียาก
4. server reply หาย → ตั้ง timer ถ้าไม่ตอบถือว่า server ล่ม/request หาย
5. client crash หลังส่ง request → เหลือ **orphan request**; ทางเลือก: **Extermination**, **Reincarnation** (แบ่งเป็น epoch), **Gentle reincarnation**, **Expiration**

**สมมติฐาน reliable communication:** synchronous; ตรวจการไม่มี message ได้; ทุก message ส่งถึง; ผู้รับรู้ผู้ส่ง; ลายเซ็นปลอมไม่ได้/แก้ไขตรวจได้/ใครก็ยืนยันได้

## จุดเชื่อมกับข้อสอบเก่า

โจทย์ที่อาจารย์ให้ทำคือเขียน Oral Message แล้วสรุปการตัดสินใจ ด้วยสองกรณี: commander ซื่อสัตย์ + lieutenant 5 ตัว (traitor 1) และ **royal commander + lieutenant 7 ตัว (loyal 5, traitor 2)** ให้แสดงว่า loyal lieutenant ได้สารถูกต้องและทำตามคำสั่ง เกณฑ์ที่ใช้ตอบคือ n ≥ 3m+1 (สำหรับข้อสอบเก่า n=7, m=2 → 7 ≥ 7 ผ่าน) โดยวาดรอบ OM(2)/OM(1)/OM(0) แล้วลงตาราง vector + คอลัมน์เสียงข้างมาก

## ต้องจำทันที และกับดัก

**จำทันที:** k+1 (silent), 2k+1 (arbitrary), 3k+1 (colluding); n ≥ 3m+1; ขั้น OM(0)/OM(m); message โตเป็น n^m; สถานการณ์ client-server 5 แบบ

**กับดัก:** อย่าสลับ "n ≥ 3m+1 node รวม" กับ "2m+1 node ซื่อสัตย์" (เทียบเท่ากัน); Oral Message สมมติ synchronous + ตรวจจับการไม่มี message ได้; two-army คือ n=3, m=1 ที่เพิ่งล้มเหลว; คำตอบลอย ๆ ว่า "ทุกคนโหวต" โดยไม่บรรยายรอบส่งต่อจะเสียคะแนน

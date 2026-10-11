# FTC06 — Self-Checking Circuits: สิ่งที่อาจารย์อธิบายเพิ่ม (จาก transcript)

> ที่มา: `transcripts/FTC06.md` (Thai ASR, 107 นาที)
> โน้ตนี้เก็บ "คำอธิบายของอาจารย์" — intuition, การไล่เหตุผล, ตัวอย่างที่ทำให้ดู, สิ่งที่เน้น, hint ข้อสอบ
> ไม่ได้ทวน bullet บนสไลด์ · จุดที่เสียงเพี้ยนจะกำกับด้วย `[ไม่แน่ใจ: ...]`

---

## 0. การบริหารคลาส + hint ข้อสอบ (ช่วงท้ายก่อนเข้าเนื้อหา และท้ายคาบ)

- **กำหนดการสอบ**: สัปดาห์หน้าคณะมีสอบ จึง **ไม่มีคลาสวันที่ 28**; "ครั้งที่ 7" ยังมีเรียนตามแผน; **วันที่ 5 กันไว้เป็นรีวิว** (ถ้าสอนทันก็ไม่มีอะไรในวันนั้น); **วันที่ 12 จัด Mid-Term**
  `[ไม่แน่ใจ: ลำดับวัน/ครั้งที่พูดตอนต้นคาบ]`
- **เนื้อหา Mid-Term ครอบคลุม FTC01–FTC07** (Fault Tolerant Computing)
- **เวลาสอบ**: ไม่ได้เริ่มบ่ายโมง แต่เป็น **13:00–16:00**; นักศึกษาเยอะจึงจองไว้ **2 ห้อง** `[ไม่แน่ใจ: "ชั้น 4 / 1701 / ชั้น 18"]`; **เป็น open book ทั้งหมด**; อาจารย์จะแบ่งกลุ่มให้
- หลัง Mid-Term จะเข้าเรื่อง **Testing Digital Circuit ประมาณ 4 ครั้ง + รีวิวอีกครั้งก่อน Final**
- คาบนี้มี **แบบฝึกหัด** และมี **การบ้าน** (ดู §13)
- **Hint ลักษณะโจทย์** (ตอนไล่ตาราง fault/ST): โจทย์แนวที่อาจารย์ยกคือ "ถามว่า self-testing มีอันไหนบ้าง, fault-secure มีอะไรบ้าง, undetectable fault เป็นยังไง" — พร้อมบอกว่า **"ปกติผมไม่ได้หมุนเยอะ"** (คือโจทย์แนวนี้ไม่ยาก/ไม่ออกเยอะ)
- **คำแนะนำวิธีทำ**: ถ้าโจทย์ไม่ยาก ให้ **"เจนด้วยเบอร์ก่อน"** คือทำตาราง (truth table / state) ให้ครบก่อน แล้วค่อยวิเคราะห์

---

## 1. ทบทวน Coding Theory — ตัวอย่าง cyclic code ที่อาจารย์ไล่ให้ดู

- โจทย์: สร้าง **cyclic code** ของ data (ให้ดูในกระดาษที่แจก) — เคส **(7,4)**: data 4 bit, n = 7, k = 4 ⇒ ต้องมี **check/parity bit n − k = 3 ตัว**
- เลือก **generator polynomial g(x) = x³ + x + 1**
- **Encode**: เอา data คูณกับ g(x); ป้อน data แบบ **MSB (high bit) ก่อน**; ฮาร์ดแวร์ทำตามสมการที่ได้จาก g(x) โดยใช้ **D flip-flop / shift register** — มีการ XOR ที่ตำแหน่ง tap ต่าง ๆ `[ไม่แน่ใจ: ตำแหน่ง tap ที่อาจารย์อ่าน ("หลักที่ 0 กับหลักที่ 2 ... หลักที่ 3")]`; ตัวอย่าง data หนึ่งตัวที่ยกคือ **0101** และรหัสที่ได้อาจารย์อ่านว่า **01011…** `[ไม่แน่ใจ: ค่า codeword]`
- **Decode/ตรวจ**: เอาค่าที่ได้ **หารด้วย g(x) อีกที** — ถ้า **remainder = 0** แสดงว่า code ที่ได้เป็น data ที่ถูกต้อง (แนวคิด divisor/remainder นี้ใช้เช็ค error ได้)
- **เคสมี error**: สมมติมี **1 bit ผิด (ตัวสีแดง)** แล้วลองหาร ⇒ **remainder ไม่เป็น 0** (อาจารย์อ่านว่า **1001**) ⇒ แปลว่าไม่ตรงสมการ = มี error และพอ decode ออกมาก็ได้ค่าที่ผิดไปด้วย
- สรุปที่อาจารย์เน้น: ใช้หลักการของ **error checking ผ่าน code** (encode → ตรวจด้วยการหาร/parity) เป็นฐานก่อนเข้าเรื่อง self-checking circuit

---

## 2. ประเภทของ error ที่อาจารย์อธิบาย

- ในระบบดิจิทัลมี error ได้หลายแบบ แบ่งเป็น **symmetric / asymmetric**; ถ้าไม่ symmetric ก็เป็น **asymmetric**
- **Single error** — คุม/แก้ได้ง่ายกว่า
- **Multiple error** — ยากกว่า และทำให้จำนวน bit ที่ต้องใช้มากขึ้น
- **Unidirectional error** — error ทุกตัว **ไปทิศทางเดียวกัน** (0→1 ทั้งหมด หรือ 1→0 ทั้งหมด) อาจเป็น single หรือ multiple ก็ได้
  - อาจารย์เน้นว่า unidirectional error เป็น **model ที่ "ใช้งานได้จริง" และคลุมกว้าง** — รองรับทั้ง single error และ multiple error
  - แหล่งที่มา/สาเหตุที่อาจารย์ยก: **noise / สัญญาณรบกวน, การทำงานที่มีคลื่นกวน**, **fiber optic ที่มี transition ผิดพลาด** (ไฟเบอร์บางทีสัญญาณดรอป/เปลี่ยนค่า), ฮาร์ดแวร์แตกระหว่างทำงาน ⇒ กลายเป็น multiple error ได้
- **Error control**: ถ้าอยู่ในขอบเขตที่แก้ได้ ก็ correct/control แล้วปล่อยผ่าน; ถ้าเกินขีดความสามารถของ code ให้มี **error signal** ส่งออกไปบอกว่าแก้ไม่ได้ (fault ที่ผิด) — เกี่ยวกับแนวคิด **false masking**

---

## 3. ECC / ภาพรวม Error Control Code

- ตัวอย่าง **ECC**: data เข้ามา → ส่วนที่สร้างรหัส (function) → เก็บลง memory **เป็น Separate Code** คือ code/check bit แยกจาก data bit ชัดเจน
- ตอนดึง data ออก: เอา m มาผ่าน function อีกที แล้ว **compare k ที่คำนวณใหม่ กับ k ที่เก็บไว้ (recompute + compare)**
  - ตรง ⇒ ส่งค่าออกไปเลย
  - ไม่ตรง และ **อยู่ในวิสัยที่แก้ได้** ⇒ ค่าที่ต่างบอก **ตำแหน่ง bit ที่ผิด** → **flip bit นั้น** (0→1 หรือ 1→0) แล้วจึงส่ง data ออก
  - ถ้าแก้ไม่ได้ ⇒ **ส่ง error signal** ออกไป
- **Overlap Parity Code**: ใช้ **parity ซ้อนกันหลายชั้น** จนสามารถ **locate ตำแหน่ง error** ได้ แล้ว flip กลับเป็นค่าปกติ ⇒ correct ได้ทันที (เพราะมีตัวอย่าง binary)
- **Level ของความสามารถ**: บาง code ไปได้แค่ **Detect** (รู้ว่ามี error แต่ไม่บอก bit ไหน); บางตัว **Correct** ได้
- Code ที่เอามาใช้จริงตามที่อาจารย์ไล่: **Overlap Parity, Checksum, Residue, Unordered, Constant Weight, Berger** `[ไม่แน่ใจ: ชื่อบางตัวที่อาจารย์อ่านเพี้ยน]`

---

## 4. Hamming Code — ตัวอย่างที่อาจารย์ไล่เอง (สำคัญ)

- data **8 bit** → ต้องสร้าง check bit; **check bit อยู่ที่ตำแหน่ง 1, 2, 4, …** (กำลังของ 2)
- เงื่อนไขจำนวน check bit: **2^k ≥ m + k + 1** (Hamming bound) `[ไม่แน่ใจ: transcript อ่านเพี้ยน แต่บริบทคือสูตรนี้]`
- **ความสำคัญ (priority) ของตำแหน่ง check bit** ใช้บอกว่าผิดที่ bit ไหน
- อาจารย์ไล่ **"data bit ตัวไหนทำให้ check bit ตัวหนึ่งเป็น 1"**:
  - **C1** มาจาก **D1, D2, D4, D5, D7**
  - **C2** มาจาก **D1, D3, D4, D6, D7**
  - (C4 มาจากกลุ่มอื่นที่ต่อเนื่องกัน) `[ไม่แน่ใจ: กลุ่มของ C4]`
  - ⇒ เขียนเป็นสมการ parity แล้ว C1 = XOR ของกลุ่มนั้น `[ไม่แน่ใจ: รายละเอียดสมการ]`
- **ตัวอย่างที่ไล่**: data ตัวอย่าง (อ่านว่า 11001) ⇒ check bit ที่คำนวณได้ (อ่านว่า 110) ถูกเก็บไว้; **เมื่อ bit ใน memory ถูก flip** แล้ว recompute ใหม่ ⇒ ได้ค่า **syndrome = 1100** ซึ่ง **เท่ากับตำแหน่ง bit ที่เสีย** (bit position) ⇒ รู้ว่าผิดที่ตำแหน่งนั้น แล้วไป **flip** กลับ ⇒ แก้ได้
- **Venn Diagram (3 วง A, B, C)** ใช้วิเคราะห์ได้ และเข้าใจง่ายกว่าสำหรับ correcting code:
  - data bit อยู่ **ข้างใน** วง, check bit อยู่ **ข้างนอก** วง (โซน ABC)
  - ทำให้แต่ละวงมี parity (จำนวน 1) ให้เป็น 0
  - พอเกิด error: จะมี **2 วงที่ parity ผิด** (วงที่ตัดผ่าน bit นั้น) ⇒ **cross กัน** หา **location** ของ bit ที่เสีย ⇒ flip กลับ
- **Multiple error** ⇒ ใช้แนวคิด **BCS / cyclic error-correcting code** (สร้างโค้ดด้วยหลักของ cyclic) `[ไม่แน่ใจ: ชื่อ code ที่อาจารย์พูด — ฟังคล้าย "BCS"/"BCH"]`; ข้อดีคือ correct ได้ แต่ซับซ้อนกว่า และมีค่าใช้จ่ายสูง

---

## 5. Checksum

- หลักการ: เอา **data มาบวก/รวมกัน** เก็บค่าไว้เป็น **checksum**; ตอนใช้งานให้รวม data ใหม่แล้ว **compare** กับค่าเดิม — ถ้าไม่ตรง ⇒ detect error ได้
- เป็น **Separable Code** (data กับ check bit แยกกันชัดเจน) และมี **error detection capability**
- ชนิดที่อาจารย์ไล่: **single precision / double precision / residue checksum / honeywell checksum** (`[ไม่แน่ใจ: บางชื่ออ่านเพี้ยน]`)
  - **Single precision**: รวม data หลายตัว (ตัวอย่าง 4 ตัว) ได้ค่า checksum ตัวเดียว
  - **Double/2 รอบ**: ทำซ้ำ/ขยายวงเพื่อลดโอกาสที่ **error ถูก "กลืน"** (mask) — ทำให้แม่นขึ้น
  - **Residue checksum** = **end-around carry addition**: bit ทด (carry) จากตำแหน่งสูงสุด **วนกลับไปบวกที่ตำแหน่งต่ำสุด** (เหมือน one's complement)
  - **Honeywell** = **pair checksum**: จับ data เป็นคู่ ๆ รวมกันก่อน แล้วค่อยทำ checksum

---

## 6. Constant Weight Code + Arithmetic Weight

- **Constant Weight Code** — เป็น (ในบริบทนี้) แบบ **Non-separable**; **weight = จำนวน bit ที่เป็น 1** และถูก **fix** ให้คงที่ เช่น weight 2 ⇒ codeword ทุกตัวมี 1 อยู่ 2 ตัว
- **ข้อดีที่อาจารย์เน้น**: ตรวจได้ **error ที่เป็น unidirectional หมดเลย** (detect ได้ทุกกรณี)
- จำนวนคำรหัสอยู่ในระดับ **~ n เลือก 2 (C(n,2))** ⇒ **วงจรไม่ใหญ่เกินไป**
- **Arithmetic Weight** — ตัวอย่างที่อาจารย์ยกต่อ: ผลรวมแบบมีการทด (carry) ค่าที่คลาดเคลื่อนจะโผล่ออกมาในรูปค่า error

---

## 7. Residue Code + Low-Cost Residue (ALU)

- **หลักคิด**: เก็บค่า **n mod A** (residue) ไว้เทียบ
- เหตุผลที่ต้องมี residue code: เวลาทำงานกับ **ALU** ควรใช้ code ที่ **"conservative"/รักษาสมบัติ (preserve) ผ่าน operation** ได้ — โค้ดแบบก่อนหน้า (non-separable/residue บางแบบ) **ไม่รักษาคุณสมบัติเมื่อผ่าน operation**; residue code ทำได้ (บวก/ดำเนินการแล้วค่า residue ยังสัมพันธ์กัน)
- **Low-cost residue**:
  - เลือก **A = 2^b − 1** (เช่น **mod 15 = 2⁴ − 1**) เพื่อ **ไม่ต้องใช้ division จริง** — ทำได้ด้วย **end-around carry addition**
  - อาจารย์ไล่ตัวอย่างการบวกทีละคู่: 001 + 1101, 001 + 1010, แล้ว + 110 ⇒ ได้ **final residue**
  - อาจารย์เน้นว่า **สร้างง่าย** และใช้ **จำนวน bit น้อย** ("7 ออกมา 3 bit")
- **Modular**: ถ้า a mod b = ... `[ไม่แน่ใจ: ตัวอย่าง 110 + 100 / ค่า 6 ที่อาจารย์พูด]` — จุดสำคัญคือ **ไม่ต้องสร้างฮาร์ดแวร์เพิ่ม** ใช้ bit เดิมที่มีอยู่มา generate code ได้ ⇒ เป็น **low-cost**
- ฝั่งตรวจ: เอา data ไปทำ mod แล้วเทียบกับ residue ที่เก็บไว้

---

## 8. Unordered Code

- **Order (การเรียง)**: ถ้า data สองตัวต่างกันแค่ **1 bit** (bit อื่นเท่ากัน) ถือว่ามี "order" ระหว่างกัน
- **Unordered Code** = code ที่ **ไม่มี codeword ตัวหนึ่งที่ "ใหญ่กว่า/ครอบ" อีกตัวในเชิง bitwise** — ไม่มีลำดับ
- **ประโยชน์ที่อาจารย์อธิบาย**: กันปัญหาว่า data ที่ผิด (มี bit เปลี่ยน) ไป **ถูกเข้าใจผิดว่าเป็น codeword อีกตัวที่ถูกต้อง** — ถ้า codeword ถูก encode ถูกต้อง จะไม่กลายไปเป็น codeword อื่น
  - ตัวอย่างที่ยก: ใช้ codeword แบบ 0011 / 1100 (ค่าที่ป้อนมา) และประเด็นว่า data ที่เข้ามา **ยังไม่ต้องแปลง** แต่ให้ดูว่าโอกาสกลายเป็น codeword อื่นมีไหม `[ไม่แน่ใจ: รายละเอียดตัวอย่างที่อ่านไม่ชัด]`
- **Constant Weight Code เป็น unordered code**; **Berger code เป็น unordered code** (Hamming distance ≈ 2)

---

## 9. Dual-Rail / Inverter-Free Code และการประยุกต์

- **Dual-rail**: ทุกเส้นมีทั้ง **x และ x′** (ใช้ inverter แปลง); เวลาสร้างฟังก์ชันจะใช้ gate ที่ไม่ใช่ inverter (เช่น NOR/NAND) เพื่อทำ operation แล้วผลลัพธ์อยู่ในรูป **dual-rail**
- **จุดสำคัญที่อาจารย์เน้นมาก**:
  - วงจร dual-rail จะ **ไม่มี Inverter (NOT)** ปรากฏในวงจรที่สร้างจริง
  - ⇒ **error ที่เกิดขึ้นจะเป็น unidirectional** ⇒ สามารถทำ **error detection** ได้ (แม้ multiple error ที่ทิศทางเดียวกัน)
  - ⇒ ได้คุณสมบัติ **fault-secure / preserve code** และ **easy to implement (encode/decode ง่าย)**
  - เปลี่ยน **single line → คู่เส้น**; เป็นแนวทางที่ cost พอรับได้และดีพอสมควร
- ตัวอย่างที่อาจารย์ไล่: ฟังก์ชัน `f = a·b + b·c + … (มี a b c)` `[ไม่แน่ใจ: พจน์ของฟังก์ชัน]` แล้วหา **f̄** เพื่อสร้าง dual circuit
- **การประยุกต์ที่อาจารย์ยก (ที่ไม่ใช่แค่ทฤษฎี)**:
  - **Checksum ใน barcode** — ตัวอย่างคือ **UPC-A check digit** ใช้ **modulo 10** และมี pattern/weight กำกับ (เช่นคูณน้ำหนักสลับตำแหน่ง); `[ไม่แน่ใจ: เลข 12/7/14/58 ที่อ่านมาประกอบตัวอย่าง]`
  - **Huffman code** → ลด resolution แล้ว **reconstruct กลับมาให้ใกล้ original** โดยใช้ code ที่ tolerates error ได้ ⇒ **image compression + error detection/correction**: ยิ่ง code ทนต่อการผิดพลาดสมบูรณ์ พอ reconstruct รูปก็ยิ่งเข้าใกล้ original

---

## 10. Self-Checking Circuits — แก่นที่อาจารย์ปู (Concept)

- บริบท: เราอยากให้ระบบ **ตรวจ fault ของตัวเองได้ (online)** ไม่ต้องรอ input จากภายนอก
- แยก **Code Word vs Non-Code Word**:
  - **Code word** = data ที่ถูกเข้ารหัสและถูกใช้งานจริง
  - **Non-code word** = ค่าที่ไม่ได้ใช้งาน
  - ตอนแสดงผล **ต้อง preserve code word ไว้**; ถ้าผลออกมาเป็น **non-code word** แสดงว่าผิด ⇒ ถ้าตรวจได้ทันที = **self-checking**
- คุณสมบัติที่ทำให้ self-checking ได้มี **2 ตัว**: **fault secure** และ **self-testing**
- **Fault Secure (FS)**: ถึงแม้เกิด fault ในกลุ่มที่กำหนด ค่าที่ได้จาก input set ที่ป้อน **ยังแสดง output ปกติ ไม่เป็น output ที่ผิด** (ไม่กลายเป็น erroneous codeword)
- **Self-Testing (ST)**: สำหรับ fault แต่ละตัว **ต้องมี input อย่างน้อย 1 ตัว** ที่ทำให้ output ออกมาเป็น **non-code word** ⇒ เอาไว้ detect/test ได้
- **TSC (Totally Self-Checking)** = มีทั้ง **ST + FS** อยู่ในตัว ⇒ เป็น ideal property
- **สิ่งที่ตรวจไม่ได้**: อาจารย์ย้ำว่า **ไม่ใช่ทุก fault ที่ code จะ detect ได้** — fault ที่ detect ไม่ได้มีอยู่ใน literature
- **ทำไม FS ต้องคู่กับ ST**: ถ้า FS แต่ตรวจไม่ทันที fault ตัวถัดไปอาจทำให้ FS **สูญเสียไป** ได้ ⇒ จึงต้องมี ST เพื่อให้ **จับได้เร็วที่สุด** ก่อนโอกาสที่ fault ใหม่จะเกิด

### 10.1 Strongly Fault Secure (SFS) / คุณสมบัติที่เกี่ยวข้อง `[ไม่แน่ใจ: ชื่อเรียกหลายตัวฟังเพี้ยน]`

- แนวคิด **SFS**: ถ้าเกิด fault แล้ว **ตราบใดที่ไม่เกิด fault ใหม่** output จะยังเป็น code word ที่ถูกต้อง หรือ non-code word (คือ **ไม่กลายเป็น code word ที่ผิด**) — พอ fault ใหม่เพิ่มขึ้น เซตความครอบคลุมก็ยังคงอยู่ (fault set ขยายเป็น f ∪ f′ ต่อไปเรื่อย ๆ) จนกว่าจะมี fault ที่ทำให้ output เป็น non-codeword ⇒ ตรวจได้ ⇒ นี่คือลักษณะของ **strongly fault secure**
- **Code Disjoint** (คุณสมบัติของ **checker**): checker ต้องแยกได้ว่า input เป็น code word หรือ non-code word; ถ้า input เข้ามาเป็น **non-code word** จะต้องออกมาเป็น **non-code word (abnormal)** — **ห้ามกลับไปเป็น code word** ⇒ ทำให้ detect ได้
- **Error Preserving**: erroneous (non-code word) input จะให้ non-code word output; code word input ให้ code word output ที่ถูกต้อง (ไม่กลับไปเป็น code word ผิด)
- กรณีของ **circuit (ไม่ใช่ checker)**: ไม่ว่าจะป้อน code word หรือ non-code word เข้าไป output จะเป็น code word ที่ถูกต้อง หรือ non-code word — **ไม่มีทางกลับไปที่ code word** ⇒ เรียกลักษณะเดียวกันนี้ได้
- ถ้า **self-test ไม่ได้** อาจารย์เรียกว่าเป็น **strongly …** `[ไม่แน่ใจ: ฟังคล้าย "strongly fault secure"/"strongly code disjoint"]` คือคงสภาพ **ไม่กลายเป็น error code word** จนกว่า fault ใหม่จะเกิด

### 10.2 ตัวอย่างที่อาจารย์ไล่จริง (F1/F2/F3) — วิธีคิดที่ควรจำ

โจทย์: มี circuit + fault F1, F2, F3; ถามว่าเป็น **code disjoint / fault secure / TSC / ไม่ self-checking**? วิธีที่อาจารย์ทำ: **เจนค่าก่อน / วาดตาราง** แล้วดูว่าแต่ละ fault ให้ output เป็นอะไร

- **F1**: ให้ output เป็น **code word ที่ผิด** ⇒ **ไม่ fault secure** และ **ไม่ self-testing** ด้วย
  - ผลสรุป: ในกรณี F1 (ร่วมกับ input/state ที่พิจารณา) **วงจรนี้ไม่ใช่ self-checking**
- **F2**: ยัง **คงสภาพ Normal** ในการ run normal operation ⇒ ถือว่า **fault secure**
- **F3**: output ออกมาเป็น **non-code word** ⇒ **self-testing** ได้เลย และนับเป็น **fault secure** ได้ด้วย (เพราะไม่กลายเป็น code word ผิด)
- อาจารย์สรุปเป็นแนวคิดว่า: วงจรที่ **ST + FS** ครบ ⇒ TSC และยกตัวอย่างว่า **gate logic หนึ่งตัว (พูดถึง Exclusive-OR)** เป็นทั้ง ST และ FS, แถมมี **code preserving** ด้วย ⇒ เป็น TSC
- ข้อสังเกต: นี่คือเหตุผลที่ checker/circuit ต้องมีคุณสมบัติ **online / concurrent** — เป็น **concurrent error detection scheme** ตรวจได้ **real-time** ก่อนที่ fault จะลุกลาม

---

## 11. การทำงานแบบ Masking vs Self-Checking (ที่อาจารย์เทียบให้)

- **For Masking**: ใช้ **2 checkers** (check code ที่คำนวณกับ code ตอนใช้งานจริง) มา **compare กัน** → ดูว่าผิดตรงไหน → ส่งผ่าน **collector** เพื่อ generate/แก้ output
- **Self-checking**: **ไม่ Masking** — **ไม่ส่ง collector output** แต่ **detect ทันที** ว่าถูกหรือผิด (ก่อน concurrent fault) ⇒ เป็นแนวคิด **concurrent error detection**
- Flow ที่อาจารย์วาด: input → **Functional Unit** → ดูว่า **code ยังเป็น code word (preserve code) หรือเปล่า** → **Checker** → บอก **Normal / Abnormal**
  - Checker จะ **check อะไรก็ได้** — check input ภายใน, check output, หรือ check output ที่เทียบกันก็ได้
- จุดที่อาจารย์ย้ำ (สำคัญมาก): **Checker ไม่ได้เช็คความถูกต้องเชิงตรรกะ** เช่น **ไม่เช็คว่า 2+2 ต้องเป็น 4** — checker เช็คแค่ **"ค่าเป็น code word หรือไม่"** ⇒ ถ้า functional unit ให้ค่าที่ผิดแต่ว่า *ยังอยู่ในรูป code word* checker **จะไม่รู้**
- อาจารย์บอกว่า **CED (Concurrent Error Detection)** เป็น **เทคนิคสำคัญ** ในปัจจุบัน ⇒ ใช้ **error-detecting code** ออกแบบ self-checking logic circuit
- การเพิ่มของที่ต้องมี 2 อย่าง: **(1) information redundancy** (เพิ่ม check bit) และ **(2) checker** ที่คอยบอกถูก/ผิด
  - Logic: **Functional Unit OK + Checker OK ⇒ Normal**; ถ้า checker เสีย อาจไม่รู้ — ต้องมีอย่างน้อย **1 output** ที่เป็น yes/no; ถ้า stuck ที่ "yes" ตลอดจะมองไม่ออก
- **Error-detecting code 2 กลุ่ม**: **Separable** (Parity, Berger) และ **Non-Separable** (`[ไม่แน่ใจ: ชื่อ — ฟังคล้าย "Bluetooth code / MRFN code"]`) — ทั้งคู่ใช้เช็ค **internal fault แบบ online** โดยไม่ต้องป้อนจากภายนอก
- **หลัก monotonic ที่อาจารย์เน้น**: ถ้าผิดพลาด ต้องไปทาง **"earlier/worse space"** (non-code word) **เท่านั้น ห้ามกลับไปที่ code space** — ไม่เช่นนั้นจะสับสนและกลายเป็น error ที่หลุด

---

## 12. Checker และการออกแบบ (รายละเอียดที่อาจารย์พูด)

- **ตัวอย่างที่ผิด (สำคัญ)**: ออกแบบ **parity checker** ที่มี **output เดียว** — อาจารย์บอกว่าอันนี้ **ผิด** เพราะถ้ามัน stuck/เสียขึ้นมา จะ **ไม่รู้ว่าถูกหรือผิด**
- **Self-testing checker**: ให้ **แบ่งเป็นส่วน ๆ (ต่อเป็น cascade)** — ถ้ามีแค่ 2 bit แล้วเอามาต่อกันจะมีหลาย bit ตามมา ⇒ **ต้อง Combine** ให้ได้
- **2-Rail Code Checker**: แทนที่จะแสดงผล 4 bit ให้ **รวม/แบ่งเหลือ 2 bit** ได้; มีการสร้าง checker เสริม
- ชนิด checker ที่อาจารย์ไล่ชื่อ (บางชื่อฟังเพี้ยน): **parity checker**, **input regeneration checker**, **duplex checker**, **constant weight code checker**, และ **2-rail / N-pair rail code checker** `[ไม่แน่ใจ: ชื่อ "Private Checker" ที่อ่านไม่ออกความหมาย + ตัวอย่าง "ต่อเป็น 3 structure"]`
  - **Input Regeneration Checker**: ป้อน output กลับเข้าวงจร (วงจร L) แล้วเทียบ **output กับ input ของ L**; เราควร **simplify** ให้ gate น้อยที่สุด
  - อาจารย์ย้ำ: **checker เองก็ควรเป็น self-checking ด้วย** ถ้าทำได้
- **m-of-2m** — หลักการคล้ายกัน ทำเป็น pair checker แล้วเชื่อมกันได้
- **k-of-m** — ต้อง **แปลงก่อน** ให้เข้ารูป (เช่น 1-of-m แล้วค่อยต่อเป็น T-of-4) `[ไม่แน่ใจ: "1 of 10"/"T of 4"]`
- **Berger code (non-separable)**: data bit → generate check bit → เข้า checker แล้วเทียบกับ check bit; มี **term prediction** เข้ามาเกี่ยวข้อง
- ทางเลือกอื่น: **decode ก่อน แล้วทำเป็น true/false checker** หรือใช้ **end-of-… code**; และพยายามทำ **self-test ให้ครอบคลุม** ให้ครบทุกค่า

---

## 13. TSC Functional Unit + การบ้าน

- อาจารย์บอกว่า **TSC functional unit แบบตรง ๆ ค่อนข้างสิ้นเปลือง (cost/area)**
- ทางที่ **ดีกว่าและ easy to implement** คือทำเป็น **dual logic / dual-rail**:
  - เปลี่ยนทุกเส้นเป็นคู่เส้น (single → dual); ใช้ non-inverter gate ⇒ ได้ **unidirectional error** + **preserve code**
  - ตัวอย่างที่อาจารย์ไล่: ฟังก์ชันหนึ่งทำเป็น dual logic; พอเกิด fault จะเห็นว่า input เข้ามาก็เปลี่ยนไป ⇒ แสดงว่า **fault secure + self-testing ครบ ⇒ TSC unit**
  - ข้อดีเพิ่ม: ส่วนที่มี **redundancy/เรียนแดน** `[ไม่แน่ใจ: คำที่อ่าน]` ตัดทิ้งได้, ลดรูป (contraction) จนได้แบบ **non-redundant**; ใช้ **non-redundant code** generate ออกไปได้
- **การบ้าน / แบบฝึกหัด**: ให้สร้าง **self-checking circuit** ของ **4-to-1 multiplexer (อ่านว่า "4D multiplexer" ที่มี n double)** `[ไม่แน่ใจ: สเปก/ชื่อ]`
  - แนวทางที่อาจารย์ใบ้: **สร้างให้เร็ว/เรียบง่าย** แล้วมี **checker** ตรงจุดที่ตรวจสอบได้ (checker ต้องดี)
- ทิ้งท้าย: อาจารย์บอกว่า **state machine (sequential) ก็ทำได้เหมือนกัน** หลักการคล้ายกับ combinational; และมีหัวข้อ **partial self-checking** ให้ไปศึกษาต่อเอง

---

## 14. สิ่งที่อาจารย์ "เน้นเป็นพิเศษ" (สรุปรวม)

1. **recompute + compare** เป็นหัวใจของการตรวจ (ใช้ทั้งใน cyclic code, ECC, checksum, residue)
2. **Syndrome = ตำแหน่ง bit ที่ผิด** (Hamming) ⇒ flip แล้วแก้ได้; และ **Venn diagram** เป็นเครื่องมือช่วยวิเคราะห์ที่เข้าใจง่าย
3. **Unidirectional error** เป็น model ที่ **realistic และคลุม single+multiple**; **dual-rail / inverter-free** ทำให้ error เป็น unidirectional โดยธรรมชาติ
4. **Checker ไม่ได้ตรวจความถูกต้องเชิงตรรกะ** — ตรวจแค่ความเป็น code word ⇒ เป็นข้อจำกัดที่ต้องเข้าใจ
5. **FS + ST = TSC**; FS เดี่ยว ๆ ไม่พอ เพราะ fault ถัดไปทำให้ FS หายได้ ⇒ ต้องจับได้เร็ว
6. **ต้องไม่กลับไปที่ code space** เมื่อเกิด error (monotonic: ไปทาง non-code word เท่านั้น)
7. วิธีทำข้อสอบ/โจทย์: **"เจนด้วยเบอร์ก่อน"** แล้วค่อยวิเคราะห์; โจทย์แนว ST/FS/SFS อาจารย์บอกว่า **"ปกติไม่ได้หมุนเยอะ"**

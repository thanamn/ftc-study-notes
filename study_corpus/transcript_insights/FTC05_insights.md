# FTC05 — Transcript Insights (Coding Theory)

> สรุปเนื้อหาที่ "อาจารย์อธิบายด้วยคำพูด" (ไม่ใช่ข้อความบนสไลด์) จาก transcript ของคาบนี้
> ภาษาไทย เก็บ English technical terms ไว้
> สิ่งที่ garbled/ไม่ชัด จะกำกับด้วย [ไม่แน่ใจ: ...]

---

## 0. ทบทวนช่วงต้นคาบ: Checkpoint / Recovery Line

- โจทย์ทบทวน: มี 4 process (P0–P3) run parallel กัน มีการส่ง message ระหว่าง process ตามรูป (ตามลูกศร/ตามรูปด้านล่าง) แล้วให้ลาก Recovery Line ที่ผ่านจุด Checkpoint ของแต่ละ process "อย่างละจุด"
- เกณฑ์ตัดสินว่าเส้นนั้นเป็น **Consistent / Strongly Consistent / Inconsistent**:
  - **Consistent** = เส้นที่จุด checkpoint เป็น "อิสระ" ต่อกัน หมายถึง **ไม่มีเส้น message ตัดผ่าน** จากอดีตไปอนาคต หรือจากอนาคตมาอดีต
  - ตัวอย่าง: **เส้นสีฟ้า** = ไม่ตัด message line เลย
  - **เส้นสีแดง** = ยอมให้มี message ตัดได้ (inconsistent) แต่วิเคราะห์ต่อว่าเป็นประเภทไหน — ในรูปนี้เส้นแดงมีอยู่ 2 เส้นที่ตัด: P2 → P0 และ P3 → P2 คือมีการส่ง message ไป แต่ฝั่งผู้รับ "ไม่รู้ว่าใครเป็นผู้ส่ง" เพราะจุด recovery อยู่ก่อนหน้านั้น
  - **เส้นสีดำ** = กรณี P2 → P1 พบว่า P0 ได้รับ message โดยไม่รู้ว่าผู้ส่งคือใคร เพราะ recovery ย้อนไปก่อนจุดนั้น
- อาจารย์ย้ำว่า ปัญหาที่เกิดคือ **orphan message** (ข้อความที่ไม่มีผู้ส่ง) [ไม่แน่ใจ: transcript ถอดเป็นคำว่า "Warfare กับ Message"] จึงต้องระวังตอนทำ recovery ให้ดี
- มีการพูดถึงเงื่อนไขจำนวน node ที่ต้องใช้เพื่อ **detect ว่า process ไหนผิด** โดยอ้างสูตรคล้าย Byzantine Generals [ไม่แน่ใจ: transcript ถอดเป็น "3m บวก 1" และ "มี f" — น่าจะเป็นแนวคิด 3f+1 node จึงจะ detect/tolerate ได้] และบอกว่าถ้ารู้ว่า process ไหนผิด ก็ทำ Recovery ได้ด้วยหลักการ Rejecting point/cluster

---

## 1. Coding Theory คืออะไร

- Coding Theory = การทำ **information redundancy** และศึกษา **property ของโค้ด** ว่ามัน fit กับการใช้งาน (application) ที่เฉพาะเจาะจงได้อย่างไร
- อาจารย์บอกที่มาว่าอิงจาก paper ที่ค่อนข้างเก่า และเนื้อหายาวต่อเนื่องมาถึงปัจจุบัน
- เป็นพื้นฐาน (พื้นศาสตร์เบื้องต้น) ของวิชานี้ และบอกว่าวันนี้ "ถ้ามีแรงก็คงเล่าให้หมด ถ้าไม่มีแรงอาจจะไปถึงแค่ cyclic code" (เพราะเนื้อหาเยอะ)
- Coding Theory ในวิชานี้ = **Theory of Error Correcting Code / Error Control Code**

### Coding Theory เกี่ยวข้องกับ Fault Tolerance อย่างไร
- **Data Compression**: เราไม่ควรใส่ data ดิบ ๆ ตรง ๆ เพราะสิ้นเปลือง จึง compress เพื่อประหยัดพื้นที่ในการส่งข้อมูล
- **การส่งข้อมูลผ่านช่องสื่อสาร**: ผู้รับอาจเจอ **Noise** แทรก ทำให้ข้อมูลที่รับผิดกลายเป็น **Error** → ใช้ coding ช่วยได้ คือทำให้เรารู้ว่าข้อมูลที่รับมามี error หรือไม่ (detection) และถ้าต้องการคุณสมบัติที่ดีขึ้นก็แก้ไขให้ (correction)

### Error Correction สำหรับข้อมูล Binary
- ถ้าเป็นข้อมูล binary การแก้ไข "ไม่ยาก": ถ้าเรารู้ว่า bit ใดผิด (รู้จำนวน bit และตำแหน่ง) ก็แค่ switch กลับ 1 → 0, 0 → 1
- **ประเด็นสำคัญที่สุดของ Error Correction** ที่อาจารย์ย้ำ = ความสามารถในการ **Locate ว่า error อยู่ที่ bit ไหน**
- สรุปศัพท์: **Error Control** = ครอบคลุมการ detect / locate / (และ) correct; "allocate" ว่า error อยู่ตำแหน่งไหนแล้วค่อยแก้

---

## 2. Coding vs Cryptography vs Steganography

- **Coding**: เข้ารหัสโดยใช้ information redundancy ทำให้ตัวรหัส "สมบูรณ์" มากกว่าเดิม — เกิดจากการป้องกัน **noise จากธรรมชาติ** ใช้ Error Control Code เป็นหลัก
- **Cryptography**: ป้องกันไม่ให้ unauthorized user เข้ามา hack — เป็น "สงคราม" ระหว่าง Code Maker กับ Code Breaker ว่าฝ่ายไหนจะเก่งกว่า
- **Steganography**: ซ่อนข้อมูลไว้ในรูป/สิ่งที่มองเห็น เช่น ใส่ **watermark** คนที่ detect ได้จะรู้ว่าข้อมูลนั้นเป็นข้อมูลจริงหรือไม่ (ดูจาก watermark)
- อาจารย์ระบุชัดว่าในคาบนี้จะพูด **เฉพาะ error control** ส่วน compression และ cryptography จะไม่กล่าวถึง

---

## 3. โครงสร้าง Layer ของการสื่อสาร (Data Processing Levels)

- เรียงจากระดับบนลงล่าง:
  1. **Encryption** (ระดับบน — cryptography)
  2. **Encode / Coding** (ทำ information redundancy)
  3. **Modulation / Demodulation** (ระดับล่างสุด — แปลง Digital ↔ Analog)
  4. **Channel**
- **Modulator = ตัว Encoding**, **Demodulator = ตัว Decoding**
- ฝั่งบน (over channel) เป็น **Analog** แล้วส่งผ่าน Channel ที่มี **Noise**; ปลายทาง Demodulator แปลงกลับเป็น Digital แล้ว Decode
- Channel ในทางปฏิบัติ: **Fiber, Telephone line, Hard Disk, Satellite link** ฯลฯ → channel ไม่ perfect มีโอกาสถูกกวนด้วย noise
- เป้าหมาย: มี source string เข้ามา → encode ส่งผ่าน noisy channel → decode กลับมาเป็น digital แล้ว **recover message เดิมได้โดยไม่มี error** แม้มี noise
- วิธีการคือ **ขยาย size/ความยาวของ code string** ให้สามารถ "มองเห็น" ตำแหน่งต่าง ๆ ได้ เพื่อ locate error
- ตัวอย่าง application ของ Error Correcting Code: **Parallel Communication, CD Player, TV, Fax Machine, Internet**

---

## 4. Shannon / Channel Capacity (Information Theory)

- อ้างถึง **Shannon**: **Maximum Rate** ที่ข้อมูลสามารถส่งผ่าน communication channel หนึ่ง ๆ ได้ ภายใต้ **Bandwidth** ที่กำหนด → นี่คือ **Channel Capacity**
- Capacity สัมพันธ์กับ **Signal to Noise Ratio (SNR)**: ถ้า noise สูงมาก signal จะอ่อน (และส่งไม่ได้)
- **Binary Symmetric Channel (BSC)**: รับ binary input 0/1 เพื่อ reproduce binary output
  - มี probability ของ error = **p**, โอกาสส่งถูกต้อง = **1 − p**
- สูตรที่อาจารย์ให้ (ถอดความ): **C = 1 − H(p)** [ไม่แน่ใจ: transcript ถอดเป็น "C = 1 ลบ sp" ซึ่งน่าจะหมายถึง 1 − H(p)]
- ค่าที่พูดถึงในห้อง:
  - p = 0.5 → **C = 0** (ส่งไม่ได้)
  - p = 0.1 → **C ≈ 0.53**
  - p = 0.01 → ค่าที่ transcript ให้ไม่ชัด [ไม่แน่ใจ: transcript พูดตัวเลขประมาณ "0.2/0.9" ซึ่งขัดกับสูตร C = 1 − H(p) ที่ควรได้ ≈ 0.92]
  - Ideal case: p = 0 → **Noise Free** → **C = 1** (รับประกัน noise free ส่งแค่ 1 bit ก็ได้)
- หลักการใช้งาน: ถ้า **Transmission Rate R < Channel Capacity** → ส่งได้; ถ้า **R > Capacity** → ส่งไม่น่าเชื่อถือ
- อาจารย์เทียบให้เห็นว่าเพื่อกัน error ถ้าใช้วิธี "ส่งซ้ำ" อาจต้องส่งถึง ~**63 ครั้ง** แต่ถ้าใช้หลัก Channel Coding Theory อาจส่งเพียง ~**2 ครั้ง** ก็ป้องกัน/แก้ error ได้ในระดับ 10⁻¹⁰⁰ ได้ [ไม่แน่ใจ: รายละเอียดตัวเลข 63 ครั้ง / 2 ครั้ง / 10⁻¹⁰⁰ จาก transcript ไม่ชัด] — ประเด็นคือ "ส่งน้อยครั้งลงได้ แต่ code word จะยาวขึ้น"

---

## 5. Repetition Code + Majority Voting (ตัวอย่างที่มือ)

- วิธีง่ายสุด: encode **0 → 000** และ **1 → 111** (ทำ redundancy)
- สมมติ Bit Error Probability **p < 1/2** (transcript พูดว่า "< 1.2" [ไม่แน่ใจ])
- ตอน decode ใช้ **majority voting**:
  - รับ `000`/`001`/`010`/`100` → ตีเป็น **000**
  - รับ `111`/`110`/`101`/`011` → ตีเป็น **111**
- **คำนวณความน่าจะเป็นที่ decode ผิด** (กรณี 3-bit repetition):
  - ผิดเมื่อมี **3 bit errors**: p³
  - หรือ **2 bit errors**: C(3,2)·p²·(1−p) = 3p²(1−p)
  - รวม ≈ 3p² − 2p³ (ซึ่ง < p เมื่อ p < 1/2)
  - อาจารย์สรุปว่า error หลัง voting น้อยกว่า p ของการส่ง bit เดียว → **ประโยชน์ของ coding สูงกว่าการไม่ encode**
- อาจารย์ยกตัวอย่างส่ง "ความยาว" และถ้าจำนวน error เกินกว่าที่ออกแบบไว้ จะได้ค่าที่แย่ลง (ต้องระวัง)

---

## 6. ตัวอย่างส่งข้อความ (Bob → Alice)

- ตัวอย่างง่าย ๆ: สมมติส่งข้อความจาก **Bob ไป Alice** เกี่ยวกับ **"การเดินทาง/เส้นทาง"** โดยใช้ชุดคำแทนทิศทาง (North, North-West, West, West-West, South-West, ...) — [ไม่แน่ใจ: รายละเอียด code word ที่ transcript ถอดออกมาเป็นคำทิศทางซ้ำ ๆ เพี้ยน (เช่น "นอดๆเวฟ", "เวทเวท", "ซ้าว") ไม่สามารถถอดกลับได้ชัดเจน]
- แนวคิด: ด้านบนคือ **โค้ดที่เราใช้ส่ง**, ฝั่งส่งใช้ **Encoder** ซึ่ง encode ได้หลายวิธี
- ถ้าเราแทนค่า (เช่น North-West, South-East ฯลฯ) แล้วได้ค่าออกมา ก็จะรู้ว่าผิดตรงไหน
- เมื่อเกิด error :
  - single error จะถูก **majority masking** ได้
  - ถ้าเปลี่ยน 3 bit พร้อมกัน จะเริ่มถูก mask / ทำให้ substantial error หายไป ได้ค่าที่ดีขึ้น
  - แต่ถ้าใช้ code ยาว **5 bit** ก็จะ correct ได้ในกรณีที่ error มากกว่าเดิม
- (สรุปเชิงคุณภาพ: ยิ่ง code ยาวขึ้น ยิ่ง correct error ได้มากขึ้น — ตรงกับ majority voting)

### Alphabet ของโค้ด
- โค้ดประกอบด้วย **Alphabet** ที่มีได้หลาย symbol → เรียกว่า **q-ary** (transcript อ่านเป็น "คิว", "คิว นารี่")
- ถ้า alphabet เป็น **Binary** (q = 2) ใช้ symbol 0 กับ 1
- จากนั้นจะดู **Encode / Decode** และ **Transmission** ต่อไป

---

## 7. Hamming Distance / Hamming Weight

- **Hamming** ค้นพบ **Hamming Distance**
- **Hamming Distance** = ระยะห่างระหว่าง code word สองตัว = **จำนวน bit ที่ค่าต่างกัน** เมื่อเทียบตำแหน่งต่อตำแหน่ง
  - ตัวอย่างที่ให้: `0000` กับ `0001` ต่างกัน 1 ตำแหน่ง → distance = 1 [ไม่แน่ใจ: ตัวเลข code word ที่ transcript ถอดมาไม่ครบ]
- **Hamming Weight** = จำนวน bit ที่ **ไม่ใช่ศูนย์** ใน code word หนึ่งตัว (เช่น code word 0000 มี weight = 0)
- **คุณสมบัติของ Hamming Distance** ที่อาจารย์ยกมา:
  1. d(x, y) = 0 ก็ต่อเมื่อ x = y (และสมมาตร d(x,y) = d(y,x))
  2. d(x, y) = d(y, x) [สมมาตร]
  3. **Triangle inequality**
- **Minimum Distance** ของโค้ด = ค่าน้อยที่สุดของ distance ระหว่างทุกคู่ของ code word
- จาก Minimum Distance ได้กฎ:
  - **Detect** error ได้: ถ้า d ≥ s + 1 (transcript พูดว่า "s4 มากกว่า s1" [ไม่แน่ใจ])
  - **Correct** error ได้: ใช้ floor((d − 1) / 2) ความสัมพันธ์คือ **t ≤ (d − 1)/2** (ปัดลง)

---

## 8. Parity Code (1 มิติ และ 2 มิติ)

- **Parity bit**: เติม bit เพิ่มอีก 1 bit แล้ว set ให้รหัสเป็น **เลขคู่ (even parity)** หรือ **เลขคี่ (odd parity)** → ใช้ **Detect** error ได้
- ถ้าต้องการ **correct** จริง ๆ ต้องใช้หลักการที่เพิ่ม bit มากกว่านั้น (เช่น Hamming)
- ตัวอย่างเชิงคำนวณ (Parity อย่างง่าย):
  - binary word ยาว ~**11 bit** เป็น code word
  - error rate = **10⁻⁸** ต่อ bit
  - transmission rate = **10⁷ bit per second**
  - โจทย์ถามโอกาส/เวลาที่จะเกิด transmission error
  - ผลเชิงคุณภาพ: ถ้า **ไม่ใส่ Parity** จะเกิด error บ่อยมาก (ระดับทุก ~10 วินาที [ไม่แน่ใจ: transcript มีตัวเลขทั้ง 10 วินาที และ 60 วินาที ปนกัน]); เมื่อใส่ **Parity 1 bit** จะ detect single error ได้ ทำให้ระยะห่างการเกิด error ที่หลุด เพิ่มขึ้นมาก (transcript พูดถึงระดับ **~2,000 วัน**) [ไม่แน่ใจ: ตัวเลขทุกตัวในย่อหน้านี้ transcript เพี้ยน]
- **Parity 2 มิติ (2-Dimensional Array)**: ถ้ามอง parity แค่ 1 มิติอย่างเดียว อาจขยายเป็น **2 มิติ** ได้ คือมี parity ทั้ง **แนวตั้งและแนวนอน** เก็บค่าใน array → ช่วยได้มากขึ้น (detect/correct ได้บางกรณี)

---

## 9. Notation (n, M, d) และการ Optimize

- อาจารย์ย้ำ **notation (n, M, d)** ให้จำ:
  - **n = ความยาวของ code word (length of code word)**
  - **M = จำนวน code word (number of code words)**
  - **d = minimum distance**
- ตัวอย่างที่ยกในห้อง: **(5, 4, 3)** = ยาว 5 bit, มี 4 code word, min distance = 3 (อาจารย์ไล่ตรวจว่า distance ระหว่างคู่ = 3 จริง)
- [ไม่แน่ใจ: อาจารย์พูดถึง "Code64" และตัวอย่าง "(5,4,3)" กับสูตรที่ transcript ถอดเป็น "เน้นเอ็มดี...สอง โค้ดเบิร์ด...เบือรต่อกับสี่" — น่าจะเป็นการเทียบขอบเขต/สูตรจำนวน code word สูงสุด แต่ถอดความไม่ชัด]
- **การ Optimize โค้ด** — อยากได้พร้อมกัน:
  - **N น้อย** (code word สั้น)
  - **M มาก** (มี code word เยอะ)
  - **d มาก** (กัน error/correct error ได้ดี)
  - ถ้า N เล็ก, M เยอะ, d ใหญ่ → optimize ได้ [ไม่แน่ใจ: transcript ถอดเป็น "จะได้ตัว A2 หรือ 8D ... D1 D2" — น่าจะเป็นชื่อ/sphere-packing bound แต่ถอดไม่ชัด]
- **ค่า d**: ถ้า d เป็น **เลขคี่** จะบวก 1 ให้เป็นเลขคู่; ถ้าเป็น **เลขคู่** ก็บวก 1 เช่นกัน [ไม่แน่ใจ: transcript ถอด "...ก็ได้รูป 1 เหมือนกัน แล้วจริงหรือเปล่า" อาจารย์เองก็ลังเล]
- **Equivalent code**: เกิดจากการทำ operations บนโค้ด ได้แก่ **permutation ของตำแหน่ง (position)** และ **การสลับ symbol (symbol permutation)** — ใช้ notation (n, M, d) ช่วยดูว่าโค้ดสองอัน equivalent กันหรือไม่

---

## 10. Linear Code และ Cyclic Code (+ ตัวอย่างสร้างโค้ด)

### Binary Linear Code
- **Binary linear code** = เซตของ **n-tuple** (n bit) ที่ใช้ **component-wise sum modulo 2** (บวกแบบ mod 2 ไม่มีตัวทด)
- คุณสมบัติ: **ผลบวก (mod 2) ของ code word ใด ๆ ยังอยู่ใน code group เดิม** → ถือเป็น linear code
- ตัวอย่างเชิงสร้างที่อาจารย์ลองทำในห้อง:
  - เริ่มจาก code word หนึ่ง แล้วหาว่าบวกอะไรได้ค่าเดิม (identity/สมาชิกเอกลักษณ์)
  - เอาเลข 2 ตัวมาบวกกัน mod 2 (เช่น 111 + 111 = 000)
  - แล้วลองบวกกับตัวอื่น ๆ ไปเรื่อย ๆ → หมุนเวียนกันมา
  - [ไม่แน่ใจ: ตัวอย่างที่ถอดได้คือ "(4,4,2)" และ "เรามี notation สิบสี่ซอง" ซึ่งไม่ชัด]
- **(7, 16, 3)** = Hamming code: 7 bit, มีทั้งหมด 16 code word, min distance = 3 → มีคุณสมบัติเป็น **Linear Code**

### Cyclic Code
- นอกจากการบวกแบบ modulo แล้ว ถ้า **shift (cyclic shift)** code word ไป แล้ว **ยังอยู่ในกลุ่ม code word เดิม** → เรียกว่า **Cyclic code**
- อาจารย์พิสูจน์แนวคิด: ถ้ามี C1, C2 → shift ก็ได้ C3, C6 ไปเรื่อย ๆ → เป็น cyclic
- ตัวอย่าง **ternary (q=3) cyclic code**: ใช้ symbol 012 สร้างเป็น `012 012 012 ...` แล้วเข้ารหัส (เช่นรวมเป็น 3 ตัว) → สร้าง code words จาก 0,1,2 ได้ทั้งหมด [ไม่แน่ใจ: ตัวอย่าง 0112/010 ที่ transcript ถอดมา ไม่ชัด]
- อาจารย์พูดว่า "Psychic Code" [ไม่แน่ใจ: น่าจะเป็นคำที่ speech-to-text ถอดเพี้ยนของ **Cyclic Code**] เป็นเป้าหมายสูงสุดของเนื้อหาวันนี้

### ตัวอย่างหา Minimum Distance (ทำงานมือ)
- กำหนด code word มา 3–4 ตัว (transcript ถอดเป็นชุดคล้าย `001, 110, 101, 011`) [ไม่แน่ใจ]
- วิธีทำ: **จับคู่ code word ทุกคู่ (combination)** แล้วหา Hamming Distance ของแต่ละคู่
  - ตัวอย่าง transcript: คู่แรก distance = 2, คู่ที่สอง = 1, คู่ที่สาม = 3
- แล้ว **minimum distance = ค่าที่น้อยที่สุด** ในบรรดาทุกคู่ (ในตัวอย่างหนึ่งอาจารย์ได้ min distance = **2**)
- โจทย์แนวนี้ (find minimum distance ของโค้ด 4 ตัว) อาจารย์บอกให้ทำทุก combination

### ตัวอย่างโค้ด 4 ตัว (ต่อ)
- อาจารย์ให้โค้ดมา 4 ตัว แล้วไล่ distance ทุกคู่: ได้ค่าต่าง ๆ เช่น 3, 5, 3, 5, 4, 2, 2, 5, 3, 4 ...
- **minimum distance = 2** → แล้วนำไปใช้ต่อกับสูตร detect/correct

---

## 11. จำนวน Error ที่ Detect / Correct ได้ (จาก Minimum Distance)

- **Detect ได้**: จำนวน error ≤ **d − 1** (transcript: "อยู่ในกฎของ Minimum Distance ลบหนึ่ง")
- **Correct ได้**: จำนวน error ≤ **(d − 1) / 2** (ปัดลง) — transcript ถอดเป็น "ลิฟต์หนึ่งส่วนสอง"
- ตัวอย่างการทำงานมือ (01:00–01:11):
  - โจทย์: ต้องการส่ง bit string (transcript ถอดเป็น "0000" ยาว ~6 bit) โดย error rate ≈ **0.01 ต่อ bit**
  - ถาม: **โอกาสที่ bit string ที่รับจะกลายเป็นรูปแบบที่กำหนด** (เช่นรับเป็น `100100`) — ต้องคำนวณจาก พหุนามการกระจายของจำนวน bit ที่ flip:
    - ตัวอย่าง: ถูก 4 ตัว ผิด 2 ตัว → (0.99)⁴ × (0.01)² [ไม่แน่ใจ: exponent จาก transcript ไม่ชัด]
  - แล้วหา minimum distance ของโค้ด (4 code word) → ทุก combination (6 คู่)
  - นำ min distance ไปเข้าสูตร detect/correct ว่าถ้า error 1 ตัว "ยังแก้ได้" ถ้าเกิน 1 ตัว "แก้ไม่ได้" (ขึ้นกับระยะ)
  - อาจารย์เน้นว่า **บางทีต้องดูว่า received word อยู่ในเกณฑ์ที่ correct ได้หรือไม่**

---

## 12. หลักการ Implement Coding ด้วย Hardware: Generator Polynomial

- คำถาม: มี data แล้ว จะ **สร้าง (implement) code** ขึ้นมาอย่างไร → ต้อง encode ก่อน แล้วฝั่งรับก็ decode กลับ
- ใช้ **Generator Polynomial** เป็นตัวคูณ: **Code = Data × Generator Polynomial** (คูณใน GF(2))
- **Degree ของ generator polynomial = จำนวน parity bit = n − k**
  - โดยที่ data = k bit, encode แล้วได้ n bit
- **Factorization**: generator ต้องเป็น **ตัวประกอบ (factor) ของ xⁿ − 1** (ใน GF(2) คือ xⁿ + 1)
  - ตัวอย่าง: **x¹⁵ + 1**, n = 15 → แยกตัวประกอบได้เป็นพหุนามกำลังน้อยกว่า เช่น x⁴ + x + 1 ฯลฯ [ไม่แน่ใจ: transcript ถอด "เอ็กซ์บวกเอ็คเกลียวฝั่งสาม", "x³", "x⁴+x+1" ปนกัน]
  - ถ้าเลือก generator = **x + 1** → ได้ **Parity Code** (เพิ่ม 1 bit) — เป็นที่มาว่าทำไม parity ถึงมองเป็น code ได้
  - generator x³ + x + 1 ฯลฯ ถูกใช้กับ n = 5, 6, 7, 10, 11 (transcript ไล่ตัวเลขนี้)
- **การ Encode**: เอา data คูณกับ generator → ผลลัพธ์เป็น code word ที่ **หารด้วย generator ลงตัว (ไม่มีเศษ)**
- ตัวอย่างการคูณ (transcript): data `1101001...` เขียนเป็น polynomial แล้วคูณกับ generator → ได้ code word; อาจารย์บอกให้ "มองกลับกัน" และเทียบกับค่า parity

### โครงสร้าง Hardware
- ใช้วงจร **shift register (delay elements)** ร่วมกับ **XOR gates** (transcript เรียกว่า "เอ็กซ์คลูซีฟออร์")
- data feed เข้ามาผ่าน delay (x, x², x³, x⁴ ...) แล้ว XOR กันตาม generator polynomial → output ที่ได้คือส่วน parity/check bits
- สรุปคือ: **เอา generator polynomial มาสร้างเป็นวงจรหาร (Divider)**

---

## 13. การ Decode ด้วย Hardware / Syndrome (Remainder)

- ฝั่งรับ: เอา code word ที่ได้ **มาหารด้วย generator polynomial (Divider)**
  - ถ้า **remainder = 0** → ไม่มี error (ข้อมูลถูกต้อง)
  - ถ้า **remainder ≠ 0** → มี error เกิดขึ้น (หรือ error 1 bit ที่ตำแหน่งนั้น)
- ใช้**ตาราง (syndrome table)** แปลงค่า remainder → ตำแหน่งของ error เพื่อแก้ไข
- ตัวอย่างที่อาจารย์ไล่: ถ้า remainder เป็น `0 0 0` = ถูก; ถ้าเริ่มเป็น `0 0 1` = ผิด → ตรวจสอบว่าค่าที่เข้ามาผิดตรงไหน
- อาจารย์แนะนำให้ **ทำตาราง encode/decode** (เช่นตารางหน้า 40 ที่บอกว่า generator ไหนใช้กับอะไร) และใช้ตารางนี้เวลา implement
- ตัวอย่างลำดับบิตที่ transcript ถอดได้: data 4 bit → encode เป็น 7 bit, จัดเรียงบิตแล้วป้อนผ่าน delay 1, 2, 3 → ได้ output เช่น `0 1 0 0 0 1 1` (แล้วให้ตรวจกับที่คำนวณมือ) → Decode เอากลับเข้าตารางแล้ว clear register → ได้ data 4 bit กลับมา [ไม่แน่ใจ: ลำดับบิตและ register operations จาก transcript ไม่ชัด]

---

## 14. โจทย์ / สิ่งที่ให้ไปทำต่อ (แนวข้อสอบ/การบ้าน)

- อาจารย์ **แจกโจทย์ท้ายคาบ** (พูดว่า "วันนี้เดี๋ยวผมปล่อยโจทย์ให้กับพวกเรา"):
  - ให้สร้าง **cyclic code แบบ (7, 4)** คือ n = 7, data k = 4
  - หา **g (generator)** ที่เหมาะสม แล้วใช้ generator polynomial ในการสร้าง code
  - **สร้าง Hardware Implementation** (วงจร) ของ encoder
  - เลือก generator ตัวใดตัวหนึ่ง (transcript พูดถึง "5" ตัวหนึ่ง) แล้วป้อน data เข้าไป ตรวจว่าผลลัพธ์ออกมาตรงกับที่คำนวณ
  - จากนั้น **decode กลับ**: ได้ 7 bit → decode กลับเป็น 4 bit ให้ถูกต้อง แล้วตรวจว่า **เศษ (remainder) จาก divider = 000** หรือไม่
  - แล้วลอง **ใส่ error 1 bit** เข้าไป decode ดูว่าเศษ **ไม่เป็นศูนย์** เพื่อยืนยันว่าฮาร์ดแวร์ที่สร้างถูกต้อง
- อาจารย์ย้ำให้ **ลองสร้างเอง/ทำด้วย** ("ตัวเองก็ทำให้หน่อยเหมือนกัน") และให้ดู hardware ให้ครบ
- **ไม่มีการพูดถึงข้อสอบอย่างชัดเจน** ในคาบนี้ [ไม่แน่ใจ: นอกจากโจทย์ท้ายคาบนี้ ซึ่งอาจารย์บอกว่าจะปล่อยให้ทำ]

---

## 15. สิ่งที่อาจารย์เน้นย้ำ (Takeaways)

1. **Locate ตำแหน่ง error ได้** คือหัวใจของ Error Correction
2. Coding Theory = information redundancy; ในวิชานี้โฟกัส **Error Control Code** เท่านั้น
3. แยกให้ชัด: **Coding (noise) ≠ Cryptography (ผู้ไม่ประสงค์ดี) ≠ Steganography (ซ่อนข้อมูล)**
4. **Modulator = Encoder, Demodulator = Decoder**; channel เป็น noisy
5. **Shannon / Channel Capacity**: ส่งได้เมื่อ **R < C**; **C = 1 − H(p)**; p = 0.5 → C = 0
6. **Repetition + Majority Voting**: error probability หลัง vote ≈ 3p² − 2p³ < p
7. **Hamming Distance = จำนวน bit ที่ต่าง**, **Hamming Weight = จำนวน bit ที่เป็น 1**
8. จาก **minimum distance d**: **detect ≤ d − 1**, **correct ≤ (d − 1)/2 (ปัดลง)**
9. **Notation (n, M, d)**: อยากได้ n สั้น, M มาก, d ใหญ่
10. **Linear code** = บวก mod 2 แล้วปิด; **Cyclic code** = shift แล้วยังอยู่ในกลุ่ม
11. **Generator Polynomial** ต้องเป็น factor ของ **xⁿ − 1**; degree = จำนวน parity bit; encode = data × g; decode = หารด้วย g, หารลงตัว (เศษ 0) = ถูก, เศษ ≠ 0 = มี error
12. โจทย์จริงท้ายคาบ = **(7,4) cyclic code + hardware encoder/decoder** แล้วทดสอบด้วยการใส่ error

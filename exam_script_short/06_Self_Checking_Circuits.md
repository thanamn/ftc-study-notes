# บทที่ 6 — FTC06 Self-Checking Circuits (ฉบับย่อ)

## แนวคิด

เราอยากให้ระบบ **ตรวจ fault ของตัวเองได้แบบ online** โดยไม่ต้องใช้สัญญาณทดสอบภายนอก **Self-checking = Concurrent Error Detection (CED)** ที่ตรวจจับได้ทั้ง temporary และ permanent fault, ตรวจจับเร็ว และระบุ field replaceable unit ได้ ภาพรวม: functional unit + **checker** ที่สร้าง syndrome/status; output ของ functional unit ต้องอยู่ใน **codespace** (ถ้าออกมาเป็น **non-codeword** แสดงว่าผิด)

**ข้อจำกัดสำคัญ:** checker **ไม่ได้ตรวจความถูกต้องเชิงตรรกะ** (ไม่รู้ว่า 2+2=4) มันตรวจแค่ว่าค่าเป็น codeword หรือไม่ ถ้า functional unit ให้ค่าผิดแต่ยังอยู่ในรูป codeword checker จะไม่รู้

**Error detecting code:** separable (Parity, Berger), non-separable (m-of-n, dual rail) **สี่กรณี FU+checker:** ทั้งคู่ดี / เฉพาะ FU ดี (false alarm แต่ปลอดภัย) / เฉพาะ checker ดี / ทั้งคู่เสีย (ต้องใช้ checker 2 output เพราะสัญญาณเดียว stuck-at-okay จะตรวจไม่เจอ → fault สะสม)

## นิยามรากฐาน

**Fault Secure (FS):** สำหรับ X ∈ N และ f ใด ๆ: **Y(X,f) = Y(X,λ) หรือ Y(X,f) ∉ S** (output ต้องเป็น codeword ที่ถูกต้อง หรือ non-codeword ห้ามเป็น codeword ที่ผิด)
**Self Testing (ST):** สำหรับทุก f มี X อย่างน้อยหนึ่งที่ **Y(X,f) ∉ S** (มี input ที่ทำให้มองเห็น fault)
ความต่าง: FS พูดถึงทุก fault และทุก input; ST พูดถึงการที่มี input บางตัวมองเห็น fault
**TSC = FS + ST** ข้อจำกัด: ไม่ใช่ทุก fault ตรวจได้ และ FS เดี่ยว ๆ ถ้ามี undetectable fault อยู่ fault ถัดไปอาจทำให้ FS เสีย

**Strongly Fault Secure (SFS)** เข้าเงื่อนไข 1 หรือ 2: (1) TSC สำหรับ {f}; (2) FS สำหรับ {f} **และ** SFS สำหรับ F−{f} ผลคือ **output error ตัวแรกเป็น non-codeword** (recursive) ทำไม FS ต้องคู่กับ ST: เพื่อจับ fault เร็วที่สุดก่อนที่ fault ใหม่จะเกิด

## Error Secure, Code Disjoint, SCD

**Error Secure (ES):** สำหรับ non-codeword input Xq: **Y(Xq,λ) ∉ S หรือ Y(Xq,λ) = Y(Xp,λ)** คือ output เป็น codeword ที่ถูกต้อง (fault masking) หรือ non-codeword
**Error Preserving = Code Disjoint (CD):** สำหรับ X นอก N: **Y(X,λ) ∉ S** (codeword input → codeword output; non-codeword → non-codeword)
ต่างกัน: ES ยอมให้ output เป็น codeword เดิมได้ (fault masking); CD บังคับ non-codeword input → non-codeword **SCD** เป็นนิยาม recursive แบบเดียวกับ SFS

## ทฤษฎีบท

**Self-checking logic network:** ถ้า LI (output interface) เป็น SFS และ SCD สำหรับ FI และ LII (internal) เป็น SFS สำหรับ FII → network ทั้งหมดเป็น SFS **Inverter-free network:** network ที่มีแต่ inverter-free block และ interface encode ด้วย unidirectional code (m-of-n, Berger) เป็น SFS สำหรับ unidirectional fault **ES/EP ที่ interface:** ES = error ที่ interface ไม่เคยทำให้เกิด incorrect codeword; EP = ในที่สุดก็สร้าง non-codeword ที่ observable interface

## Checkers

**Code Checker** (output encoded) และ **Prediction Checker** (output non-encoded): Duplication (สำเนา+เปรียบเทียบ), Parity prediction (ทำนาย parity ของ output จาก input แล้วเทียบ), Input regeneration (สร้าง input กลับจาก output ด้วย inverse logic แล้วเทียบ) มี simplified version ตรวจ input เดียว x1 = y0 ⊕ (y1·y2)
**Lemmas:** checker ต้องมี output ≥2 line และไม่มีขาคงที่; **FS ไม่จำเป็นสำหรับ checker** คุณสมบัติที่ต้องการ: 2 output line, **CD**, **ST**, **SCD**

## การออกแบบ checker

- **Parity code checker:** XOR tree แบ่ง 2 กลุ่ม (C0 จาก x8,x6,x4,x2,x0; C1 จาก x7,x5,x3,x1) → 2 output เป็น one-hot codeword {(0,1),(1,0)}, non-codeword {(0,0),(1,1)}; เป็น CD + ST
- **Two rail code checker:** duplication/comparison; ตัวอย่าง 2-pair รับ {x1x0,y1y0} ตรวจ {0101,0110,1001,1010}; sequence R,S,T ทำให้ ST สำหรับ stuck-at ทั้งหมดโดยไม่ขึ้นกับขนาดข้อมูล
- **1-of-n:** decode n → k (k = log₂n) ต่อ tree ของ two rail checker
- **m-of-2m:** แบ่ง 2m bit เป็น A,B ละ m; v,w = weight; **C0 = OR (v≥i)(w≥m−i) i คู่; C1 = OR (v≥j)(w≥m−j) j คี่** (เช่น 3-out-of-6)
- **TSC checker สำหรับ k-out-of-n** (แปลงเป็น 1-out-of-C(n,k) → m-of-2m), **separable code** (complement check bit), **Berger code**, **GPC**

**ตัวอย่างผิดที่ต้องรู้:** 5-input odd-parity checker ที่มี output ขาเดียว เป็น CD แต่ **ไม่ ST** เพราะ fault stuck-at-0 ที่ output อาจไม่ถูกตรวจ → จึงต้องมี 2 output **ตัวอย่าง conventional code checker ที่ถูกต้อง** รวม error signal สองตัวด้วย two-rail code checker (01,10 = G; 00,11 = B; กฎ GG → G นอกนั้น → B)

## TSC functional unit และ dual rail

**TSC MUX** และ **dual rail logic:** encode {0,1}→{01,10}; **ไม่มี inverter ในวงจร**, รักษา code หลัง operation → ทำให้ error เป็น **unidirectional** และได้ TSC สำหรับ unidirectional fault ตัวอย่าง F = āb + b c̄ + ac, F̄ = (a+b̄)(b̄+c)(ā+c̄) ตาราง 8 ชุด input แสดง FS + ST = TSC

**Contraction circuit** G' = วงจรที่ลบ line/output ที่ถูก fix โดย fault f **SFS → TSC theorem:** ถ้า G เป็น SFS, ไม่มี codeword ตรวจ f ได้, G' เป็น contraction ของ G → G' เป็น SFS **SFS functional unit** = non-redundant + non-inverter + output coding ด้วย unordered code

**TSC ด้วย parity prediction:** ให้ predictor สร้าง complement ของ output parity แล้วลบ XOR gate ออก → self-checking; ต้องตรวจว่า predictor testable ด้วย input codeword เท่านั้น **TSC ด้วย residue encoding:** แก้ "Find mod A" ให้สร้าง complement ของ residue, ใช้ two-rail checker แทน comparator **Partially self-checking unit:** ALU ที่ logical operation ตรวจด้วย low-redundancy code ไม่ได้ → บายพาสการตรวจเมื่อ code ใช้ไม่ได้ **Self-checking state machine (Moore):** input/output two-rail, state = k-out-of-n → next-state function เป็น monotonic (ไม่มีตัวแปร complemented) → ตรวจจับ unidirectional error

## วิธีทำโจทย์ข้อสอบเก่า

โจทย์ให้ input แล้วถามว่าเป็น FS/ST/TSC/SFS ไหม (codeword เป็น one-hot {(1,0),(0,1)}; (0,0),(1,1) = non-code) วิธี: **"เจนด้วยเบอร์ก่อน"** คือสร้าง truth table ก่อน แล้ว (1) ใส่ fault คำนวณ output ใหม่ทุกชุด (2) ถ้า output ทุกชุดเป็น codeword เดิม หรือ non-codeword ไม่มี codeword ผิด → **FS** (3) ถ้ามี input อย่างน้อยหนึ่งที่ output เป็น non-codeword → **ST** (4) ถ้า FS+ST ครบทุก fault → **TSC**; ถ้า recursive ตามนิยาม → **SFS** หลัก monotonic: เมื่อผิดต้องไปทาง non-code word เท่านั้น **ห้ามกลับไปที่ code space**

## ต้องจำทันที และกับดัก

**จำทันที:** FS (ถูกต้องหรือ non-codeword), ST (มี input เห็น fault), TSC=FS+ST, SFS (recursive, output error แรกเป็น non-codeword), ES, CD, SCD

**กับดัก:** FS ≠ ST; checker ไม่จำเป็นต้อง FS แต่ต้อง CD+ST; ES ยอมให้ output เป็น codeword เดิม แต่ CD ไม่ยอม; checker ตรวจแค่ความเป็น codeword ไม่ตรวจความถูกเชิงตรรกะ

# บทที่ 5 — FTC05 Coding Theory (ฉบับย่อ)

## กรอบแนวคิด

สื่อจริงมี noise เสมอ (fiber, satellite, hard disk) **Coding theory** ป้องกันข้อมูลจาก noise; **Cryptography** จากศัตรู; **Steganography** ซ่อนข้อมูล โครงสร้างการสื่อสาร: source → source encode → encrypt → channel encode → modulate → channel (มี noise) → demodulate → channel decode → decrypt → source decode โดย **modulator = encoder, demodulator = decoder** และ coding theory อยู่ที่ชั้น channel encode/decode

**Shannon noisy-channel coding theorem:** capacity C, rate R → ถ้า R < C ส่งได้เกือบไม่มี error; ถ้า R > C ทำ error ให้เล็กตามอำเภอใจไม่ได้ C = B·log₂(1+S/N) (เป็นข้อความเชิง asymptotic ต้องใช้ข้อความยาว) ตัวอย่าง: ทำให้ error เป็น 10⁻¹⁵ บน BSC p=0.1 ด้วย repetition code ต้องยาว ~63 เท่า แต่ Shannon บอกสองเท่าพอ

**Binary symmetric channel (BSC):** พลิกบิตอิสระด้วย p < 1/2; ความน่าจะเป็นผิด t บิต = C(n,t)p^t(1−p)^(n−t); code {000,111} ถอดด้วยเสียงข้างมาก P_err = 3p² − 2p³ < p เมื่อ p<1/2; capacity C(p) = 1 − H(p) (C(0.1)≈0.53, p=0.5 → C=0)

## นิยาม code และตัวอย่าง

code C บน alphabet Σ = subset ของ Σ*; q-nary = alphabet q symbol; binary = {0,1} เรื่องเล่า Alice/Bob: C1 = คำ 2 บิต (error ใดก็หายนะ), C2 = {000,011,101,110} (ตรวจจับ error เดียว), C3 = {00000,01101,10110,11011} (แก้ error เดียว) — สื่อสารข้อมูลเดียวกัน เลือก code ได้หลายแบบ

## Hamming weight/distance และกฎ detect/correct

**Hamming weight** w(c) = จำนวนบิตที่ไม่ใช่ศูนย์ **Hamming distance** h(x,y) = จำนวนตำแหน่งที่ต่าง **Minimum distance** h(C) = ค่าต่ำสุดของทุกคู่ที่ต่างกัน

- **ตรวจจับได้ถึง s error** ถ้า **d ≥ s+1**
- **แก้ได้ถึง t error** ถ้า **d ≥ 2t+1**
- **แก้ t + ตรวจจับ s พร้อมกัน:** **d ≥ t+s+1** → **SEC-DED ต้อง d ≥ 4** (Hamming code d=3 + parity bit)
- อีกมุมที่อาจารย์ใช้: detect ≤ d−1, correct ≤ (d−1)/2 (ปัดลง)

## (n, M, d) และ code rate

**(n, M, d):** n = ความยาว, M = จำนวน codeword, d = min distance (เช่น (2,4,1), (3,4,2), (5,4,3)) code ดี = n เล็ก, M ใหญ่, d ใหญ่ **A_q(n,d)** = M มากสุด: A_q(n,1)=q^n, A_q(n,n)=q; กฎต่อ code: d คี่ → A₂(n,d)=A₂(n+1,d+1); d คู่ → A₂(n,d)=A₂(n−1,d−1) **code rate** R = log_q(M)/n

## Linear และ cyclic code

**Linear code:** ผลบวก modulo-2 ของสอง codeword ใด ๆ ยังอยู่ใน code **Cyclic code** = linear + cyclic shift ใด ๆ ของ codeword ยังเป็น codeword (ใช้จริงเพราะแปลงเป็น shift register ได้)

## Generator polynomial และการ encode

data k บิตมองเป็นพหุนามดีกรี k−1 คูณด้วย **generator polynomial** ดีกรี r = n−k **ต้องเป็นตัวหารของ x^n − 1** ตรวจจับ single error ทั้งหมดและ burst error ที่สั้นกว่า n−k

**แยกตัวประกอบที่ต้องจำ:** x⁵+1 = (x+1)(x⁴+x³+x²+x+1); **x⁷+1 = (x+1)(x³+x+1)(x³+x²+1)** (n=7 → (7,4) code)

**สองวิธี encode:** (1) **non-separable** คูณ d(x)·g(x) (data/check ปนกัน) (2) **systematic ด้วยการหารยาว:** เลื่อน data ซ้าย n−k ตำแหน่ง → หารด้วย g(x) → ต่อ remainder

**ทำ (7,4) ทีละขั้น:** g(x)=x³+x+1 = 1011, ข้อมูล 0101 → shift เป็น 0101000 → หารด้วย 1011 แบบ modulo-2 (บวก=ลบ=XOR, ไม่ยืม) → remainder 100 → codeword = **0101100** (separable) คำอื่น: 1001→1001110, 0010→0010110, 1110→1110100, 0000→0000000

**Decode:** หารคำที่รับด้วย g(x) → **remainder 0 = ไม่พบ error**; ≠0 = พบ error (บ้างรูปแบบ 3 บิตยังให้ 0 ได้ = หลุด) **ฮาร์ดแวร์:** linear feedback shift register จำนวน delay element = ดีกรี g; k cycle แรกส่ง raw message ขณะ register หาร, r cycle สุดท้ายตัด feedback แล้ว flush parity

## Error models

symmetric/asymmetric, single/multiple, **unidirectional** (ทั้งสองทิศแต่ไม่พร้อมกันใน codeword เดียว), byte error

## Overlapped parity (ECC) และ syndrome

**Overlapped parity code** = SEC, data 8 บิต + check 4 บิต; เงื่อนไข **2^k − 1 ≥ m + k**; check bit อยู่ตำแหน่งกำลังสอง (1,2,4,8) = C1..C4
**Check bit formulas:** C1 = D1⊕D2⊕D4⊕D5⊕D7; C2 = D1⊕D3⊕D4⊕D6⊕D7; C3 = D2⊕D3⊕D4⊕D8; C4 = D5⊕D6⊕D7⊕D8
**syndrome** = XOR ของ check ที่ส่งกับที่คำนวณใหม่: **0 = ไม่มี error; ตั้ง 1 บิต = error ที่ check bit; ตั้ง >1 บิต = ค่าตัวเลขบอกตำแหน่ง data error** ตัวอย่าง syndrome 1100 ชี้ D8 เสีย → กลับบิตนั้น

## Error-detecting code

**Checksum:** single-precision (mod 2^n), double-precision (mod 2^(2n)), residue (end-around carry), Honeywell (pair) ตัวอย่าง 10101001+00111001 = 11100010 → checksum = complement 00011101
**Constant-weight / m-of-n:** ทุก codeword มีหนึ่งเท่ากัน → ตรวจจับ unidirectional error ได้ทั้งหมด
**Arithmetic weight** = จำนวน signed power of 2 น้อยสุดที่ต้องบวกเพื่อเปลี่ยนค่าถูกเป็นผิด **AN code** แทน N ด้วย A·N; **residue code** แทนด้วย (N, C), C = N mod A **Low-cost residue** A = 2^a−1 → หา N mod (2^a−1) ด้วยการบวกส่วน a-bit แบบ end-around carry **ไม่ต้องหาร** (เช่น 0101 1101 1010 1110 mod 15 → 1100) และ **รักษา code หลังการบวก/ลบ/คูณ**

## Unordered, m-of-n, Berger, dual rail

**Unordered code:** ไม่มี codeword ใด cover อีกอัน (X cover Y ถ้า X ≥ Y ทุกตำแหน่ง) → unidirectional error เปลี่ยน codeword หนึ่งเป็นอีกอันไม่ได้
**m-of-n code:** ยาว n มีหนึ่งพอดี m ตัว, non-separable, d=2
**Berger code:** separable; นับจำนวนหนึ่งใน k data bit เป็น binary แล้วต่อด้วย **bit-by-bit complement**; c = ⌈log₂(k+1)⌉, n = k+c; **ตรวจจับ unidirectional error ได้ทั้งหมด** (เช่น k=7, 0101000 มีหนึ่ง 2 ตัว → 010 → complement 101 → 0101000 101)
**Dual rail:** encode 1 บิตเป็นคู่ **1-of-2** (0→01, 1→10), สร้างจาก **non-inverter** ได้ทั้งหมด, รักษา code หลัง operation ตัวอย่าง F = āb + b c̄ + ac, F̄ = (a+b̄)(b̄+c)(ā+c̄)

## การประยุกต์

**UPC-A:** checksum weight 3,1,3,1..., A = 10, ตรวจจับ single-digit error ทั้งหมดและ transposition ส่วนใหญ่ **JPEG Huffman:** บีบอัด 20–90% และใช้ error detection/correction ช่วย reconstruct

## จุดเชื่อมกับข้อสอบเก่า

โจทย์: (n,M,d), Berger code, "การบ้านหารยาว" (cyclic) และ code ที่มี code length 6 ให้แสดง notation → นับ codeword + คำนวณ pairwise Hamming distance หา d แล้วเขียน (n,M,d) ให้แสดงตาราง distance เสมอ โจทย์กริด Hamming ให้ตอบด้วยกฎระยะ: single-error correction ต้องการ d≥3; double-error detection ต้องการ d≥3; SEC-DED ต้องการ d≥4

## ต้องจำทันที และกับดัก

**จำทันที:** weight/distance; detect d≥s+1, correct d≥2t+1, SEC-DED d≥4; (n,M,d); cyclic g หาร x^n−1; (7,4) g=1011 → 0101100; syndrome; Berger = complement check bit

**กับดัก:** detect/correct ใช้เงื่อนไขต่างกัน; modulo-2 บวก=ลบ (หารไม่ยืม); เลกเชอร์ให้ codeword non-systematic (0100111) แต่แบบฝึกหัดให้ systematic (0101100); "locate ตำแหน่ง error" คือหัวใจของ correction

# เฉลยข้อสอบกลางภาค 2110473 Fault Tolerant Computing (12 ต.ค. 2569) — ฉบับเต็ม

> **ที่มา:** ข้อความถอดจากกระดาษข้อสอบ + ภาพถ่ายข้อสอบ (ไดอะแกรมข้อ 1–3, 5) ผู้สอบรหัส 6733101021
> **การตรวจสอบ:** คำนวณด้วยสคริปต์ใน `tools/` (`solve_exam.py`, `solve_q24.py`, `verify_s2_s3.py`, `sim_om.py`, `solve_q5.py`, `solve_q4.py`)
> **ข้อ 4:** ต้องใช้ค่าบิต 42 บิตจากตาราง (8×6) — โปรดส่งค่าบิตมา แล้วผมจะเติม 4.1–4.4 ให้ครบ (ตอนนี้ให้วิธีทำ + ตัวอย่างจริง)

---

# ข้อ 1 — พื้นฐาน Fault Tolerant Computing

## 1.1 Fault Tolerant Computing ในมุมของ Safety และ Liveness

**Safety property** = "จะไม่มีอะไรแย่ ๆ เกิดขึ้นเลย" (something bad never happens)
**Liveness property** = "จะต้องมีสิ่งดี ๆ เกิดขึ้นในที่สุด" (something good eventually happens)

**คำตอบ:** FTC คือการออกแบบให้ระบบรักษาทั้งสอง property ไว้แม้มี fault:
- **Safety** → ระบบไม่ปล่อย erroneous output / ผลลัพธ์อันตรายออกไป (ไม่ลุกลามเป็น failure ที่ catastrophic) โดยใช้ fault masking หรือ fail-safe
- **Liveness** → ระบบยังให้บริการได้หรือกลับมาให้บริการได้ในที่สุด (availability / reliability / recovery)

พูดสั้น ๆ: FTC ทำให้ *Safety* คงอยู่ (ไม่มี bad output หลุด) และ *Liveness* คงอยู่ (บริการดำเนินต่อไปหรือกลับมาได้)

## 1.2 รูปที่ 1.1 (Design Techniques) — ลากเส้นแสดง Recovery, Self-Checking, Fail Safe

รูปที่ 1.1: `System Normal State` → (Specification mistakes, Implementation mistakes, External disturbances, Component defects) → `Software Faults` / `Hardware Faults` → `Errors` → `System failures`
โซน: **Fault Avoidance** (ก่อน fault) → **Fault Masking** ( faults → errors ) → **Fault Tolerance** ( errors → system failures )

| สิ่งที่ลาก | วางตรงไหน | เหตุผล |
|---|---|---|
| **Self-Checking** | รอยต่อ Faults → Errors (concurrent detection) ลากจากกล่อง Faults/Errors ไปยัง checker ที่ให้ error signal | จับ error ทันทีที่เกิด |
| **Recovery** | ระหว่าง Errors → System failures: ลากเส้นย้อนจาก Error กลับมาที่ Normal State | ตรวจพบแล้วกู้ state กลับ |
| **Fail-Safe** | ที่ปากทางก่อน System failures (ฝั่ง output/ผู้ใช้) | เมื่อพังบังคับให้ผลลัพธ์เป็นค่าปลอดภัย |
| **Fault Masking** (โซน) | ครอบช่วง Faults → Errors | บังไม่ให้ fault กลายเป็น error |

## 1.3 Bathtub Curve — 3 แนวลูกศร

รูปที่ 1.2: แกนตั้ง Failure rate, แกนนอน Time; 3 ช่วง = Infant Mortality (ลูกศร 1), Working Life (ลูกศร 2), Wearout (ลูกศร 3)

| ลูกศร | ผล | วิธี |
|---|---|---|
| **1** (ดัน Infant Mortality ซ้าย/ให้หมดเร็ว) | ลด/ตัด infant mortality | Burn-in, Screening, Stress test, ควบคุมคุณภาพการผลิต (QC) |
| **2** (กด Working Life ให้ต่ำลง) | ลด random failure rate λ | ชิ้นส่วนคุณภาพสูง λ ต่ำ, ลดจำนวน component, ออกแบบเรียบง่าย, เพิ่ม redundancy |
| **3** (ดัน Wearout ไปขวา) | ยืดอายุก่อนสึกหรอ | Preventive/Predictive maintenance, Derating, ระบายความร้อน, เปลี่ยนชิ้นส่วนสึกก่อนกำหนด |

## 1.4 รูปที่ 1.3 — Recovery Line (P0–P3, fault ที่ P1 เวลา t14)

รูป: 4 process P0–P3, message ส่งไปมา, **fault ที่ P1 ตรง t14** ต้องลาก recovery line สั้นสุด 2 เส้น

- **เส้น A: ทุก process กลับเวลาตรงกันที่ tj** → recovery line แบบ **Strongly Consistent** (ถ้าตัดแล้วไม่มี message ค้างใน transit) เป็นแบบ **Coordinated/Synchronous**
- **เส้น B: เวลาต่างกัน ti, tj, tk, tl** → recovery line แบบ **Consistent** (Uncoordinated) ได้ ตราบที่ **ไม่มี orphan message**; ถ้ามี → **Inconsistent**

**เกณฑ์ตัดสิน:** ไม่มี message ค้าง = Strongly Consistent; มี in-transit แต่ไม่มี orphan = Consistent; มี orphan = Inconsistent
**ข้อกำหนด:** recovery line ต้องลากผ่านทุก process และอยู่ **ก่อน** จุด fault (t14)

## 1.5 รูปที่ 1.4 — Data Space (SEC-DED)

**[ต้องดูรูป]** กริดจุดที่จุดติดกัน (แนวตั้ง/แนวนอน/ทแยง) ห่างกัน Hamming distance 1; มีจุดดำ 1 จุดเป็น codeword แล้วเติม codeword อื่นสำหรับ **SEC/DED**

**หลักการ:** SEC-DED ต้องมี **minimum distance ≥ 4** (SEC อย่างเดียวใช้ ≥3)
**วิธีเติม:** วาง codeword ให้ระยะ Chebyshev (จำนวนก้าวต่ำสุดในกริด, ทแยงนับ 1) ระหว่างคู่ใด ๆ **≥ 4** เช่นวางเป็น lattice เว้นระยะสม่ำเสมอทุก 4 ช่อง

> หมายเหตุ: "hamming distance = 1" ในโจทย์หมายถึง *จุดติดกัน* ห่าง 1 บิต ไม่ใช่ min distance ของรหัส (=1) เพราะถ้า min distance = 1 จะไม่มีการป้องกันเลย

---

# ข้อ 2 — Reliability Block Diagram (ให้ Ra, Rb, Rk; ไม่คิด reliability ของเส้นเชื่อม)

> **สรุปสูตรข้อ 2.1 (แยก Ra, Rb, Rk):**
> - **Rs0 = Ra · Rb**
> - **Rs1 = [1 − (1−Ra)²] · [1 − (1−Rb)³]**
> - **Rs2 = Rk·[1−(1−Ra)²]·[1−(1−Rb)²] + (1−Rk)·[1 − (1−Ra·Rb)²]**
> - **Rs3 = Rk²·[1−(1−Ra)³]·[1−(1−Rb)³] + 2Rk(1−Rk)·{1 − [1 − (1−(1−Ra)²)(1−(1−Rb)²)]·[1 − Ra·Rb]} + (1−Rk)²·[1 − (1−Ra·Rb)³]**
>
> (ข้อ 2.2–2.5 โจทย์ให้ Ra = Rb = Rk = R จึงแทนค่าแล้วแก้หา R)

**S0 = A อนุกรม B:** `Rs0 = Ra·Rb` (ถ้า Ra=Rb=R → R²)

**S1 = A ขนาน 2 ตัว อนุกรมกับ B ขนาน 3 ตัว:**
`Rs1 = [1−(1−Ra)²]·[1−(1−Rb)³]` (Ra=Rb=R → 6R² − 9R³ + 5R⁴ − R⁵)

**S2 = บริดจ์** (keystone บน K):
`Rs2 = Rk·[1−(1−Ra)²][1−(1−Rb)²] + (1−Rk)·[1−(1−RaRb)²]` (Ra=Rb=Rk=R → 2R² + 2R³ − 5R⁴ + 2R⁵)

**S3 = บริดจ์ 3 สาย 2 K** (Ra=Rb=Rk=R): `Rs3 = 4R⁸ − 18R⁷ + 27R⁶ − 10R⁵ − 9R⁴ + 4R³ + 3R²`
(ตรวจกับ enumeration แล้ว: Ra=0.9, Rb=0.8, Rk=0.95 → S2 = 0.948960, S3 = 0.990510)

## 2.2 Rs1 > 1.5·Rs0 (R = Ra = Rb)
```
6R² − 9R³ + 5R⁴ − R⁵ > 1.5R² → R²(−R³ + 5R² − 9R + 4.5) > 0
root ≈ 0.7959  →  R < 0.796
```

## 2.3 Rs2 > 1.5·Rs0 (R = Ra = Rb = Rk)
```
2R² + 2R³ − 5R⁴ + 2R⁵ > 1.5R² → R²(0.5 + 2R − 5R² + 2R³) > 0
root ≈ 0.7647  →  R < 0.765
```

## 2.4 Rs3 > 1.5·Rs0 (R = Ra = Rb = Rk)
```
Rs3 = 4R⁸ − 18R⁷ + 27R⁶ − 10R⁵ − 9R⁴ + 4R³ + 3R²
Rs3 − 1.5R² = R²·(4R⁶ − 18R⁵ + 27R⁴ − 10R³ − 9R² + 4R + 1.5) > 0
root ≈ 0.809  →  R < 0.809   (ตรวจ: R=0.809 → +0.00004; R=0.810 → −0.00209)
```

## 2.5 สรุป
เรียง reliability: **S3 ≥ S2** และ **S3 ≥ S1** → **S3 สูงสุดและยอมรับ R ได้กว้างสุด (R < 0.809)**
**คำตอบ: เลือก S3 (บริดจ์ 3 สาย 2K)**

> เกร็ด: S2 (บริดจ์เดี่ยว) ต่ำกว่า S1 ในบางช่วง (R=0.8: S2=0.911 < S1=0.952) → การเพิ่มบริดจ์ให้โครงที่ขนานอยู่แล้วไม่ได้ช่วยเสมอ แต่ S3 (3 สาย + K 2 ตัว) ชนะทุกกรณี

---

# ข้อ 3 — Byzantine Fault Tolerance (6 Nodes, N2/N3 Faulty)

**เงื่อนไข Oral Message:** ต้องมี **n ≥ 3m + 1**
n = 6, m = 2 → 3(2)+1 = **7** > 6 → **ไม่ผ่าน → Consensus FAIL**

**สาธิต (จาการจำลอง OM(2)):** N1 (ซื่อสัตย์) ส่ง A ให้ N2–N6; N2, N3 faulty ส่ง R
- OM(2)/OM(1)/OM(0) ดำเนินไป แต่เพราะ node ไม่พอ (ต้อง 7)
- ผล: loyal node บางตัวตัดสินไม่ตรงกับตัวอื่น (เช่น N4=N5=A แต่ N6 = "ตัดสินไม่ได้/TIE") → **loyal nodes ไม่ได้ข้อตกลงร่วมกัน**

**คำตอบ:** ไม่สามารถบรรลุ consensus ได้เพราะ **6 < 3m+1 = 7** ต้องเพิ่มเป็น **อย่างน้อย 7 nodes** จึงจะทน faulty 2 ตัวได้

---

# ข้อ 4 — Coding Theory (ตาราง 8×6)

**Code A (แถว 1–7):** `001100, 011100, 011110, 010010, 011111, 110011, 111011`

> หมายเหตุ: แถว 7 พิมพ์มา 7 หลัก ผมตีความว่าเป็น 6 หลัก `111011` (ตัดบิตเกินทิ้ง) — ถึงแถว 7 เปลี่ยน ค่า d ก็ยังเท่าเดิม เพราะคู่ที่ทำให้ d = 1 อยู่ในแถว 1–6

## 4.1 Notation ของ Code A

นับ M = จำนวน codeword = **7** และหา d = min pairwise Hamming distance (จับคู่ C(7,2) = 21 คู่)

ตารางยกตัวอย่างคู่ที่สำคัญ:
```
d(001100, 011100) = 1        d(011100, 011110) = 1
d(011110, 011111) = 1        d(110011, 111011) = 1
d(001100, 010010) = 4        d(001100, 110011) = 6   ...
```
ค่าต่ำสุดที่พบ = **1** → **n = 6, M = 7, d = 1**

**คำตอบ 4.1: Code A = (6, 7, 1)**

## 4.2 ใส่ Data แถวที่ 8

**เกณฑ์:** เลือก 6-bit word ที่ไม่ซ้ำกับคำเดิม (ทำให้ Code A ยังคง d = 1 เป็น (6, 8, 1))
ถ้าอยากได้คำที่ "ห่างจากทุกคำเดิมมากที่สุด" (ไม่ลดคุณภาพรหัส) — ตัวเลือกที่ดีคือ **`100110`** (ระยะต่ำสุดจากคำเดิม = 3) หรือ `100101`
**คำตอบ 4.2: แถว 8 = `100110` → Code A = (6, 8, 1)**

## 4.3 Berger Code (เลือกคำ `001100`)

separable code: นับจำนวนบิต 1 ใน data (k บิต) → เขียนเป็น binary → ต่อด้วย **complement**
- k = 6 → c = ⌈log₂(6+1)⌉ = 3 บิต
- จำนวน 1 ของ `001100` = 2 → เขียน 3 บิต = `010`
- complement ของ `010` = **`101`**

**คำตอบ 4.3: Berger = `001100 101`**

## 4.4 Cyclic Code (10,6), g(x) = x⁴+x³+x²+x+1 = `11111`

n = 10, k = 6, r = n−k = 4; generator = `11111` (ทุกสัมประสิทธิ์เป็น 1)

- **systematic (หารยาว):** เลื่อน data ซ้าย 4 → `0011000000` → หารด้วย `11111` → **remainder = `0110`** → ต่อท้าย data
  **codeword = `001100` + `0110` = `0011000110`** (ตรวจ: `0011000110` หารด้วย `11111` ลงตัว rem = 0)
- **non-separable (คูณด้วย g):** `001100` × `11111` = **`0010000100`**
- **decode:** เอา codeword ที่รับมาหารด้วย g → rem = 0 : ไม่มี error; rem ≠ 0 : มี error
- **วงจร (Hardware):** LFSR ดีกรี 4 = delay element (D flip-flop) 4 ตัว, XOR tap ทุกตำแหน่ง (เพราะ g = `11111`); ป้อน data ทีละบิต 6 รอบ (คำนวณ remainder) แล้ว 4 รอบสุดท้ายสลับสวิตช์ flush parity ออกมา

> **[หมายเหตุความไม่แน่นอน]** ถ้าค่าบิตแถว 7 ในกระดาษจริงไม่ใช่ `111011` (เช่นเป็น `110111`) ค่า d ยังคง = 1 อยู่ดี และคำตอบ 4.1–4.4 ไม่เปลี่ยน

---

# ข้อ 5 — Self-Checking Circuits

Input codespace N = 4 กรณี: (a,b,c,d) = (0,0,1,1), (0,1,1,0), (1,1,0,0), (1,0,0,1); output codeword one-hot {(1,0),(0,1)}, non-code = (0,0),(1,1)

## 5.1 วงจรซ้าย X = AD + CD, Y = AB + BC — Fault: ขา A ของ Gate AD Stuck-at-0
เมื่อ A ของ gate AD ค้าง 0 → เทอม AD = 0 → **X = CD**

| (a,b,c,d) | ปกติ (x,y) | สถานะ | หลัง fault | ผล |
|---|---|---|---|---|
| (0,0,1,1) | (1,0) | cw | (1,0) | ยังถูก (FS) |
| (0,1,1,0) | (0,1) | cw | (0,1) | ยังถูก (FS) |
| (1,1,0,0) | (0,1) | cw | (0,1) | ยังถูก (FS) |
| (1,0,0,1) | (1,0) | cw | (0,0) | **non-code → ตรวจเจอ (ST)** |

**สรุป 5.1:** ไม่มี codeword ผิดโผล่ → **FS**; มีอินพุตที่ทำให้เป็น non-code → **ST** → **เป็น Totally Self Checking (TSC)** (และ SFS)
**อินพุตที่ยัง Fault Secure** = (0,0,1,1), (0,1,1,0), (1,1,0,0); **อินพุตที่ Self Testing** = (1,0,0,1)

## 5.2 วงจรขวา X = ĀB̄CD + ĀBC̄D, Y = ĀBCD̄ + AB̄C̄D̄ — Fault: ขา C ของ Gate ĀB̄CD Stuck-at-1
เมื่อ C ของ gate ĀB̄CD ค้าง 1 → เทอม ĀB̄CD → **ĀB̄D**

| (A,B,C,D) | ปกติ (x,y) | หลัง fault | ผล |
|---|---|---|---|
| (0,0,1,1) | (1,0) | (1,0) | ยังถูก |
| (0,1,0,1) | (1,0) | (1,0) | ยังถูก |
| (0,1,1,0) | (0,1) | (0,1) | ยังถูก |
| (1,0,0,0) | (0,1) | (0,1) | ยังถูก |

**สรุป 5.2:** ทุกอินพุต codeword ให้ output เดิม → **fault ตรวจไม่เจอด้วย codeword ใดเลย** → **ไม่มี Self Testing** → **ไม่เป็น TSC** แต่ยัง **Fault Secure** → **เป็น Strongly Fault Secure (SFS)**
**อินพุตที่เป็น Self Testing = ไม่มีเลย; วงจรเป็น SFS**

---

# สรุปแนวทางตอบ
1. **ข้อ 1** เน้นเหตุผล/คำศัพท์ + วาดเส้นบนแผนภาพให้ตรงโซน
2. **ข้อ 2** ใช้ series/parallel/keystone; คำตอบเป็นช่วง R < ค่า
3. **ข้อ 3** กับดัก: 6 < 3m+1 → **fail** (อย่าหาคำตอบ consensus ที่สำเร็จ)
4. **ข้อ 4** ต้องใช้ค่าบิตจริง: notation (n,M,d), Berger = complement ของจำนวน 1, cyclic (10,6) ใช้ g=11111 + LFSR ดีกรี 4
5. **ข้อ 5** "เจนด้วยเบอร์ก่อน": ดู output หลังใส่ fault เป็น codeword เดิม / codeword ผิด / non-code → FS, ST → TSC; FS แต่ไม่ ST สำหรับ fault เดี่ยว → SFS

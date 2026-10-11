# FTC05 Coding Theory — Visual Notes

> บันทึกคำอธิบายภาพสไลด์ (visual notes) วิชา Fault Tolerant Computing หัวข้อ Coding Theory
> ข้อความบนสไลด์ภาษาอังกฤษ รูปแบบ สูตร ตาราง ชื่อตัวแปร และคำศัพท์ทางเทคนิคคงไว้ตามต้นฉบับทุกประการ

---

## Slide 1

**Title:** Home Exercise: Checkpointing

**Bullet text:**
- Find the consistent cuts in the figure below (passing by <ไอคอนลายทแยงสีฟ้า เต็มกรอบสี่เหลี่ยม>) 
- The recovery line that you found is *consistent*, *strongly consistent* or *inconsistent*?

**Diagram:** แผนภาพเวลา (timeline) แบบ distributed system มีแกนนอน 4 เส้น ระบุปลายทางขวาเป็น **P0, P1, P2, P3** (บนลงล่าง) บนแต่ละเส้นมีกล่องสี่เหลี่ยมสีน้ำเงินเข้ม (checkpoint) หลายกล่อง และมีลูกศรดำเชื่อมระหว่าง process (message) ทิศทางทแยง

- บนเส้น P1 มีเครื่องหมาย **X สีแดง** (ตำแหน่งความล้มเหลว) อยู่ทางขวา
- มีเส้นโค้งประสีแดง (red curve) พาดผ่านจากบริเวณกลางไปยังขวา และเส้นโค้งสีน้ำเงิน (blue curve) อีกเส้นหนึ่ง พาดผ่านจากบนลงล่าง สื่อถึง recovery line / consistent cut ที่ต้องตรวจสอบ
- เส้นสีน้ำเงินเข้มแนวนอนคือ life line ของแต่ละ process; กล่องสีน้ำเงินคือ state/checkpoint ณ จุดต่าง ๆ

---

## Slide 5

**Title:** Various Stages of Data Processing

**Diagram (block diagram 2 คอลัมน์):**

ฝั่งซ้าย (ผู้ส่ง):
```
Digital Source
      ↓
Source Encoder
      ↓
Encryption
      ↓
Channel Encode
      ↓
Modulator
```
ฝั่งขวา (ผู้รับ):
```
Digital Link
      ↓
Source Decoder
      ↓
Decryption
      ↓
Channel Decode
      ↓
Demodulator
```

- ตรงกลางระหว่างสองคอลัมน์ มีป้ายกำกับทฤษฎีที่เกี่ยวข้อง:
  - **Information Theory** (ระหว่าง Source Encoder ↔ Source Decoder)
  - **Cryptography** (ระหว่าง Encryption ↔ Decryption)
  - **Coding Theory** (ระหว่าง Channel Encode ↔ Channel Decode)
- ตรงกลางล่าง: **Channel** มีลูกศรชี้จากซ้ายไปขวา (จาก Modulator ไป Demodulator)
- ใต้ Channel มีสัญลักษณ์สายฟ้า (lightning) พร้อมป้าย **Noise**

---

## Slide 6

**Title:** Reliable Communication

**Diagram (block diagram):**
- **source string** (ลูกศรสีน้ำเงินลง) → กล่อง **encoder** (สีเหลือง) → กล่อง **noisy channel** (สีเหลือง) → กล่อง **decoder** (สีเหลือง) → ลูกศรสีน้ำเงินขึ้น → **decoded string**
- ลูกศรสีน้ำเงินเชื่อมระหว่างกล่องทั้งสาม

**Bullet text:**
- In practice, most media are not perfect, *Noisy channels*:
  – *Fiber-optic line, Satellite link, Hard disk, ...*
- Can we recover the original message (without errors) from a noisy code string?
- We focus two things:
  – *Length of the code string*
  – *Probability of error*

---

## Slide 9

**Title:** Basic Concept

**Intro text:** *Error-correcting codes* are used to correct messages when they are transmitted through noisy channels

**Diagram 1 — Error correcting framework:**
- กล่อง **message source** → (ป้าย **W** บนลูกศร) → กล่อง **Encoding** → ป้าย **code word** → ผ่าน **channel** (มี **noise** ระบุ C(W) noise) → ได้ **code word W'** → กล่อง **Decoding** → (ป้าย **W**) → กล่อง **user**
- ป้ายแดงใต้ไดอะแกรม: **Error correcting framework**

**Diagram 2 — Example:**
- กล่อง **message YES or NO** → (ป้าย **YES**) → กล่อง **Encoding** (ภายในระบุ **YES → 00000**, **NO → 11111**) → ส่งผ่านสัญญาณรบกวน (สัญลักษณ์คลื่น/สี่เหลี่ยม) → **00000** → **01001** → กล่อง **Decoding** (ภายในระบุ **01001** แล้ว **00000**) → (ป้าย **YES**) → กล่อง **user**

**Definitions / text:**
- A *code* **C** over an alphabet **Σ** is a subset of **Σ\*** (**C ⊆ Σ\***)
- A *q -nary code* is a code over an alphabet of **q** -symbols
- A *binary code* is a code over the alphabet **{0,1}**

**Examples of codes:**
- C₁ = {00, 01, 10, 11}
- C₂ = {000, 010, 101, 100}
- C₃ = {00000, 01101, 10111, 11011}

---

## Slide 11

**Title:** Claude Elwood Shannon

**Image:** ภาพถ่ายขาวดำของ Claude Elwood Shannon นั่งอยู่หน้ากากเครื่องคอมพิวเตอร์/แผงสวิตช์ (รูปอยู่ครึ่งซ้ายของสไลด์)

**Text (ด้านขวา):**
- **"The father of Information Theory"**
- *American mathematician, electrical engineer, and cryptographer*
- *(Apr.30, 1916 – Feb.24, 2001)*

---

## Slide 18

**Title:** Coding of a path avoiding an enemy territory

**Story text:**
- **Story:** Alice and Bob share an identical map gridded as shown. Only Alice knows the route through which Bob can reach her avoiding the enemy territory. Alice wants to send Bob the following information about the safe route he should take

**Code string (ข้อความสีดำตัวพิมพ์ใหญ่):**
`NNWNNWWS SWWNNNNWWN`

**Diagram (แผนที่ตาราง grid):**
- ด้านบนระบุชื่อ **Alice**, ด้านล่างขวาระบุ **Bob**
- มีป้าย **HQ** อยู่มุมบนซ้าย (จุดเริ่มต้น)
- ด้านขวาระบุ **N** พร้อมลูกศรทิศเหนือ (เข็มทิศ: ลูกศรขึ้น = N, ลูกศรขวา)
- มีพื้นที่แรเงา (เส้นทแยง, hatched) แทน enemy territory หลายบริเวณ
- มีเส้นทาง (route) เป็นเส้นหัก/มุมฉาก พร้อมลูกศรทิศทาง แสดงเส้นทางจาก HQ ไปยังจุด **x** ของ Bob โดยเลี่ยงพื้นที่แรเงา
- จุดสิ้นสุดคือเครื่องหมาย **x** ใกล้ป้าย **Bob** ที่มุมล่างขวา

---

## Slide 21

**Title:** Richard Wesley Hamming

**Text (ด้านซ้าย):**
- **"Hamming Distance"**
- *American mathematician*
- **"The purpose of computing is insight, not numbers"**
- *(Feb.11, 1915 – Jan.7, 1998)*

**Image:** ภาพขาวดำของ Richard Wesley Hamming กำลังยืนบรรยายหน้า whiteboard (มีสมการคณิตศาสตร์เขียนอยู่บนกระดาน) โดยมี silhouettes ของผู้ฟังอยู่ด้านหน้า (รูปอยู่ครึ่งขวา)

---

## Slide 23

**Title:** Hamming Distance

**Bullet text:**
- **Hamming Distance h(x, y):**
  – The number of positions where words x and y differs
  ex:  h(10101; 01100) = 3,  h(fourth; eighth) = 4
- **Properties:**
  – h(x,y) = 0 ⇔ x = y
  – h(x,y) = h(y,x)
  – h(x,z) ≤ h(x,y) + h(y,z) ⇒ *triangle inequality*
- **Minimal distance:**
  h(C) = min{h(x,y)|x, y ∈ C, x ≠ y}

**สูตรปิดท้าย (ตัวหนา/แดง):**
- Code C can **detect** up to s errors if **h(C) ≥ s + 1**
- Code C can **correct** up to t errors if **h(C) ≥ 2t + 1**

---

## Slide 24

**Title:** Hamming VS Shannon

**Table:**

| Hamming | Shannon |
|---|---|
| Focus on codewords itself | Directly deal wt encoding and decoding functions |
| Look at explicit codes | Not explicit at all |
| Fundamental trade off: rate vs distance (easy to handle) | Fundamental trade off: rate vs error |
| Worst case errors | Stochastic errors |

---

## Slide 40

**Title:** Factorization of Xⁿ-1 (Xⁿ+1)

**Table:** คอลัมน์ **n** และ **xⁿ + 1 =**

| n | xⁿ + 1 = |
|---|---|
| 1 | (x + 1) |
| 2 | (x + 1)² |
| 3 | (x + 1)(x² + x + 1) |
| 4 | (x + 1)⁴ |
| 5 | (x + 1)(x⁴ + x³ + x² + x + 1) |
| 6 | (x + 1)²(x² + x + 1)² |
| 7 | (x + 1)(x³ + x + 1)(x³ + x² + 1) |
| 8 | (x + 1)⁸ |
| 9 | (x + 1)(x² + x + 1)(x⁶ + x³ + 1) |
| 10 | (x + 1)²(x⁴ + x³ + x² + x + 1)² |
| 11 | (x + 1)(x¹⁰ + x⁹ + x⁸ + x⁷ + x⁶ + x⁵ + x⁴ + x³ + x² + x + 1) |
| 12 | (x + 1)⁴(x² + x + 1)⁴ |
| 13 | (x + 1)(x¹² + x¹¹ + x¹⁰ + x⁹ + x⁸ + x⁷ + x⁶ + x⁵ + x⁴ + x³ + x² + x + 1) |
| 14 | (x + 1)²(x³ + x + 1)²(x³ + x² + 1)² |
| 15 | (x + 1)(x² + x + 1)(x⁴ + x + 1)(x⁴ + x³ + 1)(x⁴ + x³ + x² + x + 1) |
| 16 | (x + 1)¹⁶ |
| 17 | (x + 1)(x⁸ + x⁵ + x⁴ + x³ + 1)(x⁸ + x⁷ + x⁶ + x⁴ + x² + x + 1) |
| 18 | (x + 1)²(x² + x + 1)²(x⁶ + x³ + 1)² |
| 19 | (x + 1)(x¹⁸ + x¹⁷ + x¹⁶ + ⋯ + x + 1) |
| 20 | (x + 1)⁴(x⁴ + x³ + x² + x + 1)⁴ |
| 21 | (x + 1)(x² + x + 1)(x³ + x + 1)(x³ + x² + 1)(x⁶ + x⁴ + x² + x + 1)(x⁶ + x⁵ + x⁴ + x² + 1) |
| 22 | (x + 1)²(x¹⁰ + x⁹ + x⁸ + x⁷ + x⁶ + x⁵ + x⁴ + x³ + x² + x + 1)² |
| 23 | (x + 1)(x¹¹ + x⁹ + x⁷ + x⁶ + x⁵ + x + 1)(x¹¹ + x¹⁰ + x⁶ + x⁵ + x⁴ + x² + 1) |
| 24 | (x + 1)⁸(x² + x + 1)⁸ |
| 25 | (x + 1)(x⁴ + x³ + x² + x + 1)(x²⁰ + x¹⁵ + x¹⁰ + x⁵ + 1) |
| 26 | (x + 1)²(x¹² + x¹¹ + x¹⁰ + x⁹ + x⁸ + x⁷ + x⁶ + x⁵ + x⁴ + x³ + x² + x + 1)² |
| 27 | (x + 1)(x² + x + 1)(x⁶ + x³ + 1)(x¹⁸ + x⁹ + 1) |
| 28 | (x + 1)⁴(x³ + x + 1)⁴(x³ + x² + 1)⁴ |
| 29 | (x + 1)(x²⁸ + x²⁷ + ⋯ + x + 1) |
| 30 | (x + 1)²(x² + x + 1)²(x⁴ + x + 1)²(x⁴ + x³ + 1)²(x⁴ + x³ + x² + x + 1)² |
| 31 | (x + 1)(x⁵ + x² + 1)(x⁵ + x³ + 1)(x⁵ + x³ + x² + x + 1)(x⁵ + x⁴ + x² + x + 1)(x⁵ + x⁴ + x³ + x + 1)(x⁵ + x⁴ + x³ + x² + 1) |

---

## Slide 41

**Title:** Modulo-2 Multiplication

**Bullet text:**
- The **5th** bit of the product is the *modulo-2* sum of the corresponding bits of the multiplicand shifted **0** times, **3** times, and **4** times
- If multiplicand is *fed in serially* – we add the shifted multiplicand
- Shifting done by *delay elements*
- This cyclic code is *not separable* - data and check bits within **110000100011101** are not separable

**Example computation (การคูณแบบ long multiplication):**

```
        10001100101
    ×        11001
    ---------------
        10001100101
       00000000000
      00000000000
     10001100101
    10001100101
    ---------------
    110000100011101
```

(แถวของ partial product มีเส้นกรอบสี่เหลี่ยมแนวตั้ง เน้นคอลัมน์บิตที่ 5 ของผลคูณ)

**Circuit diagram:** วงจร shift register / LFSR ประกอบด้วย
- delay elements **D** หลายตัวต่อกัน (4 ตัวในแนวกลาง)
- สัญญาณป้อนเข้าด้านซ้ายมีป้าย **o₄**, แล้วตามด้วย **o₁** ระหว่าง D, **o₂**, **o₁**
- มี XOR gate (วงกลมเครื่องหมาย +) ระหว่าง delay element ตัวแรกและตัวที่สอง (มี **i** กำกับอยู่ด้านใน)
- ทางขวาสุด: สัญญาณรวมผ่าน XOR-like gate ไปยังป้าย **Encoded Output**
- ด้านล่างมีเส้นสัญญาณย้อนกลับจากซ้ายไปขวา ไปยังป้าย **Data**

---

## Slide 42

**Title:** Operation of Encoding Code

**Table (columns: shift clock | input data | O₄ | i₃ | O₃,O₂,O₁ | encoded output):**

| shift clock | input data | O₄ | i₃ | O₃,O₂,O₁ | encoded output |
|---|---|---|---|---|---|
| 1 | 1 | 0 | 1 | 000 | 1 |
| 2 | 0 | 1 | 1 | 100 | 0 |
| 3 | 1 | 0 | 1 | 110 | 1 |
| 4 | 0 | 1 | 1 | 111 | 1 |
| 5 | 0 | 0 | 0 | 111 | 1 |
| 6 | 1 | 0 | 1 | 011 | 0 |
| 7 | 1 | 1 | 0 | 101 | 0 |
| 8 | 0 | 1 | 1 | 010 | 0 |
| 9 | 0 | 0 | 0 | 101 | 1 |
| 10 | 0 | 0 | 0 | 010 | 0 |
| 11 | 1 | 0 | 1 | 001 | 0 |
| 12 | 0 | 1 | 1 | 100 | 0 |
| 13 | 0 | 0 | 0 | 110 | 0 |
| 14 | 0 | 0 | 0 | 011 | 1 |
| 15 | 0 | 0 | 0 | 001 | 1 |

**Bullet text:**
- **i3** is the input to the **O3** delay element

**Circuit diagram:** เหมือน Slide 41 (shift register/LFSR)
- delay elements **D** ต่อกัน โดยมีป้าย **o₄**, **o₁**, **o₂**, **o₁** กำกับ
- มี XOR gate (วงกลม +) ระหว่าง D ตัวแรกกับตัวที่สอง (ป้าย **i** ด้านใน)
- ขวาสุด: ป้าย **Encoded Output**
- ด้านล่าง: **Data**
- หมายเลขสีน้ำเงินเหนือวงจร: **110000100011101**
- หมายเลขสีน้ำเงินใต้วงจร (ตรงป้าย Data): **10001100101**

---

## Slide 43

**Title:** Decoding Through Division by Generator Polynomial

**การหารยาวแบบ modulo-2 (long division) สองกรณี:**

กรณีซ้าย (ไม่มี่ error):
```
110000100011101 : 11001 = 10001100101
11001
-----
 10100
 11001
 -----
  11010
  11001
  -----
   11111
   11001
   -----
    11001
    11001
    -----
     00000
```
ผลลัพธ์ = **10001100101**, เศษ = **00000** (วงรีสีน้ำเงินล้อมรอบ)

กรณีขวา (มี error — บิตที่วงกลมสีแดงในเลขตั้งต้นคือ '1' ที่ตำแหน่งหนึ่ง):
```
110000100111101 : 11001 = 10001100110
11001
-----
 10100
 11001
 -----
  11011
  11001
  -----
   10111
   11001
   -----
    11100
    11001
    -----
     01011
```
- คำว่า **error!!** ตัวเอียงสีแดง (อยู่ข้างบิตที่วงกลมสีแดงในตัวตั้ง)
- เศษ = **01011** (วงรีสีแดงล้อมรอบ)

**Bullet text:**
- Division by **11001**
- Subtraction *modulo-2* - identical to addition
- *Zero remainder* indicates no error detected
- If a single error occurs – **110000100111101** (บิตที่ผิดเน้นสีแดง ตัว '1' ตรงกลาง) - *non-zero remainder*

---

## Slide 44

**Title:** Three Bit Errors

**การหารยาวแบบ modulo-2 สองกรณี (เกิด error หลายบิต):**

กรณีซ้าย (ตัวตั้ง = `110000111010101`, มีวงกลมสีแดงล้อม 2 บิตที่ตำแหน่ง 9 และ 10):
```
110000111010101 : 11001 = 10001101101
11001
-----
 10111
 11001
 -----
  11100
  11001
  -----
   10110
   11001
   -----
    11111
    11001
    -----
     11001
     11001
     -----
      00000
```
เศษ = **00000** (วงรีสีแดงล้อม) — แสดงว่า error ไม่ถูกตรวจจับ

กรณีขวา (ตัวตั้ง = `110000111011101`, มีวงกลมสีแดงล้อมบิตหนึ่ง):
```
110000111011101 : 11001 = 10001110011
11001
-----
 10011
 11001
 -----
  10100
  11001
  -----
   11011
   11001
   -----
    10110
    11001
    -----
     11111
     11001
     -----
      00110
```
เศษ = **00110** (วงรีสีแดงล้อม)

**Bullet text:**
- **110000111010101** instead of **110000100011101** - errors not detected (erroneously)
  (มีลูกศรชี้ไปยังเศษ 00000 ทางซ้าย และลูกศรชี้ไปที่คำว่า "zero remainder")
- If errors are adjacent - **110000011011101** (บิตที่ผิดเน้นสีแดง) - *non-zero remainder* indicates an error
  (ลูกศรชี้จากข้อความนี้ไปยังเศษ 00110 ทางขวา)

---

## Slide 51

**Title:** Cyclic code **encoding** example 2

**Formula line:** K = (0111), g(x) = (1 + x + x³)

**Side computation (มุมซ้ายบน, กรอบสี่เหลี่ยม — การหารยาว):**
```
0111
1101
----
0111
0111
----
0111
0111
----
0100011
```

**Circuit diagram (ด้านขวาบน):**
- สัญญาณป้อนเข้าจากซ้าย: **1 1 1 0 →** เข้าที่ป้าย **K**
- XOR gate แรก (วงกลม **+**) เอาต์พุตมีป้าย **A1** → ไปยัง XOR gate ที่สอง (วงกลม **+**) → เอาต์พุตป้าย **A3**, และป้าย **E**
- ล่างลงมา: delay elements **D1 → D2 → D3** เรียงต่อกัน มีลูกศรจาก D3 กลับขึ้นไปยัง XOR แรกและจาก D2 ขึ้นไปยัง XOR ที่สอง (เส้น blue)
- ด้านขวา: **E** → **1 1 0 0 0 1 0 →**
- ข้อความตัวแดง: **E = (0100011)**

**Table (columns: K | D1 | A1 | D2 | D3 | A3 (E)):**

| K | D1 | A1 | D2 | D3 | A3 (E) |
|---|---|---|---|---|---|
| 0 | x | 0 | x | x | 0 |
| 1 | 0 | 1 | x | x | 1 |
| 1 | 1 | 0 | 0 | x | 0 |
| 1 | 1 | 0 | 1 | 0 | 0 |
| 0 | 1 | 1 | 1 | 1 | 0 |
| 0 | 0 | 0 | 1 | 1 | 1 |
| 0 | 0 | 0 | 0 | 1 | 1 |

(คอลัมน์ **A3 (E)** อยู่ในกรอบสี่เหลี่ยมสีแดง)

---

## Slide 52

**Title:** Cyclic code **decoding** example 2

**Formula line:** E = (0100011), g(x) = (1 + x + x³) ⇒ K(X) = E(X) + K(X)(X + X³)

**Side computation (มุมซ้ายบน, กรอบสี่เหลี่ยม):**
```
0100011
 1101   :01
-----
 10111
 1101   :1
 -----
  1101
  1101  :1
  -----
   000
```

**Circuit diagram:**
- ด้านขวา: **E ← 0 1 0 0 0 1 1** (ลูกศรชี้ซ้ายเข้าใกล้ XOR ตัวขวา ป้าย **A1**)
- XOR gate (วงกลม **+**) → XOR gate ที่สอง (ป้าย **A3**) → ออกทางซ้ายเป็น **K ← 0 1 1 1**
- delay elements เรียงย้อนทาง: **D1 ← D2 ← D3** (ลูกศรชี้ไปทางซ้าย)
- มีเส้นสัญญาณจากด้านล่างของ D3 กลับไปยังปลายทาง K (ด้านซ้ายสุด)

**Table (columns: E | D1 | D2 | D3 | A1 | A3 (K)):**

| E | D1 | D2 | D3 | A1 | A3 (K) |
|---|---|---|---|---|---|
| 0 | x | x | x | 0 | 0 |
| 1 | 0 | x | x | 1 | 1 |
| 0 | 1 | 0 | x | 1 | 1 |
| 0 | 1 | 1 | 0 | 1 | 1 |
| 0 | 1 | 1 | 1 | 1 | 0 |
| 1 | 0 | 1 | 1 | 1 | 0 |
| 1 | 0 | 0 | 1 | 1 | 0 |

(คอลัมน์ **A3 (K)** อยู่ในกรอบสี่เหลี่ยมสีแดง)

---

## Slide 53

**Title:** Cyclic code **decoding** example 2

**Formula line:** E = (010**1**011), g(x) = (1 + x + x³) ⇒ K(X) = E(X) + K(X)(X + X³)
(ตัวเลข '1' ที่ 4 เน้นสีแดง)

**Side computation (มุมซ้ายบน, กรอบสี่เหลี่ยม):**
```
0101011
 1101   :01
-----
 11111
 1101   :1
 -----
  0101
  0000  :0
  -----
   101
```
(บรรทัด 101 เน้นสีแดง และบรรทัด 0000:0)

**Circuit diagram:** เหมือน Slide 52
- ด้านขวา: **E ← 0 1 0 1 0 1 1** (บิต '1' ตัวที่ 4 เน้นสีแดง ป้าย **A1**)
- XOR gates สองตัว → ออกทางซ้ายเป็น **K ← 0 1 1 0** (บิต '0' ตัวสุดท้ายเน้นสีแดง ป้าย **A3**)
- delay elements **D1 ← D2 ← D3**

**Table (columns: E | D1 | D2 | D3 | A1 | A3 (K)):**

| E | D1 | D2 | D3 | A1 | A3 (K) |
|---|---|---|---|---|---|
| 0 | x | x | x | 0 | 0 |
| 1 | 0 | x | x | 1 | 1 |
| 0 | 1 | 0 | x | 1 | 1 |
| 1 | 1 | 1 | 0 | 0 | 0 |
| 0 | 0 | 1 | 1 | 0 | 1 |
| 1 | 1 | 0 | 1 | 0 | 1 |
| 1 | 1 | 0 | 0 | 0 | 0 |

(แถว E=1 (แถวที่ 4, D1=1) เน้นสีแดงเฉพาะค่า; คอลัมน์ **A3 (K)** อยู่ในกรอบสี่เหลี่ยมสีแดง)

---

## Slide 55

**Title:** Error Detection

**Diagram (Venn-style สองวง):**
- วงรีด้านซ้ายสีฟ้า: **Data space** ภายในมี **Data words** (จุดสีน้ำเงินหลายจุด บางจุดเป็นสี่เหลี่ยมสีน้ำเงินเข้ม = data word)
- วงรีด้านขวาสีเหลือง: **Code space** ภายในมี **Codewords** (จุดสีเขียวเข้ม) และ **Errors** (จุดสีแดง อยู่บริเวณล่างขวา)
- ป้าย **Error space** อยู่มุมล่างขวาของวงสีเหลือง (บริเวณที่มีจุดแดง = **Noncodewords**)
- ลูกศรเชื่อม **Encoding** จากวง data ไปยังวง code (ชี้ไปที่ codeword)
- ลูกศรเชื่อม **Decoding** จากวง code กลับไปยังวง data
- เส้นประ (dashed) จาก codeword ไปยังจุดแดงแต่ละจุด (แสดงการเกิด error → noncodewords)

---

## Slide 61

**Title:** Home Exercise: Cyclic code 2/4 (Encoding)

**Formula line:** m = (0101), g(x) = (1 + x² + x³)

**Side computation (มุมซ้ายบน, กรอบสี่เหลี่ยม):**
```
0101
1011
----
0101
0101
----
0101
0101
----
0100111
```

**Circuit diagram:**
- สัญญาณป้อนเข้าจากซ้าย: **1 0 1 0 →** เข้าป้าย **K**
- XOR gate แรก (วงกลม **+**) เอาต์พุตป้าย **A2** → XOR gate ที่สอง → เอาต์พุตป้าย **A3**, **E**
- ป้าย **A0** อยู่บนเส้นที่มาจาก K ขึ้นไปยัง XOR แรก
- delay elements **D1 → D2 → D3** เรียงต่อ; จาก D3 ขึ้นไปยัง XOR แรก, จาก D2 ขึ้นไปยัง XOR ที่สอง (เส้น blue)
- ด้านขวา: **E → 1 1 1 0 0 1 0 →**
- ข้อความตัวแดง: **E = (0100111)**

**Table (columns: K (A0) | D1 | D2 | A2 | D3 | A3 (E)):**

| K (A0) | D1 | D2 | A2 | D3 | A3 (E) |
|---|---|---|---|---|---|
| 0 | x | x | 0 | x | 0 |
| 1 | 0 | x | 1 | x | 1 |
| 0 | 1 | 0 | 0 | x | 0 |
| 1 | 0 | 1 | 0 | 0 | 0 |
| 0 | 1 | 0 | 0 | 1 | 1 |
| 0 | 0 | 1 | 1 | 0 | 1 |
| 0 | 0 | 0 | 0 | 1 | 1 |

(คอลัมน์ **A3 (E)** อยู่ในกรอบสี่เหลี่ยมสีแดง)

---

## Slide 63

**Title:** Cyclic code **decoding** example 3/4

**Formula line:** E = (0100011), g(x) = (1 + x² + x³) ⇒ K(X) = E(X) + K(X)(X² + X³)

**Side computation (มุมซ้ายบน, กรอบสี่เหลี่ยม):**
```
0100011
 1101   :01
-----
 10111
 1101   :1
 -----
  1101
  1101  :1
  -----
   000
```

**Circuit diagram:**
- ด้านขวา: **E ← 0 1 0 0 0 1 1** (เข้าป้าย **A1**)
- XOR gate แรก → XOR gate ที่สอง (ป้าย **A3**) → ออกทางซ้ายเป็น **K ← 0 1 1 1**
- delay elements เรียงย้อนทาง: **D1 ← D2 ← D3**
- มีเส้นสัญญาณย้อนกลับจาก D3 ไปยัง K

**Table (columns: E | D1 | D2 | D3 | A1 | A3 (K)):**

| E | D1 | D2 | D3 | A1 | A3 (K) |
|---|---|---|---|---|---|
| 0 | x | x | x | 0 | 0 |
| 1 | 0 | x | x | 1 | 1 |
| 0 | 1 | 0 | x | 1 | 1 |
| 0 | 1 | 1 | 0 | 1 | 1 |
| 0 | 1 | 1 | 1 | 1 | 0 |
| 1 | 0 | 1 | 1 | 1 | 0 |
| 1 | 0 | 0 | 1 | 1 | 0 |

(คอลัมน์ **A3 (K)** อยู่ในกรอบสี่เหลี่ยมสีแดง)

---

## Slide 64

**Title:** Error Controls for Digital Systems

**Diagram (block diagram):**
- กล่อง **Digital Systems** ด้านซ้ายบน
- ลูกศรหนาสีน้ำเงินจาก Digital Systems ไปทางขวา (ป้าย **Data Transmission**) → กล่อง **Corrector**
- จาก Corrector มีลูกศรหนาไปทางขวา → ป้าย **Corrected Output**
- จาก Digital Systems มีลูกศรลง (ป้าย **Data Operation**) → กล่อง **Checker** (ด้านล่าง)
- จากกลาง (บนเส้น Data Transmission) มีลูกศรลงเข้าสู่ Checker
- จาก Checker มีลูกศรขึ้นเข้าสู่ Corrector
- จาก Checker มีเส้นบางสีน้ำเงินไปทางขวา → ป้าย **Error Signal**

---

## Slide 67

**Title:** Error Correcting Code Function

**Diagram (block diagram / signal flow):**
- ด้านซ้ายล่าง: **Data In** → (ป้าย **M** บนเส้น) → กล่อง **Memory**
- ก่อนถึง Memory มีการแยกสัญญาณลงไปยังกล่อง **f** (เล็ก) ด้านล่าง; จาก f ออกเป็น (ป้าย **K**) เข้า Memory
- จาก Memory ออกสองทาง: ทางบน (ป้าย **M**) → กล่อง **f** → (ป้าย **K**) → กล่อง **Compare**
- ทางล่างจาก Memory (ป้าย **K**) → ตรงเข้าสู่ **Compare**
- ออกจาก Memory ทางบน (ก่อนเข้า f) ยังแยกขึ้นไปยังกล่อง **Corrector** (อยู่กลางบน)
- จาก Corrector สัญญาณไปทางซ้ายเป็น **Data Out** (มีป้าย **M** บนเส้น)
- จาก Compare มีเส้นสัญญาณย้อนขึ้นไปยัง Corrector และไปทางซ้ายบนเป็น **Error Signal**
- (จาก Memory ทาง M ยังมีเส้นแยกขึ้นไปทางซ้ายบนเข้าสู่เส้น Data Out)

---

## Slide 68

**Title:** Overlapped Parity Code

**Bullet text:**
- Single Error Correcting (SEC)/ 8-Data bits wt 4-Check bits

**Table / bit layout:**
- แถวหัว บน: **12  11  10  9  8  7  6  5  4  3  2  1** พร้อมป้าย **Bit Position** ทางขวา
- 4 แถวข้อมูล:

| row | 12 | 11 | 10 | 9 | 8 | 7 | 6 | 5 | 4 | 3 | 2 | 1 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | 0 | 1 | 0 | 1 | 0 | 1 | 0 | 1 | 0 | 1 | 0 | 1 |
| 2 | 0 | 1 | 1 | 0 | 0 | 1 | 1 | 0 | 0 | 1 | 1 | 0 |
| 3 | 1 | 0 | 0 | 0 | 0 | 1 | 1 | 1 | 1 | 0 | 0 | 0 |
| 4 | 1 | 1 | 1 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |

- แถวป้ายกำกับ (ใต้ข้อมูล): **C4** (ในคอลัมน์ 8), **C3** (คอลัมน์ 4), **C2** (คอลัมน์ 2), **C1** (คอลัมน์ 1) — พร้อมป้าย **Check Bit** ทางขวา
- แถวป้ายกำกับล่าง: **D8 D7 D6 D5** (คอลัมน์ 12,11,10,9), **D4 D3 D2** (คอลัมน์ 7,6,5), **D1** (คอลัมน์ 3) — พร้อมป้าย **Data Bit** ทางขวา

**Formula & definition (ด้านล่าง):**
- **2ᵏ − 1 ≥ m + k**
- **m = data bits**
- **k = parity bits**

---

## Slide 70

**Title:** Compute Check

**Table / bit layout:** เหมือน Slide 68 (หัวตารางและข้อมูลชุดเดียวกัน)

- แถวหัว: **12  11  10  9  8  7  6  5  4  3  2  1** — ป้าย **Bit Position**

| row | 12 | 11 | 10 | 9 | 8 | 7 | 6 | 5 | 4 | 3 | 2 | 1 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | 0 | 1 | 0 | 1 | 0 | 1 | 0 | 1 | 0 | 1 | 0 | 1 |
| 2 | 0 | 1 | 1 | 0 | 0 | 1 | 1 | 0 | 0 | 1 | 1 | 0 |
| 3 | 1 | 0 | 0 | 0 | 0 | 1 | 1 | 1 | 1 | 0 | 0 | 0 |
| 4 | 1 | 1 | 1 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |

- ป้าย **Check Bit**: **C4** (คอลัมน์ 8), **C3** (คอลัมน์ 4), **C2** (คอลัมน์ 2), **C1** (คอลัมน์ 1)
- ป้าย **Data Bit**: **D8 D7 D6 D5** (12,11,10,9), **D4 D3 D2** (7,6,5), **D1** (3)

**Formulas (สมการคำนวณ check bits):**
- **C1 = D1 ⊕ D2 ⊕ D4 ⊕ D5 ⊕ D7**
- **C2 = D1 ⊕ D3 ⊕ D4 ⊕ D6 ⊕ D7**
- **C3 = D2 ⊕ D3 ⊕ D4 ⊕ D8**
- **C4 = D5 ⊕ D6 ⊕ D7 ⊕ D8**

(⊕ = เครื่องหมาย XOR วงกลมบวก)

---

## Slide 72

**Title:** Applying Syndrome

**Table / bit layout:** เหมือน Slide 68/70 โดยคอลัมน์ **12** ถูกกรอบสี่เหลี่ยมสีแดงล้อมรอบทั้ง 4 แถว

- แถวหัว: **12  11  10  9  8  7  6  5  4  3  2  1** — ป้าย **Bit Position**

| row | 12 | 11 | 10 | 9 | 8 | 7 | 6 | 5 | 4 | 3 | 2 | 1 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | 0 | 1 | 0 | 1 | 0 | 1 | 0 | 1 | 0 | 1 | 0 | 1 |
| 2 | 0 | 1 | 1 | 0 | 0 | 1 | 1 | 0 | 0 | 1 | 1 | 0 |
| 3 | 1 | 0 | 0 | 0 | 0 | 1 | 1 | 1 | 1 | 0 | 0 | 0 |
| 4 | 1 | 1 | 1 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |

- ป้าย **Check Bit**: **C4** (คอลัมน์ 8), **C3** (คอลัมน์ 4), **C2** (คอลัมน์ 2), **C1** (คอลัมน์ 1)
- ป้าย **Data Bit**: **D8 D7 D6 D5** (12,11,10,9), **D4 D3 D2** (7,6,5), **D1** (3)

**ข้อความสรุป (ด้านล่าง, ตัวหนา):**
- **Syndrome 1100 detects D8 as faulty** (หมายเลข **1100** เน้นสีแดง)
- หมายเหตุ: ค่าสี่บิตในคอลัมน์ 12 (แถวบนลงล่าง) = 0, 0, 1, 1 ⇒ อ่านจากบนลงล่างเป็น **1100** (D8, D7, D6, D5)

---

## Slide 79

**Title:** Arithmetic weight errors

**Computation (ด้านบน):**
- **Unsigned addition**

```
  0010 0111 0010 0001
+ 0101 1000 1101 0011
----------------------
  0111 1111 1111 0100   ← Correct sum
  1000 0000 0000 0100   ← Erroneous sum
```

- กล่องคำอธิบายสีเขียว (ด้านขวา): **How a single carry error can lead to an arbitrary number of bit-errors (inversions)**
- กล่องสีน้ำเงินระบุ (ตัวแดง): **errornous carry of 1** (มีเส้นชี้ไปยังตำแหน่งบิตใน erroneous sum)

**Definition text (ตัวหนา/เอียง):**
- ***Arithmetic weight errors:*** Minimum number of signed powers of 2 that must be added to the correct value to turn it into the erroneous result (contrast with Hamming weight of an error)

**Example 1 (ด้านล่างซ้าย):**
```
Example 1
__________
0111 1111 1111 0100
1000 0000 0000 0100    (มีเส้นแบ่งแนวตั้ง | ระหว่างบิตก่อนหลักสุดท้าย)
16 = 2⁴
0000 0000 0001 0000
1
Single, positive
```

**Example 2 (ด้านล่างขวา):**
```
Example 2
__________
1101 1111 1111 0100
0110 0000 0000 0100
−32752 = −2¹⁵ + 2⁴
‾1000 0000 0001 0000
2
Double, negative
```

---

## Slide 81

**Title:** Residue Code

**Bullet text:**
- If *M*mod*A* = 0, then
  |(X * Y)modM|modA = ((XmodA) * (YmodA))modA
- *Preserve code* after operation

**Diagram (block diagram):**
- ด้านซ้าย: อินพุต **X** และ **Y** เข้ากล่อง **(X * Y)modM**
- เอาต์พุตจากกล่องนี้ไปทางขวาเป็น **Result** (เส้นตรง)
- จากเส้น Result มีการแยกสัญญาณลงเข้าสู่กล่อง **Mod Generator**
- จาก Mod Generator ลงเข้าสู่กล่อง **Comparator**
- ด้านซ้ายล่าง: อินพุต **XmodA** และ **YmodA** เข้ากล่อง **(X * Y)modA** → เอาต์พุตเข้าสู่กล่อง **Comparator**
- จาก Comparator มีลูกศรไปทางขวาเป็น **Detection Signal**

---

## Slide 84

**Title:** Arithmetic on Residue-coded operands

**Bullet text:**
- *Add/subtract:* Data and check parts are handled separately
  (x, C(x)) ± (y, C(y)) = (x±y, (C(x) ± C(y)) mod A)
- *Multiply:*
  (a, C(a)) × (x, C(x)) = (a×x, (C(a)×C(x)) mod A)
- *Divide/square-root:* difficult

**Diagram (block diagram):**
- อินพุต **x** และ **C(x)** (ด้านซ้ายบน) เข้ากล่อง **Main Arithmetic Processor**
- อินพุต **y** และ **C(y)** (ด้านซ้ายล่าง) ก็เข้าสู่ Main Arithmetic Processor เช่นกัน (และแยกเข้าสู่ Check Processor ด้านล่าง)
- เอาต์พุตจาก Main Arithmetic Processor ไปทางขวาเป็น **z** และ **C(z)**
- มีการแยกสัญญาณ (จากเส้น z) ลงเข้าสู่กล่อง **mod A**
- อินพุต y, C(y) เข้ากล่อง **Check Processor** (ด้านล่าง)
- เอาต์พุตของ Check Processor และของ mod A เข้าสู่ **Compare** (วงรี)
- จาก Compare มีลูกศรลงเป็น **Error Indicator**
- กล่องคำอธิบายสีเขียว (ด้านขวาล่าง): **Arithmetic processor with residue checking**

---

## Slide 89

**Title:** Dual Rail Code

**Bullet text:**
- **1-of-2 Code**
  {0,1} ⇒ {01,10}
- **Easy Implementation** (Encoder/Decoder)
- *Preserve code* after operation
- *Non-Inverter Circuit*

**Circuit/Logic diagrams (ทางขวา เป็นคู่บิต x, x' → z, z'):**

แถวที่ 1 — Buffer/Wire:
- `x —— z`  คู่กับ  `x —— z` / `x' —— z'`
- แสดงได้ว่า: `x ——— z` และ `x' ——— z'` (เส้นตรง ไม่กลับค่า)

แถวที่ 2 — Inverter:
- สัญลักษณ์ NOT gate (triangle + วงกลม): `x →(NOT)→ z`
- คู่ dual: `x —— z`, `x' —— z'` แบบไขว้ (เส้นตัดกัน – crossover)

แถวที่ 3 — AND gate:
- `x, y →(AND)→ z` (สัญลักษณ์ D-shape)
- ลูกศรหนา (⇒) ไปยังฝั่ง dual:
  - AND gate: `x, y → z`
  - gate รูปโค้ง (dual): `x', y' → z'`

แถวที่ 4 — OR gate:
- `x, y →(OR)→ z`
- ฝั่ง dual:
  - `x, y', y → z` (gate อีกชนิด)
  - AND gate: `x', y' → z'`

(แต่ละ gate ทางซ้ายเป็นแบบ single-rail, ทางขวาเป็นคู่ dual-rail โดยใช้ทั้ง x/x' และ y/y' และสะท้อนเป็น z/z')

---

## Slide 90

**Title:** Dual Rail Code example

**Formulas:**
- **F = āb + bč + ac**
- **F̄ = (a + b̄)(b̄ + c)(ā + č)**

**Circuit diagrams:**
- วงบน (สำหรับ F): อินพุต **ā, b** → AND gate, **č** (แยกไปที่ AND ตัวที่สองด้วย), **a, c** → AND gates หลายตัว แล้วรวมกันด้วย OR gate → เอาต์พุต **F**
  - อินพุตที่แสดง: ā, b, č, a, c
- วงล่าง (สำหรับ F̄): อินพุต **a, b̄** → OR gate, **c, ā, č** → OR gates หลายตัว แล้วรวมกันด้วย AND gate → เอาต์พุต **F̄**
  - อินพุตที่แสดง: a, b̄, c, ā, č

(ทั้งสองวงวาดด้วยเส้นสีฟ้า/น้ำเงิน, gate รูปทรง D และโค้ง)

---

## Slide 91

**Title:** Applications: Error detection in UPC-A

**Bullet text:**
- **Checksum codes:** Given a data vector x₁, x₂, . . . , xₙ, encode the data by attaching the checksum xₙ₊₁ to the end
  (Σ_{j=1 to n+1} wⱼxⱼ = 0 mod A)
  (Weight vector wⱼ elements are predetermined constants)
- **Capabilities:** All single-digit errors; Most transposition errors
- **Example:** For the UPC-A checksum scheme,
- w = 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1; A= 10
- **Checking:** Verify that weighted mod-10 sum of all 12 digits is 0
- **12-digit UPC-A universal product code:**
  Sum odd indexed digits: **0+6+0+2+1+5 = 14**
  Multiply by 3: **14×3 = 42**
  Add even-indexed digits: **42+3+0+0+9+4 = 58**
  Compute check digit: **60 −58 = 2**

**Images (ด้านขวา):**
- รูปบาร์โค้ด UPC-A พร้อมเลข **0 36000 29145 2** (ด้านล่างมีหมายเลขตำแหน่ง 1 2 3 4 5 6 7 8 9 10 11) โดยหลักสุดท้าย **2** ถูกวงกลมสีแดงล้อม
- มีเส้น/กรอบสีเขียวครอบบางแท่งของบาร์โค้ด
- มุมขวาบน: ไอคอนแสดงเลข **4 ▶ 1011100 ▶** พร้อมภาพแท่งบาร์โค้ดย่อ (แสดงการเข้ารหัส 7 บิตต่อหนึ่งหลัก)
- ข้อความ: **Bar code uses 7 bits per digit, with different encodings on the right and left halves and different parities at various positions**

---

## Slide 92

**Title:** Applications: JPEG Huffman Coding

**Bullet text:**
- *Huffman codes* are widely used and very effective technique for compression data; saving of **20% to 90%**
- JPEG compression standard

**Images (ด้านล่าง 3 ภาพ เรียงซ้าย-ขวา — ภาพนกกระยางขาว (egret) บนพื้นฟ้า):**
- ภาพที่ 1: **Original image** (ภาพต้นฉบับ คมชัด)
- ภาพที่ 2: **Reconstructed image under Huffman code table error** (ภาพมีสัญญาณรบกวน/แตกเป็นบล็อก)
- ภาพที่ 3: **Reconstructed image wt error detection/correction** (ภาพถูกแก้ไข กลับมาคมชัด)

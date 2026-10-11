# FTC06 Self Checking — Visual Notes (ชุด B)

อธิบายเนื้อหาจากภาพสไลด์บรรยาย หัวข้อ Self-Checking / Self-Testing Checker
ทุกข้อความภาษาอังกฤษ ป้าย ตาราง สูตร และชื่อตัวแปร คงไว้ตามต้นฉบับทุกตัวอักษร

---

## Slide 44

**หัวข้อ (Title):** What's wrong?

**ภาพซ้าย — "Conventional code checker"**
- ป้าย "Input" ชี้ไปยังวงรีขนาดใหญ่ที่ภายในแบ่งเป็นสองส่วน: บริเวณบนป้ายกำกับ "Code space" และบริเวณล่างป้ายกำกับ "Error space"
- มีจุด (dot) หนึ่งจุดใน "Code space" และหนึ่งจุดใน "Error space"
- ลูกศรสองเส้นมีป้ายกำกับ "f" ลากจากทั้งสองจุดไปยังวงกลมเล็กด้านขวาที่ป้ายกำกับ "Output"
- ภายในวงกลม Output มีลูกศรชี้ไปที่ค่า "0" (จากจุดใน Code space) และชี้ไปที่ค่า "1" (จากจุดใน Error space)

**ภาพขวา — "Example: 5-input odd-parity checker"**
- วงจร XOR (odd-parity) แบบต้นไม้:
  - สอง input เข้า XOR gate ตัวแรก
  - สอง input เข้า XOR gate ตัวที่สอง
  - เอาต์พุตของ XOR สองตัวแรกป้อนเข้า XOR ตัวที่สาม
  - มี input เส้นล่างหนึ่งเส้นลากตรงเข้าสู่ระดับถัดไป
  - เอาต์พุตสุดท้ายออกจาก XOR ตัวขวาสุด (มีบับเบิลที่เอาต์พุต) ไปยังสัญญาณ "e"

(หมายเลขหน้าในสไลด์: 45)

---

## Slide 45

**หัวข้อ (Title):** Non-Self Testing Parity Code Checker

**ภาพซ้าย — "Conventional code checker"** (เหมือน Slide 44)
- ป้าย "Input" ชี้ไปยังวงรีที่แบ่งเป็น "Code space" (บน) และ "Error space" (ล่าง)
- จุดหนึ่งในแต่ละ space; ลูกศรป้าย "f" ลากไปยังวงกลม "Output" ที่มีค่า "0" และ "1"

**ภาพขวา — "Example: 5-input odd-parity checker"**
- วงจร XOR ต้นไม้แบบเดียวกับ Slide 44 จบที่สัญญาณ "e"
- มีข้อความสีแดงเพิ่มเติม: "s-a-0 fault on output?" พร้อมเส้นประชี้ลงมาที่เส้นสัญญาณเอาต์พุต "e"

**Bullet points (ด้านล่าง, จุดหน้าข้อ):**
- "Single output line" (สีแดง)
- "Code-Disjoint" (สีดำ)
- "non-Self Testing" (สีแดง)

(หมายเลขหน้าในสไลด์: 46)

---

## Slide 46

**หัวข้อ (Title):** Totally Self Checking Error Signal Combining

**แผนภาพบล็อก (ด้านบน):**
- "Encoded input" → บล็อกสีเหลือง "Function unit 1" → สัญญาณ "Encoded output" → บล็อกสีเหลือง "Function unit 2" → ลูกศรออก
- มีจุดแตะ (tap) ที่ "Encoded output" ระหว่าง unit 1 และ unit 2 ต่อลงไปยังบล็อกสีเขียว "Self-checking checker"
- มีจุดแตะที่เอาต์พุตของ unit 2 ต่อลงไปยังบล็อกสีเขียว "Self-checking checker" อีกตัว
- เอาต์พุตจาก self-checking checker ทั้งสองตัวลงเข้าสู่กรอบเส้นประ "Circuit to combine error signals (two-rail code checker)"

**วงจรในกรอบเส้นประ (two-rail code checker):**
- AND gate 4 ตัววางเรียงในแนวนอน (เรียงแถวเดียว)
- เอาต์พุตของ AND gate จับคู่กัน: สองตัวซ้ายรวมผ่าน OR gate ตัวหนึ่ง, สองตัวขวารวมผ่าน OR gate อีกตัวหนึ่ง
- มีสายไฟแนวนอน/แนวตั้งไขว้เชื่อมจาก self-checking checker และจากกรอบไปยัง AND gates

**ภาพซ้ายล่าง — "Simplified truth table":**
ข้อความ: "if we denote 01 and 10 as G, 00 and 11 as B"

| In | Out |
|----|-----|
| B B | B |
| B G | B |
| G B | B |
| G G | G |

**ภาพขวา — ตาราง In/Out (4 บิต):**

| In | Out |
|------|------|
| 0 0 0 0 | 0 0 |
| 0 0 0 1 | 0 0 |
| 0 0 1 0 | 0 0 |
| 0 0 1 1 | 0 0 |
| 0 1 0 0 | 0 0 |
| 0 1 0 1 | 0 1 |
| 0 1 1 0 | 1 0 |
| 0 1 1 1 | 1 1 |
| 1 0 0 0 | 0 0 |
| 1 0 0 1 | 1 0 |
| 1 0 1 0 | 0 1 |
| 1 0 1 1 | 1 1 |
| 1 1 0 0 | 0 0 |
| 1 1 0 1 | 1 1 |
| 1 1 1 0 | 1 1 |
| 1 1 1 1 | 1 1 |

(แถวแรก ๆ ใช้ตัวอักษรสีแดง ส่วนบางแถวค่าที่สื่อ codeword ใช้สีเขียว)

**ข้อความล่าง:** "Show that this circuit is self-testing"

(หมายเลขหน้าในสไลด์: 47)

---

## Slide 49

**หัวข้อ (Title):** Self Testing Parity Code Checker

**Bullet points:**
- "2 output lines" (สีแดง)
- "(C1,C0) = {(0,1),(1,0)} = codeword"
- "(C1,C0) = {(0,0),(1,1)} = non-codeword"

**ข้อความ:** "Ex. 8 bit data bit + 1 bit odd-parity bit"

**วงจร — "Self Testing Checker":**
- กลุ่มบน: อินพุต x8, x6 เข้า XOR gate ตัวหนึ่ง; อินพุต x4, x2 เข้า XOR อีกตัว; สัญญาณ x0 เข้าสู่ระดับถัดไป; เอาต์พุตรวมกันผ่าน XOR gate ไปยัง "C0"
- กลุ่มล่าง: อินพุต x7, x5 เข้า XOR ตัวหนึ่ง; x3, x1 เข้า XOR อีกตัว; รวมผ่าน XOR ไปยัง "C1"
- (โครงสร้างเป็น XOR tree: C0 มาจากกลุ่ม x8,x6,x4,x2,x0 และ C1 มาจากกลุ่ม x7,x5,x3,x1)

**Bullet ด้านขวา (สีแดง):**
- "2 output lines"
- "Code-Disjoint"
- "Self Testing"
- "(number of 1s is even)"

(หมายเลขหน้าในสไลด์: 50)

---

## Slide 50

**หัวข้อ (Title):** Two Rail Code Checker

**หัวข้อรอง (สีแดง):** "Duplication/ Comparison Check"

**แผนภาพ:**
- สัญญาณอินพุตหนึ่งเส้นแยก (branch) ออกเป็นสองทาง: ขึ้นบนเข้าบล็อก "Functional circuit L" และขึ้นขวาเข้าบล็อก "Duplicated circuit L"
- บล็อก "Functional circuit L" ให้เอาต์พุต a0, a1, ..., a(m-1) (ป้าย "a0", "a1", "am-1")
- บล็อก "Duplicated circuit L" ให้เอาต์พุต b0, b1, ..., b(m-1) (ป้าย "b0", "b1", "bm-1") ผ่านวงกลมเล็กที่มีป้าย "Inverters" (อินเวอร์เตอร์ทุกเส้น)
- เอาต์พุตทั้งสองชุด (มีจุดเชื่อมต่อ) ป้อนเข้าด้านบนของรูปสี่เหลี่ยมคางหมูคว่ำที่มีสัญลักษณ์ "*" ตรงกลาง ป้ายกำกับ "Two-rail code checker (Comparator)"
- ด้านล่างของ trapezoid มีเอาต์พุตสองเส้น: "Z0" และ "Z1"

(หมายเลขหน้าในสไลด์: 51)

---

## Slide 51

**หัวข้อ (Title):** Example of Two Rail Code Checker

**Bullet points:**
- "2 output lines" (สีแดง)
- "(C1,C0) = {(0,1),(1,0)} = codeword"
- "(C1,C0) = {(0,0),(1,1)} = non-codeword"

**ข้อความ (บางส่วนสีฟ้า):** "Ex. 2-Pair Two Rail Code Checker: Input = {x1x0, y1y0}"

**วงจร — "Self Testing Checker":**
- อินพุตสี่เส้นในแนวตั้ง (จากบนลงล่าง): x1, x0, y1, y0
- มีจุดเชื่อมต่อ (dot) บนเส้นสัญญาณและสายไฟแนวตั้งที่ไขว้กันไปยัง AND gate
- AND gate สี่ตัววางเรียงในแนวตั้ง: สองตัวบนรวมผ่าน OR gate ตัวบน → "C0"; สองตัวล่างรวมผ่าน OR gate ตัวล่าง → "C1"

**Bullet ด้านขวา (สีแดง):**
- "2 output lines"
- "Code-Disjoint"
- "Self Testing"
- "{0101,0110,1001,1010}" (วางต่อท้ายคำ Self Testing)

(หมายเลขหน้าในสไลด์: 52)

---

## Slide 53

**หัวข้อ (Title):** Two Rail Code Sequence

**ตารางที่ 1** (หัวมุม "Timing/ Sequence", คอลัมน์ 1–4):

| Timing/Sequence | 1 | 2 | 3 | 4 |
|-----------------|---|---|---|---|
| R | 01 | 01 | 10 | 10 |
| S | 01 | 10 | 01 | 10 |
| T | 01 | 10 | 10 | 01 |

**แผนภาพบล็อก (ขวาบน):**
- อินพุต x1, x0, y1, y0 ป้อนเข้าบล็อก "2PTRC"
- เอาต์พุตบล็อก "2PTRC" ออกเป็น "C1" และ "C0"
- ข้อความสีแดง: "Self Testing for all Stuck-at Faults"

**ตารางที่ 2** (หัวมุม "IO/ Timing", คอลัมน์ x1, x0, y1, y0, C1, C0):

| IO/Timing | x1 | x0 | y1 | y0 | C1 | C0 |
|-----------|----|----|----|----|----|----|
| 1 | 0 | 1 | 0 | 1 | 0 | 1 |
| 2 | 0 | 1 | 1 | 0 | 1 | 0 |
| 3 | 1 | 0 | 0 | 1 | 1 | 0 |
| 4 | 1 | 0 | 1 | 0 | 0 | 1 |

- ป้ายตัวอักษรสีแดง "R", "S", "T" วางอยู่ใต้คอลัมน์ด้านล่าง (R ใต้กลุ่ม x1 x0, S ใต้กลุ่ม y1 y0, T ใต้กลุ่ม C1 C0)

(หมายเลขหน้าในสไลด์: 54)

---

## Slide 54

**หัวข้อ (Title):** Self Testing for 6-Pair Two Rail Code Checker

**ข้อความ (กลาง-ขวาบน):** "Using RST sequence combination regardless n data bit size"
(คำ "RST sequence" เป็นสีแดง)

**แผนภาพ:**
- ด้านซ้ายมีบล็อกสี่เหลี่ยม 3 บล็อกเรียงตามแนวตั้ง แต่ละบล็อกมีอินพุตจากป้าย R (แดง) และ S (แดง) ป้อนเข้าด้านซ้าย (ข้อความ "T" สีแดงอยู่ด้านขวาของบล็อกล่าง)
- อินพุตจากด้านซ้ายไหลไปยังคอลัมน์ถัดไป และมีเส้นสัญญาณแนวนอนหลายเส้น (ป้าย R, S) เชื่อมระหว่างบล็อก
- คอลัมน์กลางมีบล็อก 2 บล็อก
- ด้านขวามีค่าคงที่ป้อนเข้าบล็อกสุดท้าย: "0011", "1100" (มีป้าย "R" สีแดงกำกับด้านบน) และ "0101", "1010" (มีป้าย "S" สีแดงกำกับด้านล่าง)
- บล็อกขวาสุดให้เอาต์พุตสองเส้นคือ "0110" และ "1001" โดยมีป้าย "T" สีแดงกำกับ

(หมายเลขหน้าในสไลด์: 55)

---

## Slide 55

**หัวข้อ (Title):** 1-of-n Code Checker

**Bullet point:**
- "Decode n to k (k = [log₂ n]) and connect to Tree-Structure k-Pair Two Rail Code Checkers"
  (ส่วน "k = [log₂ n]" เป็นสีแดง)

**แผนภาพ:**
- อินพุตทางซ้ายมีป้าย "1", "2", (เส้นประแนวตั้ง), "n" ป้อนเข้าบล็อก "Decoder"
- เอาต์พุตของ Decoder: "a1", "b1", "a2", "b2", (เส้นประแนวตั้ง), "ak", "bk" ป้อนเข้าบล็อก "Two Rail Code Checker"
- เอาต์พุตของบล็อก Two Rail Code Checker: "C1" และ "C0"

**ตัวอย่าง (ด้านล่าง):** "Ex. n=8, k=3; Decoder function:"
- a1 = (1 ∨ 2 ∨ 3 ∨ 4), b1=(5 ∨ 6 ∨ 7 ∨ 8)
- a2 = (1 ∨ 2 ∨ 5 ∨ 6), b2=(3 ∨ 4 ∨ 7 ∨ 8)
- a3 = (1 ∨ 3 ∨ 5 ∨ 7), b3=(2 ∨ 4 ∨ 6 ∨ 8)

(หมายเลขหน้าในสไลด์: 56)

---

## Slide 56

**หัวข้อ (Title):** Self Testing 1-of-n Code Checker (n≠2ᵏ)

**Bullet points:**
- "Connect pair (1,k) to Two Rail Code Checker (C1) and other pairs to k-2 Pair Two Rail Code Checker (C2)"
  (ส่วน "pair (1,k)" เป็นสีแดง)
- "All Checkers have {00,01,10,11} inputs ⟹ Self Testing" (ส่วน "Self Testing" เป็นสีแดง)

**แผนภาพ:**
- อินพุต "1", "2", (เส้นประ), "n" ป้อนเข้าบล็อก "Decoder"
- เอาต์พุต Decoder: "a1", "b1", "a2", "b2", (เส้นประแนวตั้ง), "ak-1", "bk-1", "ak", "bk"
- คู่ (1,k) คือ a1,b1 และ ak,bk ป้อนเข้าบล็อก "C1"; คู่อื่น ๆ ป้อนเข้าบล็อก "C2"
- เอาต์พุตของ C1 และ C2 ป้อนเข้าบล็อก "C3"
- เอาต์พุตของ C3 คือ "C1" และ "C0"

**ตาราง (ขวา):** คอลัมน์หัว: ai/L_ip | a1 | a2 | ... | ak-1 | ak

| ai/L_ip | a1 | a2 | ... | ak-1 | ak |
|---------|----|----|-----|------|----|
| 1 | 0 | 0 | ... | 0 | 1 |
| 2 | 0 | 0 | ... | 1 | 0 |
| 3 | 0 | 0 | ... | 1 | 1 |
| 2^(k-1) | 1 | 0 | ... | 0 | 0 |
| 2^(k-1)+1 | 1 | 0 | ... | 0 | 1 |
| ... | ... | ... | ... | ... | ... |

- คอลัมน์ "a1" และคอลัมน์ "ak" ถูกกรอบสีแดงเน้นไว้

(หมายเลขหน้าในสไลด์: 57)

---

## Slide 57

**หัวข้อ (Title):** m-of-2m Code Checker

**ข้อความ:**
- "Divide the 2m bits into two disjoint subsets A and B of m bits each"
- "Let v and w be the weight of (number of 1s in) A and B, respectively"
- "Implement the two code checker outputs e₀ and e₁ as follows:"

**สูตร:**
- C₀ = ∨ (i=0, i even, ถึง m) (v ≥ i)(w ≥ m − i)
- C₁ = ∨ (j=1, j odd, ถึง m) (v ≥ j)(w ≥ m − j)

**แผนภาพ (ขวา):**
- กล่องแบ่งเป็นสองช่อง: ช่องซ้าย "m bits" (ด้านบนมีปีกกากำกับ "v 1s", ด้านล่างป้าย "Subset A"), ช่องขวา "m bits" (ด้านบนปีกกากำกับ "w 1s", ด้านล่างป้าย "Subset B")

**ตัวอย่าง (ด้านล่าง):**
"Ex. 3-out-of-6 code checker, m = 3, A = {a, b, c}, B = {f, g, h}"
- C₀ = (v ≥ 0)(w ≥ 3) ∨ (v ≥ 2)(w ≥ 1) = fgh ∨ (ab ∨ bc ∨ ca)(f ∨ g ∨ h)
- C₁ = (v ≥ 1)(w ≥ 2) ∨ (v ≥ 3)(w ≥ 0) = (a ∨ b ∨ c)(fg ∨ gh ∨ hf) ∨ abc
- ข้อความสีแดง "Always satisfied" ใต้พจน์ (w ≥ 0) (และมีขีดเขียนทับ (v ≥ 0))

(หมายเลขหน้าในสไลด์: 58)

---

## Slide 58

**หัวข้อ (Title):** Another TSC m-out-of-2m Code Checker

**ข้อความ:**
- "Cellular realization, due to J. E. Smith:"
- "This design is testable with only 2m inputs, all having m consecutive 1s (in cyclic order)"

**แผนภาพ:**
- อาร์เรย์เซลล์ (cell) เป็นรูปสี่เหลี่ยมจัตุรัสจำนวนมาก จัดเรียงเป็นโครงข่ายสองมิติ มีเส้นสัญญาณแนวนอนและแนวตั้งไขว้กันไปมาระหว่างเซลล์ (มีเครื่องหมายจุด "." แทนเซลล์ที่ละไว้เป็นแนวดิ่ง)
- ป้ายเส้นประด้านบน: "m − 1 stages" (มีลูกศรหัว-ท้ายชี้ช่วง)
- ด้านขวามีแถวคอลัมน์เซลล์สุดท้ายที่ต่อออกไปยัง AND gate ตัวหนึ่ง (ด้านบน) และ OR gate ตัวหนึ่ง (ด้านล่าง) โดยมีสายไฟจำนวนมากป้อนเข้า
- มีวงกลมสีส้ม (inset/magnify) แสดงรายละเอียดภายในเซลล์หนึ่ง: ประกอบด้วยสี่เหลี่ยมเล็กสองช่อง มี AND gate หนึ่งตัว (ล่าง) และ OR gate หนึ่งตัว (บน) พร้อมการต่อกลับ (feedback)

(หมายเลขหน้าในสไลด์: 59)

---

## Slide 59

**หัวข้อ (Title):** Using 2-out-of-4 Checkers as Building Blocks

**ข้อความ:**
- "Building m-out-of-2m TSC checkers, 3 ≤ m ≤ 6, from 2-out-of-4 checkers (construction due to Lala, Busaba, and Zhao):"
- "Ex. 3-out-of-6 and 4-out-of-8 TSC checkers are depicted below (only the structure is shown; some design details are missing)"

**แผนภาพซ้าย — "3-out-of-6":**
- กลุ่มอินพุต "1 2 3 4 5 6" ป้อนเข้าบล็อก "2-out-of-4"
- อีกกลุ่มอินพุต "1 2 3 4 5 6" ป้อนเข้าบล็อก "2-out-of-4"
- เอาต์พุตของสองบล็อกบนป้อนเข้าบล็อก "2-out-of-4" สองบล็อกในแถวที่สอง
- เอาต์พุตป้อนเข้าบล็อกสีเหลือง "2-rail checker" (ด้านล่าง) ที่มีเอาต์พุตสองเส้น
- มีเส้นประสีแดงสองเส้นชี้จากกลุ่มกลางไปยังข้อความสีแดง: "Slightly different from an ordinary 2-out-of-4 checker"
- ป้าย "3-out-of-6" ใต้กลุ่มบล็อกซ้าย

**แผนภาพขวา — "4-out-of-8":**
- อินพุต "1 2 3 4 5 6 7 8": บล็อก "2-out-of-4" ตัวแรกมีอินพุต 1 2 3 4, ตัวที่สองมีอินพุต 5 6 7 8
- แถวถัดไป: บล็อก "2-out-of-4" มีอินพุต 3 4 7 8 และอีกบล็อกมีอินพุต 1 2 5 6
- เอาต์พุตป้อนเข้าบล็อก "2-rail checker" (สีเหลือง, ด้านล่าง) ที่มีเอาต์พุตสองเส้น
- ป้าย "4-out-of-8" ใต้กลุ่มบล็อกขวา

(หมายเลขหน้าในสไลด์: 60)

---

## Slide 60

**หัวข้อ (Title):** TSC Checker for k-out-of-n Code

**ข้อความ (ซ้าย):**
- "One design strategy is to proceed in 3 stages:"
- "Convert the k-out-of-n code to a 1-out-of-(n choose k) code"
- "Convert the latter code to an m-out-of-2m code"
- "Check the m-out-of-2m code using a TSC checker"
- "This approach is impractical for many codes"
- "A procedure due to Marouf and Friedman:"
- "Implement 6 functions of the general form"
- "(these have different subsets of bits as inputs and constitute a 1-out-of-6 code)"
- "Use a TSC 1-out-of-6 to 2-out-of-4 converter"
- "Use a TSC 2-out-of-4 code checker"
- "The process above works for 2k + 2 ≤ n ≤ 4k"
- "It can be somewhat simplified for n = 2k + 1"

**แผนภาพขวาบน (แนวตั้ง):**
- ป้าย "2-out-of-5" → บล็อก "5 bits"
- "10 AND gates" → ป้าย "1-out-of-10" → บล็อก "10 bits"
- "6 OR gates" → ป้าย "3-out-of-6" → บล็อก "6 bits"
- "TSC checker" → ลูกศรลง

**กล่องสีเหลือง (กลางขวา):** สูตร
- e₀ = ∨ (j=1, j even, ถึง m) (v ≥ j)(w ≥ m − j)

**แผนภาพขวาล่าง (แนวตั้ง):**
- อินพุต "e₀ e₁ e₂ e₃ e₄ e₅" ป้าย "1-out-of-6" → บล็อก "6 bits"
- "OR gates" → ป้าย "2-out-of-4" → บล็อก "4 bits"
- "TSC checker" → ลูกศรลง

(หมายเลขหน้าในสไลด์: 61)

---

## Slide 61

**หัวข้อ (Title):** TSC Checker for Separable Codes

**ข้อความ:** "Here is a general strategy for designing totally-self-checking checkers for separable codes"

**แผนภาพ:**
- ด้านซ้าย: "Input word" ประกอบด้วยแท่งสีเหลือง "k data bits" และแท่งสีส้ม "n − k check bits"
- ภายในกรอบเส้นประสีชมพูมีป้าย "TSC code checker"
- "k data bits" ป้อนเข้าบล็อก "Complement of check bits generator" (คำ "Complement" สีแดง)
- เอาต์พุตของ generator (n − k) และ "n − k check bits" ป้อนเข้าบล็อก "Two-rail checker"
- เอาต์พุตบล็อก: "C₀" และ "C₁" (ป้ายด้านขวา "Checker outputs")

**Bullet points:**
- "For many codes, direct synthesis will produce a faster and/or more compact totally-self-checking checker"
- "Require full combination of Two-rail Checker Inputs ⇒ ST" (สีแดง)
- "No need to consider about ST in Complement of Check Bits Generator" (สีแดง)

(หมายเลขหน้าในสไลด์: 62)

---

## Slide 62

**หัวข้อ (Title):** Berger Code Checker

**แผนภาพ (บน):**
- "Input word": แท่งสีเหลือง "k data bits" และแท่งสีส้ม "n − k check bits"
- "k data bits" ป้อนเข้าบล็อก "Number of 1s in Binary" (สีแดง)
- เอาต์พุตของบล็อก (n − k) และ "n − k check bits" ป้อนเข้าบล็อก "Two-rail checker"
- เอาต์พุต: "C₀", "C₁" (ป้าย "Checker outputs")
- กรอบเส้นประสีชมพูมีป้าย "TSC code checker"

**ตัวอย่าง (ล่าง):** "Ex. Complement of Check bit Generator of (15,4) Berger Code"
- บล็อก "1bit FA" สี่บล็อกเรียงในแนวนอน (มีอินพุตหลายเส้นด้านบน ป้อนลง)
- เอาต์พุตของ 1bit FA สองกลุ่มรวมเข้าบล็อก "2bit FA" สองบล็อก (แถวที่สอง)
- เอาต์พุตของ 2bit FA ทั้งสองรวมเข้าบล็อก "3bit FA" หนึ่งบล็อก (ด้านล่าง)
- บล็อก "3bit FA" มีเอาต์พุตหลายเส้นออกด้านล่าง

(หมายเลขหน้าในสไลด์: 63)

---

## Slide 63

**หัวข้อ (Title):** Generalized Prediction Checker (GPC)

**Bullet point:**
- "Self-testing checker of the combinational circuits having non-encoded inputs and outputs" (คำ "non-encoded inputs and outputs" สีแดง)

**แผนภาพ (ในกรอบ "CK"):**
- อินพุต "X" (มีป้ายจำนวนบิต "n") ป้อนเข้าบล็อก "L" ซึ่งให้เอาต์พุต "Y" (มีป้ายจำนวนบิต "k")
- ภายในกรอบ CK: บล็อก "I" มีฟังก์ชัน "K̄ · U" และบล็อก "J" มีฟังก์ชัน "Y ⊕ (A ⊕ K) · U"
- สัญญาณ X (n) แยกเข้า I และ J; สัญญาณ Y (k) แยกเข้า J
- เอาต์พุตของ I และ J (อย่างละ k เส้น) ป้อนเข้าบล็อกรูป trapezoid ที่มีสัญลักษณ์ "*" (ป้าย "Z")
- เอาต์พุต: "Z₀" และ "Z₁" (ป้าย "Z")
- ป้ายมุมขวาล่างของกรอบ: "CK"

(หมายเลขหน้าในสไลด์: 64)

---

## Slide 65

**หัวข้อ (Title):** Dual Rail Logic

**Bullet points:**
- "1-of-2 Code"
- "{0,1} ⇒ {01,10}"
- "Easy Implementation (Encoder/Decoder)"
- "Preserve code after operation" (สีแดง)
- "Non-Inverter Circuit" (สีน้ำเงิน)

**วงจร (ซ้าย = gate เดี่ยว, ขวา = dual-rail):**
- Buffer: "x —— z" (เดี่ยว) และ dual: "x —— z", "x′ —— z′"
- Inverter: "x —▷o— z" (เดี่ยว) และ dual แบบไขว้: "x —— z", "x′ —— z′" (เส้น 두 เส้นสลับ/ไขว้กัน)
- AND gate: "x, y → z" (เดี่ยว) และ dual: บน "x, y → z", ล่าง "x′, y′ → z′" (ใช้ AND/OR คู่ complement)
- OR gate: "x, y → z" (เดี่ยว) และ dual: บน "x, y → z" (OR), ล่าง "x′, y′ → z′" (AND) — โดย AND/OR สลับบทบาทกัน

(หมายเลขหน้าในสไลด์: 66)

---

## Slide 66

**หัวข้อ (Title):** Check Yourself: TSC Functional Unit

**Bullet points:**
- "Dual-Logic implementation for"
- สูตร: F = āb + b c̄ + ac
- "Assume one stuck-at-fault,"
  - "Find the property of each input"
  - "Conclude the property of circuit"

**วงจรบน (ให้ F):**
- อินพุต (มีปีกกา/เส้น): ā, b, c̄, a, c
- AND gate 3 ตัว (สร้าง product terms ของ F) รวมกันผ่าน OR gate → เอาต์พุต "F"

**วงจรล่าง (ให้ F̄):**
- อินพุต: a, b̄, c, ā, c̄
- OR gate 3 ตัว รวมกันผ่าน AND gate → เอาต์พุต "F̄"

(หมายเลขหน้าในสไลด์: 67)

---

## Slide 67

**หัวข้อ (Title):** Check Yourself: TSC Functional Unit

**สูตร:** F = āb + b c̄ + ac ; F̄ = (a + b̄)(b̄ + c)(ā + c̄)

**วงจร (ซ้าย):** เหมือน Slide 66
- วงจรบน (AND 3 ตัว → OR) ให้เอาต์พุต "F"
- วงจรล่าง (OR 3 ตัว → AND) ให้เอาต์พุต "F̄"
- มีสัญลักษณ์ "f" สีแดงและเครื่องหมายกากบาท "✗" ที่อินพุต a ของวงจรล่าง (แสดง fault)

**ตาราง (ขวา):** คอลัมน์: a | ā | b | b̄ | c | c̄ | F | F̄ | f_{s−a−0}

| a | ā | b | b̄ | c | c̄ | F | F̄ | f_{s−a−0} |
|---|---|---|---|---|---|---|---|-----------|
| 0 | 1 | 0 | 1 | 0 | 1 | 0 | 1 | same OP |
| 0 | 1 | 0 | 1 | 1 | 0 | 0 | 1 | same OP |
| 0 | 1 | 1 | 0 | 0 | 1 | 1 | 0 | same OP |
| 0 | 1 | 1 | 0 | 1 | 0 | 1 | 0 | same OP |
| 1 | 0 | 0 | 1 | 0 | 1 | 0 | 1 | same OP |
| 1 | 0 | 0 | 1 | 1 | 0 | 0 | 1 | same OP |
| 1 | 0 | 1 | 0 | 0 | 1 | 1 | 0 | non-codeword |
| 1 | 0 | 1 | 0 | 1 | 0 | 1 | 0 | non-codeword |

**ข้อความล่าง (สีแดง):** "The property of circuit = FS + ST = TSC"

(หมายเลขหน้าในสไลด์: 68)

---

## Slide 68

**หัวข้อ (Title):** Contraction Circuits

**นิยาม/ข้อความ:**
- "Definition: Contraction Circuit G′"
- "Circuit G′ that remove signal lines and gate outputs which are fixed by a given fault f in the original circuit G"

**แผนภาพ:**
- ด้านซ้าย: วงจรเดิม (original circuit G) ประกอบด้วย NAND gate หลายตัว (มีบับเบิลที่เอาต์พุต) เชื่อมกันเป็นโครงข่าย มีจุดเชื่อมต่อ (dot)
- มีเครื่องหมายกากบาทสีแดง "✗" พร้อมป้าย "S-a-0" ที่อินพุตของ NAND gate ตัวหนึ่ง (แสดงตำแหน่ง fault)
- ลูกศรทึบสีน้ำเงินชี้จากวงจรเดิมไปยังวงจรทางขวา
- ด้านขวา: วงจร contraction circuit G′ (มี NAND gate จำนวนน้อยลง; เส้นสัญญาณและ gate ที่ถูก fix ด้วย fault ถูกกำจัดออกไป)

(หมายเลขหน้าในสไลด์: 69)

---

## Slide 71

**หัวข้อ (Title):** TSC Design with Parity Prediction

**ข้อความบน:** "Parity prediction as an alternative to duplication"

**แผนภาพ:**
- ด้านซ้าย: "Parity-encoded inputs" ป้อนเข้าทั้งสัญญาณบน (มีป้าย "k" กำกับ slash) และล่าง (มีป้าย "k")
- บล็อก "Parity predictor" รับสัญญาณจากอินพุตทั้งสอง (มีลูกศรสามเหลี่ยมทึบ)
- อินพุตสองเส้น (บน/ล่าง) ป้อนเข้าบล็อกรูปหกเหลี่ยม/สี่เหลี่ยมคางหมูขนาดใหญ่ "ALU" (ป้าย "Ordinary ALU" ที่มุมล่างขวา)
- เอาต์พุตของ ALU แยกไปที่บล็อก "Parity generator" (ด้านบน) และต่อไปยังเอาต์พุต
- สัญญาณจาก Parity generator และเอาต์พุต ALU (มีจุดเชื่อมต่อ) ไปยัง XOR gate (ทางขวาล่าง) ซึ่งให้เอาต์พุต "Error signal"
- ด้านขวา: "Parity-encoded output" (มีป้าย "k")
- เส้นประหลายเส้นเชื่อมระหว่าง Parity predictor, อินพุต, เอาต์พุต และ XOR

**ข้อความล่าง:**
- "If the parity predictor produces the complement of the output parity, and the XOR gate is removed, we have a self-checking design"
- "To ensure the TSC property, we must also verify that the parity predictor is testable only with input codewords"

(หมายเลขหน้าในสไลด์: 72)

---

## Slide 72

**หัวข้อ (Title):** TSC Design with Residue Encoding

**ข้อความบน:** "Residue checking is applicable directly to addition, subtraction, and multiplication, and with some extra effort to other arithmetic operations"

**แผนภาพ (ซ้าย):**
- อินพุต "x, x mod A" และ "y, y mod A" (แต่ละคู่มีสองเส้น) ป้อนเข้าบล็อกรูปสี่เหลี่ยมคางหมู "Add" และบล็อกรูป trapezoid "Add mod A"
- เอาต์พุตของ "Add" แยกไปที่ (1) เอาต์พุต "s, s mod A" และ (2) บล็อก "Find mod A"
- เอาต์พุตของ "Find mod A" (มีจุดเชื่อมต่อ) และเอาต์พุตของ "Add mod A" ป้อนเข้าวงกลม "Compare"
- เอาต์พุตของ "Compare" ออกเป็นเส้นประลงล่าง มีป้าย "Not equal" → "Error"
- เอาต์พุตล่าง: "s, s mod A"

**ข้อความขวา:** "To make this scheme TSC:"
- "Modify the "Find mod A" box to produce the complement of the residue"
- "Use two-rail checker instead of comparator"
- "Verify the self-testing property if the residue channel is not completely independent of the main computation (not needed for add/subtract and multiply)"

(หมายเลขหน้าในสไลด์: 73)

---

## Slide 75

**หัวข้อ (Title):** Partially Self-Checking Units

**ข้อความ:**
- "Some ALU functions, such as logical operations, cannot be checked using low-redundancy codes"
- "Such an ALU can be made partially self-checking by circumventing the error-checking process in cases where codes are not applicable"

**แผนภาพ:**
- บล็อก "Self-checking ALU with residue code" ให้สัญญาณ "Residue-check error signal"
- มีอินพุตควบคุมสองเส้น (บนลง): สัญญาณ "0 1" (ป้าย "Do not check" ด้านซ้าย) และ "1 0" (ป้าย "Check" ด้านขวา) ป้อนเข้าบล็อกสีเหลือง
- บล็อกสีเหลืองรับทั้ง Residue-check error signal และสัญญาณควบคุม แล้วให้เอาต์พุต "ALU error indicator"

**ข้อความ:** "The check/do-not-check indicator is produced by the control unit"

**ข้อความขวา:**
- "01, 10 = G (top)"
- "01=D, 10=C (bottom)"
- "00, 11 = B"

**ตาราง (ขวา):** คอลัมน์: In | Out

| In | Out |
|----|-----|
| X B | B |
| B C | B |
| B D | G |
| G C | G |
| G D | G |

- สองแถวล่างถูกวงปีกกา (brace) มีป้าย "Normal operation" พร้อมค่าด้านขวา "01" (แถว G C) และ "10" (แถว G D)
- แถว X B, B C เป็นสีแดง; แถว B D, G C, G D เป็นสีเขียว

(หมายเลขหน้าในสไลด์: 76)

---

## Slide 76

**หัวข้อ (Title):** Self-Checking State Machines

**ข้อความ:**
- "Design method for Moore-type machines, due to Diaz and Azema:"
- "Inputs and outputs are encoded using two-rail code"
- "States are encoded as n/2-out-of-n codewords"
- "Fact: If the states are encoded using a k-out-of-n code, one can express the next-state functions (one for each bit of the next state) via monotonic expressions; i.e., without complemented variables"
- "Monotonic functions can be realized with only AND and OR gates, hence the unidirectional error detection capability"

**ตารางที่ 1 (กล่องสีเหลือง):** หัวคอลัมน์: State | Input (x = 0, x = 1) | Output z

| State | x = 0 | x = 1 | Output z |
|-------|-------|-------|----------|
| A | C | A | 1 |
| B | D | C | 1 |
| C | B | D | 0 |
| D | C | A | 0 |

**ตารางที่ 2 (กล่องสีส้ม):** หัวคอลัมน์: State | Input (x = 01, x = 10) | Output z

| State | x = 01 | x = 10 | Output z |
|-------|--------|--------|----------|
| 0011 | 1010 | 0011 | 10 |
| 0101 | 1001 | 1010 | 10 |
| 1010 | 0101 | 1001 | 01 |
| 1001 | 1010 | 0011 | 01 |

(หมายเลขหน้าในสไลด์: 77)

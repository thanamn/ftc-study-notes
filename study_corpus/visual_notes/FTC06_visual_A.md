# FTC06 Self-Checking — Visual Notes (ชุด A)

คำอธิบายเนื้อหาจากภาพสไลด์ (บรรยายเป็นภาษาไทย โดยคงข้อความ/ป้าย/ตาราง/สูตร/ตัวแปร ภาษาอังกฤษตามต้นฉบับทุกตัวอักษร)

---

## Slide 4

**หัวเรื่อง:** Error Control

**หัวข้อย่อย:** Fault Masking Scheme

**แผนภาพบล็อก (Block diagram):** เป็นแผนผัง Fault Masking Scheme ประกอบด้วยกล่องสี่เหลี่ยม 3 กล่อง และลูกศรเชื่อมต่อ

- กล่องซ้าย: `Functional Unit`
- กล่องขวาบน: `Corrector`
- กล่องล่าง: `Checker`

**การเชื่อมต่อและป้าย (labels):**
- ลูกศรจาก `Functional Unit` ไปยัง `Corrector` มีป้ายกำกับด้านบนว่า `Error Control Codes`
- ลูกศรจาก `Functional Unit` ลงไปยัง `Checker` มีป้ายกำกับว่า `Error Control Codes`
- ลูกศรจาก `Funcional Unit` ลงไปและไปยัง `Checker` (ลูกศรกลางที่แยก) มีป้าย `Error Control Codes`
- ลูกศรจาก `Checker` ขึ้นไปยัง `Corrector` มีป้ายกำกับว่า `Overlapped Parity Syndrome`
- ลูกศรจาก `Corrector` ออกไปทางขวามีป้ายว่า `Corrected Output`
- ลูกศรจาก `Checker` ออกไปทางขวา (แนวนอน) มีป้ายว่า `Status`

(มุมขวาล่างมีเลขหน้า 4)

---

## Slide 5

**หัวเรื่อง:** Self Checking Model

**หัวข้อย่อย:** Concurrent Fault/Error Detection Scheme

**แผนภาพบล็อก (Self Checking Model):** มีกรอบสี่เหลี่ยมใหญ่ล้อมรอบทั้งระบบ (ป้าย `G` ที่มุมขวาบนของกรอบ) ภายในมี:

- กล่อง `Functional Unit L`
- กล่อง `Checker CK` (อยู่ใต้ Functional Unit)

**การเชื่อมต่อและป้าย:**
- ด้านซ้ายมีลูกศรเข้าสู่ระบบ ป้าย `Input` และตัวแปร `X`
- ลูกศรจาก `Input X` แยกเป็นสองทาง: ทางหนึ่งเข้า `Functional Unit L` และอีกทางเข้า `Checker CK`
- ลูกศรจาก `Functional Unit L` ลงไปยัง `Checker CK` มีป้ายตัวแปร `W`
- ด้านขวา ลูกศรออกจากระบบ ป้าย `Output` และตัวแปร `Y` โดยมีจุดแยก (tap) ก่อนออก และมีลูกศรย้อนกลับเข้า `Checker CK` ด้วย
- ลูกศรออกจาก `Checker CK` ลงด้านล่างนอกกรอบ มีป้าย `Error Indicator` และตัวแปร `Z`

(มุมขวาล่างมีเลขหน้า 5)

---

## Slide 10

**หัวเรื่อง:** Code Space and Error Space

**แผนภาพบน:** แผนผังการไหลของสัญญาณ
- `Encoded input` → ลูกศรเข้าไปยังกล่องสีเหลือง `Functional unit`
- กล่องสีเหลือง `Functional unit` → ลูกศรออกไปเป็น `Encoded output`
- ที่จุดแยกก่อน `Encoded output` มีเส้นต่อไปยังกล่องสีเขียว `Self-checking code checker` ซึ่งมีลูกศรออกด้านล่างเป็น `Status` (เส้นคู่ออก 2 เส้น)
- มีข้อความตัวเอียงบรรยายใต้กล่องว่า `Implementation of the desired functionality with coded values`

**แผนภาพล่าง:** เวนน์/วงรีสองวงซ้อน วงรีแต่ละวงมีวงใน (Codspace/Error space) และวงนอก

- วงรีซ้าย มีป้าย `Input`, ด้านในแบ่งเป็นพื้นที่ `Codespace` และ `Error space` มีจุดสีแดงใน Codespace
- วงรีขวา มีป้าย `Output`, ด้านในแบ่งเป็นพื้นที่ `Codespace` และ `Error space`
- ลูกศรเชื่อมจากจุดในวงรีซ้ายไปยังวงรีขวา:
  - `f1` = ลูกศรสีดำทึบ (โค้ง)
  - `f2` = ลูกศรสีน้ำเงิน (จาก Codespace ไปยัง Codespace)
  - `f3` = ลูกศรเส้นประสีแดง (ไปยัง Error space)
  - `f4` = ลูกศรสีแดงชี้มาที่เครื่องหมาย `?`

(มุมขวาล่างมีเลขหน้า 10)

---

## Slide 11

**หัวเรื่อง:** Cascade of Self Checking Modules

**แผนภาพบน:** การต่อโมดูลแบบเรียงซ้อน (cascade)
- `Encoded input` → กล่องสีเหลือง `Funcional unit 1`
- จาก `Funcional unit 1` → ลูกศรมีป้าย `Encoded output` → กล่องสีเหลือง `Funcional unit 2`
- ที่จุดแยกก่อน `Funcional unit 2` มีเส้นลงไปยังกล่องสีเขียว `Self-checking checker` (มีเส้นออกด้านล่าง 2 เส้น)
- จาก `Funcional unit 2` → ลูกศรออกไปทางขวา และจุดแยกมีเส้นลงไปยังกล่องสีเขียว `Self-checking checker` อีกกล่อง (มีเส้นออกด้านล่าง 2 เส้น)

**แผนภาพล่าง:** วงรีสองวง (Input / Output) มีพื้นที่ `Codespace` และ `Error space`
- ลูกศร `f` = เส้นสีดำจาก Codespace ไป Codespace (สอดคล้อง)
- ลูกศร `fϕ` = เส้นประสีแดงจาก Codespace ไป Error space
- ป้าย `Input` ด้านซ้าย และ `Output` ด้านขวา

(มุมขวาล่างมีเลขหน้า 11)

---

## Slide 13

**หัวเรื่อง:** Characteristics of SC circuits

**หัวข้อย่อย:** `• Fault Secure (FS)` (สีแดง)
- `– The property to ensure that for any possible fault, the circuit output is either a correct codeword or non-codeword` (คำว่า `correct codeword` และ `non-codeword` เป็นสีแดง)

**แผนภาพ:** วงรีซ้อนสองวง (concentric circles)
- วงซ้าย: วงในมีป้าย `codeword` ชี้ไปที่พื้นที่วงใน และตัวแปร `i_cw` (จุดอินพุต); พื้นที่ด้านนอกมีป้าย `non-codeword` ชี้ (สีน้ำเงิน)
- วงขวา: พื้นที่วงในมีป้าย `correct` (สีน้ำเงิน) และตัวแปร `y_cc`; พื้นที่วงนอกมีป้าย `incorrect` (สีแดง) และตัวแปร `y_ic`
- ลูกศร:
  - ลูกศรทึบสีน้ำเงิน `f_fs(i_cw)` ชี้ไปที่ `y_nc` (non-codeword)
  - ลูกศรทึบสีน้ำเงินอีกเส้นชี้ไปที่ `y_cc` (correct)
  - ลูกศรเส้นประสีแดงมีป้าย `non-permissible` ชี้ไปที่ `y_ic` (incorrect)

(มุมขวาล่างมีเลขหน้า 13)

---

## Slide 14

**หัวเรื่อง:** Characteristics of SC circuits

**หัวข้อย่อย:** `• Self Testing (ST)` (สีแดง)
- `– The property to ensure that for every possible fault, there is at least one input codeword for which the resulting output is a non-codeword` (คำว่า `at least one input codeword` และ `non-codeword` เป็นสีแดง)

**แผนภาพ:** วงรีซ้อนสองวง
- วงซ้าย: พื้นที่วงในมีป้าย `codeword` (สีน้ำเงิน) มีตัวแปร `i_cwt` และ `i_cwi` (จุดอินพุต 2 จุด); พื้นที่วงนอกมีป้าย `non-codeword`
- วงขวา: พื้นที่วงในมีป้าย `correct` และตัวแปร `y_i`; พื้นที่วงนอกมีป้าย `incorrect` (สีแดง) และตัวแปร `y_nc`
- ลูกศร:
  - `f_st(i_cwt)` ชี้ไปที่ `y_nc` (non-codeword)
  - `f_st(i_cwi)` ชี้ไปที่ `y_i` (correct)

(มุมขวาล่างมีเลขหน้า 14)

---

## Slide 15

**หัวเรื่อง:** Self Testing & Fault Secure

**หัวข้อย่อย (ด้านซ้าย):**
- `• Self Testing:` ตามด้วยไอคอนสีเหลือง/แดง
- `• Fault Secure:` ตามด้วยไอคอนสีฟ้า/แดง
- `• Undetectable Fault:` ตามด้วยกล่องสีเทามีเครื่องหมาย `?`

**แผนภาพบน — "All faults":** กรอบสี่เหลี่ยมมีป้าย `All faults` ด้านบน ภายในมีวงกลมป้าย `F` (แทนเซต fault) และจุดต่าง ๆ นอกวงกลม: `f_3`, และภายในวงกลม: `f_1`, `f_2`

**แผนภาพล่าง:** สองกรอบ
- กรอบซ้าย: `Input space Ω_x` ภายในมีวงรี `N` ที่มีจุด `X_1` และ `X_2`
- กรอบขวา: `Output space Ω_y` ภายในมีวงรี `S` ที่มีจุดปลายทาง
- ลูกศรจาก `X_1`:
  - `Y(X1, f2)`
  - `Y(X1, λ)` พร้อมเครื่องหมายถูกสีแดง √
  - `Y(X1, f1)`
- ลูกศรจาก `X_2`:
  - `Y(X2, f1)`
  - `Y(X2, f3)`
  - `Y(X2, λ)` พร้อมเครื่องหมายถูกสีแดง √
  - `Y(X2, f2)`

(มุมขวาล่างมีเลขหน้า 15)

---

## Slide 16

**หัวเรื่อง:** Self Testing & Fault Secure

**หัวข้อย่อย (ด้านซ้าย):**
- `• Self Testing:`
  - `– Y(X1,f2)`, `Y(X2,f1)`, `Y(X2,f2)` โดย `Y(X1,f2)` ถูกเน้นพื้นหลังสีเหลือง
- `• Fault Secure:`
  - `– Y(X1,f1)`, `Y(X2,f1)`, `Y(X1,f2)`, `Y(X2,f2)` โดย `Y(X1,f1)` ถูกเน้นพื้นหลังสีฟ้า
- `• Undetectable Fault:`
  - `– Y(X2,f3)` โดยถูกเน้นพื้นหลังสีเทา

**แผนภาพบน — "All faults":** กรอบสี่เหลี่ยมป้าย `All faults` ภายในวงกลม `F` มีจุด `f_1`, `f_2` ภายในวง และ `f_3` ภายนอกวง

**แผนภาพล่าง:** เหมือน Slide 15 โดยเพิ่มการไฮไลต์
- `Input space Ω_x` (วงรี `N` มี `X_1`, `X_2`) และ `Output space Ω_y` (วงรี `S`)
- ลูกศรป้าย: `Y(X1, f2)` (ล้อมวงสีเหลือง), `Y(X1, λ) √`, `Y(X1, f1)` (ล้อมวงสีฟ้า), `Y(X2, f1)`, `Y(X2, f3)` (ล้อมวงสีเทา), `Y(X2, λ) √`, `Y(X2, f2)`

(มุมขวาล่างมีเลขหน้า 16)

---

## Slide 17

**หัวเรื่อง:** Self Testing & Fault Secure EXOR circuit

**แผนภาพวงจร:** กรอบเส้นประป้าย `L` ภายในมี XOR gate เรียงในแนวตั้ง (สัญลักษณ์ Exclusive-OR)
- แถวบนสุด: อินพุต `a_0`, `b_0` → เอาต์พุต `c_0`
- แถวถัดมา: อินพุต `a_1`, `b_1` → เอาต์พุต `c_1`
- จุดไข่ปลา (…) แทนแถวกลาง
- แถวล่าง: อินพุต `a_{n-1}`, `b_{n-1}` → เอาต์พุต `c_{n-1}`
- แถวล่างสุด: อินพุต `a_p`, `b_p` → เอาต์พุต `c_p`

**รายการด้านขวา (สีแดง):**
- `Fault Secure`
- `Self Testing`
- `Code Preserving`

**สูตรด้านขวา:**
- `A = (a_0 a_1 . . . a_{n-1} a_p)`
- `B = (b_0 b_1 . . . b_{n-1} b_p)`
- `C = (c_0 c_1 . . . c_{n-1} c_p)`

**สัญลักษณ์มุมขวาล่าง:** สัญลักษณ์เกต XOR พร้อมป้าย `: Exclusive-OR (XOR) gate`

(มุมขวาล่างมีเลขหน้า 17)

---

## Slide 20

**หัวเรื่อง:** Strongly Fault Secure for m faults

**ส่วนบน — "Fewer than m faults" (ป้ายเหนือกล่อง):**
- ลูกศรอินพุตป้าย `∀ X ∈ N` (ใช้สัญลักษณ์ for all)
- กล่อง `Circuit L` ภายในมี `<f1, f2, . . ., f_{m-1}>`
- ลูกศรเอาต์พุต: `Y(X, <f1, f2, . . ., f_{m-1}>) = Y(X, λ)`
- แผนภาพล่าง: วงรีซ้อน `Ω_x` (ภายใน `N`) และ `Ω_y` (ภายใน `S`) มีลูกศรป้าย `∀ X ∈ N` เข้า และ `Y(X, <f1, f2, . . ., f_{m-1}>)` ออกไปเป็น `Y(X, λ)`

**ส่วนล่าง — "m faults" (ป้ายเหนือกล่อง):**
- ลูกศรอินพุตป้าย `∃ X ∈ N` (มีอยู่อย่างน้อยหนึ่ง)
- กล่อง `Circuit L` ภายในมี `<f1, f2, . . ., f_{m-1}, f_m>`
- ลูกศรเอาต์พุต: `Y(X, <f1, f2, . . ., f_m>) ∉ S`
- แผนภาพล่าง: วงรีซ้อน `Ω_x` (ภายใน `N`) และ `Ω_y` (ภายใน `S`) ลูกศร `∃ X ∈ N` เข้า และ `Y(X, <f1, f2, . . ., f_m>)` ชี้ไปยังพื้นที่นอก `S`

(มุมขวาล่างมีเลขหน้า 20)

---

## Slide 21

**หัวเรื่อง:** Example of SFS Circuit

**แผนภาพวงจรลอจิก:**
- อินพุต `x_1` เข้าสู่ `AND_1`
- อินพุต `x_2` แยกสองทาง: ทางหนึ่งเข้าสู่ `NOT` (อินเวอร์เตอร์) และอีกทางลากไปด้านล่าง
- เอาต์พุตของ `NOT` เข้าสู่ `AND_2`
- เอาต์พุต `AND_1` และ `AND_2` เข้าสู่เกต `OR` แล้วออกเป็นเอาต์พุต
- ป้ายความผิดพลาด (faults) ระบุบนเส้น:
  - `f_4: stuck-at '1'` (บนเส้นเอาต์พุตของ `AND_1`)
  - `f_1: stuck-at '1'` (บนเส้นอินพุตที่เข้าสู่ `AND_1`)
  - `f_3: stuck-at '1'` (บนเส้นเอาต์พุตของ `NOT`)
  - `f_2: stuck-at '0'` (บนเส้นอินพุต/ทางแยกที่เข้าสู่ `NOT`/`AND_2`)
- ป้ายด้านซ้าย: `(1 0 0 / 0 1 0) = N` และคำบรรยาย `N: Input Codespace`
- ป้ายด้านขวา: `(1 0 / 0) = S` และคำบรรยาย `S: Output Codespace`
- ป้าย `F = {f_1, f_2, f_3, f_4}`

**เนื้อหาด้านล่าง (bullets และสูตร):**
- `• For Input   N = { (x_1 / x_2) } = { (0/0), (0/1), (1/0) }`
- `• Fault Secure for the fault sequence ⟨f_1, f_2, f_3⟩` (คำว่า `Fault Secure` สีฟ้า)
  - `Y(X, ⟨f_1, f_2, f_3⟩) = (Y(X, λ)  for all X ∈ N)`
- `• For Input   X_1 ∈ { (0/0), (0/1) }`
- `• Strongly Fault Secure for ⟨f_1, f_2, f_3, f_4⟩` (คำว่า `Strongly Fault Secure` สีแดง)
  - `Y(X_1, ⟨f_1, f_2, f_3, f_4⟩) = (1/0) ∉ S`

(มุมขวาล่างมีเลขหน้า 21)

---

## Slide 23

**หัวเรื่อง:** Error Secure Circuits

**หัวข้อย่อย:** `• Error Secure (ES)` (สีแดง)
- `– The property to ensure that for any non-codeword input, the circuit output will be either a correct codeword (Fault Masking) or non-codeword`
  (คำว่า `any non-codeword input`, `correct codeword (Fault Masking)` และ `non-codeword` เป็นสีแดง)

**แผนภาพ:** วงรีซ้อนสองวง
- วงซ้าย: พื้นที่วงใน `codeword` (สีน้ำเงิน) มี `i_cw`; พื้นที่วงนอก `non-codeword` มี `i_nc`
- วงขวา: พื้นที่วงใน `correct` มี `y_cw`; พื้นที่วงนอก `incorrect` (สีแดง) มี `y_nc`
- ลูกศร:
  - `f_es(i_cw)` ชี้ไปที่ `y_cw` (correct)
  - `f_es(i_nc)` ชี้ไปที่ `y_nc` (non-codeword)

(มุมขวาล่างมีเลขหน้า 23)

---

## Slide 25

**หัวเรื่อง:** Code Disjoint Circuits

**หัวข้อย่อย:** `• Code Disjoint (CD)` (สีแดง)
- `– The property of fault-free circuits to ensure that for any codeword/ non-codeword input, the output will be a correct codeword/ non-codeword`
  (คำว่า `any codeword/ non-codeword` และ `correct codeword/ non-codeword` เป็นสีแดง)

**แผนภาพ:** วงรีซ้อนสองวง
- วงซ้าย: พื้นที่วงใน `codeword` มี `i_cw`; พื้นที่วงนอก `non-codeword` มี `i_nc`
- วงขวา: พื้นที่วงใน `correct` มี `y_cw`; พื้นที่วงนอก `incorrect` (สีแดง) มี `y_nc`
- ลูกศร:
  - `f_cd(i_cw)` ชี้ไปที่ `y_cw` (correct)
  - `f_cd(i_nc)` ชี้ไปที่ `y_nc` (non-codeword)

(มุมขวาล่างมีเลขหน้า 25)

---

## Slide 27

**หัวเรื่อง:** Strongly Code Disjoint for m faults

**ส่วนบน — ป้าย "Fewer than m faults" (อยู่ใต้กล่อง):**
- ลูกศรอินพุตป้าย `∀ X ∈ Ω_x - N`
- กล่อง `Circuit L` ภายในมี `<f1, f2, . . ., f_{m-1}>`
- ลูกศรเอาต์พุต: `Y(X, <f1, f2, . . ., f_{m-1}>) ∉ S`
- แผนภาพล่าง: วงรีซ้อน `Ω_x` (ภายใน `N`) และ `Ω_y` (ภายใน `S`)
  - ลูกศร `∀ X ∈ N` เข้าสู่วง `N`
  - ลูกศร `∀ X ∈ Ω_x - N` เข้าสู่วง `Ω_x`
  - ลูกศรกลางป้าย `Y(X, <f1, f2, . . ., f_{m-1}>)`
  - ลูกศรย้อนกลับจาก `S` ไปยังพื้นที่ `Ω_x` (แยกออกจาก `N`)

**ส่วนล่าง — ป้าย "m Faults":**
- ลูกศรอินพุตป้าย `∃ X ∈ N`
- กล่อง `Circuit L` ภายในมี `<f1, f2, . . ., f_{m-1}, f_m>`
- ลูกศรเอาต์พุต: `Y(X, <f1, f2, . . ., f_m>) ∉ S`
- แผนภาพล่าง: วงรีซ้อน `Ω_x` (ภายใน `N`) และ `Ω_y` (ภายใน `S`)
  - ลูกศร `∃ X ∈ N` เข้า
  - ลูกศรป้าย `Y(X, <f1, f2, . . ., f_m>)` ชี้ไปยังพื้นที่นอก `S`

(มุมขวาล่างมีเลขหน้า 27)

---

## Slide 28

**บรรทัดบนสุด (สูตร):**
- `codeword{(A, B), (C, D), (X, Y)} ∈ {(0,0), (0,1), (1,0)}`

**โจทย์ (ภาษาไทย สีแดง):**
1. `วงจรนี้เป็น CD? ในกรณี Fault-free`
2. `วงจรนี้เป็น FS? ST? สำหรับ {f1} ในกรณีเกิด Stuck-at-0 Fault`
3. `วงจรนี้เป็น FS? ST? สำหรับ {f2} ในกรณีเกิด Stuck-at-0 Fault`
4. `วงจรนี้เป็น FS? ST? สำหรับ {f3} ในกรณีเกิด Stuck-at-1 Fault`

**แผนภาพวงจรลอจิก (ซ้าย):** อินพุต `A`, `B`, `C`, `D` เข้าสู่เกต AND หลายตัว มีป้าย: `AC`, `BD`, `AB`, `CD`, `BC`, `AD`
- เอาต์พุตบน (ผ่าน OR gate) = `X`
- เอาต์พุตล่าง (ผ่าน OR gate) = `Y`
- จุดความผิดพลาด (เครื่องหมายกากบาทสีแดง):
  - `f1` บนเส้นอินพุต `A`
  - `f2` บนเส้นอินพุต (เส้นร่วม)
  - `f3` บนเส้นเอาต์พุตของเกต `AB` (เส้นที่เข้าสู่ OR)

**ตารางความจริง (ขวา):**

| AB | CD | Normal | f1sa0 | f2sa0 | f3sa1 |
|----|----|--------|-------|-------|-------|
| 00 | 00 | 00 | | | |
| 00 | 01 | 00 | | | |
| 00 | 10 | 00 | | | |
| 01 | 00 | 00 | | | |
| 01 | 01 | 10 | | | |
| 01 | 10 | 01 | | | |
| 10 | 00 | 00 | | | |
| 10 | 01 | 01 | | | |
| 10 | 10 | 10 | | | |
| 00 | 11 | 11 | | | |
| 01 | 11 | 11 | | | |
| 10 | 11 | 11 | | | |
| 11 | 00 | 11 | | | |
| 11 | 01 | 11 | | | |
| 11 | 10 | 11 | | | |
| 11 | 11 | 11 | | | |

(คอลัมน์ `f1sa0`, `f2sa0`, `f3sa1` ว่างเปล่าในสไลด์นี้ — เป็นโจทย์ให้เติม; แถวตั้งแต่ `00 11` ลงมา คั่นด้วยเส้นสีแดง)
(มุมขวาล่างมีเลขหน้า 28)

---

## Slide 29

**บรรทัดบนสุด (สูตร):**
- `codeword{(A, B), (C, D), (X, Y)} ∈ {(0,0), (0,1), (1,0)}`

**โจทย์ (ภาษาไทย สีแดง):**
1. `วงจรนี้เป็น CD? ในกรณี Fault-free`
2. `วงจรนี้เป็น FS? ST? สำหรับ {f1} ในกรณีเกิด Stuck-at-0 Fault`
3. `วงจรนี้เป็น FS? ST? สำหรับ {f2} ในกรณีเกิด Stuck-at-0 Fault`
4. `วงจรนี้เป็น FS? ST? สำหรับ {f3} ในกรณีเกิด Stuck-at-1 Fault`

**แผนภาพวงจรลอจิก:** เหมือน Slide 28 — อินพุต `A`, `B`, `C`, `D`; เกต `AC`, `BD`, `AB`, `CD`, `BC`, `AD`; เอาต์พุต `X`, `Y`; จุด fault `f1`, `f2`, `f3`

**ตารางความจริง (เติมค่าแล้ว):**

| AB | CD | Normal | f1sa0 | f2sa0 | f3sa1 |
|----|----|--------|-------|-------|-------|
| 00 | 00 | 00 | 00 | 00 | 11 |
| 00 | 01 | 00 | 00 | 00 | 11 |
| 00 | 10 | 00 | 00 | 00 | 11 |
| 01 | 00 | 00 | 00 | 00 | 11 |
| 01 | 01 | 10 | 10 | 10 | 11 |
| 01 | 10 | 01 | 01 | 01 | 11 |
| 10 | 00 | 00 | 00 | 00 | 11 |
| 10 | 01 | 01 | 00 | 01 | 11 |
| 10 | 10 | 10 | 00 | 10 | 11 |
| 00 | 11 | 11 | 11 | 11 | 11 |
| 01 | 11 | 11 | 11 | 11 | 11 |
| 10 | 11 | 11 | 11 | 11 | 11 |
| 11 | 00 | 11 | 00 | 00 | 11 |
| 11 | 01 | 11 | 10 | 11 | 11 |
| 11 | 10 | 11 | 01 | 11 | 11 |
| 11 | 11 | 11 | 11 | 11 | 11 |

(ค่าในคอลัมน์ `f1sa0`, `f2sa0`, `f3sa1` บางช่องเป็นตัวสีแดง; แถวตั้งแต่ `00 11` ลงมา คั่นด้วยเส้นสีแดง)
(มุมขวาล่างมีเลขหน้า 29)

---

## Slide 30

**หัวเรื่อง:** Self Checking Logic Network

**แผนภาพ:** กรอบสี่เหลี่ยมเส้นหนา (แทน `Circuit network`) ภายในมี subnetwork เป็นกรอบเส้นประสองส่วน

**ป้ายกำกับ:**
- `Circuit block` ชี้ไปที่กล่อง `L_{0,0}`
- `Circuit network` (ด้านบนขวา)
- `Subnetwork L_{i1}` (กรอบเส้นประซ้าย)
- `Subnetwork L_i` (กรอบเส้นประขวา)
- `Interface circuit block` ชี้ไปที่กล่อง `L_{i,j}`

**กล่องภายใน:**
- Subnetwork ซ้าย: `L_{0,0}`, `L_{0,1}`, `L_{i-1,0}`, `L_{i-1,k}`, `L_{i-1,k+1}`
- Subnetwork ขวา: `L_{i,0}`, `L_{i,j}`, `L_{i,m}`
- มีเส้นเชื่อมต่อระหว่างกล่อง (เส้นประและเส้นทึบ) พร้อมจุดไข่ปลา (…) แทนบล็อกที่ละไว้
- มีเส้นอินพุตเข้ามาจากด้านซ้าย (3 เส้น) และเส้นเอาต์พุตออกทางขวา

(มุมขวาล่างมีเลขหน้า 31)

---

## Slide 33

**หัวเรื่อง:** Cascaded Inverter-free Network

**แผนภาพวงจร:** โมดูลเรียงซ้อน 3 โมดูล แต่ละโมดูลเป็นกรอบเส้นประ: `L_0`, `L_1`, `L_2`
- โมดูล `L_0`: มีเกต AND ป้าย `A_0` และเกต OR ป้าย `O_0`; อินพุต `a_0`, `a_1`, `b_0`, `b_1`; มีการสลับเส้น (crossover); เอาต์พุต `c_0`, `c_1`
- จุด fault: `f_1: stuck-at '1'` บนเส้น `c_0` (ก่อนเข้า `L_1`)
- โมดูล `L_1`: เกต AND ป้าย `A_1` และเกต OR ป้าย `O_1`; อินพุต `d_0`, `d_1`; เอาต์พุต `e_0`, `e_1`
- โมดูล `L_2`: เกต AND ป้าย `A_2` และเกต OR ป้าย `O_2`; อินพุต `g_0`, `g_1`; เอาต์พุต `h_0`, `h_1`
- จุด fault: `f_2: stuck-at '1'` บนเส้นอินพุต `g_1` (ก่อนเกต `O_2`)

**เนื้อหาด้านล่าง (bullets):**
- `• SFS for the unidirectional fault sequence < f1, f2 > and for restricted inputs`
- `• Each circuit block is not always CD` (คำว่า `Each circuit block is not always CD` เป็นสีแดง)
- `• Non-codewords can appear at embedded interfaces of the network before a non-codeword is produced as the first erroneous output` (คำว่า `non-codeword` และ `first erroneous output` เป็นสีแดง)

(มุมขวาล่างมีเลขหน้า 34)

---

## Slide 35

**หัวเรื่อง:** Checkers — Self Checking Model

**แผนภาพบล็อก:** เหมือน Slide 5 (แผนผัง Self Checking Model)
- กรอบใหญ่ล้อมระบบ มีป้าย `G`
- กล่อง `Functional Unit L` และ `Checker CK`
- `Input` ตัวแปร `X` เข้าทั้ง `Functional Unit L` และ `Checker CK`
- จาก `Functional Unit L` ลงไปยัง `Checker CK` ป้าย `W`
- `Output` ตัวแปร `Y` ออกทางขวา โดยมีจุดแยกย้อนกลับเข้า `Checker CK`
- `Error Indicator` ตัวแปร `Z` ออกจาก `Checker CK` ลงด้านล่าง

(มุมขวาล่างมีเลขหน้า 36)

---

## Slide 36

**หัวเรื่อง:** Types of Checker

**หัวข้อย่อยที่ 1:** `• Code Checker/ Output encoded Checker` (คำว่า `Code Checker/` เป็นสีแดง)
- แผนภาพ: กรอบใหญ่มีป้าย `G`
  - `X` เข้าสู่กล่อง `Circuit L`
  - เอาต์พุตจาก `Circuit L` แยกเป็น `Y` (ออกทางขวา) และเข้าสู่กล่อง `Code checker CK`
  - `Code checker CK` มีเอาต์พุต `Z` ออกทางขวา

**หัวข้อย่อยที่ 2:** `• Prediction Checker/ Output Non-encoded Checker` (คำว่า `Prediction Checker/` เป็นสีแดง)
  - `• Duplication checker, Parity prediction checker, Input regeneration checker`

(มุมขวาล่างมีเลขหน้า 37)

---

## Slide 37

**หัวเรื่อง:** Duplication Checkers

**หัวข้อย่อย:**
- `• The functional circuit L is duplicated, and the outputs are compared`

**แผนภาพ:** กรอบใหญ่มีป้าย `G`
- `X` เข้าสู่กล่อง `L` สองกล่อง (ดูplicated) โดยกล่องบนและกล่องล่าง
- เอาต์พุตจากกล่อง `L` บน → ไปเป็น `Y` (ออกทางขวา)
- เอาต์พุตของกล่อง `L` ทั้งสอง เข้าสู่กล่อง `Compare circuit` ซึ่งอยู่ในกรอบเส้นประป้าย `CK`
- เอาต์พุตจาก `Compare circuit` = `Z` (ออกทางขวา)

(มุมขวาล่างมีเลขหน้า 38)

---

## Slide 38

**หัวเรื่อง:** Parity Prediction Checkers

**หัวข้อย่อย:**
- `• Output parity prediction P from input X`
- `• Output parity generator from output Y`
- `• Compare both output`

**แผนภาพ:** กรอบใหญ่มีป้าย `G`
- `X` เข้าสู่กล่อง `L`
- เอาต์พุตจาก `L` → `Y` (ออกทางขวา) และแยกเข้าสู่บล็อก `Output parity generator` (มีสัญลักษณ์ ⊕ ในรูปสามเหลี่ยม)
- ป้าย `P` ชี้ไปที่กล่อง `Output parity perdiction circuit` (สะกดตามต้นฉบับ `perdiction`)
- ทั้ง `Output parity generator` และ `Output parity perdiction circuit` อยู่ในกรอบเส้นประป้าย `CK` และส่งค่าเข้าสู่กล่อง `Compare circuit`
- `Compare circuit` มีเอาต์พุต `Z`

(มุมขวาล่างมีเลขหน้า 39)

---

## Slide 39

**หัวเรื่อง:** Input Regeneration Checkers

**หัวข้อย่อย:**
- `• Regenerate inputs from outputs by inverse logic`
- `• Then compare wt the original inputs` (สะกดตามต้นฉบับ `wt`)

**แผนภาพ:** กรอบใหญ่มีป้าย `G`
- `X` เข้าสู่กล่อง `L`
- เอาต์พุตจาก `L` → `Y` (ออกทางขวา) และแยกเข้าสู่กล่อง `L^{-1}` (อยู่ในกรอบเส้นประป้าย `CK`)
- `L^{-1}` สร้างอินพุตที่สร้างใหม่ (regenerated) ส่งเข้าสู่กล่อง `Compare circuit` (ภายในกรอบ `CK`)
- อินพุตเดิม `X` ก็ถูกส่งเข้าสู่ `Compare circuit` ด้วย เพื่อเปรียบเทียบ
- เอาต์พุต `Compare circuit` ออกด้านล่างเป็น `Z`

(มุมขวาล่างมีเลขหน้า 40)

---

## Slide 40

**หัวเรื่อง:** Simplified Regeneration Checkers

**หัวข้อย่อย:**
- `• Select only 1 input to check`

**สูตร:** `x_1 = y_0 ⊕ y_1 · y_2`

**ตารางความจริง (ขวาบน):**

| x0 | x1 | x2 | y0 | y1 | y2 |
|----|----|----|----|----|----|
| 0 | 0 | 0 | 1 | 1 | 1 |
| 0 | 0 | 1 | 0 | 0 | 1 |
| 0 | 1 | 0 | 1 | 0 | 0 |
| 0 | 1 | 1 | 0 | 1 | 1 |
| 1 | 0 | 0 | 0 | 0 | 0 |
| 1 | 0 | 1 | 0 | 1 | 0 |
| 1 | 1 | 0 | 1 | 1 | 0 |
| 1 | 1 | 1 | 1 | 0 | 1 |

**แผนภาพ:** กรอบ `L` มีอินพุต `X0`, `X1`, `X2` และเอาต์พุต `y0`, `y1`, `y2`
- ที่จุดแยก `X1`, `X2` และ `y0` มีการเชื่อมต่อไปยังวงจรตรวจสอบในกรอบเส้นประป้าย `CK`
- ภายใน `CK`: เกต `A` (AND) รับ `X1`, `X2` → เข้าเกต `XOR` ร่วมกับ `y0` (ที่แยกมา) → ผลลัพธ์เข้าเกต OR อีกตัว ร่วมกับ `X1` (ที่แยกมาตรง) → เอาต์พุต `Z`

(มุมขวาล่างมีเลขหน้า 41)

---

## Slide 43

**หัวเรื่อง:** Input and Output Space of Checkers

**หัวข้อย่อยที่ 1:** `• Code Checker`
- แผนภาพ: วงรี `Ω_y` (ภายในวงใน `S`) → ลูกศร `Y` → กล่อง `Code checker` → ลูกศร `Z` → วงรี `Ω_z` (ภายในวงใน `B`)
- ป้ายใต้ `Ω_y`: `Codespace  Y(X, f) ∈ S` และ `Noncodespace  Y(X, f) ∉ S`
- ป้ายใต้ `Ω_z`: `Codespace  {(0, 1) (1, 0)}` และ `Noncodespace  {(0, 0) (1, 1)}`

**หัวข้อย่อยที่ 2:** `• Prediction Checker`
- แผนภาพ: ลูกศร `X` และ `Y` เข้าสู่กล่อง `Prediction checker` → ลูกศร `Z` → วงรี `Ω_z` (ภายในวงใน `B`)
- ป้ายใต้ `Ω_y`/ด้านซ้าย: `Codespace  {(X, Y) | Y = Y0}` และ `Noncodespace  {(X, Y) | Y ≠ Y0}   Y0 = Y(X, λ)`
- ป้ายใต้ `Ω_z`: `Codespace  {(0, 1) (1, 0)}` และ `Noncodespace  {(0, 0) (1, 1)}`

(มุมขวาล่างมีเลขหน้า 44)

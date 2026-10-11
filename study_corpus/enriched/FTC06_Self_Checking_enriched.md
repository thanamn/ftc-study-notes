# FTC06_Self_Checking — Enriched (slide text + vision of visual slides)

> Text = exact extraction from the born-digital PDF. For `visual` slides, a faithful description of the figure/table/formula is added under **รายละเอียดจากภาพ**. Vision descriptions are model-produced and marked as such.

## Slide 1: Schedule
• Mon 14 Sep, FTC06 Self Checking✓
• Mon 21 Sep, No Class
• Mon 28 Sep, FTC07 Fault Masking
• Mon 05 Oct, Review
• Mon 12 Oct, Midterm (Fault Tolerant Computing)
 - 13.30-16.30 -TBD-
 - Open any Books including notebooks!!
• Mon 19 Oct, TDC01 Overview of Testing Digital Circuits
• Mon 26 Oct, TDC02 Delay Fault Testing
• Mon 02 Nov, TDC03 Digital Circuit Testing Issues
• Mon 09 Nov, TDC04 Asynchronous Circuit Testing
• Mon 16 Nov, Review

---

## Slide 2: Fault Tolerant System Implementation
(Self Checking Circuits)

 2110473 Fault Tolerant Computing

 Eiji Fujiwara, Code Design for Dependable Systems, JOHN WILEY & SONS, 2006

---

## Slide 3: Contents
• Self Checking Concept
• Fault Secure and Self Testing
• Totally Self Checking and Strongly Fault Secure
• Error Secure and Error Preserving
• Strongly Code Disjoint
• Self Checking Logic Network
• Types of Checker
• Self Checking Checker
• Implementations of Checker
• Implementations of Functional Units

---

## Slide 4: Error Control  *(visual)*
• Fault Masking Scheme

 Error Control
 Codes
 Corrected
 Functional Unit Corrector Output

Error Control Overlapped
 Codes Parity
 Syndrome

 Checker Status

**รายละเอียดจากภาพ (vision):**

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

---

## Slide 5: Self Checking Model  *(visual)*
• Concurrent Fault/Error Detection Scheme

 G Output Input Functional
 Unit L X Y
 W
 Checker
 CK

 Error Indicator Z

**รายละเอียดจากภาพ (vision):**

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

---

## Slide 6: Self Checking Concept
• Self Checking is an approach for Concurrent error
 detection (CED) that allows:
 - detection of both temporary and permanent faults
 - early detection of errors so that corrective action can
 be initiated before data corruption
 - easy identification of the field replaceable unit (eg. a
 chip or a board)
• The use of a CED scheme in order to achieve the
 high reliability requirement of modern systems is
 becoming an important design technique

---

## Slide 7: Error Detecting Codes
• Design of Self Checking logic circuits is based
 on error detecting codes
• Error detecting codes - specific presentation of
 symbols which enables error detection inside
 codeword
• Most frequently used error detecting codes:
 - Separable:- Parity code, Berger Code
 - Non-Separable:-m-of-n Code, Dual Rail Code (Two
 Rail Code)

---

## Slide 8: Basic Idea of Self Checking
• Digital circuit has a self checking property if it is able to
 detect internal faults immediately after its occurrence,
 without using external test signals
• Information redundancy (Error Control Coding), which
 require an additional hardware, is introduced
 - The outputs of function units must satisfy specific features
• Function unit designed in a way that
 faults/errors/malfunctions manifest themselves as
 invalid (error-space) outputs, which are detectable by
 an external code checker

---

## Slide 9: Four possibilities of
Functional Unit & Checker

 Input
 Functional Unit Output

 Checker Indicator

1. Both functional unit and checker okay
2. Only functional unit okay
 - false alarm may be raised, but this is safe
3. Only checker okay
 - we have either no output error or a detectable error
4. Neither functional unit nor checker okay
 - use 2-output checker; a single check signal stuck-at-okay
 goes undetected, leading to fault accumulation

---

## Slide 10: Code Space and Error Space  *(visual)*
Encoded Functional Encoded
 input unit output

 Self-checking
Implementation of the desired
 code checker
functionality with coded values
 Status

 Codespace f1 Codespace
 f2

 f3
 f4
 Error ? Error
 space space

 Input Output

**รายละเอียดจากภาพ (vision):**

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

---

## Slide 11: Cascade of Self Checking Modules  *(visual)*
Encoded
 Encoded Functional output Functional
 input unit 1 unit 2

 Self-checking Self-checking
 checker checker

 Codespace f Codespace
 f

 Error Error
 space space

 Input Output

**รายละเอียดจากภาพ (vision):**

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

---

## Slide 12: Definition of Fault Secure and Self Testing
• A circuit 𝐿is Fault Secure (FS) for an input set
 𝑁and a fault set 𝐹, if for input 𝑋in 𝑁and for
 any fault 𝑓in 𝐹,
 𝑌𝑋, 𝑓= 𝑌𝑋, 𝜆 𝑜𝑟𝑌(𝑋, 𝑓) ∉𝑆
• A circuit L is Self Testing (ST) for an input set 𝑁
 and a fault set 𝐹, if for every fault 𝑓in 𝐹there
 is some input 𝑋in 𝑁such that 𝑌(𝑋, 𝑓) is not
 in 𝑆
 S: Output Codespace, : Null Fault

---

## Slide 13: Characteristics of SC circuits  *(visual)*
• Fault Secure (FS)
 - The property to ensure that for any possible fault,
 the circuit output is either a correct codeword or
 non-codeword

 codeword
 correct

 ffs(icw) ync
 icw ycc

 yic

 incorrect
 non-codeword 13

**รายละเอียดจากภาพ (vision):**

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

---

## Slide 14: Characteristics of SC circuits  *(visual)*
• Self Testing (ST)
 - The property to ensure that for every possible
 fault, there is at least one input codeword for
 which the resulting output is a non-codeword
 codeword
 correct

 fst(icwt) ync
 icwt yi icwi
 fst(icwi)

 incorrect
 non-codeword 14

**รายละเอียดจากภาพ (vision):**

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

---

## Slide 15: Self Testing & Fault Secure  *(visual)*
• Self Testing: ?
• Fault Secure: ?
• Undetectable Fault: ?

 

 

**รายละเอียดจากภาพ (vision):**

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

---

## Slide 16: Self Testing & Fault Secure  *(visual)*
• Self Testing:
- Y(X1,f2), Y(X2,f1), Y(X2,f2)
• Fault Secure:
- Y(X1,f1), Y(X2,f1), Y(X1,f2), Y(X2,f2)
• Undetectable Fault:
- Y(X2,f3)

 

 

**รายละเอียดจากภาพ (vision):**

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

---

## Slide 17: Self Testing & Fault Secure EXOR circuit  *(visual)*
• Fault Secure
 • Self Testing
 • Code Preserving

**รายละเอียดจากภาพ (vision):**

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

---

## Slide 18: Totally Self Checking (TSC)
• A circuit is totally self checking if it is both Self
 Testing and Fault Secure
• An Ideal property but;
 - Not every fault can be detected by codeword
 - Undetectable faults in redundant circuits

• Even FS but undetectable fault is existing; the
 next coming faults may invalidate FS property

---

## Slide 19: Strongly Fault Secure (SFS)
• A circuit is Strongly Fault Secure if 1 or 2;
 1. TSC for fault {𝑓},
 2. Both FS for fault {𝑓} AND SFS for 𝐹−{𝑓}

• In case the fault 𝑓1 ∈{𝑓} is not be detected, still
 guarantee that the next fault 𝑓2 ∈𝐹−{𝑓} also
 satisfy 1 or 2
• The first output error is non-codeword

---

## Slide 20: Strongly Fault Secure  *(visual)*
for m faults

**รายละเอียดจากภาพ (vision):**

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

---

## Slide 21: Example of SFS Circuit  *(visual)*
N: Input Codespace S: Output Codespace

 𝑥1 0 0 1 • For Input 𝑁= = , ,
 𝑥2 0 1 0
 • Fault Secure for the fault sequence 𝑓1, 𝑓2, 𝑓3
 𝑌𝑋, 𝑓1, 𝑓2, 𝑓3 = (𝑌𝑋, 𝜆 𝑓𝑜𝑟𝑎𝑙𝑙𝑋∈𝑁)
 0 0
 ∈ , • For Input 𝑋1 0 1
 • Strongly Fault Secure for 𝑓1, 𝑓2, 𝑓3, 𝑓4
 1
 𝑌𝑋1, 𝑓1, 𝑓2, 𝑓3, 𝑓4 = ∉𝑆
 21 0

**รายละเอียดจากภาพ (vision):**

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

---

## Slide 22: Error Secure
• Considering the behavior of the circuits (self-
 checking checkers) for non-codeword inputs
• A Circuit 𝐿with output codespace 𝑆is Error
 Secure (ES) for noncodespace (input) 𝛺𝑋−𝑁
 if for any input 𝑋𝑞in 𝛺𝑋−𝑁, where 𝑋𝑞=
 𝑋𝑝+ 𝐸, 𝑋𝑝∈𝑁, 𝐸≠0

 𝑌𝑋𝑞, 𝜆∉𝑆𝑜𝑟𝑌𝑋𝑞, 𝜆= 𝑌(𝑋𝑝, 𝜆)

 N: Input Codespace, E: Input Error, S: Output Codespace, : Null Fault

---

## Slide 23: Error Secure Circuits  *(visual)*
• Error Secure (ES)
 - The property to ensure that for any non-codeword
 input, the circuit output will be either a correct
 codeword (Fault Masking) or non-codeword

 codeword
 correct

 fes(icw) ycw icw

 fes(inc) inc ync
 incorrect
 non-codeword 23

**รายละเอียดจากภาพ (vision):**

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

---

## Slide 24: Error Preserving/Code Disjoint
• Synonymous with Code Disjoint (CD)
• A Circuit 𝐿with output codespaces 𝑆is Error
 Preserving for noncodespaces 𝛺𝑋−𝑁, if for
 any input 𝑋in 𝛺𝑋−𝑁

 𝑌𝑋, 𝜆∉𝑆

---

## Slide 25: Code Disjoint Circuits  *(visual)*
• Code Disjoint (CD)
 - The property of fault-free circuits to ensure that
 for any codeword/ non-codeword input, the
 output will be a correct codeword/ non-codeword

 codeword
 correct

 fcd(icw) ycw icw

 fcd(inc) inc ync
 incorrect
 non-codeword 25

**รายละเอียดจากภาพ (vision):**

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

---

## Slide 26: Strongly Code Disjoint
• A circuit is Strongly Code Disjoint (SCD),
 if 1 or 2
 1. CD before the fault 𝑓occur; and ST for fault {𝑓}
 2. CD before the fault 𝑓occur; and SCD for 𝐹−{𝑓}
 when the fault 𝑓occur

---

## Slide 27: Strongly Code Disjoint  *(visual)*
for m faults

**รายละเอียดจากภาพ (vision):**

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

---

## Slide 28: 1.  *(visual)*
codeword{ A, B), (C, D , X, Y } ∈{ 0,0), (0,1 , 1,0 }
1. วงจรนี้เป็น CD? ในกรณีFault-free
2. วงจรนี้เป็น FS? ST? สำหรับ {f1} ในกรณีเกิด Stuck-at-0 Fault
3. วงจรนี้เป็น FS? ST? สำหรับ {f2} ในกรณีเกิด Stuck-at-0 Fault
4. วงจรนี้เป็น FS? ST? สำหรับ {f3} ในกรณีเกิด Stuck-at-1 Fault

**รายละเอียดจากภาพ (vision):**

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

---

## Slide 29: 1.  *(visual)*
codeword{ A, B), (C, D , X, Y } ∈{ 0,0), (0,1 , 1,0 }
1. วงจรนี้เป็น CD? ในกรณีFault-free
2. วงจรนี้เป็น FS? ST? สำหรับ {f1} ในกรณีเกิด Stuck-at-0 Fault
3. วงจรนี้เป็น FS? ST? สำหรับ {f2} ในกรณีเกิด Stuck-at-0 Fault
4. วงจรนี้เป็น FS? ST? สำหรับ {f3} ในกรณีเกิด Stuck-at-1 Fault

**รายละเอียดจากภาพ (vision):**

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

---

## Slide 30: Self Checking Logic Network  *(visual)*
31

**รายละเอียดจากภาพ (vision):**

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

---

## Slide 31: Theorem & Corollary
Theorem:
 "If the subnetwork 𝐿𝐼consisting of the output
interface circuit blocks is SFS and SCD for fault set FI, and
if the remaining subnetwork LII consisting of the internal
circuit blocks is SFS for fault set FII, then the total network
is SFS for all fault sequences in FI and FII"

Corollary:
 "If the subnetwork 𝐿𝐼consisting of the output
interface circuit blocks is SFS and CD, and if the remaining
subnetwork LII consisting of the internal circuit blocks is
SFS, then the total network is SFS for all fault sequences
in either LI or LII, but not in both"

 32

---

## Slide 32: Inverter-free Network
Theorem:
• "A network that consists of only Inverter-free
 combinational circuit blocks and in which the
 block input/output interfaces are encoded
 with unidirectional error detecting codes (eg.,
 the m-out-of n code and the Berger code) is
 SFS with respect to unidirectional faults"

 33

---

## Slide 33: Cascaded Inverter-free Network  *(visual)*
• SFS for the unidirectional fault sequence < 𝑓1, 𝑓2 >
 and for restricted inputs
• Each circuit block is not always CD
• Non-codewords can appear at embedded interfaces
 of the network before a non-codeword is produced
 as the first erroneous output
 34

**รายละเอียดจากภาพ (vision):**

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

---

## Slide 34: Error Secure and Error Propagating
• A circuit block interface is Error Secure* (ES) at a
 given fault stage if any error that can occur at the
 interface never causes an incorrect codeword at any
 observable interface during the fault stage
• A circuit block interface is Error Propagating (EP) at a
 given fault stage if any error that can occur at the
 interface eventually produces a non-codeword at
 some observable interface during the fault stage

• Former ES: Block interfaces that may include some faults within them
• Latter ES*: Fault-free circuit blocks

 35

---

## Slide 35: Checkers  *(visual)*
Self Checking Model

 G Output Input Functional
 Unit L X Y
 W
 Checker
 CK

 Error Indicator Z

 36

**รายละเอียดจากภาพ (vision):**

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

---

## Slide 36: Types of Checker  *(visual)*
• Code Checker/ Output encoded Checker

• Prediction Checker/ Output Non-encoded Checker
 • Duplication checker, Parity prediction checker, Input
 regeneration checker

 37

**รายละเอียดจากภาพ (vision):**

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

---

## Slide 37: Duplication Checkers  *(visual)*
• The functional circuit L is duplicated, and the
 outputs are compared

 38

**รายละเอียดจากภาพ (vision):**

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

---

## Slide 38: Parity Prediction Checkers  *(visual)*
• Output parity prediction P from input X
• Output parity generator from output Y
• Compare both output

 39

**รายละเอียดจากภาพ (vision):**

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

---

## Slide 39: Input Regeneration Checkers  *(visual)*
• Regenerate inputs from outputs by inverse
 logic
• Then compare wt the original inputs

 40

**รายละเอียดจากภาพ (vision):**

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

---

## Slide 40: Simplified Regeneration Checkers  *(visual)*
• Select only 1 input to check

 𝑥1 = 𝑦0⨁𝑦1 ∙𝑦2

 41

**รายละเอียดจากภาพ (vision):**

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

---

## Slide 41: Self Checking Checker
Lemmas:
1. For single faults it is necessary that any
 checker must have at least two outputs and
 that no outputs take constant values
2. The Fault Secure property is not necessary
 for a checker

 42

---

## Slide 42: Self Checking Checker Properties
• 2 output lines
• Code-Disjoint (CD)
 - Codeword inputs generate only codeword outputs
 - Non-codeword inputs generate only non-codeword
 outputs
• Self Testing

• Strongly Code-Disjoint (SCD) if 1 or 2
 1. CD before the fault 𝑓occur; and ST for fault {𝑓}
 2. CD before the fault 𝑓occur; and SCD for 𝐹−{𝑓}
 when the fault 𝑓occur

 43

---

## Slide 43: Input and Output Space of Checkers  *(visual)*
• Code Checker

• Prediction Checker

 44

**รายละเอียดจากภาพ (vision):**

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

---

## Slide 44: What's wrong?  *(visual)*
Conventional code checker
Input Code Example: 5-input odd-parity checker
 space f Output

 0

 1

 e
 Error f
 space

 45

**รายละเอียดจากภาพ (vision):**

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

---

## Slide 45: Non-Self Testing Parity Code Checker  *(visual)*
Conventional code checker
Input Code Example: 5-input odd-parity checker
 space f Output
 s-a-0 fault
 0 on output?

 1

 e
 Error f
 space

 • Single output line
 • Code-Disjoint
 • non-Self Testing

 46

**รายละเอียดจากภาพ (vision):**

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

---

## Slide 46: Totally Self Checking Error Signal  *(visual)*
Combining
 Encoded
 outputEncoded Function Function In Out
 input unit 1 unit 2 0 0 0 0 0 0
 0 0 0 1 0 0
 Self-checking Self-checking 0 0 1 0 0 0Simplified truth table checker checker
 0 0 1 1 0 0if we denote
 0 1 0 0 0 001 and 10 as G, 0 1 0 1 0 1
00 and 11 as B 0 1 1 0 1 0
 0 1 1 1 1 1
 In Out 1 0 0 0 0 0
 1 0 0 1 1 0B B B
 1 0 1 0 0 1B G B
 1 0 1 1 1 1G B B Circuit to combine 1 1 0 0 0 0
G G G error signals 1 1 0 1 1 1
 (two-rail code checker) 1 1 1 0 1 1
 1 1 1 1 1 1
Show that this circuit is self-testing
 47

**รายละเอียดจากภาพ (vision):**

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

---

## Slide 47: Implementations of Checker
• Parity Code Checker
• Two Rail Code Checker
• 1-of-n Code Checker
• m-of-2m Code Checker
• TSC Checker for k-out-of-n Code
• TSC Checker for Separable Codes
• Generalized Prediction Checker (GPC)

 48

---

## Slide 48: Parity Code Checker
• Using Exclusive-OR gates in a Tree Structure
• Dividing inputs into Two Parity-Tree
Theorem:
• The parity-tree circuit that is divided into two
 independent parity-tree subcircuits is a self-
 testing checker for all odd-parity encoded
 inputs and for all single faults

 49

---

## Slide 49: Self Testing Parity Code Checker  *(visual)*
• 2 output lines
• (C1,C0) = {(0,1),(1,0)} = codeword
• (C1,C0) = {(0,0),(1,1)} = non-codeword
Ex. 8 bit data bit + 1 bit odd-parity bit

 x8
 x6 C0
 x4 • 2 output lines
 x2
 • Code-Disjoint x0
 x7 • Self Testing C1 x5
 x3 (number of 1s is even)
 x1
 Self Testing Checker
 50

**รายละเอียดจากภาพ (vision):**

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

---

## Slide 50: Two Rail Code Checker  *(visual)*
• Duplication/ Comparison Check

 51

**รายละเอียดจากภาพ (vision):**

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

---

## Slide 51: Example of Two Rail Code Checker  *(visual)*
• 2 output lines
• (C1,C0) = {(0,1),(1,0)} = codeword
• (C1,C0) = {(0,0),(1,1)} = non-codeword
Ex. 2-Pair Two Rail Code Checker: Input = {x1x0, y1y0}
x1

 C0x0 • 2 output lines
 • Code-Disjoint
 • Self Testingy1
 C1 {0101,0110,1001,1010}
y0

 Self Testing Checker 52

**รายละเอียดจากภาพ (vision):**

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

---

## Slide 52: n-Pair Two Rail Code Checker
• n=6 using Tree-Structure 2-Pair Two Rail Code Checker

 2PTRC

 53

---

## Slide 53: Two Rail Code Sequence  *(visual)*
Timing/
Sequence 1 2 3 4
 x1
 C1 R 01 01 10 10 x0 2PTRC y1 C0
 S 01 10 01 10 y0
 T 01 10 10 01 Self Testing for all Stuck-at Faults

 IO/
 Timing x1 x0 y1 y0 C1 C0
 1 0 1 0 1 0 1
 2 0 1 1 0 1 0
 3 1 0 0 1 1 0
 4 1 0 1 0 0 1
 R S T
 54

**รายละเอียดจากภาพ (vision):**

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

---

## Slide 54: Self Testing for 6-Pair Two Rail Code  *(visual)*
Checker

R Using RST sequence combination
 T regardless n data bit sizeS

 RS 0011
 1100 0110
 1001 T 0101
 1010
R S

S T
R

 55

**รายละเอียดจากภาพ (vision):**

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

---

## Slide 55: 1-of-n Code Checker  *(visual)*
• Decode 𝑛to 𝑘(𝑘= 𝑛) and connect to Tree- log2
 Structure k-Pair Two Rail Code Checkers

 a1
 b1 1
 a2 2 b2 Two Rail C1
 Decoder Code
 C0
 Checker
 ak
 n bk

 Ex. n=8, k=3; Decoder function:
 a1 = (1 v 2 v 3 v 4), b1=(5 v 6 v 7 v 8)
 a2 = (1 v 2 v 5 v 6), b2=(3 v 4 v 7 v 8)
 a3 = (1 v 3 v 5 v 7), b3=(2 v 4 v 6 v 8)
 56

**รายละเอียดจากภาพ (vision):**

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

---

## Slide 56: Self Testing 1-of-n Code Checker (n≠2  *(visual)*
k)

 • Connect pair (1,k) to Two Rail Code Checker (C1) and
 other pairs to k-2 Pair Two Rail Code Checker (C2)
 • All Checkers have {00,01,10,11} inputs Self Testing

 ai/Lip a1 a2 … ak-1 ak
 a1 C1 C11 1 0 0 … 0 1 b1
2 a2 C3 C0 2 0 0 … 1 0
 b2 3 0 0 … 1 1
 Decoder 2k-1 1 0 … 0 0 C2
 ak-1
 bk-1 2k-1+1 1 0 … 0 1
n ak … … … … … …
 bk

 57

**รายละเอียดจากภาพ (vision):**

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

---

## Slide 57: m-of-2m Code Checker  *(visual)*
Divide the 2m bits into two disjoint subsets A and B of m bits each
Let v and w be the weight of (number of 1s in) A and B, respectively
Implement the two code checker outputs e0 and e1 as follows:

 m
 i)(w m - i) C0 = (v
 i = 0 v 1s w 1s
 (i even)

 m bits m bits m
 j)(w m - j) Subset A Subset B C1 = (v
 j = 1
 (j odd)
 v 1s w 1s

 Ex. 3-out-of-6 code checker, m = 3, A = {a, b, c}, B = {f, g, h}
 C0 = (v 0)(w 3) (v 2)(w 1) = fgh (ab bc ca)(f g h)
 C1 = (v 1)(w 2) (v 3)(w 0) = (a b c)(fg gh hf) abc
 Always satisfied

 58

**รายละเอียดจากภาพ (vision):**

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

---

## Slide 58: Another TSC  *(visual)*
m-out-of-2m Code Checker

Cellular realization, due to J. E. Smith:
This design is testable with only 2m inputs,
all having m consecutive 1s (in cyclic order)

 m - 1 stages

 . . . .
 . . . .
 . . . .

 59

**รายละเอียดจากภาพ (vision):**

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

---

## Slide 59: Using 2-out-of-4 Checkers as Building Blocks  *(visual)*
Building m-out-of-2m TSC checkers, 3 m 6, from 2-out-of-4 checkers
(construction due to Lala, Busaba, and Zhao):

Ex. 3-out-of-6 and 4-out-of-8 TSC checkers are depicted below
(only the structure is shown; some design details are missing)

 1 2 3 4 5 6 1 2 3 4 5 6 1 2 3 4 5 6 7 8 3 4 7 8 1 2 5 6

 2-out-of-4 2-out-of-4 2-out-of-4 2-out-of-4 2-out-of-4 2-out-of-4

 2-out-of-4 2-out-of-4 2-out-of-4 2-out-of-4

 Slightly different
 from an ordinary
 2-out-of-4 checker
 2-rail checker 2-rail checker
 3-out-of-6 4-out-of-8

 60

**รายละเอียดจากภาพ (vision):**

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

---

## Slide 60: TSC Checker for  *(visual)*
k-out-of-n Code

 2-out-of-5
One design strategy is to proceed in 3 stages: 5 bits
 n
 10 AND gatesConvert the k-out-of-n code to a 1-out-of-( ) code 1-out-of-10 k
Convert the latter code to an m-out-of-2m code 10 bits

 6 OR gatesCheck the m-out-of-2m code using a TSC checker 3-out-of-6
 6 bitsThis approach is impractical for many codes
 TSC checker

A procedure due to Marouf and Friedman: m
 j)(w m - j)Implement 6 functions of the general form e0 = (v
 j = 1
 (these have different subsets of bits as (j even)
 inputs and constitute a 1-out-of-6 code)
 e0 e1 e2 e3 e4 e5
Use a TSC 1-out-of-6 to 2-out-of-4 converter
 1-out-of-6
Use a TSC 2-out-of-4 code checker 6 bits

 OR gates 2-out-of-4The process above works for 2k + 2 n 4k
It can be somewhat simplified for n = 2k + 1 4 bits
 TSC checker

 61

**รายละเอียดจากภาพ (vision):**

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

---

## Slide 61: TSC Checker for Separable Codes  *(visual)*
Here is a general strategy for designing totally-self-checking checkers
for separable codes

 Complement n - k
 k data bits of check bits
 Two-rail generator C0
 checker C1 n - k n - k
 check bits
 Input Checker
 TSC code checker word outputs

• For many codes, direct synthesis will produce a faster and/or
 more compact totally-self-checking checker
• Require full combination of Two-rail Checker Inputs ST
• No need to consider about ST in Complement of Check Bits
 62
 Generator

**รายละเอียดจากภาพ (vision):**

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

---

## Slide 62: Berger Code Checker  *(visual)*
n - k
 k data bits Number of 1s
 in Binary Two-rail C0
 checker C1 n - k n - k
 check bits
 Input Checker
 TSC code checker word outputs

Ex. Complement of Check bit Generator of (15,4) Berger Code

 1bit FA 1bit FA 1bit FA 1bit FA

 2bit FA 2bit FA

 3bit FA 63

**รายละเอียดจากภาพ (vision):**

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

---

## Slide 63: Generalized Prediction Checker (GPC)  *(visual)*
• Self-testing checker of the combinational circuits
 having non-encoded inputs and outputs

 64

**รายละเอียดจากภาพ (vision):**

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

---

## Slide 64: TSC Functional Unit
• TSC MUX
 - Non-inverter parity code data MUX is TSC for
 unidirectional faults
• Dual-Rail Logic
 - Dual-Rail Logic converted from Non-Redundant
 Single Rail Logic is TSC for unidirectional faults

 TSC Function Unit is Costly!!

 65

---

## Slide 65: Dual Rail Logic  *(visual)*
x z
• 1-of-2 Code X Z x' z'
 {0,1} {01,10} x z X Z
• Easy Implementation x' z'
 (Encoder/Decoder) x
 z
• Preserve code after X Z y
 operation Y x' z'
 y'• Non-Inverter Circuit
 x
 z X
 Z y
 x'
 Y
 z'
 y'

 66

**รายละเอียดจากภาพ (vision):**

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

---

## Slide 66: Check Yourself: TSC Functional Unit  *(visual)*
• Dual-Logic implementation
 for
 𝐹= ത𝑎𝑏+ 𝑏ҧ𝑐+ 𝑎𝑐
• Assume one stuck-at-fault,
 - Find the property of each input
 - Conclude the property of circuit

 67

**รายละเอียดจากภาพ (vision):**

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

---

## Slide 67: Check Yourself: TSC Functional Unit  *(visual)*
• 𝐹= ത𝑎𝑏+ 𝑏ҧ𝑐+ 𝑎𝑐; ത𝐹= (𝑎+ ത𝑏)(ത𝑏+ 𝑐)(ത𝑎+ ҧ𝑐)

 The property of circuit = FS + ST = TSC

 68

**รายละเอียดจากภาพ (vision):**

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

---

## Slide 68: Contraction Circuits  *(visual)*
Definition: Contraction Circuit G'
• Circuit G' that remove signal lines and gate outputs
 which are fixed by a given fault f in the original circuit G

 S-a-0

 69

**รายละเอียดจากภาพ (vision):**

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

---

## Slide 69: SFS to TSC
Theorem
• Circuit G is SFS for faults F. If no any codeword can
 detect the fault f, and G' is a contraction circuit of G
 for the fault f, and F' is an f contraction set of F, then;
 - G' is SFS for F', and
 - When no fault, Both G and G' generate the same
 outputs against all codeword inputs

 Consider Function Unit as SFS!!

 70

---

## Slide 70: SFS Functional Unit
• Function unit is SFS when;
 -Non-redundant and
 -Non-inverter circuit and
 -Output Coding wt Unordered Codes

 71

---

## Slide 71: TSC Design with Parity Prediction  *(visual)*
Parity prediction as an alternative to duplication

 Parity
 /
 generator k
Parity- Parity-
encoded Parity encoded ALU /
inputs predictor k output

 / Ordinary ALU
 k Error
 signal

 If the parity predictor produces the complement of the output parity, and
 the XOR gate is removed, we have a self-checking design

 To ensure the TSC property, we must also verify that the parity predictor
 is testable only with input codewords

 72

**รายละเอียดจากภาพ (vision):**

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

---

## Slide 72: TSC Design with Residue Encoding  *(visual)*
Residue checking is applicable directly to addition, subtraction, and
multiplication, and with some extra effort to other arithmetic operations

 x, x mod A y, y mod A To make this scheme TSC:

 Modify the "Find mod A" box
 to produce the complement
 of the residue
 Add Add mod A
 Use two-rail checker instead of
 comparator

 Find Compare Verify the self-testing property
 mod A if the residue channel is not
 Not completely independent of the
 equal
 main computation (not needed
 s, s mod A Error for add/subtract and multiply)

 73

**รายละเอียดจากภาพ (vision):**

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

---

## Slide 73: Self-Checking Design with FPGAs
LUT-based FPGAs can suffer from the following fault types:
 Single s-a faults in RAM cells
 Single s-a faults on signal lines
 Functional faults in a multiplexer within a single CLB LUT
 Functional faults in a D flip-flop within a single CLB
 Single s-a faults in pass transistors connecting CLBs

Synthesis algorithm:
(1) Use scripts in the Berkeley synthesis tool SIS to decompose an SOP
expression into an optimal collection of parts with 4 or fewer variables
(2) Assign each part to a functional cell that produces a 2-rail output
(3) Connect the outputs of a pair of intermediate functional cells to the
inputs of a checker cell and find the output equations for that cell
(4) Cascade the checker cells to form a checker tree

Ref.: P.K. Lala, and A.L. Burress, IEEE Trans. Instrumentation and Measurement,
Vol. 52, No. 5, pp. 1391-1398, October 2003

 74

---

## Slide 74: Synthesis of TSC Systems from TSC Modules
System consists of a set of modules, with interconnections modeled
by a directed graph

Theorem 1: A sufficient condition for a system to be TSC with respect
to all single-module failures is to add checkers to the system such that
if a path leads from a module Mi to itself (a loop), then it encounters at
least one checker

Theorem 2: A sufficient condition for a system to be TSC with respect
to all multiple module failures in the module set A = {Mi} is to have no
loop containing two modules in A in its path and at least one checker
in any path leading from one module in A to any other module in A

Optimal placement of checkers to satisfy these condition

Easily solved, when checker cost is the same at every interface

 75

---

## Slide 75: Partially Self-Checking Units  *(visual)*
Some ALU functions, such as logical operations, cannot be checked
using low-redundancy codes

Such an ALU can be made partially self-checking by circumventing
the error-checking process in cases where codes are not applicable

 01, 10 = G (top) Self-checking ALU
 Residue-check 01=D,10=C(bottom) with residue code error signal ALU error
 indicator 00, 11 = B

 0 1
 1 0 In Out
 Do not check Check X B B
 B C BThe check/do-not-check indicator
 B D Gis produced by the control unit
 Normal G C G 01
 operation G D G 10

 76

**รายละเอียดจากภาพ (vision):**

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

---

## Slide 76: Self-Checking State Machines  *(visual)*
Design method for Moore-type machines, due to Diaz and Azema:

Inputs and outputs are encoded using two-rail code
States are encoded as n/2-out-of-n codewords

Fact: If the states are encoded using a k-out-of-n code, one can
express the next-state functions (one for each bit of the next state)
via monotonic expressions; i.e., without complemented variables

Monotonic functions can be realized with only AND and OR gates,
hence the unidirectional error detection capability

 Input Output Input Output
State x = 0 x = 1 z State x = 01 x = 10 z

 A C A 1 0011 1010 0011 10
 B D C 1 0101 1001 1010 10
 C B D 0 1010 0101 1001 01
 D C A 0 1001 1010 0011 01
 77

**รายละเอียดจากภาพ (vision):**

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

---

## Slide 77: Further Studies
• Self-Checking Processor
• Fault Masking Scheme
• System Reconfiguration/Recovery
• Fault Tolerance in Distributed System
• Software Fault Tolerance
• Testing Digital Circuits

 78

---

## Slide 78: HW06: Self Checking Circuits
• Design a Self-Checking 2:4 Demultiplexer with Enable

 79

---

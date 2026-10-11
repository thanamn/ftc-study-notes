# Senior exam recollection — Fault Tolerant Computing

> Source: `Fault Tolerant (senior exam).docx` · Thai exam recall (incomplete; the
> author notes some parts were lost). Original `.docx` kept alongside this file.
>
> Embedded slide image: `senior_exam_image1.png` — *Design Techniques*
> (Fault Avoidance / Fault Masking / Fault Tolerance across the fault → error → failure chain).

---

1.1 Liveness and SafetyในมุมมองFTC

1.2 Threat ของ Net Bankingมีอะไรบ้าง (Hackers,Human Error) แล้วจะส่งผลกระทบต่อ (Reliability,Safety,Avaliability...)อย่างไร แล้วจะป้องกันด้วยFTCอย่างไร (rror control self checking fault masking fail safe data security)

1.3 ถ้าโปรแกรมที่มีFail ก่อน Success (MTTF<System RUnning time) ต้องแก้ปัญหาอะไรที่ไม่ใช่ เร่งReliability หรือSuccess

1.4 ถามว่า Fail-Safe,Self Checking, Recovery ลากไปไหนในนี้

1.5 ให้ตารางเรื่องRecoveryมา แล้วบอกให้ลากกลับไปที่เวลา เท่ากัน กับไม่เท่ากัน แล้วแบบไหนเป็นอะไร?

1.6 ให้ตารางมา 13*9 dot ตรงกลางมาให้แล้วถามว่าเติมยังไงให้hamming distance =1 แล้วเป็นSingle Correction,Double Detection

2.หาความน่าจะเป็นของสักสี่ตัว

2.1 A---B

2.2A---B

A---B

2.3 A----B

|

K

|

A---B

2.4 A----B

|

K

|

A---B

|

K

|

A---B

2.5 สมมติว่าA,B,K Rเท่ากันหมด หา R ที่ทำให้ 2.2-2.4 >1.2 * Rรวม ของ2.1

2.6 แล้วเลือกอะไรดี

3.Node 7 Nodes loyal 5 Traitors 2 บอกให้หาconsensus โดย N1 ส่ง A ไป N2-N7 แล้ว N4,N5 เป็น Traitorsที่ตอบR

4. notation ที่เป็น (n,m,d) numbers,dimension ซัมติง อีกข้อบอกให้ทำสักอย่างกับ Berger แล้วสุดท้ายมีพูดเกี่ยวกับสมการ (ลืมละ) แล้วน่าให้ลองแทนดู (การบ้านเรื่องหารยาวอะ)

5. ให้inputมาแล้วถามว่า เป็นStrong Fault Tolerance, Totally self Checkingไหม

a,b,c,d,x,y = (0,0,1,1,1,0) (0,1,1,0,0,1) (1,1,0,0,0,1) (1,0,0,1,1,0) x=ad+cd y=ab+bc ถ้าa stuck 0 อินพุตที่ยังfault secureคือ และเป็นtotally self checking หรือ strongly fault secure

โค้ดเอาต์พุตถูกต้อง: one-hot {(1,0),(0,1)} {(1,0),(0,1)} (ถือว่า (0,0) (0,0), (1,1) (1,1) = non-code) Fault: Aของx stuck at 0?

6.Code A = 1 1 1 1 1 1 1, 1 1 1 1 01 1 0000111 1101111 0011000 0110000 จงแสดงnotation ของcode A ที่มีcode length =6

ที่เหลือคืองัดออกมาจากchat เพราะงั้นลืมแล้ว..

6.X=A'B'CD+AB'C'D, Y=A'BCD'+ABC'D' Cขวา stuck at 1 input เดิม??

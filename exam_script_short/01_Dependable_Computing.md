# บทที่ 1 — FTC01 Dependable Computing (ฉบับย่อ)

## Dependability คืออะไร

ลองนึกถึงระบบธนาคารออนไลน์ เราคาดหวังสามอย่างคือ เปิดใช้ได้เมื่อต้องการ (availability), แสดงข้อมูลถูกต้อง (integrity), และข้อมูลไม่รั่ว (confidentiality) ระบบที่เร็วแต่แสดงยอดผิดก็ไม่น่าเชื่อถือ และระบบที่ถูกต้องแต่ล่มบ่อยก็มีปัญหา นี่คือที่มาของ **Dependability** คือคุณสมบัติที่ทำให้การให้บริการของระบบ "ได้รับความไว้วางใจได้อย่างมีเหตุผล"

นิยามมีสองเวอร์ชัน **ยุค 1960s** บอกว่า dependability คือความน่าจะเป็นที่ระบบจะทำงานเมื่อถูกเรียกใช้ **ยุค 1995 (Laprie/Avizienis)** บอกว่าเป็น integrative concept รวมคุณสมบัติหกข้อ และมีข้อความสำคัญคือ *หลีกเลี่ยง service failure ที่บ่อยหรือรุนแรงเกินกว่าจะยอมรับได้* โดยตัดสินบนสองแกนคือ **frequency** (ความถี่) และ **severity** (ความรุนแรง) ซึ่งคือ risk assessment ถ้ารับไม่ได้เรียกว่า **dependability failure** และสไลด์เชื่อมกับ **development process failure**

## สามกลุ่ม: attributes, means, threats

- **attributes** — คุณสมบัติที่เราคาดหวัง
- **means** — วิธีสร้างคุณสมบัติเหล่านั้น
- **threats** (impairments) — สาเหตุหรือผลของความไม่ dependable

## คุณสมบัติพื้นฐาน

**property-based attributes หกข้อ:** Availability (ความพร้อมใช้งาน), Reliability (ความต่อเนื่องของการให้บริการ), Safety (การไม่เกิดผลร้ายแรงต่อสภาพแวดล้อม), Confidentiality (ไม่เปิดเผยข้อมูลโดยไม่ได้รับอนุญาต), Integrity (ไม่แก้ไขข้อมูลอย่างไม่เหมาะสม), Maintainability (สามารถซ่อมและพัฒนาได้) หมายเหตุสำคัญ: **security = availability และ integrity เทียบกับการกระทำที่ได้รับอนุญาต + confidentiality**

**event-based attributes สามข้อ:** Robustness (คงอยู่เมื่อเจอ external fault), Survivability (คงอยู่เมื่อมี active fault), Resilience (คงอยู่เมื่อเจอการเปลี่ยนแปลง functional/environmental/technological) — ระบบ resilient มีสี่ลักษณะคือ Latitude, Resistance, Precariousness, Panarchy

**meta-information attributes สามข้อ:** Accountability (ตัวตนของผู้กระทำการ), Authenticity (เนื้อหาและต้นกำเนิดของข้อความ), Non-repudiability (ตัวตนของผู้ส่ง/รับ)

## Availability, Reliability, Safety

**Availability** = MTTF หารด้วย (MTTF + MTTR) ตัวอย่าง MTTF 81.5 ปี (713,940 ชม.) MTTR 1 ชม. → 99.999859% แต่ละ "nine" คือลด downtime สิบเท่า (99.99% = downtime ~50 นาที/ปี, 99.999% = ~5 นาที/ปี)

**Reliability** = ความสามารถทำหน้าที่ภายใต้เงื่อนไขที่ระบุ จนถึงเวลาที่ระบุ และ R(t) = e^(−λt), MTTF = 1/λ

ตัวอย่างที่ต้องจำ: ระบบที่พังชั่วโมงละครั้งแต่ restart ใน 10 ms = **non-reliable แต่ highly available**; ระบบที่ปิดสวิตช์ = **ไม่ reliable ไม่ available แต่ safe**

**Safety** = การไม่เกิดผลร้ายแรงต่อสภาพแวดล้อม ตัวชี้วัดคือ LTIFR (การบาดเจ็บที่เสียเวลางาน หาร ชั่วโมงทำงาน)

## Confidentiality, Integrity, และอื่น ๆ

**confidentiality เกี่ยวกับข้อมูล, privacy เกี่ยวกับบุคคล** integrity แบ่งเป็น physical (redundant hardware, UPS, RAID, ECC, hash, watchdog timer) และ logical (file permission, access control, version control, referential integrity; เสี่ยงจาก software bug/design flaw/human error) **data quality** = ข้อมูลมีประโยชน์ไหม (completeness, uniqueness, validity, timeliness, accuracy, consistency); **data integrity** = ข้อมูลน่าเชื่อถือไหม

**RAM/RMA** = Reliability + Availability + Maintainability ส่งผลต่อ life-cycle cost **การบำรุงรักษาสี่แบบ:** breakdown (ซ่อมหลังเสีย), time-based preventive (เป็นรอบ), condition-based preventive (ตามเงื่อนไข), predictive (ทำนายอายุ)

## Means — จัดการ fault สี่วิธี

**Fault prevention** (ป้องกันไม่ให้ fault เกิด), **Fault tolerance** (ให้บริการได้แม้มี fault), **Fault removal** (ลดจำนวน fault), **Fault forecasting** (ประมาณจำนวน/ผลกระทบ) ตัวอย่างภารกิจอวกาศทำให้เห็นภาพทั้งสี่

ใต้ fault tolerance: **error detection** มี concurrent (watchdog timer, assertion, process pair) และ preemptive (spare checking, memory scrubbing, rejuvenation) **error recovery** มี rollback (คืน state ก่อน error, เหมาะกับ transient), rollforward (แก้แล้วเดินหน้า), compensation (ใช้ redundancy บัง error) **fault avoidance** (ความหมายแคบ) มีสี่ขั้น: diagnosis, isolation, reconfiguration, reinitialisation

**Coverage** = ความน่าจะเป็นที่เทคนิคจะตรวจจับ/แก้ fault เมื่อเกิด fault ทุกเทคนิคมี coverage และ fault model *ไม่มี perfect fault tolerance* coverage ลดได้จาก defect ในการ implement ("who will check the checker?"), common-mode failure, สมมติฐานถูกฝ่าฝืน

## Threats — fault, error, failure

- **Fault** = สาเหตุที่สันนิษฐานว่าเป็นต้นเหตุของ error
- **Error** = ส่วนของ state ที่อาจนำไปสู่ failure
- **Failure** = บริการที่ส่งมอบเบี่ยงเบนไปจากบริการที่ถูกต้อง

สองจุดสำคัญ: **ไม่ใช่ทุก fault→error** (fault ถูก mask ได้ หรือแก้ก่อนกลายเป็น error เช่น scrubbing) และ **ไม่ใช่ทุก error→failure** (benign) และ **ระบบที่เชื่อมกัน**: failure ของระบบหนึ่งเป็น fault ของอีกระบบได้ บนแกนเวลามี **Activation Latency** (fault→error) และ **Failure Latency** (error→failure)

**จำแนก fault ตามเวลา:** transient (ครั้งเดียว), intermittent (เป็นจังหวะ), permanent (ต่อเนื่อง) **ตาม origin:** physical, human-made

**จำแนก failure ตาม:** nature (halt/fail-stop vs erratic/babbling), detection (signalled vs unsignalled/fail-silent), consistency, severity **จำแนก error ตาม:** domain (timing vs content), detection (detected vs latent), consistency, severity — สังเกตว่า failure เริ่มด้วย **nature** แต่ error เริ่มด้วย **domain**

## ขีดจำกัดและความท้าทาย

ขีดจำกัดตาม fault class: physical, design/development, interaction; **software reliability** เป็นคอขวดปัจจุบัน ความท้าทายสองข้อ: ลดต้นทุนความล้มเหลว และขยาย fault tolerance จาก product ไป production process เหตุการณ์ 2025 (Google/AWS/Azure/Cloudflare) สอนว่า configuration ผิดเดียวเอาชนะ redundancy ได้ → ต้องมี staged rollout, canary, feature flag, regional isolation, automated rollback

## จุดเชื่อมกับข้อสอบเก่า

- **Liveness/Safety ในมุม FTC** (ตีความ): safety = "ไม่มีอะไรแย่" ตรงกับ safety attribute; liveness = "มีสิ่งดีเกิดในที่สุด" ตรงกับ reliability/availability
- **Threat ของ net banking:** hacker/human error = fault → error (ข้อมูลผิด/รั่ว) → failure; โยง attribute (integrity, confidentiality, availability, reliability) และการป้องกัน (error control, self-checking, fault masking, fail-safe, data security)
- **MTTF < เวลารัน แก้ด้วยอะไรที่ไม่ใช่เพิ่ม reliability:** เปลี่ยนสถาปัตยกรรม → redundancy, fault tolerance (checkpointing/rollback), ลด MTTR ให้ availability สูงขึ้น
- **Fail-Safe / Self-Checking / Recovery วางตรงไหน** บนแผนภาพ Design Techniques: Fault Avoidance ก่อน fault → Fault Masking ระหว่าง fault-กับ-error → Fault Tolerance ระหว่าง error-กับ-failure; self-checking = โซนต้นของ error, fault masking = ซ่อน error, fail-safe = ตอน failure ให้ผลปลอดภัย, recovery = คืน state

## ต้องจำทันที และกับดัก

**จำทันที:** นิยาม fault/error/failure; means 4; attributes 6+3+3; coverage ไม่มีวันสมบูรณ์; ตัวอย่าง reliability vs availability

**กับดัก:** fault removal (ลด fault) ≠ fault tolerance (ทำงานทั้งที่มี fault); fault avoidance (ตอนออกแบบ) ≠ fault masking (ตอนรัน)

# FTC — บทนำและแผนที่รายวิชา (ฉบับย่อ)

นี่คือสคริปต์ติวฉบับย่อของวิชา Fault Tolerant Computing แต่ละไฟล์อ่านจบได้ใน 5–10 นาที เหมาะสำหรับทวนเร็ว ๆ ก่อนสอบหรือฟังซ้ำตอนเดินทาง ถ้าต้องการรายละเอียดเชิงลึกใช้ชุดเต็มในโฟลเดอร์ `exam_script`

**ตัวสอบ:** on-site 3 ชั่วโมง **open book, open notes, open internet** เนื้อหา "all about Fault Tolerant Computing" คือ FTC01 ถึง FTC07 ส่วน TDC (Testing Digital Circuits) อยู่หลัง midterm จึงไม่ออก

**แหล่งข้อมูล:** สไลด์บรรยาย ใบการบ้าน/แบบฝึกหัด ข้อสอบเก่าที่จดจำมา ภาพสไลด์ที่ถอดด้วย vision และ transcript เสียงบรรยาย จุดที่ผมตีความเกินสไลด์จะระบุไว้

## แผนที่รายวิชา — เรื่องเดียวที่ลึกลงเรื่อย ๆ

ทั้งเจ็ดบทคือเรื่องเดียวกัน โดยมีแกนกลางคือสายพาน **fault → error → failure** และคำถามว่าจะรับมือกับมันอย่างไร

- **FTC01 Dependable Computing** — คำศัพท์และแผนที่: attributes, means, threats
- **FTC02 Fault Tolerant Systems** — ด้านปริมาณ: failure rate, reliability, availability, MTTF/MTTR, series/parallel, redundancy, TMR
- **FTC03 Byzantine Fault Tolerance** — ระบบกระจาย: process group, Byzantine Generals, Oral Message, กฎ n ≥ 3m+1, client-server
- **FTC04 Rollback Recovery** — checkpointing, consistent cut, domino effect, ประเภท message, recovery ตระกูลต่าง ๆ
- **FTC05 Coding Theory** — บทใหญ่สุด: Hamming distance, cyclic code, checksum, residue, Berger, dual rail
- **FTC06 Self-Checking Circuits** — FS, ST, TSC, SFS, checker
- **FTC07 Fault Masking** — logic masking, quadded logic, keystone decomposition, TMR/NMR, fail-safe

**ความเชื่อมโยง:** code เป็นสะพานเชื่อม FTC05 (ออกแบบรหัส), FTC06 (สร้างวงจรล้อมรอบ) และ FTC07 (ใช้ redundancy บังสิ่งที่ตรวจไม่เจอ) ส่วนคณิตศาสตร์ reliability ของ FTC02 กลับมาใน FTC07 และ FTC03/FTC04 คือรูปแบบระบบกระจายของสายพาน fault→failure เดียวกัน

## วิธีใช้

อ่านตามลำดับบท ไฟล์ละ 5–10 นาที แต่ละไฟล์จบด้วย "ต้องจำทันที" และ "กับดัก" ให้ท่องส่วนนั้นก่อน ถ้าสอบแบบเปิดโน้ต สิ่งที่ต้องรู้แบบไม่ต้องคิดคือนิยามและกฎบรรทัดเดียวที่ทำให้จำแนกโจทย์ได้ (เช่น TSC คืออะไร, n ≥ 3m+1, สูตร series/parallel) ส่วนรายการยาวและทฤษฎีบทรองเปิดดูได้

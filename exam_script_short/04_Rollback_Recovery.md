# บทที่ 4 — FTC04 Rollback Recovery (ฉบับย่อ)

## Forward vs Backward recovery

สายพานคือ fault → error → failure; ถ้าแทรกก่อนกลายเป็น failure ได้ก็กู้คืนทัน
**Forward recovery** = รู้ว่าเสียหายแล้วเดินหน้าแก้เลย (TMR เป็นตัวอย่าง) แลกด้วย **ต้นทุน** เพื่อ availability ใช้ได้เฉพาะเมื่อรู้ธรรมชาติของ error ครบ — แทบเป็นไปไม่ได้ (กรณีพิเศษคือ **exception** ที่ประกาศไว้ล่วงหน้า)
**Backward / rollback recovery** = ซ่อมไม่ได้ก็ย้อนกลับ แลกด้วย **performance** เพื่อ availability ข้อเสีย: ทำงานซ้ำ, ไม่รู้ว่า fault เป็น transient หรือ permanent (อาจเกิดซ้ำ), บาง state กู้ไม่ได้ และ **ย้อน irreversible operation ไม่ได้** (พิมพ์กระดาษ, ถอน ATM) **recovery point** = state ที่ใช้แทน error

**เกณฑ์เลือก:** ถ้าไม่แคร์ performance แต่ต้องการความถูกต้องสูง → forward; ถ้าต้องการต้นทุนต่ำ → backward

## Checkpoint, dependency, domino effect

**Checkpoint** = state ที่ถูกบันทึกของ process **message ก่อ dependency:** ถ้า P1 checkpoint แล้วส่ง message ให้ P2 จะย้อน P1 ก่อนส่งไม่ได้ถ้า P2 ไม่ย้อนด้วย → เมื่อบังคับให้ process ที่ไม่ได้พังต้องย้อนด้วยเป็นทอด = **domino effect** (อาจย้อนถึงต้นการคำนวณ) และมี **livelock** ที่การย้อนเกิดซ้ำไม่จบ ทางแก้คือ **checkpoint ต้องไม่มี message ค้างใน transit** = **consistent checkpoint**

## ประเภท message 5 ชนิด

- **In-transit** — ส่งแล้วยังไม่รับ (ปัญหาถ้า protocol รับประกัน delivery)
- **Lost** — ส่งแล้ว แต่การรับถูก undo ด้วย rollback
- **Delayed** — การรับไม่ถูกบันทึก เพราะ process ล่ม หรือมาถึงหลัง rollback
- **Orphan** — การรับบันทึกแต่การส่งไม่ (ไม่เกิดถ้าย้อนไป consistent state)
- **Duplicate** — message ที่รับแล้วถูกส่งซ้ำหลัง recovery

ตัวอย่างจากสไลด์: In-transit = m1,m2; Lost = m1; Delayed = m1,m5; Orphan = none; Duplicated = m4,m5

## Consistent cut และ recovery line

**Global state** = state ของทุก process + channel **Consistent** = state ที่อาจเกิดในการรันที่ไม่ผิดพลาด (ถ้ารับ message ผู้ส่งต้องสะท้อนการส่ง) ตอนวาดเส้นตัด:
- ไม่มี message พาดผ่านเลย = **strongly consistent**
- มี message ค้างใน transit แต่ไม่มี orphan = **consistent** (ไม่ strongly)
- มี **orphan** = **inconsistent** ใช้เป็น recovery line ไม่ได้

**Hint:** recovery line ต้องลากผ่านทุก process และต้องอยู่ใต้ error state

## ตระกูลเทคนิค recovery

**Rollback recovery** → **checkpointing** (uncoordinated / coordinated [blocking, non-blocking] / communication-induced [model-based, index-based]) และ **logging** (pessimistic / optimistic / causal) สามตระกูลที่หลีก domino effect คือ coordinated, communication-induced และ log-based

## Coordinated checkpointing

process ประสาน checkpoint ให้สอดคล้องกันทั้งระบบ มี **initiator**; ต้องการ 1–2 checkpoint ต่อ process, สอดคล้องเสมอ แต่ latency สูง **Algorithm:** block การสื่อสาร → initiator take checkpoint + broadcast request → process หยุด, flush channel, take tentative checkpoint, ส่ง ACK → coordinator ได้ ACK ครบแล้ว broadcast commit → ลบ checkpoint เก่า

**Blocking** = process ค้างจนกิจกรรมเสร็จ (กัน orphan) **Non-blocking** = ทำงานต่อได้ แต่ต้องกันไม่ให้รับ application message ที่ทำให้ checkpoint ไม่สอดคล้อง **กรณี inconsistency:** message m ส่งโดย P0 หลังรับ request แต่ไปถึง P1 ก่อน P1 รับ request → C1,x แสดงการรับ m แต่ C0,x ไม่แสดงการส่ง **วิธีแก้ (channel FIFO):** ให้ message แรกหลัง checkpoint นำหน้าด้วย checkpoint request บังคับให้ take checkpoint ก่อนรับ message นั้น

## Uncoordinated และ communication-induced

**Uncoordinated:** แต่ละ process เลือกเวลาเอง ข้อดี overhead ต่ำ ข้อเสีย domino effect, recovery ช้า, ต้องเก็บหลาย checkpoint, ไม่เหมาะกับ output commit บ่อย
**Communication-induced:** มี autonomous + forced checkpoint; piggyback ข้อมูลไปกับ application message; ผู้รับตัดสินว่าต้อง take forced checkpoint เพื่อดัน global recovery line ไหม (model-based / index-based)

## Log-based rollback recovery

ใช้ความต่าง **deterministic** กับ **non-deterministic event** (การรับ message และ event ภายใน) **การส่ง message ไม่ใช่ non-deterministic event** (กับดักข้อสอบ) สมมติ **piecewise deterministic (PWD)**: event เหล่านี้ระบุได้และ **determinant** ถูก log ลง stable storage; deterministic event replay, non-deterministic simulate จาก log

**Pessimistic logging:** สมมติว่ากันไม่ให้ message ถูกส่ง/รับได้ เป้าหมายคือ **always-no-orphans** นิยาม **Stable(e)**, **Depend(e)**, **Log(e)**; เงื่อนไข **∀e : ¬Stable(e) ⇒ |Depend(e)| = 0** คือ log determinant *ก่อน* ทำ (synchronous logging) → ไม่มี orphan แต่ sync กับ stable storage บ่อย

## Stable storage, GC, output commit

**Stable storage** (ข้อกำหนดเบื้องต้น): ทน failure เดียว → volatile memory ของ process อื่น; ทน transient หลายครั้ง → local disk; ทน non-transient → สื่อ persistent นอก host เช่น replicated file system **Garbage collection** ลบ recovery information ที่ไร้ประโยชน์ (ทิ้งข้อมูลก่อน recovery line ล่าสุด) **Output commit** = state ที่ส่ง message ออกโลกภายนอกได้ กระทบ latency และ overhead

## HW04 และข้อสอบ

โจทย์ให้ไทม์ไลน์ 4 process (P0–P3) ที่ P1 มี error state งานคือหา consistent cut และบอกว่า recovery line เป็น consistent/strongly consistent/inconsistent วิธี: เลือก checkpoint หนึ่งต่อ process, ตรวจ message ทุกอัน (การส่งเหนือเส้นแต่อยู่ใต้เส้นการรับ = orphan → inconsistent; การส่งใต้เส้นแต่รับเหนือ = consistent ไม่ strongly), recovery line ต้องอยู่ใต้ error state

**โจทย์เก่า 1.5 "เวลาเท่ากัน vs ไม่เท่ากัน"** (ตีความ): เท่ากัน = coordinated/synchronous (ทุก process ย้อนไป recovery line เดียวกัน); ไม่เท่ากัน = uncoordinated/asynchronous (ย้อนอิสระ เสี่ยง domino)

## ต้องจำทันที และกับดัก

**จำทันที:** forward vs backward; ย้อน irreversible ไม่ได้; domino/livelock; ประเภท message 5; consistent/strongly/inconsistent; ต้นไม้ recovery

**กับดัก:** การส่ง message ไม่ใช่ non-deterministic event; อย่าสับสน lost/delayed/orphan/duplicate; cut ที่มี message ค้าง = consistent แต่ไม่ strongly (เฉพาะ orphan = inconsistent); TMR = forward, checkpointing = backward

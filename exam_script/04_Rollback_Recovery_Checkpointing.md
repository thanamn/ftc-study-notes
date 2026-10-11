# Part 4 — FTC04 Rollback Recovery (เรียงตามสไลด์)

สคริปต์ส่วนนี้เรียงตามลำดับสไลด์ของบท FTC04 ทุกหัวข้อมี `[สไลด์ N]` กำกับ

## ทบทวน BFT และตารางเสียงข้างมาก [สไลด์ 1–2]

สองสไลด์แรกของบทนี้เป็นการทบทวนแบบฝึกหัด Byzantine ที่เราทำในบทที่สามครับ สไลด์แรกแสดงรอบ OM ของสอง ที่ commander ส่ง A ให้ lieutenant ทั้งเจ็ดรวมกบฏสองตัว จากนั้นรอบ OM ของหนึ่ง ที่ lieutenant ทุกคนแสดงบทเป็น commander และรอบ OM ของศูนย์ ที่ทุกคนส่งต่อข้อความ

สไลด์ที่สองเป็นตารางผลลัพธ์สุดท้าย ซึ่งควรทำความเข้าใจให้ครบ เพราะมันแสดงคอลัมน์ Value from C และคอลัมน์จาก lieutenant แต่ละคน L1 ถึง L5 รวมถึงจาก traitor T1 และ T2 แล้วตามด้วยคอลัมน์ Majority Vote ผลคือ lieutenant ซื่อสัตย์ L1 ถึง L5 ทุกแถวได้เสียงข้างมากเป็น A ส่วน T1 และ T2 ทุกช่องเป็น X เพราะกบฏส่งอะไรก็ได้ ตารางนี้คือคำตอบมาตรฐานของโจทย์ Byzantine ขนาดเจ็ด node ที่กบฏสองตัว

## ภาพรวมการกู้คืนและชนิดของความล้มเหลว [สไลด์ 3–6]

สไลด์ที่ห้าเป็นแผนภาพที่วางสายพาน fault นำไปสู่ erroneous state และ erroneous state นำไปสู่ failure และมีเส้นทาง Recovery ที่พา erroneous state กลับไปสู่ valid state สไลด์นี้ยังจำแนก failure สี่ชนิดที่ต้องรู้ครับ Process failure เช่น deadlock, การละเมิดการป้องกันหน่วยความจำ หรือข้อมูลนำเข้าที่ผิด, System failure เช่นการสูญเสียความจำทั้งหมดหรือบางส่วน, Secondary storage failure ที่เข้าถึงข้อมูลไม่ได้ และ Communication failure ที่เครือข่ายเข้าถึงไม่ได้

สไลด์ที่หกนิยามว่า recovery คือการนำ process ที่ล่มกลับมาให้สอดคล้องกับ process อื่น โดยเริ่มจาก restart process, reclaim ทรัพยากร และ undo หรือ finish ทรานแซกชันที่ไม่สมบูรณ์ สไลด์ย้ำว่าระบบกระจายและ concurrency ทำให้เรื่องนี้ยากขึ้น และบอกว่าเราจะสนใจแบบจำลอง message-passing เป็นหลัก

## Forward กับ Backward Recovery [สไลด์ 7–11]

สไลด์ที่เจ็ดแบ่งการกู้คืนเป็นสองทิศ ทางแรก Forward recovery ซึ่งประเมินความเสียหาย ลบ error แล้วให้ process เดินหน้าต่อ โดย TMR เป็นตัวอย่างหนึ่งของ forward recovery และมันแลกด้วยต้นทุนเพื่อให้ได้ availability ทางที่สอง Backward หรือ rollback recovery ซึ่งแบ่งเป็น operation-based ที่ใช้ do, undo และ redo log กับ state-based ที่ใช้ checkpointing และ logging และมันแลกด้วย performance เพื่อให้ได้ availability

สไลด์ที่แปดเป็นแผนภาพสามเหลี่ยม trade-off ที่น่าสนใจครับ มุมหนึ่งคือ High Availability อีกมุมคือ Low Cost และอีกมุมคือ High Performance ตรงกลางคือ Servers and PCs และด้านซ้ายคือ Backward Error Recovery ของระบบแบบ Tandem NonStop ส่วนด้านขวาคือ Forward Error Recovery ของ IBM mainframes ประเด็นคือไม่มีระบบใดได้ครบทั้งสามมุม ต้องเลือกว่าจะแลกอะไรกับอะไร

สไลด์ที่เก้าถึงสิบเอ็ดลงรายละเอียด ว่า forward recovery ต้องการให้เรารู้ธรรมชาติของ error อย่างสมบูรณ์จึงจะลบมันได้ ซึ่งแทบเป็นไปไม่ได้ และมีกรณีพิเศษคือ exception ที่นิยามไว้ล่วงหน้าหรือประกาศโดยโปรแกรมเมอร์ ในทางกลับกัน backward recovery คืน state ก่อนหน้าโดยไม่ต้องรู้สาเหตุ แต่มีข้อเสียคือ performance penalty ไม่รับประกันว่าจะไม่เกิดซ้ำ บาง state กู้ไม่ได้ และย้ำว่าใช้กับ irreversible operation อย่างการพิมพ์หรือถอน ATM ไม่ได้

## หลักการของ rollback recovery [สไลด์ 12–21]

สไลด์ที่สิบสองนิยาม checkpoint ว่าเป็น state ที่ถูกบันทึก และอธิบายว่า rollback recovery ทำให้ระบบกลับสู่ consistent state โดยบันทึก state เป็นระยะ และเพราะ message ทำให้เกิด dependency ระหว่าง process การย้อนตัวหนึ่งจึงลากให้ตัวอื่นย้อนด้วย ปรากฏการณ์นี้คือ domino effect

สไลด์ที่สิบสามจำแนกเทคนิค state-based เป็น uncoordinated, coordinated ซึ่งมี blocking และ non-blocking, และ communication-induced ซึ่งมี model-based และ index-based ส่วน log-based มี pessimistic, optimistic และ causal สไลด์ที่สิบสี่นิยาม checkpointing ว่าเป็นการบันทึกและกู้คืน state ของระบบ สไลด์ที่สิบห้ายกตัวอย่างปัญหาสามข้อคือ consistency ที่ P1 checkpoint แล้วส่ง message ให้ P2 จะย้อน P1 ไม่ได้ถ้า P2 ไม่ย้อนด้วย, ความแพงที่เราไม่อยาก checkpoint บ่อยเกินหรือย้อนไกลเกิน และการสื่อสารกับโลกภายนอกที่ย้อนไม่ได้

สไลด์ที่สิบหกเป็นแบบจำลองระบบพื้นฐานครับ มี outside world อยู่ด้านบนและ message-passing system อยู่ด้านล่าง process แต่ละตัวมีเส้นเวลา และมี input message จาก outside world เข้ามาและ output message ออกไป โดย basic approach มีสองแบบคือ Checkpointing ที่คัดลอกและกู้คืน state กับ Logging ที่บันทึกและเล่นซ้ำ message สไลด์ที่สิบเจ็ดอธิบาย stable storage ว่าเป็นข้อกำหนดเบื้องต้น และขึ้นกับระดับความทนทานที่ต้องการ

สไลด์ที่สิบแปดถึงยี่สิบให้หลักการของ recovery สามสไลด์ครับ สไลด์ที่สิบแปดคือการ checkpoint โดยให้ process ทั้งหมดเริ่มใหม่จาก consistent cut สไลด์ที่สิบเก้าคือการ message logging ที่มีเพียงหนึ่งหรือไม่กี่ process เท่านั้นที่กู้คืนโดยใช้ข้อมูล message ในการ replay จนถึงจุดที่พัง และสไลด์ที่ยี่สิบนิยามว่า recoverable state คือ state ที่มีข้อมูลเพียงพอที่จะ replay การทำงานจนถึง coherent cut ใกล้กับจุดที่พัง และเพียงพอที่ reconstruct state ที่อาจเกิดขึ้นในการทำงานที่ไม่พังได้ และนี่คือแนวคิดของ strongly consistent cut

สไลด์ที่ยี่สิบเอ็ดแสดงการนำไปใช้สองแบบคือวาง rollback recovery ไว้บน reliable protocol หรือวางลงบน unreliable channel โดยตรง ซึ่งมีผลต่อการจัดการข้อความที่ตกค้าง

## Garbage collection และประเภทของ message [สไลด์ 22–29]

สไลด์ที่ยี่สิบสองอธิบาย garbage collection ว่าคือการลบ checkpoint และ log ที่ไม่มีประโยชน์แล้ว โดยระบุ recovery line ล่าสุดแล้วทิ้งข้อมูลก่อนหน้านั้น สไลด์ที่ยี่สิบสามให้คำนิยามของ message ทั้งห้าชนิด In-transit คือส่งแล้วยังไม่รับ, Lost คือส่งแล้วแต่การรับถูก undo, Delayed คือการรับไม่ถูกบันทึกเพราะ process ล่มหรือมาถึงหลัง rollback, Orphan คือรับบันทึกแต่ส่งไม่บันทึก และ Duplicate คือถูกส่งซ้ำหลัง recovery

สไลด์ที่ยี่สิบสี่ถึงยี่สิบแปดแสดงแต่ละชนิดด้วยแผนภาพ space-time ตัวอย่างสไลด์ที่ยี่สิบห้าแสดง lost message ที่ m1 จาก P2 ไปไม่ถึง P1 เพราะ P1 พัง แล้ว P1 ย้อนไป C2 เพื่อกู้คืน สไลด์ที่ยี่สิบหกแสดง delayed message ที่ m1 และ m5 มาถึงช้าเกินไป สไลด์ที่ยี่สิบเจ็ดแสดง orphan message พร้อมคำแนะนำว่าหลีกเลี่ยงได้โดยไม่ใช้ inconsistent cut (สำหรับ checkpointing) หรือไม่ส่ง message ซ้ำแล้ว replay (สำหรับ message logging) และสไลด์ที่ยี่สิบแปดแสดง duplicate message

สไลด์ที่ยี่สิบเก้าเป็นแบบฝึกหัดที่ให้จำแนก message ในแผนภาพครับ เฉลยคือ In-transit ได้แก่ m1 กับ m2, Lost ได้แก่ m1, Delayed ได้แก่ m1 กับ m5, Orphan ไม่มี และ Duplicated ได้แก่ m4 กับ m5 นี่เป็นแบบฝึกหัดที่ดีเพราะมันรวมทุกชนิดไว้ในภาพเดียว และข้อสอบอาจให้เราจำแนกแบบนี้

## Consistent cut และ domino effect [สไลด์ 30–34]

สไลด์ที่สามสิบนิยาม global state และ consistent global state ว่า state ที่มีการรับ message แล้วการส่งต้องสะท้อนด้วย สไลด์ที่สามสิบเอ็ดเป็นแผนภาพที่มี cut สามแบบ ซึ่งควรจำให้แน่นครับ เส้นตัดซ้ายมือเป็น inconsistent state เพราะมี orphan message เส้นตัดตรงกลางเป็น strongly consistent state เพราะไม่มี message ค้างเลย และเส้นตัดขวามือเป็น consistent state แต่มี in-transit message ค้างอยู่ จำสามคำนี้ให้แม่นเพราะข้อสอบชอบให้เราจำแนก

สไลด์ที่สามสิบสองลงรายละเอียด domino effect ด้วย process X, Y, Z ครับ ถ้า Y ย้อนไป y2 แล้ว message m เป็น orphan ก็บังคับให้ X ต้องย้อนไป x2 และถ้า Z ย้อนไป z2 ก็ทำให้ Y ย้อนไป y1 และบังคับให้ X กับ Z ย้อนไป x1 และ z1 ในที่สุด นี่คือ cascaded rollback ที่อาจย้อนถึงต้นการคำนวณ

สไลด์ที่สามสิบสามอธิบาย livelock ที่เกิดขึ้นซ้ำไม่จบ โดยเริ่มจาก Y crash ก่อนรับ n1 แล้วย้อนไป y1 บังคับให้ X ย้อนไป x1 จากนั้น Y ฟื้น รับ n1 แล้วส่ง m2 และ X ฟื้นส่ง n2 แต่ไม่มีบันทึกว่าเคยส่ง n1 Y จึงถูกบังคับให้ย้อนครั้งที่สอง และ X ก็ย้อนด้วยเพราะรับ m2 แล้วแต่ Y ไม่มีบันทึก m2 วงจรนี้เกิดซ้ำได้ไม่จบ สไลด์ที่สามสิบสี่บทเรียนคือ ทางแก้คือ checkpoint ต้องไม่มี message ค้างใน transit และยกตัวอย่างว่า {x1, y1, z1} เป็น strongly consistent checkpoint

## ตระกูลเทคนิคและ coordinated checkpointing [สไลด์ 35–43]

สไลด์ที่สามสิบห้าเป็นแผนภาพต้นไม้ที่ควรจำครับ Rollback-Recovery แยกเป็น checkpointing ที่มี uncoordinated, coordinated ซึ่งมี blocking และ non-blocking, และ communication-induced ซึ่งมี model-based และ index-based กับ logging ที่มี pessimistic, optimistic และ causal สไลด์ที่สามสิบหกบอกว่าสามตระกูลที่หลีกเลี่ยง domino effect ได้คือ coordinated, communication-induced และ log-based

สไลด์ที่สามสิบเจ็ดอธิบาย coordinated และ blocking ว่าไม่มี message ใดค้างใน transit ระหว่าง checkpoint และ {x1, y1, z1} ก่อตัวเป็น recovery line สไลด์ที่สามสิบแปดเปรียบเทียบ blocking ที่ process ถูกบล็อกจนเสร็จกับ non-blocking ที่ทำงานต่อได้ แต่ต้องกันไม่ให้รับ application message ที่ทำให้ checkpoint ไม่สอดคล้อง

สไลด์ที่สามสิบเก้าถึงสี่สิบเอ็ดให้ขั้นตอนวิธีครับ มี initiator process ที่ broadcast checkpoint request ให้ทุก process แต่ละ process หยุด flush channel แล้ว take tentative checkpoint แล้วส่ง acknowledgement และเมื่อ coordinator ได้ acknowledgement ครบก็ broadcast commit แล้วแต่ละ process ลบ checkpoint เก่า สไลด์ที่สี่สิบเอ็ดแสดง execution graph ที่มี checkpoint requests และ acknowledgments

สไลด์ที่สี่สิบสองและสี่สิบสามเป็นกรณี inconsistency ที่สำคัญ ถ้า message m ถูกส่งโดย P0 หลังรับ checkpoint request แต่ไปถึง P1 ก่อน P1 รับ checkpoint request แล้ว checkpoint C1,x แสดงการรับ m แต่ C0,x ไม่แสดงการส่ง m จะเกิด orphan วิธีแก้เมื่อ channel เป็น FIFO คือให้ message แรกหลัง checkpoint นำหน้าด้วย checkpoint request บังคับให้ P1 take checkpoint ก่อนรับ message นั้น

## Uncoordinated, communication-induced และ log-based [สไลด์ 44–50]

สไลด์ที่สี่สิบสี่อธิบาย uncoordinated ที่แต่ละ process เลือกเวลาเอง ข้อดี overhead ต่ำ ข้อเสีย domino effect, recovery ช้า, ต้องเก็บหลาย checkpoint และไม่เหมาะกับ output commit บ่อย สไลด์ที่สี่สิบห้าอธิบาย communication-induced ที่มี autonomous และ forced checkpoint โดย piggyback ข้อมูลไปกับ application message เพื่อดัน global recovery line

สไลด์ที่สี่สิบหกอธิบาย log-based ที่ใช้ความต่างของ deterministic และ non-deterministic event โดยย้ำว่าการส่ง message ไม่ใช่ non-deterministic event เราบันทึก determinant ของ non-deterministic event ลง stable storage สไลด์ที่สี่สิบเจ็ดอธิบาย pessimistic logging ที่สมมติว่าป้องกันไม่ให้ message ถูกส่งหรือรับได้ และมี always-no-orphans condition โดยใช้เซต Stable, Depend และ Log

สไลด์ที่สี่สิบเก้าให้เงื่อนไขที่แม่นยำของ synchronous logging ซึ่งเขียนได้ว่า สำหรับทุก event e ถ้า e ยังไม่ stable แล้วขนาดของ Depend ของ e ต้องเท่ากับศูนย์ นั่นคือก่อนที่ event จะถูกบันทึกลง stable storage อย่างสมบูรณ์ ต้องไม่มี process ใดได้รับผลจากมัน สไลด์ยังบอกว่า orphan process ไม่เคยเกิด แต่ต้อง sync กับ stable storage บ่อย และมีข้อสังเกตว่ามีเพียงหนึ่ง process ที่ restart ส่วน message ที่ส่งซ้ำระหว่าง recovery อาจต้องถูกยกเลิก สไลด์ที่ห้าสิบปิดด้วยประเด็นอื่น ๆ ได้แก่ output commit, stable storage และ garbage collection

## การบ้าน HW04 [สไลด์ 51]

สไลด์สุดท้ายให้โจทย์ที่มีไทม์ไลน์สี่ process P0 ถึง P3 โดย P1 มี error state อยู่ด้านขวาสุด งานคือหา consistent cut และตอบว่า recovery line ที่ได้เป็น consistent, strongly consistent หรือ inconsistent วิธีทำคือเลือก checkpoint หนึ่งอันต่อ process แล้วตรวจ message ทุกอัน ถ้าการส่งอยู่เหนือเส้นแต่การรับอยู่ใต้เส้นก็เกิด orphan และ cut นั้น inconsistent ถ้าการส่งอยู่ใต้เส้นแต่การรับอยู่เหนือเส้นก็มี message ค้าง ซึ่งเป็น consistent แต่ไม่ strongly และถ้าไม่มี message ค้างเลยก็เป็น strongly consistent และ recovery line ต้องอยู่ใต้ error state บน P1 เสมอ


## จากคำบรรยายในห้อง [insights]

**เกณฑ์เลือกระหว่าง forward กับ backward recovery** อาจารย์ให้เกณฑ์ที่ใช้ตัดสินได้จริงคือ ถ้าระบบ **ไม่แคร์ performance แต่ต้องการความถูกต้องสูง** ให้เน้น forward recovery (เกิด error ก็ข้ามไปเลย) แต่ถ้าระบบ **ต้องการต้นทุนต่ำ** ให้เน้น backward หรือ rollback เพราะ forward ต้องลงทุนสูงกว่ามาก นี่เป็นกรอบที่ช่วยตอบคำถาม "ควรเลือกวิธีไหน" ได้ดีกว่าการท่องนิยาม

**ทำไม rollback ถึงซับซ้อน** อาจารย์ขยายว่าเรามักซ่อม fault ไม่ได้ จึงต้องย้อนกลับไปยังจุดที่กำหนด แต่พอย้อนแล้วเดินต่อเราจะเจอปัญหาสองอย่าง คือต้องทำงานซ้ำ (performance penalty) และที่สำคัญคือ **เราไม่รู้ว่า fault ที่เพิ่งเกิดเป็น transient หรือ permanent** ดังนั้นมันอาจเกิดซ้ำอีกได้ ซึ่งเป็นเหตุผลที่เราต้องมี checkpoint ที่ดี ไม่ใช่แค่ย้อนกลับ

**checkpoint ถี่แค่ไหน** อาจารย์เน้น trade-off ว่าทำถี่ทุกวินาทีทำได้แต่สิ้นเปลือง และทำห่างเกินไปก็ไม่ต่างจากการเริ่มใหม่หมด จึงต้องเลือกความถี่ให้เหมาะ และย้ำว่า rollback recovery มีความซับซ้อน "ขึ้นอยู่กับ message" เพราะบาง message มีลำดับหรือ ordering ติดมาด้วย

**ความหมายของ consistency** จุดที่อาจารย์ย้ำคือ ข้อความต้องรู้ชัดว่า **ใครเป็นผู้ส่งและใครเป็นผู้รับ** ถ้าไม่รู้ แล้วย้อนกลับมา จะไม่รู้ว่า message นั้นใครเป็นเจ้าของ การกู้คืนก็จะทำไม่ได้ นี่คือรากของปัญหา orphan message

**การหุ่น recovery line** อาจารย์ให้ hint ที่ตรงไปตรงมาว่า "เวลาลาก recovery line ต้องลากผ่านทุก process" และเกณฑ์ตัดสินคือถ้ามี **orphan message** ก็เป็น inconsistent ถ้ามีแค่ **in-transit** ก็ยังนับเป็น consistent และถ้าไม่มีทั้งสองอย่างเลยก็เป็น strongly consistent

หมายเหตุ: คาบนี้ถูกตัดจบเร็ว อาจารย์บอกว่าจะอธิบาย coordinated/uncoordinated และ pessimistic logging เพิ่มเติมภายหลัง [ไม่แน่ใจ: รายละเอียดบางส่วนอาจยังไม่ครบในคลาส]

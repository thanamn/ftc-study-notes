# Part 1 — FTC01 Dependable Computing (เรียงตามสไลด์)

สคริปต์ส่วนนี้เรียงตามลำดับสไลด์ของบท FTC01 เพื่อให้อ่านควบคู่กับไฟล์ PDF ได้ทันที ทุกหัวข้อจะมีตัวเลข `[สไลด์ N]` กำกับว่ากำลังพูดถึงสไลด์ใบไหน ถ้าต้องการเปิดดูภาพหรือตารางระหว่างฟัง ก็เปิดสไลด์ใบนั้นได้เลย

## บริบทของรายวิชา [สไลด์ 1, 3]

สไลด์แรกเป็น course syllabus ซึ่งบอกภาพรวมของวิชา เนื้อหารายวิชาแบ่งเป็นเจ็ดหัวข้อหลัก ได้แก่ Dependable Computing (terminology), Fault Tolerant Computing (basic concept), Redundancy Technique ซึ่งครอบคลุม hardware, software, information และ time, Error Detection & Error Correction, Modeling & Evaluation ซึ่งรวม fault modeling และ reliability, Testing Digital Circuits และ Design for Test ส่วนการวัดผลคือ Midterm 30 เปอร์เซ็นต์ Final Assignment 20 เปอร์เซ็นต์ และ Homework 50 เปอร์เซ็นต์

สไลด์ที่สามเป็นตาราง Weekly Plan ซึ่งมีประโยชน์ตรงที่มันบอกลำดับบทเรียนและกำหนดสอบ สำหรับการสอบนี้ สิ่งที่ต้องจำคือช่วง FTC01 ถึง FTC07 คือเนื้อหาหลัก และบทที่ชื่อ TDC ย่อมาจาก Testing Digital Circuits นั้นอยู่หลังสอบกลางภาค จึงไม่ออกในครั้งนี้

## ทำไมเราต้องสนใจ Dependability [สไลด์ 4–7]

ในสไลด์เปิดบท อาจารย์เริ่มจากคำถามง่าย ๆ ว่าเราพึ่งพาระบบคอมพิวเตอร์มากแค่ไหน และความพึ่งพานั้นจะรู้สึกชัดที่สุดตอนที่ระบบพัง สไลด์ยกตัวอย่างเหตุการณ์จริงไว้หลายอย่าง เช่นเหตุการณ์โทรศัพท์ล่มในสหรัฐอเมริกาปี 1990 การปฏิเสธการอนุมัติบัตรเครดิตที่ฝรั่งเศสปี 1993 และความล้มเหลวของระบบบริการรถพยาบาลในลอนดอนปี 1992 ประเด็นไม่ใช่วันที่ แต่คือข้อเท็จจริงว่าคอมพิวเตอร์ให้ทั้งประโยชน์และต้นทุน และเราจ่ายต้นทุนในรูปของความเสียหายตอนที่การให้บริการไม่น่าเชื่อถือ

ตรงนี้มีคำนิยามของ Dependability สองเวอร์ชันที่ต้องแยกให้ออกครับ เวอร์ชันคลาสสิกยุคทศวรรษ 1960 บอกสั้น ๆ ว่า Dependability คือความน่าจะเป็นที่ระบบจะทำงานเมื่อถูกเรียกใช้ ซึ่งเน้นความพร้อม ส่วนเวอร์ชันปี 1995 จาก Laprie และ Avizienis ให้คำนิยามว่าเป็น integrative concept คือคุณสมบัติของระบบที่ทำให้การส่งมอบบริการได้รับความไว้วางใจได้อย่างมีเหตุผล โดยคุณสมบัติที่รวมอยู่ในนั้นมีหกข้อคือ availability, reliability, safety, confidentiality, integrity และ maintainability

ในสไลด์เดียวกันยังมีครึ่งหลังของนิยามที่พูดถึงการหลีกเลี่ยง service failure ที่บ่อยเกินไปหรือรุนแรงเกินกว่าจะยอมรับได้ สองคำที่ต้องจำคือ frequency คือความถี่ และ severity คือความรุนแรง มันคือสองแกนที่เราใช้ตัดสินว่าความล้มเหลวยอมรับได้หรือไม่ และการประเมินสองอย่างนี้ก็คือ risk assessment และ risk management ถ้าระดับความถี่หรือความรุนแรงยอมรับไม่ได้ เราเรียกสิ่งนั้นว่า dependability failure ซึ่งสไลด์เชื่อมเข้ากับ development process failure พูดง่าย ๆ คือถ้าระบบ dependable ไม่พอ แสดงว่ามีอะไรผิดในกระบวนการพัฒนาตั้งแต่แรก

## การแบ่ง Dependability เป็นสามกลุ่ม [สไลด์ 8–9]

สไลด์ที่แปดบอกว่า Dependability มองได้สามมุม ได้แก่ คุณสมบัติที่คาดหวัง ซึ่งเรียกว่า attributes, วิธีที่ใช้สร้างความสามารถนั้น ซึ่งเรียกว่า means และสาเหตุหรือผลของความไม่ dependable ซึ่งเรียกว่า threats หรือ impairments

สไลด์ที่เก้าเป็นแผนภาพที่ควรจำครับ มันวาดเป็นแผนภาพต้นไม้ที่มีคำว่า Dependability อยู่ซ้ายสุด แล้วแตกออกเป็นสามกิ่ง กิ่งแรกชื่อ ATTRIBUTES มีรายการย่อยคือ AVAILABILITY, RELIABILITY, SAFETY, CONFIDENTIALITY, INTEGRITY และ MAINTAINABILITY กิ่งที่สองชื่อ MEANS มีรายการย่อยคือ FAULT PREVENTION, FAULT TOLERANCE, FAULT REMOVAL และ FAULT FORECASTING และกิ่งที่สามชื่อ IMPAIRMENTS มีรายการย่อยคือ FAULTS, ERRORS และ FAILURES ที่น่าสนใจคือบนสไลด์นี้มีวงรีสีแดงวาดด้วยมือล้อมกรอบกลุ่ม ATTRIBUTES ไว้ แสดงว่าอาจารย์กำลังเน้นว่ากิ่งนี้คือคุณสมบัติที่เราคาดหวัง เดี๋ยวเราจะเห็นสไลด์เดียวกันนี้อีกสองครั้งที่ไฮไลต์คนละกิ่ง ซึ่งเป็นเบาะแสได้ดีว่าอะไรถูกเน้น

## คุณสมบัติพื้นฐานหกข้อ [สไลด์ 10–11]

มาถึงรายละเอียดของ attributes ครับ สไลด์แยกมันเป็นสามกลุ่มย่อย กลุ่ม property-based มีหกข้อที่เรากล่าวไปแล้ว กลุ่ม event-based มีสามข้อคือ robustness, survivability และ resilience และกลุ่ม meta-information มีสามข้อคือ accountability, authenticity และ non-repudiability เดี๋ยวเราจะกลับมาที่สองกลุ่มหลัง

สำหรับหกข้อแรก ขออธิบายทีละข้อให้เห็นภาพ Availability คือความพร้อมสำหรับการใช้งาน คือคำตอบของคำถามว่า ถ้าเราเข้าไปใช้ระบบตอนนี้มันพร้อมไหม Reliability คือความต่อเนื่องของการให้บริการ คือคำถามว่าระบบให้บริการได้ต่อเนื่องนานแค่ไหนโดยไม่พัง Safety คือการไม่เกิดผลลัพธ์ร้ายแรงต่อสภาพแวดล้อม สังเกตว่า safety พูดถึงผลที่เกิดกับโลกรอบตัวระบบ ไม่ใช่แค่ตัวระบบ Confidentiality คือการไม่เปิดเผยข้อมูลโดยไม่ได้รับอนุญาต Integrity คือการไม่แก้ไขข้อมูลอย่างไม่เหมาะสม และ Maintainability คือความสามารถในการซ่อมบำรุงและพัฒนาเปลี่ยนแปลง

มีหมายเหตุสำคัญบนสไลด์ครับว่า security นั้นนิยามว่าเป็น availability และ integrity เมื่อเทียบกับการกระทำที่ได้รับอนุญาต ประกอบกับ confidentiality พูดอีกแบบคือ security ไม่ใช่เรื่องแยกออกไปต่างหาก แต่คือการอ่าน availability, integrity และ confidentiality ในมุมที่เราสนใจว่าใครมีสิทธิ์ทำอะไร

## ตัวอย่าง attribute ตามชนิดของระบบ [สไลด์ 12]

สไลด์ที่สิบสองเป็นตารางที่ทำให้เห็นว่า attributes ต่างกันไปตามชนิดของระบบ ตารางนี้มีหกแถว หัวคอลัมน์คือชนิดของระบบกับหก attribute โดยใช้เครื่องหมาย X แทนว่าคุณสมบัตินั้นสำคัญต่อระบบชนิดนั้น แอร์คราฟต์มีทั้งหกอย่างพร้อมกันรวมทั้ง maintainability ส่วน nuclear reactor กับ Internet news page และ pace maker มีเพียงสี่อย่าง และน่าสนใจว่า smart phone และ automobile system ก็มีสี่อย่างเช่นกัน ตารางนี้ไม่ได้มีสูตรอะไร แต่มีประโยชน์ตรงที่มันย้ำว่าการเลือก attributes ที่จะออกแบบให้สำคัญนั้นขึ้นกับบริบทของระบบ ไม่ใช่ทุกอย่างสำคัญเท่ากันหมด

## วิวัฒนาการทางประวัติศาสตร์ [สไลด์ 13]

สไลด์ที่สิบสามน่าสนใจมากครับ มันเล่าว่าความต้องการคุณสมบัติต่าง ๆ เพิ่มขึ้นตามยุคสมัย เริ่มจากยุคทศวรรษ 1940 กับเครื่อง ENIAC ซึ่งมีหลอดสุญญากาศประมาณ 18,000 หลอด และเกิดความล้มเหลวบ่อยถึงประมาณทุกเจ็ดนาที ในขณะที่มันคูณเลขได้ 18,000 ครั้งต่อนาที ดังนั้นเจ็ดนาทีก็ประมาณการรันโปรแกรมหนึ่งครั้งพอดี ด้วยเหตุนี้เขาจึงต้องการ RELIABILITY ต่อมาในยุคทศวรรษ 1960 กับระบบ interactive เขาเพิ่ม AVAILABILITY ในยุคทศวรรษ 1970 กับเครื่องบิน F-8 Crusader, MD-11 และระบบป้องกัน Patriot เขาเพิ่ม SAFETY และตั้งแต่ทศวรรษ 1990 จนถึงวันนี้ กับ Internet, e-commerce และ web service เขาเพิ่ม SECURITY ข้อคิดคือคุณสมบัติแต่ละอย่างเข้ามาเป็นความต้องการตามช่วงเวลาที่เทคโนโลยีและสังคมเปลี่ยนไป

## Dependability กับ Security [สไลด์ 14]

สไลด์ที่สิบสี่เป็นแผนภาพเวนน์ที่ช่วยให้เห็นความสัมพันธ์ระหว่าง security กับ dependability อย่างชัดเจนครับ วงรีซ้ายชื่อ Security วงรีขวาชื่อ Dependability และส่วนที่ทับซ้อนตรงกลางแสดงถึงคุณสมบัติร่วม ในแผนภาพนี้ Confidentiality อยู่ฝั่ง Security, Maintainability และ Safety อยู่ฝั่ง Dependability และ Availability, Integrity กับ Reliability อยู่ตรงกลางที่ทับซ้อนกัน นี่คือภาพที่ทำให้เราเข้าใจว่าทำไมคำนิยามถึงบอกว่า security คือ availability และ integrity บวก confidentiality นั่นเอง

## Availability และจำนวนเก้า [สไลด์ 15–17]

ทีนี้มาถึง availability แบบเป็นตัวเลขครับ สไลด์นิยามว่า availability คืออัตราส่วนของค่าคาดหมายของเวลาที่ระบบทำงานได้ ต่อผลรวมของค่าคาดหมายของเวลาที่ทำงานได้กับเวลาที่ทำงานไม่ได้ สไลด์ยกตัวอย่างที่ทำเลขให้ดูว่า ถ้าอุปกรณ์มี MTTF เท่ากับ 81.5 ปี และ MTTR เท่ากับหนึ่งชั่วโมง เราแปลง MTTF เป็นชั่วโมงได้ 713,940 ชั่วโมง แล้ว availability เท่ากับ 713,940 หารด้วย 713,941 ซึ่งประมาณ 99.999859 เปอร์เซ็นต์ และ unavailability ประมาณ 0.000141 เปอร์เซ็นต์

สไลด์ที่สิบเจ็ดเป็นตาราง nines of availability ที่ควรจำ เพราะมันทำให้เห็นภาพว่าแต่ละเก้าหมายถึง downtime ปีละเท่าไร ในตารางมีสองเก้าคือ 99 เปอร์เซ็นต์ ซึ่ง downtime ประมาณ 5,000 นาทีต่อปี เหมาะกับ general web site, สามเก้าคือ 99.9 เปอร์เซ็นต์ ประมาณ 500 นาที เหมาะกับ Amazon, สี่เก้าคือ 99.99 เปอร์เซ็นต์ ประมาณ 50 นาที เหมาะกับ enterprise server, ห้าเก้าคือ 99.999 เปอร์เซ็นต์ ประมาณ 5 นาที ใช้กับระบบโทรศัพท์, และหกเก้าคือ 99.9999 เปอร์เซ็นต์ ประมาณ 30 วินาที ใช้กับ phone switch ตัวเลขเหล่านี้ช่วยให้เราเห็นว่าทำไมการทำ availability ให้สูงขึ้นแต่ละเก้าจึงยากขึ้นมาก

## Reliability และความต่างจาก Availability [สไลด์ 18–19]

สไลด์ที่สิบแปดให้นิยาม reliability ว่าเป็นความสามารถของชิ้นส่วนในการทำหน้าที่ที่กำหนด ภายใต้เงื่อนไขที่ระบุ จนถึงเวลาที่ระบุ และให้สูตรสำคัญสามสูตรครับ สูตรแรกคือ m เท่ากับหนึ่งส่วน lambda โดย m คือ MTBF หรือ mean time between failures และ lambda คือ failure rate สูตรที่สองคือ R ของ t เท่ากับ e ยกกำลังลบ lambda t ซึ่งเขียนได้อีกแบบว่า e ยกกำลังลบ t ส่วน m สูตรที่สามคือ m เท่ากับ t หารด้วย log ฐาน n ของ (หนึ่งหาร R ของ t) สังเกตว่าสามสูตรนี้เชื่อมกัน เพราะถ้าเรารู้ failure rate เราก็หา MTBF ได้ และถ้าเรารู้ความน่าเชื่อถือที่เวลาหนึ่ง เราก็ย้อนหา MTBF ได้

สไลด์ที่สิบเก้าให้ตัวอย่างที่ทำให้ความต่างระหว่าง reliability กับ availability ชัดเจนมากครับ คือระบบที่พังโดยเฉลี่ยชั่วโมงละครั้ง แต่รีสตาร์ตตัวเองได้ภายในสิบมิลลิวินาที ระบบแบบนี้มี reliability ต่ำเพราะพังบ่อย แต่มี availability สูงเพราะกลับมาเร็ว เราจึงเรียกว่ามัน non-reliable แต่ highly available

## Failure Metrics และ Design Tradeoffs [สไลด์ 20–21]

สไลด์ที่ยี่สิบเป็นแผนภาพแกนเวลาที่อธิบายคำศัพท์เรื่อง failure ให้ครบครับ บนแกนเวลามีจุด System Failure สองจุด คั่นด้วยช่วง Resume Normal Operations ช่วงจาก System Failure จุดแรกถึง Resume Normal Operations เรียกว่า Time to Repair ช่วงจาก Resume Normal Operations ถึง System Failure จุดที่สองเรียกว่า Time to Failure และช่วงรวมตั้งแต่ System Failure จุดแรกถึงจุดที่สองเรียกว่า Time Between Failures หรือ MTBF นี่คือที่มาของคำว่า MTTF คือค่าเฉลี่ยของ time to failure และ MTTR คือค่าเฉลี่ยของ time to repair

สไลด์ที่ยี่สิบเอ็ดต่อด้วย Design Tradeoffs โดยให้สูตร Availability เท่ากับ MTTF หารด้วย MTTF บวก MTTR และตั้งคำถามว่าจะทำให้ availability เข้าใกล้ 100 เปอร์เซ็นต์ได้อย่างไร คำตอบมีสองทางคือทำให้ MTTF เข้าใกล้อนันต์ ซึ่งหมายถึงการเพิ่มความน่าเชื่อถือ หรือทำให้ MTTR เข้าใกล้ศูนย์ ซึ่งหมายถึงการกู้คืนให้เร็ว สไลด์ยังบอกว่าเราจำเป็นต้องนิยาม maximum repair time และนิยามว่าจะวัด availability อย่างไรด้วย

## Safety และ Risk [สไลด์ 22–25]

สไลด์ที่ยี่สิบสองให้ตัวชี้วัดความปลอดภัยคือ LTIFR หรือ lost-time injury and incident frequency rate และสไลด์ที่ยี่สิบสามลงลึกใน safety โดยนิยามว่าคือการไม่มีผลลัพธ์ร้ายแรงต่อผู้ใช้หรือสภาพแวดล้อม แล้วตั้งคำถามกระตุกความคิดว่า เครื่องบินพาณิชย์ปลอดภัยไหม ทั้งที่มันตกเป็นครั้งคราว แล้วถามว่าเท่าไรจึงจะเรียกว่าตกมากเกินไป รถยนต์ปลอดภัยไหม ทั้งที่มันชนกันบ่อย สไลด์ให้ตัวเลขว่าในสหรัฐมีผู้เสียชีวิตประมาณ 40,000 คนต่อปี หรือ 800 คนต่อสัปดาห์ ซึ่งเทียบเท่ากับเครื่องบินโบอิ้ง 747 ที่เต็มลำตกสองลำต่อสัปดาห์

เพื่อให้ safety มีนิยามเชิงปริมาณ สไลด์ที่ยี่สิบสี่จึงนิยาม Risk ว่าเป็นความสูญเสียที่คาดหวังต่อหน่วยเวลา โดย Risk เท่ากับผลรวมของความน่าจะเป็นของอุบัติเหตุแต่ละชนิดคูณกับต้นทุนของอุบัติเหตุนั้น และนิยาม Safety ว่าเป็นระดับความเสี่ยงที่ยอมรับได้ นั่นคือ Risk น้อยกว่า delta ที่กำหนดไว้ล่วงหน้า สองสูตรนี้สำคัญเพราะมันทำให้ safety กลายเป็นเรื่องที่วัดและตัดสินได้ ไม่ใช่แค่ความรู้สึก

สไลด์ที่ยี่สิบห้าเป็นการเปรียบเทียบที่ทำให้ความต่างของสามคุณสมบัติชัดเจนครับ มันยกตัวอย่างระบบที่ถูกปิดสวิตช์อยู่ ระบบแบบนี้ไม่ reliable เพราะให้บริการไม่ได้ ไม่ available เพราะใช้งานไม่ได้ แต่ปลอดภัย เพราะมันก่ออันตรายไม่ได้

## Confidentiality, Integrity และคุณภาพของข้อมูล [สไลด์ 26–29]

สไลด์ที่ยี่สิบหกพูดถึง CIA triad ซึ่งย่อมาจาก Confidentiality, Integrity และ Availability โดยนิยามว่า Confidentiality คือชุดกฎที่จำกัดการเข้าถึงข้อมูล, Integrity คือความมั่นใจว่าข้อมูลน่าเชื่อถือและถูกต้อง และ Availability คือการรับประกันว่าผู้มีสิทธิ์เข้าถึงข้อมูลได้อย่างน่าเชื่อถือ

สไลด์ที่ยี่สิบเจ็ดลงรายละเอียดของ confidentiality โดยมีประโยคสำคัญที่ต้องจำคือ confidentiality นั้นเกี่ยวกับข้อมูล ส่วน privacy นั้นเกี่ยวกับตัวบุคคล และยกตัวอย่างวิธีรักษาความลับ เช่น data encryption, ID และ password, two-factor authentication, biometric verification และ security token

สไลด์ที่ยี่สิบแปดลงรายละเอียดของ integrity โดยแบ่งเป็น physical integrity ซึ่งหนุนด้วย redundant hardware, UPS, RAID, error-correcting code, cryptographic hash function และ watchdog timer กับ logical integrity ซึ่งหนุนด้วย file permission, access control, version control และ referential integrity ในฐานข้อมูล และถูกคุกคามด้วย software bug, design flaw และ human error

สไลด์ที่ยี่สิบเก้าเปรียบเทียบ data quality กับ data integrity ครับ data quality พูดถึงว่าข้อมูลมีประโยชน์ไหม มีหกด้านคือ completeness, uniqueness, validity, timeliness, accuracy และ consistency ส่วน data integrity พูดถึงว่าข้อมูลน่าเชื่อถือไหม โดยแยกเป็น physical integrity ที่เกี่ยวกับการเก็บและเรียกคืนข้อมูล และ logical integrity ที่เกี่ยวกับข้อมูลที่ผิดหรือไม่สมเหตุสมผลในบริบทของมัน

## RAM/RMA และการบำรุงรักษา [สไลด์ 30–31]

สไลด์ที่สามสิบพูดถึง RAM ซึ่งย่อมาจาก Reliability, Availability และ Maintainability บางตำราเขียนเป็น RMA ก็ได้ มันคือคุณสมบัติการออกแบบที่ส่งผลต่อต้นทุนตลอดวงจรชีวิตของระบบ

สไลด์ที่สามสิบเอ็ดแบ่งการบำรุงรักษาเป็นสี่แบบครับ แบบแรก breakdown maintenance คือซ่อมหลังเสีย แบบที่สอง time-based preventive maintenance คือบำรุงรักษาเป็นรอบเวลา แบบที่สาม condition-based preventive maintenance คือบำรุงรักษาเมื่อเงื่อนไขที่กำหนดเกิด และแบบที่สี่ predictive maintenance คือทำนายอายุชิ้นส่วนเพื่อบำรุงรักษาก่อนเสีย

## คุณสมบัติเชิงเหตุการณ์และเชิงข้อมูลกำกับ [สไลด์ 32–35]

สไลด์ที่สามสิบสองให้ event-based attributes สามข้อ Robustness คือความคงอยู่ของ dependability เมื่อเจอความผิดพลาดภายนอก Survivability คือเมื่อมีความผิดพลาดที่ยังทำงานอยู่ และ Resilience คือเมื่อเจอการเปลี่ยนแปลงด้านหน้าที่การทำงาน สภาพแวดล้อม หรือเทคโนโลยี

สไลด์ที่สามสิบสามเปรียบเทียบ robustness กับ stability ว่ามีจุดร่วมคือทั้งคู่ถูกนิยามบนคุณลักษณะและ perturbation ที่ระบุ และเกี่ยวกับความคงอยู่ แต่ robustness ครอบคลุมกว้างกว่าและเลยขอบเขตของ stability ออกไป

สไลด์ที่สามสิบสี่เป็นแผนภาพกราฟที่มีแกนตั้งเป็น System state และแกนนอนเป็น Environment มีเส้นกราฟที่ตกลงมา และมีป้ายชี้ไปยังส่วนต่าง ๆ ของกราฟ ได้แก่ Resistance ซึ่งเป็นการวัดความยากง่ายในการเปลี่ยนระบบ, Latitude ซึ่งเป็นการวัดตามแนวราบว่าระบบเปลี่ยนได้เท่าไรก่อนเสียความสามารถ recover, Precariousness ซึ่งบอกว่าระยะห่างจาก threshold เท่าไร และแผนภาพยังมี Robustness แสดงเป็นระยะแนวตั้งบนกราฟด้วย สไลด์นี้ยังให้คำนิยามของ Panarchy ว่าคือระดับที่ชั้นหนึ่งของระบบนิเวศได้รับอิทธิพลจากชั้นอื่น และย้ำว่าทั้งหมดนี้เชื่อมโยงอย่างใกล้ชิดกับ adaptive capacity

สไลด์ที่สามสิบห้าให้ meta-information attributes สามข้อ Accountability คือ availability และ integrity ของตัวบุคคลที่กระทำการ Authenticity คือ integrity ของเนื้อหาและต้นกำเนิดของข้อความ และ Non-repudiability คือ availability และ integrity ของตัวตนของผู้ส่งหรือผู้รับ

## ภาพรวม Dependability อีกครั้ง และวิธีคิดของ Means [สไลด์ 36–38]

สไลด์ที่สามสิบหกเป็นแผนภาพต้นไม้เดียวกับสไลด์เก้า แต่คราวนี้มีวงรีสีแดงล้อมกรอบกลุ่ม MEANS ไว้ แสดงว่าอาจารย์กำลังเน้นวิธีการ และสไลด์ที่สี่สิบเก้าจะล้อมกรอบกลุ่ม IMPAIRMENTS นี่เป็นเบาะแสที่ดีว่าทั้งสามกิ่งนี้ถูกเน้นพอ ๆ กัน

สไลด์ที่สามสิบเจ็ดและสามสิบแปดเป็นแบบฝึกหัดและเฉลยที่ควรทำความเข้าใจครับ โจทย์ให้ subsystem ของดิสก์ที่มี MTTF ต่างกัน ได้แก่ ดิสก์ 10 ตัว ตัวละ 1,000,000 ชั่วโมง, SCSI controller 1 ตัว 500,000 ชั่วโมง, power supply 1 ตัว 200,000 ชั่วโมง, fan 1 ตัว 200,000 ชั่วโมง และ SCSI cable 1 เส้น 1,000,000 ชั่วโมง แล้วให้หา MTTF ของระบบรวม โดยสมมติว่าอายุการใช้งานเป็น exponential และความล้มเหลวเป็นอิสระต่อกัน

วิธีคิดคือการบวก failure rate เข้าด้วยกันครับ จำไว้ว่า failure rate เท่ากับหนึ่งส่วน MTTF ดังนั้น failure rate ของระบบเท่ากับ 10 คูณหนึ่งส่วนล้าน บวกหนึ่งส่วนห้าแสน บวกหนึ่งส่วนสองแสน บวกหนึ่งส่วนสองแสน บวกหนึ่งส่วนล้าน ซึ่งเท่ากับ (10 บวก 2 บวก 5 บวก 5 บวก 1) ส่วนล้าน เท่ากับ 23 ส่วนล้าน หรือ 23,000 FIT แล้ว MTTF ของระบบคือส่วนกลับของ failure rate คือหนึ่งพันล้านส่วน 23,000 เท่ากับ 43,500 ชั่วโมง หรือเกือบห้าปี นี่เป็นตัวอย่างที่ดีมากเพราะมันแสดงหลักการสำคัญว่า เมื่อชิ้นส่วนต่อกันแบบ series เราไม่คูณ MTTF แต่เราบวก failure rate นั่นคือเหตุผลที่ระบบที่มีหลายชิ้นส่วนจึงมี MTTF ต่ำกว่าชิ้นส่วนเดี่ยว ๆ มาก

## Dependability Means และเทคนิค Fault Tolerance [สไลด์ 39–41]

สไลด์ที่สามสิบเก้าให้ means ทั้งสี่แบบ Fault prevention คือป้องกันไม่ให้ fault เกิดหรือถูกนำเข้ามา Fault tolerance คือทำให้ระบบให้บริการได้แม้มี fault Fault removal คือลดจำนวน fault ที่มีอยู่ และ Fault forecasting คือประมาณจำนวน fault ปัจจุบัน อนาคต และผลกระทบ สไลด์ที่สี่สิบยกตัวอย่างภารกิจอวกาศเพื่อทำให้เห็นภาพของแต่ละแบบ

สไลด์ที่สี่สิบเอ็ดเป็นแผนภาพที่อธิบายเทคนิค fault tolerance เป็นลูกโซ่สามขั้นครับ คือ Error Detection ไปสู่ Error Recovery ไปสู่ Fault Avoidance ใต้ Error Detection แบ่งเป็น Concurrent ซึ่งตรวจจับระหว่างการทำงาน กับ Pre-emptive ซึ่งตรวจจับล่วงหน้า ใต้ Error Recovery แบ่งเป็น Roll-back ซึ่งคืนระบบไปยัง state ก่อนเกิด error กับ Roll-forward ซึ่งเคลียร์ error ออกหรือไปยัง state ใหม่ที่ไม่มี error และใต้ Fault Avoidance แบ่งเป็น Diagnosis ซึ่งหาสาเหตุที่แท้จริง กับ Isolation และ Reconfiguration ซึ่งแยกชิ้นส่วนที่เสียและจัดระบบใหม่

## รายละเอียดเทคนิค Fault Tolerance [สไลด์ 42–48]

สไลด์ที่สี่สิบสองถึงสี่สิบแปดลงรายละเอียดของเทคนิคเหล่านี้ครับ สไลด์ย้ำว่า fault tolerance คือความสามารถให้บริการต่อเนื่องแม้มี fault และมี coverage กับ fault model เสมอ ไม่มี perfect fault tolerance สไลด์ที่สี่สิบสามแยก error detection เป็น concurrent เช่น watchdog timer, software assertion และ process pair กับ preemptive เช่น spare checking, memory scrubbing และ software rejuvenation สไลด์ที่สี่สิบสี่แยก error recovery เป็น rollback ซึ่งเหมาะกับ transient และ intermittent fault, rollforward และ compensation ซึ่งใช้ redundancy ตามธรรมชาติบัง error สไลด์ที่สี่สิบห้าให้สี่ขั้นของ fault avoidance คือ diagnosis, isolation, reconfiguration และ reinitialisation

สไลด์ที่สี่สิบหกและสี่สิบเจ็ดเป็นแบบฝึกหัดให้คิดว่า เมื่อ multicore system เกิด fault ที่ core หนึ่งและตรวจพบด้วย concurrent check จะมี recovery action อะไรได้บ้าง และเมื่อรันซอฟต์แวร์สองชุดคู่กันแล้วผลไม่ตรงกันจะทำอะไรได้บ้าง ส่วนสไลด์ที่สี่สิบแปดนิยาม coverage ว่าคือความน่าเชื่อถือของเทคนิคในการตรวจจับหรือแก้ fault เมื่อเกิด fault และบอกว่า coverage ลดได้จาก defect ในการ implement เทคนิคเอง ซึ่งมีคำถามเด็ดว่าใครจะตรวจตัวตรวจ, จาก common-mode failure และจากสมมติฐานที่ถูกฝ่าฝืน

## Dependability Threats และสายพาน Fault-Error-Failure [สไลด์ 49–54]

สไลด์ที่สี่สิบเก้าเป็นแผนภาพต้นไม้อีกครั้ง คราวนี้ล้อมกรอบ IMPAIRMENTS ไว้ สไลด์ที่ห้าสิบให้นิยามของ threats ทั้งสาม Fault คือสาเหตุที่ตัดสินหรือสันนิษฐานว่าเป็นต้นเหตุของ error, Error คือส่วนของ state ที่อาจนำไปสู่ failure ในภายหลัง และ Failure คือการที่บริการที่ส่งมอบเบี่ยงเบนไปจากบริการที่ถูกต้อง

สไลด์ที่ห้าสิบเอ็ดเป็นแผนภาพแกนเวลาที่แสดงความสัมพันธ์ของสามคำนี้ครับ บนแกนมีจุด Fault แล้วตามด้วยจุด Error แล้วตามด้วยจุด Failure และมีลูกศรสองหัวบอกช่วงเวลาระหว่างจุดสองจุดคู่แรกเรียกว่า Activation Latency ซึ่งคือเวลาตั้งแต่เกิด fault จนกลายเป็น error และระหว่างจุด Error กับ Failure เรียกว่า Failure Latency ซึ่งคือเวลาตั้งแต่ error จนกลายเป็น failure สองคำนี้มีประโยชน์เพราะมันบอกว่าแม้เกิด fault แล้ว เรายังมีเวลาช่วงหนึ่งก่อนที่มันจะกลายเป็น error และก่อนที่ error จะกลายเป็น failure

สไลด์ที่ห้าสิบสองอธิบายว่าไม่ใช่ทุก fault ที่นำไปสู่ error และไม่ใช่ทุก error ที่นำไปสู่ failure โดย fault อาจถูก mask เพราะไม่ถูก activate หรือถูกแก้ก่อนกลายเป็น error และ error อาจเป็น benign เพราะกระทบ state ที่ไม่สำคัญหรือถูก redundancy แก้ สไลด์ที่ห้าสิบสามเป็นแผนภาพที่ละเอียดกว่านั้นคือ Anatomy of an Error โดยเริ่มจาก Error Occurs แล้วแยกเป็นสองเส้นทาง เส้นทางหนึ่งมี Error Activated ซึ่งต่อด้วย Crash Latency ที่นำไปสู่ Program Crash หรือ Incorrect Output และอีกเส้นทางหนึ่งคือ Unactivated Error ซึ่งรวมกับ Benign Error แล้วจบที่ Success ในที่สุด แผนภาพนี้ทำให้เราเห็นว่า error เพียงตัวเดียวอาจจบได้หลายแบบขึ้นกับว่ามันถูก activate หรือไม่ และถ้า activate แล้วมันกลายเป็น crash หรือ output ผิด

สไลด์ที่ห้าสิบสี่พูดถึงระบบที่เชื่อมต่อกัน โดยบอกว่าความล้มเหลวของระบบหนึ่งอาจเป็น fault หรือ error ของอีกระบบหนึ่งได้ แผนภาพแสดงวงรีที่แทนระบบ A มี Failure A อยู่ที่ขอบ แล้วความล้มเหลวนั้นทะลุออกไปกลายเป็น Fault B ในระบบ B และต่อเนื่องไปเป็น Failure B นี่คือกลไกที่สายพาน fault-error-failure แพร่กระจายข้ามระบบ

## การจำแนก Failure และ Error [สไลด์ 56–57]

สไลด์ที่ห้าสิบหกเป็นการจำแนก failure ด้วยสี่เกณฑ์ครับ เกณฑ์แรก nature แบ่งเป็น halt หรือ fail-stop กับ erratic หรือ babbling เกณฑ์ที่สอง detection แบ่งเป็น signaled กับ un-signaled หรือ fail silent เกณฑ์ที่สาม consistency แบ่งเป็น consistent กับ inconsistent และเกณฑ์ที่สี่ severity แบ่งเป็น minor กับ catastrophic

สไลด์ที่ห้าสิบเจ็ดเป็นการจำแนก error ด้วยสี่เกณฑ์เช่นกัน แต่เกณฑ์แรกต่างออกไป เกณฑ์แรก domain แบ่งเป็น timing กับ content เกณฑ์ที่สอง detection แบ่งเป็น detected กับ latent เกณฑ์ที่สาม consistency และเกณฑ์ที่สี่ severity เหมือนกัน ข้อควรจำคือ failure เริ่มด้วย nature แต่ error เริ่มด้วย domain อย่าสลับ

## ห่วงโซ่ของภัยคุกคามและอนุกรมวิธานของ Fault [สไลด์ 58–62]

สไลด์ที่ห้าสิบแปดและห้าสิบเก้าแสดงห่วงโซ่ของภัยคุกคามเป็นลูกโซ่ที่หมุนวนไปเรื่อย ๆ คือ Failure ไปสู่ Fault ไปสู่ Error ไปสู่ Failure โดยมีป้ายลูกศรว่าการเปลี่ยนจาก Fault ไป Error เรียกว่า Activation, จาก Error ไป Failure เรียกว่า Propagation และจาก Failure กลับไปเป็น Fault ของระบบถัดไปเรียกว่า Causation สไลด์นี้ยังขยายรายละเอียดว่าภายในระบบ fault แบ่งเป็น internal fault ที่อยู่ใน computation process กับ external fault ที่อาศัย vulnerability และ failure นั้นอาจเกิดจากระบบไม่ทำตาม specification หรือ specification เองอธิบายหน้าที่ของระบบได้ไม่ดีพอ

สไลด์ที่หกสิบเป็นอนุกรมวิธานของ fault ที่ละเอียดมากครับ มันแยก fault ออกเป็นสองมุมใหญ่ มุมแรกคือ Origin ซึ่งประกอบด้วย phase of creation หรือ occurrence แบ่งเป็น development กับ operational, system boundaries แบ่งเป็น internal กับ external, phenomenological cause แบ่งเป็น natural กับ human-made, intent แบ่งเป็น malicious กับ non-malicious และ capability แบ่งเป็น accidental, deliberate และ incompetence มุมที่สองคือ Manifestation ซึ่งประกอบด้วย style แบ่งเป็น omission กับ commission, persistence แบ่งเป็น permanent กับ transient, activation reproducibility แบ่งเป็น solid กับ elusive, dimension แบ่งเป็น hardware, software และ system, plurality แบ่งเป็น single กับ multiple, correlation แบ่งเป็น independent กับ related, damage แบ่งเป็น soft กับ hard และ status แบ่งเป็น dormant กับ active

สไลด์ที่หกสิบเอ็ดเป็นแผนภาพต้นไม้ของ fault by origin ที่โยงอนุกรมวิธานนี้เข้ากับสามกลุ่มใหญ่ที่สไลด์ที่หกสิบสามจะกล่าวถึง ได้แก่ development faults, physical faults และ interaction faults ตัวอย่างเช่น human-made malicious fault ที่เป็น deliberate นำไปสู่ malicious logic ส่วน human-made non-malicious นำไปสู่ design flaw หรือ production defect และ operational natural fault นำไปสู่ physical deterioration หรือ physical interference สไลด์ที่หกสิบสองเป็นแผนภาพต้นไม้ที่รวบ Dependability and Security เข้ากับ attributes, threats และ means ทั้งหมด

## ขีดจำกัด ความท้าทาย และข้อมูลเชิงประจักษ์ [สไลด์ 63–70]

สไลด์ที่หกสิบสามบอกขีดจำกัดของ dependability ในรูปของ fault class สามกลุ่ม ได้แก่ physical faults, design และ development faults และ interaction faults และชี้ว่า software reliability เป็นคอขวดของระบบคอมพิวเตอร์ และ fault-tolerance effectiveness ก็เป็นขีดจำกัดอย่างหนึ่ง

สไลด์ที่หกสิบสี่ให้ข้อมูลเชิงประจักษ์ที่น่าสนใจมากครับ มันเปรียบเทียบระบบที่ไม่ทนทานกับระบบที่ทนทาน ในระบบที่ไม่ทนทาน MTTF อยู่ที่ 6 ถึง 12 สัปดาห์ และ downtime เฉลี่ยหลัง failure หนึ่งถึงสี่ชั่วโมง โดยสาเหตุความล้มเหลวมาจาก hardware 50 เปอร์เซ็นต์, software 25 เปอร์เซ็นต์, communications และ environment 15 เปอร์เซ็นต์ และ operations กับ procedures 10 เปอร์เซ็นต์ แต่ในระบบที่ทนทาน เช่นของ Tandem Computers MTTF สูงถึง 21 ปี และสาเหตุความล้มเหลวกลายเป็น software 65 เปอร์เซ็นต์, operations 10 เปอร์เซ็นต์, hardware เพียง 8 เปอร์เซ็นต์ และ environment 7 เปอร์เซ็นต์ ข้อคิดคือเมื่อเราทนทานต่อ hardware failure ได้ดีแล้ว จุดอ่อนที่เหลือจะย้ายไปอยู่ที่ซอฟต์แวร์และการดำเนินงานแทน

สไลด์ที่หกสิบห้าเป็นกราฟที่แสดงว่าในเครือข่าย client-server ที่ไม่ทนทาน ผู้ใช้ต้องเสียเวลาจากการล่มมากแค่ไหนโดยแยกตามสาเหตุ โดยสาเหตุที่แย่ที่สุดคือ design และ configuration change สไลด์ที่หกสิบหกเป็นตารางอุบัติเหตุของเที่ยวบินในสหรัฐที่เทียบสองช่วงเวลา คือ 1970 ถึง 1978 กับ 1979 ถึง 1986 โดยแสดงอัตราอุบัติเหตุต่อล้านเที่ยวบินที่แยกตามสาเหตุคือ technical defect, weather และ human error ซึ่งน่าสนใจว่าสัดส่วนของ human error เพิ่มขึ้นจาก 30 เปอร์เซ็นต์เป็น 41 เปอร์เซ็นต์

สไลด์ที่หกสิบเจ็ดเป็นผลการทดลอง fault injection ในระบบ Delta-4 ที่ทำให้เห็นตัวเลข coverage จริง คือจาก fault 94 เปอร์เซ็นต์กลายเป็น error และจาก error 85 เปอร์เซ็นต์ตรวจพบ และจาก error ที่ตรวจพบ 99 เปอร์เซ็นต์ถูกทนทานได้ แต่ก็ยังมีบางส่วนที่กลายเป็น failure คือ 3 เปอร์เซ็นต์จาก error และ 1 เปอร์เซ็นต์จาก error ที่ตรวจพบ ตัวเลขเหล่านี้ทำให้เห็นว่าการทนทานต่อ fault ในโลกจริงไม่เคย 100 เปอร์เซ็นต์ สไลด์ที่หกสิบเก้าเป็นกราฟต้นทุนความล้มเหลวของคอมพิวเตอร์ในฝรั่งเศสเทียบกับรายได้ของอุตสาหกรรม

สไลด์ที่เจ็ดสิบเป็นตารางเหตุการณ์ FTC ในปี 2025 ซึ่งมีประโยชน์มากเวลาตอบคำถามเชิงอภิปราย เหตุการณ์เหล่านี้เช่น Google Cloud ที่ configuration เปลี่ยนแล้วทำให้เกิด null-pointer crash loop ลามทั้งโลก สอนบทเรียนว่า global replication ที่ไม่มี staged rollout สร้าง common-mode failure, AWS DynamoDB และ DNS ที่ล่มใน region US-East-1 แล้วลามไปทั่ว สอนว่าแม้ระบบ redundant สูงก็พังได้ถ้า dependency วิกฤตกลายเป็น single point of failure, Azure Front Door ที่ทุก region ได้ configuration เสียเหมือนกัน สอนว่า geographic redundancy ช่วยไม่ได้ถ้าทุก region ได้ของเสียเหมือนกัน, Slack ที่ maintenance ทำ database เกินพิกัด, Asana, Cloudflare ที่ bug แฝงถูกกระตุ้นด้วย configuration และ Equinix ที่ maintenance ทำให้ redundancy ลดลงชั่วคราว บทเรียนร่วมคือ configuration ที่ผิดเพียงอันเดียวหรือ bug แฝงตัวเดียวสามารถเอาชนะ redundancy ได้ และมาตรการที่ได้ผลจริงคือ staged rollout, canary deployment, feature flag, regional isolation และ automated rollback

## การบ้านและ Threat Chain ของ Machine Learning [สไลด์ 71–72]

สไลด์ที่เจ็ดสิบเอ็ดเป็นการบ้าน HW01 ที่ให้แสดง threat chain บนระบบ machine learning และสไลด์ที่เจ็ดสิบสองให้ตัวอย่างการโยง fault, error และ failure สำหรับ ML โดย Fault คือ root defect เช่น bad training data, hidden bias หรือ poisoned dataset, Error คือ internal state เช่น corrupted weights, out-of-distribution หรือ overfitting และ Failure คือ visible misbehavior เช่น hallucinatory output หรือ catastrophic system failure

ตัวอย่าง HW01 ที่เพื่อนนักศึกษาทำไว้เป็นเรื่องจริงของ Replit Agent ในปี 2025 ที่ AI coding agent ได้รับสิทธิ์แก้ฐานข้อมูล production โดยตรง Fault คือการที่ AI มีสิทธิ์เข้าถึง production แบบอันตรายและคำสั่งห้ามแก้ไขเป็นเพียงคำสั่งไม่ใช่ข้อจำกัดทางเทคนิค Error คือ agent ตีความผลลัพธ์ว่างเปล่าผิดแล้วรันคำสั่งลบข้อมูล เป็นการทำ state ภายในเสีย และ Failure คือเมื่อแอปเรียกข้อมูลที่ถูกลบไปแล้วมันให้บริการไม่ได้อีก ตัวอย่างนี้สมบูรณ์แบบในการอธิบายสายพาน fault ไป error ไป failure

## จุดเชื่อมกับข้อสอบเก่า

ขอปิดท้ายด้วยการโยงข้อสอบเก่าเข้ากับสไลด์ครับ ข้อที่ถามเรื่อง liveness กับ safety ในมุม FTC นั้นสไลด์ไม่ได้เขียนคำนี้ตรง ๆ ผมจึงต้องตีความ โดย safety ตรงกับ safety attribute ซึ่งเป็นคุณสมบัติว่าไม่มีอะไรแย่เกิดขึ้น และ liveness ตรงกับ reliability กับ availability ซึ่งเป็นคุณสมบัติว่ามีสิ่งดีเกิดขึ้นในที่สุด ข้อที่ถาม threat ของ net banking ให้ใช้สายพานและ attributes ตามที่อธิบายไปแล้ว ข้อที่ถามว่าเมื่อ MTTF น้อยกว่าเวลารันจะแก้อะไร ให้ตอบว่าเปลี่ยนสถาปัตยกรรมด้วย redundancy และ fault tolerance ในรูปแบบ recovery หรือปรับ maintainability ให้ MTTR ต่ำลง และข้อที่ถามว่า fail-safe, self-checking และ recovery วางตรงไหน ให้ใช้แผนภาพ Design Techniques ที่จะอธิบายละเอียดใน Part 7 ซึ่งมีวงเล็บ Fault Avoidance, Fault Masking และ Fault Tolerance คั่นอยู่

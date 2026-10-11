# Part 6 — FTC06 Self-Checking Circuits (เรียงตามสไลด์)

สคริปต์ส่วนนี้เรียงตามลำดับสไลด์ของบท FTC06 ทุกหัวข้อมี `[สไลด์ N]` กำกับ

## ภาพรวมและแนวคิด self-checking [สไลด์ 1–6]

สไลด์ที่หนึ่งเป็นตารางเวลาและย้ำว่าการสอบเป็นแบบเปิดหนังสือ สไลด์ที่สี่แสดง error control สองแบบคือ fault masking scheme ที่ functional unit ป้อน corrector ผ่าน error control codes และป้อน checker ผ่าน error control codes เช่นกัน โดย checker ส่ง syndrome กลับไปยัง corrector และส่ง status ออกมา

สไลด์ที่ห้าเป็น self checking model ที่ควรจำครับ มันมีกรอบ G ล้อมระบบ มี Functional Unit L และ Checker CK โดย input X เข้าทั้งสอง unit, functional unit ส่ง W ให้ checker, output Y ยังถูก tap กลับเข้า checker และ checker ส่ง Error Indicator Z ออกมา สไลด์ที่หกอธิบายว่า self checking คือวิธีทำ concurrent error detection ที่ตรวจจับได้ทั้ง temporary และ permanent fault ตรวจจับได้เร็ว และระบุ field replaceable unit ได้ง่าย

## Error detecting codes และหลักการ [สไลด์ 7–11]

สไลด์ที่เจ็ดบอกว่า code ที่ใช้มีทั้ง separable เช่น parity และ Berger กับ non-separable เช่น m-of-n และ dual rail สไลด์ที่แปดอธิบายว่าเราออกแบบ functional unit ให้ fault ปรากฏเป็น output ที่อยู่ใน error space ซึ่ง checker ตรวจได้ สไลด์ที่เก้าให้สี่กรณีของ functional unit กับ checker ได้แก่ทั้งคู่ดี, เฉพาะ FU ดี (อาจ false alarm แต่ปลอดภัย), เฉพาะ checker ดี และทั้งคู่เสีย (ต้องใช้ checker สอง output)

สไลด์ที่สิบและสิบเอ็ดอธิบาย code space กับ error space และการต่อ module แบบ cascade โดยในแต่ละจุดต่อจะมี self-checking checker คอยตรวจ

## นิยามรากฐาน FS, ST และ TSC [สไลด์ 12–18]

สไลด์ที่สิบสองให้สองนิยามที่สำคัญที่สุดครับ Fault Secure คือสำหรับ input ใน N และ fault ใด ๆ ค่า Y ต้องเท่ากับ Y ที่ไม่มี fault หรือไม่ก็ไม่อยู่ใน output codespace S ส่วน Self Testing คือสำหรับทุก fault ต้องมี input อย่างน้อยหนึ่งตัวที่ทำให้ Y ออกไปนอก S สไลด์ที่สิบสามและสิบสี่อธิบายสองอย่างนี้ด้วยแผนภาพ concentric circle โดย FS ห้าม output เป็น incorrect codeword ส่วน ST ต้องการให้มี input ที่เผย fault

สไลด์ที่สิบห้าและสิบหกเป็นตัวอย่างที่ช่วยให้เห็นความต่างจริง กำหนด input space ที่มี X1 กับ X2 และ fault มี f1, f2 อยู่ภายในเซต F แต่ f3 อยู่นอกเซต Self Testing หมายถึงค่าที่เกิดจาก Y(X1,f2), Y(X2,f1) และ Y(X2,f2) นั้นเผย fault ได้ ส่วน Fault Secure ครอบคลุมกว่า และ f3 นั้นเป็น undetectable fault คือ Y(X2,f3) ยังอยู่ใน S สไลด์ที่สิบเจ็ดยกวงจร EXOR เป็นตัวอย่างที่เป็นทั้ง Fault Secure, Self Testing และ Code Preserving

สไลด์ที่สิบแปดนิยาม Totally Self Checking ว่าคือ FS บวก ST และบอกข้อจำกัดว่าไม่ใช่ทุก fault ตรวจจับได้ และแม้ FS แต่ถ้ามี undetectable fault อยู่ fault ถัดไปอาจทำให้คุณสมบัติเสียได้

## Strongly Fault Secure [สไลด์ 19–21]

สไลด์ที่สิบเก้านิยาม SFS เพื่อแก้ข้อจำกัดนั้นครับ วงจรเป็น SFS ถ้าเข้าเงื่อนไขข้อหนึ่งคือเป็น TSC สำหรับ fault เดียว {f} หรือเป็น FS สำหรับ {f} และ SFS สำหรับ F ลบ {f} คุณสมบัติที่ได้คือ output error ตัวแรกเป็น non-codeword สไลด์ที่ยี่สิบขยายไปหลาย fault โดยแสดงว่าเมื่อมี fault น้อยกว่า m ค่า Y ยังเท่ากับ Y ที่ไม่มี fault แต่เมื่อครบ m fault แล้วต้องมี input อย่างน้อยหนึ่งที่ทำให้ Y ออกนอก S

สไลด์ที่ยี่สิบเอ็ดเป็นตัวอย่าง SFS ที่ดีมากครับ วงจรมี input codespace N เท่ากับ (0/0), (0/1), (1/0) และ output codespace S เท่ากับ (1/0), (0/1) พร้อม fault f1 ถึง f4 ที่เป็น stuck-at ต่าง ๆ ผลคือวงจรเป็น Fault Secure สำหรับลำดับ ⟨f1, f2, f3⟩ และเป็น Strongly Fault Secure สำหรับลำดับ ⟨f1, f2, f3, f4⟩ โดยเมื่อใส่ fault ครบแล้วได้ (1/0) ซึ่งยังอยู่ใน S

## Error Secure, Code Disjoint และ SCD [สไลด์ 22–27]

สไลด์ที่ยี่สิบสองและยี่สิบสามนิยาม Error Secure ว่าคือคุณสมบัติที่ถ้า input เป็น non-codeword ผลลัพธ์จะเป็น codeword ที่ถูกต้อง (คือ fault masking) หรือไม่ก็เป็น non-codeword สไลด์ที่ยี่สิบสี่และยี่สิบห้านิยาม Error Preserving หรือ Code Disjoint ว่าคือคุณสมบัติของวงจรที่ไม่มีความผิดพลาด ที่ถ้า input เป็น codeword หรือ non-codeword แล้ว output ก็เป็น codeword หรือ non-codeword ตามลำดับ จุดต่างคือ ES ยอมให้ output เป็น codeword เดิมได้ แต่ CD บังคับว่าถ้า input ไม่ใช่ codeword output ต้องไม่ใช่ codeword

สไลด์ที่ยี่สิบหกและยี่สิบเจ็ดนิยาม Strongly Code Disjoint แบบเวียนเกิดเช่นเดียวกับ SFS สไลด์ที่ยี่สิบแปดและยี่สิบเก้าเป็นแบบฝึกหัดที่ตรงกับข้อสอบเก่าครับ มันให้วงจรที่มีความสัมพันธ์แบบ one-hot โดย codeword คือ (0,0), (0,1), (1,0) และถามว่าวงจรเป็น CD ไหมในกรณี fault-free และเป็น FS หรือ ST สำหรับ f1, f2, f3 ไหม สไลด์ที่ยี่สิบเก้าให้ตารางที่เติมคำตอบแล้ว ซึ่งแสดงว่าคอลัมน์ f3sa1 ให้ค่า 11 ในทุกแถว ซึ่งเป็น non-codeword ทั้งหมด นี่คือตัวอย่างที่ควรฝึกทำความเข้าใจเพราะมันคือโจทย์ที่ข้อสอบเก่าถามโดยตรง

## Self-checking logic network และ inverter-free [สไลด์ 30–34]

สไลด์ที่สามสิบถึงสามสิบสองให้ทฤษฎีบทที่ว่าถ้า subnetwork LI ซึ่งเป็น output interface เป็น SFS และ SCD สำหรับ FI และ subnetwork LII ที่เหลือเป็น SFS สำหรับ FII แล้ว network ทั้งหมดเป็น SFS ในทำนองเดียวกันกับ inverter-free network ที่ interface encode ด้วย unidirectional code จะเป็น SFS สำหรับ unidirectional fault สไลด์ที่สามสิบสามและสามสิบสี่แสดง cascaded inverter-free network และย้ำว่าแต่ละ block ไม่ได้เป็น CD เสมอ และ non-codeword อาจปรากฏที่ embedded interface ก่อนที่จะกลายเป็น output error ตัวแรก

## Checker และชนิดของมัน [สไลด์ 35–43]

สไลด์ที่สามสิบห้าถึงสามสิบเก้าให้ self checking model และชนิดของ checker ครับ Code Checker ตรวจ output ที่ encode แล้ว ส่วน Prediction Checker ใช้กับ output ที่ไม่ encode มีสามแบบคือ Duplication checker ที่ทำสำเนาแล้วเปรียบเทียบ, Parity prediction checker ที่ทำนาย parity ของ output จาก input แล้วเทียบกับ parity จริง และ Input regeneration checker ที่สร้าง input กลับจาก output ด้วย inverse logic แล้วเทียบกับ input เดิม สไลด์ที่สี่สิบให้ simplified regeneration checker ที่ตรวจ input เดียวด้วยสูตร x1 เท่ากับ y0 XOR (y1 คูณ y2)

สไลด์ที่สี่สิบเอ็ดให้ lemmas สองข้อที่ต้องจำ ข้อแรก checker ต้องมี output อย่างน้อยสองขาและไม่มีขาคงที่ ข้อที่สอง Fault Secure ไม่จำเป็นสำหรับ checker สไลด์ที่สี่สิบสองสรุปคุณสมบัติที่ checker ต้องมีคือ 2 output line, Code-Disjoint, Self Testing และ SCD สไลด์ที่สี่สิบสามแสดง input และ output space ของ code checker กับ prediction checker

## ตัวอย่างที่ผิดและ TSC error combining [สไลด์ 44–46]

สไลด์ที่สี่สิบสี่และสี่สิบห้าแสดง "What's wrong" กับ conventional code checker ครับ ตัวอย่างคือ 5-input odd-parity checker ที่มี output ขาเดียวและเป็น Code-Disjoint แต่ไม่เป็น Self Testing เพราะ fault แบบ stuck-at-0 ที่ output อาจไม่ถูกตรวจพบ นี่คือบทเรียนว่าทำไม checker ต้องมีสอง output

สไลด์ที่สี่สิบหกแสดงการรวม error signal ของ checker สองตัวด้วย two-rail code checker โดยมีตาราง simplified truth table ที่กำหนดให้ 01 กับ 10 เป็น G และ 00 กับ 11 เป็น B และกฎคือ GG ให้ G นอกนั้นให้ B

## การออกแบบ checker ชนิดต่าง ๆ [สไลด์ 47–63]

สไลด์ที่สี่สิบแปดและสี่สิบเก้าให้ parity code checker ที่เป็น XOR tree แบ่งเป็นสองกลุ่ม โดย C0 มาจากกลุ่ม x8, x6, x4, x2, x0 และ C1 มาจากกลุ่ม x7, x5, x3, x1 ทำให้มีสอง output เป็น codeword ที่เป็น one-hot สไลด์ที่ห้าสิบและห้าสิบเอ็ดให้ two rail code checker ที่เปรียบเทียบสำเนา a กับ b โดย b ผ่าน inverter และให้ตัวอย่าง 2-pair ที่ตรวจชุด 0101, 0110, 1001, 1010

สไลด์ที่ห้าสิบสองถึงห้าสิบสี่อธิบาย two rail code sequence โดยใช้ชุดทดสอบ R, S, T ที่ทำให้ checker เป็น self testing สำหรับ stuck-at fault ทั้งหมดโดยไม่ขึ้นกับขนาดข้อมูล สไลด์ที่ห้าสิบห้าถึงห้าสิบเก้าให้ 1-of-n code checker ที่ถอดรหัส n ไป k แล้วต่อ tree ของ two rail checker, m-of-2m code checker ที่ใช้สูตร C0 และ C1 ตามค่าน้ำหนัก v และ w, และการสร้าง m-out-of-2m จาก 2-out-of-4 checker

สไลด์ที่หกสิบถึงหกสิบสามให้ TSC checker สำหรับ k-out-of-n, สำหรับ separable code โดยใช้ complement ของ check bit, สำหรับ Berger code และ Generalized Prediction Checker

## TSC functional unit และ dual rail [สไลด์ 64–70]

สไลด์ที่หกสิบสี่และหกสิบห้าอธิบาย TSC MUX และ dual rail logic ที่ encode 1 บิตเป็น 01 หรือ 10 และรักษา code หลัง operation สไลด์ที่หกสิบหกและหกสิบเจ็ดเป็นแบบฝึกหัด dual-logic ที่น่าสนใจครับ ให้ F เท่ากับ a-bar b บวก b c-bar บวก ac และ F-bar เป็น dual ของมัน และเมื่อใส่ fault a stuck-at-0 จะพบว่า output ของ 8 ชุด input นั้นมีบางชุดให้ผลเป็น non-codeword จึงสรุปว่าวงจรมีคุณสมบัติ FS บวก ST เท่ากับ TSC นี่คือโจทย์ที่ควรฝึกทำความเข้าใจ

สไลด์ที่หกสิบแปดและหกสิบเก้าให้ contraction circuit และทฤษฎีบทที่ว่า SFS นำไปสู่ TSC และสไลด์ที่เจ็ดสิบให้นิยาม SFS functional unit ว่าเป็น non-redundant, non-inverter และ output coding ด้วย unordered code

## การออกแบบ TSC ขั้นสูง [สไลด์ 71–76]

สไลด์ที่เจ็ดสิบเอ็ดอธิบาย TSC ด้วย parity prediction ที่ใช้ parity predictor แทน duplication และแก้ให้เป็น self-checking ด้วยการให้ predictor สร้าง complement ของ output parity แล้วลบ XOR gate ออก สไลด์ที่เจ็ดสิบสองอธิบาย TSC ด้วย residue encoding ที่ใช้ได้กับการบวก ลบ คูณ และต้องแก้กล่อง Find mod A ให้สร้าง complement ของ residue พร้อมใช้ two-rail checker แทน comparator

สไลด์ที่เจ็ดสิบสามพูดถึง self-checking design บน FPGA และสไลด์ที่เจ็ดสิบสี่ให้ทฤษฎีบทการวาง checker ให้ path loop มี checker สไลด์ที่เจ็ดสิบห้าอธิบาย partially self-checking unit ที่บายพาสการตรวจเมื่อ code ใช้ไม่ได้ เช่น logical operation และสไลด์ที่เจ็ดสิบหกอธิบาย self-checking state machine ของ Diaz และ Azema ที่ encode input และ output ด้วย two-rail และ encode state เป็น k-out-of-n ทำให้ next-state function เป็น monotonic และตรวจจับ unidirectional error ได้

## การบ้าน HW06 [สไลด์ 77–78]

สไลด์ที่เจ็ดสิบเจ็ดเป็นหัวข้ออ่านเพิ่มเติม และสไลด์ที่เจ็ดสิบแปดเป็นการบ้าน HW06 ที่ให้ออกแบบ self-checking 2:4 demultiplexer with enable ซึ่งเป็นโจทย์ที่ต้องออกแบบวงจรที่มี checker ตรวจสอบตัวเองได้ วิธีคิดคือสร้างวงจรที่ output เป็น one-hot และเพิ่ม checker ที่ตรวจว่ามีหนึ่งพอดีหนึ่งตัวตลอดเวลา


## จากคำบรรยายในห้อง [insights]

**เคล็ดวิธีทำโจทย์** อาจารย์แนะนำว่า ถ้าโจทย์ไม่ยากให้ **"เจนด้วยเบอร์ก่อน"** คือสร้างตาราง truth table หรือ state ให้ครบก่อน แล้วค่อยวิเคราะห์ว่า output เป็น code word หรือ non-code word วิธีนี้ตรงกับวิธีที่ผมแนะนำในหัวข้อโจทย์ FS/ST ท้าย Part และอาจารย์ยังบอกว่าโจทย์แนว self-testing กับ fault-secure นั้น "ปกติไม่ได้หมุนเยอะ" คือไม่ได้ออกบ่อยหรือออกลึกมาก แต่วิธีเจนตารางยังต้องใช้เวลาเจอ

**ข้อจำกัดของ checker ที่ต้องเข้าใจ** มีจุดที่อาจารย์เน้นมากว่า **checker ไม่ได้ตรวจความถูกต้องเชิงตรรกะ** เช่นมันไม่รู้ว่า 2 บวก 2 ต้องเป็น 4 checker ตรวจแค่เพียงว่า **ค่าที่ได้ยังอยู่ในรูป code word หรือไม่** ถ้า functional unit ให้ค่าที่ผิดแต่ยังอยู่ในรูป code word checker จะไม่รู้ นี่เป็นข้อจำกัดเชิงแนวคิดที่สำคัญ และเป็นเหตุผลว่าทำไมเราต้องเลือก code ให้ดี

**ทำไม Fault Secure ต้องคู่กับ Self Testing** อาจารย์อธิบายว่า ถ้าวงจรเป็น FS แต่ตรวจไม่เจอทันที fault ตัวถัดไปอาจทำให้คุณสมบัติ FS หายไปได้ เราจึงต้องมี ST เพื่อจับให้เร็วที่สุดก่อนที่ fault ใหม่จะเกิด และมีหลัก **monotonic** ที่สำคัญคือ เมื่อผิดพลาดแล้วต้องไปทาง non-code word เท่านั้น **ห้ามกลับไปที่ code space** ไม่งั้นจะกลายเป็น error ที่หลุดการตรวจจับ

**dual rail ทำให้ error เป็น unidirectional** อาจารย์อธิบายว่าวงจร dual rail ไม่มี inverter ปรากฏในวงจรจริง จึงทำให้ error ที่เกิดขึ้นเป็น unidirectional ซึ่งเป็นแบบจำลองที่ใช้งานได้จริงและคลุมทั้ง single และ multiple error และเมื่อรวมกับ recompute แล้ว compare ก็ได้คุณสมบัติ fault secure และ preserve code

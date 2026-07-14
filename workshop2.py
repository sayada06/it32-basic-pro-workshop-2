name = input("ชื่อ : ")
age = int(input("อายุ (ปี) : "))
height = float(input("ส่วนสูง (cm) : "))
strength = int(input("พละกำลัง (1-10) : "))
money = float(input("เงินติดตัว (Starter Pack Dollar) : "))

#age <= 35 and height > 180 and strength > 8 = Caporegime (หัวหน้าหน่วย)
#height > 180 or strength > 8 = Soldier (สมาชิก)
#age > 35 and or strength < 8 = janitor (ภารโรง)

if age <= 35 and height > 180 and strength > 8:
    print (f"ยินดีด้วย!!", name, "ตอนนี้แกได้เป็นหัวหน้าหน่วยของพวกเราแล้ว ฮะฮะฮ่าาาา" )
elif height > 180 or strength > 8:
    print (f"ยินดีด้วย!!", name, "ตอนนี้แกได้เป็นสมาชิกของพวกเราแล้ว ฮะฮะฮ่าาาา" )
elif age > 35 and strength > 5:
    print (f"ยินดีด้วย!!", name, "ตอนนี้แกได้เป็นภารโรงของพวกเราแล้ว ฮะฮะฮ่าาาา" )
else:
    print (f"แกมันช่างอ่อนด๋อยจริงๆเลยนะ", name, "ไสหัวออกไปจากที่ของฉันซะ!")
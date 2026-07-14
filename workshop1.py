quantity = int(input("จำนวนปืนที่รับมาขาย (กระบอก) : "))
cost_price = float(input("ต้นทุนของปืนที่รับ (บาท/กระบอก) : "))
sell_price = float(input("ราคาที่จะนำไปขายต่อ (บาท/กระบอก) : "))
team_member = int(input("จำนวนลูกน้องในทีมที่ไปทำงาน (คน) : "))

income = sell_price * quantity
cost = cost_price * quantity
profit = income - cost
boss = profit * (20 / 100)

print (f"ต้นทุนทั้งหมด (บาท) : ", cost)
print (f"รายรับทั้งหมด (บาท) : ", income)
print (f"กำไรสุทธิ (บาท) : ", profit)
print (f"จำนวนเงินที่หักไปให้บอส (บาท) : ", boss)
print (f"จำนวนเงินที่ลูกน้องแต่ละคนได้ (บาท) : ", ((profit - boss) / team_member))

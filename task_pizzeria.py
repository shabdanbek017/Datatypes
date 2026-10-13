#Задача: Пиццерия
item1_name  = "Маргарита"
item1_price = 2200
item1_qty   = 2

item2_name  = "Пепперони"
item2_price = 2700
item2_qty   = 1

item3_name  = "Кола 1л"
item3_price = 700
item3_qty   = 3

item4_name  = "Чизкейк"
item4_price = 1500
item4_qty   = 2

delivery         = True
delivery_price   = 800
discount_percent = 10

price1 = item1_price * item1_qty
price2 = item2_price * item2_qty
price3 = item3_price * item3_qty
price4 = item4_price * item4_qty
sum_all = sum([price1, price2, price3, price4])
Discount_all = sum_all * discount_percent / 100
total_amount_withdiscount = sum_all - Discount_all
deliveryfee = delivery_price * int(delivery)
final_amount = total_amount_withdiscount + deliveryfee
Average_cost = sum_all / 4
print("======== Чек =======")
print(f"{item1_name} \t {item1_price} x {item1_qty} = {item1_price * item1_qty} " )
print(f"{item2_name} \t {item2_price} x {item2_qty} = {item2_price * item2_qty} " )
print(f"{item3_name} \t {item3_price} x {item3_qty} = {item3_price * item3_qty} " )
print(f"{item4_name} \t {item4_price} x {item4_qty} = {item4_price * item4_qty} " )
print("-------------------")
print(f"Подытог: \t {sum_all}")
print(f"Скидка(10%): \t {Discount_all}")
print(f"Итог со скидкой: \t {total_amount_withdiscount}")
print(f"Доставка: \t {deliveryfee} \n --------------- \n К ОПЛАТЕ: \t {final_amount} \n =============== \n Позиций: 4 ")
print(f"Средняя стоимость позиций: {Average_cost}")
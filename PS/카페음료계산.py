menu={"아메리카노":1500,"바닐라라떼":2000,"카푸치노":2500}
orders=[]
total=0
while True:
  order=input("주문:")
  if order=="끝":
    break
  if order in menu:
    total+=menu[order]
    orders.append(order)
  else:
    print('메뉴에 없습니다 다시 입력해 주세요')
print(f'총 결제 금액은 {total} 원입니다.')
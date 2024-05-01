##
#	이 프로그램은 람다식을 이용하여 주문을 처리한다.  
#
orders = [ ["1", "재킷", 5, 120000], 
           ["2", "셔츠", 6, 24000], 
           ["3", "바지", 3, 50000],
           ["4", "코트", 6, 300000] ]

result = list(map(lambda x: (x[0], x[2] * x[3]), orders))
print(result)
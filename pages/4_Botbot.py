import random
import time

products = ['iPhone', 'iPad', 'MacBook'] 
prices = [1000, 800, 1500]

balance = 0
last_game_time = 0

def print_menu():
    print('МЕНЮ:')
    print('1. Выбрать товар')
    print('2. Посмотреть баланс')    
    print('3. Сыграть в игру на скидку')
    
def print_header(text):
    print('=' * 10, text, '=' * 10)
    
def choose_product():
    print_header('Выбор товара')  
    for i, p in enumerate(products):
        print(f'{i+1}. {p} - {prices[i]} руб') 
    choice = int(input('> ')) - 1   
    selected_product = products[choice]
    selected_price = prices[choice] 
    
    print(f'Вы выбрали {selected_product}, цена {selected_price} руб')
    return selected_product, selected_price

def play_discount_game():
    global last_game_time
    global balance
    
    current_time = int(time.time()) 
    if current_time - last_game_time < 24*3600:
        print('Играть можно раз в сутки')
        return
        
    print_header('Игра на скидку')       
    discount = random.randint(1, 15)
    airpods_chance = random.random() < 0.001
    
    if airpods_chance:
        print('Вы выиграли AirPods!!!') 
        balance += 1  
    else:
        print(f'Ваша скидка: {discount}%')
        balance += discount
        
    last_game_time = current_time
        
def print_balance():     
    print_header('Баланс')
    if balance > 0:
        print(f'На вашем счету: {balance} баллов')
    else:
        print('У вас пока нет баллов')
        
while True:
    print_menu()
    choice = int(input('> '))
    
    if choice == 1:
        choose_product() 
    elif choice == 2:
        print_balance()
    elif choice == 3:
        play_discount_game()

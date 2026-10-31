import time 

#synchronous code
def make_coffee():
    print("Starting coffee machine...")
    time.sleep(2)
    print("Coffee ready")
    return 'cappucino'

def make_toast():
    print("Starting toast...")
    time.sleep(2)
    print("toast ready")
    return 'cruny bread'

def main():
    coffee = make_coffee()
    toast = make_toast()
    break_fast = []
    break_fast.append(coffee)
    break_fast.append(toast)
    print(f'Breakfast served...{break_fast}')
    
main()
    

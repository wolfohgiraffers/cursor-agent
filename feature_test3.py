"""
Feature Test 3
새로운 기능 테스트를 위한 모듈입니다.
"""

def calculate_sum(a, b):
    """두 숫자의 합을 계산합니다."""
    return a + b

def calculate_product(a, b):
    """두 숫자의 곱을 계산합니다."""
    return a * b

def greet_user(name):
    """사용자에게 인사말을 전달합니다."""
    return f"안녕하세요, {name}님!"

class Calculator:
    """간단한 계산기 클래스입니다."""
    
    def __init__(self):
        self.history = []
    
    def add(self, a, b):
        result = a + b
        self.history.append(f"{a} + {b} = {result}")
        return result
    
    def multiply(self, a, b):
        result = a * b
        self.history.append(f"{a} * {b} = {result}")
        return result
    
    def get_history(self):
        return self.history

if __name__ == "__main__":
    # 테스트 실행
    print("Feature Test 3 실행 중...")
    
    # 함수 테스트
    print(f"5 + 3 = {calculate_sum(5, 3)}")
    print(f"4 * 6 = {calculate_product(4, 6)}")
    print(greet_user("개발자"))
    
    # 클래스 테스트
    calc = Calculator()
    calc.add(10, 20)
    calc.multiply(5, 7)
    
    print("\n계산 기록:")
    for record in calc.get_history():
        print(f"  {record}")
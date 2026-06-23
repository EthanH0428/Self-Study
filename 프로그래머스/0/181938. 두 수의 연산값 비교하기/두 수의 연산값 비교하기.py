def solution(a, b):
    # a ⊕ b 연산 (문자열로 붙였다가 숫자로 변환)
    ab = int(str(a) + str(b))
    
    # 2 * a * b 연산 (일반 정수 곱셈)
    two_ab = 2 * a * b
    
    # 두 값 중 더 큰 값을 반환 (같으면 ab 반환)
    return max(ab, two_ab)
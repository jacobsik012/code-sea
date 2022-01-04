class ThailandPackage:
     def detail(self):
        print("[태국 패키지 3박 5일] 방콕, 파타야 여행 (야시장 투어) 50만원")

# if __name__ == "__main__": # __name__ 이 __main__ 이면 (thailand 모듈에서 직접 호출)
print("thailand 모듈을 직접 실행")
print("이 문장은 모듈을 직접 실행할 때만 실행돼요")
trip_to = ThailandPackage()
trip_to.detail()
# else: # __name__ 이 __main__ 아니면 (thailand 모듈 외부에서 호출)
#     print("thailand 외부에서 모듈 호출")

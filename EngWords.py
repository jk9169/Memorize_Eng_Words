import pandas as pd
import random

# 엑셀 파일명, 열 이름 변수로 관리
excel_file = 'EngWords_Data.xlsx'
engword_col = '단어'
mean_col = '뜻'

def test_mode():
    
    
    wrong_words = []        # 오답 리스트
    selected_words = []     # 이미 테스트한 단어들

    # 차례대로 테스트하기
    score = 0
    cnt = 0
    print("영어 단어 암기 프로그램 시작!\n")

    # 엑셀 파일 불러오기 
    word = pd.read_excel(excel_file, sheet_name='words')

    while (cnt < len(word[mean_col])):
        word_list = list(zip(word[engword_col], word[mean_col]))
        random_word = random.choice([w for w in word_list if w[0] not in selected_words])   #이미 선택된 단어는 제외

        print("뜻:", random_word[1])
        answer = input("영어 : ")

        #정답인 경우
        if answer == random_word[0]:
            print("정답입니다!")
            score += 1

        #오답인 경우
        else:
            print("오답, 정답은 "+ random_word[0])
            wrong_words.append(random_word[0])
        
        
        #다음으로 넘어가기 전
        selected_words.append(random_word[0])
        print("\n")   
        cnt += 1

    #테스트 종료
    print("당신의 점수는","%.2f" %( (score*100)/len(word[mean_col]) )+"점 입니다.")

    if len(wrong_words) > 0:
        print("틀린 단어 목록")
        print(wrong_words)




def add_mode():
    word = pd.read_excel(excel_file, sheet_name='words')
    # while True:
    new_word = pd.DataFrame([[input("단어를 입력하세요: "), input("뜻을 입력하세요: ")]],columns=[engword_col, mean_col])
    word = word.append(new_word, ignore_index=True)
    
    #새로운 데이터를 기존의 데이터셋에 추가
    word.to_excel(excel_file, sheet_name='words', index=False)            





if __name__ == "__main__":
    
    # print("영어 단어 암기 프로그램 시작!\n")

    while True:
        mode = input("모드를 선택하세요. (1:암기, 2:단어 추가, 3:종료) ")
        
        if mode == '1':
            test_mode()
            
        elif mode == '2':
            add_mode()
        
        elif mode == '3':
            print("프로그램을 종료합니다.")
            break
        
        else:
            print("잘못된 입력입니다. 다시 입력해주세요.\n")

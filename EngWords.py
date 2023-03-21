import pandas as pd



#엑셀 파일명, 열 이름 변수로 관리
exel_file = 'EngWords_Data.xlsx'
engword_col = '단어'
mean_col = '뜻'

# 엑셀 파일 불러오기 
word = pd.read_excel(exel_file, sheet_name='words')


#차례대로 테스트하기
score = 0
cnt = 0
print("영어 단어 암기 프로그램 시작!\n")

while (cnt < len(word[mean_col]) ):
    print("뜻:", word[mean_col][cnt])
    answer = input("영어 : ")
    #정답인 경우
    if answer == word[engword_col][cnt] :
        print("정답입니다!")
        score += 1
    #오답인 경우
    else:
        print("오답, 정답은 "+word[engword_col][cnt] )
    #다음으로 넘어가기 전 
    print("\n")   
    cnt += 1

#테스트 종료
print("당신의 점수는","%.2f" %( (score*100)/len(word[mean_col]) )+"점 입니다.")

    

korean = int(input('국어 '))
english = int(input('영어 '))
math = int(input('수학 '))
science = int(input('과학 '))

sum = korean + english + math + science
avg = sum / 4

if avg >= 95:
    score = 'A+'
elif avg < 95 and avg >= 90:
    score = 'A0'
elif avg < 90 and avg >= 85:
    score = 'B+'
elif avg < 85 and avg >= 80:
    score = 'B0'
elif avg < 80 and avg >= 75:
    score = 'C+'
elif avg < 75 and avg >= 70:
    score = 'C0'
elif avg < 70 and avg >= 65:
    score = 'D+'
elif avg < 65 and avg >= 60:
    score = 'D0'
elif avg < 60:
    score = 'F'
print('국어 ', korean, '점')
print('영어 ', english, '점')
print('수학 ', math, '점')
print('과학 ', science, '점')

print('합계 ', sum, '점, ', end = ' ')
print('평균 ', avg, '점, ', end = ' ' )
print('학점 ', score)
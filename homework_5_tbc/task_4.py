n = int(input('Enter your number: '))

if n > 0 and n < 50:
    print(" " * (n - 1) + "*" * (1))
    for i in range(n):
        print(" " * (n - i - 1) + "/" * (i) + '|' + "\\" * (i) + " " * (n - i - 1))

    print(" " * (n - 1) + "|" * (1))
else:
    print('Enter your number between 0 and 50')
    exit(1)

'''    
ამ სავარჯიშოში ერთი რამ ვერ გამოვასწორე, print-ის დროს
ერთადერთია ხარვეზია რაცაა ის რო  *-ის მერე მოდის პირდაპირ
| სიმბოლო /|/ ამის მაგივრად და მაგას ვერ ვაკეთებ ერთადერთი
'''
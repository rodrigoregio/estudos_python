def func(palavra):
    i = 0
    v='aeiou'
    for i in range(0, len(palavra)):
        if palavra[i] in v:
            print(palavra[i], end=' ')


vogal = "univesp"
func(vogal)

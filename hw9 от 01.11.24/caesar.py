class Caesar:
    alphabet = "яюэьыъщшчцхфутсрпонмлкйизжёедгвба"

    def __init__(self, key):
        self._encode = dict()
        for i in range(len(self.alphabet)):
            letter = self.alphabet[i]
            encoded = self.alphabet[(i + key) % len(self.alphabet)]
            self._encode[letter] = encoded
            self._encode[letter.upper()] = encoded.upper()
        self._decode = {}  # TODO
        for i in range(len(self.alphabet)):
            letter = self.alphabet[i]
            encoded = self.alphabet[(i - key) % len(self.alphabet)]
            self._encode[letter] = encoded
            self._encode[letter.upper()] = encoded.upper()
    def encode(self, text):
        return ''.join([self._encode.get(char, char) for char in text])

    def decode(self, line):
        return ''.join([self._encode.get(char, char) for char in line])


key = 14
#int(input('Введите ключ '))
cipher = Caesar(key)

line = 'Кыжг вгбдебь ътячан. Вбъцгтфюсчя д гтдкыжгбфэбь гтъцчют! Ыетэ, фн цбхтцтюыдо вбйчяё кыжг Ичътгс ач сфюсчедс эгывебдебьэыя: дюыкэбя ятют яблабдео яабщчдефт эюрйчь ы аёщань эюрй ючхэб атьеы ячебцбя вбюабхб вчгчубгт. Ябщаб юы ёфчюыйыео эгывебдебьэбдео, ач ячасс ячебц кыжгбфтаыс? Цт, ябщаб. Чдюы ътячасео бцыа дыяфбю тюжтфыет ат бвгчцчюшаань цгёхбь дыяфбю ебхб щч тюжтфыет вб этэбь-еб етуюыич ътяча, еб дтят етуюыит ътяча ы сфюсчедс эюрйбя. Яабщчдефб эюрйчь — пеб яабщчдефб фбъябщанз етуюыи вгбденз ътяча. Цюс гёддэбхб тюжтфыет яблабдео яабщчдефт етуюыи вгбденз ътяча гтфат жтэебгытюё бе 33. 33! = 8683317618811886495518194401280000000. Чдюы егтеыео ат вгбфчгэё бцабхб фтгытает 0.000001 дчэёацн, вбюёйыедс 2.8e+23 юче. Ябщче вбэтътеодс, йеб кыжг вгбдебь ътячан фвбюач эгывебдебьэыь, бцатэб пеб ач етэ. Чхб цбдетебйаб вгбдеб фъюбятео вгы вбяблы [йтдебеабхб татюыът]. Цчюб ф ебя, йеб йтдебет вбсфючаыс ътцтаабь уёэфн тюжтфыет ф цбдетебйаб цюыаанз ечэдетз бцат ы ет щч цюс гтъанз ечэдебф бцабхб сънэт. Чдюы ф кыжгбечэдеч уёцче дыяфбю д фчгбсеабдеор вбсфючаыс, татюбхыйабь детацтгеабь цюс сънэт, еб ябщаб вгчцвбюбщыео, йеб ба ы сфюсчедс ёэтътаабь ъткыжгбфтаабь уёэфбь. Ячебц йтдебеабхб эгывебтатюыът ыъфчдеча д IX-хб фчэт, збес атыубючч ыъфчдеаня дюёйтчя чхб вгыячачаыс ф гчтюоабь щыъаы, фбъябщаб, сфюсчедс цчкыжгбфэт чхывчедэыз ычгбхюыжбф ф 1822 хбцё. Ыетэ, дючцёрлтс йтдео гтубен ъткыжгбфтат вгы вбяблы дючцёрлчь вгбхгтяян: Вгбхгтяяё цюс йтдебеабхб татюыът дючцёче атвыдтео дтябдебсечюоаб. Ёдвчзбф!'

while line:
    print(cipher.decode(line))
    line = input()
    
    
'''Шифр Цезаря — это вид шифра подстановки, в котором каждый символ в открытом тексте заменяется символом, 
находящимся на некотором постоянном числе позиций левее или правее него в алфавите. Например, в шифре 
со сдвигом вправо на 3, А была бы заменена на Г, Б станет Д, и так далее. Шифр назван в честь римского императора
Гая Юлия Цезаря, использовавшего его для секретной переписки со своими генералами. 

Следующая часть работы зашифрована шифром Цезаря. Допишите метод decode и расшифруйте следующий раздел лабораторной работы. 
Подумайте, почему вам не сообщили ключ шифрования и что вам с этим делать.'''
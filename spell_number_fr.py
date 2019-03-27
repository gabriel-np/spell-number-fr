def num_to_french(num):
    chiffres = {'1':'un','2':'deux','3':'trois','4':'quatre','5':'cinq','6':'six','7':'sept','8':'huit','9':'neuf',
            '10':'dix','11':'onze','12':'douze','13':'treize','14':'quatorze','15':'quinze','16':'seize','17':'dix-sept','18':'dix-huit','19':'dix-neuf',
            '20':'vingt','30':'trente','40':'quarante','50':'cinquante','60':'soixante','70':'soixante-dix','80':'quatre-vingt','90':'quatre-vingt-dix',}

    def dizaine(num, num_str):
        if num < 10:
            return chiffres.get(num_str[1])
        elif num >= 10 and num <21:
            return chiffres.get(num_str)
        else:
            pre_int = int(num_str[0]) * 10
            pre = chiffres.get(str(pre_int))
            if num_str[1] != '0':
                suf = chiffres.get(num_str[1])
            else:
                suf = ''
                mid = ''
            if num_str[0] == '7' and num > 70:
                pre = chiffres.get('60')
                suf_int = int(num_str[1]) + 10
                suf = chiffres.get(str(suf_int))
            if num_str[0] == '9' and num > 90:
                pre = chiffres.get('80')
                suf_int = int(num_str[1]) + 10
                suf = chiffres.get(str(suf_int))
            if suf == 'un' or num == 71:
                mid = '-et-'
            else:
                mid = '-'
            return '{}{}{}'.format(pre, mid, suf)

    def centaine(num, num_str):
        if num < 100:
            if num_str[0] == '0':
                num_str = num_str[1:]
            return dizaine(num, num_str)
        else:
            mid = 'cent'
            if num_str[0] == '1':
                pre = ''
            else:
                pre = chiffres.get(num_str[0]) + '-'
            if num_str[1:3] == '00':
                suf = ''
            else:
                mid = mid + '-'
                unit = int(num_str[0]) * 100
                reste = num%unit
                suf = dizaine(reste, num_str[1:3])
            return '{}{}{}'.format(pre, mid, suf)

    def millier(num, num_str):
        if num < 1000:
            if num_str[:2] == '00':
                num_str = num_str[2:]
            if num_str[:1] == '0':
                num_str = num_str[1:]
            return centaine(num, num_str)
        else:
            mid = 'mille'
            if num_str[0] == '1':
                pre = ''
            else:
                pre = chiffres.get(num_str[0]) + '-'
            if num_str[1:] == '000':
                suf = ''
            else:
                mid = mid + '-'
                unit = int(num_str[0]) * 1000
                reste = num%unit
                suf = centaine(reste, num_str[1:])
            return '{}{}{}'.format(pre, mid, suf)

    def dix_millier(num, num_str):
        pre = dizaine(int(num_str[:2]), num_str[:2])
        pre = pre + '-mille'
        if num_str[2:] == '000':
            suf = ''
        else:
            pre = pre + '-'
            suf = centaine(int(num_str[2:]), num_str[2:])
        return '{}{}'.format(pre,suf)

    def cent_millier(num, num_str):
        pre = int(num_str[:3])
        pre_str = num_str[:3]
        mid = '-mille-'
        if num_str[3:] == '000':
            mid = '-mille'
            suf = ''
        else:
            suf = int(num_str[3:])
            suf_str = num_str[3:]
            suf = centaine(suf, suf_str)
        return '{}{}{}'.format(centaine(pre, pre_str), mid, suf)

    def million(num, num_str):
        pre = num_str[0]
        pre = chiffres.get(pre)
        if pre == 'un':
            mid = ' million '
        else:
            mid = ' millions '
        suf = int(num_str[1:])
        suf_str = num_str[1:]
        if suf_str == '000000':
            mid = mid[:-1]
            return '{}{}'.format(pre, mid)
        if suf_str[0:3] == '000':
            suf = centaine(suf, suf_str[3:])
            return '{}{}{}'.format(pre, mid, suf)
        else:
            suf = cent_millier(suf, suf_str)
            return '{}{}{}'.format(pre, mid, suf)

    try:
        num = int(num)
        num_str = str(num)
        places = int(len(num_str))

        if num < 1 or num > 9999999:
            raise ValueError
        elif places == 1:
            name = chiffres.get(num_str)
        elif places == 2:
            name = dizaine(num, num_str)
        elif places == 3:
            name = centaine(num, num_str)
        elif places == 4:
            name = millier(num, num_str)
        elif places == 5:
            name = dix_millier(num, num_str)
        elif places == 6:
            name = cent_millier(num, num_str)
        elif places == 7:
            name = million(num, num_str)

        print(name.capitalize())

    except ValueError:
        print('Oops! Mauvais nombre. Recommencez...')

def spell_number():
    def clean_str(num_str):
        num_str = num_str.replace(' ', '')
        num_str = num_str.replace(',', '')
        num_str = num_str.replace('.', '')
        return num_str
    num = input('Entrez un nombre entre 1 et 9999999 : ')
    num_to_french(clean_str(num))

spell_number()

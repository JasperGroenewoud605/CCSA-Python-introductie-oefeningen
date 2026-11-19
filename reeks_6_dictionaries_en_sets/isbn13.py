def geldig(code):
    if len(code) != 13:
        return False
    o, e = 0, 0 
    for i in range(0, 11, 2):
        o += int(code[i])
    for i in range(1, 12, 2):
        e += int(code[i])
    if int(code[12]) == (10 - (o + (3*e)) % 10)% 10:
        return True
    else:
        return False

def overzicht(lijst_van_codes):
    overzicht_dict = {naam: [] for naam in ['Engelstalige landen', 'Franstalige landen', 'Duitstalige landen',
           'Japan', 'Russischtalige landen', 'China', 'Overige landen', 'Fouten']}
    
    for code in dict.fromkeys(lijst_van_codes):
        startcode = int(str(code[:3]))
        if not geldig(code) or startcode not in (978, 979):
            overzicht_dict['Fouten'].append(code)
            continue
        groepsid = int(code[3])
        match groepsid:
            case 0 | 1:
                overzicht_dict['Engelstalige landen'].append(code)
            case 2:
                overzicht_dict['Franstalige landen'].append(code)
            case 3:
                overzicht_dict['Duitstalige landen'].append(code)
            case 4:
                overzicht_dict['Japan'].append(code)
            case 5:
                overzicht_dict['Russischtalige landen'].append(code)
            case 7:
                overzicht_dict['China'].append(code)
            case 6 | 8 | 9:
                overzicht_dict['Overige landen'].append(code)
    for registratiegroep in overzicht_dict:
        print(f'{registratiegroep}: {len(overzicht_dict[registratiegroep])}')



codes = [
    '9789743159664', '9785301556616', '9797668174969', '9781787559554',
    '9780817481461', '9785130738708', '9798810365062', '9795345206033', 
    '9792361848797', '9785197570819', '9786922535370', '9791978044523', 
    '9796357284378', '9792982208529', '9793509549576', '9787954527409', 
    '9797566046955', '9785239955499', '9787769276051', '9789910855708', 
    '9783807934891', '9788337967876', '9786509441823', '9795400240705', 
    '9787509152157', '9791478081103', '9780488170969', '9795755809220', 
    '9793546666847', '9792322242176', '9782582638543', '9795919445653', 
    '9796783939729', '9782384928398', '9787590220100', '9797422143460', 
    '9798853923096', '9784177414990', '9799562126426', '9794732912038', 
    '9787184435972', '9794455619207', '9794270312172', '9783811648340', 
    '9799376073039', '9798552650309', '9798485624965', '9780734764010', 
    '9783635963865', '9783246924279', '9797449285853', '9781631746260', 
    '9791853742292', '9781796458336', '9791260591924', '9789367398012']

overzicht(codes)
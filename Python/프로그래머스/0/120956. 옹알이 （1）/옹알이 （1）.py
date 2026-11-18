def solution(babbling):
    speek = [
        "aya", "ye", "woo", "ma",
        "ayaye", "ayawoo", "ayama",
        "yeaya", "yewoo", "yema",
        "wooaya", "wooye", "wooma",
        "maaya", "maye", "mawoo",
        "ayayewoo", "ayayema", "ayawooye", "ayawooma", "ayamaye", "ayamawoo",
        "yeayawoo", "yeayama", "yewooaya", "yewooma", "yemaaya", "yemawoo",
        "wooayaye", "wooayama", "wooyeaya", "wooyema", "woomaaya", "woomaye",
        "maayaye", "maayawoo", "mayeaya", "mayewoo", "mawooaya", "mawooye",
        "ayayewooma", "ayayemawoo", "ayawooyema", "ayawoomaye", "ayamayewoo", "ayamawooye",
        "yeayawooma", "yeayamawoo", "yewooayama", "yewoomaaya", "yemaayawoo", "yemawooaya",
        "wooayayema", "wooayamaye", "wooyeayama", "wooyemaaya", "woomaayaye", "woomayeaya",
        "maayayewoo", "maayawooye", "mayeayawoo", "mayewooaya", "mawooayaye", "mawooyeaya"
    ]
    count = 0
    for b in babbling:
        if b in speek:
            count += 1
    return count
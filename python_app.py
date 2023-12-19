name_dict={"cringe":"iğrenç","lol":"komik bir şeye verilen cevap","rofl":"bir şakaya karşılık cevap"}
while True:
 word=input("kelime sorunuz")
 if word in name_dict.keys():
    print(name_dict[word])
 else:
    print("bu kelime bulunamıyor,lütfen koda ekleyin:")
    anlam=input("anlamını giriniz:")
    name_dict[word]=anlam

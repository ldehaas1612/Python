def lang_genoeg(cm):
    if cm >= 120:
        print("Je bent lang genoeg voor de attractie!")
    else:
        print("Sorry, je bent te klein!")
lang_genoeg(int(input("Vul je lengte in cm in: ")))
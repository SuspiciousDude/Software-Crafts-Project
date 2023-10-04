import random
tips = ['Sprinkle used coffee grounds around your garden to help deter slugs, snails, and ants. The rough texture of the grounds can be irritating to these pests.',
        'Crushed eggshells are an excellent source of calcium for your plants. Scatter them in your garden to provide a calcium boost to plants like tomatoes and peppers.',
        'Mix a few drops of dish soap with water and use it as a natural insect repellent. Spray it on your plants to deter common garden pests like aphids and spider mites.',
        ' Dissolve a tablespoon of Epsom salt in a gallon of water and use it to water your flowering plants. The magnesium in Epsom salt can promote more vibrant blooms.',
        'Banana peels are rich in potassium, which is essential for plant growth and flowering. Chop up banana peels and bury them in the soil around your plants.',
        'Sprinkle ground cinnamon on the soil to help prevent fungal diseases in your garden. It has natural anti-fungal properties.',
        "Sink a small container filled with beer into the ground to attract and drown slugs. They are attracted to the beer's scent and will crawl in and not come out.",
        'Plant certain crops together to help deter pests and improve growth. For example, marigolds can help deter nematodes when planted near tomatoes.',
        "Dip the cut end of plant cuttings in honey before planting them. Honey's natural enzymes can promote root development.",
        "Mix equal parts milk and water and spray it on plants suffering from powdery mildew. The milk's proteins can help combat the mildew"]

usedTips = []

todaysTip = random.choice(tips)
tipIndex = tips.index(todaysTip)

print(f'Your secret tip of the day is ->\n{todaysTip}')

#tips.pop(tips)
tips.pop(tipIndex)
print(tips)
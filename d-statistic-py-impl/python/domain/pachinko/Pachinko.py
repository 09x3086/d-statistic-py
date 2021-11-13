from scipy.special import comb

probability: float = 1 / 319.68

numberOfTrials: int = int(input())

combination: int = comb(numberOfTrials, 1)

px: float = (combination * (probability * 1.0)) * (1.0 - probability) ** (numberOfTrials - 1.0)

print(probability)
print(combination)
print("投資額" + str(1000 * numberOfTrials / 20) + "円")
print("初当たり確率" + str(round(px * 100, 2)) + "%")
print("確変突入率" + str(round((px * (1 / 2)) * 100, 2)) + "%")

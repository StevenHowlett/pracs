"""

CP1404/CP5632 - Practical

Broken program to determine score status

"""
def main():
    score = float(input("Enter score: "))

    if score < 0 or score > 100:

        print("Invalid score")

    else:
        text = text_for_scores(score)
        print (text)

def text_for_scores(score):
    if score >= 90:

        text = "Excellent"

    elif score >= 50:

        text = "Passable"

    else:

        text = "Bad"
    return text
main()
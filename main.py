def main():
    print("This program converts Naira to US dollars")
    print()

    naira = eval(input("Enter amount in naira: "))

    dollars = convert_to_dollars(naira)

    print("That is", dollars, "US dollars.")


convert_to_dollars = lambda naira: naira * 0.002210

main()
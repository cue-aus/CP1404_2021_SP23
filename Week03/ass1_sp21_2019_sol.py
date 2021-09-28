__author__ = 'Cue'

# Initialize the constants
COUNTRIES = ['USA', 'EURO', 'UNITED KINGDOM', 'CHINA', 'INDIA', 'JAPAN', 'SINGAPORE']
CURRENCY_CODES = ['USD', 'EUR', 'GBP', 'CNY', 'INR', 'JPY', 'SGD']
BUY_RATES = [0.7662, 0.7178, 0.4940, 4.7680, 56.0820, 100.4600, 1.1420]
SELL_RATES = [0.6965, 0.6346, 0.4463, 4.2459, 42.9885, 86.0200, 0.9540]
SELL_FEE_RATE = 0.0025

def main():
    # Welcome message
    print("\nWelcome to CP5632 Foreign Exchange Calculator")
    print("Written by Cue Nguyen")

    no_of_countries = len(COUNTRIES)
    again = 'y'

    while again != 'n':

        # Get requested currency
        requested_money_type = input('\nPlease enter your requested currency (a=Australia, f=Foreign): ')
        requested_money_type = requested_money_type.lower()

        # Display a list of countries to choose
        print("\nCurrency")
        print("========")
        for i in range(no_of_countries):
            print(str(i+1) + ". " +  COUNTRIES[i])
        print()

        # Get either aud_amount or foreign_amount
        aud_amount = 0.0
        foreign_amount = 0.0
        if requested_money_type == 'f':
            option = int(input("Please enter 1-7 for your requested currency: "))
            aud_amount = float(input('Please enter your AUD amount: '))
            aud_amount = round(aud_amount,2)
        else:
            option = int(input("Please enter 1-7 for your currency: "))
            foreign_amount = float(input('Please enter your ' + CURRENCY_CODES[option - 1] + ' amount: '))
            foreign_amount = round(foreign_amount,2)

        # Calculate the transaction fee, received amount and display results
        trans_fee = 0.0
        print("\nResult")
        print("======")

        if requested_money_type == 'f':

            if aud_amount <= 2000.0:
                trans_fee = 5.00
            else:
                trans_fee = round(aud_amount * SELL_FEE_RATE, 2)
            foreign_amount = round((aud_amount - trans_fee) * SELL_RATES[option - 1], 2)

            print("%22s" % 'Amount:', 'AUD', "%.2f" % aud_amount)
            print("%22s" % 'Transaction fee:', 'AUD', "%.2f" % trans_fee)
            print("%22s" % 'Exchange rate:', 'AUD 1', '=', CURRENCY_CODES[option - 1], "%.4f" % SELL_RATES[option - 1])
            print("%22s" % 'Total amount received:', CURRENCY_CODES[option -1], "%.2f" % foreign_amount)

        else:  # requested_money_type = 'a'

            aud_amount = round(foreign_amount / BUY_RATES[option - 1],2)
            trans_fee = 5.00

            print("%22s" % 'Amount:', CURRENCY_CODES[option - 1], "%.2f" % foreign_amount, '=','AUD', "%.2f" % aud_amount)
            print("%22s" % 'Transaction fee:', 'AUD', "%.2f" % trans_fee)
            print("%22s" % 'Exchange rate:', CURRENCY_CODES[option - 1], '1', '=', 'AUD', "%.4f" % (1.0 / BUY_RATES[option - 1]))
            print("%22s" % 'Total amount received:', 'AUD', "%.2f" %(aud_amount - trans_fee))

        again = input("\nAnother transaction (n=no, another key = yes): ")
        again = again.lower()
        # end of while

    print ("Thank you!")
# end of main()

# Start the program
main()
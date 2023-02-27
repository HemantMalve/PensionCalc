# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from datetime import datetime
import locale
from dateutil import relativedelta
from datetime import date
import os

locale.setlocale(locale.LC_ALL, 'en_IN')


def calculate_maturity_amount(principal, interest_rate, time_years, monthly_deposit):
    """Calculates the maturity amount for a monthly recurring deposit with half-yearly interest compounding"""

    # Calculate the monthly interest rate
    monthly_rate = interest_rate / (2 * 100)

    # Calculate the total number of half-yearly periods
    periods = time_years * 2

    # Calculate the interest for each half-yearly period
    interest_period = principal * (monthly_rate * 6)

    # Calculate the maturity amount for each half-yearly period
    maturity_period = 0
    for i in range(periods):
        maturity_period = (maturity_period + monthly_deposit) * (1 + monthly_rate) ** 6

    # Calculate the total maturity amount
    maturity_amount = maturity_period + (interest_period * periods)

    return maturity_amount


def calculate_pension(date_of_joining, pensionable_salary, date_of_birth):
    retirement_age = 58
    date_of_retirement = datetime(date_of_birth.year + retirement_age, date_of_birth.month, date_of_birth.day)
    pensionable_service = (date_of_retirement - date_of_joining).days / 365
    pension_amount = (pensionable_service * pensionable_salary) / 70
    print(f"Retrirement date\t", date_of_retirement.date(), "\npensionable service\t", int(pensionable_service),
          sep=" ")
    return (pension_amount, date_of_retirement)


def calculate_basic_da(pf_contribution, pf_contribution_percentage):
    total_monthly_salary = pf_contribution / (pf_contribution_percentage / 100)
    basic_salary = (pf_contribution / pf_contribution_percentage) * 100
    da = total_monthly_salary - basic_salary
    return (basic_salary, da)


def rupaiya(rs):
    return locale.currency(rs, grouping=True)


def swp(investment_amount, withdrawal_amount, investment_duration, interest_rate):
    # calculate the number of withdrawals
    num_withdrawals = investment_duration // 12

    # calculate the remaining investment value after each withdrawal
    remaining_investment = [investment_amount]

    for i in range(num_withdrawals):
        # calculate the interest earned for the year
        interest_earned = remaining_investment[i] * (interest_rate / 100)

        # calculate the remaining investment after withdrawal and interest earned
        remaining = remaining_investment[i] - withdrawal_amount - interest_earned

        # add the remaining investment to the list
        remaining_investment.append(remaining)

    return remaining_investment


def swp_duration(investment_amount, withdrawal_amount, investment_duration, interest_rate):
    # calculate the number of withdrawals
    num_withdrawals = investment_duration

    # calculate the remaining investment value after each withdrawal
    remaining_investment = investment_amount

    for i in range(num_withdrawals):
        # calculate the interest earned for the year
        if i % 3 == 0 :
            interest_earned = remaining_investment * (interest_rate / 1200)
        else:
            interest_earned = 0

        # calculate the remaining investment after withdrawal and interest earned
        remaining_investment = remaining_investment - withdrawal_amount + interest_earned

        # break the loop if the remaining investment is less than or equal to 0
        if remaining_investment <= 0:
            break
    return i + 1


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print("\033[1mDisclaimer\033[0m: \n--------------------------------------------------------------------------------------------------------")
    print("Operational : \nI have given few default values if you do not enter the it will take default value. Please mind the\n"
          " date format\n"
          "\033[3mCalculation assumptions\033[0m :\n "
          "Pension amount was changed on Oct 2014 before that it was 6500 later it is 15,000 so the  calculation is\n"
          "split between two parts Lets calculate our portion.Thus before Oct 2014 PF contribution was 8.33 of your\n"
          "basic + da (if any) or 541 and after Oct 2014 was 8.33 or max 1250. This is not exact calculation but it\n"
          "is an Aprox calculation. Below assumptions are made to achieve best Aprox amount to take Go/No Go decision\n"
          "for New pension scheme:Below assumptions are made to reduce complexity of calculation or to take less input\n"
          "1. Age of retirement is 58 Years\n"
          "2. Till retirement you will receive same salary as of today\n"
          "3. Your salary before Oct 2014 will be always less then Oct 2014 but not huge difference\n"
          "4. "
          "Fact : \n1. if you opt out new pension scheme that case you will continue to pay 1250\n"
          "2. Your contribution towards pension is 8.33 of your basic+DA or max 1250\n"
          "3. if you out in then calculation is made on half yearly compounding of not paid amount\n"
          "4. SWP is calculated on quarterly compounding basis\n"
          "5. All calculation is done only the changing factors all other facts will remain constant\n"
          "")
while input("Continue (y/n) press enter for y ;) ") != 'n':
    os.system('cls' if os.name == 'nt' else 'clear')
    date_str = input(
        "First PF contribution date (in YYYY-MM-DD format): ") or "2023-01-01"
    datex = datetime.strptime(date_str, "%Y-%m-%d")
    date_of_joining = datex

    date_str = input("Enter a date of birth (in YYYY-MM-DD format): ") or "2000-01-01"
    datex = datetime.strptime(date_str, "%Y-%m-%d")
    date_of_birth = datex
    if date_of_joining.year < date_of_birth.year + 18:
        print("Birth year ", date_of_birth.year, " Date of Joning", date_of_joining.year)
        print(
            "**************** Bhai ma ke pet sehi job chalu kiya kay? ya ki ande se bahar kate hi lag gaye bhai *************")
        exit()

    pf_contribution = input("Please give me your present pf contribution amount ") or "15000"
    pf_contribution = int(pf_contribution)
    if date_of_joining.year  <=2014 and date_of_joining.month <= 10:
        pf_contribution_init = input("Please give me your Oct 2014 pf contribution amount ") or "15000"
        pf_contribution_init = int(pf_contribution_init)
        Before2014 = True
    else:
        Before2014 = False
        pf_contribution_init= 0

    pf_contribution_percentage = input("please share pf % default 12") or 12
    pf_contribution_percentage = float(pf_contribution_percentage)

    if Before2014 :
        basic_salary, da = calculate_basic_da(pf_contribution_init, pf_contribution_percentage)
        inital_pensionable_salary = basic_salary + da
        print("Total Salary Intialy:{: .2f}\t ".format(inital_pensionable_salary))

    basic_salary, da = calculate_basic_da(pf_contribution, pf_contribution_percentage)
    now_pensionable_salary = basic_salary + da
    print("Total Salary Now:{: .2f}\t".format(now_pensionable_salary))

    pension_amount, date_of_ret = calculate_pension(date_of_joining, now_pensionable_salary, date_of_birth)

    if Before2014:
        pension_contry_then = (inital_pensionable_salary ) * 0.08333

    pension_contry_now = (now_pensionable_salary ) * 0.08333


    if Before2014 :
        print("if opt out then 541/Month else Your contribution before Oct 2014 is "+str(rupaiya(pension_contry_then))+"\nIf opt out 1250/Month else after oct 2014 "+str(rupaiya(pension_contry_now)))
        print("Note its NOT PF contribution its pension contribution")
    else:
        print("if opt out then 1250/month else Your contribution towards pension ", rupaiya( pension_contry_now))

    print(f"As per new pension you will get Pension Amount:\t ", int(pension_amount))

    delta = relativedelta.relativedelta( date.fromisoformat("2014-10-01"),date_of_joining)
    mon_befor_Oct14 = delta.years * 12 + delta.months
    mon_befor_Oct14 = 0 if mon_befor_Oct14 <= 0 else mon_befor_Oct14
    delta = relativedelta.relativedelta(date_of_ret, date.fromisoformat("2014-10-01") if date_of_joining.year < date.fromisoformat("2014-10-01").year else  date_of_joining )
    mon_after_Oct14 = delta.years * 12 + delta.months

    if Before2014:
        monthly_excess_then = (pension_contry_then - 541) * mon_befor_Oct14
    else:
        monthly_excess_then = 0

    monthly_excess_now = (pension_contry_now - 1250) * mon_after_Oct14

    total_paid = monthly_excess_then + monthly_excess_now
    x=calculate_maturity_amount(total_paid*6,0.085,35,mon_after_Oct14)

    if Before2014:
        print("Excess amount before Oct 2014:\t", rupaiya(monthly_excess_then))
        print("Excess amount After Oct 2014:\t ", rupaiya(monthly_excess_now), ' Till retirement')
    else:
        print("Excess PF amount paid to Pension account:\t ", rupaiya(monthly_excess_now), 'Till retirement')


    print("Total extra amount we pay till retirement :\t", rupaiya(total_paid),"\nIf not paid you will have excess PF deposited with 8.5% interest",rupaiya(x))


    print("\nNow lets clculate Systematic withdrawal plan (SWP) on your {:.2f} pension amount per month ".format(pension_amount))
    swp_int_str = input("Please provide return rate you want to keep your saved amount from PF : ")
    if swp_int_str:
        swp_int = float(swp_int_str)
    else:
        swp_int = 8.0

    y = swp_duration(x, pension_amount-15000, 420, swp_int)
    print('Systematic Withdrawal Plan (SWP) of Amount '+str(rupaiya(pension_amount))+' -15000 /month will last '+str(y)+' months  if invested '+str(rupaiya(x))+' @ '+str(swp_int)+'% interest rate qtrly compounding')

    if not Before2014:
        print("\n\nSummary: This person was born on "+str(date_of_birth.strftime("%Y-%m-%d"))+" and started his job on "+str(date_of_joining.strftime("%Y-%m-%d"))+" having current salary "+ rupaiya(now_pensionable_salary)+"\n"  
              "is paying PF contribution of "+rupaiya(pf_contribution)+" same amount is contributed by employer, Out of employer contribution 8.33% of salary will go to Pension account\n" 
              "thus he will pay "+rupaiya(pension_contry_now)+" till retirement and "+" will retire on "+str(date_of_ret.strftime("%Y-%m-%d"))+". if opt in else will pay only 1250 and will \n "
              "save in PF account "+rupaiya(pension_contry_now-1250)+" so one will save in total of "+rupaiya(total_paid)+" till retirement in "+str(mon_after_Oct14)+" months and\n"
              "accumulate amount of "+rupaiya(x)+" with 8.5% IR. And later one invest in SWP he will get "+rupaiya(pension_amount)+" pension till " +str(y)+" Month later 15000/Month "
              "")
    else:
        print("\n\nSummary: This person was born on "+str(date_of_birth.strftime("%Y-%m-%d"))+" and started his job on "+str(date_of_joining.strftime("%Y-%m-%d"))+" having current salary "+ rupaiya(now_pensionable_salary)+"\n"
              "on or before Oct 2014 "+rupaiya(inital_pensionable_salary) +
              "is paying now  PF contribution of "+rupaiya(pf_contribution)+ "before " +rupaiya(pf_contribution_init)+
              " same amount is \ncontributed by employer, Out of employer contribution 8.33% of salary will go to Pension accountthus before you had \nto pay "+rupaiya(pension_contry_then)+
              "and now will pay "+rupaiya(pension_contry_now)+" till retirement and "+" will retire on "+str(date_of_ret.strftime("%Y-%m-%d"))+". if opt in else will pay only 1250 and will \n"
              "save in PF account after Oct 2014 "+rupaiya(pension_contry_now-1250)+" and Befor Oct 2014" + rupaiya(pension_contry_then-514) +
                "so one will save in total of "+rupaiya(total_paid)+"\nbefore Oct 2014 "+ str(mon_befor_Oct14)+" month and  "+str(mon_after_Oct14)+" months after Oct 2014 and"
              "accumulate amount of "+rupaiya(x)+" \nwith 8.5% IR. And later one invest in SWP he will get "+rupaiya(pension_amount)+" pension till " +str(y)+" Month later 15000/Month "
              "")


    print("\n\033[5m********************  xxxx---  If happy with results buy a coffee for me on 7447767471 ---xxxx ********************\033[0m\n")

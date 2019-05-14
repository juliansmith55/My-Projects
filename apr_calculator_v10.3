import pandas as pd
from datetime import date, datetime
from dateutil import relativedelta
pd.set_option('display.max_rows', 1000) #display every row in dataframe



#STEP 1:  These are the givens

    #Repayment type
repayment_type = 'interest_only'

    #Interest rate
rate = .10123

    #ACH Discount
ach = .0000

    #n (number of months of repayment)
n = 144

    #Disb1 Amount
disb1 = int(5000)

    #Disb Date 1
disb1_date = '08/22/2017'
disb1_date = date(int(disb1_date[-4:]),int(disb1_date[:2]),int(disb1_date[3:5]))

    #Disb2 Amount
disb2 = int(5000)

    #Disb Date 2
disb2_date = '01/16/2018'
disb2_date = date(int(disb2_date[-4:]),int(disb2_date[:2]),int(disb2_date[3:5]))

    #Date of capitalization / separation from school
date_of_capitalization = '11/18/2021'
date_of_capitalization = date(int(date_of_capitalization[-4:]),int(date_of_capitalization[:2]),int(date_of_capitalization[3:5]))

    #Date of first full principal and interest payment
pmt1_date = '12/18/2021'
pmt1_date = date(int(pmt1_date[-4:]),int(pmt1_date[:2]),int(pmt1_date[3:5]))

    #Date of first interest only payment set
io_pmt_date1 = '08/22/2017' #probably one month after disb1
io_pmt_date1 = date(int(io_pmt_date1[-4:]),int(io_pmt_date1[:2]),int(io_pmt_date1[3:5]))

    #Date of second interest only payment set
io_pmt_date2 = '02/22/2018' #probably one month after disb2
io_pmt_date2 = date(int(io_pmt_date2[-4:]),int(io_pmt_date2[:2]),int(io_pmt_date2[3:5]))


#STEP 2:  Calculations


    #interest rate with ACH
rate_ach = rate - ach

    #days between disb date 1 and disb date 2
deferment_period_1 = (disb2_date - disb1_date).days

    #interest accrued in deferment period 1
if repayment_type != 'interest_only':
    interest_accrued_1 = deferment_period_1 * rate/365 * disb1
elif repayment_type == 'interest_only':
    interest_accrued_1 = 0 #if interest only: all accrued interest is paid during deferment period

    #days between disb date 2 and capitalization
deferment_period_2 = (date_of_capitalization - disb2_date).days

    #interest accuried in deferment period 2
if repayment_type != 'interest_only':
    interest_accrued_2 = deferment_period_2 * rate/365 * (disb1 + disb2)
elif repayment_type == 'interest_only':
    interest_accrued_2 = 0 #if interest only: all accrued interest is paid during deferment period

    #balance upon capitalization
balance_1 = disb1 + disb2 + round(interest_accrued_1,2) + round(interest_accrued_2,2)
balance_upon_separation = balance_1




#STEP 3:   Calculate monthly payment

    #monthly interest rate with ach --- ach is activated at date of first full principal and interest payment
i = (rate_ach/12)
v = 1/(1+i)
annuity_immediate = (1-v**n)/i
pmt_immediate = round(balance_1/annuity_immediate,2)



#STEP 4:   create amortization table and balloon payment

amort_table = [[0, 0, 0, 0, round(balance_1,2)]]


pmt = 0
while pmt < n:

    pmt = pmt+1
    pmt_amount = pmt_immediate
    interest = round(i * balance_1,2)
    pmt_towards_principal = round(pmt_amount - interest, 2)
    balance_1 = round(balance_1 - pmt_towards_principal, 2)

    amort_table.append([pmt, pmt_amount, interest, pmt_towards_principal, balance_1])

balloon_payment = pmt_amount + balance_1




# Step 5 Create Cash Flow table

unit_period = 0
    # columns:  Year | Month | Day | unit_period | Partial_unit_period | Cash_flow | Description

    #first disbursement
cash_flow = [[disb1_date.year, disb1_date.month, disb1_date.day, unit_period, 0, -disb1, "disbursement"]]
       
    #second disbursement
cash_flow.append([disb2_date.year, disb2_date.month, disb2_date.day, relativedelta.relativedelta(disb2_date, disb1_date).years*12 + relativedelta.relativedelta(disb2_date, disb1_date).months, relativedelta.relativedelta(disb2_date, disb1_date).days, -disb2, "disbursement"])
    
    #interest only payment 1
if repayment_type == 'interest_only':
    io_pmt_num = 0
    while io_pmt_num < relativedelta.relativedelta(disb2_date.replace(day=1), disb1_date.replace(day=1)).years*12 + relativedelta.relativedelta(disb2_date.replace(day=1), disb1_date.replace(day=1)).months:


        io_pmt_year = (io_pmt_date1 + relativedelta.relativedelta(months=+io_pmt_num)).year
        io_pmt_month = (io_pmt_date1 + relativedelta.relativedelta(months=+io_pmt_num)).month
        io_pmt_day = (io_pmt_date1 + relativedelta.relativedelta(months=+io_pmt_num)).day


        cash_flow.append([ io_pmt_year
                         , io_pmt_month
                         , io_pmt_day
                         , relativedelta.relativedelta(date(io_pmt_year,io_pmt_month,io_pmt_day), disb1_date).years*12 + relativedelta.relativedelta(date(io_pmt_year,io_pmt_month,io_pmt_day), disb1_date).months
                         , relativedelta.relativedelta(date(io_pmt_year,io_pmt_month,io_pmt_day), disb1_date).days
                         , round(rate/12 * disb1,2)
                         , "interest_payment"])
        io_pmt_num = io_pmt_num + 1

    #interest only payment 2
    io_pmt_num2 = 0
    while io_pmt_num < relativedelta.relativedelta(date_of_capitalization.replace(day=1), disb1_date.replace(day=1)).years*12 + relativedelta.relativedelta(date_of_capitalization.replace(day=1), disb1_date.replace(day=1)).months:


        io_pmt_year = (io_pmt_date2 + relativedelta.relativedelta(months=+io_pmt_num2)).year
        io_pmt_month = (io_pmt_date2 + relativedelta.relativedelta(months=+io_pmt_num2)).month
        io_pmt_day = (io_pmt_date2 + relativedelta.relativedelta(months=+io_pmt_num2)).day


        cash_flow.append([ io_pmt_year
                         , io_pmt_month
                         , io_pmt_day
                         , relativedelta.relativedelta(date(io_pmt_year,io_pmt_month,io_pmt_day), disb1_date).years*12 + relativedelta.relativedelta(date(io_pmt_year,io_pmt_month,io_pmt_day), disb1_date).months
                         , relativedelta.relativedelta(date(io_pmt_year,io_pmt_month,io_pmt_day), disb1_date).days
                         , round(rate/12 * (disb1+disb2),2)
                         , "interest_payment"])
        io_pmt_num = io_pmt_num + 1
        io_pmt_num2 = io_pmt_num2 + 1

    
    #pmt
pmt_num = 0
while pmt_num < n-1:
    
    full_pmt_year = (pmt1_date + relativedelta.relativedelta(months =+ pmt_num)).year
    full_pmt_month = (pmt1_date + relativedelta.relativedelta(months =+ pmt_num)).month
    full_pmt_day = (pmt1_date + relativedelta.relativedelta(months =+ pmt_num)).day
    
    cash_flow.append([ full_pmt_year
                     , full_pmt_month
                     , full_pmt_day
                     , relativedelta.relativedelta(date(full_pmt_year,full_pmt_month,full_pmt_day), disb1_date).years*12 + relativedelta.relativedelta(date(full_pmt_year,full_pmt_month,full_pmt_day), disb1_date).months
                     , relativedelta.relativedelta(date(full_pmt_year,full_pmt_month,full_pmt_day), disb1_date).days
                     , pmt_immediate
                     , "full_payment"])
    pmt_num = pmt_num + 1

    #balloon pmt
full_pmt_year = (pmt1_date + relativedelta.relativedelta(months=+pmt_num)).year
full_pmt_month = (pmt1_date + relativedelta.relativedelta(months=+pmt_num)).month
full_pmt_day = (pmt1_date + relativedelta.relativedelta(months=+pmt_num)).day

cash_flow.append([full_pmt_year
                  , full_pmt_month
                  , full_pmt_day
                  , relativedelta.relativedelta(date(full_pmt_year,full_pmt_month,full_pmt_day), disb1_date).years*12 + relativedelta.relativedelta(date(full_pmt_year,full_pmt_month,full_pmt_day), disb1_date).months 
                  , relativedelta.relativedelta(date(full_pmt_year,full_pmt_month,full_pmt_day), disb1_date).days
                  , balloon_payment
                  , "balloon_payment"])

    
df = pd.DataFrame(cash_flow, columns=['Year','Month','Day','Unit_period','Partial_unit_period', 'Cash_flow', 'Description'])


#STEP 5b: solve for x with newton raphson

x = i/12
diff = 1
count = 0
while abs(diff) >= .000005:
    #f(x)
    df['f_n'] = df['Cash_flow']/((1+(df['Partial_unit_period']/30)*x)*(1+x)**df['Unit_period'])
    #f'(x)

                       # new derivative formula -n*(1+i)^(-n-1)/(1+if/30) - f*(1+i)^-n/30*(1+if/30)^2
                            # n = unit period
                            # f = days between disb1 day of month and cashflow(n) day of month
                            # i = x [rate we're trying to find]
    
    df['f_n_deriv'] = df['Cash_flow']*(-df['Unit_period'])*(1+x)**(-df['Unit_period']-1)/(1+x*df['Partial_unit_period']/30) - df['Partial_unit_period']*(1+x)**(-df['Unit_period'])/(30*(1+x*df['Partial_unit_period']/30)**2)

    f_n_sum = df['f_n'].sum()
    f_n_deriv_sum = df['f_n_deriv'].sum()

    xn = x - f_n_sum/f_n_deriv_sum
    diff = xn - x
    x = xn
    count = count + 1



APR = round(x * 12 * 100,3)


print("Repayment type:                     " + str(repayment_type))
print("Balance upon separation:            " + str(balance_upon_separation))
print("Full p/i payment:                   " + str(pmt_immediate))
print("Annual Percentage Rate:             " + str(APR))
print("It took " + str(count) + " iterations to calculate the APR.")
print("Below is the DCF table:")
df.sort_values(['Unit_period','Partial_unit_period']).reset_index(drop=True)


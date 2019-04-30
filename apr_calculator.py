
#apr_calculator


import pandas as pd
from datetime import date
from datetime import datetime
from dateutil import relativedelta




#STEP 1:  These are the givens

    #Repayment type
repayment_type = 'deferred'

    #Interest rate
rate = .06

    #ACH Discount
ach = .0000

    #n (number of months of repayment)
n = 84

    #Disb1 Amount
disb1 = int(5000)

    #Disb Date 1
disb1_date = '06/21/2019'
disb1_date = date(int(disb1_date[-4:]),int(disb1_date[:2]),int(disb1_date[3:5]))

    #Disb2 Amount
disb2 = int(5000)
    
    #Disb Date 2
disb2_date = '09/21/2019'
disb2_date = date(int(disb2_date[-4:]),int(disb2_date[:2]),int(disb2_date[3:5]))
    
    #Date of capitalization
date_of_capitalization = '09/21/2023'
date_of_capitalization = date(int(date_of_capitalization[-4:]),int(date_of_capitalization[:2]),int(date_of_capitalization[3:5]))
    
    #Date of first payment
pmt1_date = '10/21/2023'
pmt1_date = date(int(pmt1_date[-4:]),int(pmt1_date[:2]),int(pmt1_date[3:5]))






#STEP 2:   These are the initial calculations we need to make
    #Deferment period
difference = relativedelta.relativedelta(date_of_capitalization,disb1_date)
months_deferred = difference.years*12 + difference.months

    #interest rate with ACH
rate_ach = rate - ach
    
    #days between disb date 1 and disb date 2
deferment_period_1 = (disb2_date - disb1_date).days
    
    #interst accrued in deferment period 1
interest_accrued_1 = deferment_period_1 * rate/365 * disb1
    
    #days between disb date 2 and capitalization
deferment_period_2 = (date_of_capitalization - disb2_date).days

    #interest accuried in deferment period 2
interest_accrued_2 = deferment_period_2 * rate/365 * (disb1 + disb2)
    
    #balance upon capitalization
balance_1 = disb1 + disb2 + round(interest_accrued_1,2) + round(interest_accrued_2,2)






#STEP 3:   Calculate monthly payment

    #monthly interest rate with ach --- ach is activated at date of first full principal and interest payment
i = (rate_ach/12)
v = 1/(1+i)
annuity_immediate = (1-v**n)/i
pmt_immediate = round(balance_1/annuity_immediate,2)






#STEP 4:   create amortization table

amort_table = [[0, 0, 0, 0, round(balance_1,2)]]

pmt = 0
while pmt < n:

    pmt = pmt+1
    pmt_amount = pmt_immediate
    interest = round(i * balance_1,2)
    pmt_towards_principal = round(pmt_amount - interest,2)
    balance_1 = round(balance_1 - pmt_towards_principal,2)
    
    amort_table.append([pmt, pmt_amount, interest, pmt_towards_principal, balance_1])
    
#balloon payment
amort_table.append([pmt, pmt_amount+balance_1, interest, pmt_amount+balance_1-interest, 0])


df = pd.DataFrame(amort_table, columns=['PMT_Number', 'PMT_Amount', 'Interest', 'PMT_towards_principal', 'Principal'])
df = df[((df.PMT_Number != n) | (df.PMT_Amount != pmt_amount))]
df.reset_index(inplace=True,drop=True)




#STEP 5: APR Calculation

difference = relativedelta.relativedelta(disb2_date,disb1_date)
disb2_unit_period = difference.months


cash_flow = [[0,disb1_date.day, -disb1],
             [disb2_unit_period,disb2_date.day, -disb2]]

PMT_Number = 0
while PMT_Number < n:
    months_deferred = months_deferred + 1
    PMT_Number = PMT_Number + 1
    PMT_Amount = df.iloc[PMT_Number,df.columns.get_loc('PMT_Amount')]
    cash_flow.append([months_deferred, pmt1_date.day, PMT_Amount])

    
df2 = pd.DataFrame(cash_flow, columns=['Unit_period','Day_of_month','Cash_flow'])


#solve for x with newton raphson

x = i/12
diff = 1
count = 0
while abs(diff) >= .000000005:
    #f(x)
    df2['f_n'] = df2['Cash_flow']/((1+((df2['Day_of_month']-disb1_date.day)/30)*x)*(1+x)**df2['Unit_period'])
    #f'(x)
    df2['f_n_deriv'] = df2['Cash_flow']*(-30*(((df2['Unit_period']+1)*(df2['Day_of_month']-disb1_date.day)*x)+30*df2['Unit_period']+(df2['Day_of_month']-disb1_date.day))/(((df2['Day_of_month']-disb1_date.day)*x+30)**2*(1+x**(df2['Unit_period']+1))))
    
    f_n_sum = df2['f_n'].sum()
    f_n_deriv_sum = df2['f_n_deriv'].sum()
    
    xn = x - f_n_sum/f_n_deriv_sum
    diff = xn - x
    x = xn
    count = count + 1

    
    
APR = round(x * 12 * 100,3)

print(APR, count)

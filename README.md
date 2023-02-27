# PensionCalc
This Project help Indian employees to Calculate pension and amount that will be deducted from PF accumulated account. If not opted, then how the future SWP will work for them. 

Disclaimer: 
--------------------------------------------------------------------------------------------------------
Operational : 
I have given few default values if you do not enter the it will take default value. Please mind the
 date format
Calculation assumptions :
 Pension amount was changed on Oct 2014 before that it was 6500 later it is 15,000 so the  calculation is
split between two parts Lets calculate our portion.Thus before Oct 2014 PF contribution was 8.33 of your
basic + da (if any) or 541 and after Oct 2014 was 8.33 or max 1250. This is not exact calculation but it
is an Aprox calculation. Below assumptions are made to achieve best Aprox amount to take Go/No Go decision
for New pension scheme:Below assumptions are made to reduce complexity of calculation or to take less input
1. Age of retirement is 58 Years
2. Till retirement you will receive same salary as of today
3. Your salary before Oct 2014 will be always less then Oct 2014 but not huge difference

Fact : 
1. if you opt out new pension scheme that case you will continue to pay 1250
2. Your contribution towards pension is 8.33 of your basic+DA or max 1250
3. if you out in then calculation is made on half yearly compounding of not paid amount
4. SWP is calculated on quarterly compounding basis
5. All calculation is done only the changing factors all other facts will remain constant

Error hendeling:
I have not wirtten any code for error handelling and much of the data quality check for input data is not done its just a basic calculator to give a high level understanding

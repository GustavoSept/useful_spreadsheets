# What is this repository?
This is a personal collection of useful spreadsheets I actually use. They're mostly in Portuguese, but functionalities are pretty straightforward.

_OBS: All values in these spreadsheets were randomly generated, they're for preview purposes only._

Here's breakdown of each spreadsheet purpose and functionalities:

## Household Budget & Costs Sharing
This is spreadsheet provides various stats and charts to visualize how money is being spent on a household.

See 'PTBR_Household Sheet.xlsx' for a preview in excel for this sheet.

Original [Google Sheet link](https://docs.google.com/spreadsheets/d/1R5Y-YtyYPQ8UfNlO88i3_BSQSj7OkC3Ea1Zp0OYaTbI/edit?usp=sharing)

### Features:
- Easy & Straightforward filling process
	- Each entry can store a date, spending type, value, an observation and a payerID.
- A separated sheet just for earnings (with support for multiple income sources)
- The main page serves as a Dashboard, with many stats and charts, for instance:
	- Sum of Monthly Spending
	- Monthly Spending by spending type
	- Central Value for each spending type
	- Standard Deviation (as a % of Central Value)
	- Pie Chart showing each spending type (and which spending is Fixed vs Discritionary)
	- Plots on Total Earnings vs Spending
- A dedicated costs-sharing calculator, with the following features:
	- Automatically fills spending by type, and by person
	- Calculates how much each person earns relative to total household income
		- As a result, each person only spends proportionally to their income.
		- The calculation has support for moving-average, so income fluctuations are accounted for (last 6 months)
	-  There's a built-in accounting system, to allow for liabilities (push a debt to the next month) and transfers between people in the household.
		- Each month, we can see exactly how much (and who) has to pay up to the other person.

### Limitations:
This sheet only supports 2 people. It'd have to receive a considerable amount of editing to support _n_ people in a household.


## Investment Portfolio Guidance
This spreadsheet semi-automates decision-making in portfolio balancing. After set-up, it'll tell exactly which asset class to buy and sell, and by how much.

It works by letting the user configure the proportions for an ideal portfolio and setting a threshold to sell a portion of the asset type (if it appreciates too much). Then, it's just a matter of the user filling the spreadsheet with investments and letting it do the calculations.

See 'Onde Investir Completo_PTBR.xlsx' for a preview in excel for this sheet.

Original [Google Sheet link](https://docs.google.com/spreadsheets/d/168S69ckOY9rqN7M3nANy0LgzVHldvlRLFbf6mjyjb4c/edit?usp=sharing)

### Features:
- Dashboard with a summary of:
	- How much to buy, by investment category (in total)
	- How much to sell, by investment category (in total)
	- How much to buy, by investment category (in proportion to allocation size)
	- Visualization of Current Allocation vs Ideal Allocation
	- Total Wealth, 'Investible' Wealth and Total Invested Wealth
- Set up page, with:
	- Automatic price updating for USDBRL pair, and BTC, ETH and ADA prices.
	- Setting Allocation Size, Liquid Wealth, Emergency Reserve
	- In-depth detailing of how much money is allocated to each investment type
	- Setting ideal proportion for each category (Fixed Income, Variable Income, Crypto), and also for each sub-category.
	- Setting Threshold parameter: the higher the threshold, the more an asset type needs to appreciate before we need to sell.
		- This parameter is essentially a more complicated multiplier. It (intelligently) caps values with diminishing returns. The formula is as follows:
		- ```excel
			= MAX((
					SIN(IdealValue*0,49*PI())+IdealValue*((MIN(ABS(Threshold-2);
					if(Threshold>2;0;2)))+1))/(2+(MIN(ABS(Threshold-2);
							if(Threshold>2;0;2))));
							if(IdealValue<50%; IdealValue+0,03; 0))
			```
		- This monolith formula produces  a linear scaling at first, then smoothly reaches up to 100%. (Which is the maximum. No single asset can occupy more than 100% of the portfolio)
		- ![Plot image of the monolithic formula](https://prnt.sc/3roQg3ZoCuuP)
		- I've actually tried other (simpler) formulas before, such as:
			- ```excel
			  = IF((1-Ideal)*((Risk+Ideal/2-1))+Ideal > MIN((Ideal)+12%,Ideal*1.3*Risk),
					MIN((Ideal)+12%,Ideal*1.3*Risk),
					(1-Ideal)*((Risk+Ideal/2-1))+Ideal)
				```
				- This produces a three-pointed arc (so, it's definitely not smooth)
			- ```excel
			  = (1-ideal)*(Risk-1)+ideal
				```
				- This produces a straight line, that goes from 0+risk to 100. (so, not sophisticated enough).
- Various pages to fill with investment, divided by type of investment.
	- There are 2 fixed income sub-categories

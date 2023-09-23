# 📁 What's Inside This Repository?
Welcome to my personal collection of highly useful spreadsheets that I actively use. Although they are primarily in Portuguese, their functionalities are intuitive and easy to navigate.

📌 Note: All values in these spreadsheets are randomly generated and are solely for preview purposes.

Below, you'll find a detailed breakdown of each spreadsheet, its purpose, and features:

## 🏠 Household Budget & Costs Sharing
This spreadsheet offers a comprehensive insight into household expenses, providing various statistics and visual aids to help you understand where your money is going.

See 'PTBR_Household Sheet.xlsx' for a preview in excel for this sheet.

🔗 Original [Google Sheet link](https://docs.google.com/spreadsheets/d/1R5Y-YtyYPQ8UfNlO88i3_BSQSj7OkC3Ea1Zp0OYaTbI/edit?usp=sharing)

### 🌟 Features:

- **User-Friendly Input:** Add entries with date, spending type, value, notes, and payerID.
- **Earnings Sheet:** A separate tab for recording earnings from multiple sources.
- **Dashboard:** Packed with metrics and charts such as:
	- Total monthly spending
	- Breakdown of monthly expenses by type
	- Central value for each spending category
	- Standard deviation (% of Central Value)
	- Pie chart showcasing fixed vs discretionary spending
	- Graphs comparing total earnings and spending
 - **Cost-Sharing Calculator:**
	 - Auto-fill expenses by type and person.
	 - Determine each person's contribution based on their earnings.
	 - Built-in accounting for liabilities and transfers.
	 - Monthly insights into settlements between members.

### ⚠️ Limitations:

This tool is designed for two people. To accommodate more members, significant modifications would be required.


## 📊 Investment Portfolio Guidance
This spreadsheet semi-automates decision-making in portfolio balancing. After set-up, it'll tell exactly which asset class to buy and sell, and by how much.

It works by letting the user configure the proportions for an ideal portfolio and setting a threshold to sell a portion of the asset type (if it appreciates too much). Then, it's just a matter of the user filling the spreadsheet with investments and letting it do the calculations.

See 'Onde Investir Completo_PTBR.xlsx' for a preview in excel for this sheet.

🔗 Original [Google Sheet link](https://docs.google.com/spreadsheets/d/168S69ckOY9rqN7M3nANy0LgzVHldvlRLFbf6mjyjb4c/edit?usp=sharing)

### 🌟 Features:
- **Dashboard with a summary of**:
	- How much to buy, by investment category (in total)
	- How much to sell, by investment category (in total)
	- How much to buy, by investment category (in proportion to allocation size)
	- Visualization of Current Allocation vs Ideal Allocation
	- Total Wealth, 'Investible' Wealth and Total Invested Wealth
- **Set up page, with**:
	- Automatic price updating for USDBRL pair, and BTC, ETH and ADA prices.
	- Setting Allocation Size, Liquid Wealth, Emergency Reserve
	- In-depth detailing of how much money is allocated to each investment type
	- Setting ideal proportion for each category (Fixed Income, Variable Income, Crypto), and also for each sub-category.
	- Setting Threshold parameter: the higher the threshold, the more an asset type needs to appreciate before we need to sell.
		- This parameter is essentially a more complicated multiplier. It (intelligently) caps values with diminishing returns. The formula is as follows:
		- ```python
			= MAX((
					SIN(IdealValue*0,49*PI())+IdealValue*((MIN(ABS(Threshold-2);
					if(Threshold>2;0;2)))+1))/(2+(MIN(ABS(Threshold-2);
							if(Threshold>2;0;2))));
							if(IdealValue<50%; IdealValue+0,03; 0))
			```
		- This monolith formula produces  a linear scaling at first, then smoothly reaches up to 100%. (Which is the maximum. No single asset can occupy more than 100% of the portfolio)
		- ![Plot image of the monolithic formula](https://i.imgur.com/AYr0eZD.jpg)
		- The reason I've designed the formula like this is so that any Ideal value will output a sensible Threshold that makes sense. More on that later.
  			- The linear beginning means that we 'protect' low-values from scaling too rapidly (see why that's an issue on the third formula).
     			- Extremely high-values suffer less from slow-scaling (~95% Ideal results in ~97.2% Threshold).
		- I've actually tried other (simpler) formulas before, such as:
			- ```python
			  = IF((1-Ideal)*((Risk+Ideal/2-1))+Ideal > MIN((Ideal)+12%,Ideal*1.3*Risk),
					MIN((Ideal)+12%,Ideal*1.3*Risk),
					(1-Ideal)*((Risk+Ideal/2-1))+Ideal)
				```
				- This produces a three-pointed arc
    				- ![Plot of the intermediate formula](https://i.imgur.com/VYxOXRd.jpg)
        			- This formula is a step in the right direction, but it has weird turning points in the scaling (which is too arbitrary for this purpose). Essentially, the newer formula above is a reworked version of this idea, with smoothing after a certain point.
			- ```python
			  = (1-ideal)*(Risk-1)+ideal
				```
				- This produces a straight line, that goes from 0+risk to 100. (so, not sophisticated enough).
    				- ![Plot of the simplest formula](https://i.imgur.com/TxGwiv4.jpg)
          			- This formula works well for middle-values, but if we choose a low Ideal value (say, 5%) for any investment type, we'll have to double/triple our investment before having to sell. Also, high values (~95%) produce odd scaling (threshold would be set at ~95.5%). Not ideal. In practice, extremely high values aren't practical for investment portfolios, but I wanted to support any type of strategy, including the ones that invested +95% into a single category (or sub-category within a category).
- Various pages to fill with investment, divided by type of investment.
	- There are 2 fixed income sub-categories: private company bonds (essentially Debentures), and the rest (treasury, bank-based bonds).
 		- These pages support adding dates, to plot a chart of when bonds expire. And a pie plot to check which specific investments there are, by value. 
	- There are 2 (standard) variable income sub-categories: National and International
 		- Support the same pie chart from above. There's an additional 'results' column, to make it easier to see how much in profit/loss each investment is.
	- There are 3 crypto projects specified (One could easily swap them, or simply ignore them): BTC, ETH and ADA.
 		- These pages calculates average purchasing price of the asset
		- There's also a feature to dynamically calculate each quartile by quantity and average price
  			- The interesting part is that it takes into account any sale you may have done, and automatically sells the most expensive purchases first.
     			- Calculations for this step are not that trivial (at least in spreadsheets without scripting), see hidden columns from H through S.
        		- This quartile calculation makes it much easier to file taxes in certain countries.
          		- It can be used as a stand-alone page to calculate any variable income asset, not just crypto.
### ⚠️ Limitations:
While this tool aids in portfolio balancing and provides "exit" strategies, it doesn't evaluate the viability of specific investments. Ensure to review the performance and fundamentals of your assets periodically.



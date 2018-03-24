import pandas as pd

'''
Search unemployment data by state for counties with
unemployment rates greater than or equal to X,
less than X,
or between X and Y.
Find counties with highest unemployment rates, by a specified state.
'''

#Open CSV file, create dataframe:
file = pd.read_csv('cleaned_laucnty16.csv')
df = pd.DataFrame(file)

#The search functions:
def count_unemp_greater_equal(number):
	'''
	Number of counties, by state, that have unemployment rates greater than or equal to X.
	'''
	greaterdf = df[df['unemp_rate'] >= number]['state'].value_counts()
	print(greaterdf)

def count_unemp_less_than(number):
	'''
	Number of counties, by state, that have unemployment rates less than or equal to X.
	'''
	lessdf = df[df['unemp_rate'] <number]['state'].value_counts()
	print(lessdf)

def count_unemp_between(low, high):
	'''
	Number of counties, by state, with unemployment rates in a certain range.
	'''
	btwndf = df[(df['unemp_rate'] >low) & (df['unemp_rate'] < high)]['state'].value_counts()
	print(btwndf)

def highest_unemp(ST,num):
	'''
	highest_unemp(AZ,10) yields the top ten counties in Arizona with the highest unemployment rates.
	To instead exclude a state or territory: df[(df['state'] != ST)]....
	'''
	statedf = (df[(df['state'] == ST)].sort_values('unemp_rate', ascending=False).head(num))
	print(statedf[['state','county','labor_force','num_employed','num_unemployed','unemp_rate']])

#Examples of use:

#Number of counties, by state, with unemployment rates greater than or equal to:
greaterthan = 10 #integer
print('These many counties have unemployment rates greater than or equal to ' + str(greaterthan) + ':')
count_unemp_greater_equal(greaterthan)

#Number of counties, by state, with unemployment rates less than:
lessthan = 4 #integer
print('These many counties have unemployment rates less than ' + str(lessthan) + ':')
count_unemp_less_than(lessthan)

#Number of counties, by state, with unemployment rates between:
low = 5 #integer
high = 8 #integer
print('These many counties have unemployment rates between ' + str(low) + ' and ' + str(high) + ':')
count_unemp_between(low, high)

#Top 15 counties in Michigan with highest unemployment rates:
state = 'MI' #state abbreviation
num_results = 15 #integer
print('The top ' + str(num_results) + ' counties with the highest unemployment rates in ' + state + ':')
highest_unemp(state, num_results)

#Counties with highest unemployment rates across the US, except Puerto Rico:
highest_unemp('PR',10)
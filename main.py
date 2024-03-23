import urllib.request
from bs4 import BeautifulSoup

# What year?
year = 2011

# Create/open a file called wunder.txt
f = open('wunder-data-' + str(year) + '.txt', 'w')
f.write('datestamp,tmean,tmax,tmin,precip,dewpoint\n')

# Iterate through months and days
for m in range(1, 13):
    for d in range(1, 32):

        # Check if already gone through month
        if (m == 2 and d > 28):
            break
        elif (m in [4, 6, 9, 11] and d > 30):
            break

        # Open wunderground.com url
        datestamp = str(year) + '-' + str(m) + '-' + str(d)
        print('Getting data for ' + datestamp)
        url = 'https://www.wunderground.com/history/daily/us/ca/los-angeles/KLAX/date/' + str(year) + '-' + str(m) + '-' + str(d)

        try:
            page = urllib.request.urlopen(url)
            soup = BeautifulSoup(page, 'html.parser')
        except urllib.error.HTTPError as e:
            if e.code == 404:
                print(f"No data found for {datestamp}")
                continue  # Skip if the page doesn't exist
            else:
                raise

        summary_table = soup.find('div', class_='summary-table')
        if summary_table:
            # Find all table rows
            print(summary_table)
            rows = summary_table.find_all('tr')
            if rows:
            # Ensure there are enough rows
                if len(rows) > 2:  # Check if there are at least 3 rows
                    # Extract average day temperature data from the third row
                    temperature_row = rows[2]  
                    average_temp_cell = temperature_row.find('td')

                    if average_temp_cell:  # Check if the cell exists
                        average_temp = average_temp_cell.text.strip()
                        
                        # Write timestamp and average day temperature to file
                        f.write(datestamp + ',' + average_temp + '\n')
                    else:
                        print(f"No average day temperature data found for {datestamp}")
                else:
                    print(f"Not enough rows in the summary table for {datestamp}")
            else:
                print(f"No rows found in the summary table for {datestamp}")
        else:
            print(f"No summary table found for {datestamp}")
from funct import*



titles=["AMD", "AVGO", "PLAB", "XPER", "MU", "TSM"]
# titles=["CORN", "UGA", "NDAQ", "FB", "RDS-A"]

for i in range(len(titles)):
 
 print("scraping ", titles[i], " stock quotes in action...", end='', flush=True)
 
 # dates management....
 today, date_1, code_1, date_2, code_2 = Dates_man()

 # URL generation for querying web....
 url=urlGenerator(code_1, code_2, titles)

 # web scraping & HTML parsing
 data=scraping(url[i])


 # convert dates from original codes
 code2Dates(date_1, code_1, data)



 # adjust file for better viewing & save final data
 saveResult(today, date_2, titles[i])
 print("done!") 
 
print("\nScarping process fully completed!")
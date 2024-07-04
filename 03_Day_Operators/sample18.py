# Write a script that prompts the user to enter number of years. Calculate the number of seconds a person can live. Assume a person can live hundred years

number_years = int(input("Enter number of years: "))
seconds_per_year = 365 * 24 * 60 * 60
total_seconds = number_years * seconds_per_year

print(f"You have lived for {total_seconds} seconds.")

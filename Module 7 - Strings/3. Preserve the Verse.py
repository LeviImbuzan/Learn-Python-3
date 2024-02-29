# Given string of highlighted poems
highlighted_poems = "Afterimages:Audre Lorde:1997, The Shadow:William Carlos Williams:1915, Ecstasy:Gabriela Mistral:1925, Georgia Dusk:Jean Toomer:1923, Parting Before Daybreak:An Qi:2014, The Untold Want:Walt Whitman:1871, Mr. Grumpledump's Song:Shel Silverstein:2004, Angel Sound Mexico City:Carmen Boullosa:2013, In Love:Kamala Suraiyya:1965, Dream Variations:Langston Hughes:1994, Dreamwood:Adrienne Rich:1987"

# Split the string into a list of individual poems
highlighted_poems_list = highlighted_poems.split(',')

# Strip whitespace from each item in the list
highlighted_poems_stripped = []
for poem in highlighted_poems_list:
    highlighted_poems_stripped.append(poem.strip())

# Split each poem into its title, poet, and date parts
highlighted_poems_details = []
for poem in highlighted_poems_stripped:
    highlighted_poems_details.append(poem.split(':'))

# Print the details of each poem
titles = []
poets = []
dates = []

for item in highlighted_poems_details:
    titles.append(item[0])
    poets.append(item[1])
    dates.append(item[2])

# Print out the details of each poem
for i in range(0, len(highlighted_poems_details)):
    print('The poem "{}" was published by {} in {}'.format(titles[i], poets[i], dates[i]))

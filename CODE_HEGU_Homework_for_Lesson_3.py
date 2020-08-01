## Homework 3
## Author: Ana He Gu
## Date: 27th February 2020 


'''
Intro | 
'''
In [1]: import pandas as pd                                                                                                                                                             
In [2]: import numpy as np   

In [3]: hwdata_df = pd.read_csv('https://raw.githubusercontent.com/fivethirtyeight/data/master/biopics/biopics.csv', encoding = "ISO-8859-1")                                           
In [4]: hwdata_df.head()                                                                                                                                                                
Out[4]: 
                 title                                  site country  year_release box_office  ... race_known      subject_race person_of_color subject_sex    lead_actor_actress
0  10 Rillington Place  http://www.imdb.com/title/tt0066730/      UK          1971          -  ...    Unknown               NaN               0        Male  Richard Attenborough
1     12 Years a Slave  http://www.imdb.com/title/tt2024544/   US/UK          2013     $56.7M  ...      Known  African American               1        Male      Chiwetel Ejiofor
2            127 Hours  http://www.imdb.com/title/tt1542344/   US/UK          2010     $18.3M  ...    Unknown               NaN               0        Male          James Franco
3                 1987  http://www.imdb.com/title/tt2833074/  Canada          2014          -  ...      Known             White               0        Male     Jean-Carl Boucher
4             20 Dates  http://www.imdb.com/title/tt0138987/      US          1998      $537K  ...    Unknown               NaN               0        Male       Myles Berkowitz
[5 rows x 14 columns]
In [5]: hwdata_df.tail()                                                                                                                                                                
Out[5]: 
                     title                                  site country  year_release box_office  ... race_known  subject_race person_of_color subject_sex lead_actor_actress
756  Young Man with a Horn  http://www.imdb.com/title/tt0043153/      US          1950          -  ...      Known         White               0        Male       Kirk Douglas
757      Young Mr. Lincoln  http://www.imdb.com/title/tt0032155/      US          1939          -  ...      Known         White               0        Male        Henry Fonda
758       Young Tom Edison  http://www.imdb.com/title/tt0033289/      US          1940          -  ...      Known         White               0        Male      Mickey Rooney
759          Young Winston  http://www.imdb.com/title/tt0069528/      US          1972          -  ...      Known         White               0        Male         Simon Ward
760    Your Cheatin' Heart  http://www.imdb.com/title/tt0058765/      US          1964          -  ...    Unknown           NaN               0        Male    George Hamilton
[5 rows x 14 columns]

In [6]: hwdata_df.describe()                                                                                                                                                            
Out[6]: 
       year_release  number_of_subjects  person_of_color
count    761.000000          761.000000       761.000000
mean    1986.935611            1.268068         0.131406
std       24.039547            0.561148         0.338066
min     1915.000000            1.000000         0.000000
25%     1969.000000            1.000000         0.000000
50%     1995.000000            1.000000         0.000000
75%     2007.000000            1.000000         0.000000
max     2014.000000            4.000000         1.000000

In [7]: hwdata_df.dtypes                                                                                                                                                                
Out[7]: 
title                 object
site                  object
country               object
year_release           int64
box_office            object
director              object
number_of_subjects     int64
subject               object
type_of_subject       object
race_known            object
subject_race          object
person_of_color        int64
subject_sex           object
lead_actor_actress    object
dtype: object



'''
Problem 1 | 
'''
In [8]: hwdata_df.rename(columns={"country":"Count"}, inplace=True)                                                                                                                     
In [9]: hwdata_df[hwdata_df.year_release>2000].groupby("Count").agg({"Count":["count"]}).reset_index()                                                                              
Out[9]: 
          Count      
                count
0        Canada    14
1     Canada/UK     8
2            UK    58
3            US   169
4     US/Canada    10
5         US/UK    46
6  US/UK/Canada     2


# I started my renaming country as "Count" 		    #
# On the following code, I picked year of release   #
# after 1999 (not included), then grouped them by   #
# newly named "Count" and lastly, summed the number #
# of films by "Count" (country)						#

'''
Problem 2 | Paste Code Below
'''
# Part (a)
In [11]: hwdata_df[hwdata_df.year_release>2000].groupby("type_of_subject").agg({"type_of_subject":["count"]}).reset_index().sort_values([('type_of_subject', 'count')], ascending=Fa
    ...: lse)                                                                                                                                                                       
Out[11]: 
       type_of_subject      
                       count
19               Other    67
6              Athlete    39
11            Criminal    35
18            Musician    31
13          Historical    20
1             Activist    14
17            Military    12
5               Artist    12
0             Academic    11
8               Author    11
15               Media     9
2                Actor     9
20              Singer     8
9        Author (poet)     7
21        World leader     7
3              Actress     5
12          Government     3
14          Journalist     2
16            Medicine     2
10            Comedian     1
7   Athlete / military     1
4             Actress      1

# Part (b)
In [12]: hwdata_df[hwdata_df.year_release<2001].groupby("type_of_subject").agg({"type_of_subject":["count"]}).reset_index().sort_values([('type_of_subject', 'count')], ascending=Fa
    ...: lse)                                                                                                                                                                       
Out[12]: 
           type_of_subject      
                           count
19                   Other    92
13              Historical    56
11                Criminal    46
18                Musician    45
7                  Athlete    35
8                   Author    34
16                Military    33
2                 Activist    17
6                   Artist    17
21                  Singer    12
4                  Actress    11
0                 Academic    10
23            World leader    10
15                Medicine     7
14                   Media     6
10                Comedian     6
9            Author (poet)     6
3                    Actor     5
1   Academic (Philosopher)     1
17     Military / activist     1
5       Actress / activist     1
20              Politician     1
22                 Teacher     1
12              Government     1


# I started by grouping the movies by type, on the  #
# first code analyzing the movies after 2000 and on #
# on the second one using movies before 2000.       #
# I used the sort_values method to see which types  #
# of movies were trending according to the time 	#
# range. Disregarding the "other" category, we can  #
# observe that before 2000, historical, musician, 	#
# and criminal movies were in high demand. On the   #
# other hand, after 2000 athlete, criminal and 		#
# musician became the most produced movie types. 	#
# In both time ranges we have musician and criminal #
# on the top, but as time went on athlete movies 	#
# were given preference over historical movies.		#

'''
Problem 3 | Paste Code Below
'''
In [13]: hwdata_df.rename(columns={"number_of_subjects":"mean_num_of_subjects"}, inplace=True)                                                                                      
In [14]: hwdata_df[hwdata_df.year_release>1980].groupby("year_release").agg({"mean_num_of_subjects":["mean"]}).reset_index()                                                        
Out[14]: 
   year_release mean_num_of_subjects
                                mean
0          1981             1.250000
1          1982             1.000000
2          1983             1.000000
3          1984             1.666667
4          1985             1.000000
5          1986             1.333333
6          1987             1.444444
7          1988             1.000000
8          1989             1.166667
9          1990             1.923077
10         1991             1.400000
11         1992             1.333333
12         1993             1.117647
13         1994             1.266667
14         1995             1.375000
15         1996             1.333333
16         1997             1.000000
17         1998             1.250000
18         1999             1.307692
19         2000             1.187500
20         2001             1.090909
21         2002             1.142857
22         2003             1.461538
23         2004             1.000000
24         2005             1.333333
25         2006             1.083333
26         2007             1.214286
27         2008             1.344828
28         2009             1.333333
29         2010             1.608696
30         2011             1.461538
31         2012             1.307692
32         2013             1.333333
33         2014             1.363636


# First, I renamed number_of_subjects to 		       	#
# mean_num_of_subjects. Then group the average 		  #
# number og subjects in movies per year, for years  #
# after 1980.										                    #

'''
Problem 4 | Paste Code Below
'''
In [15]: hwdata_df[(hwdata_df.Count=="Canada")&(hwdata_df.year_release>2000)&(hwdata_df.race_known=="Known")].groupby(["subject_race","year_release"]).agg({"title":["count"]}).rese
    ...: t_index().sort_values([('year_release')], ascending=True)                                                                                                                  
Out[15]: 
       subject_race year_release title
                                 count
2             White         2001     1
3             White         2005     1
4             White         2008     2
1  African American         2010     1
5             White         2010     2
0           African         2011     1
6             White         2013     2
7             White         2014     1


# First, I applied my three conditions        #
# 'Canada', 'after 2000' and 'known race'.    #
# Then I race and year of release. Lastly,    #
# I sorted in chronological order.            #
'''
Problem 5 | Paste Code Below
'''
In [16]: hwdata_df[hwdata_df.year_release>2000].groupby("subject_sex").agg({"subject_sex":["count"]}).reset_index()                                                                 
Out[16]: 
  subject_sex      
              count
0      Female    71
1        Male   236
In [17]: hwdata_df[(hwdata_df.year_release<2001)&(hwdata_df.year_release>1980)].groupby("subject_sex").agg({"subject_sex":["count"]}).reset_index()                                 
Out[17]: 
  subject_sex      
              count
0      Female    47
1        Male   161

In [18]: hwdata_df.head()                                                                                                                                                           
Out[18]: 
                 title                                  site   Count  year_release box_office  ... race_known      subject_race person_of_color subject_sex    lead_actor_actress
0  10 Rillington Place  http://www.imdb.com/title/tt0066730/      UK          1971          -  ...    Unknown               NaN               0        Male  Richard Attenborough
1     12 Years a Slave  http://www.imdb.com/title/tt2024544/   US/UK          2013     $56.7M  ...      Known  African American               1        Male      Chiwetel Ejiofor
2            127 Hours  http://www.imdb.com/title/tt1542344/   US/UK          2010     $18.3M  ...    Unknown               NaN               0        Male          James Franco
3                 1987  http://www.imdb.com/title/tt2833074/  Canada          2014          -  ...      Known             White               0        Male     Jean-Carl Boucher
4             20 Dates  http://www.imdb.com/title/tt0138987/      US          1998      $537K  ...    Unknown               NaN               0        Male       Myles Berkowitz
[5 rows x 14 columns]
In [19]: hwdata_df[hwdata_df.year_release>2000].groupby(["Count","subject_sex"]).agg({"subject_sex":["count"]}).reset_index()                                                       
Out[19]: 
           Count subject_sex      
                             count
0         Canada      Female     2
1         Canada        Male    12
2      Canada/UK      Female     2
3      Canada/UK        Male     6
4             UK      Female    13
5             UK        Male    45
6             US      Female    32
7             US        Male   137
8      US/Canada      Female     4
9      US/Canada        Male     6
10         US/UK      Female    18
11         US/UK        Male    28
12  US/UK/Canada        Male     2

In [20]: hwdata_df[(hwdata_df.year_release<2001)&(hwdata_df.year_release>1980)].groupby(["Count","subject_sex"]).agg({"subject_sex":["count"]}).reset_index()                       
Out[20]: 
       Count subject_sex      
                         count
0     Canada        Male     4
1  Canada/UK        Male     5
2         UK      Female    14
3         UK        Male    37
4         US      Female    24
5         US        Male    93
6  US/Canada      Female     1
7      US/UK      Female     8
8      US/UK        Male    22

# I wanted to see gender differences by country #
# before and after 2000. As we can observe,     #
# the number of actors always surpassed the     #
# number of actresses. There were not actresses #
# at all in Canada between 1980 and 2000        #
# The number increased as time passed           #




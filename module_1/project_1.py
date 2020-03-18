
answer_ls = [] # создадим список с ответами. сюда будем добавлять ответы по мере прохождения теста
# сюда можем вписать создание новых колонок в датасете




1. У какого фильма из списка самый большой бюджет?
Варианты ответов:
The Dark Knight Rises (tt1345836)
Spider-Man 3 (tt0413300)
Avengers: Age of Ultron (tt2395427)
The Warrior's Way (tt1032751)
Pirates of the Caribbean: On Stranger Tides (tt1298650)
In [146]:


# тут вводим ваш ответ и добавлем в его список ответов (сейчас для примера стоит "1")
import pandas as pd
df = pd.read_csv('C:/Users/User/ASUS_neidj/data.csv')
display(df[df.budget == df.budget.max()].original_title)



491    The Warrior's Way
Name: original_title, dtype: object
In [ ]:


answer_ls.append(4)




2. Какой из фильмов самый длительный (в минутах)
The Lord of the Rings: The Return of the King (tt0167260)
Gods and Generals (tt0279111)
King Kong (tt0360717)
Pearl Harbor (tt0213149)
Alexander (tt0346491)
In [145]:


import pandas as pd
df = pd.read_csv('C:/Users/User/ASUS_neidj/data.csv')
display(df[df.runtime == df.runtime.max()].original_title)
​
answer_ls.append(2)



1158    Gods and Generals
Name: original_title, dtype: object

3. Какой из фильмов самый короткий (в минутах)
Варианты ответов:
Home on the Range tt0299172
The Jungle Book 2 tt0283426
Winnie the Pooh tt1449283
Corpse Bride tt0121164
Hoodwinked! tt0443536
In [144]:


import pandas as pd
df = pd.read_csv('C:/Users/User/ASUS_neidj/data.csv')
display(df[df.runtime == df.runtime.min()].original_title)
answer_ls.append(3)



769    Winnie the Pooh
Name: original_title, dtype: object

4. Средняя длительность фильма?
Варианты ответов:
115
110
105
120
100
In [143]:


import pandas as pd
df = pd.read_csv('C:/Users/User/ASUS_neidj/data.csv')
display(df.runtime.mean())
answer_ls.append(2)



109.65343915343915

5. Средняя длительность фильма по медиане?
Варианты ответов:
106
112
101
120
115
In [142]:


import pandas as pd
df = pd.read_csv('C:/Users/User/ASUS_neidj/data.csv')
display(df.runtime.median())
answer_ls.append(1)



106.5

6. Какой самый прибыльный фильм?
Варианты ответов:
The Avengers tt0848228
Minions tt2293640
Star Wars: The Force Awakens tt2488496
Furious 7 tt2820852
Avatar tt0499549
In [141]:


import pandas as pd
df = pd.read_csv('C:/Users/User/ASUS_neidj/data.csv')
df['profit']=df.revenue-df.budget
display(df[df.profit == df.profit.max()].original_title)        
answer_ls.append(5)



239    Avatar
Name: original_title, dtype: object

7. Какой фильм самый убыточный?
Варианты ответов:
Supernova tt0134983
The Warrior's Way tt1032751
Flushed Away tt0424095
The Adventures of Pluto Nash tt0180052
The Lone Ranger tt1210819
In [139]:




import pandas as pd
df = pd.read_csv('C:/Users/User/ASUS_neidj/data.csv')
df['loss']=df.budget-df.revenue
display(df[df.loss == df.loss.max()].original_title)   
answer_ls.append(2)



491    The Warrior's Way
Name: original_title, dtype: object

8. Сколько всего фильмов в прибыли?
Варианты ответов:
1478
1520
1241
1135
1398
In [140]:


import pandas as pd
df = pd.read_csv('C:/Users/User/ASUS_neidj/data.csv')
df['profit']=df.revenue-df.budget
display(len(df[df.profit>0].original_title))
answer_ls.append(1)



1478

9. Самый прибыльный фильм в 2008 году?
Варианты ответов:
Madagascar: Escape 2 Africa tt0479952
Iron Man tt0371746
Kung Fu Panda tt0441773
The Dark Knight tt0468569
Mamma Mia! tt0795421
In [194]:


import pandas as pd
df = pd.read_csv('C:/Users/User/ASUS_neidj/data.csv')
df['profit']=df.revenue-df.budget
max_profit = df[(df.release_year==2008)].profit.max()
display(df[(df.profit == max_profit)].original_title)
answer_ls.append(4)



600    The Dark Knight
Name: original_title, dtype: object

10. Самый убыточный фильм за период с 2012 по 2014 (включительно)?
Варианты ответов:
Winter's Tale tt1837709
Stolen tt1656186
Broken City tt1235522
Upside Down tt1374992
The Lone Ranger tt1210819
In [201]:


import pandas as pd
df = pd.read_csv('C:/Users/User/ASUS_neidj/data.csv')
df['loss']=df.budget-df.revenue
max_loss = df[((df.release_year>=2012) & (df.release_year<=2014))].loss.max()
display(df[(df.loss == max_loss)].original_title)
answer_ls.append(5)



1246    The Lone Ranger
Name: original_title, dtype: object

11. Какого жанра фильмов больше всего?
Варианты ответов:
Action
Adventure
Drama
Comedy
Thriller
In [214]:




import pandas as pd
df = pd.read_csv('C:/Users/User/ASUS_neidj/data.csv')
list_genres = []
for i in df.genres:
    for j in i.split('|'):
        list_genres.append(j)
df1 = pd.Series(list_genres)
​
# print(df1.value_counts())
print(df1.value_counts().index[0])
answer_ls.append(3)



Drama



# 12. Какого жанра среди прибыльных фильмов больше всего?
Варианты ответов:
1. Drama
2. Comedy
3. Action
4. Thriller
5. Adventure

In [215]:




import pandas as pd
df = pd.read_csv('C:/Users/User/ASUS_neidj/data.csv')
df['profit']=df.revenue-df.budget
list_genres = []
for i in df[(df.profit > 0)].genres:
    for j in i.split('|'):
        list_genres.append(j)
df1 = pd.Series(list_genres)
​
# print(df1.value_counts())
print(df1.value_counts().index[0])
answer_ls.append(1)
​



Drama

13. Кто из режиссеров снял больше всего фильмов?
Варианты ответов:
Steven Spielberg
Ridley Scott 
Steven Soderbergh
Christopher Nolan
Clint Eastwood
In [219]:




import pandas as pd
df = pd.read_csv('C:/Users/User/ASUS_neidj/data.csv')
list_director = []
for i in df.director:
    for j in i.split('|'):
        list_director.append(j)
df1 = pd.Series(list_director)
​
# print(df1.value_counts())
print(df1.value_counts().index[0])
answer_ls.append(3)



Steven Soderbergh

14. Кто из режиссеров снял больше всего Прибыльных фильмов?
Варианты ответов:
Steven Soderbergh
Clint Eastwood
Steven Spielberg
Ridley Scott
Christopher Nolan
In [221]:


import pandas as pd
df = pd.read_csv('C:/Users/User/ASUS_neidj/data.csv')
df['profit']=df.revenue-df.budget
list_director = []
for i in df[(df.profit>0)].director:
    for j in i.split('|'):
        list_director.append(j)
df1 = pd.Series(list_director)
​
# print(df1.value_counts())
print(df1.value_counts().index[0])
answer_ls.append(4)



Ridley Scott

15. Кто из режиссеров принес больше всего прибыли?
Варианты ответов:
Steven Spielberg
Christopher Nolan
David Yates
James Cameron
Peter Jackson
In [247]:





import pandas as pd
df = pd.read_csv('C:/Users/User/ASUS_neidj/data.csv')
df['profit']=df.revenue-df.budget
list_director = {}
for index, i_row in df[(df.profit>0)].iterrows(): # перебор по строкам
    for j_director in i_row.director.split('|'):
        if j_director in list_director:
            list_director[j_director]+=i_row.profit
        else:
            list_director[j_director]=i_row.profit
df1 = pd.DataFrame(list_director.items(), columns=['director', 'profit']) #делаем из словаря датафрейм и задаем название колонок
​
display(df1[df1.profit == df1.profit.max()].director) 
​
answer_ls.append(5)



113    Peter Jackson
Name: director, dtype: object

16. Какой актер принес больше всего прибыли?
Варианты ответов:
Emma Watson
Johnny Depp
Michelle Rodriguez
Orlando Bloom
Rupert Grint
In [248]:


import pandas as pd
df = pd.read_csv('C:/Users/User/ASUS_neidj/data.csv')
df['profit']=df.revenue-df.budget
list_cast = {}
for index, i_row in df[(df.profit>0)].iterrows(): # перебор по строкам
    for j_cast in i_row.cast.split('|'):
        if j_cast in list_cast:
            list_cast[j_cast]+=i_row.profit
        else:
            list_cast[j_cast]=i_row.profit
df1 = pd.DataFrame(list_cast.items(), columns=['cast', 'profit']) #делаем из словаря датафрейм и задаем название колонок
​
display(df1[df1.profit == df1.profit.max()].cast) 
​
answer_ls.append(1)



616    Emma Watson
Name: cast, dtype: object

17. Какой актер принес меньше всего прибыли в 2012 году?
Варианты ответов:
Nicolas Cage
Danny Huston
Kirsten Dunst
Jim Sturgess
Sami Gayle
In [254]:


import pandas as pd
df = pd.read_csv('C:/Users/User/ASUS_neidj/data.csv')
df['profit']=df.revenue-df.budget
list_cast = {}
for index, i_row in df[(df.release_year==2012)].iterrows(): # перебор по строкам
    for j_cast in i_row.cast.split('|'):
        if j_cast in list_cast:
            list_cast[j_cast]+=i_row.profit
        else:
            list_cast[j_cast]=i_row.profit
df1 = pd.DataFrame(list_cast.items(), columns=['cast', 'profit']) #делаем из словаря датафрейм и задаем название колонок
​
display(df1[df1.profit == df1.profit.min()].cast) 
​
answer_ls.append(3)



172    Kirsten Dunst
Name: cast, dtype: object

18. Какой актер снялся в большем количестве высокобюджетных фильмов? (в фильмах где бюджет выше среднего по данной выборке)
Варианты ответов:
Tom Cruise
Mark Wahlberg 
Matt Damon
Angelina Jolie
Adam Sandler
In [253]:


import pandas as pd
df = pd.read_csv('C:/Users/User/ASUS_neidj/data.csv')
list_cast = []
for i in df[(df.budget>df.budget.mean())].cast:
    for j in i.split('|'):
        list_cast.append(j)
df1 = pd.Series(list_cast)
​
# print(df1.value_counts())
print(df1.value_counts().index[0])
answer_ls.append(3)



Matt Damon

19. В фильмах какого жанра больше всего снимался Nicolas Cage?
Варианты ответа:
Drama
Action
Thriller
Adventure
Crime
In [262]:




import pandas as pd
df = pd.read_csv('C:/Users/User/ASUS_neidj/data.csv')
list_genres = []
for i in df[(df.cast.str.find('Nicolas Cage') != -1)].genres: #-1 возвращаем если в cast не найден актер
    for j in i.split('|'):
        list_genres.append(j)
df1 = pd.Series(list_genres)
​
#print(df1.value_counts())
print(df1.value_counts().index[0])
​
answer_ls.append(2)



Action

20. Какая студия сняла больше всего фильмов?
Варианты ответа:
Universal Pictures (Universal)
Paramount Pictures
Columbia Pictures
Warner Bros
Twentieth Century Fox Film Corporation
In [265]:




import pandas as pd
df = pd.read_csv('C:/Users/User/ASUS_neidj/data.csv')
list_production_companies = []
for i in df.production_companies:
    for j in i.split('|'):
        list_production_companies.append(j)
df1 = pd.Series(list_production_companies)
​
# print(df1.value_counts())
print(df1.value_counts().index[0])
answer_ls.append(1)



Universal Pictures

21. Какая студия сняла больше всего фильмов в 2015 году?
Варианты ответа:
Universal Pictures
Paramount Pictures
Columbia Pictures
Warner Bros
Twentieth Century Fox Film Corporation
In [267]:


import pandas as pd
df = pd.read_csv('C:/Users/User/ASUS_neidj/data.csv')
list_production_companies = []
for i in df[(df.release_year==2015)].production_companies:
    for j in i.split('|'):
        list_production_companies.append(j)
df1 = pd.Series(list_production_companies)
​
# print(df1.value_counts())
print(df1.value_counts().index[0])
answer_ls.append(4)



Warner Bros.

22. Какая студия заработала больше всего денег в жанре комедий за все время?
Варианты ответа:
Warner Bros
Universal Pictures (Universal)
Columbia Pictures
Paramount Pictures
Walt Disney
In [271]:



import pandas as pd
df = pd.read_csv('C:/Users/User/ASUS_neidj/data.csv')
list_production_companies={}
for index, i_row in df[(df.genres.str.find('Comedy') != -1)].iterrows(): # перебор по строкам
    for j_production_company in i_row.production_companies.split('|'):
        if j_production_company in list_production_companies:
            list_production_companies[j_production_company]+=i_row.revenue
        else:
            list_production_companies[j_production_company]=i_row.revenue
​
df1 = pd.DataFrame(list_production_companies.items(), columns=['production_companies', 'revenue']) #делаем из словаря датафрейм и задаем название колонок
​
display(df1[df1.revenue == df1.revenue.max()].production_companies) 
​
​
answer_ls.append(2)



0    Universal Pictures
Name: production_companies, dtype: object

23. Какая студия заработала больше всего денег в 2012 году?
Варианты ответа:
Universal Pictures (Universal)
Warner Bros
Columbia Pictures
Paramount Pictures
Lucasfilm
In [273]:





import pandas as pd
df = pd.read_csv('C:/Users/User/ASUS_neidj/data.csv')
list_production_companies={}
for index, i_row in df[(df.release_year==2012)].iterrows(): # перебор по строкам
    for j_production_company in i_row.production_companies.split('|'):
        if j_production_company in list_production_companies:
            list_production_companies[j_production_company]+=i_row.revenue
        else:
            list_production_companies[j_production_company]=i_row.revenue
​
df1 = pd.DataFrame(list_production_companies.items(), columns=['production_companies', 'revenue']) #делаем из словаря датафрейм и задаем название колонок
​
display(df1[df1.revenue == df1.revenue.max()].production_companies) 
answer_ls.append(3)



10    Columbia Pictures
Name: production_companies, dtype: object

24. Самый убыточный фильм от Paramount Pictures
Варианты ответа:
K-19: The Widowmaker tt0267626
Next tt0435705
Twisted tt0315297
The Love Guru tt0811138
The Fighter tt0964517
In [275]:



import pandas as pd
df = pd.read_csv('C:/Users/User/ASUS_neidj/data.csv')
df['loss']=df.budget-df.revenue
​
list_loss = {}
for index, i_row in df[(df.production_companies.str.find('Paramount Pictures') != -1)].iterrows():
            list_loss[i_row.original_title]=i_row.loss
df1 = pd.DataFrame(list_loss.items(), columns=['original_title', 'loss']) #делаем из словаря датафрейм и задаем название колонок
​
display(df1[(df1.loss == df1.loss.max())].original_title)
​
answer_ls.append(1)



54    K-19: The Widowmaker
Name: original_title, dtype: object

25. Какой Самый прибыльный год (заработали больше всего)?
Варианты ответа:
2014
2008
2012
2002
2015
In [279]:





import pandas as pd
df = pd.read_csv('C:/Users/User/ASUS_neidj/data.csv')
df['profit']=df.revenue-df.budget
list_release_year={}
for index, i_row in df.iterrows(): # перебор по строкам
        if i_row.release_year in list_release_year:
            list_release_year[i_row.release_year]+=i_row.profit
        else:
            list_release_year[i_row.release_year]=i_row.profit
​
df1 = pd.DataFrame(list_release_year.items(), columns=['release_year', 'profit']) #делаем из словаря датафрейм и задаем название колонок
​
display(df1[df1.profit == df1.profit.max()].release_year) 
answer_ls.append(5)



0    2015
Name: release_year, dtype: int64

26. Какой Самый прибыльный год для студии Warner Bros?
Варианты ответа:
2014
2008
2012
2010
2015
In [280]:





import pandas as pd
df = pd.read_csv('C:/Users/User/ASUS_neidj/data.csv')
df['profit']=df.revenue-df.budget
list_release_year={}
for index, i_row in df[(df.production_companies.str.find('Warner Bros') != -1)].iterrows(): # перебор по строкам
        if i_row.release_year in list_release_year:
            list_release_year[i_row.release_year]+=i_row.profit
        else:
            list_release_year[i_row.release_year]=i_row.profit
​
df1 = pd.DataFrame(list_release_year.items(), columns=['release_year', 'profit']) #делаем из словаря датафрейм и задаем название колонок
​
display(df1[df1.profit == df1.profit.max()].release_year) 
answer_ls.append(1)



1    2014
Name: release_year, dtype: int64

27. В каком месяце за все годы суммарно вышло больше всего фильмов?
Варианты ответа:
Январь
Июнь
Декабрь
Сентябрь
Май
In [285]:


import pandas as pd
df = pd.read_csv('C:/Users/User/ASUS_neidj/data.csv')
list_month = []
for i in df.release_date:
    month = i.split('/')[0]
    list_month.append(month)
df1 = pd.Series(list_month)
​
#print(df1.value_counts())
print(df1.value_counts().index[0])
​
answer_ls.append(4)



9

28. Сколько суммарно вышло фильмов летом? (за июнь, июль, август)
Варианты ответа:
345
450
478
523
381
In [301]:


import pandas as pd
df = pd.read_csv('C:/Users/User/ASUS_neidj/data.csv')
list_month = []
for i in df.release_date:
    month = i.split('/')[0]
    list_month.append(month)
df1 = pd.Series(list_month)
​
#print(df1.value_counts())
print(df1.value_counts().loc['6']+df1.value_counts().loc['7']+df1.value_counts().loc['8'])
answer_ls.append(2)



450

29. Какой режисер выпускает (суммарно по годам) больше всего фильмов зимой?
Варианты ответов:
Steven Soderbergh
Christopher Nolan
Clint Eastwood
Ridley Scott
Peter Jackson
In [308]:


import pandas as pd
df = pd.read_csv('C:/Users/User/ASUS_neidj/data.csv')
list_director = []
for index, i_row in df.iterrows(): # перебор по строкам 
    month = i_row.release_date.split('/')[0]
    if month in ['12', '1', '2']:
        for j_director in i_row.director.split('|'):
            list_director.append(j_director)
df1 = pd.Series(list_director)
​
#print(df1.value_counts())
print(df1.value_counts().index[0])
answer_ls.append(5)



Peter Jackson

30. Какой месяц чаще всего по годам самый прибыльный?
Варианты ответа:
Январь
Июнь
Декабрь
Сентябрь
Май
In [350]:


import pandas as pd
df = pd.read_csv('C:/Users/User/ASUS_neidj/data.csv')
df['profit']=df.revenue-df.budget
most_profitable_month=[]
list_years = df.release_year.unique()
​
# считаем самый прибыльный месяц дя каждого года
for year in list_years:
    list_month = {}
    for index, i_row in df[df.release_year==year].iterrows(): # перебор по строкам
        month = i_row.release_date.split('/')[0]
        if month in list_month:
            list_month[month]+=i_row.profit
        else:
            list_month[month]=i_row.profit
​
    df1 = pd.DataFrame(list_month.items(), columns=['month', 'profit']) #делаем из словаря датафрейм и задаем название колонок
    most_profitable_month_in_year = df1[df1.profit == df1.profit.max()].month.iloc[0]
    most_profitable_month.append(most_profitable_month_in_year)
​
# самый часто встречающийся месяц
df2=pd.Series(most_profitable_month)
#display(df2.value_counts())   
display(df2.value_counts().index[0])   
answer_ls.append(2)



'6'

31. Названия фильмов какой студии в среднем самые длинные по количеству символов?
Варианты ответа:
Universal Pictures (Universal)
Warner Bros
Jim Henson Company, The
Paramount Pictures
Four By Two Productions
In [391]:




import pandas as pd
df = pd.read_csv('C:/Users/User/ASUS_neidj/data.csv')
df['col_len']=df['original_title'].str.len()
​
# словарь длин названий фильмов по компании
list_production_companies={}
for index, i_row in df.iterrows(): # перебор по строкам
    for j_production_company in i_row.production_companies.split('|'):
            if j_production_company in list_production_companies:
                list_production_companies[j_production_company].append(i_row.col_len)
            else:
                list_production_companies[j_production_company]=[i_row.col_len]
​
# словарь средней длины названий фильмов по компании
list_production_companies_mean={}
for index, values in list_production_companies.items():
    list_production_companies_mean[index]=sum(values)/len(values)
​
df2 = pd.DataFrame(list_production_companies_mean.items(), columns=['production_companies', 'col_mean'])
display(df2[df2['col_mean']==df2['col_mean'].max()].production_companies)
answer_ls.append(5)



1506    Four By Two Productions
Name: production_companies, dtype: object

32. Названия фильмов какой студии в среднем самые длинные по количеству слов?
Варианты ответа:
Universal Pictures (Universal)
Warner Bros
Jim Henson Company, The
Paramount Pictures
Four By Two Productions
In [405]:




import pandas as pd
df = pd.read_csv('C:/Users/User/ASUS_neidj/data.csv')
​
# словарь длин названий фильмов по кол-ву слов по компании
list_production_companies={}
for index, i_row in df.iterrows(): # перебор по строкам
    col_len = len(i_row.original_title.split(' '))
    for j_production_company in i_row.production_companies.split('|'):
            if j_production_company in list_production_companies:
                list_production_companies[j_production_company].append(col_len)
            else:
                list_production_companies[j_production_company]=[col_len]
​
# словарь средней длины названий фильмов по кол-ву слов по компании
list_production_companies_mean={}
for index, values in list_production_companies.items():
    list_production_companies_mean[index]=sum(values)/len(values)
​
df2 = pd.DataFrame(list_production_companies_mean.items(), columns=['production_companies', 'col_mean'])
display(df2[df2['col_mean']==df2['col_mean'].max()].production_companies)
answer_ls.append(5)



1506    Four By Two Productions
Name: production_companies, dtype: object

33. Сколько разных слов используется в названиях фильмов?(без учета регистра)
Варианты ответа:
6540
1002
2461
28304
3432
In [411]:


import pandas as pd
df = pd.read_csv('C:/Users/User/ASUS_neidj/data.csv')
list_words = []
for i in df.original_title: 
    for j in i.split(' '):
        # фильтруем пустые значения (если была 2 и более пробела подряд)
        if (len(j) > 0):
            list_words.append(j.lower())
df1 = pd.Series(list_words)
​
print(df1.nunique())
​
answer_ls.append(2)



2461

34. Какие фильмы входят в 1 процент лучших по рейтингу?
Варианты ответа:
Inside Out, Gone Girl, 12 Years a Slave
BloodRayne, The Adventures of Rocky & Bullwinkle
The Lord of the Rings: The Return of the King
300, Lucky Number Slevin
In [449]:




import pandas as pd
df = pd.read_csv('C:/Users/User/ASUS_neidj/data.csv')
list_vote_average = []
len_df=int(len(df)/100)
df_sort=df.vote_average.sort_values().tail(len_df)
#print(df_sort)
rating_min=df_sort.iloc[0]
for i in df[df.vote_average>=rating_min].original_title:
        list_vote_average.append(i)
print(sorted(list_vote_average))
answer_ls.append(1)



['12 Years a Slave', '3 Idiots', 'Big Hero 6', 'Dallas Buyers Club', 'Eternal Sunshine of the Spotless Mind', 'Gone Girl', 'Guardians of the Galaxy', 'Her', 'Inception', 'Inside Out', 'Interstellar', 'Memento', 'Mr. Nobody', 'Prisoners', 'Room', 'Spotlight', 'The Dark Knight', 'The Fault in Our Stars', 'The Grand Budapest Hotel', 'The Imitation Game', 'The Lord of the Rings: The Fellowship of the Ring', 'The Lord of the Rings: The Return of the King', 'The Lord of the Rings: The Two Towers', 'The Pianist', 'The Prestige', 'The Theory of Everything', 'The Wolf of Wall Street', 'There Will Be Blood']

35. Какие актеры чаще всего снимаются в одном фильме вместе
Варианты ответа:
Johnny Depp & Helena Bonham Carter
Hugh Jackman & Ian McKellen
Vin Diesel & Paul Walker
Adam Sandler & Kevin James
Daniel Radcliffe & Rupert Grint
In [468]:


import pandas as pd
df = pd.read_csv('C:/Users/User/ASUS_neidj/data.csv')
list_casts = []
​
for i in df.cast: # перебор по строкам
    cast = i.split('|')
    for actor_1 in cast:
        for actor_2 in cast:
            if actor_1!=actor_2:
                list_casts.append(actor_1+' and '+actor_2)
       
​
df1 = pd.Series(list_casts)
​
value_count = df1.value_counts()
display(value_count[(value_count==value_count.max())])
​
answer_ls.append(5)



Daniel Radcliffe and Rupert Grint    8
Rupert Grint and Daniel Radcliffe    8
Daniel Radcliffe and Emma Watson     8
Emma Watson and Daniel Radcliffe     8
Emma Watson and Rupert Grint         8
Rupert Grint and Emma Watson         8
dtype: int64

36. У какого из режиссеров выше вероятность выпустить фильм в прибыли? (5 баллов)101
Варианты ответа:
Quentin Tarantino
Steven Soderbergh
Robert Rodriguez
Christopher Nolan
Clint Eastwood
In [ ]:


import pandas as pd
df = pd.read_csv('C:/Users/User/ASUS_neidj/data.csv')
df['profit']=df.revenue-df.budget
df_directors=pd.DataFrame(columns=['director', 'total_movies', 'profitable_movies'])
for index, i_row in df.iterrows(): # перебор по строкам
    for j_director in i_row.director.split('|'):
        if j_director in df_directors.director.values:
            #df_directors[df_directors.director==j_director].total_movies+=1
            r = 0
        else:
            df_directors.append(pd.Series([j_director, 1, 0]), ignore_index=True)
        if i_row.profit > 0:
            df_directors.loc[df_directors.director==j_director].profitable_movies+=1
display(df_directors)
answer_ls.append(1)




Submission
In [497]:


len(answer_ls)


Out[497]:
174
In [498]:



​




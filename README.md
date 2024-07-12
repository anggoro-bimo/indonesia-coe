# Indonesia Cup Of Excellence

Cup of Excellence (COE) is a prestigious competition in the coffee industry that seeks to find and recognize the highest quality coffees from around the world. It’s like the Oscars for coffee! Here’s how it works:

- **Finding the Best Beans**: Coffee farmers from different regions submit their best coffee beans to the competition. These beans are carefully grown and processed to ensure they have the most delicious flavors.
- **Expert Judging**: A panel of expert coffee tasters, also known as cuppers, evaluates each batch of beans. They use their finely-tuned taste buds to assess factors like flavor, aroma, acidity, and body.
- **Scoring The Best Coffees**: These coffees have each been cupped a minimum of five different times during the cupping process. The coffees that scored above 87 are categorized in the Cup Of Excellence list. These are the cream of the crop, the absolute best coffees that stand out for their exceptional quality and unique flavors.
- **Worldwide Open Auction**: Buyers around the world compete for the honor to owning and selling these unique coffees to their customers. These auctions have set the standard for the increased premiums that farmers have been able to receive for their exemplary coffees and have set the standard for transparency in pricing.
- **Promoting Excellence**: Cup of Excellence doesn’t just celebrate great coffee; it also helps to promote sustainable practices and fair treatment of coffee farmers. By highlighting the best coffees, the competition encourages farmers to strive for excellence and rewards them for their hard work.

![Alt text](https://cupofexcellence.org/wp-content/uploads/2020/05/coe-infographic-v5-pdf.jpg)

Cup of Excellence is essentially a celebration of the skill and commitment that go into making exceptional coffee. It draws attention to the skilled growers and producers who are committed to providing coffee enthusiasts all over the world with extraordinary coffee experiences.

## The Project's Steps.

### 1. Web Scraping from the Official Website

All the data, including the historical COE results per country per year, is published on their official website: https://allianceforcoffeeexcellence.org/competition-auction-results/

I do the web scraping with Python, using the requests and BeautifulSoup libraries. The detailed code can be checked at this link: [Web Scraping Google Colab Notebook](https://colab.research.google.com/drive/1ON7HYpzdF-IZH_Sd9N9YjrgDWX1NoQxg?usp=sharing&source=post_page-----c17811366a33--------------------------------) or [Github](https://github.com/anggoro-bimo/indonesia-coe/blob/main/notebooks/01.%20website_scraping%20.ipynb)

The web scraping tutorial for this project is also published at this link: [Medium Article](https://medium.com/@anggoro-bimo/indonesia-cup-of-excellence-exposing-indonesian-diversity-of-delicacies-through-coffee-c17811366a33)

### 2. Data Collection

By compiling the code for web scraping, I define a function to extract the data from the official websites and save it to local storage as .csv files.

The .py file can be checked at this link: [website_scraping.py](https://github.com/anggoro-bimo/indonesia-coe/blob/main/src/website_scraping.py)

The published article for the data collection step of this project can be read at this link: [Medium Article](https://medium.com/@anggoro-bimo/indonesia-cup-of-excellence-exposing-indonesian-diversity-of-delicacies-through-coffee-190e63bbe4b7)


### 3. Data Remediation

The raw data was prepared and transformed into a usable format for analysis. After being cleaned to correct errors and remove inconsistencies, the data is then integrated into a cohesive dataset, often enriched with additional context to enhance its utility. Once the data remediation stage is complete, the cleaned and organized data is ready for analysis, enabling meaningful insights and informed decision-making.

The published article for this stage can be read at this link: [Medium Article](https://medium.com/@anggoro-bimo/indonesia-cup-of-excellence-exposing-indonesian-diversity-of-delicacies-through-coffee-190e63bbe4b7)

While the detailed code can be checked at this link: [Data Wrangling Notebook](https://github.com/anggoro-bimo/indonesia-coe/blob/main/notebooks/03.%20data_wrangling.ipynb)


### 4. EDA for The Numerical Features

The combined dataset from Indonesia's COE outcomes during the three years of participation is currently available, and we are now proceeding with the exploratory data analysis (EDA) for the numerical features. We investigate and analyze the data in this step to identify its characteristics.

The published article for this stage can be read at this link: [Medium Article](https://medium.com/@anggoro-bimo/indonesia-cup-of-excellence-exposing-indonesian-diversity-of-delicacies-through-coffee-128d6db079e3)

While the detailed code can be checked at this link: [Numerical Features EDA Notebook](https://github.com/anggoro-bimo/indonesia-coe/blob/main/notebooks/04.%20eda_num.ipynb)

### 5. EDA for The Categorical Features

Now we assess the categorical features on the combined dataset from Indonesia COE.  Several anomalies in the data's nomenclature were discovered at this point and will be fixed in consultation with the coffee expert throughout the data validation stage.

The detailed code can be checked at this link: [Categorical Features EDA Notebook](https://github.com/anggoro-bimo/indonesia-coe/blob/main/notebooks/05.%20eda_cat.ipynb)
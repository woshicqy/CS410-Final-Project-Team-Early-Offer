# Movie Recommendation Systems

## Description

We developed a website that is used for recommending movies to the user. The website is based on the three recommender system algorithms, user can get movie recommendations based on them.

1. Content-based Filter System

  The users could use this system by searching for a movie, and the system will show ten relevant movies based on the input movie. This recommendation system is based on two kinds of filters. 
  - The overview expresses the basic content of the movie and we use the overview to build a TF-IDF matrix to get similar movies.
  - The keyword, cast, crew, and genres are also good for finding the relevant movies that the users may like so we create a count vector for these factors to get the relevant movies.
  Each filter would return the top 5 relevant movies so the whole content-based filter system would return 10 movies for the users. 

2. User-based Filter System

3. Matrix Factorization-based System

  The matrix factorization system is a system based on the Singular Value Decomposition (SVD) method. Popularized by Simon Funk and tied for third place on the Netflix Prize. The system utilizes matrix factorization to generalize users' ratings and recommend based on the rating trend. Users can input a user id to observe other users' rating history, whereas entering an id can recommend the top 10 relevant movies to the user based on the prediction score generated by the system.

## Getting Started

### Front End File Structure
```bash
front_end
├── app/
│ ├── static/
│ │ ├── script/
│ │ │ └── model.js
│ │ ├── styles/
│ │ │ └── custom.css
│ │ └── layout.html
│ ├── templates/
│ │ └── autoencoder_based.html
│ │ └── content_based.html
│ │ └── home.html
│ │ └── layout.html
│ │ └── user_content
│ └── __init__.py
│ ├── routes.py
├── Back_end
│ └── user_based_system.py
│ └── matrix_factorization_system.py
│ └── content_based_system.py
│ └── dataset 
│── webforms
└── main.py
```

### Dependencies

* random
* pandas
* numpy
* sklearn
* flask 
* scikit-suprise
* python >= 3.5

### Installing

* git clone git@github.com:woshicqy/CS410-Final-Project-Team-Early-Offer.git
* pip install flask flask_sqlalchemy pymysql pyyaml
* pip install scikit-surprise

### Executing program

```bash
cd front_end
python3 -m venv env
source env/bin/activate
export FLASK_APP=app && export FLASK_DEBUG=1
flask run
```
You can now running the website by clicking http://127.0.0.1:5000/home

## Help

1. The movie name for searching in the content-based page must exist in the database.

## Authors

Xipeng Song, xipengs2@illinois.edu

Xinyi Ai xinyia2@illinois.edu

Yunfei Ouyang, yunfeio2@illinois.edu

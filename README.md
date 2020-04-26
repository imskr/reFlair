<p align="center">
  <img src="static/image/logodesign.png" alt="logo" height="200">
</p>
<h4 align="center">Reddit Flair Detection Web Application for r/india.</h4>

<br>

<p align="center">   
  <a href="https://github.com/imskr/reFlare/blob/master/LICENSE">
    <img src="https://img.shields.io/badge/License-MIT-orange.svg?longCache=true" alt="License">
  </a>
  
  <a href="https://github.com/imskr/reFlare/stargazers">
    <img src="https://img.shields.io/github/stars/imskr/reFlare.svg?style=social" alt="Stargazers">
  </a>

 <a href="https://github.com/imskr">
    <img src="https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg" alt="awesome">
  </a>
</p>

<p align="center">
  <sub>Created by <a href="https://github.com/imskr"><strong>Shubham Kumar</strong></a>
</p>
<hr noshade>

## Local Set-up

* **Linux**
  ```bash
  $ git clone https://github.com/imskr/reflair.git
  $ cd reflair
  $ python3 -m venv env_name
  $ source env_name/bin/activate
  $ pip3 install -r requirements.txt
  $ python3 app.py
  ```

`Go to http://127.0.0.1:5000 to test your app`

*Note: If you have `fish` terminal run `$ source env_name/bin/activate.fish`*
* **Windows**
  ```bash
  $ git clone https://github.com/imskr/reflair.git
  $ cd reflair
  $ python3 -m venv env_name
  $ source env_name/bin/activate
  $ pip3 install -r requirements.txt
  $ python3 app.py
  ```

`Go to http://localhost:5000 to test your app`

## Data (r/india)
* **Data fetched using `PRAW` reddit API**.
* **Flairs supporting (currently 11)**
  
  | Label | Flair              | Samples       | After Cleaning     |  
  | ---   | ---                | ---           | ---                |
  | 1.    | AskIndia           | 11            | 11                 |
  | 2.    | Business/Finance   | 458           | 458                |
  | 3.    | CAA-NRC-NPR        | 11            | 11                 |
  | 4.    | Food               | 121           | 121                |
  | 5.    | Non-Political      | 1322          | 1322               |
  | 6.    | Policy/Economy     | 165           | 165                |
  | 7.    | Politics           | 124           | 124                |
  | 8.    | Scheduled          | 369           | 369                |
  | 9.    | Science/Technology | 11            | 11                 |
  | 10.   | Coronavirus        | 88            | 88                 |
  | 11.   | Sports             | 3             | 03                 |
  | 12.   | Photography        |               |                    |
  | 13.   | TIL                |               |                    |
  | 14.   | Unverified         |               |                    |
  | 15.   | na                 |               |                    |


* **Distribution Graph**
<br>

  ![plot](static/image/distribution.png)


## Training Algorithms

* **Title as Feature**
  ![title](static/image/title.png)

* **Body as Feature**
  ![title](static/image/body.png)

* **Title+Body+URL as Feature**
  ![title](static/image/tbu.png)
  ![tbu](static/image/tbufinal.png)
## References
* [Scrap Reddit Data](https://www.storybench.org/how-to-scrape-reddit-with-python/)
* [PRAW: Docs](https://praw.readthedocs.io/en/latest/)
<p align="center">
  <img src="static/image/logodesign.png" alt="logo" height="200">
</p>
<h4 align="center">Reddit Flair Detection Web Application for r/india.</h4>

<br>

<p align="center">   
  <a href="https://github.com/imskr/reFlare/blob/master/LICENSE">
    <img src="https://img.shields.io/badge/License-MIT-orange.svg?longCache=true" alt="License">
  </a>
  
  <a href="https://github.com/imskr/reFlair/stargazers">
    <img src="https://img.shields.io/github/stars/imskr/reFlair?style=social" alt="Stargazers">
  </a>

 <a href="https://github.com/imskr">
    <img alt="Twitter Follow" src="https://img.shields.io/twitter/follow/TheTweetofSKR?style=social">
  </a>
</p>

<p align="center">
  <sub>Created by <a href="https://github.com/imskr"><strong>Shubham Kumar</strong></a>
</p>
<hr noshade>

## Live: https://reflair.herokuapp.com

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
  $ pip3 install -r requirements.txt
  $ python3 app.py
  ```

`Go to http://localhost:5000 to test your app`

## Data (r/india)
* **Data fetched using `PRAW` reddit API**.
* **Flairs supporting (currently 14)**
* *Note: `na` is added for unlabeled flair*
  
  | Label | Flair              | Samples(Clean)|  
  | ---   | ---                | ---           |              
  | 1.    | AskIndia           | 754           |               
  | 2.    | Business/Finance   | 1688          |                
  | 3.    | CAA-NRC-NPR        | 77            |                
  | 4.    | Food               | 99            |                
  | 5.    | Non-Political      | 1355          |               
  | 6.    | Policy/Economy     | 113           |                
  | 7.    | Politics           | 468           |                
  | 8.    | Scheduled          | 1419          |              
  | 9.    | Science/Technology | 11            |                 
  | 10.   | Coronavirus        | 44            |                 
  | 11.   | Sports             | 3232          |                 
  | 12.   | Photography        | 88            |                   
  | 13.   | TIL                | 11            |                   
  | 14.   | Unverified         | 55            |                    
  | 15.   | na                 | 121           |                    


* **Distribution Graph**
<br>

  ![plot](static/image/distribution.png)


## Training Algorithms

* **Title+Body+URL as Feature**
  ![title](static/image/tbu.png)
  ![tbu](static/image/tbufinal.png)
## References
* [Scrap Reddit Data](https://www.storybench.org/how-to-scrape-reddit-with-python/)
* [PRAW: Docs](https://praw.readthedocs.io/en/latest/)

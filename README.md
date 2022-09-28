<!-- PROJECT LOGO -->
<div align="center">
  <a href="https://github.com/JensBender/internet-speed-database">
    <img src="images/logo.png" width=80%>
  </a>
  <p>
    <br />
    Collect, store and analyze data on your internet speed.
    <br />
  </p>
</div> 

---

## Table of Contents
<ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
</ol>

<!-- ABOUT THE PROJECT -->
## About The Project
Do you get what you pay for when it comes to your internet speed? 

The Internet Speed Database project answers this question by doing the following:
+ **Data collection**: Perform automated internet speedtests and collect data on your download speed, upload speed, and internet provider 
+ **Data entry**: Perform automated data entry by submitting the collected data to a Google Form 
+ **Data storage**: Create an internet speed database in the form of a simple Google Sheet and store it in your Google Drive
+ **Data analysis**: Analyze your average download speed and upload speed across multiple speedtests and compare it with the internet speed promised by your internet provider

### Built With
* [![Selenium][Selenium-badge]][Selenium-url]
* [![Pandas][Pandas-badge]][Pandas-url]
* [![PyCharm][PyCharm-badge]][PyCharm-url]

<!-- GETTING STARTED -->
## Getting Started

Follow these steps to get the program running on your local machine.

### Prerequisites

This is a list of things you need to use this program.
<ul>
  <li>Python libraries</li>
  <ul>
    <li>Selenium</li>
    <li>Pandas</li>
    <li>Requests</li>
  </ul>
  <li>Google Account</li>
  <ul>
    <li>Google Forms</li>
    <li>Google Sheets</li>
  </ul>
  <li>Sheety Account</li>
</ul>

### Installation

<ol>
    <li>Create a Google Form "Internet Speed Database".</li>
    <li>
      Create three questions for (1) Download speed, (2) Upload speed, and (3) Internet provider in precisely this order. <br /> 
      For all questions, select "Short answer" as the response format.<br />
      <a href="https://github.com/JensBender/internet-speed-database"><img src="images/google_form.png" width=80%></a>
    </li>
    <li>
      Go to "Responses" and click on "Create Spreadsheet".<br />
      <a href="https://github.com/JensBender/internet-speed-database"><img src="images/create_spreadsheet.png" width=80%></a>
    </li>
    <li>
      Create a new spreadsheet with the same name.<br />
      <a href="https://github.com/JensBender/internet-speed-database"><img src="images/create_spreadsheet_2.png" width=80%></a>
    </li>
    <li>
      This is how your Google Sheet should look like.<br />
      <a href="https://github.com/JensBender/internet-speed-database"><img src="images/google_sheet.png" width=80%></a>
    </li>
</ol>

<!-- MARKDOWN LINKS -->
[Pandas-badge]: https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white
[Pandas-url]: https://pandas.pydata.org/
[PyCharm-badge]: https://img.shields.io/badge/pycharm-143?style=for-the-badge&logo=pycharm&logoColor=black&color=black&labelColor=green
[PyCharm-url]: https://www.jetbrains.com/pycharm/
[Selenium-badge]: https://img.shields.io/badge/-selenium-%43B02A?style=for-the-badge&logo=selenium&logoColor=white
[Selenium-url]: https://www.selenium.dev/

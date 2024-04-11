<div align="center">
  <h1><b>Sepsis Detection Using ML API</b></h1>
</div>

<!-- TABLE OF CONTENTS -->

# 📖 Table of Contents

- [📖 Table of Contents](#-table-of-contents)
- [Sepsis Detection API](#sepsis-detection-api)
  - [🛠 Built With](#-built-with)
    - [Tech Stack](#tech-stack)
  - [Application Features](#application-features)
  - [💻 Getting Started](#-getting-started)
    - [Prerequisites](#prerequisites)
    - [Setup](#setup)
    - [Install](#install)
    - [Usage](#usage)
  - [👥 Authors](#-authors)
  - [🔭 Future Features](#-future-features)
  - [🤝 Contributing](#-contributing)
  - [⭐️ Show Your Support](#️-show-your-support)
  - [🙏 Acknowledgments](#-acknowledgments)
  - [📝 License](#-license)

<!-- PROJECT DESCRIPTION -->

# Sepsis Detection API <a name="sepsis-detection-api"></a>



## 🛠 Built With <a name="-built-with"></a>

### Tech Stack <a name="tech-stack"></a>

<!--
<details>
  <summary>GUI</summary>
  <ul>
    <li><a href="">Streamlit</a></li>
  </ul>
</details>
-->

<!--
<details>
<summary>Database</summary>
  <ul>
    <li><a href="">Microsoft SQL Server</a></li>
  </ul>
</details>
-->

<details>
<summary>Language</summary>
  <ul>
    <li><a href="">Python</a></li>
  </ul>
</details>

<details>
<summary>Model</summary>
  <ul>
    <li><a href="">Sklearn</a></li>
  </ul>
</details>

<details>
<summary>Deployment</summary>
  <ul>
    <li><a href="">FastAPI</a></li>
    <li><a href="">Docker</a></li>
  </ul>
</details>


## Application Features <a name="application-features"></a>

- **Multiple models to select for prediction of sepsis likelihood**


<!-- GETTING STARTED -->

## 💻 Getting Started <a name="-getting-started"></a>

To get a local copy up and running, follow these steps.


### Prerequisites <a name="prerequisites"></a>

To run this project you need:

- Python
- FastAPI
- Docker

### Setup <a name="setup"></a>

Clone this repository to your desired folder:

```sh
  cd desired-folder
  git clone https://github.com/pk-aduyaw/Sepsis-Detection-using-ML-API.git
```

Change into the cloned repository:

```sh
  cd Sepsis-Detection-using-ML-API
```

Create a virtual environment

```sh
  python -m venv venv
```

Activate the virtual environment

```sh
  venv/Scripts/activate
```

### Install <a name="install"></a>

Install the required packages needed for this project which can be found in the `requirements.txt` file
```sh
  pip install -r requirements.txt
```

### Usage <a name="usage"></a>

Run the app by executing the command below

```sh
    uvicorn main:app --reload
```

After the application finishes running, a URL will appear in the terminal. You can access the API page by either `copying and pasting the URL into your browser` or `holding Ctrl while clicking on the link`.

You will be met with a JSON output view in the browser.

![Screenshot (107)](https://github.com/pk-aduyaw/Sepsis-Detection-using-ML-API/assets/148882212/1ffaf5ab-69b6-4fd3-a237-bc1063ed3469)

To view the output in a GUI environment to test the API add `/docs` to the URL in the browser.

Click on any of the post tags to enter input features to predict the Sepsis likelihood

![Screenshot (106)](https://github.com/pk-aduyaw/Sepsis-Detection-using-ML-API/assets/148882212/06f33c53-0643-4067-8686-2b9036fa595c)

## 👥 Authors <a name="-authors"></a>

### Prince Kwabena Amoako Aduyaw

- GitHub: [GitHub Profile](https://github.com/pk-aduyaw)
- X : [X Profile](https://twitter.com/pk_aduyaw)
- LinkedIn: [LinkedIn Profile](https://www.linkedin.com/in/prince-kwabena-aduyaw)



## 🔭 Future Features <a name="-future-features"></a>

- **Deployment of APIs into a Streamlit App**
  
  



## 🤝 Contributing <a name="-contributing"></a>

Contributions, issues, and feature requests are welcome!


## ⭐️ Show Your Support <a name="-show-your-support"></a>

Your support is greatly appreciated! Please remember to leave a star to help me on my journey. Thank you!


## 🙏 Acknowledgments <a name="-acknowledgments"></a>

I would like to acknowledge all the free resources made available online.



<!-- LICENSE -->

## 📝 License <a name="-license"></a>

This project is [MIT](./LICENSE) licensed.



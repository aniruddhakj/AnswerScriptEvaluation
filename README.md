# AnswerScriptEvaluation

A project to automate an answer script evaluator.

## INDEX
[Getting Started](https://github.com/aniruddhakj/AnswerScriptEvaluation/blob/main/README.md#getting-started)
[Setting Up Dev Environment](https://github.com/aniruddhakj/AnswerScriptEvaluation/blob/main/README.md#setting-up-dev-environment)

## Getting Started
1. Download and install Python3 from [this link](https://www.python.org/downloads/)
2. Install [venv](https://pypi.org/project/virtualenv/) to create a virtual environment for the project.
    - You can do this using a terminal and type :
        ```bash
        py -m pip install --user virtualenv
        ```
    - For macOS and Linux:
        ```zsh
        python3 -m pip install --user virtualenv
        ```  
3. Now create and activate the virtual environment
    ```bash
    venv AnswerScriptEvalution
    ```
    - For Windows
        ```bash
        cd AnswerScriptEvaluation\Scripts
        activate
        ```
    - For macOS and Linux
      ```zsh
      source AnswerScriptEvaluation/bin/activate
      ```

## Setting Up Dev Environment

1. Clone the repo

```bash
git clone https://github.com/aniruddhakj/AnswerScriptEvaluation
```

- install streamlit

```bash
pip3 install streamlit
```

- install google-cloud-vision library

```bash
pip3 install google-cloud-vision
```

- run main program

```bash
streamlit run main.py
```

[streamlit API reference](https://docs.streamlit.io/en/stable/)

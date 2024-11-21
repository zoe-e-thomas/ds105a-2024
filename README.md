# LSE DS105A 2024/25: Data for Data Science

<figure>
    <img src="./figures/ds105/DS105A_person_icon.jpeg" alt="Image created with the AI embedded in MS Designer using the prompt 'abstract salmon pink light blue icon depicting the metaphysical experience of cleaning up, reshaping, pivoting, and manipulating data in search of the purest insights in data science.'" title="Image created with the AI embedded in MS Designer using the prompt 'abstract salmon pink light blue icon depicting the metaphysical experience of cleaning up, reshaping, pivoting, and manipulating data in search of the purest insights in data science.''" role="presentation" style="object-fit: cover;width:5em;height:5em;border-radius: 50%;margin-bottom:1em;">
</figure>

Welcome to the central hub for all lecture and class materials used in the Autumn Term edition of DS105A (2024/25) at LSE. This repository embodies the course's core principles: clear communication, reproducible code, and insightful data exploration.

## 🔗 Links

- **Course Website:** Access the [public course website](https://lse-dsi.github.io/DS105) or the [Moodle page](https://moodle.lse.ac.uk/course/info.php?id=9236) (LSE students only) for the latest updates and announcements.

## 🧭 Navigating the Repository

The repository has recently undergone a [reorganisation](https://github.com/lse-ds105/ds105a-2024/issues/3) and materials are now structured as follows:

```
ds105a-2024/
│
├── notebooks/
│   ├── ... # Lecture and lab notebooks
│
├── data/
│   ├── ... # Folders and files with datasets
│
├── figures/
│   ├── ... # Figures referenced in notebooks
│
├── .gitignore # Python-specific .gitignore file
└── README.md
```

Notebook names follow the format `WXX-[Lecture/Lab]-[Topic].ipynb`, where `XX` is the week number.

Found an issue with a notebook or anoter file? Create a [new issue](https://github.com/lse-ds105/ds105a-2024/issues/new) and explain the problem. 

## 🚀 Getting Started

1. **Fork this repository:** Click the 'Fork' button at the top right to create a copy under your GitHub account. This allows you to experiment and learn without affecting the original repository.

2. **Clone your forked repository:** Use `git clone` to download a copy to your local machine or the Nuvolos platform. Replace `<username>` with your GitHub username (remove the `<>` symbols).

    ```bash
    git clone git@github.com:<username>/ds105a-2024.git
    ```

3. **Add a pointer to the 'upstream' repository:** This allows you to fetch changes from the original repository.

    ```bash
    git remote add upstream git@github.com:lse-ds105/ds105a-2024.git
    ```

4. **Add the `upstream` remote:**

    ```bash
    git remote add upstream git@github.com:lse-ds105/ds105a-2024.git
    ```

5. **Stay Updated:** Regularly fetch and merge changes from the original repository using these commands:
    ```bash
    git fetch upstream main
    git merge upstream main
    ```

    (Fix [merge conflicts](https://docs.github.com/en/github/collaborating-with-pull-requests/addressing-merge-conflicts/about-merge-conflicts) if needed.)

## 🐍 Python environment

To guarantee that the code runs smoothly, we recommend creating a [virtual environment](https://www.geeksforgeeks.org/python-virtual-environment/). If you already have `conda` installed, it's straightforward to create a new environment. If not, you can use Python's built-in `venv` module.

👉🏻 If you type `conda` on your terminal and it says "command not found," then you probably don't have it installed. In that case, you can use Python's built-in `venv` module to create a virtual environment.

1. If you already have conda installed: 

    - you can create a new environment with the following command:

        ```bash
        conda create -n .venv
        ```

    - Then, activate the environment:

        ```bash
        conda activate .venv
        ```

    - Install `pip` inside conda:

        ```bash
        conda install pip
        ```

2. Otherwise, let's use `venv`. 

    - On the command line, run the following commands:

        ```bash
        cd /path/to/ds105a-2024
        python -m venv .venv
        ```

    - Then, activate the virtual environment.

        If on Windows, run:

        ```powershell
        .venv\Scripts\activate
        ```

        If on MacOS or Linux, run:

        ```bash
        source .venv/bin/activate
        ```

You should see a `(.venv)` in your terminal prompt now.

3. Install the required packages:

    ```bash
    pip install -r requirements.txt
    ```

4. Use the same kernel when running Jupyter notebooks.

## 🙏 Acknowledgements

This repository is maintained by Dr. [Jon Cardoso-Silva](https://github.com/jonjoncardoso) and the teaching team of DS105A, [Alex Soldatkin](https://github.com/alex-soldatkin) and [Riya Chhikara](https://github.com/RiyaChhikara). Alex, in particular, has made several contributions to the content (datasets and lab suggestions). Many thanks also to the course representatives, [Courtney Powers](https://github.com/cmpowers9) and [Doris Huang](dorishuang033) who have provided valuable feedback on the course materials.


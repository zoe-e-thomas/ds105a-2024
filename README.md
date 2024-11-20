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

2. **Clone your forked repository:** Use `git clone` to download a copy to your local machine or the Nuvolos platform. Replace `<username>` with your GitHub username.

    ```bash
    git clone git@github.com:lse-ds105/ds105a-2024-<username>.git
    ```
3. **Add the `upstream` remote:**

    ```bash
    git remote add upstream git@github.com:lse-ds105/ds105a-2024.git
    ```

4. **Stay Updated:** Regularly fetch and merge changes from the original repository using these commands:
    ```bash
    git fetch upstream main
    git merge upstream main
    ```

    (Fix [merge conflicts](https://docs.github.com/en/github/collaborating-with-pull-requests/addressing-merge-conflicts/about-merge-conflicts) if needed.)

## 🙏 Acknowledgements

This repository is maintained by Dr. [Jon Cardoso-Silva](https://github.com/jonjoncardoso) and the teaching team of DS105A, [Alex Soldatkin](https://github.com/alex-soldatkin) and [Riya Chhikara](https://github.com/RiyaChhikara). Alex, in particular, has made several contributions to the content (datasets and lab suggestions). Many thanks also to the course representatives, [Courtney Powers](https://github.com/cmpowers9) and [Doris Huang](dorishuang033) who have provided valuable feedback on the course materials.


Project Organization
XTrade/
├── main.py
├── README.md
├── api/
│   ├── __init__.py
│   ├── api_client.py
│   ├── api_exceptions.py
│   ├── api_response.py
├── auth/
│   ├── __init__.py
│   ├── model_one.py
│   ├── model_two.py
├── gui/
│   ├── __init__.py
│   ├── main_win.py
│   ├── login_win.py
│   ├── exit_win.py
└── utils/
    ├── __init__.py
    ├── json_utils.py
    ├── log_utils.py

























├── README.md          <- The top-level README for developers using this project.
├── data
│   ├── interm         <- Intermediate data that has been transformed
│   ├── processed      <- The final, canonical data sets for modeling
│   └── raw            <- The original, immutable data dump
│
├── guide              <- A set of markdown files with documented best practices, guidelines and rools for collaborative projects
│
├── models             <- Trained and serialized models, model predictions, or model summaries
│
├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
│                         the creator's initials, and a short `-` delimited description, e.g
│                         `1.0-jqp-initial-data-exploration`
│
├── references         <- Data dictionaries, manuals, and all other explanatory materials.
│
├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
│   └── figures        <- Generated graphics and figures to be used in reporting
│
├── requirements.txt   <- The requirements file for reproducing the analysis environment
│
└── da-project         <- Source code for use in this project.
    │
    ├── data           <- Scripts to download or generate data
    │   └── make_dataset.py
    │
    ├── features       <- Scripts to turn raw data into features for modeling
    │   └── build_features.py
    │
    ├── models         <- Scripts to train models and then use trained models to make
    │   │                 predictions
    │   ├── predict_model.py
    │   └── train_model.py
    │
    └── visualization  <- Scripts to create exploratory and results oriented visualizations
        └── visualize.py
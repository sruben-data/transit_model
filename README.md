# transit_model

## Tech Stack
1. 511.org API & GTFS Static and Realtime Feeds
2. Python
3. Matplotlib/Seaborn
4. Looker Studio

## Setup (one-time)
   ```shell
   # To persist across sessions, "-Scope CurrentUser"
   Set-ExecutionPolicy -ExecutionPolicy Unrestricted -Scope Process
   ```

## venv Dev Setup

1. Create the virtual environment in project directory and then activate it

    ```shell
    py -m venv .venv # set up venv using system Python, can indicate version with py -3.X
    # venv folder can be named anything, for multiple, can distinguish with suffix ".venv1"
    .venv/Scripts/activate # ".venv" being the name of the venv folder
    python -c "import sys; print(sys.prefix)" # Confirm activation using local python call
    ```

2. Install requirements

    ```shell
    python -m pip install -r requirements.txt
    python -m pip freeze -l # check installation
    # To generate a requirements file from current venv packages
    python -m pip freeze > requirements.txt
    ```

3. Run main file locally
    
    ```shell
    python main.py
    ```
   
4. Deactivate venv
    
    ```shell
    deactivate
    ```

## [`uv`](https://docs.astral.sh/uv/getting-started/installation/) Dev Setup


### One-Time Setup
1. Create the virtual environment

```shell
    uv venv .venv # create venv using uv
```

2. Install requirements

```shell
    uv pip install -r requirements.txt
    uv pip freeze # check installation
    # to generate a requirements.txt file from current packages
    uv pip freeze > requirements.txt
```

### Run Your Script

Use `uv run` to execute main.py (activates venv, runs script, deactivates automatically):

```shell
uv run python main.py
```

**Alternative: Manual activation** (if you prefer staying in the venv)

```shell
.venv\Scripts\activate
python main.py
deactivate
```

### Testing
Run all the the tests with `pytest` or specific tests with prefixing files `pytest tests/blueprints/*`

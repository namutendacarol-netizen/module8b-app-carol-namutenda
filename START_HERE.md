# Replacing your existing flower app — do this first
1. In VS Code, click in the running terminal and press Ctrl+C to stop the flower app.
2. Extract this NEW ZIP to a NEW folder, for example Documents/EHA/ASSIGNMENTS/Module8B_Health.
3. In VS Code choose File → Open Folder and select the new extracted folder containing app.py.
4. Create the environment, install packages and launch using section 2 below. Python 3.12 is already installed on your laptop.
5. Your browser may still show the old page until you refresh http://localhost:8501. The new title must be Diabetes Progression Explorer.
6. Continue to Docker, GitHub, cloud deployment and video steps below. The public links and video are still required for submission.

# Start here — opening and finishing your assignment
Prepared for Carol Namutenda. No student number is included.

## 1. Extract and open in VS Code
1. Download the ZIP file and locate it in Downloads.
2. Right-click it → Extract All → Extract.
3. Open VS Code → File → Open Folder.
4. Select the extracted `module8b-app-carol-namutenda` folder that directly contains `app.py`, then click Select Folder.
5. If prompted about trust, trust the folder only after reviewing its source.
6. Open Terminal → New Terminal. Commands below are typed in this terminal, not inside app.py and not in a notebook.

## 2. Install and start
Use Python 3.12 (install it if `py -3.12 --version` fails). Run each line separately:
```powershell
py -3.12 -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe -m streamlit run app.py
```
The supplied model is already trained. You do not need to run train_model.py first. Wait for the Local URL and open http://localhost:8501. Leave the terminal running. Press Ctrl+C to stop. Using the full environment path avoids PowerShell activation-policy problems.

## 3. Check predictions
Select Example 1 and click Predict progression. A numeric progression score and input table should appear. Select Example 2 and click again; the score should change. Expand About the model and evaluation. This health model estimates a dataset-specific one-year progression score for people already living with diabetes. It does not diagnose diabetes and is not for patient care.

## 4. Test Docker locally
Install Docker Desktop if needed and start it. Stop Streamlit with Ctrl+C so port 8501 is free. In the same project terminal:
```powershell
docker compose up --build
```
Open http://localhost:8501 and make a prediction. To stop, press Ctrl+C, then run `docker compose down`. Docker must be running for these commands. The cloud deployment below uses requirements.txt directly; the Docker files satisfy the container deliverable.

## 5. Create the public GitHub repository
1. Sign into https://github.com and choose New repository.
2. Name it `module8b-app-carol-namutenda`, select Public, and create it.
3. Choose the option to upload existing files.
4. Open your project folder in File Explorer. Upload the project files, including app.py, model.pkl, Dockerfile, docker-compose.yml, requirements.txt, README.md, train_model.py, metrics.json and diabetes_data.csv. Do not upload .venv.
5. Commit the files. Confirm app.py appears directly in the repository root, not inside another folder.
6. Copy the repository's real browser URL. Check it in a signed-out/private window.

## 6. Deploy the app
1. Go to https://share.streamlit.io and sign in using GitHub.
2. Choose Create app, then the option for an existing app if shown.
3. Choose your repository, branch `main`, and main file path `app.py`.
4. In Advanced settings, select Python 3.12. Deploy and wait for installation.
5. Open the resulting live URL, make a prediction and check that it opens in a private browser window.
6. Save that actual URL for submission. Do not submit localhost:8501.
Official guide: https://docs.streamlit.io/deploy/streamlit-community-cloud/deploy-your-app/deploy

## 7. Record the required 60-second video
Use Windows Snipping Tool screen recording or another screen recorder. Record the real running app and save/export as `module8b_demo_carol_namutenda.mp4`. Aim for exactly 60 seconds and check playback.
- 0–10 sec: “My name is Carol Namutenda. This is my Module 8B Diabetes Progression Explorer, built using Python and Streamlit.” Show the live app URL.
- 10–25 sec: “The model uses ten baseline health measurements.” Show and explain the ten input boxes.
- 25–40 sec: Choose Example 1. Click Predict progression and show the numeric score. Explain that it is an educational estimate, not a diagnosis.
- 40–50 sec: Show the probabilities and model evaluation section. Explain that training and test data were separated.
- 50–60 sec: “The code, saved model and Docker configuration are in my public GitHub repository.” Show that repository briefly.

## 8. Submit
Submit the actual public GitHub repository link, the actual live Streamlit app link and the MP4 video on the assignment page. The instructions also ask you to share these with the module facilitator. The ZIP is a working project package; it does not replace these three required submission items.

## Troubleshooting
- ModuleNotFoundError: run the pip command above using the same .venv Python.
- Model compatibility error: install requirements exactly; if needed run `.\.venv\Scripts\python.exe train_model.py`, then restart and upload the new model.pkl and metrics.json together.
- Port already in use: stop the earlier app/Docker instance or add `--server.port 8502` to the local Streamlit command and open the displayed URL.
- Cloud installation error: check the build log, Python 3.12 and root requirements.txt.

```batch
@echo off
:menu
cls
echo ======================================================
echo   QSAR Solubility Project Automation Tool (Windows)   
echo ======================================================
echo  1. Run Full Training Pipeline (main.py)
echo  2. Run CLI Inference Example (predict.py - Aspirin)
echo  3. Launch Streamlit Interactive Web App (app.py)
echo  4. Run Unit Tests (pytest)
echo  5. Exit
echo ======================================================
set /p choice="Enter your choice (1-5): "

if "%choice%"=="1" goto train
if "%choice%"=="2" goto predict
if "%choice%"=="3" goto streamlit
if "%choice%"=="4" goto test
if "%choice%"=="5" goto exit
goto menu

:train
echo.
echo [EXEC] Running training pipeline...
python main.py
echo.
pause
goto menu

:predict
echo.
echo [EXEC] Predicting solubility for Aspirin (CC(=O)Oc1ccccc1C(=O)O)...
python predict.py --smiles "CC(=O)Oc1ccccc1C(=O)O"
echo.
pause
goto menu

:streamlit
echo.
echo [EXEC] Launching Streamlit dashboard...
python -m streamlit run app.py
echo.
pause
goto menu

:test
echo.
echo [EXEC] Running test suite with pytest...
pytest
echo.
pause
goto menu

:exit
echo Goodbye!
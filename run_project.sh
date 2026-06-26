#!/bin/bash
show_menu() {
    clear
    echo "======================================================"
    echo "   QSAR Solubility Project Automation Tool (Linux/Mac)  "
    echo "======================================================"
    echo "1. Run Full Training Pipeline (main.py)"
    echo "2. Run CLI Inference Example (predict.py - Aspirin)"
    echo "3. Launch Streamlit Interactive Web App (app.py)"
    echo "4. Run Unit Tests (pytest)"
    echo "5. Exit"
    echo "======================================================"
    echo -n "Enter your choice (1-5): "
}

while true; do
    show_menu
    read choice
    case $choice in
        1)
            echo -e "\n[EXEC] Running training pipeline..."
            python3 main.py
            echo ""
            read -p "Press [Enter] to return to menu..."
            ;;
        2)
            echo -e "\n[EXEC] Predicting solubility for Aspirin..."
            python3 predict.py --smiles "CC(=O)Oc1ccccc1C(=O)O"
            echo ""
            read -p "Press [Enter] to return to menu..."
            ;;
        3)
            echo -e "\n[EXEC] Launching Streamlit dashboard..."
            python3 -m streamlit run app.py
            echo ""
            read -p "Press [Enter] to return to menu..."
            ;;
        4)
            echo -e "\n[EXEC] Running test suite with pytest..."
            pytest
            echo ""
            read -p "Press [Enter] to return to menu..."
            ;;
        5)
            echo "Goodbye!"
            exit 0
            ;;
        *)
            echo "Invalid choice. Please pick 1-5."
            sleep 1
            ;;
    esac
done
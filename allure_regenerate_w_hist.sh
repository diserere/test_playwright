#!/usr/bin/env bash

# Script to regenerate allure report with history
# - copy allure history dir from last report to raw allure results dir if found
# - generates new report
# - opens it with fixed port
# 
# Usage: ./allure_regenerate_w_hist.sh

unset GTK_PATH

ALLURE_HISTORY_DIR=./allure-report/history/
ALLURE_RESULTS_DIR=./allure-results/

if [ -e "${ALLURE_HISTORY_DIR}" -a -e "${ALLURE_RESULTS_DIR}" ]
    then 
        echo "[ INFO ] ${0}: Copying allure history ${ALLURE_HISTORY_DIR} to ${ALLURE_RESULTS_DIR}"
        cp -r ${ALLURE_HISTORY_DIR} ${ALLURE_RESULTS_DIR}
    else
        echo "[ WARNING ] ${0}: !!! Error copying allure history ${ALLURE_HISTORY_DIR} to ${ALLURE_RESULTS_DIR}"
        ls  ${ALLURE_HISTORY_DIR} > /dev/null
        ls  ${ALLURE_RESULTS_DIR} > /dev/null
fi

echo "[ INFO ] ${0}: Regenerating allure report with history"
allure generate -c && allure open -p 11123